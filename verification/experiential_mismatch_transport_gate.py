#!/usr/bin/env python3
"""Exact finite checks of a conditional calibration-transport bound.

No empirical data, experiential assay, subject constitution, or new statistics theorem.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def optimum(s, t, budget):
    """Fractional knapsack: zero-source cells first, then decreasing t/s."""
    f = [F(0) for _ in s]
    for i, p in enumerate(s):
        if p == 0:
            f[i] = F(1)
    rem = budget
    for i in sorted((i for i, p in enumerate(s) if p > 0),
                    key=lambda i: t[i] / s[i], reverse=True):
        f[i] = min(F(1), rem / s[i])
        rem -= s[i] * f[i]
    return sum((t[i] * f[i] for i in range(len(s))), F(0)), f


def dual(s, t, budget):
    lambdas = {F(0)} | {t[i] / s[i] for i in range(len(s)) if s[i] > 0}
    return min(lam * budget + sum((max(F(0), t[i] - lam * s[i])
                                  for i in range(len(s))), F(0))
               for lam in lambdas)


def vertex_max(s, t, budget):
    # Enumerate every box vertex with at most one fractional coordinate.
    # Also include all corners whose source cost is below budget.
    n = len(s)
    candidates = []
    for f in product((F(0), F(1)), repeat=n):
        if sum((s[i] * f[i] for i in range(n)), F(0)) <= budget:
            candidates.append(f)
    for j in range(n):
        if s[j] == 0:
            continue
        for bits in product((F(0), F(1)), repeat=n - 1):
            f = list(bits[:j]) + [F(0)] + list(bits[j:])
            rem = budget - sum((s[i] * f[i] for i in range(n)), F(0))
            f[j] = rem / s[j]
            if 0 <= f[j] <= 1:
                candidates.append(f)
    return max(sum((t[i] * f[i] for i in range(n)), F(0)) for f in candidates)


def dist(n=3, denom=4):
    for a in product(range(denom + 1), repeat=n):
        if sum(a) == denom:
            yield tuple(F(v, denom) for v in a)


def main():
    s, t, eps = (F(3, 4), F(1, 4)), (F(1, 4), F(3, 4)), F(1, 20)
    bound, f = optimum(s, t, eps)
    assert f == [0, F(1, 5)] and bound == F(3, 20)
    assert sum(s[i] * f[i] for i in range(2)) == eps
    assert dual(s, t, eps) == bound
    support, fs = optimum((F(1), F(0)), (F(1, 2), F(1, 2)), F(0))
    assert support == F(1, 2) and fs[1] == 1
    same, _ = optimum((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)), F(0))
    assert same == 0  # holds only if the conditional error kernel transports
    count = 0
    for a in dist():
        for b in dist():
            for e in (F(0), F(1, 8), F(1, 4), F(1, 2), F(1)):
                value, f = optimum(a, b, e)
                assert value == dual(a, b, e) == vertex_max(a, b, e)
                assert sum((a[i] * f[i] for i in range(3)), F(0)) <= e
                count += 1
    report = {
        'scope': 'Exact finite probability exercises; no real experiences, assay, shift-invariance or empirical calibration established.',
        'example': {'source': [str(x) for x in s], 'target': [str(x) for x in t],
                    'source_error_bound': str(eps), 'saturating_conditional_errors': [str(x) for x in f_for_example()],
                    'sharp_target_error_bound': str(bound)},
        'unsupported_target_mass_with_zero_source_error': str(support),
        'identical_marginal_zero_error_if_kernel_stable': str(same),
        'three_cell_rational_grid_cases_checked_against_dual_and_vertex_enumeration': count,
    }
    out = ROOT / 'verification/experiential_mismatch_transport_gate.json'
    out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


def f_for_example():
    return optimum((F(3, 4), F(1, 4)), (F(1, 4), F(3, 4)), F(1, 20))[1]


if __name__ == '__main__':
    main()
