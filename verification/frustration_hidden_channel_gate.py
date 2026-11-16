#!/usr/bin/env python3
"""Tests of a conditional triangle certificate, dilution, and hidden-channel ambiguity.

No neuroscience or phenomenal data. The proof is in the associated report; random
checks do not establish it. Uses Python stdlib only.
"""
import json
import math
import random
from fractions import Fraction
from pathlib import Path

PI = math.pi
EDGES = ((0, 1), (1, 2), (2, 0))
def wrap(x):
    return (x + PI) % (2 * PI) - PI

def cycle_distance(a):
    return abs(wrap(sum(a)))

def energy(phi, a, k):
    return sum(w * (1 - math.cos(phi[i] - phi[j] - off))
               for (i, j), off, w in zip(EDGES, a, k))

def equal_residual_phases(a):
    r = wrap(-sum(a)) / 3
    p0 = 0.0
    p1 = p0 - a[0] - r
    p2 = p1 - a[1] - r
    return (p0, p1, p2)

def grad(phi, a, k):
    g = [0.0] * 3
    for (i, j), off, w in zip(EDGES, a, k):
        t = w * math.sin(phi[i] - phi[j] - off)
        g[i] += t
        g[j] -= t
    return g

r = random.Random(50261)
num = 5000
min_slack = float('inf')
max_gauge_error = 0.0
max_cancel_error = 0.0
for _ in range(num):
    a = [PI + r.uniform(-PI/12, PI/12) for _ in EDGES]
    k = [r.uniform(0.9, 1.1) for _ in EDGES]
    phi = [r.uniform(-PI, PI) for _ in range(3)]
    theta = [r.uniform(-PI, PI) for _ in range(3)]
    d = cycle_distance(a)
    assert d + 1e-12 >= 3*PI/4
    lower = 2 * min(k) * d*d / (3 * PI*PI)
    v = energy(phi, a, k)
    assert v + 1e-12 >= lower >= 27/80 - 1e-12
    min_slack = min(min_slack, v - lower)
    candidate = energy(equal_residual_phases(a), a, k)
    upper = 3 * max(k) * (1 - math.cos(d/3))
    assert candidate <= upper + 1e-12
    aa = [a[e] + theta[i] - theta[j] for e, (i, j) in enumerate(EDGES)]
    pp = [phi[i] + theta[i] for i in range(3)]
    max_gauge_error = max(max_gauge_error, abs(energy(pp, aa, k)-v),
                          abs(cycle_distance(aa)-d))
    # Each pair has two independent, equally weighted 0 and pi channels.
    ant = energy(phi, [PI]*3, [1]*3)
    align = energy(phi, [0]*3, [1]*3)
    ga, gb = grad(phi, [PI]*3, [1]*3), grad(phi, [0]*3, [1]*3)
    err = max(abs(ant+align-6), *(abs(x+y) for x,y in zip(ga,gb)))
    max_cancel_error = max(max_cancel_error, err)
    assert err < 1e-12
assert max_gauge_error < 1e-12
# Exact, analytic triangle and normalization example, not numerical optimization.
F_triangle = Fraction(3,2)
F_double = Fraction(6)
D_triangle_at_zero = Fraction(6)-F_triangle
D_double_at_zero = Fraction(6)-F_double
assert (D_triangle_at_zero, D_double_at_zero) == (Fraction(9,2), Fraction(0))
N = 100
normalized = F_triangle / (3 + N)
assert normalized == Fraction(3,206)
report = {
    'status': 'passed',
    'scope': 'classical finite phase-cost models only; conditional bounds not empirical evidence or experience assay',
    'sampled_triangle_graphs_and_states': num,
    'certified_triangle_and_any_nonnegative_extension_lower_bound': '27/80',
    'conditions': 'three unit-estimated weights each at least 9/10; each offset within pi/12 of pi; edges persist unchanged, extra costs nonnegative',
    'triangle_only_upper_bound': '33/20',
    'min_sampled_state_energy_minus_loop_lower_bound': min_slack,
    'max_gauge_reference_error': max_gauge_error,
    'max_equal_opposed_channel_cancellation_error': max_cancel_error,
    'original_antiphase_triangle_F': str(F_triangle),
    'original_state_excess_at_zero': str(D_triangle_at_zero),
    'doubled_opposite_channel_F': str(F_double),
    'doubled_state_excess_at_zero': str(D_double_at_zero),
    'pendant_edges_count': N,
    'normalized_F_after_100_unit_pendants': str(normalized),
    'phase_only_observational_equivalence': 'both opposed-channel and zero-interaction models have the same zero phase force for every phase assignment',
    'note': 'Floating-point random assertions are spot checks; general claims follow from the report proofs.'
}
out = Path(__file__).resolve().parent / 'frustration_hidden_channel_gate.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
