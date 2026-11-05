"""Finite-mass clock scattering detector. Analytic bound is derived in the report.

Floating-point witnesses and quadrature convergence checks are not formal interval
certification. The Hamiltonian and scattering amplitudes are explicitly supplied.
"""
import cmath
import json
import math
from pathlib import Path


def scattering(p,m,g,length,b):
    assert p>0 and m>0 and g>=0 and p*p>2*m*g and length>0 and abs(b)<=1
    k=math.sqrt(p*p-2*m*g*b)
    c,s=math.cos(k*length),math.sin(k*length)
    D=c-1j*(p*p+k*k)/(2*p*k)*s
    t=cmath.exp(-1j*p*length)/D
    r=-1j*(p*p-k*k)/(2*p*k)*s/D
    return t,r


def boundary_matching(p,m,g,length,b):
    """Independent linear solve imposing psi and psi' continuity at both edges."""
    k=math.sqrt(p*p-2*m*g*b)
    c,s=math.cos(k*length),math.sin(k*length)
    u0,u1=c+1j*p*s/k,c-1j*p*s/k
    v0,v1=-k*s+1j*p*c,-k*s-1j*p*c
    r=(1j*p*u0-v0)/(v1-1j*p*u1)
    t=cmath.exp(-1j*p*length)*(u0+u1*r)
    return t,r


def bounds(m,g,length,p0,spread,edge_error=0):
    pmin=p0-spread
    assert 0<spread<p0 and 0<=edge_error<length and 2*m*g<pmin*pmin
    delta=2*m*g/(pmin*pmin)
    s=math.sqrt(1-delta)
    alpha=delta*delta/(2*s*(1+s)**2)
    beta=(length+edge_error)*m*m*g*g/(2*pmin**3*(1-delta)**1.5)
    bandwidth=g*m*length*spread/(pmin*p0)
    calibration=g*m*edge_error/pmin
    reflection=min(1,delta*delta/(4*(1-delta)))
    transmission=alpha+beta+bandwidth+calibration
    vector=math.sqrt(transmission**2+reflection)
    return {'delta_max':delta,'impedance_amplitude_bound':alpha,
            'phase_curvature_bound':beta,'momentum_spread_phase_bound':bandwidth,
            'spatial_calibration_phase_bound':calibration,
            'reflection_probability_bound':reflection,
            'transmitted_operator_error_bound':transmission,
            'outgoing_vector_error_bound':vector,
            'any_event_probability_error_bound':min(1,vector),
            'wrong_pointer_or_reflection_bound_for_system_1':min(1,vector**2)}


def simpson(fn,a,b,n):
    assert n%2==0
    h=(b-a)/n
    total=fn(a)+fn(b)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*fn(a+j*h)
    return total*h/3


def packet_result(m,g,length,p0,spread,n=1024,actual_length=None):
    L=length if actual_length is None else actual_length
    def weight(p):
        return math.cos(math.pi*(p-p0)/(2*spread))**2/spread
    def component(p,which):
        tp,rp=scattering(p,m,g,L,1)
        tm,rm=scattering(p,m,g,L,-1)
        if which=='reflection':
            return weight(p)*(abs(rp)**2+abs(rm)**2)/2
        if which=='wrong_transmitted_pointer':
            return weight(p)*abs((tp+tm)/2)**2
        if which=='amplitude':
            return weight(p)*1j*(tp-tm)/2
        if which=='normalization':
            return weight(p)
        raise ValueError(which)
    out={key:simpson(lambda p:component(p,key),p0-spread,p0+spread,n)
         for key in ('reflection','wrong_transmitted_pointer','amplitude','normalization')}
    amplitude=out.pop('amplitude')
    overlap=(1+amplitude)/2  # initial system |+>, detector |0>; ideal theta=pi/2
    out['plus_input_full_outgoing_trace_distance']=math.sqrt(max(0,1-abs(overlap)**2))
    out['wrong_pointer_or_reflection_system_1']=out['reflection']+out['wrong_transmitted_pointer']
    return out


