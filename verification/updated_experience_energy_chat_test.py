#!/usr/bin/env python3
"""Small exact checks for the updated experience/energy chat audit.

These are conditional arithmetic checks, not measures of experience or a
calculation of the actual universe's total energy.
"""
from fractions import Fraction as F
from itertools import product
import unittest


class UpdatedExperienceEnergyTests(unittest.TestCase):
    def test_zero_sum_with_positive_entry_requires_negative_entry(self):
        cases = 0
        for values in product(range(-3, 4), repeat=3):
            if sum(values) == 0 and any(v > 0 for v in values):
                self.assertTrue(any(v < 0 for v in values))
                cases += 1
        self.assertGreater(cases, 0)

    def test_valence_signs_do_not_set_equal_magnitudes(self):
        q = (1, -1)
        f = lambda x: 2*x if x >= 0 else x
        mapped = tuple(f(x) for x in q)
        self.assertEqual(sum(q), 0)
        self.assertEqual(mapped, (2, -1))
        self.assertEqual(sum(mapped), 1)
        self.assertTrue(all((x > 0) == (y > 0) and (x < 0) == (y < 0) for x, y in zip(q, mapped)))

    def test_zero_valence_does_not_mean_no_experience(self):
        actual_labelled_experiences = (('pleasant', 1), ('painful', -1))
        self.assertEqual(sum(v for _, v in actual_labelled_experiences), 0)
        self.assertEqual(len(actual_labelled_experiences), 2)

    def test_uniform_sphere_idealization(self):
        # GM/(Rc^2)=1/2 follows if R=c/H and rho=3H^2/(8pi G).
        potential_over_rest = -F(3, 5) * F(1, 2)
        kinetic_over_rest = F(3, 10)  # Newtonian homologous v=Hr, R=c/H
        self.assertEqual(potential_over_rest, -F(3, 10))
        self.assertEqual(kinetic_over_rest + potential_over_rest, 0)
        self.assertEqual(1 + kinetic_over_rest + potential_over_rest, 1)


if __name__ == '__main__':
    unittest.main()
