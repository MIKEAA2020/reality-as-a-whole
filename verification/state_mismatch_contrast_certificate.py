#!/usr/bin/env python3
"""Conditional state-cost contrast bounds; finite checks, no biological data."""
import json
import math
import random
from pathlib import Path

PI = math.pi
ROOT = Path(__file__).resolve().parent.parent


def distance(a, b):
    return abs((a - b + PI) % (2 * PI) - PI)


def f(theta):
    return 1 - math.cos(theta)


def edge_calibration(y0, y1, eps, lambda_min, lambda_max):
    if not (eps >= 0 and 0 < lambda_min <= lambda_max):
        raise ValueError('invalid calibration assumptions')
    rho = math.sqrt(2) * eps
    r = math.hypot(y0, y1)
    if r <= rho:
        return None
    return {'a_hat': math.atan2(-y0, y1),
            'angle_error': math.asin(rho / r),
            'k_low': (r - rho) / lambda_max,
            'k_high': (r + rho) / lambda_min}


def f_interval(cal, measured_x, x_error):
    if not (0 <= x_error <= PI):
        raise ValueError('phase error must be in [0, pi]')
    d = distance(measured_x, cal['a_hat'])
    err = x_error + cal['angle_error']
    return (f(max(0.0, d - err)), f(min(PI, d + err)))


def contribution_interval(cal, a, da, b, db):
    a_low, a_high = f_interval(cal, a, da)
    b_low, b_high = f_interval(cal, b, db)
    z_low, z_high = a_low - b_high, a_high - b_low
    products = [k * z for k in (cal['k_low'], cal['k_high'])
                for z in (z_low, z_high)]
    return min(products), max(products)


def cost(k, x, a):
    return k * f(x-a)


def main():
    eps, lmin, lmax, phaseerr = 0.1, 0.5, 1.0, 0.05
    cal = edge_calibration(0.0, -1.0, eps, lmin, lmax)
    assert cal is not None
    lo, hi = contribution_interval(cal, 0.0, phaseerr, PI, phaseerr)
    assert lo > 0
    # Model A: only the calibrated antiphase channel; model B has an
    # additional in-phase channel with weight K. On-minus-off targeting the
    # antiphase channel and ungated endpoint forces agree for both systems.
    hidden = {}
    for K in (0.0, 2.0):
        def total(x): return cost(1.0,x,PI) + cost(K,x,0.0)
        def force(x): return -math.sin(x) + K * math.sin(x)
        assert abs(force(0.0)) < 1e-12 and abs(force(PI)) < 1e-12
        assert abs((-math.sin(0.0)) - 0.0) < 1e-12
        assert abs((-math.sin(PI/2)) + 1.0) < 1e-12
        hidden[str(K)] = {'total_cost_A':total(0.0), 'total_cost_B':total(PI),
                          'total_cost_difference_A_minus_B':total(0.0)-total(PI),
                          'net_force_at_A':force(0.0),'net_force_at_B':force(PI),
                          'net_force_at_pi_over_2':force(PI/2)}
    assert hidden['0.0']['total_cost_difference_A_minus_B'] > 0
    assert hidden['2.0']['total_cost_difference_A_minus_B'] < 0
    # Check uncertainty containment including cases with negative contrast.
    rng=random.Random(918243)
    tested=0; unresolved=0
    for _ in range(20000):
        a=rng.uniform(-PI,PI); k=rng.uniform(.1,5.0)
        lam=rng.uniform(lmin,lmax)
        y0=-lam*k*math.sin(a)+rng.uniform(-eps,eps)
        y1=lam*k*math.cos(a)+rng.uniform(-eps,eps)
        c=edge_calibration(y0,y1,eps,lmin,lmax)
        if c is None:
            unresolved+=1
            continue
        xA=rng.uniform(-PI,PI); xB=rng.uniform(-PI,PI)
        xAh=xA+rng.uniform(-phaseerr,phaseerr)
        xBh=xB+rng.uniform(-phaseerr,phaseerr)
        lb,ub=contribution_interval(c,xAh,phaseerr,xBh,phaseerr)
        true=cost(k,xA,a)-cost(k,xB,a)
        assert lb-1e-10 <= true <= ub+1e-10
        assert c['k_low']-1e-10 <= k <= c['k_high']+1e-10
        assert distance(c['a_hat'],a)<=c['angle_error']+1e-10
        # Relabel phase reference for the full calibration and both states.
        shift=rng.uniform(-PI,PI)
        shifted=dict(c,a_hat=c['a_hat']+shift)
        sl,su=contribution_interval(shifted,xAh+shift,phaseerr,xBh+shift,phaseerr)
        assert abs(sl-lb)<1e-10 and abs(su-ub)<1e-10
        tested+=1
    assert edge_calibration(0,0,eps,lmin,lmax) is None
    # Unknown attenuation down to arbitrarily close to zero: same observed
    # gated response has k=1/lambda, so absolute scale is unbounded.
    gain_examples=[{'lambda':lam,'k':1/lam,'observed_response_magnitude':lam*(1/lam)}
                   for lam in (1.0,0.1,0.01,0.001)]
    result={
      'status':'completed',
      'scope':'conditional deterministic first-harmonic model; not a biological observation, physical channel validation, experiential assay, or proof of ground',
      'illustrative_calibration':{'y0':0.0,'y1':-1.0,'epsilon_component':eps,
        'lambda_min':lmin,'lambda_max':lmax,'phase_error_each_radians':phaseerr,
        'k_low':cal['k_low'],'k_high':cal['k_high'],'angle_error_radians':cal['angle_error'],
        'measured_state_A':0.0,'measured_state_B':PI,
        'certified_contribution_difference_lower':lo,'certified_contribution_difference_upper':hi},
      'hidden_parallel_channel_example':hidden,
      'arbitrarily_small_gain_examples':gain_examples,
      'seed':918243,'random_cases':20000,'resolved_cases_checked':tested,'unresolved_cases':unresolved,
      'tested_invariants':['true k and offset contained','true A-minus-B contribution contained',
         'common phase-reference shift leaves bounds unchanged','unresolved zero response','hidden-channel contrast reversal'],
      'caution':'Random tests check implementation; mathematical bounds require assumptions and independent error calibration.'}
    path=ROOT/'verification/state_mismatch_contrast_certificate.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
