import unittest

import numpy as np
from witzel_2025_exp1a_aggregate_recheck import signed_angular_difference, condition_stats, LABELS


class RecheckTests(unittest.TestCase):
    def test_wrapping_and_tie(self):
        np.testing.assert_allclose(signed_angular_difference([359, 1, 180, -180], 0), [-1, 1, 180, 180])

    def test_valid_synthetic_design(self):
        comp = np.zeros((8, 9, 3))
        comp[:, :, 1] = np.arange(-40, 41, 10)
        indi = np.tile(np.arange(31) % 3, (8, 1)).T
        results = condition_stats(LABELS, comp, indi)
        self.assertEqual(len(results), 8)
        self.assertTrue(all(row['n'] == 31 for row in results))

    def test_bad_grid_rejected(self):
        comp = np.zeros((8, 9, 3))
        with self.assertRaises(ValueError):
            condition_stats(LABELS, comp, np.ones((31, 8)))

    def test_out_of_range_response_rejected(self):
        comp = np.zeros((8, 9, 3))
        comp[:, :, 1] = np.arange(-40, 41, 10)
        indi = np.ones((31, 8)); indi[0, 0] = 50
        with self.assertRaises(ValueError):
            condition_stats(LABELS, comp, indi)


if __name__ == '__main__':
    unittest.main()
