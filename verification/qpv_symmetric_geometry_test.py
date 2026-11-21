#!/usr/bin/env python3
"""Independent numerical-area and set-membership controls for ideal symmetric toy."""
import math
import unittest
from fractions import Fraction as F
from scipy.integrate import quad
from qpv_symmetric_geometry import geometry, membership


class SymmetricGeometryTests(unittest.TestCase):
    def test_area_by_independent_cross_section_integration(self):
        for a, r in ((1, 2), (100, 110), (3, 10)):
            g = geometry(a, r)
            # The two integrations compute area from positive-x half widths;
            # the square-root integral is evaluated numerically, not from acos.
            lens = 4*quad(lambda x: math.sqrt(max(0., r*r-(x+a)**2)), 0, r-a, epsabs=1e-8)[0]
            ellipse = 4*quad(lambda x: math.sqrt(max(0., (r*r-a*a)*(1-x*x/(r*r)))), 0, r, epsabs=1e-8)[0]
            self.assertAlmostEqual(g['quantum_projected_area'], lens, delta=1e-8*max(1, lens))
            self.assertAlmostEqual(g['classical_projected_area'], ellipse, delta=1e-8*max(1, ellipse))

    def test_membership_and_verifier_nonremoteness_condition(self):
        self.assertEqual(membership(100, 110, 0, 40, 0), (True, True, True))
        self.assertEqual(membership(100, 110, 0, 46, 0), (False, False, False))
        self.assertEqual(membership(100, 110, -100, 0, 0), (False, True, True))
        # Once R >= 2a, the opposite sphere also contains a verifier.
        self.assertEqual(membership(100, 200, -100, 0, 0), (True, True, True))
        self.assertEqual(membership(100, 250, -100, 0, 0), (True, True, True))

    def test_ratios_and_invalid(self):
        self.assertEqual(geometry(100, 110)['volume_ratio'], F(231, 16))
        self.assertEqual(geometry(100, 110)['length_ratio'], 11)
        self.assertGreater(geometry(1, F(101, 100))['volume_ratio'], 100)
        self.assertLess(geometry(1, 1000)['volume_ratio'], F(1002, 1000))
        for args in ((0, 1), (1, 1), (2, 1)):
            with self.assertRaises(ValueError):
                geometry(*args)


if __name__ == '__main__':
    unittest.main()
