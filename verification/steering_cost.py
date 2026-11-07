"""Finite exact filters and readout relaxations for COMMUTANT_STEERING_AND_COST.md.

The infinite commutant optimum is an analytic standard-form argument in the report.
Gaussian samples below are floating-point illustrations, not certified tail bounds.
"""
from fractions import Fraction as Q
from math import erfc, sqrt, log
from pathlib import Path
import json
if __package__:
    from .local_preparation import mm, tr, add, scale, trace
else:
    from local_preparation import mm, tr, add, scale, trace


def outer(v):
    return [[x*y for y in v] for x in v]


def subtract(a, b):
    return add(a, scale(Q(-1), b))


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def run():
    d = [Q(3, 5), Q(4, 5)]
    rho = [[d[0]**2, Q(0)], [Q(0), d[1]**2]]
    I = [[Q(1), Q(0)], [Q(0), Q(1)]]
    filters = []
    for psi in ([Q(1), Q(0)], [Q(0), Q(1)],
                [Q(3, 5), Q(4, 5)], [Q(5, 13), Q(12, 13)]):
        assert sum(x*x for x in psi) == 1
        row = [psi[i]/d[i] for i in range(2)]
        c = sum(x*x for x in row)
        p = 1/c
        A = [row, [Q(0), Q(0)]]
        effect = scale(p, mm(tr(A), A))
        assert mm(effect, effect) == effect
        failure = subtract(I, effect)
        assert add(effect, mm(tr(failure), failure)) == I
        # K=A/sqrt(c); its unnormalized right density is p |psi><psi|.
        amplitudes = [[A[i][j]*d[j] for j in range(2)] for i in range(2)]
        conditional = mm(tr(amplitudes), amplitudes)
        target = outer(psi)
        assert conditional == target
        assert trace(scale(p, conditional)) == p
        residual = subtract(rho, scale(p, target))
        assert residual[0][0] >= 0 and residual[1][1] >= 0 and det(residual) == 0
        for extra in (Q(1, 100), Q(1, 10)):
            assert det(subtract(rho, scale(p+extra, target))) < 0
        filters.append({'target_vector': [str(x) for x in psi],
                        'D_max': 'log('+str(c)+')', 'optimal_probability': str(p),
                        'filter_norm_squared': str(c)})
    assert filters[2]['optimal_probability'] == '1/2'
    assert filters[3]['optimal_probability'] == '1521/2650'
    classical = []
    for q, r in (([Q(1, 2), Q(1, 3), Q(1, 6)], [Q(1, 3)]*3),
                 ([Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]),
                 ([Q(1, 2), Q(1, 4), Q(1, 4)], [Q(1, 2), Q(0), Q(1, 2)]),
                 ([Q(1, 5), Q(4, 5)], [Q(1), Q(0)])):
        assert sum(q) == sum(r) == 1
        p = min(qj/rj for qj, rj in zip(q, r) if rj)
        effects = [p*rj/qj for qj, rj in zip(q, r)]
        assert all(Q(0) <= e <= Q(1) for e in effects)
        assert sum(qj*e for qj, e in zip(q, effects)) == p
        assert [qj*e/p for qj, e in zip(q, effects)] == r
        assert any(e == 1 for e in effects)
        classical.append({'prior': [str(x) for x in q], 'target': [str(x) for x in r],
                          'relaxed_optimum': str(p), 'success_effects': [str(x) for x in effects]})
    assert classical[1]['relaxed_optimum'] == '1'
    assert classical[2]['relaxed_optimum'] == '1/2'
    gaussian = []
    last = float('inf')
    for R in (2., 4., 6., 8.):
        q = erfc(R/sqrt(2))/2
        r = erfc((R-1)/sqrt(2))/2
        p = min(q/r, (1-q)/(1-r))
        assert p == q/r and p < last
        last = p
        gaussian.append({'threshold': R, 'reference_tail': q, 'target_tail': r,
                         'binary_readout_relaxed_probability': p,
                         'binary_D_max': -log(p)})
    return {
        'status': 'passed', 'exact_arithmetic': 'rational matrices and filter effects',
        'pure_target_optimal_filters': filters,
        'finite_readout_relaxations': classical,
        'gaussian_binary_examples_floating_point': gaussian,
        'analytic_not_finite_tests': ['standard-form implementing vector theorem invoked',
                                     'p phi <= omega iff a commutant contraction prepares phi',
                                     'full-commutant optimum exp(-D_max)',
                                     'smoothed supremum and bounded-region upper bound'],
        'not_inferred': ['commutant optimum attained in any specified disjoint interval',
                         'remote-state preparation fixes all global correlations',
                         'finite readout filtering is a distant implementation',
                         'finite density matrix for a field interval algebra'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: optimal rational steering filters, failure completions and readout refinements')
    print(path)
