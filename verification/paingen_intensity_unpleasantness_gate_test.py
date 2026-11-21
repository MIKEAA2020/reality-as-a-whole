import unittest
import numpy as np

from paingen_intensity_unpleasantness_gate import (
    bootstrap_ratio, bootstrap_rmse_delta, make_pairs, pair_summary, score,
)


class PainComparisonTests(unittest.TestCase):
    def test_scores_distinguish_row_and_family_weighting(self):
        result = score([0, 0, 0], [1, 1, 0], ['a', 'a', 'b'])
        self.assertAlmostEqual(result['row_rmse'], (2 / 3) ** .5)
        self.assertAlmostEqual(result['family_rmse'], .5 ** .5)
        self.assertAlmostEqual(result['row_mae'], 2 / 3)
        self.assertAlmostEqual(result['family_mae'], .5)

    def test_cluster_bootstrap_constant_value(self):
        self.assertEqual(bootstrap_ratio([3., 3., 3.], ['a', 'a', 'b'], 50, 7), [3., 3.])
        self.assertEqual(bootstrap_rmse_delta([1, 2, 3], [0, 1, 2], [0, 1, 2],
                                              ['a', 'a', 'b'], 50, 7), [0., 0.])

    def test_matched_pair_sign_and_contrast_scoring(self):
        rows = [dict(person='x', family='f', fold=0, condition=(.5, 0., -.5), y=.8, intensity=.5),
                dict(person='x', family='f', fold=0, condition=(.5, 0., .5), y=.3, intensity=.2),
                dict(person='y', family='g', fold=1, condition=(-.5, 0., -.5), y=.2, intensity=.1)]
        pairs, cells = make_pairs(rows)
        self.assertEqual((len(pairs), cells), (1, 2))
        result = pair_summary(rows, {'m': np.array([.7, .2, .1])}, pairs)
        self.assertAlmostEqual(result['mean_dU'], .5)
        self.assertAlmostEqual(result['mean_dI'], .3)
        self.assertAlmostEqual(result['mean_dU_minus_dI'], .2)
        self.assertAlmostEqual(result['contrast_oof_scores']['m']['row_rmse'], 0.)
        self.assertIsNone(result['correlation_dU_dI'])
        self.assertNotIn('predictions_below_zero', result['contrast_oof_scores']['m'])

    def test_matching_rejects_different_fold(self):
        rows = [dict(person='x', family='f', fold=0, condition=(.5, 0., -.5)),
                dict(person='x', family='f', fold=1, condition=(.5, 0., .5))]
        with self.assertRaisesRegex(ValueError, 'family/fold'):
            make_pairs(rows)

    def test_empty_bootstrap_is_error(self):
        with self.assertRaises(ValueError):
            bootstrap_ratio([], [])


if __name__ == '__main__':
    unittest.main()
