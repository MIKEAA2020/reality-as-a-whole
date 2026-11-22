#!/usr/bin/env python3
"""Independent algebra, endpoint and potential-outcome checks for the synthetic contrast."""
from fractions import Fraction as F
from itertools import product
import unittest
from randomized_experience_contrast import stats


class ContrastTest(unittest.TestCase):
    def test_rate_rectangle_bounds_and_feasibility(self):
        # Independent fine rational grid: direct inversion, not verifier's bound code.
        deltas = []
        for s_int, f_int in product(range(75, 91), range(5, 21)):
            s, f = F(s_int,100), F(f_int,100)
            p0 = (F(1,2)-f)/(s-f)
            p1 = (F(7,10)-f)/(s-f)
            self.assertTrue(0 <= p0 <= p1 <= 1)
            deltas.append(p1-p0)
        self.assertEqual((min(deltas), max(deltas)), (F(4,17), F(4,11)))

    def test_same_marginals_different_joint_potential_outcomes(self):
        rates = [(F(9,10), F(1,20))]*2
        a = {(0,0): F(4,17), (0,1): F(4,17), (1,0): F(0), (1,1): F(9,17)}
        b = {(0,0): F(0), (0,1): F(8,17), (1,0): F(4,17), (1,1): F(5,17)}
        sa, sb = stats(a, rates), stats(b, rates)
        self.assertEqual((sa['q'], sa['p']), (sb['q'], sb['p']))
        self.assertEqual((sa['benefit'], sa['harm']), (F(4,17), F(0)))
        self.assertEqual((sb['benefit'], sb['harm']), (F(8,17), F(4,17)))
        for row in (sa, sb):
            self.assertEqual(row['benefit'] - row['harm'], row['p'][1] - row['p'][0])

    def test_channel_drift_generates_positive_report_contrast_without_effect(self):
        r = stats({(0,0): F(1,2), (1,1): F(1,2)},
                  [(F(9,10), F(1,10)), (F(9,10), F(1,2))])
        self.assertEqual(r['p'], [F(1,2), F(1,2)])
        self.assertEqual(r['q'], [F(1,2), F(7,10)])
        self.assertEqual((r['benefit'], r['harm']), (0, 0))

    def test_partial_identification_bounds_for_couplings(self):
        p0, p1 = F(9,17), F(13,17)
        lower = max(F(0), p1-p0)
        upper = min(p1, 1-p0)
        self.assertEqual((lower, upper), (F(4,17), F(8,17)))
        self.assertEqual((lower - (p1-p0), upper - (p1-p0)), (0, F(4,17)))


if __name__ == '__main__':
    unittest.main()
