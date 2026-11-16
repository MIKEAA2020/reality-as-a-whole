#!/usr/bin/env python3
"""Four-spin graph margin and ideal measurement budget; not subject evidence."""
from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, exp, log
import json
from pathlib import Path

from causal_influence_subject_gate import influence_graph, score
from competing_subject_constitution_rules import connected_components, overlapping_local_maxima, lists

ROOT = Path(__file__).resolve().parent.parent
V = frozenset(range(4))
_, base = influence_graph(F(1, 4))
outer = ((0,1),(2,3))
middle = (1,2)
nonedges = ((0,2),(0,3),(1,3))
edges = ((0,1), middle, (2,3))
assert [base[x] for x in edges] == [F(10,21), F(4,21), F(10,21)]
assert all(base[e] == 0 for e in nonedges)
subsets = [frozenset(s) for k in range(2, 5) for s in combinations(sorted(V), k)]
outer_sets = {frozenset(e) for e in outer}
assert len(subsets) == 11
assert all(score(s, base) <= F(4,21) for s in subsets if s not in outer_sets)
assert all(score(s, base) == F(10,21) for s in outer_sets)

eta = F(1,20)
assert eta < F(2,35)
checks = 0
for edge_deltas in product((-eta, F(0), eta), repeat=3):
    for additions in product((F(0), eta/2, eta), repeat=3):
        pair = dict(base)
        for e, d in zip(edges, edge_deltas): pair[e] += d
        for e, d in zip(nonedges, additions): pair[e] += d
        c = connected_components(V, pair)
        l, ties = overlapping_local_maxima(V, pair)
        assert lists(c) == [[0,1,2,3]]
        assert lists(l) == [[0,1],[2,3]] and not ties
        checks += 1
assert checks == 729

# The all-six-edges L-infinity radius is sharp: construct an exact tie at 2/35.
tight = F(2,35)
boundary = dict(base)
for e in outer: boundary[e] -= tight
boundary[middle] += tight
for e in nonedges: boundary[e] += tight
assert score({0,1}, boundary) == score({2,3}, boundary) == score(V, boundary) == F(44,105)
c = connected_components(V,boundary)
l, ties = overlapping_local_maxima(V,boundary)
assert lists(c) == [[0,1,2,3]] and not l
assert {frozenset((0,1)), frozenset((2,3)), V} <= ties

# Cell probabilities: true vs observed bias b, sample fluctuation lambda.
# Clamped minimum of two directional differences is 1-Lipschitz in l-infinity;
# differences of two cells incur at most twice a cell error.
physical_drift = F(1,100)
clamp_bias = F(1,400)
readout_bias = F(1,400)
sampling = F(3,200)
combined = physical_drift + 2*(clamp_bias + readout_bias + sampling)
assert combined == eta and combined < tight
cells = 24  # 4*3 directed pairs, two intervention signs
alpha = .05
n = ceil(log(2*cells/alpha) / (2*float(sampling)**2))
failure = 2*cells*exp(-2*n*float(sampling)**2)
assert failure <= alpha
assert 2*cells*exp(-2*(n-1)*float(sampling)**2) > alpha

# Keep finite-horizon record error mathematically separate from the influence
# edge budget; one does not imply the other.
horizon = 100
row_error = F(1,10000)
path_bound = 1 - (1-row_error)**horizon
result = {
  'scope': 'Stipulated finite classical edge scores, controlled Bernoulli measurements and independently assumed kernel bound. No real subjects, neuroscience, phenomenology, data or quantum-gravity derivation.',
  'all_six_edge_certificate': {'sharp_linf_radius': '2/35 (strict)',
      'radius_tested': str(eta), 'grid_cases_checked': checks,
      'tie_witness_at_boundary': {'pair_score': '44/105', 'whole_score': '44/105',
         'L_winners': lists(l), 'L_unresolved': lists(ties), 'C': lists(c)}},
  'illustrative_measurement_budget': {
      'number_of_cells': cells, 'physical_weight_drift': str(physical_drift),
      'clamp_bias_per_cell': str(clamp_bias), 'readout_bias_per_cell': str(readout_bias),
      'sampling_error_per_cell': str(sampling), 'combined_weight_error': str(combined),
      'iid_trials_per_cell_hoeffding': n, 'total_trials': n*cells,
      'simultaneous_failure_upper_bound': failure,
      'assumptions': 'Cellwise iid bounded outcomes, controlled backgrounds, independently justified deterministic bias bounds and true graph-drift bound; correlations across cells allowed by union bound.'},
  'independent_horizon_assumption': {'horizon_steps': horizon,
      'uniform_full_kernel_row_tv': str(row_error), 'path_tv_upper_bound': float(path_bound),
      'scope': 'Separate uniform kernel assumption; graph weights and graph estimation do not establish it.'}
}
(ROOT/'verification/four_spin_hidden_edge_robustness.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
