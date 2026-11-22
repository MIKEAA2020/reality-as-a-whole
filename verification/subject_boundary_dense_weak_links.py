#!/usr/bin/env python3
"""Check an existing min-cut selector under many weak cross-edges.

Abstract symmetric weighted graphs, not empirical brains, subjects, or IIT.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


@lru_cache(maxsize=None)
def type_score(a, b, m, epsilon):
    """Unnormalized induced minimum cut of a nodes from A, b from B."""
    epsilon = F(epsilon)
    if m < 2 or not (0 <= a <= m and 0 <= b <= m and a+b >= 2 and epsilon >= 0):
        raise ValueError('invalid graph or subset')
    cuts = []
    for i, j in product(range(a+1), range(b+1)):
        if i+j == 0 or i+j == a+b:
            continue
        cuts.append(F(i*(a-i) + j*(b-j)) + epsilon*(i*(b-j) + (a-i)*j))
    return min(cuts)


def classify_scores(scores):
    """Existing overlap-local competition: strict winners and unresolved ties."""
    groups = defaultdict(list)
    for mask, score in scores.items():
        if score > 0:
            groups[score].append(mask)
    above = 0
    winners, ties = set(), set()
    for value in sorted(groups, reverse=True):
        group = groups[value]
        counts = Counter(bit for mask in group for bit in range(mask.bit_length()) if mask & (1 << bit))
        for mask in group:
            if mask & above:
                continue
            has_tie = any(counts[bit] > 1 for bit in range(mask.bit_length()) if mask & (1 << bit))
            (ties if has_tie else winners).add(mask)
        for mask in group:
            above |= mask
    return frozenset(winners), frozenset(ties)


def analyze(m, epsilon, normalized=False):
    eps = F(epsilon)
    if m < 2 or eps < 0:
        raise ValueError('invalid graph')
    candidates = {}
    for mask in range(1, 1 << (2*m)):
        size = mask.bit_count()
        if size < 2:
            continue
        a = (mask & ((1 << m)-1)).bit_count()
        b = size - a
        value = type_score(a,b,m,eps)
        candidates[mask] = value/size if normalized else value
    return classify_scores(candidates)


def members(mask, n):
    return [i for i in range(n) if mask & (1 << i)]


def main():
    rows=[]
    for m in (3,4,6):
        full = (1 << (2*m))-1
        cores = frozenset(((1 << m)-1, ((1 << m)-1) << m))
        for label, eps in (('sparse_total',F(1,2*m)), ('many_weak',F(1,m)), ('uniform',F(1))):
            for normalized in (False,True):
                winners,ties = analyze(m,eps,normalized)
                if label == 'sparse_total' or (label == 'many_weak' and normalized):
                    assert winners == cores and not ties
                else:
                    assert winners == frozenset((full,)) and not ties
                rows.append({'m':m, 'regime':label, 'cross_edge':str(eps),
                    'score':'mincut / subset size' if normalized else 'unnormalized mincut',
                    'core_score':str(F(m-1, m) if normalized else F(m-1)),
                    'whole_score':str(type_score(m,m,m,eps)/(2*m) if normalized else type_score(m,m,m,eps)),
                    'winner_supports':[members(mask,2*m) for mask in sorted(winners)],
                    'unresolved_support_count':len(ties)})
    data={'scope':'Exact abstract weighted-graph exercise, not physiological influence, subject counts or IIT.',
          'blocks':'Two size-m complete graphs of within-edge weight 1, all cross-edges weight epsilon.',
          'cases':rows,
          'closed_form_m_ge_3':{'epsilon_1_over_2m':'Both selectors choose two cores.',
                'epsilon_1_over_m':'Unnormalized chooses whole; size-normalized chooses two cores.',
                'epsilon_1':'Both choose whole.',
                'cross_edge_to_within_edge':'1/m', 'cross_total_to_within_total':'1/(m-1)',
                'unnormalized_whole_vs_any_other_gap_lower_bound':'1/m',
                'sufficient_uniform_edge_perturbation_radius':'eta < 1/(2*m^3)'}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__ == '__main__': main()
