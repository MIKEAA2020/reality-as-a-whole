#!/usr/bin/env python3
"""Finite structural controls, not a theory or measurement of experience."""
from fractions import Fraction as F
from itertools import product
import unittest


P = (F(4, 7), F(2, 7), F(1, 7))


def moments(p, values):
    mean = sum(w*x for w, x in zip(p, values))
    variance = sum(w*(x-mean)**2 for w, x in zip(p, values))
    return mean, variance


def score(p, values):
    mean, variance = moments(p, values)
    return tuple(mean-x for x in values), variance


def tv(r, p):
    return sum(abs(a-b) for a, b in zip(r, p))/2


class ActualIncidenceTests(unittest.TestCase):
    def test_organization_distinguishes_same_bare_energy(self):
        bare = (F(2),)*3
        organization = (F(-1), F(0), F(1))
        effective = tuple(e+l for e, l in zip(bare, organization))
        s, variance = score(P, effective)
        self.assertEqual(effective, (1, 2, 3))
        self.assertEqual(s, (F(4, 7), F(-3, 7), F(-10, 7)))
        self.assertEqual(variance, F(26, 49))
        self.assertEqual(sum(w*x for w, x in zip(P, s)), 0)

    def test_same_energy_context_reverses_score(self):
        a, va = score(P, (F(1), F(2), F(3)))
        b, vb = score(P, (F(2), F(3), F(4)))
        self.assertEqual(va, vb)
        self.assertEqual(a[1], F(-3, 7))
        self.assertEqual(b[0], F(4, 7))
        self.assertLess(a[1], 0)
        self.assertGreater(b[0], 0)

    def test_actual_counts_not_identical_to_ensemble(self):
        s, var = score(P, (F(1), F(2), F(3)))
        self.assertEqual(sum(n*x for n, x in zip((4, 2, 1), s)), 0)
        self.assertEqual(sum(n*x for n, x in zip((3, 3, 1), s)), -1)
        # Dividing the latter by sigma=sqrt(26)/7 gives -7/sqrt(26).
        self.assertEqual(var, F(26, 49))

    def test_different_actual_distribution_can_still_balance(self):
        s, _ = score(P, (F(1), F(2), F(3)))
        r = (F(3, 7), F(4, 7), F(0))
        self.assertNotEqual(r, P)
        self.assertEqual(sum(r), 1)
        self.assertEqual(sum(w*x for w, x in zip(r, s)), 0)

    def test_total_variation_bound_for_all_seven_occurrence_counts(self):
        s, _ = score(P, (F(1), F(2), F(3)))
        count = 0
        for a in range(8):
            for b in range(8-a):
                c = 7-a-b
                r = tuple(F(n, 7) for n in (a, b, c))
                discrepancy = abs(sum(w*x for w, x in zip(r, s)))
                bound = 2*max(abs(x) for x in s)*tv(r, P)
                self.assertLessEqual(discrepancy, bound)
                count += 1
        self.assertEqual(count, 36)

    def test_independent_draw_sum_expectation_and_variance(self):
        s, var = score(P, (F(1), F(2), F(3)))
        n = 3
        mean = F(0)
        second = F(0)
        for outcomes in product(range(3), repeat=n):
            probability = F(1)
            total = F(0)
            for i in outcomes:
                probability *= P[i]
                total += s[i]
            mean += probability*total
            second += probability*total*total
        self.assertEqual(mean, 0)
        self.assertEqual(second / var, n)  # variance after score normalization
        self.assertEqual(second / (var*n*n), F(1, n))


if __name__ == '__main__':
    unittest.main()
