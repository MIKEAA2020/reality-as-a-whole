#!/usr/bin/env python3
"""Source-coupled gradient pointer: exact cancellation control.

The analytic gauge/canonical argument is in GRAVITY_GRADIENT_POINTER_GATE.md.
This script checks differential equations, a classical recollapse, and an
energy-matched Ramsey comparison numerically. It does not implement hardware.
"""
import cmath
import json
import math
from pathlib import Path

if __package__:
    from .gravitating_clock_probe import hyper, loggamma, scatter
    from .gravity_volume_clock_obstruction import simpson
else:
    from gravitating_clock_probe import hyper, loggamma, scatter
    from gravity_volume_clock_obstruction import simpson

M=1.3
OMEGA=.6
A=.8
L=1.


def bump(x):
    # G is a smooth step: g=G' is nonnegative and compactly supported.
    if x<=-L: return 0.
    if x>=L: return A
    t=(x+L)/(2*L)
    return A*(10*t**3-15*t**4+6*t**5)


def slope(x):
    if abs(x)>=L: return 0.
    t=(x+L)/(2*L)
    return A*30*t*t*(1-t)**2/(2*L)


def curvature(x):
    if abs(x)>=L: return 0.
    t=(x+L)/(2*L)
    return A*(60*t-180*t*t+120*t**3)/(4*L**2)


def kappa(n,p,mass=M):
    if n not in (0,1) or mass<=0: raise ValueError('invalid oscillator level or pointer mass')
    return 2/3*(OMEGA*(n+.5)+p*p/(2*mass))


def raw_mode(k,kap,x):
    z=2*math.exp(x)
    value=first=second=0j
    for sign in (1,-1):
        s=sign*1j*k
        coeff=cmath.exp(loggamma(-2*s)-loggamma(.5-kap-s))
        f,fp,fpp=hyper(.5+s-kap,1+2*s,z)
        u=cmath.exp(s*math.log(z)-z/2)
        d=s-z/2
        value+=coeff*u*f
        first+=coeff*u*(d*f+z*fp)
        second+=coeff*u*((d*d-z/2)*f+(2*d+1)*z*fp+z*z*fpp)
    return value,first,second


def ode_residual(k,n,p,x):
    kap=kappa(n,p)
    f,fp,fpp=raw_mode(k,kap,x)
    g,gp=slope(x),curvature(x)
    phase=cmath.exp(1j*bump(x)*p)
    psi=phase*f
    psip=phase*(fp+1j*g*p*f)
    psipp=phase*(fpp+2j*g*p*fp+(1j*gp*p-g*g*p*p)*f)
    covariant_p_squared=-psipp+2j*g*p*psip+1j*gp*p*psi+g*g*p*p*psi
    potential=math.exp(2*x)-2*kap*math.exp(x)
    return covariant_p_squared+potential*psi-k*k*psi


def trajectory(t,k,kap):
    r=math.sqrt(k*k+kap*kap)
    den=r*math.cosh(t)-kap
    volume=k*k/den
    pi=-k*r*math.sinh(t)/den
    return math.log(volume),pi


def shift_integral(t,k,kap,panels=2048):
    # Integral from -10; outside bump support the contribution is exactly 0.
    return simpson(lambda s:-slope(trajectory(s,k,kap)[0])*trajectory(s,k,kap)[1]/k,
                   -10,t,panels)


def readout_probability(k,p):
    s=[scatter(k,kappa(n,p)) for n in (0,1)]
    return (1+(s[1]*s[0].conjugate()).real)/2


def simpson_values(values,a,b):
    n=len(values)-1
    if n<=0 or n%2: raise ValueError('positive even panel count required')
    return (b-a)/(3*n)*(values[0]+values[-1]+sum((4 if i%2 else 2)*values[i] for i in range(1,n)))


def finite_pointer_readout(k,panels=128,q_limit=4.,p_limit=.6):
    """Oscillator +/- and pointer Q in/out, initial chi(p) proportional to 1-p^2/a^2."""
    ps=[-p_limit+2*p_limit*i/panels for i in range(panels+1)]
    chi=[math.sqrt(15/(16*p_limit))*(1-(p/p_limit)**2) for p in ps]
    modes=[[chi[i]*scatter(k,kappa(n,p)) for i,p in enumerate(ps)] for n in (0,1)]
    rows=[[],[]]
    for j in range(panels+1):
        q=-q_limit+2*q_limit*j/panels
        phases=[cmath.exp(1j*p*q) for p in ps]
        amps=[simpson_values([v*phase for v,phase in zip(mode,phases)],-p_limit,p_limit)/math.sqrt(2*math.pi) for mode in modes]
        rows[0].append(abs((amps[0]+amps[1])/2)**2)
        rows[1].append(abs((amps[0]-amps[1])/2)**2)
    inside=[simpson_values(row,-q_limit,q_limit) for row in rows]
    total_plus=simpson_values([chi[i]**2*readout_probability(k,p) for i,p in enumerate(ps)],-p_limit,p_limit)
    total_norm=simpson_values([c*c for c in chi],-p_limit,p_limit)
    totals=[total_plus,total_norm-total_plus]
    return {'plus_inside':inside[0],'plus_outside':totals[0]-inside[0],
            'minus_inside':inside[1],'minus_outside':totals[1]-inside[1]}


