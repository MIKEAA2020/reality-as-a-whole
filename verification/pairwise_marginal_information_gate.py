#!/usr/bin/env python3
"""Finite examples of what singleton and pairwise marginals do not determine.

Standard parity and marginal-polytope counterexamples, not discoveries or data.
The latter reproduces Wainwright and Jordan, section 4.1.1, Example 4.1.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import math

STATES = list(product((0, 1), repeat=3))
PAIRS = list(combinations(range(3), 2))


def parity_law(a):
    return {x: (1 + a * (-1 if sum(x) % 2 else 1)) / 8 for x in STATES}


def marginal(p, indices):
    return {y: sum(v for x, v in p.items() if tuple(x[i] for i in indices) == y)
            for y in product((0, 1), repeat=len(indices))}


def entropy(p):
    return -sum(float(v) * math.log2(float(v)) for v in p.values() if v)


def kl(p, q):
    return sum(float(v) * math.log2(float(v / q[x])) for x, v in p.items() if v)


uniform = parity_law(F(0))
rows = []
for a in (F(0), F(1, 2), F(1)):
    p = parity_law(a)
    assert sum(p.values()) == 1 and min(p.values()) >= 0
    for indices in [(0,), (1,), (2,), *PAIRS]:
        assert marginal(p, indices) == marginal(uniform, indices)
    even = sum(v for x, v in p.items() if sum(x) % 2 == 0)
    tv = sum(abs(p[x] - uniform[x]) for x in STATES) / 2
    assert even == (1 + a) / 2 and tv == a / 2
    assert math.isclose(kl(p, uniform), 3 - entropy(p), abs_tol=1e-12)
    rows.append({'parity_bias': str(a), 'P_even': str(even),
                 'total_variation_from_uniform': str(tv),
                 'entropy_bits': entropy(p), 'KL_to_uniform_bits': kl(p, uniform)})

# Reproduce Wainwright–Jordan's local-consistency counterexample on a triangle.
beta = {(0, 1): F(2, 5), (1, 2): F(2, 5), (0, 2): F(1, 10)}
for b in beta.values():
    mat = [[b, F(1, 2) - b], [F(1, 2) - b, b]]
    assert sum(map(sum, mat)) == 1 and min(map(min, mat)) >= 0
    assert all(sum(row) == F(1, 2) for row in mat)
    assert all(sum(row[j] for row in mat) == F(1, 2) for j in (0, 1))
# The equalities 01 and 12 imply 02, so P(01 unequal)+P(12 unequal)
# must be at least P(02 unequal) under any joint probability law.
p_unequal_01 = 1 - 2 * beta[(0, 1)]
p_unequal_12 = 1 - 2 * beta[(1, 2)]
p_unequal_02 = 1 - 2 * beta[(0, 2)]
assert p_unequal_02 > p_unequal_01 + p_unequal_12

out = {'status': 'passed', 'scope': 'exact finite toy distributions, not retinal data or subject evidence',
       'single_and_pairwise_marginals': 'identical uniform singleton and pair distributions for every listed law',
       'laws': rows,
       'triangle_pseudomarginal': {'source': 'Wainwright and Jordan, Section 4.1.1, Example 4.1',
           'P_01_unequal': str(p_unequal_01), 'P_12_unequal': str(p_unequal_12),
           'P_02_unequal': str(p_unequal_02), 'global_probability_law_exists': False},
       'limitations': 'Parity example does not model retina; higher-order data can distinguish its distributions. Local-consistency example is not a causal or physical impossibility result outside its stated probability model.'}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