def run():
    samples=0
    max_matching=0
    # Multiple strengths, geometries and all three eigenchannels; right incidence also retained.
    for m in (0.5,1,2):
        for g in (0.1,1,3):
            for length in (0.3,2,11):
                for p in (5,8,12):
                    for b in (-1,0,1):
                        t,r=scattering(p,m,g,length,b)
                        tt,rr=boundary_matching(p,m,g,length,b)
                        max_matching=max(max_matching,abs(t-tt),abs(r-rr))
                        assert abs(t-tt)<2e-12 and abs(r-rr)<2e-12
                        assert abs(abs(t)**2+abs(r)**2-1)<2e-12
                        r_right=r*cmath.exp(-2j*p*length)
                        assert abs(r.conjugate()*t+t.conjugate()*r_right)<2e-12
                        if b==0:
                            assert abs(t-1)<2e-12 and abs(r)<2e-12
                        samples+=1
    cases=[]
    for g,spread,edge_fraction in ((1,0.1,0),(0.1,0.1,0),(0.1,0.02,0),(0.1,0.1,0.01)):
        m,p0=1,10
        length=math.pi*p0/(2*m*g)
        ell=edge_fraction*length
        bound=bounds(m,g,length,p0,spread,ell)
        # Uniform bound witnesses include momentum-band endpoints and spatial calibration extremes.
        for actual_L in sorted({length-ell,length,length+ell}):
            for j in range(101):
                p=p0-spread+2*spread*j/100
                theta=g*m*length/p0
                for b in (-1,0,1):
                    t,r=scattering(p,m,g,actual_L,b)
                    ideal=cmath.exp(-1j*b*theta)
                    assert abs(t-ideal)<=bound['transmitted_operator_error_bound']+1e-11
                    assert abs(r)**2<=bound['reflection_probability_bound']+1e-11
                    assert abs(t-ideal)**2+abs(r)**2<=bound['outgoing_vector_error_bound']**2+1e-11
                # Pointer instrument completeness on system 1, with all exit directions retained.
                tp,rp=scattering(p,m,g,actual_L,1)
                tm,rm=scattering(p,m,g,actual_L,-1)
                ks=((tp+tm)/2,1j*(tp-tm)/2,(rp+rm)/2,1j*(rp-rm)/2)
                assert abs(sum(abs(k)**2 for k in ks)-1)<2e-12
        quadratures=[]
        for actual_L in sorted({length-ell,length,length+ell}):
            coarse=packet_result(m,g,length,p0,spread,512,actual_L)
            fine=packet_result(m,g,length,p0,spread,1024,actual_L)
            discrepancy=max(abs(fine[k]-coarse[k]) for k in fine)
            assert discrepancy<1e-8
            assert abs(fine['normalization']-1)<1e-10
            assert fine['plus_input_full_outgoing_trace_distance']<=bound['any_event_probability_error_bound']+1e-9
            assert fine['wrong_pointer_or_reflection_system_1']<=bound['wrong_pointer_or_reflection_bound_for_system_1']+1e-9
            quadratures.append({'actual_length':actual_L,'quadrature_512_1024_max_difference':discrepancy,**fine})
        weak_limit=simpson(lambda p: math.cos(math.pi*(p-p0)/(2*spread))**2/spread
                           *math.cos(math.pi*p0/(2*p))**2,p0-spread,p0+spread,1024)
        assert weak_limit>0
        var_p=simpson(lambda p: (p-p0)**2*math.cos(math.pi*(p-p0)/(2*spread))**2/spread,
                      p0-spread,p0+spread,1024)
        assert abs(var_p-spread**2*(1/3-2/math.pi**2))<1e-11
        cases.append({'mass':m,'p0':p0,'g':g,'momentum_half_band':spread,
                      'nominal_length':length,'length_calibration_half_band':ell,
                      'ideal_detector_angle':math.pi/2,
                      'nominal_length_weak_coupling_bandwidth_failure_limit_numerical':weak_limit,
                      'clock_mean_free_energy':(p0*p0+spread**2*(1/3-2/math.pi**2))/(2*m),
                      'packet_position_standard_deviation':math.pi/(2*spread),
                      'packet_momentum_standard_deviation':spread*math.sqrt(1/3-2/math.pi**2),
                      'uniform_analytic_bounds':bound,'packet_numerical_witnesses':quadratures})
    return {'status':'passed','units':'hbar=1','scalar_scattering_checks':samples,
            'max_independent_boundary_matching_discrepancy':max_matching,
            'hamiltonian':'P^2/(2m) + g 1_[0,L](X) (|1><1|_S tensor Y_D)',
            'free_system_and_detector_hamiltonians':'zero (degenerate baseline)',
            'detector_ready_state':'|0>_D','ideal_pointer_instrument':['P0','P1'],
            'clock_packet':'cos(pi*(p-p0)/(2*Delta))/sqrt(Delta), compact positive momentum band',
            'parameter_cases':cases,
            'interpretation':['analytic inequalities, not grid sampling, provide the uniform model bound',
                              'quadratures and boundary comparisons are floating-point witnesses, not interval certificates',
                              'preparation is an asymptotic incoming scattering state; bound states are excluded from that preparation, not from H',
                              'position description retains reflected orientation and flux; no single-branch first-order reduction is claimed',
                              'auxiliary T-constraint rigging and matched-event equivalence are derived analytically in the report',
                              'not calibrated to the released cold-atom images, and not a gravitational constraint model']}


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: Hamiltonian detector scattering, flux, full pointer instrument and uniform-bound witnesses')
    print(path)
