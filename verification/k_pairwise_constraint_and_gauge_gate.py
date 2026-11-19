#!/usr/bin/env python3
"""Exact counterexample for K-pairwise constraints; reproduce published gauge freedom.

A finite diagnostic, not a claim about a particular experiment or a new theorem.
Gauge freedom is explicitly discussed by Tkacik et al., DOI 10.1371/journal.pcbi.1003408.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import math

N = 4
STATES = list(product((0, 1), repeat=N))
PAIRS = list(combinations(range(N), 2))
# Null direction of the matrix of normalization, singleton, pair and K counts.
delta = {
    (0, 1, 0, 0): -1, (0, 1, 0, 1): 1,
    (0, 1, 1, 0): 1,  (0, 1, 1, 1): -1,
    (1, 0, 0, 0): 1,  (1, 0, 0, 1): -1,
    (1, 0, 1, 0): -1, (1, 0, 1, 1): 1,
}
base = {x: F(1, 16) for x in STATES}
plus = {x: base[x] + F(delta.get(x, 0), 32) for x in STATES}
minus = {x: base[x] - F(delta.get(x, 0), 32) for x in STATES}


def mean(p, f):
    return sum(v * f(x) for x, v in p.items())


def entropy(p):
    return -sum(float(v) * math.log2(float(v)) for v in p.values())


def expectation_fingerprint(p):
    return [mean(p, lambda x, i=i: x[i]) for i in range(N)] + [
        mean(p, lambda x, i=i, j=j: x[i] * x[j]) for i, j in PAIRS] + [
        mean(p, lambda x, k=k: int(sum(x) == k)) for k in range(N + 1)]

for p in (base, plus, minus):
    assert sum(p.values()) == 1 and min(p.values()) > 0
assert expectation_fingerprint(plus) == expectation_fingerprint(minus) == expectation_fingerprint(base)
triplet = lambda x: x[0] * x[2] * x[3]
p3, m3 = mean(plus, triplet), mean(minus, triplet)
assert p3 == F(5, 32) and m3 == F(3, 32)
tv = sum(abs(plus[x] - minus[x]) for x in STATES) / 2
assert tv == F(1, 4)
# Uniform has largest possible entropy on 16 states; it satisfies the common
# constraints, so it is the unique maximum-entropy joint distribution.
assert entropy(plus) < entropy(base) and entropy(minus) < entropy(base)

# Write log weight as h.x + sum J_ij x_i x_j + V(K), not minus energy.
h = [F(1, 10), F(-1, 5), F(3, 10), F(-2, 5)]
j = {pair: F(i - 2, 11) for i, pair in enumerate(PAIRS)}
v = [F(k * k, 9) for k in range(N + 1)]
a, b = F(2, 7), F(-3, 8)


def score(x, fields, pairs, potential):
    return sum(fields[i] * x[i] for i in range(N)) + sum(
        pairs[i, j] * x[i] * x[j] for i, j in PAIRS) + potential[sum(x)]

h2 = [z + a for z in h]
j2 = {pair: value + b for pair, value in j.items()}
v2 = [v[k] - a * k - b * F(k * (k - 1), 2) for k in range(N + 1)]
assert h != h2 and j != j2 and v != v2
assert all(score(x, h, j, v) == score(x, h2, j2, v2) for x in STATES)

out = {'status': 'passed', 'scope': 'four-bit exact example, not a retinal fit or biological test',
       'constraints': 'all single-site means, all pairwise coincidences, and the complete distribution of total K',
       'all_joint_states_strictly_positive': True,
       'same_constraints_different_joint': {'P_plus_all_ones_on_indices_0_2_3': str(p3),
           'P_minus_all_ones_on_indices_0_2_3': str(m3),
           'total_variation': str(tv), 'entropy_plus_bits': entropy(plus),
           'entropy_minus_bits': entropy(minus), 'constraint_maxent_uniform_entropy_bits': entropy(base)},
       'gauge': {'published_antecedent': 'Tkacik et al., K-pairwise parametrization methods, DOI 10.1371/journal.pcbi.1003408',
           'field_shift': str(a), 'pair_shift': str(b),
           'potential_adjustment': '-a*K-b*K*(K-1)/2',
           'log_weights_identical_on_all_states': True},
       'limitations': 'Special feasible constraints and uniform MaxEnt baseline; no general bound on error; all triplets are not equal; constraints and phenomenology are not causal mechanisms.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
