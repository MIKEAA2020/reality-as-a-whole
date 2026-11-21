#!/usr/bin/env python3
"""Synthetic paired estimators and optional aggregate archive recomputation."""
import json
import os
import unittest
from pathlib import Path

from shelat_2026_color_exposure_followup import collect, exact_mcnemar, summarize

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / 'verification/shelat_2026_color_exposure_followup.json'


def subject(first, tenth):
    result = [{'block': 1, 'trial': i+1, 'trigger': 'fast', 'category': 'reward', 'accuracy': 1, 'rt': 500}
              for i in range(10)]
    result[0]['accuracy'] = first
    result[9]['accuracy'] = tenth
    return result


class EarlyExposureChecks(unittest.TestCase):
    def test_synthetic_pair_table_and_missing(self):
        data = {1: subject(0, 1), 2: subject(1, 0), 3: subject(1, 1),
                4: subject(None, 0), 5: subject(0, None), 6: []}
        result = summarize(data)
        self.assertEqual(result['participants'], 6)
        self.assertEqual(result['occurrences']['1']['outcomes'], {'correct': 2, 'incorrect': 2, 'missing': 1})
        self.assertEqual(result['occurrences']['10']['outcomes'], {'correct': 2, 'incorrect': 2, 'missing': 1})
        self.assertEqual(result['paired_usable_n'], 3)
        self.assertEqual(result['paired_table_first_then_tenth'], {'incorrect_incorrect': 0, 'incorrect_correct': 1, 'correct_incorrect': 1, 'correct_correct': 1})
        self.assertEqual(result['accuracy_change_tenth_minus_first'], 0)
        self.assertAlmostEqual(result['exact_two_sided_mcnemar_p_unadjusted'], 1)
        self.assertAlmostEqual(exact_mcnemar(0, 4), .125)
        self.assertAlmostEqual(exact_mcnemar(3, 13), .021270751953125)

    def test_saved_key_aggregates(self):
        data = json.loads(OUTPUT.read_text())
        pooled = data['results']['pooled']
        self.assertEqual(pooled['occurrences']['1']['trigger'], {'fixed': 100})
        self.assertEqual(pooled['occurrences']['10']['trigger'], {'fast': 67, 'slow': 33})
        self.assertEqual(pooled['paired_usable_n'], 87)
        self.assertAlmostEqual(pooled['accuracy_change_tenth_minus_first'], -15/87)
        within = data['post_result_within_trigger']
        self.assertEqual(within['fast']['pooled']['paired_usable_n'], 94)
        self.assertEqual(within['slow']['pooled']['paired_usable_n'], 77)
        self.assertEqual(within['fixed']['pooled']['occurrences']['10']['available_occurrences'], 98)

    @unittest.skipUnless(os.getenv('SHELAT_ARCHIVE_INTEGRATION') == '1', 'set SHELAT_ARCHIVE_INTEGRATION=1 with archives present')
    def test_recompute(self):
        data = json.loads(OUTPUT.read_text())
        one = collect(ROOT / '.arena/shelat2026/exp1.zip', 1)
        two = collect(ROOT / '.arena/shelat2026/exp2.zip', 2)
        groups = {'exp1': one, 'exp2': two, 'pooled': {**one, **two}}
        for name, group in groups.items():
            self.assertEqual(summarize(group), data['results'][name])
            for trigger in ('fast', 'slow', 'fixed'):
                subgroup = {subject: [r for r in records if r['trigger'] == trigger]
                            for subject, records in group.items()}
                self.assertEqual(summarize(subgroup), data['post_result_within_trigger'][trigger][name])


if __name__ == '__main__':
    unittest.main()
