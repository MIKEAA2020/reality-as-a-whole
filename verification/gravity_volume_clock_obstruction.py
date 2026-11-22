#!/usr/bin/env python3
"""Volume-evaluation obstruction in the existing two-channel Morse clock.

Calculations check pointwise mode identities and a chosen finite spectral
packet. Eigenvalue existence and unbounded-inverse claims are analytical in the
report, not established by sampling. Standard library only.
"""
import json
import math
from pathlib import Path

if __package__:
    from .gravitating_clock_probe import loggamma, morse_mode
else:
    from gravitating_clock_probe import loggamma, morse_mode

KAPPAS=(.2,.6)


def mode(k,kappa,volume=1.0):
    """Continuum-normalized real Morse mode at x=log(volume)."""
    if k<=0 or volume<=0:
        raise ValueError('positive k and volume required')
    f=morse_mode(k,kappa,2*volume)[0]
    if abs(f.imag)>1e-9*max(1,abs(f.real)):
        raise ArithmeticError('expected real standing mode')
    norm=math.exp(loggamma(.5-kappa-1j*k).real-loggamma(-2j*k).real)/math.sqrt(2*math.pi)
    return norm*f.real


def response(k,kappa,volume=1.0):
    # Group-averaged positive-frequency history (the 1/sqrt(2k) Jacobian).
    return mode(k,kappa,volume)/math.sqrt(2*k)


def bisect_root(kappa,left,right,volume=1.0):
    a,b=left,right
    fa=mode(a,kappa,volume)
    fb=mode(b,kappa,volume)
    if fa*fb>=0: raise ValueError('interval must bracket a sign change')
    for _ in range(65):
        mid=(a+b)/2
        fm=mode(mid,kappa,volume)
        if fa*fm<=0: b=mid
        else: a=mid; fa=fm
    return (a+b)/2


def simpson(f,a,b,n=1024):
    if n<=0 or n%2: raise ValueError('positive even subdivision count required')
    h=(b-a)/n
    return h*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))/3


def packet_filter(a,b,n=1024):
    if not 0<a<b: raise ValueError('positive nonempty packet band required')
    r=lambda k: [abs(response(k,kap)) for kap in KAPPAS]
    denom=simpson(lambda k:sum(x*x for x in r(k)),a,b,n)/(b-a)
    cross=simpson(lambda k:math.prod(r(k)),a,b,n)/(b-a)
    return {'band':[a,b], 'root_record_plus_probability':1.0,
            'conditional_record_plus_probability':.5+cross/denom,
            'unnormalized_evaluation_weight':denom/2}


def volume_max(k,kappa):
    return kappa+math.sqrt(k*k+kappa*kappa)


def run():
    roots=[bisect_root(.2,2.8,2.9),bisect_root(.6,2.49,2.50)]
    assert abs(roots[0]-2.817906089935545)<2e-11
    assert abs(roots[1]-2.49654621513618)<2e-11
    assert abs(response(roots[1],.6))<1e-12
    assert abs(response(roots[1],.2))>.18
    # A normalized packet with support shrinking around the excited-channel node
    # makes the filtered joint + record approach 1/2, not its original value 1.
    packets=[]
    for width in (.01,.002,.0004):
        x=packet_filter(roots[1]-width/2,roots[1]+width/2)
        assert .5<=x['conditional_record_plus_probability']<.53
        packets.append(x)
    for left,right in zip(packets,packets[1:]):
        assert abs(right['conditional_record_plus_probability']-.5)<abs(left['conditional_record_plus_probability']-.5)
    p512=packet_filter(2.49,2.50,512)
    p1024=packet_filter(2.49,2.50,1024)
    assert abs(p512['conditional_record_plus_probability']-p1024['conditional_record_plus_probability'])<2e-8
    # Classic turning volumes differ for the two gravitating detector channels.
    turn=[volume_max(2,kap) for kap in KAPPAS]
    assert turn[0]<2.4<turn[1]
    assert volume_max(2.01,.2)<2.4<volume_max(2,.6)
    return {'status':'passed',
            'scope':'Numerical consistency controls for assumed Morse model; not an operational clock or B7 pass.',
            'volume':1.0,'numerical_mode_nodes_k':{'kappa_0_2':roots[0],'kappa_0_6':roots[1]},
            'ground_response_at_excited_node':response(roots[1],.2),
            'uniform_bands_centered_on_excited_node':packets,
            'packet_2_49_to_2_50':p1024,
            'classical_turning_volumes_at_k_2':turn,
            'classical_volume_between_turns':2.4}


def main():
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
