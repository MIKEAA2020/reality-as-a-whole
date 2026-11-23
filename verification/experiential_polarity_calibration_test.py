#!/usr/bin/env python3
"""Exact finite tests of a stipulated polarity map; not phenomenal evidence."""
from fractions import Fraction as F
from itertools import product
import unittest


def polarity(x, alpha):
    p, n, r = x
    return (alpha * n, p / alpha, r)


def linear_q(x, a, b, c):
    p, n, r = x
    return a*p + b*n + c*r


class PolarityCalibrationTests(unittest.TestCase):
    def test_involution_and_odd_linear_quantity(self):
        for alpha in (F(1, 2), F(1), F(2), F(3, 2)):
            for x in product(map(F, range(3)), repeat=3):
                y = polarity(x, alpha)
                self.assertEqual(polarity(y, alpha), x)
                self.assertEqual(y[0]-alpha*y[1], -(x[0]-alpha*x[1]))

    def test_coefficient_conditions_on_basis(self):
        basis = ((F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1)))
        for alpha in (F(1, 2), F(1), F(2)):
            for a, b, c in product(map(F, range(-2, 3)), repeat=3):
                odd = all(linear_q(polarity(x, alpha), a, b, c) == -linear_q(x, a, b, c) for x in basis)
                self.assertEqual(odd, b == -alpha*a and c == 0)

    def test_unit_change_preserves_zero_and_polarity(self):
        for alpha, u, v in product((F(1, 2), F(1), F(2)), repeat=3):
            for x in ((F(1), F(2), F(0)), (F(3), F(1), F(2))):
                p, n, r = x
                ap = u*alpha/v
                prime = (u*p, v*n, r)
                self.assertEqual(prime[0]-ap*prime[1], u*(p-alpha*n))
                mapped = polarity(x, alpha)
                self.assertEqual(polarity(prime, ap), (u*mapped[0], v*mapped[1], r))

    def test_paired_whole_has_zero_but_local_contributions_nonzero(self):
        alpha = F(2)
        x = (F(4), F(0), F(1))
        y = polarity(x, alpha)
        qx = x[0]-alpha*x[1]
        qy = y[0]-alpha*y[1]
        self.assertEqual((qx, qy), (4, -4))
        self.assertEqual(F(3)*qx + F(3)*qy, 0)
        self.assertNotEqual(F(2)*qx + F(3)*qy, 0)

    def test_map_existence_alone_does_not_make_whole_symmetric(self):
        alpha = F(1)
        xs = ((F(2), F(0), F(0)), (F(0), F(1), F(0)))
        self.assertEqual(sum(p-alpha*n for p, n, r in xs), 1)
        self.assertNotEqual(sorted(xs), sorted(polarity(x, alpha) for x in xs))

    def test_nonlinear_odd_quantity_exists(self):
        alpha = F(2)
        def cubic(x):
            return (x[0]-alpha*x[1])**3
        x, y = (F(1), F(0), F(0)), (F(2), F(0), F(0))
        self.assertEqual(cubic(polarity(x, alpha)), -cubic(x))
        self.assertNotEqual(cubic(tuple(a+b for a, b in zip(x,y))), cubic(x)+cubic(y))


if __name__ == '__main__':
    unittest.main()
