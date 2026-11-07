"""Exact same-constraint clock reductions and anchored records; see CLOCK_CHOICE_EQUIVALENCE.md."""
from fractions import Fraction as Q
from pathlib import Path
import json
if __package__:
    from .local_preparation import mm, tr, add, scale, trace
else:
    from local_preparation import mm, tr, add, scale, trace


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def sub(a, b):
    return add(a, scale(Q(-1), b))


def outer(v):
    return [[x*y for y in v] for x in v]


def conj(a, b):
    return mm(mm(a, b), tr(a))


def normalize(rho):
    return scale(1/trace(rho), rho)


def block(a, b, c, d):
    return [x+y for x, y in zip(a, b)]+[x+y for x, y in zip(c, d)]


def run():
    I = eye(2)
    U = [[Q(3, 5), Q(-4, 5)], [Q(4, 5), Q(3, 5)]]
    C = block(I, scale(Q(-1), tr(U)), scale(Q(-1), U), I)
    J_unscaled = I+U
    assert mm(C, J_unscaled) == [[Q(0)]*2 for _ in range(4)]
    assert mm(tr(J_unscaled), J_unscaled) == scale(Q(2), I)
    Ep, Em = scale(Q(1, 2), add(I, U)), scale(Q(1, 2), sub(I, U))
    wp, wm = Q(4, 5), Q(1, 5)
    assert mm(tr(Ep), Ep) == scale(wp, I)
    assert mm(tr(Em), Em) == scale(wm, I)
    Bp = [[Q(2), Q(-1)], [Q(1), Q(2)]]
    Bm = [[Q(1), Q(2)], [Q(-2), Q(1)]]
    assert mm(tr(Bp), Bp) == mm(tr(Bm), Bm) == scale(Q(5), I)
    W = scale(Q(1, 5), mm(Bm, tr(Bp)))
    assert W == [[Q(0), Q(1)], [Q(-1), Q(0)]]
    assert mm(tr(W), W) == I
    HX_unscaled = block(I, I, I, scale(Q(-1), I))
    CX = scale(Q(1, 2), conj(HX_unscaled, C))
    JX = Ep+Em
    assert mm(tr(JX), JX) == I
    assert CX == scale(Q(2), sub(eye(4), mm(JX, tr(JX))))
    assert mm(CX, JX) == [[Q(0)]*2 for _ in range(4)]
    D = [x+y for x, y in zip(scale(Q(-1, 2), W), I)]
    assert CX == scale(2*wp, mm(tr(D), D))
    naive_D = [x+y for x, y in zip(scale(Q(-1), W), I)]
    assert mm(naive_D, JX) != [[Q(0)]*2 for _ in range(2)]
    rho = outer([Q(3, 5), Q(4, 5)])
    P0 = [[Q(1), Q(0)], [Q(0), Q(0)]]
    P1 = sub(I, P0)
    projectors = (P0, P1)
    probabilities = []
    branch_completeness = [[Q(0)]*2 for _ in range(2)]
    observables = (I, P0, P1, [[Q(0), Q(1)], [Q(1), Q(0)]])
    for B, w, E in ((Bp, wp, Ep), (Bm, wm, Em)):
        rho_c = scale(Q(1, 5), conj(B, rho))
        assert rho_c == scale(1/w, conj(E, rho))
        for A in observables:
            A_c = scale(Q(1, 5), conj(B, A))
            assert trace(mm(rho_c, A_c)) == trace(mm(rho, A))
    for a, Pa in enumerate(projectors):
        row = []
        for b, Pb in enumerate(projectors):
            K1 = Pa
            K2 = mm(mm(tr(U), Pb), U)
            branch = mm(K2, K1)
            branch_completeness = add(branch_completeness, mm(tr(branch), branch))
            p = trace(conj(branch, rho))
            for B in (Bp, Bm):
                state_c = scale(Q(1, 5), conj(B, rho))
                branch_c = scale(Q(1, 5), conj(B, branch))
                assert trace(conj(branch_c, state_c)) == p
            K1_plus = scale(Q(1, 5), conj(Bp, K1))
            K2_minus = scale(Q(1, 5), conj(Bm, K2))
            branch_moving = mm(mm(K2_minus, W), K1_plus)
            assert branch_moving == scale(Q(1, 5), mm(mm(Bm, branch), tr(Bp)))
            state_plus = scale(Q(1, 5), conj(Bp, rho))
            assert trace(conj(branch_moving, state_plus)) == p
            row.append(str(p))
        probabilities.append(row)
    assert branch_completeness == I
    assert probabilities == [['81/625', '144/625'], ['256/625', '144/625']]
    # Bad X clock for U=Z: projectors filter the physical sector.
    plus = [[Q(1, 2)]*2 for _ in range(2)]
    minus = [[Q(1, 2), Q(-1, 2)], [Q(-1, 2), Q(1, 2)]]
    assert trace(mm(plus, minus)) == 0
    assert all(conj(E, plus) == conj(E, minus) for E in projectors)
    assert trace(conj(P0, plus)) == Q(1, 2)
    assert trace(conj(P0, P0)) == 1
    # An invertible nonideal filter, its metric, and physical reversal.
    E = [[Q(3, 5), Q(0)], [Q(0), Q(4, 5)]]
    Einv = [[Q(5, 3), Q(0)], [Q(0), Q(5, 4)]]
    R = [[Q(1), Q(0)], [Q(0), Q(3, 4)]]
    assert mm(R, E) == scale(Q(3, 5), I)
    G = mm(tr(E), E)
    metric = mm(tr(Einv), Einv)
    X = [[Q(0), Q(1)], [Q(1), Q(0)]]
    transported_X = mm(mm(E, X), Einv)
    assert transported_X != tr(transported_X)
    assert mm(tr(transported_X), metric) == mm(metric, transported_X)
    assert normalize(conj(E, scale(Q(1, 2), I))) != scale(Q(1, 2), add(
        normalize(conj(E, P0)), normalize(conj(E, P1))))
    for state in (rho, plus, minus, P0, P1, scale(Q(1, 2), I)):
        assert trace(conj(mm(R, E), state)) == Q(9, 25)
        assert trace(mm(G, state)) >= Q(9, 25)
    return {
        'status': 'passed', 'arithmetic': 'exact rationals; common unitary square roots canceled',
        'same_constraint_noncommuting_clocks': True,
        'old_reading_weights': ['1/2', '1/2'], 'new_reading_weights': [str(wp), str(wm)],
        'weighted_transformed_constraint_verified': True,
        'naive_equal_weight_replacement_changes_kernel': True,
        'anchored_two_event_probabilities_all_frames': probabilities,
        'moving_frame_record_probabilities_verified': True,
        'bad_clock_erases_two_orthogonal_physical_states': True,
        'invertible_filter_joint_recovery_probability': '9/25',
        'pulled_back_metric_self_adjointness_verified': True,
        'analytic_not_just_finite_checks': ['ideal evaluation criterion E_c^* E_c=w_c I',
                                          'frame composition and anchored instrument equivalence',
                                          'probabilistic inverse-filter recovery formula'],
        'not_solved': ['global monotonic clock or turning points', 'gravitational refoliation algebra',
                       'physical clock/state/localization selection', 'unique physical time'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: same-constraint clock changes, weighted kernel, anchored records and failed clocks')
    print(path)
