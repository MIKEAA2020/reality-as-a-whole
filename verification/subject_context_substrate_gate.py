#!/usr/bin/env python3
"""Conditional finite gate: local organization, context, boundaries and detection.

Toy interventions and subject labels are stipulated, not neuroscience or proof
of experience. Fraction arithmetic establishes the finite transition claims.
"""
from fractions import Fraction
from itertools import product
from math import ceil, log, log1p
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BITS = (0, 1)


def kernel(x, y, i, j, epsilon):
    # x' = x XOR i; y' = y XOR j XOR (x AND noise)
    # noise is an independent Bernoulli(epsilon) at this local step.
    out = {}
    for noise, prob in ((0, 1 - epsilon), (1, epsilon)):
        s = (x ^ i, y ^ j ^ (x & noise))
        out[s] = out.get(s, Fraction(0)) + prob
    return {s: p for s, p in out.items() if p}


def marginal_x(dist):
    return {v: sum(p for (a, _), p in dist.items() if a == v) for v in BITS}


def prob_y1(dist):
    return sum(p for (_, b), p in dist.items() if b == 1)


def tv(p, q):
    return sum(abs(p.get(s, 0)-q.get(s, 0)) for s in p.keys() | q.keys()) / 2


base_eps = Fraction(0)
values = [Fraction(0), Fraction(1, 100), Fraction(1, 10000)]
checks = 0
rows = []
for eps in values:
    distances = []
    for x, y, i, j in product(BITS, repeat=4):
        base = kernel(x, y, i, j, base_eps)
        changed = kernel(x, y, i, j, eps)
        assert marginal_x(base) == marginal_x(changed)
        assert marginal_x(changed)[x ^ i] == 1
        distances.append(tv(base, changed))
        checks += 1
    assert max(distances) == eps
    # Maximum absolute effect of ideal do-clamps, over fixed backgrounds.
    influence_xy = max(abs(prob_y1(kernel(1, y, i, j, eps)) -
                           prob_y1(kernel(0, y, i, j, eps)))
                       for y, i, j in product(BITS, repeat=3))
    influence_yx = max(abs(marginal_x(kernel(x, 1, i, j, eps))[1] -
                           marginal_x(kernel(x, 0, i, j, eps))[1])
                       for x, i, j in product(BITS, repeat=3))
    assert influence_xy == eps and influence_yx == 0
    # Compute weak components of the inferred positive-influence graph.
    adjacency = {'x': set(), 'y': set()}
    if influence_xy > 0 or influence_yx > 0:
        adjacency['x'].add('y')
        adjacency['y'].add('x')
    components, remaining = [], set(adjacency)
    while remaining:
        stack, seen = [min(remaining)], set()
        while stack:
            node = stack.pop()
            if node not in seen:
                seen.add(node)
                stack.extend(adjacency[node] - seen)
        components.append(sorted(seen))
        remaining -= seen
    selected_x = ['x'] in components
    assert selected_x == (eps == 0)
    rows.append({'epsilon': str(eps), 'max_joint_tv_from_zero': str(max(distances)),
                 'directed_influence_x_to_y': str(influence_xy),
                 'directed_influence_y_to_x': str(influence_yx),
                 'stipulated_weak_components': components,
                 'x_is_selected_singleton': selected_x})

# Ideal repeated controlled preparation x=1,y=0,i=j=0: zero-change model
# has no positive outcomes, changed model is independent Bernoulli(epsilon).
epsilon = Fraction(1, 10000)
n = 1000
all_zero_probability = (1 - epsilon) ** n
bayes_equal_prior_error = all_zero_probability / 2
minimax_error = all_zero_probability / (1 + all_zero_probability)
n_95 = ceil(log(0.05) / log1p(-float(epsilon)))
assert (1-float(epsilon))**n_95 <= 0.05
assert (1-float(epsilon))**(n_95-1) > 0.05
result = {
    'scope': 'Stipulated finite classical kernels and idealized inference. Component-to-subject identity and experiential bridge are not established; no claim about actual systems or metaphysical possibility.',
    'transition_state_input_comparisons': checks,
    'rows': rows,
    'ideal_repeated_detection': {
        'epsilon': str(epsilon), 'independent_trials': n,
        'no_positive_outcomes_given_positive_epsilon': float(all_zero_probability),
        'optimal_equal_prior_bayes_error': float(bayes_equal_prior_error),
        'optimal_minimax_error_with_randomized_decision': float(minimax_error),
        'trials_for_at_least_95_percent_chance_of_one_positive': n_95,
        'scope': 'Known exactly zero versus known epsilon; perfect preparations/readout; independent trials; n_95 is power for an any-positive rule with zero false positives, not a general confidence bound or human study recommendation.'
    }
}
(ROOT / 'verification/subject_context_substrate_gate.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
