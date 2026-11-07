"""Semibounded autonomous stop clock: exact step scattering and timing bounds.

Analytic completeness/error proofs are in AUTONOMOUS_STOP_CLOCK.md. Standard
library quadrature checks exact moment integrals, not an empirical arrival law.
"""
import json
import math
from pathlib import Path

CVAR=1/3-2/math.pi**2


def scattering(e,eps):
    assert e>0 and eps>=0
    # Stable ratios avoid subtraction of nearly equal square roots.
    ratio=math.sqrt(1+eps/e)
    r=-(eps/e)/(1+ratio)**2
    t=2*math.sqrt(ratio)/(1+ratio)
    assert abs(r*r+t*t-1)<1e-14
    return r,t


def resources(lam):
    assert lam>=2
    m,M=lam**6,lam**2
    return dict(scale=lam,m=m,M=M,e0=m/2,band=lam**4/4,
                k0=lam**2,kband=lam,distance=1)


def bounds(c,radius=.1):
    m,M,e0,band,k0,kband,d=[c[k] for k in ('m','M','e0','band','k0','kband','distance')]
    emin,emax=e0-band,e0+band
    kmax=k0+kband
    epsmax=kmax*kmax/(2*M)
    r,_=scattering(emin,epsmax);rho=abs(r)
    pmin=math.sqrt(2*m*emin)
    interface=math.sqrt(2)*rho
    envelope=epsmax*math.pi/(2*band)
    curvature=d*m*m*epsmax*epsmax/(2*pmin**3)
    delta=interface+envelope+curvature
    t0=d*math.sqrt(m/(2*e0))
    tmin,tmax=d*math.sqrt(m/(2*emax)),d*math.sqrt(m/(2*emin))
    jitter=max(tmax-t0,t0-tmin)
    ideal_mse=(M*math.pi/(2*k0*kband))**2+CVAR*kband*kband/(k0*k0)*tmax*tmax+jitter*jitter
    derivative=(M/k0*math.pi/(2*kband)+kmax/k0*(math.pi/(2*band)+rho/(4*emin)))
    actual_mse=derivative**2+(kband/k0*tmax+jitter)**2
    return dict(c,minimum_clock_energy=emin,maximum_clock_energy=emax,
                pointer_energy_maximum=epsmax,nominal_time=t0,
                ideal_time_minimum=tmin,ideal_time_maximum=tmax,
                reflection_probability_bound=rho*rho,
                interface_vector_bound=interface,envelope_vector_bound=envelope,
                phase_curvature_vector_bound=curvature,
                full_outgoing_trace_distance_bound=min(1,delta),
                ideal_time_mse_bound=ideal_mse,
                actual_unnormalized_click_time_mse_bound=actual_mse,
                conditional_click_time_mse_bound=actual_mse/(1-rho*rho),
                timing_radius=radius,
                failure_or_bad_time_bound_via_reference=min(1,delta+ideal_mse/radius**2),
                failure_or_bad_time_bound_direct=min(1,rho*rho+actual_mse/radius**2))


