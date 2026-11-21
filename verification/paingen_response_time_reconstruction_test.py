import collections
import unittest
from paingen_response_time_reconstruction import compare_cell, count_cell, missing_cell, rt_status


class ResponseTimeTests(unittest.TestCase):
    def test_strict_exclusion_boundaries(self):
        self.assertEqual(rt_status(.01999), 'below')
        self.assertEqual(rt_status(.02), 'in_range')
        self.assertEqual(rt_status(5.01), 'in_range')
        self.assertEqual(rt_status(5.01001), 'above')
        self.assertEqual(rt_status(None), 'unavailable')
        self.assertEqual(rt_status('nan'), 'unavailable')

    def test_screening_applies_both_ratings(self):
        trials = [(.2, .4, '01', 2.), (.8, .6, '04', 5.1)]
        r = compare_cell(trials, (.2, .4))
        self.assertEqual(r['old'], (False, False))
        self.assertEqual(r['new'], (True, True))
        self.assertEqual((r['retained'], r['removed']), (1, 1))
        c = collections.Counter(); count_cell(c, r)
        self.assertEqual(c['pair_mismatch_to_match'], 1)

    def test_unavailable_stops_reconstruction(self):
        r = compare_cell([(.1, .2, '01', None), (.3, .4, '04', 2.)], (.2, .3))
        self.assertEqual(r['reason'], 'unavailable_rt')
        self.assertIsNone(r['new'])
        c = collections.Counter(); count_cell(c, r)
        self.assertEqual(c['unresolved_unavailable_rt'], 1)

    def test_no_retained_is_unresolved(self):
        r = compare_cell([(.1, .2, '01', 5.5)], (.1, .2))
        self.assertEqual(r['reason'], 'no_retained_trials')
        self.assertIsNone(r['new'])

    def test_missing_cell_does_not_impute(self):
        c = collections.Counter()
        missing_cell(c, [(.1, .2, '01', 8.), (.3, .4, '04', .01)], (None, None))
        self.assertEqual(c['both_ratings_missing'], 1)
        self.assertEqual(c['all_recorded_rt_outside_range'], 1)
        self.assertEqual(c['recorded_trial_pairs'], 2)
        missing_cell(c, [(.1, .2, '01', None)], (None, .4))
        self.assertEqual(c['one_rating_missing'], 1)
        self.assertEqual(c['any_unavailable_rt'], 1)

    def test_worsening_and_no_drop(self):
        r = compare_cell([(.2, .4, '01', 2.), (.8, .6, '04', 6.)], (.5, .5))
        c = collections.Counter(); count_cell(c, r)
        self.assertEqual(c['pair_match_to_mismatch'], 1)
        r2 = compare_cell([(.2, .4, '01', 2.)], (.2, .4))
        self.assertEqual(r2['removed'], 0)
        self.assertEqual(r2['new'], (True, True))


if __name__ == '__main__':
    unittest.main()
