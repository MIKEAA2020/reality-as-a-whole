import unittest
from paingen_remaining_mismatch_runs import dimension, run_category


class RunCompletenessTests(unittest.TestCase):
    def test_categories_ignore_order(self):
        self.assertEqual(run_category(['accepted', 'accepted']), 'two_accepted')
        self.assertEqual(run_category(['rejected', 'accepted']), 'one_accepted_one_rejected')
        self.assertEqual(run_category(['accepted', 'absent']), 'one_accepted_one_absent')

    def test_impossible_or_bad_status_fails(self):
        for statuses in ([], ['absent', 'rejected'], ['accepted'], ['accepted', 'unknown']):
            with self.subTest(statuses=statuses), self.assertRaises(ValueError):
                run_category(statuses)

    def test_mismatch_dimensions(self):
        self.assertEqual(dimension((True, True)), 'both_match')
        self.assertEqual(dimension((False, False)), 'both_mismatch')
        self.assertEqual(dimension((False, True)), 'intensity_only_mismatch')
        self.assertEqual(dimension((True, False)), 'unpleasantness_only_mismatch')
        with self.assertRaises(ValueError):
            dimension((None, True))


if __name__ == '__main__':
    unittest.main()
