#!/usr/bin/env python3
"""Finite arithmetic controls, not a measurement or theory of experience."""
from fractions import Fraction as F
from itertools import product
import unittest


def totals(components):
    positive = sum(p for p, n, r in components)
    negative = sum(n for p, n, r in components)
    magnitude = sum(p + n + r for p, n, r in components)
    return positive - negative, magnitude, positive, negative


class ExperientialCandidateTests(unittest.TestCase):
    def test_zero_preserves_represented_magnitude(self):
        separate = [(F(1), F(0), F(0)), (F(0), F(1), F(0))]
        mixed = [(F(1), F(1), F(0))]
        neutral = [(F(0), F(0), F(2))]
        self.assertEqual(totals(separate)[:2], (0, 2))
        self.assertEqual(totals(mixed)[:2], (0, 2))
        self.assertEqual(totals(neutral)[:2], (0, 2))
        self.assertNotEqual(len(separate), len(mixed))

    def test_zero_with_negative_net_requires_positive_net(self):
        count = 0
        for q in product(range(-2, 3), repeat=3):
            if sum(q) == 0 and any(x < 0 for x in q):
                self.assertTrue(any(x > 0 for x in q))
                count += 1
        self.assertGreater(count, 0)

    def test_negative_component_does_not_entail_negative_net(self):
        mixed = (F(2), F(1), F(0))
        self.assertGreater(mixed[1], 0)
        self.assertGreater(mixed[0] - mixed[1], 0)

    def test_relative_scaling_can_force_zero(self):
        for positive, negative in product(map(F, (1, 2, 3)), repeat=2):
            alpha = positive / negative
            self.assertEqual(positive - alpha * negative, 0)
            self.assertNotEqual(positive - (alpha + 1) * negative, 0)

    def test_history_zero_does_not_imply_slice_zero(self):
        early, late = (2, -1), (-2, 1)
        self.assertEqual(sum(early), 1)
        self.assertEqual(sum(late), -1)
        self.assertEqual(sum(early + late), 0)

    def test_nonnegative_local_energy_not_directly_proportional_to_both_signs(self):
        for gamma in map(F, (-3, -1, 1, 3)):
            q = (F(1), F(-1))
            e = tuple(gamma * x for x in q)
            self.assertTrue(any(x < 0 for x in e))


if __name__ == '__main__':
    unittest.main()
