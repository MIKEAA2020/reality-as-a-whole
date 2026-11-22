#!/usr/bin/env python3
"""Synthetic-only tests for the fixed three-state analysis."""
import unittest
import numpy as np
from roy_s09_three_state_pilot import label_window, train, predictions, assess
from roy_s09_eeg_report_transfer import feature


def row(label, value, slot=0, bad=False):
    return {'label':label, 'feature':value, 'slot':slot, 'bad':bad}


class ThreeStateTest(unittest.TestCase):
    def test_majority_threshold_and_unknown(self):
        self.assertEqual(label_window([1]*3 + [3]), 1)
        self.assertEqual(label_window([3]*3 + [0]), 3)
        self.assertEqual(label_window([3]*2 + [1, 0]), 0)
        self.assertEqual(label_window([0]*4), 0)
        with self.assertRaises(ValueError): label_window([4])

    def test_frequency_feature_orders_tags(self):
        t = np.arange(500)/250
        self.assertGreater(feature(np.sin(2*np.pi*(20/3)*t), 250, 20/3, 60/7), 0)
        self.assertLess(feature(np.sin(2*np.pi*(60/7)*t), 250, 20/3, 60/7), 0)

    def test_training_and_ties(self):
        model = train([row(1, 0.0, 0), row(2, 1.0, 0), row(3, 2.0, 1)])
        self.assertEqual(model['majority'], 1)
        self.assertEqual(model['slot_rules'][:3], [1, 3, 1])
        self.assertEqual(predictions(row(0, 0.5), model)['eeg'], 1)
        with self.assertRaises(ValueError): train([row(1,0.0), row(2,1.0)])

    def test_scoring_abstention_and_no_label_leakage(self):
        model = train([row(1,0.0), row(2,1.0), row(3,2.0)])
        self.assertEqual(predictions(row(0, 1.8), model), predictions(row(1, 1.8), model))
        self.assertIsNone(predictions(row(3, None, bad=True), model))
        rows = [row(1,0.1), row(2,0.9), row(3,1.8), row(0,1.9),
                row(3,None,bad=True), row(0,None,bad=True)]
        result = assess(rows, model)
        self.assertEqual((result['total_windows'], result['report_unresolved_windows'],
                          result['artifact_windows'], result['unresolved_artifact_overlap'],
                          result['labeled_clean_windows']), (6,2,2,1,3))
        eeg = result['models']['eeg']
        self.assertEqual(eeg['confusion_true_rows_pred_columns'], [[1,0,0],[0,1,0],[0,0,1]])
        self.assertEqual(eeg['labeled_clean_accuracy'], 1)
        self.assertEqual(eeg['macro_recall'], 1)
        self.assertEqual(eeg['full_grid_correct_fraction'], 0.5)
        self.assertEqual(eeg['clean_unresolved_predictions'], [0,0,1])

    def test_fitting_does_not_change_on_scoring_test_labels(self):
        model = train([row(1,0.0),row(2,1.0),row(3,2.0)])
        before = repr(model)
        assess([row(1,1.0),row(3,0.0)], model)
        self.assertEqual(before, repr(model))


if __name__ == '__main__':
    unittest.main()
