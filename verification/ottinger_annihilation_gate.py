#!/usr/bin/env python3
"""Algebraic and numerical checks of a quoted zero-dissipation QED benchmark.

Not a derivation of the QED amplitude, an experimental fit, or an interacting
continuum/dissipative-QFT proof. No dependencies outside the standard library.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math


def amplitude_a(x, u):
    """Book eq. (3.288), normalized by 4 e_0^4, m=1 and E^2=1+x^2."""
    e2 = 1 + x*x
    q4 = e2*e2
    pdotq2 = x*x*e2*u*u
    denominator = q4-pdotq2
    return (q4+pdotq2+2*e2)/denominator - 2*q4/(denominator*denominator)


def amplitude_b(x, u):
    """Book eq. (3.289), same normalized amplitude, x=p/m, u=cos(theta)."""
    denominator = 1+x*x*(1-u*u)
    return (3+x*x*(1+u*u))/denominator - 2/(denominator*denominator)


def limit_shape(u):
    return (1+u*u)/(1-u*u)


def simpson(f, z, steps=4096):
    if steps <= 0 or steps % 2:
        raise ValueError('steps must be a positive even number')
    h = z/steps
    return h/3*(f(0)+f(z)+4*sum(f(h*i) for i in range(1, steps, 2))
                + 2*sum(f(h*i) for i in range(2, steps, 2)))


def run():
    rational_count = 0
    for x in (F(0), F(1, 4), F(1), F(2), F(10), F(100)):
        for u in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1), F(-1, 2)):
            assert amplitude_a(x, u) == amplitude_b(x, u)
            assert amplitude_b(x, u) >= 0
            rational_count += 1
    assert all(amplitude_b(F(0), F(u, 10)) == 1 for u in range(11))
    for x in (F(1), F(2), F(10), F(100)):
        assert amplitude_b(x, F(1)) == 1+2*x*x
    # Moving-angle sequence u=1-1/x^2 exposes non-uniformity near the endpoint.
    moving = []
    for n in (10, 100, 1000, 10000):
        x = F(n); u = 1-F(1, n*n)
        scaled = amplitude_b(x, u)/(x*x)
        moving.append({'x': n, 'scaled_amplitude': float(scaled)})
    assert abs(moving[-1]['scaled_amplitude'] - 2/3) < 1e-7
    integrals = []
    for z in (0.1, 0.5, 0.742, 0.9):
        numeric = simpson(limit_shape, z)
        closed = math.log((1+z)/(1-z))-z
        assert abs(numeric-closed) < 2e-11
        integrals.append({'z': z, 'simpson': numeric, 'closed': closed})
    # Fixed z away from forward direction: normalized finite-x integral converges.
    finite_x = []
    for n in (5, 20, 100, 1000):
        integral = simpson(lambda u: amplitude_b(float(n), u), 0.742)
        finite_x.append({'x': n, 'integral': integral})
    assert abs(finite_x[-1]['integral']-integrals[2]['closed']) < 1e-5
    # 0.511 MeV = 0.000511 GeV, not 0.511 GeV.
    assert F(511, 1000)/1000 == F(511, 1000000)
    return {'scope': 'quoted lowest-order zero-dissipation expressions; not an amplitude derivation',
            'exact_rational_comparisons': rational_count,
            'threshold_shape': '1', 'forward_shape': '1+2*x^2',
            'moving_angle_scaled_limit': '2/3', 'moving_angle_samples': moving,
            'fixed_angle_integrals': integrals, 'finite_x_integrals': finite_x,
            'electron_mass_MeV_rounded': 0.511, 'electron_mass_GeV_rounded': 0.000511}


if __name__ == '__main__':
    report = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
