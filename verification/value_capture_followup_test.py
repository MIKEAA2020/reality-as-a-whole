#!/usr/bin/env python3
"""Arithmetic and model-output checks; not a reproduction of source studies."""
import json
import unittest
from pathlib import Path

from scipy.stats import t

ROOT = Path(__file__).resolve().parent


class FollowupChecks(unittest.TestCase):
    def test_reported_t_statistics(self):
        # Two-sided p, with t and df taken exactly as printed; no raw data.
        p2017_sample = 2 * t.sf(2.30, 39)
        p2011_pooled = 2 * t.sf(2.19, 49)
        p2011_cross = 2 * t.sf(2.73, 58)
        self.assertAlmostEqual(p2017_sample, .027, delta=.001)
        self.assertAlmostEqual(p2011_pooled, .034, delta=.001)
        self.assertAlmostEqual(p2011_cross, .00837, delta=.00002)
        self.assertGreater(abs(p2011_cross - .016), .007)

    def test_selected_model_contrast_values(self):
        models = json.loads((ROOT / 'shelat_2026_laplace_accuracy_reproduction.json').read_text())['results']
        contrasts = models['pooled_full']['exploratory_observed_block_contrasts']
        checks = [('block1:fast:reward_vs_neutral', .420, .187, .652),
                  ('block1:fast:reward_vs_selection', .186, -.047, .420),
                  ('block2:fast:reward_vs_selection', .096, -.056, .248),
                  ('block4:fast:reward_vs_selection', -.084, -.334, .165)]
        for name, estimate, low, high in checks:
            with self.subTest(name=name):
                result = contrasts[name]
                for actual, expected in [(result['estimate'], estimate), (result['wald_95_ci'][0], low), (result['wald_95_ci'][1], high)]:
                    self.assertAlmostEqual(actual, expected, delta=.0006)


if __name__ == '__main__':
    unittest.main()
