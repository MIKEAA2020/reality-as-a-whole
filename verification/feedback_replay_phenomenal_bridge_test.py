#!/usr/bin/env python3
"""Check closed-form transition identities for the feedback/replay example."""
from itertools import product
import unittest
from feedback_replay_phenomenal_bridge import NOMINAL, trace, outputs, incidence


class FeedbackReplayTest(unittest.TestCase):
    def test_closed_form_outputs(self):
        for a, b, c, d in product((0, 1), repeat=4):
            expected_f = (a, b ^ a, c ^ b, d ^ c)
            expected_r = (a, b, c ^ 1, d ^ 1)
            self.assertEqual(outputs(trace((a, b, c, d), 'feedback')), expected_f)
            self.assertEqual(outputs(trace((a, b, c, d), 'replay')), expected_r)
            self.assertEqual(expected_f == expected_r, (a, b, c) == NOMINAL[:3])

    def test_nominal_state_and_output_match(self):
        self.assertEqual(trace(NOMINAL, 'feedback'), trace(NOMINAL, 'replay'))

    def test_alternative_recovers_only_feedback(self):
        history = (0, 1, 0, 0)
        self.assertEqual(outputs(trace(history, 'feedback')), (0, 1, 1, 0))
        self.assertEqual(outputs(trace(history, 'replay')), (0, 1, 1, 1))

    def test_internal_intervention_distinguishes_observationally_equivalent_updates(self):
        for h in product((0, 1), repeat=4):
            self.assertEqual(trace(h, 'feedback'), trace(h, 'direct_copy'))
        f = trace(NOMINAL, 'feedback', {1: 0})
        d = trace(NOMINAL, 'direct_copy', {1: 0})
        self.assertEqual(outputs(f), (0, 0, 1, 0))
        self.assertEqual(outputs(d), (0, 0, 0, 0))

    def test_incidence_rules_agree_on_anchor_and_diverge_elsewhere(self):
        self.assertTrue(incidence(True, True, 'functional'))
        self.assertTrue(incidence(True, True, 'biology_required'))
        self.assertTrue(incidence(True, False, 'functional'))
        self.assertFalse(incidence(True, False, 'biology_required'))
        self.assertFalse(incidence(False, False, 'functional'))
        self.assertFalse(incidence(False, False, 'biology_required'))

    def test_reject_bad_inputs(self):
        for bad in ((0, 1), (0, 1, 3, 0)):
            with self.assertRaises(ValueError):
                trace(bad, 'feedback')
        with self.assertRaises(ValueError):
            trace(NOMINAL, 'invented')


if __name__ == '__main__':
    unittest.main()
