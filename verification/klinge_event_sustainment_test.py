import unittest
from klinge_event_sustainment import (event_activity, finite_horizon_counts, lifetime_covered,
                                      nonoverlapping, present_supported, window_counts)


class EventSustainmentTests(unittest.TestCase):
    def test_birth_can_outlast_present_base(self):
        b = [1, 0, 0]
        self.assertEqual(event_activity(b, 2), [1, 1, 0])
        self.assertFalse(present_supported(b, b, 2))
        self.assertFalse(lifetime_covered(b, b, 2))

    def test_one_slot_events_are_supported(self):
        b = [0, 1, 0, 1]
        self.assertTrue(lifetime_covered(b, b, 1))
        self.assertTrue(present_supported(b, b, 1))
        self.assertEqual(window_counts(1)['active_without_current_base'], 0)

    def test_overlapping_events_are_not_one_token(self):
        self.assertEqual(event_activity([1, 0, 1, 0, 0, 0], 3), [1, 1, 2, 1, 1, 0])

    def test_sequential_counterexample_and_exhaustive_restriction(self):
        base, starts = [1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 0, 0]
        self.assertTrue(nonoverlapping(starts, 3))
        self.assertEqual(event_activity(starts, 3), [1, 1, 1, 1, 1, 1])
        self.assertFalse(present_supported(base, starts, 3))
        self.assertFalse(nonoverlapping([1, 0, 1], 3))
        for d in range(1, 5):
            counts = finite_horizon_counts(d, require_nonoverlap=True)
            self.assertEqual(counts['supported_at_all_observed_slots'], counts['all_event_lifetimes_covered_within_horizon'])

    def test_finite_boundary_does_not_prove_future(self):
        self.assertTrue(lifetime_covered([1], [1], 4))
        self.assertGreater(finite_horizon_counts(4)['supported_but_some_events_extend_beyond_horizon'], 0)

    def test_history_condition_rejects_birth_without_base(self):
        with self.assertRaises(ValueError): lifetime_covered([0], [1], 2)
        with self.assertRaises(ValueError): lifetime_covered([1], [], 2)
        with self.assertRaises(ValueError): event_activity([1], 0)
        with self.assertRaises(ValueError): event_activity([True], 1)

    def test_formula_and_all_joint_histories(self):
        for d in range(1, 9):
            self.assertEqual(window_counts(d)['active_without_current_base'], 2**(d-1)-1)
            self.assertEqual(window_counts(d)['same_base_different_activity_unordered_pairs'], 2**(d-1)-1)
        for d in range(1, 5):
            counts = finite_horizon_counts(d)
            self.assertEqual(counts['allowed_histories'], 729)
            self.assertEqual(counts['supported_at_all_observed_slots'], counts['all_event_lifetimes_covered_within_horizon'])


if __name__ == '__main__':
    unittest.main()
