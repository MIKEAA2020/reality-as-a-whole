#!/usr/bin/env python3
"""Continuum proper-time scalar result: numerical checks, not a QFT proof.

Requires mpmath. Evaluates the manifestly subtracted Euclidean Bessel integral;
uses a small-argument series to avoid catastrophic subtraction in its bracket.
"""
import json
from pathlib import Path
import mpmath as mp


def angular_bracket(z):
    """1-2*J1(z)/z-z^2/8; stable near zero."""
    z = mp.mpf(z)
    if abs(z) < 1:
        # n=0 and n=1 cancel exactly. Work to current precision.
        if z == 0:
            return mp.mpf(0)
        total = mp.mpf(0)
        n = 2
        term = z**4/192
        while True:
            total -= term
            n += 1
            term *= -(z*z/4)/(n*(n+1))
            if abs(term) <= mp.eps*abs(total):
                break
        return total
    return 1-2*mp.besselj(1, z)/z-z*z/8


def moment(power):
    return mp.quad(lambda u: u**power*mp.besselk(1, u)**3,
                   [0, 1, 4, 12, mp.inf])


def continuum_value(k, mass=1):
    k, mass = mp.mpf(k), mp.mpf(mass)
    if mass <= 0:
        raise ValueError('mass must be positive')
    if k == 0:
        return mp.mpf(0)
    return mass**2/(8*mp.pi**4)*mp.quad(
        lambda u: mp.besselk(1, u)**3*angular_bracket(abs(k)*u/mass),
        [0, 1, 4, 12, mp.inf])


def run():
    mp.mp.dps = 25
    c4 = moment(4)/(1536*mp.pi**4)
    c6 = moment(6)/(73728*mp.pi**4)
    vals = []
    for k in (mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2')):
        value = continuum_value(k)
        remainder = abs(value+c4*k**4)
        assert value < 0 and remainder <= c6*k**6
        vals.append({'k_over_m': str(k), 'continuum_value_m_squared_units': str(value),
                     'absolute_remainder': str(remainder), 'remainder_bound': str(c6*k**6)})
    return {'scope': 'infinite-volume proper-time continuum expression; m>0, not book sharp cutoff',
            'precision_decimal_digits': mp.mp.dps,
            'fourth_order_coefficient_integral': str(c4),
            'sixth_order_remainder_bound_integral': str(c6), 'samples': vals}


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
