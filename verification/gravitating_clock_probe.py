"""Einstein-scalar plus a smeared comoving oscillator clock: Morse scattering.

Closed-form spectrum/scattering and proper-time response, with an explicit
Ramsey instrument. Standard library; no full inhomogeneous GR claim.
"""
import cmath
import json
import math
from pathlib import Path
if __package__:
    from .recollapsing_gravitational_clock import loggamma, reflection, mode_integral
else:
    from recollapsing_gravitational_clock import loggamma, reflection, mode_integral


def digamma(z):
    correction=0j
    while z.real<16:
        correction-=1/z;z+=1
    inv=1/z
    out=cmath.log(z)-inv/2
    for power,coeff in [(2,-1/12),(4,1/120),(6,-1/252),(8,1/240),(10,-1/132),(12,691/32760)]:
        out+=coeff*inv**power
    return out+correction


def log_s(k,kappa,mu=1):
    assert k>0 and mu>0
    a=.5-kappa
    return (loggamma(2j*k)-loggamma(-2j*k)+loggamma(a-1j*k)
            -loggamma(a+1j*k)-2j*k*math.log(2*mu))


def scatter(k,kappa,mu=1):return cmath.exp(log_s(k,kappa,mu))


def hyper(a,b,z):
    """1F1 and its first two derivatives by convergent power series."""
    term=1+0j;f=term;fp=fpp=0j
    for n in range(1,501):
        term*=((a+n-1)/(b+n-1))*z/n
        f+=term;fp+=n*term/z
        fpp+=n*(n-1)*term/(z*z)
        if n>20 and abs(term)<1e-17*max(1,abs(f)):return f,fp,fpp
    raise AssertionError('hypergeometric series did not converge')


def morse_mode(k,kappa,z):
    """z^-1/2 W_{kappa,ik}(z) and its second x derivative, x=ln(z/2mu)."""
    value=second=0j
    for sign in (1,-1):
        s=sign*1j*k
        coeff=cmath.exp(loggamma(-2*s)-loggamma(.5-kappa-s))
        f,fp,fpp=hyper(.5+s-kappa,1+2*s,z)
        u=cmath.exp(s*math.log(z)-z/2)
        d=s-z/2
        value+=coeff*u*f
        second+=coeff*u*((d*d-z/2)*f+(2*d+1)*z*fp+z*z*fpp)
    return value,second


def proper_duration(k,kappa,mu=1):
    return 4/(3*mu)*(math.pi/2+math.atan(kappa/k))


def quantum_response(k,kappa,mu=1):
    return 4/(3*mu)*digamma(.5-kappa+1j*k).imag


def bound_levels(kappa):
    return [-(kappa-n-.5)**2 for n in range(max(0,math.ceil(kappa-.5))) if n<kappa-.5]


def laguerre(n,alpha,z):
    vals=[0.,0.,0.]
    for j in range(n+1):
        c=(-1)**j*math.exp(math.lgamma(n+alpha+1)-math.lgamma(alpha+j+1)
                            -math.lgamma(n-j+1)-math.lgamma(j+1))
        vals[0]+=c*z**j
        if j:vals[1]+=j*c*z**(j-1)
        if j>1:vals[2]+=j*(j-1)*c*z**(j-2)
    return vals


def phase_lipschitz(kmin,kmax,kappa_max):
    # Digamma recurrence shifts all real parts positive; the remaining series
    # is bounded by a first term plus an integral. No sampled supremum used.
    j=max(0,math.ceil(kappa_max))
    amin=.5-kappa_max+j
    return 2*(kmax*(1/amin**2+1/amin)+j/kmin)


