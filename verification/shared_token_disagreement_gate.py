#!/usr/bin/env python3
"""Finite checks for a conditional shared-token/duplication identifiability gate.

The toy outcomes and assumptions are not clinical measurements or evidence of
consciousness. Exact arithmetic; no external packages or downloaded data.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'verification/shared_token_disagreement_gate.json'


def compositions(total, n):
    if n == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, n - 1):
            yield (first,) + rest


def check_sharp_grid(n):
    # A cell is (truth-disagrees, left-error, right-error). Global left truth
    # may be set to zero by simultaneous bit-flip without changing these events.
    cells = list(product((0, 1), repeat=3))
    summaries = []
    for counts in compositions(n, len(cells)):
        delta = sum(k * b for k, (b, _, _) in zip(counts, cells))
        left = sum(k * e for k, (_, e, _) in zip(counts, cells))
        right = sum(k * f for k, (_, _, f) in zip(counts, cells))
        disagreement = sum(k * (b ^ e ^ f) for k, (b, e, f) in zip(counts, cells))
        summaries.append((delta, left, right, disagreement))
    # Bounds are on marginal errors, not exact error rates.
    comparisons = 0
    for delta, a, b in product(range(n + 1), repeat=3):
        vals = [d for t, e, f, d in summaries if t == delta and e <= a and f <= b]
        assert vals
        assert min(vals) == max(0, delta - a - b), (n, delta, a, b, min(vals))
        assert max(vals) == min(n, delta + a + b), (n, delta, a, b, max(vals))
        comparisons += 1
    return len(summaries), comparisons


def history_distribution(policy, duplicate):
    # Every history record is (action,left_report,right_report), with a fresh
    # physical fair bit each stage and a correlated pair of output error bits.
    # 'duplicate' changes token identity only; both local truth values equal z.
    errors = [(0, 0, Fraction(1, 2)), (1, 0, Fraction(1, 4)),
              (0, 1, Fraction(1, 8)), (1, 1, Fraction(1, 8))]
    dist = {(): Fraction(1)}
    for stage in range(2):
        nxt = defaultdict(Fraction)
        for h, ph in dist.items():
            # 32 policies: action at root, then at each of four report histories.
            a = policy[0] if stage == 0 else policy[1 + 2 * h[0][1] + h[0][2]]
            for x in (0, 1):
                z = x ^ a
                # One token g vs two different tokens gl,gr; q forgets identity.
                if duplicate:
                    token_values = {'gl': z, 'gr': z}
                    tl, tr = token_values['gl'], token_values['gr']
                else:
                    token_values = {'g': z}
                    tl, tr = token_values['g'], token_values['g']
                for el, er, pe in errors:
                    record = (a, tl ^ el, tr ^ er)
                    nxt[h + (record,)] += ph * Fraction(1, 2) * pe
        dist = nxt
    assert sum(dist.values()) == 1
    return dist


def main():
    grid = []
    for n in range(1, 9):
        compositions_count, comparisons = check_sharp_grid(n)
        grid.append({'denominator': n, 'distributions': compositions_count,
                     'budget_triplets': comparisons})
    policies = list(product((0, 1), repeat=5))
    for p in policies:
        assert history_distribution(p, False) == history_distribution(p, True)
    e = Fraction(1, 10)
    delta0 = Fraction(1, 2)
    threshold = Fraction(1, 4)
    assert e < threshold < delta0 - e
    tail_bound = math.exp(-2 * 100 * float(threshold - e) ** 2)
    result = {
        'status': 'passed',
        'scope': 'Exact finite toy checks, not an experience assay, subject count, empirical evidence, or proof of metaphysical possibility.',
        'grid_checks': grid,
        'adaptive_two_stage_policies_checked': len(policies),
        'construction': 'Same controlled physical/output kernel, one common token vs two distinct tokens with equal local quality; common realizations coupled.',
        'illustration': {'total_report_error_bound': str(e), 'duplicate_disagreement_lower_bound': str(delta0),
                         'shared_observed_upper': str(e), 'duplicate_observed_lower': str(delta0-e),
                         'decision_threshold': str(threshold), 'independent_trials': 100,
                         'per_hypothesis_hoeffding_error_upper': tail_bound,
                         'note': 'All numbers hypothetical; bound excludes calibration/model failure.'},
    }
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(f"PASS: {sum(x['budget_triplets'] for x in grid)} sharp grid cases; {len(policies)} adaptive policies")
    print(f"Hypothetical per-hypothesis iid Hoeffding error <= {tail_bound:.6f}")
    print('No empirical consciousness or subject-count claim.')


if __name__ == '__main__':
    main()
