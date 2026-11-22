#!/usr/bin/env python3
"""Independent elementary checks of the illustrative witness."""
from fractions import Fraction as F
import unittest
from graded_rivalry_witness import spatial_traces, causal_three_point


class GradedWitnessTest(unittest.TestCase):
    def test_local_patterns_distinct_but_spatial_totals_match(self):
        binary, uniform, a, b = spatial_traces()
        self.assertEqual(a, [F(k, 4) for k in range(5)])
        self.assertEqual(a, b)
        for k in (1, 2, 3):
            self.assertNotEqual(binary[k], uniform[k])
            self.assertEqual(sum(binary[k]), sum(uniform[k]))
            self.assertTrue(all(x in (0, 1) for x in binary[k]))
            self.assertTrue(all(x == F(k,4) for x in uniform[k]))

    def test_one_sample_pulse_never_changes_sign(self):
        self.assertEqual(causal_three_point([-1,-1,1,-1,-1,-1]),
                         [F(-1), F(-1), F(-1,3), F(-1,3), F(-1,3), F(-1)])

    def test_two_sample_pulse_does_change_sign(self):
        self.assertEqual(causal_three_point([-1,-1,1,1,-1,-1,-1]),
                         [F(-1), F(-1), F(-1,3), F(1,3), F(1,3), F(-1,3), F(-1)])

    def test_one_sample_pulse_visible_without_smoothing(self):
        signal = [-1,-1,1,-1,-1,-1]
        self.assertEqual(sum(x > 0 for x in signal), 1)
        self.assertEqual(sum(x > 0 for x in causal_three_point(signal)), 0)


if __name__ == '__main__':
    unittest.main()
