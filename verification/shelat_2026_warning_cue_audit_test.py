#!/usr/bin/env python3
import json
import os
import unittest
from pathlib import Path
from shelat_2026_warning_cue_audit import audit, classify

ROOT = Path(__file__).resolve().parent.parent
RESULT = ROOT / 'verification/shelat_2026_warning_cue_audit.json'


class WarningCueChecks(unittest.TestCase):
    def test_arrays_and_actual_color_validation(self):
        row = {'infreq_trigger': 'fast', 'triggered_colors': 'red',
               'actual_shape_colors': "['red', 'yellow', 'cyan', 'coral', 'magenta', 'lightgray']",
               'actual_bar_orientations': '[90, 45, -45, 45, -45, 45]'}
        self.assertEqual(classify(row, 'r', 'g', 'v'), ('fast', 'reward'))
        with self.assertRaises(ValueError):
            classify({**row, 'triggered_colors': 'green'}, 'r', 'g', 'v')
        with self.assertRaises(ValueError):
            classify({**row, 'actual_shape_colors': "['red', 'blue', 'cyan', 'coral', 'magenta', 'lightgray']"}, 'r', 'g', 'v')
        with self.assertRaises(ValueError):
            classify(row, 'r', 'g', 'h')
        neutral = {**row, 'infreq_trigger': '', 'triggered_colors': '',
                   'actual_shape_colors': "['yellow', 'cyan', 'coral', 'magenta', 'lightgray', 'SaddleBrown']",
                   'actual_bar_orientations': '[0, 45, -45, 45, -45, 45]'}
        self.assertEqual(classify(neutral, 'r', 'g', 'v'), ('nontrigger', 'neutral'))

    def test_saved_aggregates(self):
        data = json.loads(RESULT.read_text())['experiments']
        for result, expected in zip(data, [(119400, 6355, 2111, 110934), (115800, 6049, 2149, 107602)]):
            total, rgb, neutral_rare, nontrigger = expected
            self.assertEqual(result['data_rows'], total)
            self.assertEqual(result['rare_given_rgb'], {'numerator': rgb, 'denominator': rgb})
            self.assertEqual(result['rare_given_no_rgb'], {'numerator': neutral_rare, 'denominator': neutral_rare + nontrigger})
            self.assertEqual(result['matched_structure_rows'], total)

    @unittest.skipUnless(os.getenv('SHELAT_ARCHIVE_INTEGRATION') == '1', 'set SHELAT_ARCHIVE_INTEGRATION=1 with archives present')
    def test_archive_recomputation(self):
        saved = json.loads(RESULT.read_text())['experiments']
        for i in (1, 2):
            self.assertEqual(audit(ROOT / f'.arena/shelat2026/exp{i}.zip', i), saved[i-1])


if __name__ == '__main__':
    unittest.main()
