#!/usr/bin/env python3
import unittest
from fractions import Fraction as F
from binocular_appearance_memory_gate import (appearance, histories, interaction,
                                                mismatch_bound, predictions, probe)


class BinocularMemoryGateTest(unittest.TestCase):
    def test_example_predictions(self):
        p = predictions(1, F(1, 4))
        self.assertEqual(p['A'], {'appearance': F(0), 'L': F(-1, 4), 'R': F(1, 4), 'both': F(0)})
        self.assertEqual(p['B'], {'appearance': F(0), 'L': F(1, 4), 'R': F(-1, 4), 'both': F(0)})
        self.assertEqual(interaction(p), F(1))

    def test_general_linear_formula_and_controls(self):
        for a in (F(0), F(1, 5), F(3, 2)):
            for k in (F(0), F(1, 3), F(2)):
                p = predictions(a, k)
                self.assertEqual(interaction(p), 4 * a * k)
                self.assertEqual(p['A']['both'], p['B']['both'])
                self.assertEqual(p['A']['appearance'], p['B']['appearance'])
                self.assertEqual(p['B']['L'], p['A']['R'])

    def test_mismatch_bound(self):
        self.assertEqual(mismatch_bound(F(1, 20), 1, 1), F(1, 10))
        self.assertEqual(mismatch_bound(F(1, 20), 2, 3), F(1, 4))
        self.assertEqual(mismatch_bound(0, 3, 3), 0)
        with self.assertRaises(ValueError):
            mismatch_bound(-1, 1, 1)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            histories(-1)
        with self.assertRaises(ValueError):
            probe((F(1), F(-1)), -1, 'L')
        with self.assertRaises(ValueError):
            probe((F(1), F(-1)), 1, 'center')
        self.assertEqual(appearance((F(2), F(-2))), 0)


if __name__ == '__main__':
    unittest.main()
