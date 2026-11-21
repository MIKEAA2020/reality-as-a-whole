#!/usr/bin/env python3
"""Imperfect intervention bounds in a conditional four-spin Ising model.

No biological data, actual selective intervention, or phenomenal assay.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil, exp, log
from pathlib import Path
import json

from four_spin_mismatch_measurement_gate import dist


def conditional_cells(outer):
    p = dist(outer)
    values = [p[a, b, 1, 1] for a, b in ((1, 1), (-1, -1), (1, -1), (-1, 1))]
    total = sum(values)
    return tuple(v / total for v in values)


def odds(c):
    return c[0] * c[1] / (c[2] * c[3])


def odds_box(c, eps):
    lo = [x-eps for x in c]
    hi = [x+eps for x in c]
    assert min(lo) > 0 and max(hi) < 1
    return lo[0]*lo[1]/(hi[2]*hi[3]), hi[0]*hi[1]/(lo[2]*lo[3])


def coef_box(delta_lo, delta_hi, b, lam_lo, lam_hi):
    assert delta_lo <= delta_hi and 0 < lam_lo <= lam_hi and b >= 0
    endpoints = [(d-r)/l for d, r, l in product((delta_lo, delta_hi), (-b, b), (lam_lo, lam_hi))]
    return min(endpoints), max(endpoints)


def calc():
    base = conditional_cells(F(1, 2))
    a = conditional_cells(F(0))
    b = conditional_cells(F(4, 5))
    assert odds(base) == 9 and odds(a) == 1 and odds(b) == 81
    eps = F(1, 50)
    n = 7360  # permits exact integer frequencies for every illustrative cell
    alpha = 16*exp(-2*n*float(eps)**2)
    assert alpha < .05 and n == 7360
    assert all((n*v).denominator == 1 for row in (base, a, b) for v in row)
    basebox = odds_box(base, eps)
    rows = {}
    for name, values in (('A', a), ('B', b)):
        endbox = odds_box(values, eps)
        d0 = log(float(basebox[0]/endbox[1]))/4
        d1 = log(float(basebox[1]/endbox[0]))/4
        target = coef_box(d0, d1, .1, .8, 1.)
        rows[name] = {'hypothetical_frequencies': [str(v) for v in values],
                      'odds_interval': [str(x) for x in endbox],
                      'delta_interval': [d0, d1], 'target_J_interval': list(target)}
    assert rows['A']['target_J_interval'][0] > 0
    assert rows['B']['target_J_interval'][1] < 0
    # Same on/off total couplings, opposite designated target coefficients.
    net0, net1, lam = F(1, 2), F(1, 5), F(1)
    candidates = []
    for target in (F(1, 2), F(-1, 10)):
        r0 = net0-target
        r1 = net1-(1-lam)*target
        drift = r0-r1
        assert abs(drift) <= F(2, 5)
        assert net0-net1 == lam*target+drift
        candidates.append({'target_J': str(target), 'residual_on': str(r0),
                           'residual_off': str(r1), 'residual_drift': str(drift)})
    checks = 0
    # Exact rational exhaustive containment for overlapping signs and nonzero
    # gain, independently checking all interior grid points against corners.
    for L in map(F, (-1, 0, 1)):
        for U in (L, L+1, L+2):
            for radius in (F(0), F(1, 2), F(1)):
                lower, upper = coef_box(L, U, radius, F(1, 2), F(1))
                for d, r, l in product((L, (L+U)/2, U), (-radius, F(0), radius), (F(1, 2), F(3, 4), F(1))):
                    assert lower <= (d-r)/l <= upper
                    checks += 1
    return {'status': 'passed',
            'scope': 'Hypothetical equilibrium Ising gate; no physical or experiential human data.',
            'exact_conditional_odds': {'baseline': '9', 'A_gate': '1', 'B_gate': '81'},
            'hypothetical_n_per_condition': n, 'sampling_epsilon': str(eps),
            'simultaneous_Hoeffding_failure_bound': alpha,
            'baseline_conditional_frequencies': [str(v) for v in base],
            'baseline_odds_interval': [str(x) for x in basebox],
            'intervention_assumptions': {'residual_drift_bound': 0.1, 'attenuation_fraction': [0.8, 1.0]},
            'hypothetical_results': rows,
            'nonselective_opposite_target_counterexample': {'net_couplings': [str(net0), str(net1)],
                 'attenuation': str(lam), 'max_residual_drift': '2/5', 'models': candidates},
            'rational_grid_containment_checks': checks}


def main():
    text = json.dumps(calc(), indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
