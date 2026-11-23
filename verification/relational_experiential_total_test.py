#!/usr/bin/env python3
"""Clock and signed-measure arithmetic controls, not experience measurements."""
from fractions import Fraction as F
from math import fsum, log
import unittest


A = ((F(0), F(1), F(2)), (F(1), F(2), F(-1)))
B = ((F(0), F(1), F(-1)),)


def integral(pieces, start, end):
    if end < start:
        raise ValueError('interval must be oriented forward')
    return sum(max(F(0), min(end, hi)-max(start, lo))*value
               for lo, hi, value in pieces)


def harmonic(n):
    return sum((F(1, k) for k in range(1, n+1)), F(0))


class RelationalExperientialTotalTests(unittest.TestCase):
    def test_actual_history_zero_and_nonzero_local_parts(self):
        qa = integral(A, F(0), F(2))
        qb = integral(B, F(0), F(1))
        self.assertEqual((qa, qb, qa+qb), (1, -1, 0))
        self.assertEqual(integral(A, F(0), F(1)), 2)
        self.assertEqual(integral(A, F(1), F(2)), -1)

    def test_overlapping_window_inclusion_exclusion(self):
        w1 = integral(A, F(0), F(3, 2))
        w2 = integral(A, F(1, 2), F(2))
        overlap = integral(A, F(1, 2), F(3, 2))
        self.assertEqual((w1, w2, overlap), (F(3, 2), 0, F(1, 2)))
        self.assertEqual(w1+w2-overlap, integral(A, F(0), F(2)))
        self.assertNotEqual(w1+w2, integral(A, F(0), F(2)))

    def test_reparameterization_requires_jacobian(self):
        # tau=2*lambda; values are scalars, d tau=2 d lambda.
        lambda_pieces = ((F(0), F(1, 2), F(2)), (F(1, 2), F(1), F(-1)))
        uncorrected = integral(lambda_pieces, F(0), F(1))
        corrected = 2*uncorrected
        self.assertEqual(uncorrected, F(1, 2))
        self.assertEqual(corrected, integral(A, F(0), F(2)))

    def test_common_units_versus_independent_weight(self):
        qa, qb = integral(A, F(0), F(2)), integral(B, F(0), F(1))
        for common in (F(1, 2), F(1), F(3)):
            self.assertEqual(common*qa+common*qb, 0)
        self.assertEqual(qa+2*qb, -1)

    def test_unequal_time_slices_do_not_imply_nonzero_history(self):
        early = integral(A, F(0), F(1))
        late = integral(A, F(1), F(2)) + integral(B, F(0), F(1))
        self.assertEqual((early, late), (2, -2))
        self.assertEqual(early+late, 0)
        # These are chosen groupings, not asserted simultaneous cosmic slices.

    def test_two_positive_then_one_negative_exact_identity(self):
        for n in range(1, 15):
            reordered = (sum((F(1, 2*k-1) for k in range(1, 2*n+1)), F(0))
                         - sum((F(1, 2*k) for k in range(1, n+1)), F(0)))
            self.assertEqual(reordered, harmonic(4*n)-harmonic(2*n)/2-harmonic(n)/2)

    def test_conditional_series_order_has_different_limits(self):
        n = 40000
        ordinary = fsum((1 if k % 2 else -1)/k for k in range(1, 4*n+1))
        reordered = fsum([1/(2*k-1) for k in range(1, 2*n+1)] +
                         [-1/(2*k) for k in range(1, n+1)])
        self.assertAlmostEqual(ordinary, log(2), delta=1e-4)
        self.assertAlmostEqual(reordered, 1.5*log(2), delta=1e-4)
        self.assertGreater(reordered-ordinary, 0.3)

    def test_pair_grouping_does_not_supply_ordinary_convergence(self):
        partials = [sum(1 if i % 2 == 0 else -1 for i in range(n)) for n in range(1, 11)]
        self.assertEqual(partials[::2], [1]*5)
        self.assertEqual(partials[1::2], [0]*5)


if __name__ == '__main__':
    unittest.main()
