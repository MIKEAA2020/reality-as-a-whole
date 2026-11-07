"""Exact chart gluing, folded clock channels and records for TURNING_CLOCK_ATLAS.md."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
if __package__:
    from .infinite_coherence import gadd, gmul
else:
    from infinite_coherence import gadd, gmul


Z = (Q(0), Q(0))
ONE = (Q(1), Q(0))


def real(x):
    return Q(x), Q(0)


def star(z):
    return z[0], -z[1]


def scale(c, A):
    return [[(c*z[0], c*z[1]) for z in row] for row in A]


def add(A, B):
    return [[gadd(x, y) for x, y in zip(a, b)] for a, b in zip(A, B)]


def dag(A):
    return [[star(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def mm(A, B):
    out = []
    for a in A:
        row = []
        for col in zip(*B):
            z = Z
            for x, y in zip(a, col):
                z = gadd(z, gmul(x, y))
            row.append(z)
        out.append(row)
    return out


def word(*As):
    out = As[0]
    for A in As[1:]:
        out = mm(out, A)
    return out


def conj(A, rho):
    return word(A, rho, dag(A))


def probability(A, rho):
    state = conj(A, rho)
    p = gadd(state[0][0], state[1][1])
    assert p[1] == 0 and p[0] >= 0
    return p[0]


def U(q, r):
    assert q*q+r*r == 1
    return [[ONE, Z], [Z, (q, -r)]]


def run():
    I = [[ONE, Z], [Z, ONE]]
    points = [(Q(1), Q(0)), (Q(3, 5), Q(4, 5)), (Q(0), Q(1)),
              (Q(-3, 5), Q(4, 5)), (Q(-1), Q(0)), (Q(-3, 5), Q(-4, 5)),
              (Q(0), Q(-1)), (Q(3, 5), Q(-4, 5)), (Q(1), Q(0))]
    atlas, overlaps = [], 0
    for q, r in points:
        phase_frame = U(q, r)
        assert mm(dag(phase_frame), phase_frame) == I
        if abs(r) > Q(1, 2):
            s = Q(1 if r > 0 else -1)
            from_q = U(q, s*abs(r))
            assert from_q == phase_frame
            chart = 'q, orientation '+str(s)
        else:
            c = Q(1 if q > 0 else -1)
            from_r = U(c*abs(q), r)
            assert from_r == phase_frame
            chart = 'r, orientation '+str(c)
        if abs(r) > Q(1, 2) and abs(q) > Q(1, 2):
            hq, hr, dqdr = -1/r, 1/q, -r/q
            assert hr == hq*dqdr
            assert Q(1)/abs(q) == Q(1)/abs(r)*abs(dqdr)
            overlaps += 1
        atlas.append({'q': str(q), 'r': str(r), 'regular_chart': chart})
    accumulated = I
    for previous, current in zip(points, points[1:]):
        transport = mm(U(*current), dag(U(*previous)))
        accumulated = mm(transport, accumulated)
    assert accumulated == I
    Pxp = [[real(Q(1, 2))]*2 for _ in range(2)]
    Pxm = [[real(Q(1, 2)), real(Q(-1, 2))], [real(Q(-1, 2)), real(Q(1, 2))]]
    Pyp = [[real(Q(1, 2)), (Q(0), Q(-1, 2))], [(Q(0), Q(1, 2)), real(Q(1, 2))]]
    Pym = add(I, scale(Q(-1), Pyp))
    measurements = ((Pxp, Pxm), (Pxp, Pxm), (Pyp, Pym))
    us = [U(Q(3, 5), Q(4, 5)), U(Q(-1), Q(0)), U(Q(3, 5), Q(-4, 5))]
    rho = Pxp
    rows, lookup = [], {}
    wrong_differs = False
    for a, b, c in product(range(2), repeat=3):
        Pa, Pb, Pc = measurements[0][a], measurements[1][b], measurements[2][c]
        root = word(conj(dag(us[2]), Pc), conj(dag(us[1]), Pb), conj(dag(us[0]), Pa))
        chronological = word(Pc, us[2], dag(us[1]), Pb, us[1], dag(us[0]), Pa, us[0])
        assert chronological == mm(us[2], root)
        p = probability(root, rho)
        assert probability(chronological, rho) == p
        wrong = word(Pc, us[0], dag(us[1]), Pb, us[1], dag(us[0]), Pa, us[0])
        wrong_differs |= probability(wrong, rho) != p
        lookup[a, b, c] = p
        rows.append({'record': str(a)+str(b)+str(c), 'probability': str(p)})
    assert [row['probability'] for row in rows] == ['2/125', '18/125', '72/125', '8/125',
                                                   '2/125', '18/125', '9/250', '1/250']
    assert wrong_differs
    assert sum(lookup.values()) == 1
    for a, b in product(range(2), repeat=2):
        prefix = word(conj(dag(us[1]), measurements[1][b]), conj(dag(us[0]), measurements[0][a]))
        assert sum(lookup[a, b, c] for c in range(2)) == probability(prefix, rho)
    for a in range(2):
        assert sum(p for (aa, b, c), p in lookup.items() if aa == a) == probability(
            conj(dag(us[0]), measurements[0][a]), rho)
    # Folded readout retains q but discards orientation.
    states = (rho, Pxm, [[real(Q(9, 25)), (Q(0), Q(-12, 25))],
                        [(Q(0), Q(12, 25)), real(Q(16, 25))]])
    for q, r in points:
        for state in states:
            folded = scale(Q(1, 2), add(conj(U(q, r), state), conj(U(q, -r), state)))
            expected = [[state[0][0], (q*state[0][1][0], q*state[0][1][1])],
                        [(q*state[1][0][0], q*state[1][0][1]), state[1][1]]]
            assert folded == expected
    zero_plus = scale(Q(1, 2), add(conj(U(Q(0), Q(1)), rho), conj(U(Q(0), Q(-1)), rho)))
    zero_minus = scale(Q(1, 2), add(conj(U(Q(0), Q(1)), Pxm), conj(U(Q(0), Q(-1)), Pxm)))
    assert zero_plus == zero_minus == scale(Q(1, 2), I)
    assert conj(us[0], rho) != conj(us[2], rho)
    return {
        'status': 'passed', 'arithmetic': 'exact rational real and imaginary parts',
        'regular_atlas_cycle': atlas, 'overlap_chain_rule_checks': overlaps,
        'full_cycle_transport': 'identity', 'three_event_records_crossing_q_turn': rows,
        'record_normalization_and_all_prefixes': True,
        'same_unoriented_reading_wrong_frame_changes_records': wrong_differs,
        'folded_clock_offdiagonal_factor': 'q', 'q_zero_erases_plus_minus_distinction': True,
        'analytic_not_finite_discretization': ['periodic self-adjoint constraint and exact physical kernel',
                                             'Jacobian-correct arcsine clock measure',
                                             'regular q/r atlas and integrable turning singularity',
                                             'density connection for half-density amplitudes'],
        'not_supplied': ['autonomous winding counter', 'unbounded physical time',
                         'interacting clock-matter deparametrization', 'gravitational refoliation'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: turning-clock atlas, full-cycle gluing, folded information loss and anchored records')
    print(path)
