#!/usr/bin/env python3
"""Finite checks of strong persistency and moment-matrix eigenvalue claims.

Standard roof-duality / local-polytope concepts; see the associated report.
Exact arithmetic, no external solver, and no claim of novel general theorem.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

nodes = range(4)
triangle = [(1, 2), (2, 3), (1, 3)]
edges = [(0, 1), *triangle]  # The first edge has zero weight.


def integral_score(x):
    return sum(x[i] != x[j] for i, j in triangle)

states = list(product((0, 1), repeat=4))
best = max(integral_score(x) for x in states)
optimizers = [x for x in states if integral_score(x) == best]
assert best == 2 and len(optimizers) == 12
assert {x[0] for x in optimizers} == {0, 1}

single = {0: (Q(1), Q(0)), 1: (Q(1, 2), Q(1, 2)),
          2: (Q(1, 2), Q(1, 2)), 3: (Q(1, 2), Q(1, 2))}
pair = {(0, 1): ((Q(1, 2), Q(1, 2)), (Q(0), Q(0)))}
for edge in triangle:
    pair[edge] = ((Q(0), Q(1, 2)), (Q(1, 2), Q(0)))
for i in nodes:
    assert sum(single[i]) == 1 and all(v >= 0 for v in single[i])
for i, j in edges:
    mat = pair[i, j]
    assert sum(map(sum, mat)) == 1 and all(v >= 0 for row in mat for v in row)
    assert tuple(sum(row) for row in mat) == single[i]
    assert tuple(sum(mat[a][b] for a in (0, 1)) for b in (0, 1)) == single[j]
relaxed_score = sum(pair[i, j][0][1] + pair[i, j][1][0] for i, j in triangle)
assert relaxed_score == 3  # each normalized edge disagreement probability <= 1
assert any(x[0] == 0 for x in optimizers) and any(x[0] == 1 for x in optimizers)
# This fractional solution is also a vertex: it uniquely maximizes the
# exposing objective sum(edge disagreement)-P(X0=1). The bound is 3;
# equality forces every triangle edge to disagree and fixes X0 to 0.
# Pairwise consistency on an odd cycle then forces all triangle singletons
# to 1/2, and all pair tables (including 01) are uniquely determined.
assert relaxed_score - single[0][1] == 3

# With independent uniform binary X1,X2, all four joint atom probabilities
# are 1/4. The monomial moment matrix has a different trace, so these
# four probabilities cannot be its eigenvalues (eigenvalues sum to trace).
monomials = [lambda x: 1, lambda x: x[0], lambda x: x[1], lambda x: x[0] * x[1]]
xs = list(product((0, 1), repeat=2))
N = [[sum(Q(f(x) * g(x), 4) for x in xs) for g in monomials] for f in monomials]
assert N == [[Q(1), Q(1,2), Q(1,2), Q(1,4)],
             [Q(1,2), Q(1,2), Q(1,4), Q(1,4)],
             [Q(1,2), Q(1,4), Q(1,2), Q(1,4)],
             [Q(1,4), Q(1,4), Q(1,4), Q(1,4)]]
trace = sum(N[i][i] for i in range(4))
atom_probabilities = [Q(1,4)] * 4
assert trace == Q(9, 4) and sum(atom_probabilities) == 1 and trace != sum(atom_probabilities)
# The matrix is PSD by construction: for every vector c,
# c^T N c = E[(sum_i c_i monomials_i)^2] >= 0.

result = {
 'status': 'passed',
 'scope': 'two exact finite counterexamples, not a general roof-duality proof or empirical model',
 'lp_example': {'objective': 'sum of disagreements on edges 12, 23, 13; edge 01 has zero weight',
   'locally_consistent_fractional_lp_score': str(relaxed_score),
   'certified_lp_upper_bound': 3, 'exact_integer_optimum': best,
   'integer_optimizers': len(optimizers), 'integral_lp_label_x0': 0,
   'optimal_integer_x0_values': [0, 1], 'strong_persistency': False,
   'weak_persistency_for_this_point': True,
   'fractional_point_is_exposed_vertex': True,
   'vertex_certificate': 'unique maximizer of sum of triangle disagreements minus P(X0=1)'},
 'moment_example': {'uniform_binary_pair_atom_probabilities': [str(x) for x in atom_probabilities],
   'moment_matrix_trace': str(trace), 'sum_claimed_eigenvalues': str(sum(atom_probabilities)),
   'probabilities_are_eigenvalues': False, 'psd_by_gram_construction': True},
 'limitations': 'Counterexample to a literal strong-persistency wording under ties; not a failure of weak persistency. Does not challenge PSD/realizability equivalence under the correct congruence transformation.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
