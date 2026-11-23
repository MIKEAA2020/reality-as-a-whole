#!/usr/bin/env python3
"""Weighted finite variational controls; not a physical or phenomenal theory."""
from fractions import Fraction as F
from itertools import product
import unittest


def mean(values, weights):
    return sum(w*v for w, v in zip(weights, values))/sum(weights)


def variance(values, weights):
    avg = mean(values, weights)
    return mean([(v-avg)**2 for v in values], weights)


def ystar(x, weights, k):
    avg = mean(x, weights)
    return tuple(avg+(v-avg)/(1+k) for v in x)


def functional(x, y, weights, k, a, m, lam):
    r = variance(x, weights)
    return (mean([(v-w)**2 for v, w in zip(x, y)], weights)/2
            + k*variance(y, weights)/2 + (a-m)*r/2 + lam*r*r/4)


def gradient_density(x, y, weights, k, a, m, lam):
    xbar, ybar = mean(x, weights), mean(y, weights)
    r = variance(x, weights)
    gx = tuple(xi-yi+(a-m+lam*r)*(xi-xbar) for xi, yi in zip(x, y))
    gy = tuple(yi-xi+k*(yi-ybar) for xi, yi in zip(x, y))
    return gx, gy


class RelationalActualHistoryTests(unittest.TestCase):
    def test_two_actual_histories_and_global_minimum(self):
        x, weights = (F(2), F(-1), F(-1)), (F(1),)*3
        k, a, m, lam = F(1), F(1), F(7, 2), F(1)
        y = ystar(x, weights, k)
        q = tuple(v-w for v, w in zip(x, y))
        self.assertEqual(y, (1, F(-1, 2), F(-1, 2)))
        self.assertEqual(q, (1, F(-1, 2), F(-1, 2)))
        self.assertEqual(variance(x, weights), 2)
        self.assertEqual((sum(q[:2]), q[2], sum(q)), (F(1, 2), F(-1, 2), 0))
        self.assertEqual(functional(x, y, weights, k, a, m, lam), -1)
        self.assertEqual(gradient_density(x, y, weights, k, a, m, lam), ((0, 0, 0), (0, 0, 0)))
        self.assertEqual(mean([v*v for v in q], weights), F(1, 2))

    def test_weighted_complete_square_and_zero(self):
        weights = (F(1), F(2), F(3))
        k, a, m, lam = F(2), F(1), F(5), F(1)
        r0 = (m-a-k/(1+k))/lam
        for x in product(map(F, range(-1, 2)), repeat=3):
            ys = ystar(x, weights, k)
            q = tuple(v-w for v, w in zip(x, ys))
            self.assertEqual(mean(q, weights), 0)
            for y in product(map(F, range(-1, 2)), repeat=3):
                d = tuple(v-w for v, w in zip(y, ys))
                residual = (lam*(variance(x, weights)-r0)**2/4
                            + mean([v*v for v in d], weights)/2
                            + k*variance(d, weights)/2)
                self.assertEqual(functional(x, y, weights, k, a, m, lam)+lam*r0*r0/4, residual)
                self.assertGreaterEqual(residual, 0)

    def test_common_origin_and_clock_segment_redescription(self):
        x, y, w = (F(2), F(-1), F(-1)), (F(1), F(-1, 2), F(-1, 2)), (F(1),)*3
        args = (F(1), F(1), F(7, 2), F(1))
        baseline = functional(x, y, w, *args)
        self.assertEqual(functional(tuple(v+7 for v in x), tuple(v+7 for v in y), w, *args), baseline)
        # The same first segment is partitioned into two equal-measure views.
        self.assertEqual(functional((x[0], x[0], x[1], x[2]), (y[0], y[0], y[1], y[2]),
                                    (F(1, 2), F(1, 2), F(1), F(1)), *args), baseline)

    def test_changing_a_physical_weight_changes_the_stationary_response(self):
        x = (F(2), F(-1), F(-1))
        old_w, new_w = (F(1),)*3, (F(1), F(1), F(2))
        old_y, new_y = ystar(x, old_w, F(1)), ystar(x, new_w, F(1))
        old_q = tuple(v-w for v, w in zip(x, old_y))
        new_q = tuple(v-w for v, w in zip(x, new_y))
        self.assertNotEqual(sum(w*q for w, q in zip(new_w, old_q)), 0)
        self.assertEqual(sum(w*q for w, q in zip(new_w, new_q)), 0)
        self.assertNotEqual(old_q, new_q)

    def test_uniform_configuration_remains_stationary(self):
        x = y = (F(5),)*3
        weights = (F(1), F(2), F(3))
        self.assertEqual(gradient_density(x, y, weights, F(1), F(1), F(7, 2), F(1)), ((0, 0, 0), (0, 0, 0)))
        self.assertEqual(functional(x, y, weights, F(1), F(1), F(7, 2), F(1)), 0)

    def test_reverse_fit_of_zero_mean_profile(self):
        w, k, a, lam = (F(1),)*3, F(1), F(1), F(1)
        for q in ((F(1), F(-1, 2), F(-1, 2)), (F(-2), F(1), F(1))):
            self.assertEqual(mean(q, w), 0)
            x = tuple((1+k)*v/k for v in q)
            y = tuple(v/(1+k) for v in x)
            m = a+k/(1+k)+lam*mean([v*v for v in x], w)
            self.assertEqual(ystar(x, w, k), y)
            self.assertEqual(tuple(v-t for v, t in zip(x, y)), q)
            self.assertEqual(gradient_density(x, y, w, k, a, m, lam), ((0, 0, 0), (0, 0, 0)))
            self.assertEqual(variance(x, w), (m-a-k/(1+k))/lam)


if __name__ == '__main__':
    unittest.main()
