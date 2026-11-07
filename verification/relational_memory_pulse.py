"""Linear-response evolution of an explicitly clock-switched detector on a
backreacting clock/rod FLRW background. stdlib only; see report for scope.

Cosine-Galerkin modes in z and RK4 in the scalar clock T. This is NOT a
numerical solution of the full nonlinear Einstein-matter equations.
"""
from math import exp, sqrt
from fractions import Fraction
from pathlib import Path
import json

F_ROD=.5
TAU=1.5
END=.4
FINAL=.6


def bump(s):
    return exp(-1/(s*(1-s))) if 0<s<1 else 0.0

def bump_prime(s):
    if not 0<s<1: return 0.0
    return bump(s)*(1-2*s)/(s*s*(1-s)**2)

def normalization(n=4000):
    h=1/n
    return h/3*(bump(0)+bump(1)+sum((4 if i%2 else 2)*bump(i*h) for i in range(1,n)))
I=normalization()


def product_w(x,n,spatial):
    # W=1+cos z, or W=1. In cosine series x0 + sum x_n cos(nz).
    y=x.copy()
    if spatial:
        y[1]+=x[0]
        for k in range(1,n+1):
            y[k-1]+=x[k]/2
            if k<n: y[k+1]+=x[k]/2
    return y


def run(n,steps,lam,kind='balanced',spatial=True):
    # y=(scale, unperturbed signal, its clock derivative, signal modes,
    # signal derivatives, detector modes, detector derivatives).
    count=n+1
    P=3; V=P+count; C=V+count; D=C+count; size=D+count
    y=[0.0]*size; y[0]=1.0; y[1]=1.0; y[P+1]=1.0
    def rhs(t,y):
        a,ref,refdot=y[0:3]
        aa=a**4/TAU**2
        pulse=0.0
        if 0<t<END:
            q=t/END
            if kind=='balanced':
                assert ref>.1
                pulse=-2*TAU**2*bump_prime(q)/(I*END**2*a**6*ref)
            elif kind=='positive':
                pulse=bump(q)/I
            else: raise ValueError(kind)
        wphi=product_w(y[P:P+count],n,spatial)
        wchi=product_w(y[C:C+count],n,spatial)
        factor=lam*a**6*pulse/TAU**2
        o=[0.0]*size
        o[0]=a**3/TAU*sqrt(F_ROD**2/4+TAU**2/(12*a**4))
        o[1]=refdot; o[2]=-aa*ref
        for k in range(count):
            o[P+k]=y[V+k]; o[V+k]=-aa*k*k*y[P+k]-factor*wchi[k]
            o[C+k]=y[D+k]; o[D+k]=-aa*k*k*y[C+k]-factor*wphi[k]
        return o
    h=FINAL/steps
    observations={}
    checkpoints={round(steps*t/FINAL):t for t in [.4,.5,.6]}
    for i in range(steps):
        t=i*h
        k1=rhs(t,y)
        k2=rhs(t+h/2,[a+h*b/2 for a,b in zip(y,k1)])
        k3=rhs(t+h/2,[a+h*b/2 for a,b in zip(y,k2)])
        k4=rhs(t+h,[a+h*b for a,b in zip(y,k3)])
        y=[a+h*(b+2*c+2*d+e)/6 for a,b,c,d,e in zip(y,k1,k2,k3,k4)]
        j=i+1
        if j in checkpoints:
            observations[str(checkpoints[j])]={'scale_factor':y[0], 'reference_signal':y[1],
                'detector_zero_mode':y[C], 'detector_zero_mode_clock_slope':y[D],
                'detector_mode1':y[C+1]}
    return observations


def main():
    # Exact zero/second-harmonic constraints of the sign-symmetric p=0,
    # b=1 initial data: u=-cos(2z)/188, alpha0=-1, a=-1/12, L=15.
    Q=Fraction
    alpha0=Q(-1); correction=Q(-1,12); u2=Q(-1,188); L=Q(15)
    assert -3*alpha0*correction+Q(1,4)==0
    assert -(32+L)*u2-Q(1,4)==0
    lam=.01
    balanced=run(12,2400,lam)
    coarse=run(8,1200,lam)
    time_refined=run(8,2400,lam)
    modes_refined=run(12,1200,lam)
    zero=run(8,1200,0)
    uniform=run(8,1200,lam,spatial=False)
    small=run(12,2400,lam/2)
    positive=run(12,2400,lam,kind='positive')
    for t in balanced:
        assert abs(balanced[t]['detector_zero_mode']-coarse[t]['detector_zero_mode'])<1e-7
        assert zero[t]['detector_zero_mode']==0
        assert uniform[t]['detector_zero_mode']==0
    # At weak coupling the endpoint error and leftover drift scale cubically.
    err=balanced['0.4']['detector_zero_mode']-lam
    errhalf=small['0.4']['detector_zero_mode']-lam/2
    drift=balanced['0.4']['detector_zero_mode_clock_slope']
    drifthalf=small['0.4']['detector_zero_mode_clock_slope']
    assert abs(err/errhalf-8)<0.1,(err,errhalf)
    assert abs(drift/drifthalf-8)<0.1,(drift,drifthalf)
    assert abs(positive['0.4']['detector_zero_mode_clock_slope'])>abs(drift)
    result={'status':'passed','scope':'first-order field amplitude on exact homogeneous clock-and-rod FLRW background; coupled linear scalar fields, finite-mode RK4',
            'parameters':{'f':F_ROD,'tau':TAU,'pulse_end_clock':END,'end_clock':FINAL,'lambda':lam,'fourier_modes':12,'rk4_steps':2400},
            'bump_normalization':I,'balanced':balanced,'half_lambda':small,
            'unbalanced_positive_pulse':positive,'uniform_coupling_control':uniform,
            'endpoint_error_ratio_halving_lambda':err/errhalf,
            'post_pulse_slope_ratio_halving_lambda':drift/drifthalf,
            'coarse_endpoint_difference':balanced['0.6']['detector_zero_mode']-coarse['0.6']['detector_zero_mode'],
            'time_only_refinement_difference':time_refined['0.6']['detector_zero_mode']-coarse['0.6']['detector_zero_mode'],
            'mode_only_refinement_difference':modes_refined['0.6']['detector_zero_mode']-coarse['0.6']['detector_zero_mode'],
            'limitations':'No nonlinear inhomogeneous Einstein evolution, POVM, readout, noise or persistence theorem.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