def run():
    classical=0
    for mu in (.7,1.3):
        for kap in (0,.2,.6,1.2):
            for k in (.5,1,3):
                for t in (-3,-1,0,1,3):
                    root=math.sqrt(k*k+kap*kap)
                    den=root*math.cosh(t)-kap
                    volume=k*k/(mu*den)
                    px=-k*root*math.sinh(t)/den
                    assert abs(k*k-px*px-mu*mu*volume**2+2*mu*kap*volume)<1e-11
                    classical+=1
                turn=(kap+math.sqrt(kap*kap+k*k))/mu
                assert turn>=k/mu
    ode=zero_probe=bound_ode=0
    for kap in (0,.2,.6,1.2):
        for k in (.5,1,2,4):
            for z in (.1,.5,2,5):
                f,fxx=morse_mode(k,kap,z)
                assert abs(-fxx+(z*z/4-kap*z)*f-k*k*f)<1e-9
                assert abs(f.imag)<1e-10
                assert abs(abs(scatter(k,kap))-1)<1e-12
                ode+=1
    for k in (.5,1,2,3):
        assert abs(scatter(k,0)-reflection(k,1))<1e-11
        for z in (.1,.5,2,5):
            f,_=morse_mode(k,0,z)
            assert abs(f-mode_integral(k,z/2)[0]/math.sqrt(math.pi))<1e-10
            zero_probe+=1
    for kap in (.6,1.2,2.3,3.1):
        for n,eigen in enumerate(bound_levels(kap)):
            s=kap-n-.5
            for z in (.1,1,3):
                f,fp,fpp=laguerre(n,2*s,z)
                u=z**s*math.exp(-z/2);d=s-z/2
                psi=u*f;psixx=u*((d*d-z/2)*f+(2*d+1)*z*fp+z*z*fpp)
                assert abs(-psixx+(z*z/4-kap*z)*psi-eigen*psi)<1e-9
                assert eigen<0
                bound_ode+=1
    response_checks=0
    for kap in (0,.2,.6,1.2):
        for k in (.5,2,10):
            h=1e-5
            # kappa=2E/(3mu): d phase/dE=(2/3mu)d phase/dkappa.
            fd=(log_s(k,kap+h).imag-log_s(k,kap-h).imag)/(2*h)*2/3
            assert abs(fd-quantum_response(k,kap))<1e-8
            response_checks+=1
    for k in (.2,.5,1,3,10):
        assert abs(quantum_response(k,0)-2*math.pi/3*math.tanh(math.pi*k))<1e-12
    classical_limits=[]
    for kap in (.2,.6,1.2):
        for k in (10,30,100):
            q=quantum_response(k,kap);c=proper_duration(k,kap)
            assert abs(q-c)<2/k**3
            classical_limits.append(dict(k=k,kappa=kap,quantum_response=q,classical_proper_duration=c))
    for scale in (10,30,100):
        # Nontrivial classical limit keeps kappa/k fixed, not only E fixed.
        assert abs(quantum_response(scale,.6*scale)-proper_duration(scale,.6*scale))<1/scale**2
    mu,omega=1,.6
    energies=[omega/2,3*omega/2]
    kappas=[2*e/(3*mu) for e in energies]
    probes=[]
    for k in (.4,.7,1,2,4,8):
        s0,s1=[scatter(k,kap,mu) for kap in kappas]
        plus,minus=(s0+s1)/2,(s0-s1)/2
        assert abs(abs(plus)**2+abs(minus)**2-1)<1e-12
        # Joint dressed readout projectors in the incoming continuum frame.
        eplus=[[sa.conjugate()*sb/2 for sb in (s0,s1)] for sa in (s0,s1)]
        eminus=[[complex(i==j)-eplus[i][j] for j in range(2)] for i in range(2)]
        for effect in (eplus,eminus):
            squared=[[sum(effect[i][l]*effect[l][j] for l in range(2)) for j in range(2)] for i in range(2)]
            assert max(abs(squared[i][j]-effect[i][j]) for i in range(2) for j in range(2))<1e-12
        probes.append(dict(k=k,probability_plus=abs(plus)**2,probability_minus=abs(minus)**2))
    assert max(x['probability_minus'] for x in probes)-min(x['probability_minus'] for x in probes)>.01
    # Geometry superposition of two spectral alternatives. This is an algebra
    # control; actual continuum packets can be placed in narrow disjoint bands.
    ka,kb=.7,2.3
    sa=[scatter(ka,kap) for kap in kappas];sb=[scatter(kb,kap) for kap in kappas]
    overlap=sum(a*b.conjugate() for a,b in zip(sa,sb))/2
    purity=(1+abs(overlap)**2)/2
    assert purity<.999
    # Trace detector versus summing the two outcome Kraus channels.
    ma=[(sa[0]+sa[1])/2,(sa[0]-sa[1])/2]
    mb=[(sb[0]+sb[1])/2,(sb[0]-sb[1])/2]
    assert abs(sum(a*b.conjugate() for a,b in zip(ma,mb))-overlap)<1e-12
    weak=[]
    for om in (.03,.01,.003,.001):
        kap0,kap1=om/3,om
        lip=phase_lipschitz(.4,8,kap1)
        signal_bound=min(1,((kap1-kap0)*lip)**2/4)
        actual=max(abs((scatter(k,kap0)-scatter(k,kap1))/2)**2 for k in (.4,.7,1,2,4,8))
        assert actual<=signal_bound+1e-12
        weak.append(dict(oscillator_frequency=om,analytic_minus_probability_bound=signal_bound,
                         sampled_minus_probability=actual))
    # A negative Morse eigenvalue is not an admissible scalar-frequency state:
    # p_T^2-(-s^2)=p_T^2+s^2 is strictly positive for all real p_T.
    excited_bound=bound_levels(kappas[1])
    assert len(excited_bound)==1 and abs(excited_bound[0]+.01)<1e-12
    return dict(status='passed',classical_backreacted_constraints=classical,
                whittaker_mode_ode_checks=ode,zero_probe_bessel_checks=zero_probe,
                negative_bound_mode_ode_checks=bound_ode,phase_response_checks=response_checks,
                detector_frequency=omega,detector_energies=energies,morse_parameters=kappas,
                detector_record_examples=probes,proper_time_classical_limit=classical_limits,
                ignored_detector_geometry_purity_witness=purity,
                weak_probe_examples=weak,excited_channel_negative_auxiliary_levels=excited_bound,
                scope=['Action-derived homogeneous comoving oscillator energy in the gravitational constraint.',
                       'Gravitational Ramsey/phase clock, not the old arrival/completion apparatus coupled by assertion.',
                       'Negative auxiliary bound modes removed by the real-spectrum constraint, not an unjustified square root.',
                       'Incoming-channel product preparation; finite-volume wavefunction is not assumed factorized.',
                       'No inhomogeneous refoliation, fully modelled preparation/readout engine, finite completion guarantee or singularity resolution.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: gravitating oscillator clock, Morse reflection, proper-time response and complete readout instrument')
    print(path)
