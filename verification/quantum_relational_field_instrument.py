"""Gaussian quantum field readout with quantum Z2 reference, fixed FLRW background.

A finite cosine-Galerkin cutoff yields a self-adjoint time-dependent quadratic
Hamiltonian in each reference block. This code integrates its exact linear
symplectic equations with RK4. It does NOT quantize GR, the clock/rod fields,
or the classical scalar reference of the parent model.
"""
from math import erf, exp, sqrt, pi
from pathlib import Path
import json
from relational_memory_pulse import bump_prime, I

TAU=1.5; F_ROD=.5
T1=.4; R0=.42; R1=.62; FINAL=.8


def coupled(n,steps,lam,g,include_matrix=False):
    modes=n+1; fields=3*modes; dim=2*fields
    # Matrix rows are qPhi,qChi,qD,pPhi,pChi,pD; columns are initial operators.
    S=[[float(i==j) for j in range(dim)] for i in range(dim)]
    y=[1.,1.,0.] # scale factor, uncoupled normalized signal mode, its derivative
    def rhs(t,y,S):
        a,u,ud=y
        p1=p2=0.
        if 0<t<T1:
            assert u>.1
            p1=-2*TAU**2*bump_prime(t/T1)/(I*T1**2*a**6*u)
        if R0<t<R1:
            p2=-TAU**2*bump_prime((t-R0)/(R1-R0))/(I*(R1-R0)**2*a**6)
        # Hamiltonian in T: p²/(2 tau)+a^4 n² q²/(2 tau)
        # + a^6/(tau)*(lambda F1 qPhi W qChi + g F2 qChi qD).
        freq=a**4/TAU
        c1=lam*a**6*p1/TAU; c2=g*a**6*p2/TAU
        dy=[a**3/TAU*sqrt(F_ROD**2/4+TAU**2/(12*a**4)),ud,-a**4/TAU**2*u]
        out=[[0.]*dim for _ in range(dim)]
        for i in range(fields):
            out[i]=[v/TAU for v in S[fields+i]]
        for k in range(modes):
            pp=k; cc=modes+k; dd=2*modes+k
            # W=1+cos z in orthonormal real modes e0=1, en=sqrt(2)cos(nz).
            def wrow(offset):
                rows=[(1.,S[offset+k])]
                if k>0: rows.append(((1/sqrt(2)) if k==1 else .5,S[offset+k-1]))
                if k<n: rows.append(((1/sqrt(2)) if k==0 else .5,S[offset+k+1]))
                return [sum(w*row[j] for w,row in rows) for j in range(dim)]
            wc=wrow(modes); wp=wrow(0)
            out[fields+pp]=[-freq*k*k*S[pp][j]-c1*wc[j] for j in range(dim)]
            out[fields+cc]=[-freq*k*k*S[cc][j]-c1*wp[j]-c2*S[dd][j] for j in range(dim)]
            out[fields+dd]=[-freq*k*k*S[dd][j]-c2*S[cc][j] for j in range(dim)]
        return dy,out
    def advance(y,S,k,dt):
        dy,dS=k
        return ([v+dt*dv for v,dv in zip(y,dy)],
                [[v+dt*dv for v,dv in zip(row,drow)] for row,drow in zip(S,dS)])
    h=FINAL/steps
    for i in range(steps):
        t=i*h; k1=rhs(t,y,S)
        k2=rhs(t+h/2,*advance(y,S,k1,h/2))
        k3=rhs(t+h/2,*advance(y,S,k2,h/2))
        k4=rhs(t+h,*advance(y,S,k3,h))
        y=[v+h*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(y,k1[0],k2[0],k3[0],k4[0])]
        S=[[v+h*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(row,r1,r2,r3,r4)]
            for row,r1,r2,r3,r4 in zip(S,k1[1],k2[1],k3[1],k4[1])]
    # Measure symplectic defect max|S^T J S - J|, J=[[0,I],[-I,0]].
    defect=0.
    for i in range(dim):
        for j in range(dim):
            x=sum(S[k][i]*S[fields+k][j]-S[fields+k][i]*S[k][j] for k in range(fields))
            wanted=(1. if i<fields and j==fields+i else -1. if j<fields and i==fields+j else 0.)
            defect=max(defect,abs(x-wanted))
    assert defect < 1e-8,defect
    # Initial independent pure Gaussians: n>0 oscillator vacua; n=0
    # normalizable squeezed-free-particle Gaussian, Var q=1, Var p=1/4.
    variance=[]
    for field in range(3):
        for k in range(modes): variance.append(1. if k==0 else 1/(2*k))
    for field in range(3):
        for k in range(modes): variance.append(.25 if k==0 else k/2)
    row=S[2*modes] # q_D,0
    var=sum(z*z*v for z,v in zip(row,variance))
    transfer=row[1] # unit displacement of q_Phi,1
    q_index=2*modes; p_index=fields+q_index
    q_coefficient=row[q_index]; p_coefficient=row[p_index]
    remaining=var-q_coefficient**2*variance[q_index]-p_coefficient**2*variance[p_index]
    assert remaining >= -1e-12,remaining
    result={'nmax':n,'steps':steps,'scale':y[0],'transfer':transfer,'variance':var,
            'readout_q_coefficient':q_coefficient,'readout_p_coefficient':p_coefficient,
            'other_mode_variance':max(0.,remaining), 'symplectic_defect':defect}
    if include_matrix: result['matrix']=S
    return result


