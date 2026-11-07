"""Einstein-scalar recollapse: classical constraint, KL modes, reflection, records.

Standard library checks. Continuum domains and KL transform are analytic in the
report; finite matrix controls test instrument identities, not KL discretization.
"""
import cmath
import json
import math
from pathlib import Path

COEFF=[.99999999999980993,676.5203681218851,-1259.1392167224028,
       771.32342877765313,-176.61502916214059,12.507343278686905,
       -.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7]


def loggamma(z):
    if z.real<.5:return loggamma(z+1)-cmath.log(z)
    w=z-1
    a=complex(COEFF[0])
    for j,c in enumerate(COEFF[1:],1):a+=c/(w+j)
    t=w+7.5
    return .5*math.log(2*math.pi)+(w+.5)*cmath.log(t)-t+cmath.log(a)


def log_reflection(k,mu):
    return loggamma(1j*k)-loggamma(-1j*k)-2j*k*math.log(mu/2)


def reflection(k,mu):return cmath.exp(log_reflection(k,mu))


def mode_integral(k,z,panels=4096):
    # K_ik(z), dK/dz and d2K/dz2 from their real integral representations.
    end=math.acosh(max(2,50/z))
    step=end/panels
    out=[0.,0.,0.]
    for j in range(panels+1):
        t=j*step;c=math.cosh(t)
        f=math.exp(-z*c)*math.cos(k*t)
        weight=1 if j in (0,panels) else (4 if j%2 else 2)
        for i,v in enumerate((f,-c*f,c*c*f)):out[i]+=weight*v*step/3
    return out


