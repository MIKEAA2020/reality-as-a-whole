#!/usr/bin/env python3
"""Finite stationary-response controls; not evidence of experience."""
from fractions import Fraction as F
from itertools import product
import unittest


def stationary(a, source=F(0)):
    """Unique stationary solution for the specified triangle functional."""
    total = sum(a)
    return tuple((ai+total)/4 + source for ai in a)


def local_response(x, a):
    return tuple(xi-ai for xi, ai in zip(x, a))


def gradient(x, a, source=F(0)):
    return tuple(x[i]-a[i] + sum(x[i]-x[j] for j in range(3) if j != i) - source for i in range(3))


def functional(x, a, source=F(0)):
    local = sum((xi-ai)**2 for xi, ai in zip(x, a))/2
    coupling = sum((x[i]-x[j])**2 for i in range(3) for j in range(i+1, 3))/2
    return local + coupling-source*sum(x)


class StationaryResponseTests(unittest.TestCase):
    def test_exact_nontrivial_actual_example(self):
        a = (F(-8, 3), F(4, 3), F(4, 3))
        x = stationary(a)
        q = local_response(x, a)
        self.assertEqual(x, (F(-2, 3), F(1, 3), F(1, 3)))
        self.assertEqual(gradient(x, a), (0, 0, 0))
        self.assertEqual(q, (2, -1, -1))
        self.assertEqual(sum(q), 0)
        self.assertNotEqual(sorted(q), sorted(-v for v in q))
        self.assertEqual(functional(x, a), 4)

    def test_all_small_reference_triples_stationary_and_zero(self):
        for a in product(map(F, range(-2, 3)), repeat=3):
            x, q = stationary(a), local_response(stationary(a), a)
            self.assertEqual(gradient(x, a), (0, 0, 0))
            self.assertEqual(sum(q), 0)
            self.assertEqual(all(v == 0 for v in q), len(set(a)) == 1)
            for i in range(3):
                self.assertEqual(q[i], -sum(x[i]-x[j] for j in range(3) if j != i))

    def test_unique_minimum_by_exact_positive_difference(self):
        a = (F(1), F(-2), F(3))
        x = stationary(a)
        for d in product(map(F, range(-1, 2)), repeat=3):
            y = tuple(xi+di for xi, di in zip(x, d))
            delta = functional(y, a)-functional(x, a)
            expected = sum(di*di for di in d)/2 + sum((d[i]-d[j])**2 for i in range(3) for j in range(i+1, 3))/2
            self.assertEqual(delta, expected)
            self.assertEqual(delta == 0, d == (0, 0, 0))

    def test_common_origin_change_is_not_varying_x_alone(self):
        a = (F(1), F(-2), F(3))
        x = stationary(a)
        shift = F(5)
        shifted_x = tuple(v+shift for v in x)
        shifted_a = tuple(v+shift for v in a)
        self.assertEqual(functional(x, a), functional(shifted_x, shifted_a))
        self.assertEqual(local_response(x, a), local_response(shifted_x, shifted_a))
        self.assertGreater(functional(shifted_x, a), functional(x, a))

    def test_source_changes_partial_response_sum(self):
        a = (F(1), F(-2), F(3))
        for source in map(F, (-2, 0, 3)):
            x = stationary(a, source)
            self.assertEqual(gradient(x, a, source), (0, 0, 0))
            self.assertEqual(sum(local_response(x, a)), 3*source)

    def test_any_zero_sum_triple_can_be_fit_by_references(self):
        for q1, q2 in product(map(F, range(-3, 4)), repeat=2):
            q = (q1, q2, -q1-q2)
            a = tuple(-F(4, 3)*v for v in q)
            self.assertEqual(local_response(stationary(a), a), q)

    def test_collective_stationarity_without_individual_stationarity(self):
        # q=(1,-1,0) has zero sum; independent derivatives need not vanish.
        a = (F(0), F(0), F(0))
        x = (F(1), F(-1), F(0))
        self.assertEqual(sum(gradient(x, a)), 0)
        self.assertNotEqual(gradient(x, a), (0, 0, 0))


if __name__ == '__main__':
    unittest.main()
