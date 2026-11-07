"""Exact polynomial checks for MODULAR_LOCAL_NET.md; no infinite-space discretization."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json


def add(f, g):
    n = max(len(f), len(g))
    out = [(f[k] if k < len(f) else Q(0)) + (g[k] if k < len(g) else Q(0)) for k in range(n)]
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def mul(f, g):
    out = [Q(0)]*(len(f)+len(g)-1)
    for j, x in enumerate(f):
        for k, y in enumerate(g):
            out[j+k] += x*y
    return out


def derivative(f):
    return [k*f[k] for k in range(1, len(f))] or [Q(0)]


def value(f, x):
    return sum(c*x**k for k, c in enumerate(f))


def integral(f, a, b):
    return sum(c*(b**(k+1)-a**(k+1))/Q(k+1) for k, c in enumerate(f))


def shift(f, a):
    # f(x-a)
    out = [Q(0)]*len(f)
    for k, c in enumerate(f):
        for j in range(k+1):
            out[j] += c*comb(k, j)*(-a)**(k-j)
    return out


def phase(f, left, right, g, other_left, other_right):
    a, b = max(left, other_left), min(right, other_right)
    return integral(mul(f, derivative(g)), a, b) if a < b else Q(0)


def run():
    f = [Q(0), Q(0), Q(1), Q(-2), Q(1)]
    g = [Q(0)]+f
    for h in (f, g):
        for x in (Q(0), Q(1)):
            assert value(h, x) == value(derivative(h), x) == 0
    sigma = integral(mul(f, derivative(g)), Q(0), Q(1))
    assert sigma == Q(1, 1260)
    assert sigma == integral(mul(f, f), Q(0), Q(1))/2
    assert integral(mul(g, derivative(f)), Q(0), Q(1)) == -sigma
    translations = []
    for a in (Q(-2), Q(-1), Q(-1, 2), Q(-1, 4), Q(0), Q(1, 4), Q(1, 2), Q(1), Q(2)):
        h = shift(f, a)
        s = phase(f, Q(0), Q(1), h, a, a+1)
        reverse = phase(h, a, a+1, f, Q(0), Q(1))
        assert s == -reverse
        if abs(a) >= 1:
            assert s == 0
        elif a:
            assert (s > 0) == (a > 0)
        translations.append({'translation': str(a), 'symplectic_phase': str(s)})
    # Affine push-forward f(x)->f((x-c)/r) leaves the symplectic form fixed.
    affine_cases = 0
    for r in (Q(1, 3), Q(2), Q(5, 2)):
        for c in (Q(-2), Q(0), Q(4, 3)):
            ff = shift([v/r**k for k, v in enumerate(f)], c)
            gg = shift([v/r**k for k, v in enumerate(g)], c)
            assert integral(mul(ff, derivative(gg)), c, c+r) == sigma
            affine_cases += 1
    # Laurent polynomials in a formal local unitary U. Star sends U^k to U^-k.
    def product(a, b):
        out = {}
        for j, x in a.items():
            for k, y in b.items():
                out[j+k] = out.get(j+k, Q(0))+x*y
        return {k: v for k, v in out.items() if v}
    def star(a):
        return {-k: v for k, v in a.items()}
    plus, minus = {0: Q(1, 2), 1: Q(1, 2)}, {0: Q(1, 2), 1: Q(-1, 2)}
    completeness = {}
    for K in (plus, minus):
        for k, v in product(star(K), K).items():
            completeness[k] = completeness.get(k, Q(0))+v
    assert {k: v for k, v in completeness.items() if v} == {0: Q(1)}
    assert product(star(plus), plus) == {0: Q(1, 2), 1: Q(1, 4), -1: Q(1, 4)}
    def padd(*terms):
        out = {}
        for term in terms:
            for k, v in term.items():
                out[k] = out.get(k, Q(0))+v
        return {k: v for k, v in out.items() if v}
    def neg(a):
        return {k: -v for k, v in a.items()}
    Ks = (plus, minus)
    U = [[{}, star(plus), star(minus)]]
    for i in range(2):
        U.append([Ks[i]]+[padd({0: Q(1)} if i == j else {},
                              neg(product(Ks[i], star(Ks[j])))) for j in range(2)])
    adjoint = [[star(U[j][i]) for j in range(3)] for i in range(3)]
    assert adjoint == U
    for i in range(3):
        for j in range(3):
            assert padd(*(product(adjoint[i][k], U[k][j]) for k in range(3))) == (
                {0: Q(1)} if i == j else {})
    assert [U[1][0], U[2][0]] == [plus, minus]
    return {
        'status': 'passed', 'arithmetic': 'exact rational polynomial integration',
        'noncommuting_interval_phase': str(sigma),
        'rescaled_g_phase': str(1260*sigma),
        'affine_symplectic_checks': affine_cases,
        'translated_same_smear_phases': translations,
        'localized_instrument_completeness': True,
        'local_three_level_record_completion_unitary': True,
        'vacuum_record_before': '(1+exp(-norm(F_f)^2/2))/2',
        'vacuum_record_after_local_Wg': '(1+exp(-norm(F_f)^2/2)*cos(sigma(f,g)))/2',
        'analytic_proofs_not_finite_tests': [
            'compact-smear Hardy-strip membership and interval-algebra membership',
            'nontriviality, isotony, locality and affine covariance of intersections',
            'positive energy, unique translation-invariant vacuum and global cyclicity',
            'no signaling for arbitrary complete instruments in disjoint intervals'],
        'not_claimed': ['bounded-interval vacuum cyclicity', 'Haag duality or conformal completion',
                        'four-dimensional causal geometry', 'independent selection of the modular pair'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: interval symplectic phases, affine invariance and local instrument completeness')
    print(path)