def frobenius(a):return math.sqrt(sum(abs(x)**2 for row in a for x in row))
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def adj(a):return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]
def diag(xs):return [[complex(xs[i]) if i==j else 0j for j in range(len(xs))] for i in range(len(xs))]
def vecmul(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def norm(v):return math.sqrt(sum(abs(x)**2 for x in v))


def run():
    classical=0
    for mu in (.4,1,3):
        for k in (.5,2,7):
            for t in (-5,-2,0,1,4):
                x=math.log(k/mu)-math.log(math.cosh(t))
                px=-k*math.tanh(t)
                assert abs(k*k-px*px-mu*mu*math.exp(2*x))<1e-12
                assert abs(-k/math.cosh(t)**2+mu*mu*math.exp(2*x)/k)<1e-12
                classical+=1
            b=math.log(k/mu)-1
            delta=math.acosh(k/(mu*math.exp(b)))
            for s in (-1,1):
                x=math.log(k/mu)-math.log(math.cosh(s*delta))
                assert abs(x-b)<1e-12
    gamma_checks=0
    for k in (.2,.5,1,2,5,10,30,100):
        lg=loggamma(1j*k)
        expected=math.log(math.pi)-math.log(k)-math.log(math.sinh(math.pi*k))
        assert abs(2*lg.real-expected)<1e-11
        assert abs(loggamma(1j*k+1)-lg-cmath.log(1j*k))<1e-11
        for mu in (.4,1,3):assert abs(abs(reflection(k,mu))-1)<1e-12
        gamma_checks+=1
    ode=0;asympt=0;worst=0.
    for k in (.5,1,2,3):
        for z in (.1,.3,1,3):
            f,fp,fpp=mode_integral(k,z)
            residual=z*z*fpp+z*fp+(k*k-z*z)*f
            assert abs(residual)<1e-11
            ode+=1
        z=.001
        exact=mode_integral(k,z)[0]
        plane=(cmath.exp(loggamma(1j*k)-1j*k*math.log(z/2))+
               cmath.exp(loggamma(-1j*k)+1j*k*math.log(z/2)))/2
        bound=abs(cmath.exp(loggamma(1j*k)))*math.expm1(z*z/4)
        assert abs(exact-plane)<=bound+1e-12
        worst=max(worst,abs(exact-plane));asympt+=1
    delays=[]
    for k in (10,30,100):
        h=1e-4
        phase_derivative=(log_reflection(k+h,1).imag-log_reflection(k-h,1).imag)/(2*h)
        classical_delay=2*math.log(2*k)
        assert abs(phase_derivative-classical_delay)<.2/(k*k)
        delays.append(dict(k=k,quantum_asymptotic_intercept_sum=phase_derivative,
                           classical_asymptotic_intercept_sum=classical_delay))
    # Finite spectral algebra control: NOT a unitary quadrature of KL modes.
    n=8;ks=[.5+.4*j for j in range(n)]
    s=diag([reflection(k,1) for k in ks])
    ft=[[cmath.exp(2j*math.pi*i*j/n)/math.sqrt(n) for j in range(n)] for i in range(n)]
    v=mul(ft,diag([cmath.exp(-.7j*k) for k in ks]))
    ident=diag([1]*n)
    assert frobenius([[x-y for x,y in zip(r,q)] for r,q in zip(mul(adj(v),v),ident)])<1e-12
    p=diag([j<n//2 for j in range(n)])
    q=mul(adj(ft),mul(p,ft))
    branches=[p,diag([j>=n//2 for j in range(n)])]
    second=[q,[[ident[i][j]-q[i][j] for j in range(n)] for i in range(n)]]
    a=[cmath.exp(.3j*j)*(j+1) for j in range(n)];scale=norm(a);a=[x/scale for x in a]
    branches_checked=0;bad_witness=0.
    eta=.02
    roots=[]
    for b1 in branches:
        for b2 in second:
            roots.append([[math.sqrt(1-eta)*x for x in row] for row in mul(b2,b1)])
    roots.append(diag([math.sqrt(eta)]*n)) # failure halts before second event
    for frame in (s,v,mul(v,adj(s))):
        af=vecmul(frame,a)
        total=0.
        for root in roots:
            anchored=mul(frame,mul(root,adj(frame)))
            correct=norm(vecmul(anchored,af))**2
            target=norm(vecmul(root,a))**2
            assert abs(correct-target)<1e-12
            total+=correct
            bad_witness=max(bad_witness,abs(norm(vecmul(root,af))**2-target))
            branches_checked+=1
        assert abs(total-1)<1e-12
        assert abs(norm(vecmul(roots[-1],af))**2-eta)<1e-12
    assert bad_witness>.01
    # Finite completion: retain a failure branch, no conditioning away errors.
    eta=.02
    ks_complete=[[[math.sqrt(1-eta)*x for x in row] for row in b] for b in branches]+[diag([math.sqrt(eta)]*n)]
    check=[[0j]*n for _ in range(n)]
    for b in ks_complete:
        term=mul(adj(b),b)
        check=[[x+y for x,y in zip(r,t)] for r,t in zip(check,term)]
    assert frobenius([[x-y for x,y in zip(r,t)] for r,t in zip(check,ident)])<1e-12
    # Rigging Jacobian versus a naive time-slice evaluation.
    raw=[complex(j+1,.2*j) for j in range(n)]
    physical=sum(abs(z)**2/(2*k) for z,k in zip(raw,ks))
    reduced=sum(abs(z/math.sqrt(2*k))**2 for z,k in zip(raw,ks))
    naive=sum(abs(z/(2*k))**2 for z,k in zip(raw,ks))
    assert abs(physical-reduced)<1e-12 and abs(physical-naive)>1
    return dict(status='passed',classical_constraint_checks=classical,
                gamma_modulus_and_recurrence_checks=gamma_checks,
                bessel_ode_checks=ode,small_volume_asymptotic_checks=asympt,
                largest_small_volume_mode_discrepancy=worst,
                asymptotic_phase_delay_examples=delays,
                completed_record_branch_transport_checks=branches_checked,
                untransported_event_probability_error_witness=bad_witness,
                complete_instrument_including_failure=True,
                rigging_jacobian_check=True,
                scope=['Actual flat FLRW Einstein-massless-scalar model with negative cosmological constant.',
                       'Declared densitization and factor ordering; one Hamiltonian constraint, no full refoliation algebra.',
                       'KL continuum identities/domains analytic; finite matrix controls are not KL discretization.',
                       'Completed instrument transport is exact passive representation, not a new gravity-coupled detector Hamiltonian.',
                       'No transplanted nongravitational detector error, singularity resolution or phenomenal constitution claim.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: recollapsing Einstein-scalar constraint, quantum reflection and completed-record transport')
    print(path)
