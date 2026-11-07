"""Robust premise/assay bounds for a hypothetical binary disclosure contrast.

Exact fractions throughout except the Hoeffding sample bound. No human data,
empirical calibration, or phenomenal attribution are supplied by this code.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil, exp, log
from pathlib import Path
import json

ZERO, ONE = F(0), F(1)


def limits(alpha, beta, eta_m, eta_d):
    assert all(ZERO <= x <= ONE for x in (alpha, beta, eta_m, eta_d))
    return (ONE - eta_m) * (ONE - beta), alpha + eta_d * (ONE - alpha)


def mass_table(g, y_good, y_bad):
    """Joint table of (G,Y); conditional Y values are supplied directly."""
    return {(1, 1): g * y_good, (1, 0): g * (ONE - y_good),
            (0, 1): (ONE - g) * y_bad, (0, 0): (ONE - g) * (ONE - y_bad)}


def witness_m(beta, eta, q):
    """Construct a compatible H_M joint law for any q in its sharp range."""
    low = (ONE - eta) * (ONE - beta)
    assert low <= q <= ONE
    weight = (q - low) / (ONE - low) if low != ONE else ZERO
    return mass_table(ONE - eta, (ONE - weight) * (ONE - beta) + weight, weight)


def witness_d(alpha, eta, q):
    """Construct a compatible H_D joint law for any q in its sharp range."""
    high = alpha + eta * (ONE - alpha)
    assert ZERO <= q <= high
    weight = q / high if high else ZERO
    return mass_table(ONE - eta, weight * alpha, weight)


def check_law(table, q, eta, max_error, which):
    assert all(ZERO <= x <= ONE for x in table.values())
    assert sum(table.values()) == ONE
    assert table[(1, 1)] + table[(0, 1)] == q
    good_mass = table[(1, 0)] + table[(1, 1)]
    assert good_mass >= ONE - eta
    error_mass = table[(1, 0) if which == 'M' else (1, 1)]
    # Joint form remains meaningful when P(G)=0, without conditioning on zero.
    assert error_mass <= max_error * good_mass


def str_table(table):
    return {f'G={g},Y={y}': str(table[(g, y)]) for g, y in product((0, 1), repeat=2)}


def main():
    grid = [F(i, 4) for i in range(5)]
    qgrid = [F(i, 20) for i in range(21)]
    checked, overlapping, separated, witnesses = 0, 0, 0, 0
    for alpha, beta, eta_m, eta_d in product(grid, repeat=4):
        low, high = limits(alpha, beta, eta_m, eta_d)
        checked += 1
        for q in qgrid:
            if q >= low:
                check_law(witness_m(beta, eta_m, q), q, eta_m, beta, 'M')
                witnesses += 1
            if q <= high:
                check_law(witness_d(alpha, eta_d, q), q, eta_d, alpha, 'D')
                witnesses += 1
        if low <= high:
            overlapping += 1
            q = (low + high) / 2
            check_law(witness_m(beta, eta_m, q), q, eta_m, beta, 'M')
            check_law(witness_d(alpha, eta_d, q), q, eta_d, alpha, 'D')
        else:
            separated += 1

    # Illustrative numbers: no empirical calibration is claimed.
    alpha = beta = F(1, 10)
    eta = F(3, 25)  # union-bound example: 0.05 + 0.05 + 0.02
    low, high = limits(alpha, beta, eta, eta)
    assert (low, high, low - high) == (F(99, 125), F(26, 125), F(73, 125))
    delta = float(low - high)
    target = 0.025  # each one-sided error bound, separate from calibration uncertainty
    n = ceil(2 * log(1 / target) / (delta * delta))
    assert n == 22 and exp(-n * delta * delta / 2) <= target
    assert exp(-(n - 1) * delta * delta / 2) > target

    # Concrete overlap: same observable Bernoulli(1/2), opposite targets on G.
    eta_overlap = F(1, 2)
    l2, u2 = limits(alpha, beta, eta_overlap, eta_overlap)
    assert l2 == F(9, 20) and u2 == F(11, 20)
    q = F(1, 2)
    m = witness_m(beta, eta_overlap, q)
    d = witness_d(alpha, eta_overlap, q)
    check_law(m, q, eta_overlap, beta, 'M')
    check_law(d, q, eta_overlap, alpha, 'D')

    result = {
        'status': 'passed',
        'exhaustive_parameter_grid_cases': checked,
        'separated_cases': separated,
        'overlapping_or_touching_cases': overlapping,
        'grid_witnesses_checked': witnesses,
        'illustration_only': {
            'alpha': str(alpha), 'beta': str(beta), 'each_gate_failure_upper_bound': str(eta),
            'maintenance_positive_probability_lower_bound': str(low),
            'distribution_positive_probability_upper_bound': str(high),
            'separation_gap': str(low - high), 'threshold': str((low + high) / 2),
            'independent_bernoulli_sample_size_hoeffding': n,
            'bound_for_each_error_probability': exp(-n * delta * delta / 2),
            'target_each_error_probability': target,
        },
        'indistinguishable_overlap_example': {
            'gate_failure_upper_bound_each': str(eta_overlap),
            'maintenance_minimum': str(l2), 'distribution_maximum': str(u2),
            'observed_positive_probability_both': str(q),
            'maintenance_joint_G_Y': str_table(m), 'distribution_joint_G_Y': str_table(d),
        },
        'limitations': ('The gate and calibration bounds, subject-specific target, independence, '
                        'and choice of experimental domain are assumptions, not observed facts. '
                        'This does not identify the whole ontology or establish a phenomenal mapping.'),
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
