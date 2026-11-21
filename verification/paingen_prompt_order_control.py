#!/usr/bin/env python3
"""Exact prompt-order control from a public task source; no participant outcomes."""
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

N_ROWS = 16
N_PAIN = 8
N_FIRST = 8


def enumerate_orders():
    # MATLAB indices 2,4,...,16 are painful; Python indices are 1,3,...,15.
    pain_slots = set(range(1, N_ROWS, 2))
    assert len(pain_slots) == N_PAIN and N_FIRST == N_ROWS//2
    counts = Counter()
    for selected in itertools.combinations(range(N_ROWS), N_FIRST):
        intensity_first = set(selected)
        assert len(intensity_first) == N_FIRST
        # Every painful slot receives one of two explicit, nonempty prompt orders.
        for slot in pain_slots:
            order = ('intensity', 'unpleasantness') if slot in intensity_first else ('unpleasantness', 'intensity')
            assert len(order) == 2 and set(order) == {'intensity', 'unpleasantness'}
        counts[len(pain_slots & intensity_first)] += 1
    return counts


def exact_summary(counts):
    total = sum(counts.values())
    probs = {k: Fraction(counts[k], total) for k in range(9)}
    mean = sum((k*p for k, p in probs.items()), Fraction())
    variance = sum(((k-mean)**2*p for k, p in probs.items()), Fraction())
    return {'count_table': {str(k): counts[k] for k in range(9)},
            'total': total, 'mean': str(mean), 'variance': str(variance),
            'prob_exactly_four': str(probs[4]),
            'prob_three_to_five': str(sum((probs[k] for k in (3,4,5)), Fraction())),
            'prob_all_same': str(probs[0]+probs[8]),
            'independent_fair_coin_variance': '2',
            'independent_fair_coin_prob_all_same': str(Fraction(2, 2**8))}


def main():
    counts = enumerate_orders()
    assert sum(counts.values()) == math.comb(16,8)
    assert all(counts[k] == math.comb(8,k)*math.comb(8,8-k) for k in range(9))
    result = {'scope': 'exact combinatorial control, not participant data or a randomization audit',
              'task_source_repository': 'canlab/Paradigms_Public',
              'task_source_commit': '89ec44cc82d09a6cddced6e7fcf2dd73c8a87281',
              'task_generator_blob_git_sha1': '8df967543bb5e4d72fdd3ce975cee9b97b64a9cc',
              'results': exact_summary(counts)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
