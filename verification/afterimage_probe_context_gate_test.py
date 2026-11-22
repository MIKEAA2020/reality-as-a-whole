#!/usr/bin/env python3
import unittest
from fractions import Fraction as F
from afterimage_probe_context_gate import (selective_margin, criterion_margin,
                                            common_gain_margin, probability,
                                            decision_point, run)


class ProbeContextTest(unittest.TestCase):
    def test_all_grid_choices_and_counts(self):
        out = run()
        self.assertEqual(out['grid']['number_of_conditions'], 30)
        self.assertTrue(out['all_selective_and_criterion_choice_probabilities_equal'])
        self.assertTrue(out['no_adaptation_probabilities_equal_across_contexts'])

    def test_equivalence_beyond_grid(self):
        for p in (F(-5, 3), F(2, 7), F(3, 2)):
            for h in (F(-1, 3), F(0), F(7, 5)):
                for g in (F(1, 4), F(1), F(7, 3)):
                    self.assertEqual(selective_margin(p, h, g), criterion_margin(p, h, g))

    def test_null_points_and_common_gain(self):
        for h in (F(-2), F(0), F(1)):
            for g in (F(1, 2), F(1), F(2)):
                self.assertEqual(decision_point(h, g, g, 0), h)
                self.assertEqual(common_gain_margin(h, h, g), 0)
                self.assertEqual(decision_point(h, g, 1, 0), g*h)
                self.assertEqual(decision_point(h, 1, 1, (g-1)*h), g*h)
        with self.assertRaises(ValueError):
            decision_point(1, 1, 0, 0)

    def test_probability_domain(self):
        self.assertEqual(probability(F(0)), F(1, 2))
        with self.assertRaises(ValueError):
            probability(F(9))


if __name__ == '__main__':
    unittest.main()
