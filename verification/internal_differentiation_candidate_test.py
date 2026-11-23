#!/usr/bin/env python3
"""Exact finite functional checks; not evidence of physical experience."""
from fractions import Fraction as F
from itertools import permutations, product
import unittest


def centered(x):
    mean = sum(x)/3
    return tuple(v-mean for v in x)


def norm2(x):
    return sum(v*v for v in x)


def laplacian(x):
    return tuple(sum(x[i]-x[j] for j in range(3) if j != i) for i in range(3))


def optimal_y(x):
    mean = sum(x)/3
    return tuple(mean + v/4 for v in centered(x))


def functional(x, y, mu, lam):
    z = centered(x)
    r2 = norm2(z)
    xy = sum((a-b)**2 for a, b in zip(x, y))/2
    xx = sum((x[i]-x[j])**2 for i in range(3) for j in range(i+1, 3))/2
    yy = sum((y[i]-y[j])**2 for i in range(3) for j in range(i+1, 3))/2
    return xy+xx+yy-mu*r2/2+lam*r2*r2/4


def gradient(x, y, mu, lam):
    z = centered(x)
    r2 = norm2(z)
    lx, ly = laplacian(x), laplacian(y)
    gx = tuple(x[i]-y[i]+lx[i]+(-mu+lam*r2)*z[i] for i in range(3))
    gy = tuple(y[i]-x[i]+ly[i] for i in range(3))
    return gx, gy


class InternalDifferentiationTests(unittest.TestCase):
    def test_elimination_and_zero_response(self):
        for x in product(map(F, range(-2, 3)), repeat=3):
            y = optimal_y(x)
            z = centered(x)
            q = tuple(a-b for a, b in zip(x, y))
            self.assertEqual(q, tuple(3*v/4 for v in z))
            self.assertEqual(sum(q), 0)
            self.assertEqual(gradient(x, y, F(1), F(1))[1], (0, 0, 0))
            self.assertEqual(functional(x, y, F(1), F(1)), F(11, 8)*norm2(z)+norm2(z)**2/4)

    def test_y_minimizer_is_unique_for_fixed_x(self):
        x = (F(2), F(-1), F(3))
        y = optimal_y(x)
        for delta in product(map(F, range(-1, 2)), repeat=3):
            y2 = tuple(a+b for a, b in zip(y, delta))
            diff = functional(x, y2, F(53, 12), F(1))-functional(x, y, F(53, 12), F(1))
            expected = norm2(delta)/2 + sum((delta[i]-delta[j])**2 for i in range(3) for j in range(i+1, 3))/2
            self.assertEqual(diff, expected)
            self.assertEqual(diff == 0, delta == (0, 0, 0))

    def test_exact_nonuniform_global_minimum(self):
        mu, lam = F(53, 12), F(1)
        x = (F(2, 3), F(-1, 3), F(-1, 3))
        y = optimal_y(x)
        q = tuple(a-b for a, b in zip(x, y))
        self.assertEqual(norm2(centered(x)), F(2, 3))
        self.assertEqual(y, (F(1, 6), F(-1, 12), F(-1, 12)))
        self.assertEqual(q, (F(1, 2), F(-1, 4), F(-1, 4)))
        self.assertEqual(gradient(x, y, mu, lam), ((0, 0, 0), (0, 0, 0)))
        self.assertEqual(functional(x, y, mu, lam), F(-1, 9))
        self.assertEqual(sorted(q), [F(-1, 4), F(-1, 4), F(1, 2)])
        self.assertNotEqual(sorted(q), sorted(-v for v in q))

    def test_global_lower_bound_in_unstable_regime(self):
        mu, lam = F(53, 12), F(1)
        r0sq = (mu-F(15, 4))/lam
        for x in product(map(F, range(-2, 3)), repeat=3):
            y = optimal_y(x)
            r2 = norm2(centered(x))
            self.assertEqual(functional(x, y, mu, lam)+F(1, 9), (r2-r0sq)**2/4)
            self.assertGreaterEqual(functional(x, y, mu, lam), F(-1, 9))

    def test_uniform_regime_and_threshold(self):
        for mu in (F(2), F(15, 4)):
            for x in product(map(F, range(-2, 3)), repeat=3):
                y = optimal_y(x)
                value = functional(x, y, mu, F(1))
                self.assertGreaterEqual(value, 0)
                self.assertEqual(value == 0, len(set(x)) == 1)

    def test_symmetry_and_multiple_minima(self):
        mu, lam = F(53, 12), F(1)
        x = (F(2, 3), F(-1, 3), F(-1, 3))
        y = optimal_y(x)
        flipped = tuple(-v for v in x)
        self.assertNotIn(flipped, set(permutations(x)))
        self.assertEqual(functional(flipped, optimal_y(flipped), mu, lam), functional(x, y, mu, lam))
        shifted_x, shifted_y = tuple(v+5 for v in x), tuple(v+5 for v in y)
        self.assertEqual(functional(shifted_x, shifted_y, mu, lam), functional(x, y, mu, lam))
        for order in permutations(range(3)):
            self.assertEqual(functional(tuple(x[i] for i in order), tuple(y[i] for i in order), mu, lam), functional(x, y, mu, lam))

    def test_uniform_stationary_even_when_not_global_minimum(self):
        mu, lam = F(53, 12), F(1)
        zero = (F(0),)*3
        self.assertEqual(gradient(zero, zero, mu, lam), (zero, zero))
        self.assertEqual(functional(zero, zero, mu, lam), 0)
        x = (F(2, 3), F(-1, 3), F(-1, 3))
        self.assertLess(functional(x, optimal_y(x), mu, lam), 0)


if __name__ == '__main__':
    unittest.main()
