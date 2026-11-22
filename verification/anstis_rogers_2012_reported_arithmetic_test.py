#!/usr/bin/env python3
import unittest
from fractions import Fraction
from anstis_rogers_2012_reported_arithmetic import valid_xy, squared_distance, ratio, results


class ArithmeticTest(unittest.TestCase):
    def test_cie_triangle(self):
        self.assertTrue(valid_xy('0.3','0.4'))
        self.assertTrue(valid_xy('0.5','0.5'))
        self.assertFalse(valid_xy('0.627','0.667'))
        self.assertFalse(valid_xy('0.894','0.608'))
        self.assertFalse(valid_xy('-0.1','0.5'))

    def test_round_coordinate_distances(self):
        self.assertEqual(squared_distance(('0.454','0.448'),('0.440','0.452')),Fraction(212,1000000))
        x=results()
        self.assertAlmostEqual(x['exp2_ratio_from_printed_coordinates'],6.038399138094742)
        self.assertAlmostEqual(x['exp4_ratio_from_printed_coordinates'],4.033704157566492)
        with self.assertRaises(ValueError):ratio((('0','0'),('0','0')),(('1','0'),('0','0')))

    def test_probability_arithmetic(self):
        self.assertAlmostEqual(results()['hypothetical_independent_400_fair_binary_success_probability']/3.8725919148493183e-121,1)


if __name__=='__main__':unittest.main()
