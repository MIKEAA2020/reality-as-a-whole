"""Exact finite-core checks for INFINITE_RELATIONAL_CLOCK.md.

Infinite existence/nonexistence statements are proved in the report. No finite
cutoff is used as numerical evidence of those theorems. Standard library only.
"""
from fractions import Fraction as F
from functools import cache
from itertools import product
import json
from pathlib import Path
if __package__:
    from .relational_constraint import eye, transpose, mv, dot, scale
    from .relational_records import mm, add, branch_probabilities
else:
    from relational_constraint import eye, transpose, mv, dot, scale
    from relational_records import mm, add, branch_probabilities


R = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
I = eye(2)
PHI = [F(3, 5), F(4, 5)]


@cache
def P(n):
    if n < 0:
        return transpose(P(-n))
    out, base, k = I, R, n
    while k:
        if k % 2:
            out = mm(base, out)
        base = mm(base, base)
        k //= 2
    return out


def eta(f, moment=0):
    out = [F(0), F(0)]
    for n, v in f.items():
        transformed = mv(transpose(P(n)), v)
        weight = n**moment
        out = [a+weight*b for a, b in zip(out, transformed)]
    return out


def inner(f, g):
    return sum(dot(v, g.get(n, [F(0), F(0)])) for n, v in f.items())


def shift(f, k=1):
    return {n+k: mv(mm(P(n+k), transpose(P(n))), v) for n, v in f.items()}


def combine(*terms):
    out = {}
    for coefficient, f in terms:
        for n, v in f.items():
            old = out.get(n, [F(0), F(0)])
            out[n] = [a+coefficient*b for a, b in zip(old, v)]
    return {n: v for n, v in out.items() if any(v)}


def constraint(f):
    return combine((2, f), (-1, shift(f)), (-1, shift(f, -1)))


def dirac(v, A, n):
    return mm(mm(mm(mm(P(n), transpose(P(v))), A), P(v)), transpose(P(n)))


def apply_dirac(f, v, A):
    return {n: mv(dirac(v, A, n), x) for n, x in f.items()}


def core_adjoint(a):
    return {(m, n): transpose(b) for (n, m), b in a.items()}


def core_product(a, b):
    out = {}
    for (n, k), x in a.items():
        for (j, m), y in b.items():
            if k == j:
                out[n, m] = add(out.get((n, m), scale(0, I)), mm(x, y))
    return out


def history_functional(a, diagonal_only=False):
    total = F(0)
    for (n, m), b in a.items():
        if not diagonal_only or n == m:
            total += dot(PHI, mv(mm(mm(transpose(P(n)), b), P(m)), PHI))
    return total


def left_shift(a, k=1):
    return {(n+k, m): mm(mm(P(n+k), transpose(P(n))), b) for (n, m), b in a.items()}


def right_shift(a, k=1):
    return {(n, m-k): mm(b, mm(P(m), transpose(P(m-k)))) for (n, m), b in a.items()}


def corner(a, window):
    return {(n, m): b for (n, m), b in a.items() if n in window and m in window}


def local_state(a, window):
    return history_functional(corner(a, window))/len(window)


