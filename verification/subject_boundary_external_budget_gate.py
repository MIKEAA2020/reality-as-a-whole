#!/usr/bin/env python3
"""Finite graph checks for a stipulated subject-selector; no phenomenal inference."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json

from causal_influence_subject_gate import influence_graph, score
from competing_subject_constitution_rules import overlapping_local_maxima, lists

ROOT = Path(__file__).resolve().parent.parent
CORE = frozenset((0, 1))


def graph(n, default=F(0)):
    return {e: default for e in combinations(range(n), 2)}


def leakage(core, pair):
    return sum((w for (i, j), w in pair.items() if (i in core) != (j in core)), F(0))


def cycle(d):
    p = graph(4)
    p[(0, 1)] = F(1)
    p[(0, 2)] = p[(1, 3)] = p[(2, 3)] = d
    return p


# Exhaust every graph with five edges in {0,1/4,1/2,3/4,1}, core edge fixed to 1.
values = [F(i, 4) for i in range(5)]
edges = [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
checked = certified = 0
for weights in product(values, repeat=len(edges)):
    p = graph(4)
    p[(0, 1)] = F(1)
    p.update(zip(edges, weights))
    d = leakage(CORE, p)
    win, ties = overlapping_local_maxima(range(4), p)
    checked += 1
    if d < 1:
        assert CORE in win and CORE not in ties
        certified += 1

# Exact strictness witness for the total-leakage threshold, not for other scores.
cycle_rows = []
for d in [F(49, 100), F(1, 2), F(51, 100)]:
    p = cycle(d)
    win, ties = overlapping_local_maxima(range(4), p)
    full = frozenset(range(4))
    full_score = score(full, p)
    assert full_score == 2*d and leakage(CORE, p) == 2*d
    if d < F(1, 2):
        assert CORE in win and CORE not in ties
    elif d == F(1, 2):
        assert CORE in ties and full in ties
    else:
        assert win == {full} and CORE not in ties
    cycle_rows.append({'each_cross_and_outer_edge': str(d), 'leakage': str(2*d),
                       'full_score': str(full_score), 'winners': lists(win),
                       'unresolved': lists(ties)})

# Same fixed four-spin target previously studied; add no hidden vertices.
_, base = influence_graph(F(1, 4))
assert base[(0, 1)] == F(10, 21) and leakage(CORE, base) == F(4, 21)
assert base[(2, 3)] == F(10, 21) and leakage(frozenset((2, 3)), base) == F(4, 21)

# Dense weak links: k outsiders, all edges epsilon except strong core.
# Verify every proper competitor score for two finite k values.
dense_rows = []
for k in (4, 8):
    eps = F(1, k)
    p = graph(k+2, eps)
    p[(0, 1)] = F(1)
    full = frozenset(range(k+2))
    full_score = score(full, p)
    assert full_score == (k+1)*eps > 1
    subsets_checked = 0
    for size in range(2, k+2):
        for subset in combinations(range(k+2), size):
            s = frozenset(subset)
            expected = F(1) if s == CORE else (size-1)*eps
            assert score(s, p) == expected < full_score
            subsets_checked += 1
    dense_rows.append({'outsiders': k, 'per_added_edge': str(eps),
                       'full_score': str(full_score), 'core_leakage': str(leakage(CORE,p)),
                       'proper_candidates_checked': subsets_checked})

out = {
    'status': 'passed',
    'scope': 'Finite nonnegative weighted graph and stipulated min-cut selector; not IIT, QFT, a brain, evidence of subjects, or an experiential measurement.',
    'four_node_exhaustion': {'edge_values': [str(v) for v in values], 'graphs_checked': checked,
                             'certified_by_D_less_than_w': certified},
    'sharp_cycle_witness': cycle_rows,
    'existing_four_spin_target': {'core_score': '10/21', 'leakage_each_outer_pair': '4/21',
                                  'remaining_budget_each': '2/7'},
    'weak_edge_many_outsiders': dense_rows,
    'limitations': 'Graph weights assumed fixed under extension; nonnegative finite graph. Does not derive influence graph from interventions or establish physical relevance.'
}
(ROOT/'verification/subject_boundary_external_budget_gate.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
