#!/usr/bin/env python3
"""Independent algebra and numerical checks for the constructed scalar example."""
import math
import unittest
from fractions import Fraction as F
from chemotaxis_integral_feedback_example import activity, drift, simulate, time_to_z, invert_time


class IntegralFeedbackExampleTest(unittest.TestCase):
    def test_exact_equilibria_and_saturation(self):
        # Independent rational arithmetic, including the unconstrained boundary flux.
        for L in range(1, 10):
            z = F(L-1)
            A = (1+z)/(1+z+F(L))
            self.assertEqual(A, F(1, 2))
        z, L = F(2), F(8)
        A = (1+z)/(1+z+L)
        self.assertEqual(A, F(3, 11))
        self.assertEqual(F(1, 2)-A, F(5, 22))
        self.assertGreater(drift(2, 8), 0)

    def test_activity_direction(self):
        for L in (1, 2, 8):
            for z in (0, 0.5, 2, 7):
                self.assertGreater(activity(z+0.01, L), activity(z, L))
                self.assertLess(activity(z, L+0.01), activity(z, L))

    def test_analytic_inversion_and_rk4(self):
        for gain in (0.5, 1, 2):
            for t in (1.0, 4.0, 10.0):
                z = invert_time(t, 2, gain)
                self.assertAlmostEqual(time_to_z(z, 2, gain), t, places=10)
                self.assertAlmostEqual(simulate(2, gain=gain, time=t, dt=0.002)['z'], z, places=8)

    def test_bounded_after_hit_and_frozen_no_adaptation(self):
        self.assertLess(time_to_z(2, 8), 20)
        self.assertAlmostEqual(simulate(8, cap=2, time=20, dt=0.002)['activity'], 3/11)
        self.assertAlmostEqual(activity(0, 2), 1/3)
        self.assertNotEqual(activity(0, 2), 0.5)

    def test_hit_formula(self):
        self.assertAlmostEqual(time_to_z(2, 8), -4-32*math.log(F(5, 7)), places=12)


if __name__ == '__main__':
    unittest.main()