def run():
    maxres=0.
    for k in (2.,3.,5.):
        for n in (0,1):
            for p in (-.5,0.,.4):
                for x in (-1.2,-.7,0.,.4,.9,1.2):
                    maxres=max(maxres,abs(ode_residual(k,n,p,x)))
    assert maxres<1e-9
    # Same physical recollapse and the canonical shift for a single classical
    # trajectory; at the endpoints both baselines have the same pointer shift.
    k,p=2.,.4
    kap=kappa(0,p)
    maxshift=0.
    rows=[]
    for t in (-4.,-2.,-.8,0.,.8,2.,4.):
        x,pi=trajectory(t,k,kap)
        actual=shift_integral(t,k,kap,8192)
        target=-bump(x)
        maxshift=max(maxshift,abs(actual-target))
        rows.append({'scalar_T':t,'x':x,'direction':1 if pi>0 else (-1 if pi<0 else 0),
                     'extra_pointer_shift':actual,'minus_G':target})
    assert maxshift<2e-8
    b=-.25
    r=math.sqrt(k*k+kap*kap)
    tc=math.acosh((k*k/math.exp(b)+kap)/r)
    incoming=shift_integral(-tc,k,kap,8192)
    outgoing=shift_integral(tc,k,kap,8192)
    assert abs(incoming-outgoing)<2e-8
    full=shift_integral(10,k,kap,8192)
    assert abs(full)<2e-8
    # Same pointer energy is present in the reference and interacting
    # Hamiltonians; P-dependent reference phase is not attributed to g.
    at_zero=readout_probability(2,0)
    at_p=readout_probability(2,.6)
    assert abs(at_zero-at_p)>1e-4
    meanp=simpson(lambda pp:simpson(lambda kk:readout_probability(kk,pp),2,2.01,48)/.01,
                  -.6,.6,48)/1.2
    # Uniform, normalizable k packet; genuine finite-norm pointer packet.
    ks=[2+.01*i/4 for i in range(5)]
    values=[finite_pointer_readout(x,128) for x in ks]
    probabilities={key:simpson_values([v[key] for v in values],2,2.01)/.01 for key in values[0]}
    assert all(v>=0 for v in probabilities.values())
    assert abs(sum(probabilities.values())-1)<2e-8
    coarse=finite_pointer_readout(2.005,128)
    fine=finite_pointer_readout(2.005,256)
    assert max(abs(coarse[x]-fine[x]) for x in coarse)<1e-7
    return {'status':'passed',
            'scope':'Exact cancellation for one source-accounted pure-gradient coupling, not a universal detector no-go or a B7 pass.',
            'max_covariant_morse_ode_residual':maxres,
            'classical_example':{'k':k,'pointer_momentum':p,'pointer_mass':M,
                                 'kappa_including_pointer_energy':kap,
                                 'turning_volume':kap+math.sqrt(k*k+kap*kap),
                                 'chosen_volume':math.exp(b),
                                 'scalar_crossing_times':[-tc,tc],
                                 'extra_pointer_shift_at_crossings':[incoming,outgoing],
                                 'extra_pointer_shift_full_cycle':full,
                                 'max_trajectory_shift_error':maxshift,'samples':rows},
            'energy_matched_reference':{'p_plus_at_p_0':at_zero,'p_plus_at_p_0_6':at_p,
                    'uniform_k_2_to_2_01_and_p_minus_0_6_to_0_6':meanp,
                    'coupled_and_reference_scattering_identical_by_unitary_conjugation':True},
            'complete_finite_packet_pointer_and_ramsey_readout':{'q_interval':[-4,4],
                    'pointer_wavefunction':'sqrt(15/(16a))*(1-(p/a)^2) for |p|<=a, a=0.6',
                    'k_band':[2,2.01], 'probabilities':probabilities,
                    'max_128_vs_256_panel_difference_at_midband':max(abs(coarse[x]-fine[x]) for x in coarse)}}


def main():
    r=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__': main()
