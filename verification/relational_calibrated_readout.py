"""Calibrated field-readout dynamics plus a separate finite quantum instrument.

The field simulation is linear in field amplitudes on an exactly backreacting
homogeneous reference-field FLRW background; it is NOT full quantum gravity.
The finite instrument is a qubit model, not a quantization of these fields.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import sqrt
import json
from relational_memory_pulse import bump_prime, I, product_w

TAU=1.5
F_ROD=.5
T1=.4
R0=.42
R1=.62
FINAL=.8


def run(n,steps,lam,g,signal=1,reference=1):
    count=n+1
    P=3; V=P+count; C=V+count; D=C+count; B=D+count; E=B+count
    size=E+count
    y=[0.0]*size; y[0]=1.; y[1]=1.; y[P+1]=float(signal)
    def rhs(t,y):
        a,ref,refdot=y[:3]
        freq=a**4/TAU**2
        pulse1=0.; pulse2=0.
        if 0<t<T1:
            assert ref>.1
            pulse1=-2*TAU**2*bump_prime(t/T1)/(I*T1**2*a**6*ref)
        if R0<t<R1:
            pulse2=-TAU**2*bump_prime((t-R0)/(R1-R0))/(I*(R1-R0)**2*a**6)
        wphi=product_w(y[P:P+count],n,True)
        wchi=product_w(y[C:C+count],n,True)
        first=lam*a**6*pulse1/TAU**2
        second=g*reference*a**6*pulse2/TAU**2
        o=[0.0]*size
        o[0]=a**3/TAU*sqrt(F_ROD**2/4+TAU**2/(12*a**4))
        o[1]=refdot; o[2]=-freq*ref
        for k in range(count):
            o[P+k]=y[V+k]; o[V+k]=-freq*k*k*y[P+k]-first*wchi[k]
            o[C+k]=y[D+k]; o[D+k]=-freq*k*k*y[C+k]-first*wphi[k]-second*y[B+k]
            o[B+k]=y[E+k]; o[E+k]=-freq*k*k*y[B+k]-second*y[C+k]
        return o
    h=FINAL/steps; out={}
    points={round(steps*t/FINAL):t for t in [.4,.42,.62,.7,.8]}
    for i in range(steps):
        t=i*h
        k1=rhs(t,y)
        k2=rhs(t+h/2,[a+h*b/2 for a,b in zip(y,k1)])
        k3=rhs(t+h/2,[a+h*b/2 for a,b in zip(y,k2)])
        k4=rhs(t+h,[a+h*b for a,b in zip(y,k3)])
        y=[a+h*(b+2*c+2*d+e)/6 for a,b,c,d,e in zip(y,k1,k2,k3,k4)]
        if i+1 in points:
            out[str(points[i+1])]={'detector_mean':y[C], 'readout_mean':y[B],
                                  'readout_clock_slope':y[E], 'scale':y[0]}
    return out


def madd(a,b): return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def mscale(a,z): return [[z*x for x in row] for row in a]
def mmul(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0))
                         for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a): return [list(row) for row in zip(*a)]
def kron(a,b): return [[x*y for x in rowa for y in rowb] for rowa in a for rowb in b]
def identity(n): return [[Q(int(i==j)) for j in range(n)] for i in range(n)]

def instrument(r,q):
    # Explicit rational 16x16 density-matrix check: signal, reference, two
    # memory qubits; diagonal parity twirl, controlled two-bit write, noise.
    X=[[Q(0),Q(1)],[Q(1),Q(0)]]; Z=[[Q(1),Q(0)],[Q(0),Q(-1)]]
    I2=identity(2); I4=identity(4); I16=identity(16)
    xx=kron(X,X); parity=kron(Z,Z)
    plus=mscale(madd(I4,xx),Q(1,2)); minus=mscale(madd(I4,mscale(xx,-1)),Q(1,2))
    gate=madd(kron(plus,I4),kron(minus,kron(X,X)))
    assert mmul(gate,transpose(gate))==I16
    p0=[[Q(1),Q(0)],[Q(0),Q(0)]]; mem=kron(p0,p0)
    output={}
    for s in (1,-1):
        signal=mscale(madd(I2,mscale(X,s)),Q(1,2))
        reference=mscale(madd(I2,mscale(X,r)),Q(1,2))
        raw=kron(signal,reference)
        state=mscale(madd(raw,mmul(mmul(parity,raw),parity)),Q(1,2))
        assert state==mscale(madd(I4,mscale(xx,s*r)),Q(1,4))
        after=mmul(mmul(gate,kron(state,mem)),transpose(gate))
        ideal=[sum((after[4*i+m][4*i+m] for i in range(4)),Q(0)) for m in range(4)]
        row={}
        for a in (0,1):
            for b in (0,1):
                prob=Q(0)
                for m,p in enumerate(ideal):
                    errors=(a^(m//2))+(b^(m%2))
                    prob+=p*q**errors*(1-q)**(2-errors)
                k=a+b
                expected=(1+s*r)/2*(1-q)**(2-k)*q**k+(1-s*r)/2*q**(2-k)*(1-q)**k
                assert prob==expected
                row[f'{a}{b}']=prob
        assert sum(row.values())==1
        output[str(s)]=row
    distinguishability=sum(abs(output['1'][key]-output['-1'][key]) for key in output['1'])/2
    assert distinguishability==abs(r)*(1-2*q)
    return output,distinguishability,(1+distinguishability)/2


def main():
    # Potential monomials in (Phi,chi,D,R); both independent sign changes
    # preserve every monomial. Kinetic terms are each separately even.
    monomials=[(1,1,0,0),(0,1,1,1),(4,0,0,0),(0,4,0,0),
               (0,0,4,0),(2,2,0,0),(2,0,2,0),(0,2,2,0),(0,0,0,4),(0,0,0,2)]
    for phi,chi,d,ref in monomials:
        assert (phi+chi+d)%2==0 and (ref+d)%2==0
    lam=g=.01
    main=run(10,3200,lam,g)
    coarse=run(7,1600,lam,g)
    negative_signal=run(7,1600,lam,g,signal=-1)
    negative_reference=run(7,1600,lam,g,reference=-1)
    both_negative=run(7,1600,lam,g,signal=-1,reference=-1)
    missing=run(7,1600,lam,0)
    half=run(10,3200,lam/2,g/2)
    for t in main:
        a=coarse[t]['readout_mean']
        assert abs(main[t]['readout_mean']-a)<1e-8
        assert abs(negative_signal[t]['readout_mean']+a)<1e-14
        assert abs(negative_reference[t]['readout_mean']+a)<1e-14
        assert abs(both_negative[t]['readout_mean']-a)<1e-14
        assert missing[t]['readout_mean']==0
    assert abs(main['0.62']['readout_mean']/(lam*g)-1)<.01
    assert abs(main['0.62']['readout_mean']/half['0.62']['readout_mean']-4)<.01
    rows,dist,success=instrument(Q(3,5),Q(1,10))
    no_reference,dist0,_=instrument(Q(0),Q(1,10))
    assert dist0==0
    serial_rows={s:{k:str(v) for k,v in row.items()} for s,row in rows.items()}
    result={'status':'passed','scope':'linear-amplitude classical fields on reference FLRW background, plus a distinct abstract two-qubit instrument',
            'parameters':{'lambda':lam,'g':g,'reference_amplitude':1,'n':10,'steps':3200,'readout_window':[R0,R1]},
            'field_evolution':main,'joint_sign_and_reference_flip_control':'unchanged',
            'single_sign_flip_control':'changes sign','zero_readout_coupling_control':'zero',
            'readout_ratio_halving_both_couplings':main['0.62']['readout_mean']/half['0.62']['readout_mean'],
            'coarse_difference_t0_8':main['0.8']['readout_mean']-coarse['0.8']['readout_mean'],
            'abstract_instrument':{'reference_polarization':'3/5','independent_memory_flip_probability':'1/10',
                'joint_probabilities':serial_rows,'total_variation':str(dist),'optimal_equal_prior_success':str(success),
                'unpolarized_reference_total_variation':str(dist0),
                'interpretation':'This instrument is not derived by quantizing the field model.'}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