def run():
    X = [[F(0), F(1)], [F(1), F(0)]]
    Z = [[F(1), F(0)], [F(0), F(-1)]]
    f = {-2: [F(1), F(2)], 0: [F(3, 7), F(-1)], 3: [F(2), F(1, 5)]}
    g = {-1: [F(2, 3), F(1)], 1: [F(-2), F(1, 2)], 2: [F(0), F(3)]}
    differences = {n-m for n in f for m in g}
    average = sum(inner(f, shift(g, k)) for k in differences)
    assert average == dot(eta(f), eta(g))
    assert eta(shift(f)) == eta(f)
    assert eta(constraint(f)) == [F(0), F(0)]
    # Second-order distributional constraint alone allows an extra affine mode.
    assert eta(constraint(f), moment=1) == [F(0), F(0)]
    assert eta(shift(f), moment=1) == [a+b for a, b in zip(eta(f, moment=1), eta(f))]
    for A in (X, Z, mm(X, Z)):
        applied = apply_dirac(f, 1, A)
        assert eta(applied) == mv(mm(mm(transpose(P(1)), A), P(1)), eta(f))
        assert combine((1, shift(applied)), (-1, apply_dirac(shift(f), 1, A))) == {}
    quotient_null = combine((1, {0: PHI}), (-1, shift({0: PHI})))
    assert eta(quotient_null) == [F(0), F(0)] and inner(quotient_null, quotient_null) > 0
    # Algebraic core: positive functionals and exact translation Ward identities.
    a = {(-2, 0): R, (0, 1): X, (2, -1): Z, (0, 0): I}
    positive = core_product(core_adjoint(a), a)
    assert history_functional(positive) >= 0
    for core in (a, positive):
        assert history_functional(left_shift(core)) == history_functional(core)
        assert history_functional(right_shift(core)) == history_functional(core)
    E, window = {0, 1}, {-2, -1, 0, 1, 2}
    pE = {(n, n): I for n in E}
    assert local_state(pE, window) == F(len(E), len(window))
    assert local_state(corner(positive, E), window)/local_state(pE, window) == local_state(positive, E)
    windows = [{0}, {-1, 0, 1}, {-4, -3, 1, 2, 3, 7}]
    relative_value = dot(PHI, mv(mm(mm(transpose(P(1)), Z), P(1)), PHI))
    for Fset in windows:
        D = {(n, n): dirac(1, Z, n) for n in Fset}
        assert local_state(D, Fset) == relative_value
    # The coherent core is not the diagonal counting weight.
    transported_unit = {(1, -1): mm(P(1), transpose(P(-1)))}
    assert history_functional(transported_unit) == 1
    assert history_functional(transported_unit, diagonal_only=True) == 0
    pF = {(n, n): I for n in window}
    CpF = {}
    for coefficient, core in ((2, pF), (-1, left_shift(pF)), (-1, left_shift(pF, -1))):
        for key, b in core.items():
            CpF[key] = add(CpF.get(key, scale(0, I)), scale(coefficient, b))
    assert history_functional(CpF) == 0
    assert history_functional(CpF, diagonal_only=True) == 2*len(window)
    # Finite windows: exact boundary energy; these are approximate, not exact infinite-constraint vectors.
    boundary_checks = []
    for length in (1, 2, 3, 8, 16, 32):
        Fset = set(range(-(length//2), -(length//2)+length))
        vector = {n: mv(P(n), PHI) for n in Fset}
        cvector = constraint(vector)
        energy = inner(vector, cvector)/inner(vector, vector)
        residual = inner(cvector, cvector)/inner(vector, vector)
        assert energy == F(2, length)
        assert residual == (F(6) if length == 1 else F(4, length))
        boundary_checks.append({'length': length, 'constraint_energy': str(energy),
                                'squared_constraint_residual': str(residual)})
    disconnected = {-4, -3, 1, 2, 3, 7}
    vector = {n: mv(P(n), PHI) for n in disconnected}
    assert inner(vector, constraint(vector))/inner(vector, vector) == F(len(disconnected ^ {n+1 for n in disconnected}), len(disconnected))
    # Scalar root-frame form q(f)=|sum f_n|^2 is not closable in l2.
    closability = []
    previous = None
    for length in (1, 2, 8, 64, 512):
        v = {n: F(1, length) for n in range(length)}
        assert sum(v.values())**2 == 1
        assert sum(x*x for x in v.values()) == F(1, length)
        if previous is not None:
            assert (sum(v.values())-sum(previous.values()))**2 == 0
        closability.append({'length': length, 'l2_norm_squared': str(F(1, length)),
                            'history_form': '1'})
        previous = v
    # Infinite record process: previous two-event experiment followed by scalar Kraus writes.
    joint = branch_probabilities(PHI, R)
    coin = (F(9, 25), F(16, 25))
    assert F(3, 5)**2 + F(4, 5)**2 == 1
    def cylinder(prefix):
        if not prefix:
            return F(1)
        if len(prefix) == 1:
            return sum(joint[prefix[0]])
        p = joint[prefix[0]][prefix[1]]
        for a in prefix[2:]:
            p *= coin[a]
        return p
    for n in range(8):
        assert sum(cylinder(h) for h in product(range(2), repeat=n)) == 1
        for h in product(range(2), repeat=n):
            assert sum(cylinder(h+(a,)) for a in range(2)) == cylinder(h)
    # All four prior event effects have window-independent relational probabilities.
    projectors = [[[F(1), F(0)], [F(0), F(0)]], [[F(0), F(0)], [F(0), F(1)]]]
    for a0, a1 in product(range(2), repeat=2):
        B = mm(mm(projectors[a1], R), projectors[a0])
        effect = mm(transpose(B), B)
        for Fset in windows:
            D = {(n, n): dirac(0, effect, n) for n in Fset}
            assert local_state(D, Fset) == joint[a0][a1]
    return {
        'status': 'passed', 'arithmetic': 'exact rational; finite cores only',
        'rigging': 'group average, quotient null vectors, shift invariance and Dirac intertwining',
        'second_order_warning': 'affine distribution solves C but is not shift invariant',
        'coherent_core': 'positive; left/right Ward identities; conditional corner consistency',
        'coherence_not_diagonal_weight': {'off_diagonal_history': '1', 'off_diagonal_counting': '0'},
        'finite_window_boundary': boundary_checks,
        'normal_weight_nonclosability_witness': closability,
        'record_process': {'first_two_events': [[str(x) for x in row] for row in joint],
                           'tail_scalar_kraus_probabilities': ['9/25', '16/25'],
                           'prefix_normalization_and_consistency_through_length': 7,
                           'infinite_extension': 'analytic cylinder-algebra / Kolmogorov theorem'},
        'relational_event_probabilities': 'independent of every tested nonempty window',
        'not_claimed': ['a normalized stationary normal state of the infinite clock',
                        'a normal coherent clock weight', 'a derived clock or physical arrow',
                        'full gravitational time, outcome selection, or phenomenal ownership'],
    }


if __name__ == '__main__':
    result = run()
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: infinite-clock finite cores, rigging, boundary limits and record cylinders')
    print(target)
