#!/usr/bin/env python3
"""Conditional finite-band Ramsey calibration in the existing Morse clock.

The analytic bounds are documented in GRAVITY_CLOCK_FINITE_RANGE_CALIBRATION.md.
Numerical checks use the parent scattering code, not independent validation of it.
"""
import cmath
import json
import math
from pathlib import Path

if __package__:
    from .gravitating_clock_probe import log_s, proper_duration, quantum_response, scatter
else:
    from gravitating_clock_probe import log_s, proper_duration, quantum_response, scatter

MU, OMEGA = 1.0, 0.6
KMIN, KMAX, WIDTH = 2.0, 8.0, 0.01
KAP0, KAP1 = OMEGA / 3, OMEGA
AMIN, AMAX = 1.5 - KAP1, 1.5 - KAP0


def constants(n=200_000, alpha=.05):
    if n <= 0 or not 0 < alpha < 1:
        raise ValueError('positive sample size and 0 < alpha < 1 required')
    # Bounds on the phase, then a positive lower bound for sin on that interval.
    lo = OMEGA * 4 / 3 * (math.pi / 2 - math.atan(AMAX / KMIN))
    hi = OMEGA * 4 / 3 * (math.pi / 2 + 2 / KMIN)
    if not 0 < lo < hi < math.pi:
        raise ValueError('phase branch is not certified')
    sinmin = min(math.sin(lo), math.sin(hi))
    lipschitz = 4 / 3 * (1 / AMIN**2 + 1 / AMIN + 1 / KMIN**2)
    epsilon = math.sqrt(math.log(2 / alpha) / (2 * n))
    return {'phase_lower': lo, 'phase_upper': hi, 'sin_lower': sinmin,
            'response_lipschitz': lipschitz, 'statistical_probability_error': epsilon,
            'statistical_duration_error': 2 * epsilon / (OMEGA * sinmin),
            'band_duration_error': lipschitz * WIDTH,
            'total_duration_error': 2 * epsilon / (OMEGA * sinmin) + lipschitz * WIDTH,
            'n': n, 'alpha': alpha}


def estimate_from_frequency(frequency):
    if not 0 <= frequency <= 1:
        raise ValueError('frequency must be in [0,1]')
    b = constants()
    # Clipping is nonexpansive relative to a true probability in this interval.
    pmin = (1 + math.cos(b['phase_upper'])) / 2
    pmax = (1 + math.cos(b['phase_lower'])) / 2
    p = min(pmax, max(pmin, frequency))
    return math.acos(2 * p - 1) / OMEGA


def tau(k):
    if not KMIN <= k <= KMAX:
        raise ValueError('outside declared spectral domain')
    return (log_s(k, KAP1, MU) - log_s(k, KAP0, MU)).imag / OMEGA


def simpson(f, a, b, n=512):
    h = (b-a)/n
    return h / 3 * (f(a) + f(b) + sum((4 if i % 2 else 2)*f(a+i*h) for i in range(1,n)))


def band_probability(start):
    if start < KMIN or start + WIDTH > KMAX:
        raise ValueError('band outside domain')
    return (1 + simpson(lambda k: (scatter(k,KAP1)*scatter(k,KAP0).conjugate()).real,
                         start,start+WIDTH)/WIDTH)/2


def check():
    b=constants()
    samples=[]
    for i in range(61):
        k=KMIN+(KMAX-KMIN)*i/60
        t=tau(k)
        assert b['phase_lower'] <= OMEGA*t <= b['phase_upper']
        # Finite energy gap corresponds to an energy-averaged quantum response.
        integral=simpson(lambda kap: quantum_response(k,kap),KAP0,KAP1)/(KAP1-KAP0)
        assert abs(t-integral)<1e-9
        for kap in (KAP0,.4,KAP1):
            assert abs(quantum_response(k,kap)) < 10
        if k < KMAX:
            h=1e-4
            kp=min(k+h,KMAX)
            assert abs(tau(kp)-t) <= b['response_lipschitz']*(kp-k)+1e-12
    for start in (2,2.5,4,6,7.99):
        p=band_probability(start)
        estimate=estimate_from_frequency(p)
        target=tau(start+WIDTH/2)
        assert abs(estimate-target) <= b['band_duration_error']
        samples.append({'band':[start,start+WIDTH], 'p_plus':p,
                        'estimated_response_at_mean_probability':estimate,
                        'midband_response':target,
                        'midband_classical_at_kappa_0_4':proper_duration(start+WIDTH/2,.4),
                        'difference_from_midband':estimate-target})
    # No globally unique duration from a periodic two-level phase.
    assert abs(math.cos(1.2)-math.cos(1.2+2*math.pi)) < 1e-14
    return {'status':'passed', 'scope':'Conditional numerical checks, not B7 or an experimental result.',
            'bounds':b,'examples':samples}


def main():
    result=check()
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
