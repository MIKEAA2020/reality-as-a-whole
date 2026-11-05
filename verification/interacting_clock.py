"""Exact checks for INTERACTING_CLOCK_RATE.md; continuum rigging is analytic in the report."""
from fractions import Fraction as Q
from pathlib import Path
import json
if __package__:
    from .local_preparation import mm as rm, tr, add as ra, scale as rs, trace as rt
    from .turning_clock import real, mm, dag, add, scale, word, conj, probability, Z, ONE
else:
    from local_preparation import mm as rm, tr, add as ra, scale as rs, trace as rt
    from turning_clock import real, mm, dag, add, scale, word, conj, probability, Z, ONE


def outer(v):
    return [[x*y for y in v] for x in v]


def cm(A):
    return [[real(x) for x in row] for row in A]


def mv(A, v):
    return [sum(x*y for x, y in zip(row, v)) for row in A]


def dot(v, w):
    return sum(x*y for x, y in zip(v, w))


def ctrace(A):
    value = (A[0][0][0]+A[1][1][0], A[0][0][1]+A[1][1][1])
    assert value[1] == 0
    return value[0]


def U(c, s):
    assert c*c+s*s == 1
    return [[real(c), (Q(0), -s)], [(Q(0), -s), real(c)]]


def run():
    Ir = [[Q(1), Q(0)], [Q(0), Q(1)]]
    Nr = [[Q(1), Q(0)], [Q(0), Q(4)]]
    Mr = [[Q(1), Q(0)], [Q(0), Q(2)]]
    Fir = [[Q(1), Q(0)], [Q(0), Q(1, 2)]]
    Hr = [[Q(0), Q(2)], [Q(2), Q(0)]]
    Kr = [[Q(0), Q(1)], [Q(1), Q(0)]]
    assert rm(Nr, Hr) != rm(Hr, Nr)
    assert rm(rm(Fir, Hr), Fir) == Kr
    residues, projectors = {}, {}
    for kappa in (Q(-1), Q(1)):
        Pi = rs(Q(1, 2), [[Q(1), kappa], [kappa, Q(1)]])
        w = [Q(1), kappa/2]
        Ck = ra(rs(-kappa, Nr), Hr)
        assert mv(Ck, w) == [Q(0), Q(0)]
        norm2 = dot(w, w)
        slope = dot(w, mv(Nr, w))/norm2
        assert norm2 == Q(5, 4) and slope == Q(8, 5)
        residue = rs(1/(norm2*slope), outer(w))
        assert residue == rm(rm(Fir, Pi), Fir)
        residues[kappa], projectors[kappa] = residue, Pi
    spectral_family_checks = 0
    for energy, roots in ((Q(-2), (Q(0), Q(5, 2))),
                          (Q(0), (Q(-1), Q(1))),
                          (Q(2), (Q(-5, 2), Q(0)))):
        KE = ra(Kr, rs(-energy, rm(Fir, Fir)))
        for root, other in (roots, tuple(reversed(roots))):
            Pi = rs(1/(root-other), ra(KE, rs(-other, Ir)))
            assert rm(Pi, Pi) == Pi and rt(Pi) == 1
            CminusE = ra(ra(rs(-root, Nr), Hr), rs(-energy, Ir))
            assert rm(rm(CminusE, Fir), Pi) == [[Q(0)]*2 for _ in range(2)]
            spectral_family_checks += 1
    data = ({Q(-1): [Q(1), Q(2)], Q(1): [Q(2), Q(-1)]},
            {Q(-1): [Q(0), Q(1)], Q(1): [Q(3), Q(2)]},
            {Q(-1): [Q(5, 3), Q(2, 5)], Q(1): [Q(-1), Q(0)]})
    def eta(values):
        terms = [mv(rm(projectors[k], Fir), values[k]) for k in residues]
        return [sum(term[i] for term in terms) for i in range(2)]
    gram_checks = 0
    for f in data:
        for g in data:
            assert dot(eta(f), eta(g)) == sum(dot(f[k], mv(residues[k], g[k])) for k in residues)
            gram_checks += 1
    I, N, M, F = map(cm, (Ir, Nr, Mr, Fir))
    rho = cm(outer([Q(3, 5), Q(4, 5)]))
    points = [(Q(1), Q(0)), (Q(3, 5), Q(4, 5)), (Q(0), Q(1)),
              (Q(-3, 5), Q(4, 5)), (Q(-1), Q(0))]
    ordinary_norms = []
    for c, s in points:
        E = mm(F, U(c, s))
        bare = conj(E, rho)
        assert ctrace(mm(N, bare)) == 1
        ordinary = ctrace(bare)
        assert Q(1, 4) <= ordinary <= 1
        ordinary_norms.append(str(ordinary))
        for cc, ss in points:
            T = word(F, U(cc, ss), dag(U(c, s)), M)
            assert word(dag(T), N, T) == N
    assert ordinary_norms[0] == '13/25' and ordinary_norms[2] == '73/100'
    A_bare = word(F, cm(Kr), M)
    assert A_bare != dag(A_bare)
    assert mm(dag(A_bare), N) == mm(N, A_bare)
    Pz0 = cm([[Q(1), Q(0)], [Q(0), Q(0)]])
    Pz1 = add(I, scale(Q(-1), Pz0))
    U1, U2 = U(Q(3, 5), Q(4, 5)), U(Q(0), Q(1))
    bare_initial = conj(F, rho)
    completeness = [[Z, Z], [Z, Z]]
    bare_completeness = [[Z, Z], [Z, Z]]
    rows, all_probabilities, wrong_sum = [], [], Q(0)
    for Pa in (Pz0, Pz1):
        row = []
        L1 = conj(dag(U1), Pa)
        for Pb in (Pz0, Pz1):
            L2 = conj(dag(U2), Pb)
            branch = mm(L2, L1)
            p = probability(branch, rho)
            Bbare = word(F, U2, branch, M)
            state = conj(Bbare, bare_initial)
            assert ctrace(mm(N, state)) == p
            wrong_sum += ctrace(state)
            completeness = add(completeness, mm(dag(branch), branch))
            bare_completeness = add(bare_completeness, word(dag(Bbare), N, Bbare))
            row.append(p)
        assert sum(row) == probability(L1, rho)
        all_probabilities.extend(row)
        rows.append([str(p) for p in row])
    assert rows == [['5392/15625', '3033/15625'], ['2592/15625', '4608/15625']]
    assert probability(conj(dag(U1), Pz0), rho) != probability(Pz0, rho)
    assert sum(all_probabilities) == 1 and completeness == I and bare_completeness == N
    assert wrong_sum != 1
    R = scale(Q(1, 2), M)
    assert mm(R, F) == scale(Q(1, 2), I)
    for c, s in points:
        flux_state = conj(U(c, s), rho)
        assert probability(mm(R, F), flux_state) == Q(1, 4)
    return {
        'status': 'passed', 'arithmetic': 'exact rational real and imaginary parts',
        'system_clock_rate_noncommutes_with_H': True,
        'spectral_zero_slope': '8/5', 'spectral_rigging_gram_checks': gram_checks,
        'off_constraint_spectral_family_checks': spectral_family_checks,
        'ordinary_norms_at_sample_phases': ordinary_norms, 'all_flux_norms': '1',
        'two_event_flux_and_bare_metric_probabilities': rows,
        'unweighted_bare_branch_sum_not_physical': str(wrong_sum),
        'metric_effect_completeness': True, 'filter_and_recovery_joint_success': '1/4',
        'analytic_not_finite_discretization': ['self-adjoint C=N p_t+H on real clock line',
                                             'spectral slopes and group-average rigging metric',
                                             'no normalizable kinematic zero vector',
                                             'full spectral transform and strong kinematic Dirac representatives',
                                             'physical unitarity and anchored records in flux metric'],
        'not_solved': ['clock-rate zeros and sign changes', 'general unbounded matter',
                       'multiple gravitational constraints and refoliation', 'physical clock selection'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: coupled clock rate, spectral rigging residues, flux metric and anchored records')
    print(path)
