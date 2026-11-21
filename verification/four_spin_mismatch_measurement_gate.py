#!/usr/bin/env python3
"""Conditional measurement construction for the existing four-spin model.

Exact rational controls, not measurements in brains or of feeling.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json

from coupled_subject_boundary_gate import STATES, stationary
from integrated_subject_horizon_audit import kernel, mismatch


def dist(outer, middle=F(1, 4), right=F(1, 2)):
    return {s: F(1, 16) * (1 + outer*s[0]*s[1]) *
            (1 + middle*s[1]*s[2]) * (1 + right*s[2]*s[3])
            for s in STATES}


def majority_failure(n):
    assert n % 2 == 1
    return sum((F(comb(n, k)) * F(3, 4)**k * F(1, 4)**(n-k)
                for k in range(n//2 + 1)), F(0))


def posterior(joint, e, d):
    # H=11: with correct orientation each noisy bit must read 1;
    # with reversed orientation each noisy bit must read 0.
    observed = F(0)
    true_11_and_observed = F(0)
    for (a, b), mass in joint.items():
        prob11 = ((1-e if a else e) * (1-e if b else e))
        prob00 = ((e if a else 1-e) * (e if b else 1-e))
        weight = mass * ((1-d)*prob11 + d*prob00)
        observed += weight
        if (a, b) == (1, 1):
            true_11_and_observed += weight
    return observed, 1-true_11_and_observed/observed


def run():
    p = dist(F(1, 2))
    assert p == stationary(F(1, 4), (None,) * 4)
    assert sum(p.values()) == 1
    odds = []
    for s2, s3 in product((-1, 1), repeat=2):
        odds.append(p[1, 1, s2, s3] * p[-1, -1, s2, s3] /
                    (p[1, -1, s2, s3] * p[-1, 1, s2, s3]))
    assert odds == [F(9)] * 4
    assert sum(v for s, v in p.items() if s[0] == s[1]) == F(3, 4)
    # Single channel A factor (1+x/2); B has target (1-x/2)
    # and a parallel residual (1+4x/5). Their product is 3/5 of A.
    for x in (-1, 1):
        assert (1-F(1, 2)*x)*(1+F(4, 5)*x) == F(3, 5)*(1+F(1, 2)*x)
    # Exact heat-bath transition law depends only on ratios of full weights.
    K = kernel(F(1, 4))
    for s in STATES:
        for i in range(4):
            flipped = tuple(-v if j == i else v for j, v in enumerate(s))
            assert K[s][flipped] == F(1, 4)*p[flipped]/(p[s]+p[flipped])
    # Under selective target removal, A loses its only edge; B retains 4/5.
    prob_a_gate = sum(v for s, v in dist(F(0)).items() if s[0] == s[1])
    prob_b_gate = sum(v for s, v in dist(F(4, 5)).items() if s[0] == s[1])
    assert (prob_a_gate, prob_b_gate) == (F(1, 2), F(9, 10))
    j = {(a, b): F(0) for a in (0, 1) for b in (0, 1)}
    for s, mass in p.items():
        for z, prob in K[s].items():
            j[mismatch(s), mismatch(z)] += mass*prob
    assert j == {(0, 0): F(295, 448), (0, 1): F(41, 448),
                 (1, 0): F(41, 448), (1, 1): F(71, 448)}
    sensor_bit_error = F(1, 20)
    q_error = 2*sensor_bit_error*(1-sensor_bit_error)
    assert q_error == F(19, 200)
    d = majority_failure(19)
    w0, rho0 = posterior(j, q_error, F(0))
    w, rho = posterior(j, q_error, d)
    assert d == F(611828695, 68719476736)
    assert (w0, rho0) == (F(678631, 4480000), F(388493, 2714524))
    assert (w, rho) == (F(373009915633097, 2405181685760000),
                         F(2034055896400553, 11936317300259104))
    minima = {}
    for goal in (F(1, 20), F(1, 100), F(1, 1000)):
        n = next(n for n in range(1, 201, 2) if majority_failure(n) <= goal)
        assert all(majority_failure(k) > goal for k in range(1, n, 2))
        minima[str(goal)] = {'odd_n': n, 'failure': str(majority_failure(n))}
    return {
        'status': 'passed',
        'scope': 'Exact physical-model controls only; no empirical mismatch measurement, subject, phenomenal assay, or selective intervention established.',
        'conditional_cross_product_odds': [str(x) for x in odds],
        'passive_aligned_fraction': '3/4',
        'equal_full_weight_ratio_B_to_A': '3/5',
        'selective_gate_aligned_fractions': {'A': str(prob_a_gate), 'B': str(prob_b_gate)},
        'odd_calibration_sizes_and_failure': minima,
        'noise_example': {'per_spin_error': str(sensor_bit_error), 'per_q_readout_error': str(q_error),
            'independent_19_state_calibration_failure': str(d),
            'observed_11_probability_known_orientation': str(w0),
            'conditional_true_cell_error_known_orientation': str(rho0),
            'observed_11_probability_including_calibration_error': str(w),
            'conditional_true_cell_error_including_calibration_error': str(rho)},
    }


def main():
    data = run()
    text = json.dumps(data, indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
