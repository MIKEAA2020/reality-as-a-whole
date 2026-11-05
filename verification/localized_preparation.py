"""Exact correlated-environment counterexample for LOCALIZED_PREPARATION_CRITERION.md.

No finite factorization is inferred for the field net. Its criterion is proved analytically.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
if __package__:
    from .local_preparation import mm, tr, add, scale, trace
else:
    from local_preparation import mm, tr, add, scale, trace


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def sub(a, b):
    return add(a, scale(Q(-1), b))


def diag(xs):
    return [[x if i == j else Q(0) for j in range(len(xs))] for i, x in enumerate(xs)]


def outer(v):
    return [[x*y for y in v] for x in v]


def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def right_marginal(rho):
    return [[sum(rho[2*e+r][2*e+s] for e in range(2)) for s in range(2)] for r in range(2)]


def run():
    weights = [Q(3), Q(1), Q(1), Q(3)]
    q = [x*x/20 for x in weights]
    rho = diag(q)
    plus = [[Q(1, 2)]*2 for _ in range(2)]
    assert right_marginal(rho) == scale(Q(1, 2), eye(2))
    w = [2*q[2*e]*q[2*e+1]/(q[2*e]+q[2*e+1]) for e in range(2)]
    assert w == [Q(9, 100)]*2
    optimum = sum(w)
    assert optimum == Q(9, 50)
    for e in range(2):
        block = diag(q[2*e:2*e+2])
        residual = sub(block, scale(w[e], plus))
        assert residual[0][0] >= 0 and residual[1][1] >= 0 and det2(residual) == 0
        assert det2(sub(block, scale(w[e]+Q(1, 1000), plus))) < 0
    A = [[Q(x) for x in row] for row in
         ((1, 3, 0, 0), (0, 0, 0, 0), (0, 0, 3, 1), (0, 0, 0, 0))]
    effect = scale(Q(1, 10), mm(tr(A), A))
    assert mm(effect, effect) == effect
    failure = sub(eye(4), effect)
    assert add(effect, mm(tr(failure), failure)) == eye(4)
    # Omega coefficient matrix is diag(weights)/sqrt(20); K=A/sqrt(10).
    branch_coeff = mm(A, diag(weights))
    er_success = scale(Q(1, 200), mm(tr(branch_coeff), branch_coeff))
    assert er_success == scale(Q(1, 20), mm(mm(diag(weights), tr(effect)), diag(weights)))
    assert trace(er_success) == optimum
    er_conditional = scale(1/optimum, er_success)
    assert right_marginal(er_conditional) == plus
    assert er_conditional == [[Q(1, 4) if i//2 == j//2 else Q(0) for j in range(4)] for i in range(4)]
    assert er_success == scale(optimum, er_conditional)
    # Fixed global normalized output: R_chi=A*sqrt(20)/6, squared norm 50/9.
    global_cost = Q(10*20, 36)
    assert global_cost == 1/optimum
    # Full target commutant filter on LE: projection onto eta_plus.
    v = [Q(x) for x in (3, 0, 1, 0, 0, 1, 0, 3)]
    commutant_filter = scale(Q(1, 20), outer(v))
    assert mm(commutant_filter, commutant_filter) == commutant_filter
    omega_coeff = [[Q(0), Q(0)] for _ in range(8)]
    omega_coeff[0][0] = Q(3)
    omega_coeff[2][1] = Q(1)
    omega_coeff[5][0] = Q(1)
    omega_coeff[7][1] = Q(3)
    prepared = mm(commutant_filter, omega_coeff)
    right_success = scale(Q(1, 20), mm(tr(prepared), prepared))
    assert trace(right_success) == Q(1, 2)
    assert scale(Q(2), right_success) == plus
    Z_E = diag([Q(1 if i % 2 == 0 else -1) for i in range(8)])
    assert mm(commutant_filter, Z_E) != mm(Z_E, commutant_filter)
    return {
        'status': 'passed', 'arithmetic': 'exact rational matrices; common square roots factored out',
        'target': 'pure plus state on R',
        'complementary_prior': [str(x) for x in q],
        'target_only_optimum': '1/2',
        'actual_control_optimum': str(optimum),
        'overestimate_factor': str(Q(1, 2)/optimum),
        'fixed_global_target_cost': str(global_cost),
        'per_environment_success_capacity': [str(x) for x in w],
        'control_filter_effect_projection': True,
        'failure_completion': True,
        'finite_complementary_SDP_feasible_solution': True,
        'full_commutant_filter_uses_inaccessible_E': True,
        'analytic_not_finite_tests': [
            'complete complementary-state domination iff bounded local success operator exists',
            'exact local pure-vector success optimum 1/c_M',
            'vector smoothing and algebra-inclusion monotonicity',
            'restricted target requires optimization over global extensions'],
        'not_inferred': ['field-region tensor factorization', 'efficient optimal filter synthesis',
                         'single-vector formula covers unresolved mixed success ensembles',
                         'phenomenal ownership or necessary actuality'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: exact localized steering gap, optimal filters and complementary-state bounds')
    print(path)
