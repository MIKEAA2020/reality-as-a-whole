#!/usr/bin/env python3
"""Boundary and constructive tests for the retrospective axial-geometry audit."""
import unittest
from fractions import Fraction as F
from kavuri_qpv_axial_identity import axial_geometry, intersect, union


class AxialIdentityTest(unittest.TestCase):
    def test_lightcone_boundaries_and_positive_overlap(self):
        # Both pairs exactly lightlike, and the quantum interval has positive length.
        p = axial_geometry(2, 0, 2, 6, 4)
        self.assertIsNotNone(p)
        self.assertTrue(p['condition_release'] and p['condition_response'])
        self.assertEqual(p['qlen'], 2)
        self.assertEqual(p['clen'], 4)
        self.assertEqual(p['classical'], [(F(-2), F(2))])

    def test_zero_length_intersection_is_excluded(self):
        # Opposing balls touch at one point; it has no positive 1D measure.
        self.assertIsNone(axial_geometry(2, 0, 0, 2, 2))

    def test_degenerate_ellipsoid_is_excluded(self):
        # One ellipsoid has major-axis length equal to focal separation.
        self.assertIsNone(axial_geometry(2, 0, 2, 4, 6))

    def test_negative_and_zero_round_trip_excluded(self):
        self.assertIsNone(axial_geometry(2, 0, 0, 0, 6))
        self.assertIsNone(axial_geometry(2, 0, 0, -1, 6))
        self.assertIsNone(axial_geometry(0, 0, 0, 6, 6))

    def test_condition_violations_not_equivalent(self):
        p = axial_geometry(1, 0, -1, 1, 3)
        self.assertTrue(p['condition_release'])
        self.assertFalse(p['condition_response'])
        self.assertEqual((p['qlen'], p['clen']), (1, 3))
        self.assertNotEqual(p['clen'], 1 + p['qlen'])
        p = axial_geometry(1, 0, -8, 1, 2)
        self.assertFalse(p['condition_release'])
        self.assertTrue(p['condition_response'])
        self.assertEqual(p['clen'], 1 + p['qlen'])

    def test_interval_operations(self):
        self.assertIsNone(intersect((0, 1), (1, 2)))
        self.assertEqual(union([(0, 2), (1, 3), (5, 6), None]), [(0, 3), (5, 6)])

    def test_reported_inputs_exact_arithmetic(self):
        p = axial_geometry('195.1', '1291.0', '1429.1', '2340.3', '2207.7', '0.299792458')
        self.assertTrue(p['condition_release'] and p['condition_response'])
        self.assertEqual(p['qlen'], F(788953169891, 10000000000))
        self.assertEqual(p['clen'], F('195.1') + p['qlen'])
        self.assertAlmostEqual(float(p['clen']/p['qlen']), 3.4728970925733726)


if __name__ == '__main__':
    unittest.main()
