#!/usr/bin/env python3
"""Exact orientation controls; not proof of physical or experiential symmetry."""
from fractions import Fraction as F
from itertools import permutations, product
import unittest

from verification.internal_differentiation_candidate_test import (
    centered, functional, norm2, optimal_y,
)


MU, LAM, KAPPA = F(23, 4), F(1), F(1)


def prod3(values):
    return values[0]*values[1]*values[2]


def phi(x, y):
    return functional(x, y, MU, LAM)+KAPPA*prod3(centered(x))**2


def gap_formula(x, y):
    z = centered(x)
    y0 = optimal_y(x)
    d = tuple(v-w for v, w in zip(y, y0))
    edges = sum((d[i]-d[j])**2 for i in range(3) for j in range(i+1, 3))/2
    return (norm2(z)-2)**2/4+KAPPA*prod3(z)**2+norm2(d)/2+edges


class IntrinsicOrientationTests(unittest.TestCase):
    def test_exact_square_identity_for_distinct_x_and_y(self):
        for x in product(map(F, range(-1, 2)), repeat=3):
            for y in product(map(F, range(-1, 2)), repeat=3):
                self.assertEqual(phi(x, y)+1, gap_formula(x, y))
                self.assertGreaterEqual(phi(x, y), -1)

    def test_all_six_minima_and_actual_zero_response(self):
        orientations = set(permutations(map(F, (1, -1, 0))))
        self.assertEqual(len(orientations), 6)
        for x in orientations:
            y = optimal_y(x)
            q = tuple(a-b for a, b in zip(x, y))
            self.assertEqual(phi(x, y), -1)
            self.assertEqual(sorted(q), [F(-3, 4), F(0), F(3, 4)])
            self.assertEqual(sum(q), 0)
            self.assertEqual(norm2(q), F(9, 8))

    def test_other_old_minimum_gets_lifted(self):
        x = (F(5, 7), F(3, 7), F(-8, 7))
        y = optimal_y(x)
        self.assertEqual(sum(x), 0)
        self.assertEqual(norm2(x), 2)
        self.assertEqual(functional(x, y, MU, LAM), -1)
        self.assertEqual(prod3(x), F(-120, 343))
        self.assertEqual(phi(x, y), -1+F(14400, 117649))
        self.assertGreater(phi(x, y), -1)
        self.assertNotIn(x, set(permutations(map(F, (1, -1, 0)))))

    def test_joint_shift_and_permutation_invariant(self):
        x, y = (F(1), F(0), F(-2)), (F(3), F(-1), F(2))
        expected = phi(x, y)
        self.assertEqual(phi(tuple(v+5 for v in x), tuple(v+5 for v in y)), expected)
        self.assertEqual(phi(tuple(-v for v in x), tuple(-v for v in y)), expected)
        for order in permutations(range(3)):
            self.assertEqual(phi(tuple(x[i] for i in order), tuple(y[i] for i in order)), expected)

    def test_fixed_first_role_leaves_three_orbits(self):
        orientations = set(permutations(map(F, (1, -1, 0))))
        orbits = set()
        for x in orientations:
            swap = (x[0], x[2], x[1])
            orbits.add(frozenset((x, swap)))
        self.assertEqual(len(orbits), 3)
        self.assertEqual({next(iter(orbit))[0] for orbit in orbits}, {-1, 0, 1})

    def test_grid_minima_only_six_centered_orientations(self):
        seen = set()
        for x in product(map(F, range(-2, 3)), repeat=3):
            y = optimal_y(x)
            if phi(x, y) == -1:
                seen.add(centered(x))
        self.assertEqual(seen, set(permutations(map(F, (1, -1, 0)))))


if __name__ == '__main__':
    unittest.main()
