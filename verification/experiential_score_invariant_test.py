#!/usr/bin/env python3
"""Exact finite score controls, not measurements of experiential valence."""
from fractions import Fraction as F
from math import sqrt
import unittest


def scores(p, derivative):
    if len(p) != len(derivative) or not p or any(x <= 0 for x in p):
        raise ValueError('fixed positive support required')
    if sum(p) != 1 or sum(derivative) != 0:
        raise ValueError('normalization and normalized tangent required')
    s = [d / w for w, d in zip(p, derivative)]
    information = sum(w*x*x for w, x in zip(p, s))
    return s, information


class ScoreInvariantTests(unittest.TestCase):
    def setUp(self):
        self.p = [F(1, 3)]*3
        self.dp = [F(2, 3), F(-1, 3), F(-1, 3)]

    def test_weighted_zero_and_nonzero_norm(self):
        s, information = scores(self.p, self.dp)
        self.assertEqual(s, [2, -1, -1])
        self.assertEqual(sum(w*x for w, x in zip(self.p, s)), 0)
        self.assertEqual(information, 2)
        u = [float(x)/sqrt(float(information)) for x in s]
        self.assertAlmostEqual(sum(float(w)*x*x for w, x in zip(self.p, u)), 1)
        self.assertFalse(any(x == -s[0] for x in s))

    def test_reparameterization_and_orientation(self):
        s, information = scores(self.p, self.dp)
        for factor in map(F, (F(1, 3), 2, -3)):
            transformed, info2 = scores(self.p, [factor*x for x in self.dp])
            self.assertEqual(transformed, [factor*x for x in s])
            self.assertEqual(info2, factor*factor*information)
            u = [float(x)/sqrt(float(info2)) for x in transformed]
            for got, original in zip(u, s):
                self.assertAlmostEqual(got, (1 if factor > 0 else -1)*float(original)/sqrt(float(information)))

    def test_same_state_different_tangents(self):
        first, _ = scores(self.p, self.dp)
        second, _ = scores(self.p, [F(-1, 3), F(2, 3), F(-1, 3)])
        self.assertEqual(second, [-1, 2, -1])
        self.assertNotEqual(first, second)

    def test_any_zero_mean_vector_can_be_score(self):
        for p, v in [([F(1, 3)]*3, [F(2), F(-1), F(-1)]),
                     ([F(1, 4), F(3, 4)], [F(3), F(-1)])]:
            dp = [w*x for w, x in zip(p, v)]
            result, _ = scores(p, dp)
            self.assertEqual(result, v)
            for t in (F(-1, 10), F(1, 10)):
                perturbed = [w*(1+t*x) for w, x in zip(p, v)]
                self.assertTrue(all(w > 0 for w in perturbed))
                self.assertEqual(sum(perturbed), 1)

    def test_coarse_graining_loses_information(self):
        s, info = scores(self.p, self.dp)
        # Merge components 0 and 1, leave component 2 separate.
        p2 = [self.p[0]+self.p[1], self.p[2]]
        dp2 = [self.dp[0]+self.dp[1], self.dp[2]]
        s2, info2 = scores(p2, dp2)
        self.assertEqual(s2, [F(1, 2), F(-1)])
        self.assertEqual(info2, F(1, 2))
        self.assertLess(info2, info)
        self.assertEqual(sum(w*x for w, x in zip(p2, s2)), 0)

    def test_stationary_tangent_cannot_be_normalized(self):
        s, info = scores(self.p, [F(0)]*3)
        self.assertEqual(s, [0, 0, 0])
        self.assertEqual(info, 0)
        with self.assertRaises(ZeroDivisionError):
            _ = s[0] / sqrt(float(info))

    def test_bad_support_or_derivative_rejected(self):
        with self.assertRaises(ValueError):
            scores([F(1), F(0)], [F(0), F(0)])
        with self.assertRaises(ValueError):
            scores(self.p, [F(1), F(0), F(0)])


if __name__ == '__main__':
    unittest.main()
