import collections
import unittest
from fractions import Fraction
from paingen_order_rt_selection import ORDERS, analyze, person_summary, synthetic_selection, timing_category
from paingen_response_time_reconstruction import rt_status


class OrderSelectionTests(unittest.TestCase):
    def test_synthetic_control(self):
        x = synthetic_selection()
        self.assertEqual(sum(Fraction(v) for v in x['joint'].values()), 1)
        self.assertEqual(x['retention_given_order'], {'0':'1/2', '1':'1/2'})
        self.assertEqual(x['outcome_mean_given_order_and_retained'], {'0':'1/4', '1':'3/4'})
        self.assertEqual(x['full_outcome_mean_given_order'], {'0':'1/2', '1':'1/2'})
        self.assertEqual(x['population_effect'], '0')
        self.assertEqual(x['retained_contrast_order1_minus_order0'], '1/2')

    def test_rt_boundaries_and_missingness(self):
        self.assertEqual([rt_status(x) for x in (0.019, .02, 5.01, 5.011, None)],
                         ['below', 'in_range', 'in_range', 'above', 'unavailable'])

    def test_timing_categories(self):
        self.assertEqual(timing_category(1.0005, 1.0)[0], 'within_0.001')
        self.assertEqual(timing_category(1.2, 1.0)[0], 'duration_greater')
        self.assertEqual(timing_category(1.0, 1.2)[0], 'response_time_greater')
        for d,r in ((None,1), (0,1), (1,-1), (1, 'NaN')):
            self.assertEqual(timing_category(d,r), ('unusable',None))

    def test_person_unweighted_and_available_counts(self):
        def row(i0,n0,i1,n1,missing=0):
            return {ORDERS[0]:collections.Counter(in_range=i0, above=n0-i0),
                    ORDERS[1]:collections.Counter(in_range=i1, above=n1-i1-missing, unavailable=missing)}
        people = {'p1':row(1,2,1,4), 'p2':row(1,2,1,1), 'p3':row(0,1,0,1,1),
                  'one_order': {ORDERS[0]:collections.Counter(in_range=1), ORDERS[1]:collections.Counter()}}
        x = person_summary(people)
        self.assertEqual((x['eligible_people'],x['intensity_first_higher'],x['unpleasantness_first_higher'],x['equal']),(3,1,1,1))
        self.assertEqual(x['with_any_unavailable_rt'],1)
        self.assertEqual(x['mean_person_rate_difference_exact'], '-1/12')

    def test_unexpected_or_incomplete_input_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({})
        with self.assertRaises(ValueError):
            analyze({'not-an-event-path': b''})


if __name__ == '__main__':
    unittest.main()
