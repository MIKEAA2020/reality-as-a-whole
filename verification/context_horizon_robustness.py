#!/usr/bin/env python3
"""Finite operational horizon checks; no inference to experience or ontology."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import ceil, log, log1p
import json
from pathlib import Path

from causal_influence_subject_gate import influence_graph
from competing_subject_constitution_rules import connected_components, overlapping_local_maxima, lists

ROOT = Path(__file__).resolve().parent.parent


def latent_kernel(state, eps):
    x, y = state
    x_next = x ^ y
    result = defaultdict(F)
    for noise, p in ((0, 1-eps), (1, eps)):
        result[(x_next, y | noise)] += p
    return {s: p for s, p in result.items() if p}


def tv(p, q):
    return sum(abs(p.get(k, 0)-q.get(k, 0)) for k in p.keys() | q.keys()) / 2


def observed_paths(n, eps):
    # Exact finite distribution over output histories (x_0,...,x_n).
    dist = {(0, 0, (0,)): F(1)}
    for _ in range(n):
        next_dist = defaultdict(F)
        for (x, y, path), mass in dist.items():
            for (nx, ny), prob in latent_kernel((x, y), eps).items():
                next_dist[(nx, ny, path + (nx,))] += mass * prob
        dist = next_dist
    outputs = defaultdict(F)
    for (x, y, path), mass in dist.items():
        outputs[path] += mass
    assert sum(outputs.values()) == 1
    return dict(outputs)


# Full kernel discrepancy is exactly eps, but local output depends on delayed
# activation. Compare all output histories for small horizons exactly.
eps = F(1, 10)
states = [(x, y) for x in (0, 1) for y in (0, 1)]
distances = [tv(latent_kernel(s, F(0)), latent_kernel(s, eps)) for s in states]
assert max(distances) == eps
path_cases = 0
for n in range(1, 13):
    base, changed = observed_paths(n, F(0)), observed_paths(n, eps)
    exact = 1-(1-eps)**(n-1)
    assert tv(base, changed) == exact
    assert exact <= 1-(1-eps)**n <= n*eps
    path_cases += 1

# Uniformly contractive endpoint example: Bernoulli(1/4+x/2) vs
# Bernoulli(1/4+delta+x/2). Propagate P(X_n=1) exactly.
delta = F(1, 100)
a = F(1, 2)
p = q = F(0)
for n in range(1, 21):
    p = F(1, 4) + a*p
    q = F(1, 4) + delta + a*q
    exact_gap = delta*(1-a**n)/(1-a)
    assert q-p == exact_gap and exact_gap < delta/(1-a)
assert (F(3,4)-F(1,4)) == a
assert F(3,4)+delta <= 1

# Reuse the frozen four-spin influence graph and its actual C and L rules.
# Under fixed chain topology, all three edge weights may vary within eta.
_, pair = influence_graph(F(1, 4))
edges = ((0,1), (1,2), (2,3))
assert [pair[e] for e in edges] == [F(10,21), F(4,21), F(10,21)]
active = frozenset(range(4))
eta = F(1, 8)  # less than (outer-middle)/2 = 1/7
checks = 0
for offsets in product((-eta, F(0), eta), repeat=3):
    changed = dict(pair)
    for edge, offset in zip(edges, offsets):
        changed[edge] += offset
    c = connected_components(active, changed)
    l, ties = overlapping_local_maxima(active, changed)
    assert lists(c) == [[0,1,2,3]]
    assert lists(l) == [[0,1], [2,3]] and not ties
    checks += 1
# At the limiting radius, all three edges can tie and L is unresolved.
boundary = dict(pair)
for edge, offset in zip(edges, (-F(1,7), F(1,7), -F(1,7))):
    boundary[edge] += offset
l, ties = overlapping_local_maxima(active, boundary)
assert not l and len(ties) == 6

small = F(1, 10000)
large_horizons = [1, 2, 1001, 10001, 29957]
rows = []
for n in large_horizons:
    # Closed form is exact; display only a rounded floating-point value.
    difference = 1 - (1-small)**(n-1)
    rows.append({'updates': n, 'local_history_tv': float(difference)})
assert rows[-1]['local_history_tv'] >= 0.95
first_95 = 1 + ceil(log(.05)/log1p(-float(small)))
assert first_95 == 29957
result = {
    'scope': 'Finite stipulated classical stochastic models, not a subject, experience, empirical data, physical laws, fundamental time, or evidence for metaphysical possibility.',
    'latent_model': {'epsilon': '1/10000', 'one_step_full_kernel_sup_tv': '1/10000',
                     'exact_local_history_tv': '1-(1-epsilon)^(n-1), n>=1',
                     'small_horizon_exact_distribution_checks': path_cases,
                     'large_horizon_values': rows,
                     'first_horizon_reaching_95_percent': first_95},
    'contraction_model': {'delta': str(delta), 'dobrushin_coefficient': str(a),
                          'endpoint_gap_after_n': 'delta*(1-a^n)/(1-a)',
                          'endpoint_gap_limit': str(delta/(1-a)),
                          'exact_endpoint_checks': 20},
    'four_spin_fixed_topology': {'original_weights': [str(pair[e]) for e in edges],
                                 'edge_error_radius_checked': str(eta),
                                 'perturbation_combinations_checked': checks,
                                 'C_selected': [[0,1,2,3]], 'L_selected': [[0,1],[2,3]],
                                 'strict_radius_certificate': 'eta < 1/7',
                                 'L_unresolved_candidates_at_radius_1_over_7': len(ties),
                                 'scope': 'Uncertainty in abstract edge weights with fixed zero nonedges, not physical-kernel reconstruction or an experience assay.'},
    'note': 'Bounds concern specified physical record distributions; mapping them to phenomenal equivalence requires additional premises.'
}
(ROOT / 'verification/context_horizon_robustness.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
