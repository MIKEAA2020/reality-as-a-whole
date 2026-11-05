"""Checks for LOCAL_PREPARATION_AND_ACCESS.md.

Rational finite instruments check identities, not Reeh-Schlieder density.
Gaussian samples are floating-point sanity checks of the analytically proved bound.
"""
from fractions import Fraction as Q
from math import erfc, exp, sqrt
from pathlib import Path
import json


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def remote_density(v):
    # Amplitudes indexed by local then remote index; keep subnormalization.
    return [[sum(v[2*a+b]*v[2*a+c] for a in range(2)) for c in range(2)] for b in range(2)]


def local_action(K, v):
    return [sum(K[a][c]*v[2*c+b] for c in range(2)) for a in range(2) for b in range(2)]


def run():
    I = [[Q(1), Q(0)], [Q(0), Q(1)]]
    rotations = [I, [[Q(3, 5), Q(-4, 5)], [Q(4, 5), Q(3, 5)]]]
    projectors = [I, [[Q(1), Q(0)], [Q(0), Q(0)]],
                  [[Q(0), Q(0)], [Q(0), Q(1)]],
                  [[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]]]
    omega = [Q(3, 5), Q(0), Q(0), Q(4, 5)]
    remote = remote_density(omega)
    checks = 0
    for R in rotations:
        for first, second in (((Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13))),
                              ((Q(1), Q(0)), (Q(3, 5), Q(4, 5)))):
            K = mm(mm(R, [[first[0], Q(0)], [Q(0), second[0]]]), tr(R))
            L = mm(mm(R, [[first[1], Q(0)], [Q(0), second[1]]]), tr(R))
            assert add(mm(tr(K), K), mm(tr(L), L)) == I
            success = remote_density(local_action(K, omega))
            failure = remote_density(local_action(L, omega))
            assert add(success, failure) == remote
            p = trace(success)
            assert p > 0 and p <= 1
            conditional = scale(1/p, success)
            for projection in projectors:
                assert mm(projection, projection) == projection
                q = trace(mm(remote, projection))
                q_success = trace(mm(conditional, projection))
                assert p*q_success <= q
                if q_success:
                    assert p <= q/q_success
                checks += 1
    # An exactly saturated preparation bound in a transparent two-qubit example.
    K = [[Q(1), Q(0)], [Q(0), Q(1, 2)]]
    success = remote_density(local_action(K, omega))
    p = trace(success)
    assert p == Q(13, 25)
    q, q_conditional = remote[0][0], success[0][0]/p
    assert q/q_conditional == p
    gaussian = []
    for variance in (0.5, 1.0, 2.0):
        for mu in (0.5, 1.0, 2.0):
            for n in (2, 4, 6):
                R = mu+n*sqrt(variance)
                q = erfc(R/sqrt(2*variance))/2
                q_target = erfc((R-mu)/sqrt(2*variance))/2
                ratio_bound = exp(-mu*R/variance+mu*mu/(2*variance))
                assert 0 < q < q_target < 1
                assert q/q_target <= ratio_bound*(1+1e-12)
                epsilon = q_target/4
                preparation_bound = q/(q_target-2*epsilon)
                assert preparation_bound <= 2*ratio_bound*(1+1e-12)
                gaussian.append({'variance': variance, 'mean_shift': mu,
                                 'threshold': R, 'accuracy_threshold': epsilon,
                                 'probability_upper_bound': preparation_bound,
                                 'analytic_envelope': 2*ratio_bound})
    return {
        'status': 'passed',
        'exact_rational_checks': checks,
        'saturated_finite_example': {'success_probability': str(p),
                                     'remote_prior_Q': str(q_conditional*p),
                                     'remote_conditional_Q': str(q_conditional)},
        'gaussian_samples_floating_point_only': gaussian,
        'analytic_not_computational': [
            'interval one-particle density from positive-energy boundary uniqueness',
            'Fock local cyclicity via standard CCR exponential-vector theorem',
            'local conditional approximation to every target vector',
            'p <= q_R/(q_target_R-2*epsilon)',
            'fixed disjoint Weyl target forces p to zero as epsilon tends to zero'],
        'not_established': ['efficient preparation algorithm', 'universal success rate',
                            'phenomenal scope or intrinsic qualitative identity'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: exact local instrument/no-signaling identities and Gaussian bound sanity checks')
    print(path)
