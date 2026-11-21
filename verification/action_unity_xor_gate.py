#!/usr/bin/env python3
"""Physical response/information check only: no subject or experience inferred."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

from coupled_subject_boundary_gate import stationary
from integrated_subject_horizon_audit import mismatch


def distribution():
    out = defaultdict(F)
    for s, p in stationary(F(1, 4), (None,) * 4).items():
        out[(mismatch(s, (0, 1)), mismatch(s, (2, 3)))] += p
    return dict(out)


def local_oracle(dist, side):
    """Max XOR success using only one of the two bits; exact Bayes bound."""
    weights = defaultdict(lambda: [F(0), F(0)])
    for (x, y), p in dist.items():
        weights[(x, y)[side]][x ^ y] += p
    return sum((max(v) for v in weights.values()), F(0))


def local_strategies(dist, side):
    results = []
    for table in product((0, 1), repeat=2):
        results.append(sum((p for (x, y), p in dist.items()
                            if table[(x, y)[side]] == (x ^ y)), F(0)))
    return results


def run():
    balanced = {(x, y): F(1, 4) for x, y in product((0, 1), repeat=2)}
    equilibrium = distribution()
    assert equilibrium == {(0, 0): F(9, 16), (0, 1): F(3, 16),
                           (1, 0): F(3, 16), (1, 1): F(1, 16)}
    for dist, expected in ((balanced, F(1, 2)), (equilibrium, F(3, 4))):
        for side in (0, 1):
            assert local_oracle(dist, side) == expected
            assert max(local_strategies(dist, side)) == expected
    # Explicit random-input preparation, not the stationary distribution.
    for x, y in product((0, 1), repeat=2):
        s = (1, (-1) ** x, 1, (-1) ** y)
        assert mismatch(s, (0, 1)) == x and mismatch(s, (2, 3)) == y
        a = x ^ y
        assert a != ((1 - x) ^ y) and a != (x ^ (1 - y))
    # Exact marginal independence under balanced inputs; action depends on pair.
    for side in (0, 1):
        for bit, a in product((0, 1), repeat=2):
            joint = sum((p for (x, y), p in balanced.items()
                         if (x, y)[side] == bit and x ^ y == a), F(0))
            assert joint == F(1, 4)
    return {'status': 'passed',
            'scope': 'Hypothetical physical response model; no real intervention, phenomenal states, subject count or calibrated report.',
            'inputs': 'q(0,1), q(2,3) at t=1/4; preparation assumed, not equilibrium',
            'balanced_one_input_best_accuracy': str(local_oracle(balanced, 0)),
            'equilibrium_one_input_best_accuracy': str(local_oracle(equilibrium, 0)),
            'equilibrium_pair_probabilities': {f'{x}{y}': str(equilibrium[x,y])
                                               for x, y in sorted(equilibrium)},
            'balanced_action_independent_of_either_input_marginally': True,
            'action_changes_under_either_input_flip_for_all_four_inputs': True,
            'local_boolean_strategies_checked_per_distribution': 8}


def main():
    text = json.dumps(run(), indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
