#!/usr/bin/env python3
"""Audit saved model aggregates and, when available, reproduce archive fits."""
import json
import os
import unittest
from pathlib import Path

from shelat_2026_laplace_accuracy_reproduction import design, load, fit

ROOT = Path(__file__).resolve().parent.parent
RESULT = ROOT / 'verification/shelat_2026_laplace_accuracy_reproduction.json'


class AccuracyChecks(unittest.TestCase):
    def test_contrast_design(self):
        self.assertEqual(design(2, 'neutral', 'fast', 'full'), [1, 2] + [0.0]*14)
        x = design(2, 'reward', 'slow', 'full')
        self.assertEqual(x, [1, 2, 0., 1., 0., 1., 0., 2., 0., 2., 0., 1., 0., 0., 2., 0.])

    def test_fit_diagnostics_and_paper_selected_values(self):
        results = json.loads(RESULT.read_text())['results']
        for model, value in results.items():
            with self.subTest(model=model):
                self.assertTrue(value['optimizer_success'])
                self.assertLess(value['max_abs_gradient'], 1e-5)
                self.assertLess(value['gradient_check_max_abs_difference'], 1e-5)
                self.assertGreater(value['hessian_min_eigenvalue'], 0)
                self.assertGreater(value['random_intercept_sd'], 0)
        for model, n, beta, p in [('exp1_full', 6781, .75, .0032),
                                  ('exp2_full', 6447, .41, .089),
                                  ('pooled_full', 13228, .57, .0011)]:
            row = results[model]
            self.assertEqual(row['retained_trials'], n)
            reward = row['terms']['distractor_reward']
            self.assertAlmostEqual(reward['estimate'], beta, delta=.0051)
            self.assertAlmostEqual(reward['p'], p, delta=.0006)
        pooled = results['pooled_full']['terms']
        contrasts = results['pooled_full']['exploratory_observed_block_contrasts']
        self.assertEqual(len(contrasts), 16)
        c = contrasts['block1:fast:reward_vs_selection']
        expected = (pooled['distractor_reward']['estimate'] - pooled['distractor_selection']['estimate'] +
                    pooled['block:distractor_reward']['estimate'] - pooled['block:distractor_selection']['estimate'])
        self.assertAlmostEqual(c['estimate'], expected, places=10)
        self.assertLess(c['wald_95_ci'][0], c['estimate'])
        self.assertGreater(c['wald_95_ci'][1], c['estimate'])
        midpoint = results['pooled_full']['exploratory_block_2_5_contrasts']
        fast = midpoint['fast:reward_vs_selection']['estimate']
        slow = midpoint['slow:reward_vs_selection']['estimate']
        self.assertAlmostEqual(midpoint['slow_minus_fast:reward_vs_selection']['estimate'], slow-fast, places=10)
        self.assertAlmostEqual(fast, .0509, delta=.0001)
        for term, beta, p in [('block:distractor_reward', -.15, .020),
                              ('distractor_reward:trigger_slow', -.65, .030),
                              ('block:distractor_reward:trigger_slow', .21, .053)]:
            self.assertAlmostEqual(pooled[term]['estimate'], beta, delta=.0051)
            self.assertAlmostEqual(pooled[term]['p'], p, delta=.001)

    @unittest.skipUnless(os.getenv('SHELAT_ARCHIVE_INTEGRATION') == '1', 'set SHELAT_ARCHIVE_INTEGRATION=1 with archives present')
    def test_archive_recomputation(self):
        one = load(ROOT / '.arena/shelat2026/exp1.zip', 1)
        two = load(ROOT / '.arena/shelat2026/exp2.zip', 2)
        saved = json.loads(RESULT.read_text())['results']
        for model, data, mode in [('exp1_trigger', one, 'trigger'), ('exp2_trigger', two, 'trigger'),
                                  ('exp1_full', one, 'full'), ('exp2_full', two, 'full'),
                                  ('pooled_full', {**one, **two}, 'full'),
                                  ('pooled_block_distractor', {**one, **two}, 'block_distractor')]:
            fitted = fit(data, mode)
            self.assertTrue(fitted['optimizer_success'], model)
            self.assertEqual(fitted['retained_trials'], saved[model]['retained_trials'])
            for term, stats in fitted['terms'].items():
                for name in ('estimate', 'se', 'p'):
                    self.assertAlmostEqual(stats[name], saved[model]['terms'][term][name], delta=1e-5, msg=model + ':' + term)
            for section in ('exploratory_observed_block_contrasts', 'exploratory_block_2_5_contrasts'):
                for contrast, stats in fitted[section].items():
                    for name in ('estimate', 'se', 'p_unadjusted'):
                        self.assertAlmostEqual(stats[name], saved[model][section][contrast][name], delta=1e-5, msg=model + ':' + contrast)


if __name__ == '__main__':
    unittest.main()
