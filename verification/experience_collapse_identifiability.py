#!/usr/bin/env python3
"""Exact check of the declared one-step dephasing/collapse identifiability model.

Not a model of consciousness, a test of actual collapse, or a no-go theorem for
all dynamical theories. All parameters and matrices are rational.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def dephase(mat, strength):
    assert 0 <= strength <= 1
    return tuple(tuple(mat[i][j] if i == j else (1-strength)*mat[i][j]
                       for j in range(2)) for i in range(2))


def matadd(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def scale(c, a):
    return tuple(tuple(c*a[i][j] for j in range(2)) for i in range(2))


def trigger(mat, s, p):
    # With probability s apply Λ_p, else do nothing. No selector is derived.
    return matadd(scale(1-s, mat), scale(s, dephase(mat, p)))


def score(k):
    # Fixed 3/5,4/5 local settings of the preceding friend circuit.
    return F(6, 5) + F(8, 5)*k


def main():
    unit = [tuple(tuple(F(int((i, j) == (a, b))) for j in range(2))
                  for i in range(2)) for a, b in product(range(2), repeat=2)]
    grid = [F(i, 10) for i in range(11)]
    composition = 0
    for p, q in product(grid, repeat=2):
        effective = p+q-p*q
        for e in unit:
            assert dephase(dephase(e, p), q) == dephase(e, effective)
        composition += 1
    trigger_checks = 0
    for s, p in product(grid, repeat=2):
        for e in unit:
            assert trigger(e, s, p) == dephase(e, s*p)
        trigger_checks += 1

    # Scenario A/B have equal physical background and different event strength
    # and prevalence. Scenario C has no trigger and more unobserved ordinary noise.
    scenarios = [
        {'s': F(1), 'p': F(1, 6), 'q': F(1, 10)},
        {'s': F(1, 2), 'p': F(1, 3), 'q': F(1, 10)},
        {'s': F(0), 'p': F(1), 'q': F(1, 4)},
    ]
    reference = [dephase(e, F(1,4)) for e in unit]
    for row in scenarios:
        s,p,q = row['s'],row['p'],row['q']
        assert [trigger(dephase(e,q),s,p) for e in unit] == reference
        k = (1-q)*(1-s*p)
        assert k == F(3,4) and score(k) == F(12,5)

    # Exact identified-set projection for independently calibrated intervals.
    rlo, rhi = F(88,100), F(92,100)
    klo, khi = F(74,100), F(76,100)
    lo = max(F(0), 1-khi/rlo)
    hi = min(F(1), 1-klo/rhi)
    assert (lo, hi) == (F(3,22), F(9,46))
    assert lo == 1 - khi/rlo and hi == 1 - klo/rhi
    # If 1/2 ≤ s ≤ 1, the projected p range is [lo, 2*hi].
    assert (lo, hi/F(1,2)) == (F(3,22), F(9,23))
    # Same observed coherence but 121 different background/trigger pairs.
    alternatives = 0
    target = F(1,4)
    for i in range(101):
        effect = target*F(i,100)
        q = (target-effect)/(1-effect)
        assert 0 <= q <= 1 and (1-q)*(1-effect) == F(3,4)
        alternatives += 1
    result = {
        'status': 'passed',
        'scope': 'One declared finite dephasing slot, with interventions outside the slot and observed environment inaccessible. No actual subject, consciousness, experimental or general physical law established.',
        'channel_composition_pairs_checked': composition,
        'trigger_strength_prevalence_pairs_checked': trigger_checks,
        'equal_choi_action_example': {'coherence': '3/4', 'fixed_setting_CHSH': '12/5', 'scenario_a': {'s':'1','p':'1/6','q':'1/10'}, 'scenario_b': {'s':'1/2','p':'1/3','q':'1/10'}, 'scenario_c': {'s':'0','p':'1','q':'1/4'}},
        'confounded_noise_trigger_pairs_for_same_channel': alternatives,
        'illustrative_intervals': {'background_retention':['22/25','23/25'], 'observed_retention':['37/50','19/25'], 'effective_trigger_probability':['3/22','9/46'], 'strength_if_s_at_least_half':['3/22','9/23']},
        'limitations': 'The intervals are stipulated examples, not confidence intervals or empirical values. Stronger models, temporal probes, environmental access and independent subject calibration can change identifiability.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
