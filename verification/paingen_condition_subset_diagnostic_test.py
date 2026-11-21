import unittest

from paingen_condition_subset_diagnostic import MAX_TRIALS, bucket, classify
import collections


class SubsetDiagnosticTests(unittest.TestCase):
    def test_unique_proper_complete_run(self):
        trials = [(0., 0., '01'), (.2, .4, '01'), (.8, .6, '04')]
        result = classify(trials, (.1, .2))
        self.assertEqual(result['category'], 'proper_subset_only')
        self.assertEqual(result['matching_subsets'], 1)
        self.assertTrue(result['whole_single_run_witness'])
        self.assertTrue(result['unique_witness_whole_single_run'])
        self.assertEqual(result['unique_excluded_count'], 1)

    def test_dimension_witnesses_need_not_be_same_subset(self):
        trials = [(0., 0., '01'), (.8, .6, '04')]
        result = classify(trials, (0., .6))
        self.assertEqual(result['category'], 'no_common_subset')
        self.assertTrue(result['intensity_only_exists'])
        self.assertTrue(result['unpleasantness_only_exists'])
        c = collections.Counter()
        bucket(c, result)
        self.assertEqual(c['no_common_both_individually_exist'], 1)

    def test_full_match_does_not_mean_unique(self):
        result = classify([(.2, .4, '01'), (.2, .4, '04')], (.2, .4))
        self.assertEqual(result['category'], 'full_set_matches')
        self.assertEqual(result['matching_subsets'], 3)

    def test_proper_subset_can_have_multiple_witnesses(self):
        result = classify([(.2, .4, '01'), (.2, .4, '04'), (.8, .7, '04')], (.2, .4))
        self.assertEqual(result['category'], 'proper_subset_only')
        self.assertEqual(result['matching_subsets'], 3)
        self.assertIsNone(result['unique_excluded_count'])

    def test_max_trials_is_a_stop(self):
        with self.assertRaises(ValueError):
            classify([(0., 0., '01')] * (MAX_TRIALS + 1), (0., 0.))
        with self.assertRaises(ValueError):
            classify([], (0., 0.))


if __name__ == '__main__':
    unittest.main()
