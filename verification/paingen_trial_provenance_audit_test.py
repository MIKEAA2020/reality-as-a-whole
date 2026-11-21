import csv
import io
import unittest

from paingen_trial_provenance_audit import compare_rating, mean_comparison, parse_run, percentile, posthoc_strata, rating


class TrialProvenanceTests(unittest.TestCase):
    def make_run(self):
        output = io.StringIO()
        fields = ['onset', 'duration', 'trial_type', 'int_rating', 'unp_rating', 'level']
        writer = csv.DictWriter(output, fieldnames=fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        for j in range(8):
            for offset, t in enumerate(['warning_cue', 'heat', 'int_rating', 'unp_rating']):
                writer.writerow(dict(onset=str(4*j+offset), duration='1', trial_type=t,
                                     int_rating='n/a', unp_rating='n/a', level='n/a'))
        return output.getvalue().encode()

    def test_valid_run_grammar(self):
        episodes, failure = parse_run(self.make_run())
        self.assertIsNone(failure)
        self.assertEqual(len(episodes), 8)

    def test_duplicate_onset_is_not_ordered_by_file_position(self):
        raw = self.make_run().decode().replace('\n1\t1\theat', '\n0\t1\theat', 1).encode()
        self.assertEqual(parse_run(raw)[1], 'tied_onsets')

    def test_sort_by_onset_not_file_order(self):
        rows = self.make_run().decode().splitlines()
        rows[3], rows[4] = rows[4], rows[3]
        episodes, failure = parse_run(('\n'.join(rows) + '\n').encode())
        self.assertIsNone(failure)
        self.assertEqual(episodes[0][2]['trial_type'], 'int_rating')
        self.assertEqual(episodes[0][3]['trial_type'], 'unp_rating')

    def test_reject_wrong_sequence(self):
        raw = self.make_run().decode().replace('warning_cue', 'unknown', 1).encode()
        self.assertEqual(parse_run(raw)[1], 'episode_grammar')

    def test_missing_invalid_and_equal_cases(self):
        self.assertEqual(rating('n/a'), ('missing', None))
        self.assertEqual(rating('nan'), ('invalid', None))
        self.assertEqual(rating('-0.1'), ('invalid', None))
        self.assertEqual(compare_rating('n/a', 'n/a'), 'both_missing')
        self.assertEqual(compare_rating('0.3', 'n/a'), 'one_missing')
        self.assertEqual(compare_rating('0.3', '0.30000000001'), 'both_equal')
        self.assertEqual(compare_rating('0.3', '0.4'), 'both_unequal')

    def test_condition_join_counts_missing_and_different(self):
        rec = {('a', 1): {'Yint': [.1, .3], 'Yunp': []},
               ('b', 1): {'Yint': [.6], 'Yunp': [.5]}}
        source = {('a', 1): {'Yint': '0.2', 'Yunp': 'NA'},
                  ('b', 1): {'Yint': '0.8', 'Yunp': 'NA'},
                  ('c', 1): {'Yint': 'NA', 'Yunp': 'NA'}}
        result = mean_comparison(rec, source)
        self.assertEqual(result['overlap_keys'], 2)
        self.assertEqual(result['export_only_keys'], 1)
        self.assertEqual(result['outcomes']['Yint_both_equal'], 1)
        self.assertEqual(result['outcomes']['Yint_both_unequal'], 1)
        self.assertEqual(result['outcomes']['Yunp_both_missing'], 1)
        self.assertEqual(result['outcomes']['Yunp_export_missing_only'], 1)
        self.assertAlmostEqual(result['maximum_finite_absolute_difference'], .2)

    def test_posthoc_classifies_disagreement_and_run_completeness(self):
        key = ('person', 1, 3, 0)
        rec = {key: {'Yint': [.1], 'Yunp': [.2]}}
        src = {key: {'Yint': '.1', 'Yunp': '.5'}}
        result = posthoc_strata(rec, src, {'person': {'01', '02', '03', '04'}})
        self.assertEqual(result['overall']['unpleasantness_only_unequal'], 1)
        self.assertEqual(result['strata']['run_completion:four_accepted_runs']['unpleasantness_only_unequal'], 1)

    def test_percentile_interpolation(self):
        self.assertEqual(percentile([2, 0, 1], .25), .5)


if __name__ == '__main__':
    unittest.main()
