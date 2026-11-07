#!/usr/bin/env python3
"""Scoped arithmetic checks for the OPH finite-calibration/energy bridge.

The finite rank obstruction in the report is an analytic infinite-dimensional
argument. Finite linear algebra below is only an illustration, not its proof.
"""
from fractions import Fraction as F
from math import ceil, log, log1p, sqrt
from pathlib import Path
import json
import random


def null_vector(rows):
    a = [[F(v) for v in row] for row in rows]
    if not a:
        return [F(1)]
    nr, nc = len(a), len(a[0])
    pivots = []
    r = 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][c]
        a[r] = [v/d for v in a[r]]
        for i in range(nr):
            if i != r and a[i][c]:
                d = a[i][c]
                a[i] = [x-d*y for x,y in zip(a[i],a[r])]
        pivots.append(c)
        r += 1
        if r == nr:
            break
    free = next(c for c in range(nc) if c not in pivots)
    v = [F(0)]*nc
    v[free] = 1
    for i in reversed(range(len(pivots))):
        c = pivots[i]
        v[c] = -sum(a[i][j]*v[j] for j in range(c+1,nc))
    assert any(v) and all(sum(F(x)*y for x,y in zip(row,v)) == 0 for row in rows)
    return v


def main():
    target = F(1, 10)
    alpha = 0.05
    rows = []
    for n in (4, 16, 64):
        root = int(sqrt(n))
        assert root*root == n
        settings = n+1
        # OPH: half-diamond ≤ 2*sqrt(n*eps)*(2+sqrt(n)).
        eps = target**2 / (4*n*(2+root)**2)
        assert 4*n*eps*(2+root)**2 == target**2
        x = float(eps)
        required = ceil(log(settings/alpha)/(-log1p(-x)))
        logfail = log(settings)-required*(-log1p(-x))
        logfail_before = log(settings)-(required-1)*(-log1p(-x))
        assert logfail <= log(alpha) < logfail_before
        rows.append({'input_dimension':n,'settings':settings,
                     'per_setting_failure_allowance':str(eps),
                     'trials_per_setting_zero_failures':required,
                     'total_trials':required*settings})

    # A pure two-level test, P=|0><0|, with |ψ>=(12|0>+5|1>)/13.
    # id and replacement agree on P, but their output trace distance is 5/13.
    a,b = F(12,13),F(5,13)
    assert a*a+b*b == 1
    t=b*b
    # Difference between |ψ><ψ| and |0><0| has eigenvalues ±b.
    assert t*t+(a*b)**2 == t
    assert b <= 2*b+t

    rng = random.Random(20261107)
    controls = 0
    # Illustrate finite-rank obstruction: m constraints, m+1 low-energy
    # independent states. There is always a vector in their common kernel.
    for rank_bound in range(1, 16):
        for _ in range(10):
            rows_small = [[rng.randint(-5,5) for _ in range(rank_bound+1)]
                          for _ in range(rank_bound)]
            v = null_vector(rows_small)
            norm = sum(x*x for x in v)
            energy = sum(F(1,4)*x*x for x in v)/norm
            assert energy == F(1,4) and energy < 1
            controls += 1
    out = {'status':'passed',
           'scope':'Illustrative OPH finite-probe sample-size arithmetic, two-level tail control and finite orthogonality analogues; no validation of laboratory calibration or infinite-dimensional field dynamics.',
           'target_half_diamond':str(target),'familywise_alpha':alpha,
           'sample_size_examples':rows,
           'two_level_control':{'low_subspace_error':'0', 'tail_probability':str(t),
                                'actual_half_trace_distance':str(b),
                                'declared_upper_bound':'2*sqrt(t)+t'},
           'finite_low_energy_orthogonality_examples':controls,
           'limitations':'Zero-failure sample sizes are sufficient under iid calibration and trusted finite probes; finite analogues do not prove the infinite-dimensional no-finite-rank statement.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
