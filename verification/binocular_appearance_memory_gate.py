#!/usr/bin/env python3
"""Exact toy predictions for matched binocular appearances and later probes.

All coordinates and parameters are stipulations, not human colorimetric data.
"""
from fractions import Fraction
import json


def fraction(value):
    return value if isinstance(value, Fraction) else Fraction(str(value))


def histories(amplitude):
    """Opposite, swapped eye histories; a is an effective adaptation input."""
    a = fraction(amplitude)
    if a < 0:
        raise ValueError('amplitude must be nonnegative')
    return {'A': (a, -a), 'B': (-a, a)}


def appearance(history):
    left, right = history
    return (left + right) / 2


def probe(history, gain, eye):
    """Signed aftereffect with identical neutral test stimuli, no noise."""
    k = fraction(gain)
    if k < 0:
        raise ValueError('gain must be nonnegative')
    left, right = history
    if eye == 'L':
        return -k * left
    if eye == 'R':
        return -k * right
    if eye == 'both':
        return -k * (left + right) / 2
    raise ValueError('eye must be L, R, or both')


def predictions(amplitude, gain):
    states = histories(amplitude)
    return {name: {'appearance': appearance(state),
                   **{eye: probe(state, gain, eye) for eye in ('L', 'R', 'both')}}
            for name, state in states.items()}


def interaction(p):
    """B minus A for the left probe, minus B minus A for the right probe."""
    return (p['B']['L'] - p['A']['L']) - (p['B']['R'] - p['A']['R'])


def mismatch_bound(epsilon, lipschitz_left, lipschitz_right):
    """Bound on absolute interaction from eye-wise response Lipschitz bounds."""
    e, kl, kr = map(fraction, (epsilon, lipschitz_left, lipschitz_right))
    if min(e, kl, kr) < 0:
        raise ValueError('bounds must be nonnegative')
    return e * (kl + kr)


def as_string(value):
    return str(value)


def main():
    amplitude, gain = Fraction(1), Fraction(1, 4)
    p = predictions(amplitude, gain)
    receipt = {
        'scope': 'Exact arithmetic for stipulated abstract models; not participant data or measured gains.',
        'amplitude': as_string(amplitude),
        'gain': as_string(gain),
        'eye_memory_predictions': {h: {key: as_string(value) for key, value in row.items()}
                                   for h, row in p.items()},
        'appearance_only_predictions': {'interaction': '0',
                                        'reason': 'Same appearance history and probe conditions.'},
        'eye_memory_interaction': as_string(interaction(p)),
        'example_appearance_mismatch_bound': {
            'epsilon': '1/20', 'K_left': '1', 'K_right': '1',
            'interaction_absolute_upper_bound': as_string(mismatch_bound('1/20', 1, 1)),
            'warning': 'Invented bounds, not calibration or statistical uncertainty.'},
    }
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
