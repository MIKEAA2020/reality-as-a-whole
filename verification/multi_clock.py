"""Exact closure/path/measure witnesses for MULTI_CLOCK_CONSTRAINT_CLOSURE.md."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
if __package__:
    from .turning_clock import real, mm, dag, add, scale, word, conj, probability, Z, ONE
    from .infinite_coherence import gmul
else:
    from turning_clock import real, mm, dag, add, scale, word, conj, probability, Z, ONE
    from infinite_coherence import gmul


def zscale(z, A):
    return [[gmul(z, x) for x in row] for row in A]


def comm(A, B):
    return add(mm(A, B), scale(Q(-1), mm(B, A)))


def UA(c, s):
    assert c*c+s*s == 1
    return [[(c, -s), Z], [Z, (c, s)]]


def UB(c, s):
    assert c*c+s*s == 1
    return [[real(c), (Q(0), -s)], [(Q(0), -s), real(c)]]


def routes(Aa, Ba, Ab, Bb):
    deltaA = mm(Ab, dag(Aa))
    y_step = mm(Bb, dag(Ba))
    x_at_a = conj(Ba, deltaA)
    x_at_b = conj(Bb, deltaA)
    return mm(y_step, x_at_a), mm(x_at_b, y_step)


def run():
    I = [[ONE, Z], [Z, ONE]]
    A = [[ONE, Z], [Z, real(-1)]]
    B = [[Z, ONE], [ONE, Z]]
    zero = [[Z, Z], [Z, Z]]
    incompatible = comm(A, B)
    assert mm(incompatible, incompatible) == scale(Q(-4), I)
    phases = ((Q(1), Q(0)), (Q(3, 5), Q(4, 5)),
              (Q(5, 13), Q(12, 13)), (Q(0), Q(1)))
    Y = [[Z, (Q(0), Q(-1))], [(Q(0), Q(1)), Z]]
    curvature_checks = 0
    for c, s in phases:
        H1 = conj(UB(c, s), A)
        cos2, sin2 = c*c-s*s, 2*c*s
        assert H1 == add(scale(cos2, A), scale(-sin2, Y))
        derivative_y = add(scale(-2*sin2, A), scale(-2*cos2, Y))
        assert derivative_y == zscale((Q(0), Q(-1)), comm(B, H1))
        curvature = add(scale(Q(-1), derivative_y), zscale((Q(0), Q(1)), comm(H1, B)))
        assert curvature == zero
        curvature_checks += 1
    endpoint_checks = 0
    points = [(UA(*x), UB(*y)) for x, y in product(phases, repeat=2)]
    for Aa, Ba in points:
        for Ab, Bb in points:
            xy, yx = routes(Aa, Ba, Ab, Bb)
            expected = word(Bb, Ab, dag(Aa), dag(Ba))
            assert xy == yx == expected
            endpoint_checks += 1
    a = Q(3, 5)
    f0 = 1/(1+a)
    cx, sx = Q(3, 5), Q(4, 5)
    f = 1/(1+a*cx)
    beta = a*sx*f
    fprime = a*sx*f*f
    assert f0 == Q(5, 8) and f == Q(25, 34)
    assert beta == Q(6, 17) and fprime == beta*f
    raw = Q(4, 5)
    assert raw*f == Q(10, 17) and raw*f0 == Q(1, 2)
    adjusted = raw*f/f0
    assert adjusted == Q(16, 17) and adjusted*f0 == raw*f
    # Exact circle Fourier moments: profiles c0+c1*cos(x).
    profiles = ((Q(1), Q(0)), (Q(0), Q(1)), (Q(1), Q(2)))
    m = [c0 for c0, c1 in profiles]
    mf = [c0+a*c1/2 for c0, c1 in profiles]
    naive = [[x*y for y in mf] for x in m]
    corrected = [[x*y for y in m] for x in m]
    assert naive[0][1] == Q(3, 10) and naive[1][0] == 0
    assert corrected[0][1] == corrected[1][0] == 0
    assert all(corrected[i][j] == corrected[j][i] for i in range(3) for j in range(3))
    for v in product((Q(-2), Q(-1), Q(0), Q(1), Q(2)), repeat=3):
        assert sum(v[i]*corrected[i][j]*v[j] for i in range(3) for j in range(3)) == sum(x*y for x, y in zip(v, m))**2
    # Anchored two-event experiment, compared through both coordinate routes.
    A0, B0 = I, I
    A1, B1 = UA(Q(3, 5), Q(4, 5)), UB(Q(5, 13), Q(12, 13))
    A2, B2 = I, UB(Q(0), Q(1))
    U1, U2 = mm(B1, A1), mm(B2, A2)
    T10s = routes(A0, B0, A1, B1)
    T21s = routes(A1, B1, A2, B2)
    P0 = [[ONE, Z], [Z, Z]]
    P1 = add(I, scale(Q(-1), P0))
    v = [Q(3, 5), Q(4, 5)]
    rho = [[real(x*y) for y in v] for x in v]
    rows, wrong_rows = [], []
    wrong10 = mm(A1, B1)
    wrong21 = word(A2, dag(A1), B2, dag(B1))
    allp = []
    for Pa in (P0, P1):
        row, wrongrow = [], []
        L1 = conj(dag(U1), Pa)
        for Pb in (P0, P1):
            root = mm(conj(dag(U2), Pb), L1)
            p = probability(root, rho)
            for T10, T21 in product(T10s, T21s):
                reduced = word(Pb, T21, Pa, T10)
                assert reduced == mm(U2, root)
                assert probability(reduced, rho) == p
            wrongrow.append(str(probability(word(Pb, wrong21, Pa, wrong10), rho)))
            row.append(p)
        assert sum(row) == probability(L1, rho)
        allp.extend(row)
        rows.append([str(p) for p in row])
        wrong_rows.append(wrongrow)
    assert sum(allp) == 1 and rows != wrong_rows
    return {
        'status': 'passed', 'arithmetic': 'exact rational Fourier moments and Gaussian rational matrices',
        'zero_curvature_checks': curvature_checks,
        'two_route_endpoint_transport_checks': endpoint_checks,
        'structure_function_at_test_point': str(beta),
        'raw_update_endpoints_y': ['10/17', '1/2'], 'compensated_parameter': str(adjusted),
        'naive_rigging_gh_hg': [str(naive[0][1]), str(naive[1][0])],
        'jacobian_corrected_rigging_gram': [[str(x) for x in row] for row in corrected],
        'anchored_record_probabilities_both_routes': rows,
        'incompatible_constant_generator_probabilities': wrong_rows,
        'analytic_not_finite_discretization': [
            'self-adjoint noncommuting D1,D2 and common test core',
            '[D1,D2]=-i beta(x) D2',
            'positive corrected averaging P1 f P2=P2 f P1',
            'physical quotient and strong selected Dirac algebra'],
        'not_claimed': ['gravitational hypersurface-deformation algebra',
                        'unique rigging for the full kinematic commutant',
                        'autonomous clocks or event triggers', 'physical clock selection'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: multi-clock closure witnesses, endpoint routes, Jacobian averaging and records')
    print(path)