def statistics(transfer,var,amplitude,r,q):
    # Threshold q_D,0>=0 writes bit 0. Input displacement +s amplitude;
    # reference Z=+/- with probabilities (1+/-r)/2. Negative reference block
    # reverses the mean, but not the variance, by Gaussian parity covariance.
    d=r*erf(abs(transfer)*amplitude/sqrt(2*var))
    probs={}
    for s in (1,-1):
        p0=(1+s*d)/2
        probs[str(s)]={f'{a}{b}':p0*(1-q)**(2-a-b)*q**(a+b)+(1-p0)*q**(2-a-b)*(1-q)**(a+b) for a in (0,1) for b in (0,1)}
        assert abs(sum(probs[str(s)].values())-1)<1e-14
    tv=sum(abs(probs['1'][k]-probs['-1'][k]) for k in probs['1'])/2
    assert abs(tv-d*(1-2*q))<1e-14
    return {'amplitude':amplitude,'reference_polarization':r,'memory_flip_probability':q,
            'single_readout_contrast':d,'probabilities':probs,'total_variation':tv,'success':(1+tv)/2}


def main():
    fine=coupled(4,1600,.01,.01)
    coarse=coupled(3,800,.01,.01)
    zero=coupled(3,800,.01,0.)
    assert abs(fine['transfer']-coarse['transfer'])<1e-8
    assert abs(fine['variance']-coarse['variance'])<1e-8
    assert abs(fine['transfer']/(sqrt(2)*.01*.01)-1)<.001
    assert zero['transfer']==0.
    realistic=statistics(fine['transfer'],fine['variance'],1.,.6,.1)
    perfect=statistics(fine['transfer'],fine['variance'],1.,1.,0.)
    no_ref=statistics(fine['transfer'],fine['variance'],1.,0.,.1)
    assert no_ref['total_variation']==0
    # Fixed-background extrapolation only: amplitude needed for 70% success.
    # Its quadratic signal energy is compared with bare homogeneous clock/rod
    # energy on the torus. This ratio is NOT an Einstein-equation error bound.
    lo=0.; hi=1.
    while statistics(fine['transfer'],fine['variance'],hi,.6,.1)['success']<.7: hi*=2
    for _ in range(80):
        mid=(lo+hi)/2
        if statistics(fine['transfer'],fine['variance'],mid,.6,.1)['success']<.7: lo=mid
        else: hi=mid
    required=hi
    background_energy=((3*F_ROD**2+TAU**2)/2)*(2*pi)**3
    # On initial a=1 slice, signal coherent displacement in n=1 has E=A²/2.
    result={'status':'passed','scope':'quantum cutoff field Hamiltonian on classical FLRW; separate ideal reference qubit and memories; not constrained quantum gravity',
            'fine':fine,'coarse':coarse,'g_zero':zero,
            'signal_amplitude_1_reference_0_6_noise_0_1':realistic,
            'ideal_reference_and_memories':perfect,'unpolarized_reference':no_ref,
            'initial_signal_plus_reference_helstrom_bound':{
                'trace_distance':.6*sqrt(1-exp(-2)),
                'maximum_success_before_memory_noise':(1+.6*sqrt(1-exp(-2)))/2,
                'note':'Benchmark for the stipulated Gaussian preparations and reference qubit; not a proven local gravitational measurement.'},
            'fixed_background_extrapolation_to_70_percent':{'amplitude':required,
                'initial_signal_coherent_energy':required**2/2,
                'initial_clock_rod_classical_energy':background_energy,
                'signal_to_background_energy_ratio':(required**2/2)/background_energy,
                'warning':'Bare energy ratio at cutoff; neither a backreaction estimate nor a valid self-consistent strong-signal calculation.'},
            'limitations':'fixed clock/rod background; ideal QND reference qubit; pointer Gaussian and classical noise supplied; no nonlinear gravity or field-reference embedding.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
