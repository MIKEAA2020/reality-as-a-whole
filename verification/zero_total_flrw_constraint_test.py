#!/usr/bin/env python3
"""Exact algebra checks for a restricted massless-scalar FLRW constraint.

Checks the equations used in ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md;
it does not derive GR, establish cosmology, or interpret the constraint as an
observable total energy. Uses rational units in which kappa=6.
"""
import unittest
from fractions import Fraction as F
from itertools import product

KAPPA = F(6)


def constraint(a, pa, pphi):
    return -KAPPA * pa * pa / (12 * a) + pphi * pphi / (2 * a**3)


def hamilton_derivatives(a, pa, pphi, lapse):
    da = -lapse * KAPPA * pa / (6 * a)
    dphi = lapse * pphi / a**3
    dpa = -lapse * (KAPPA * pa * pa / (12 * a**2) - 3 * pphi * pphi / (2 * a**4))
    return da, dphi, dpa


class FLRWConstraintTests(unittest.TestCase):
    def test_opposite_terms_and_positive_matter_density(self):
        for a, pphi, sign in product(map(F, (1, 2, 3)), map(F, (-2, -1, 1, 2)), (-1, 1)):
            pa = sign * pphi / a  # sqrt(6/kappa)=1
            grav = -KAPPA * pa**2 / (12 * a)
            matter = pphi**2 / (2 * a**3)
            self.assertEqual(grav + matter, 0)
            self.assertGreater(matter, 0)
            self.assertGreater(pphi**2 / (2 * a**6), 0)

    def test_relational_evolution_and_friedmann(self):
        for a, pphi, sign, lapse in product(map(F, (1, 2, 3)), map(F, (-2, -1, 1, 2)), (-1, 1), map(F, (1, 3))):
            pa = sign * pphi / a
            da, dphi, _ = hamilton_derivatives(a, pa, pphi, lapse)
            self.assertEqual(da / dphi, -sign * a)
            hubble = da / (lapse * a)
            density = pphi**2 / (2 * a**6)
            self.assertEqual(hubble**2, KAPPA * density / 3)

    def test_hamilton_equations_preserve_constraint(self):
        for a, pa, pphi, lapse in product(map(F, (1, 2, 3)), map(F, (-2, 1)), map(F, (-1, 2)), map(F, (1, 3))):
            da, _, dpa = hamilton_derivatives(a, pa, pphi, lapse)
            dc_da = KAPPA * pa**2 / (12 * a**2) - 3 * pphi**2 / (2 * a**4)
            dc_dpa = -KAPPA * pa / (6 * a)
            self.assertEqual(dc_da * da + dc_dpa * dpa, 0)

    def test_reversal_preserves_rather_than_negates_constraint(self):
        a, pa, pphi = F(2), F(1), F(3)
        c = constraint(a, pa, pphi)
        self.assertNotEqual(c, 0)
        self.assertEqual(constraint(a, -pa, -pphi), c)
        self.assertNotEqual(constraint(a, -pa, -pphi), -c)

    def test_shifted_constraint_is_a_different_equation(self):
        a, pa, pphi = F(1), F(0), F(2)
        c = constraint(a, pa, pphi)
        self.assertEqual(c, 2)
        self.assertNotEqual(c, 0)
        self.assertEqual(c - 2, 0)


if __name__ == '__main__':
    unittest.main()