def moment_integrals(c,n):
    """Transmission probability and unnormalized actual pointer-time moments.

    Integrate in e,k, but differentiate amplitudes at FIXED OUTGOING E=e+eps.
    Unit coordinates u=(e-e0)/band,w=(k-k0)/kband keep quadrature conditioned.
    """
    m,M,e0,band,k0,kband,d=[c[k] for k in ('m','M','e0','band','k0','kband','distance')]
    t0=d*math.sqrt(m/(2*e0))
    prob=reflection=mean=second=0.0
    ideal_mse=0.0
    for i in range(n):
        u=-1+(i+.5)*2/n
        e=e0+band*u
        ca,sa=math.cos(math.pi*u/2),math.sin(math.pi*u/2)
        a=ca/math.sqrt(band);ap=-math.pi/(2*band**1.5)*sa
        tau=d*math.sqrt(m/(2*e))
        for j in range(n):
            w=-1+(j+.5)*2/n;k=k0+kband*w
            cg,sg=math.cos(math.pi*w/2),math.sin(math.pi*w/2)
            g=cg/math.sqrt(kband);gp=-math.pi/(2*kband**1.5)*sg
            eps=k*k/(2*M);E=e+eps
            r,t=scattering(e,eps)
            amp=t*a*g
            # d log(T)/de at fixed E equals |r|/(4e).
            te=t*abs(r)/(4*e)
            damp=t*a*gp-k/M*(te*a+t*ap)*g
            weight=4*band*kband/(n*n)
            prob+=amp*amp*weight
            reflection+=r*r*a*a*g*g*weight
            ymean=k/M*tau
            mean+=amp*amp*ymean*weight
            second+=(damp*damp+amp*amp*ymean*ymean)*weight
            ideal_mse+=ca*ca*cg*cg*4/(n*n)*((M*math.pi/(2*k0*kband))**2
                       +tau*tau*CVAR*kband*kband/(k0*k0)+(tau-t0)**2)
    time_mean=M/k0*mean/prob
    # Derived exact moment formula, not an inference from trace distance.
    time_mse=(M/k0)**2*second-2*t0*(M/k0)*mean+t0*t0*prob
    assert abs(prob+reflection-1)<1e-10
    return dict(transmission_probability=prob,reflection_probability=reflection,
                conditional_mean_time=time_mean,
                unnormalized_click_time_mse=time_mse,
                conditional_click_time_mse=time_mse/prob,
                ideal_time_mse_quadrature=ideal_mse)


def run():
    # Boundary/flux solve at the step, independently of the normalized formula.
    matches=0
    for m,e,eps in [(m,e,z) for m in (1,7) for e in (.1,.3,1,2,20,100) for z in (0,.01,1,100)]:
        p,q=math.sqrt(2*m*e),math.sqrt(2*m*(e+eps))
        r,t=scattering(e,eps)
        plane_t=t*math.sqrt(p/q)
        assert abs(1+r-plane_t)<1e-12
        assert abs(p*(1-r)-q*plane_t)<1e-12
        assert abs(r*r+q/p*plane_t**2-1)<1e-12
        matches+=1
    cases=[]
    for lam in (10,30,100,1000):
        c=resources(lam);b=bounds(c)
        coarse,fine=moment_integrals(c,64),moment_integrals(c,128)
        assert fine['reflection_probability']<=b['reflection_probability_bound']*(1+1e-8)+1e-20
        assert fine['unnormalized_click_time_mse']<=b['actual_unnormalized_click_time_mse_bound']+1e-10
        assert fine['ideal_time_mse_quadrature']<=b['ideal_time_mse_bound']+1e-12
        discrepancy=max(abs(fine[k]-coarse[k]) for k in fine)
        assert discrepancy<1e-6
        cases.append(dict(analytic=b,moments_128=fine,quadrature_64_128_max_difference=discrepancy))
    assert cases[2]['analytic']['full_outgoing_trace_distance_bound']<.000334
    assert cases[3]['analytic']['failure_or_bad_time_bound_via_reference']<.000264
    # Pure joint energy shifts are retained. Correct physical outgoing energy is
    # E=e+eps because H_pointer,right=0; no trace over incoming total energy as
    # if the pointer retained its former free Hamiltonian is performed.
    return dict(status='passed',independent_boundary_flux_matches=matches,cases=cases,
                scope=['Exact two-channel step instrument, including reflected no-click branch.',
                       'Pointer coordinate is frozen in the outgoing free channel; asymptotic outcome statistics need no readout epoch.',
                       'Operational stopped/dwell clock, not a universal exact quantum first-entry POVM.',
                       'Analytic bounds and floating moment checks; no interval certificate, PDE simulation or experimental calibration.',
                       'Separate model from the finite registration tape; combined device not yet derived.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: autonomous stop-clock scattering, complete click/no-click instrument and timing bounds')
    print(path)
