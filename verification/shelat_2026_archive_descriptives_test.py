#!/usr/bin/env python3
"""Check archive-summary invariants and Table 1 agreement; not a model test."""
import json
import unittest
from pathlib import Path

from shelat_2026_archive_descriptives import label

ROOT = Path(__file__).resolve().parent
PUBLISHED = {
    1: {'fast_neutral': (18.04, 3.78), 'fast_novel': (18.34, 5.30),
        'fast_reward': (18.18, 5.72), 'fast_selection': (18.58, 5.51),
        'slow_neutral': (16.02, 4.54), 'slow_novel': (15.56, 4.94),
        'slow_reward': (15.16, 4.86), 'slow_selection': (15.74, 5.48)},
    2: {'fast_neutral': (19.08, 5.81), 'fast_novel': (17.28, 4.79),
        'fast_reward': (18.02, 5.76), 'fast_selection': (17.46, 5.18),
        'slow_neutral': (14.42, 4.78), 'slow_novel': (14.36, 4.78),
        'slow_reward': (13.68, 4.25), 'slow_selection': (14.64, 5.10)},
}


class Checks(unittest.TestCase):
    def test_color_labels_and_invalid_mappings(self):
        self.assertEqual(label('red', 'r', 'g'), 'reward')
        self.assertEqual(label('green', 'r', 'g'), 'selection')
        self.assertEqual(label('blue', 'r', 'g'), 'novel')
        self.assertEqual(label('neutral', 'r', 'g'), 'neutral')
        with self.assertRaises(ValueError):
            label('red', 'r', 'r')
        with self.assertRaises(ValueError):
            label('purple', 'r', 'g')

    def test_saved_aggregate_matches_published_table_one(self):
        report = json.loads((ROOT / 'shelat_2026_archive_descriptives.json').read_text())
        for experiment in report['experiments']:
            number = experiment['experiment']
            self.assertEqual(experiment['sart_subject_folders'], 50)
            self.assertEqual(experiment['raw_fast_slow_trials'],
                             sum(x['raw_n'] for x in experiment['trigger_condition_counts'].values()))
            n = sum(x['retained_n'] for x in experiment['trigger_condition_counts'].values())
            self.assertEqual(n + experiment['excluded_no_response_or_missing_rt'] +
                             experiment['excluded_lt200_after_no_response'],
                             experiment['raw_fast_slow_trials'])
            for key, (mean, sd) in PUBLISHED[number].items():
                with self.subTest(experiment=number, cell=key):
                    row = experiment['trigger_condition_counts'][key]
                    self.assertAlmostEqual(row['participant_count_mean'], mean, delta=.0051)
                    self.assertAlmostEqual(row['participant_count_sample_sd'], sd, delta=.0051)


if __name__ == '__main__':
    unittest.main()
