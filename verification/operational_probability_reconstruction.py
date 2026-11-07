"""Exact rational-complex verification of a positive probability reconstruction.

The general C*-algebra theorem is proved in OPERATIONAL_PROBABILITY_RECONSTRUCTION.md.
These finite checks test its formulas, an explicit qubit obstruction, and two
instruments with identical effects but different conditional dynamics. They are
not empirical measurements, a novel theorem, or phenomenal assignments.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import json


@dataclass(frozen=True)
class G:
    re: Q = Q(0)
    im: Q = Q(0)

    def __add__(self, other):
        other = scalar(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-scalar(other))

    def __mul__(self, other):
        other = scalar(other)
        return G(self.re*other.re - self.im*other.im,
                 self.re*other.im + self.im*other.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)


def scalar(x):
    return x if isinstance(x, G) else G(Q(x))


def matrix(rows):
    return tuple(tuple(scalar(x) for x in row) for row in rows)


I = matrix(((1, 0), (0, 1)))
ZERO = matrix(((0, 0), (0, 0)))
P0 = matrix(((1, 0), (0, 0)))
P1 = matrix(((0, 0), (0, 1)))
PX = matrix(((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2))))
PY = matrix(((Q(1, 2), G(0, Q(-1, 2))),
             (G(0, Q(1, 2)), Q(1, 2))))
PN = matrix(((Q(4, 5), Q(2, 5)), (Q(2, 5), Q(1, 5))))
PV = matrix(((Q(9, 25), Q(12, 25)), (Q(12, 25), Q(16, 25))))
PC = matrix(((Q(9, 25), G(0, Q(-12, 25))),
             (G(0, Q(12, 25)), Q(16, 25))))


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def scale(t, a):
    return tuple(tuple(scalar(t)*x for x in row) for row in a)


def sub(a, b):
    return add(a, scale(-1, b))


def mul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)), G())
                       for j in range(2)) for i in range(2))


def adjoint(a):
    return tuple(tuple(a[j][i].conj() for j in range(2)) for i in range(2))


def trace(a):
    return a[0][0] + a[1][1]


def positive(a):
    if adjoint(a) != a:
        return False
    determinant = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    return (a[0][0].im == a[1][1].im == determinant.im == 0
            and a[0][0].re >= 0 and a[1][1].re >= 0
            and determinant.re >= 0)


def effect(a):
    return positive(a) and positive(sub(I, a))


def probability(rho, e):
    if not positive(rho) or trace(rho) != G(1):
        raise ValueError('A positive trace-one state is required')
    if not effect(e):
        raise ValueError('An operator between zero and identity is required')
    p = trace(mul(rho, e))
    assert p.im == 0 and 0 <= p.re <= 1
    return p.re


def instrument(rho, k):
    output = mul(mul(k, rho), adjoint(k))
    p = trace(output)
    assert p.im == 0 and p.re >= 0 and positive(output)
    if p.re == 0:
        assert output == ZERO
        return p.re, None
    conditional = scale(1/p.re, output)
    assert positive(conditional) and trace(conditional) == G(1)
    return p.re, conditional


def run():
    projectors = (P0, PX, PY, PN, PV, PC)
    states = (P0, P1, PX, sub(I, PX), PY, sub(I, PY),
              PN, PC, scale(Q(1, 2), I))
    for p in projectors:
        assert mul(p, p) == p and effect(p) and trace(p) == G(1)
    contexts = 0
    outcome_probabilities = 0
    for rho in states:
        for p in projectors:
            for na in range(5):
                for nb in range(5):
                    a, b = Q(na, 4), Q(nb, 4)
                    e0, e1 = scale(a, p), scale(b, sub(I, p))
                    e2 = sub(I, add(e0, e1))
                    probs = tuple(probability(rho, e) for e in (e0, e1, e2))
                    assert sum(probs) == 1
                    assert probability(rho, add(e0, e1)) == probs[0] + probs[1]
                    assert probability(rho, e0) == a*probability(rho, p)
                    contexts += 1
                    outcome_probabilities += 3

    # A nonlinear projective assignment f(P_n)=(1+n_z^3)/2 is normalized
    # on every qubit binary projective test, but cannot extend to all effects.
    def nonlinear_projector(p):
        assert mul(p, p) == p and trace(p) == G(1)
        nz = p[0][0].re - p[1][1].re
        return (1 + nz**3)/2

    for p in projectors:
        assert nonlinear_projector(p) + nonlinear_projector(sub(I, p)) == 1
    e_left = add(scale(Q(1, 2), PN), scale(Q(1, 10), I))
    e_right = add(scale(Q(2, 5), PX), scale(Q(3, 10), P0))
    assert e_left == e_right and effect(e_left)
    bad_left = Q(1, 2)*nonlinear_projector(PN) + Q(1, 10)
    bad_right = Q(2, 5)*nonlinear_projector(PX) + Q(3, 10)*nonlinear_projector(P0)
    assert bad_left == Q(101, 250) and bad_right == Q(1, 2)
    assert bad_left != bad_right
    for rho in states:
        left = Q(1, 2)*probability(rho, PN) + Q(1, 10)
        right = Q(2, 5)*probability(rho, PX) + Q(3, 10)*probability(rho, P0)
        assert left == right == probability(rho, e_left)

    # Same first-readout effects for every input; different actual instruments.
    luders = (P0, P1)
    reset = (matrix(((Q(3, 5), 0), (Q(4, 5), 0))),
             matrix(((0, Q(3, 5)), (0, Q(4, 5)))))
    for family in (luders, reset):
        assert add(*(mul(adjoint(k), k) for k in family)) == I
    for kl, kr, p in zip(luders, reset, (P0, P1)):
        assert mul(adjoint(kl), kl) == mul(adjoint(kr), kr) == p
        for rho in states:
            pl, _ = instrument(rho, kl)
            pr, _ = instrument(rho, kr)
            assert pl == pr == probability(rho, p)
    mixed = scale(Q(1, 2), I)
    pl, rl = instrument(mixed, luders[0])
    pr, rr = instrument(mixed, reset[0])
    assert rl == P0 and rr == PV and pl == pr == Q(1, 2)
    joint_l = pl*probability(rl, PV)
    joint_r = pr*probability(rr, PV)
    assert joint_l == Q(9, 50) and joint_r == Q(1, 2)
    assert probability(PX, PX) == 1
    assert probability(mixed, PX) == Q(1, 2)
    assert probability(PX, P0) == probability(mixed, P0) == Q(1, 2)
    for rho, e in ((I, P0), (mixed, scale(2, I))):
        try:
            probability(rho, e)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid state/effect accepted')
    return {
        'status': 'passed',
        'arithmetic': 'exact rational complex; no floating point',
        'states_checked': len(states),
        'projector_directions_checked': len(projectors),
        'three_outcome_POVM_contexts': contexts,
        'outcome_probabilities_checked': outcome_probabilities,
        'nonlinear_projective_assignment_same_effect_values':
            [str(bad_left), str(bad_right)],
        'same_first_readout_effects_for_both_instruments': True,
        'postselection_sequential_joint_probabilities':
            {'luders': str(joint_l), 'reset': str(joint_r)},
        'coherent_vs_dephased_future_test_probabilities': ['1', '1/2'],
        'general_Cstar_extension_proved_in_report_not_by_finite_enumeration': True,
        'normality_not_assumed_or_proved_by_finite_checks': True,
        'quantum_algebra_derived_from_metaphysics': False,
        'specific_physical_state_derived': False,
        'cosmic_observer_measure_derived': False,
        'phenomenal_identity_established': False,
        'scope': 'positive mathematical reconstruction and exact instrument distinction; not experimental data or zero-residue completion',
    }


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f"PASS: {result['three_outcome_POVM_contexts']} POVMs, {result['outcome_probabilities_checked']} exact probabilities, nonlinear obstruction and equal-effect/different-update witness.")
