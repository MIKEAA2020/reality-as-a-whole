#!/usr/bin/env python3
"""Check Gaussian REML against a separately built dense synthetic model."""
import json
import os
import unittest
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from shelat_2026_rt_mixed_reproduction import design, fit, load

ROOT = Path(__file__).resolve().parent.parent
RESULT = ROOT / 'verification/shelat_2026_rt_mixed_reproduction.json'


class RTChecks(unittest.TestCase):
    def test_cell_reml_matches_dense_trial_level_synthetic_model(self):
        rng = np.random.default_rng(674)
        cells = {}
        X, y, groups = [], [], []
        for subject in range(7):
            offset = rng.normal(0, 19)
            for condition in ('neutral', 'novel', 'reward', 'selection'):
                for trigger in ('fast', 'slow'):
                    vector = design(condition, trigger)
                    vals = 600 + offset + 7*vector[2] + 14*vector[4] + rng.normal(0, 25, 3)
                    cells[(str(subject), condition, trigger)] = [len(vals), vals.sum(), (vals**2).sum(), len(vals)]
                    for val in vals:
                        X.append(vector)
                        y.append(val)
                        groups.append(subject)
        X, y, groups = np.array(X), np.array(y), np.array(groups)
        n, p = X.shape
        Z = (groups[:, None] == np.arange(7)[None, :]).astype(float)

        def dense(logratio, details=False):
            V = np.eye(n) + np.exp(logratio)*(Z @ Z.T)
            # This intentionally uses a full trial-by-trial covariance matrix.
            solved = np.linalg.solve(V, np.column_stack((X, y)))
            xx, xy = X.T @ solved[:, :p], X.T @ solved[:, p]
            beta = np.linalg.solve(xx, xy)
            residual = y @ solved[:, p] - beta @ xy
            sig2 = residual/(n-p)
            value = (n-p)*np.log(sig2) + np.linalg.slogdet(V)[1] + np.linalg.slogdet(xx)[1]
            return (value, beta, sig2, sig2*np.linalg.inv(xx)) if details else value

        opt = minimize_scalar(dense, bounds=(-12, 8), method='bounded', options={'xatol': 1e-10})
        _, beta, sig2, cov = dense(opt.x, True)
        aggregate = fit(cells)
        self.assertTrue(aggregate['optimizer_success'])
        self.assertAlmostEqual(aggregate['log_variance_ratio'], opt.x, delta=2e-4)
        self.assertAlmostEqual(aggregate['residual_sd_ms'], np.sqrt(sig2), delta=2e-4)
        for i, term in enumerate(('Intercept', 'distractor_novel', 'distractor_reward', 'distractor_selection', 'trigger_slow', 'distractor_novel:trigger_slow', 'distractor_reward:trigger_slow', 'distractor_selection:trigger_slow')):
            self.assertAlmostEqual(aggregate['terms'][term]['estimate_ms'], beta[i], delta=2e-4)
            self.assertAlmostEqual(aggregate['terms'][term]['se_ms'], np.sqrt(cov[i, i]), delta=2e-4)

    def test_saved_results_and_article_comparison(self):
        results = json.loads(RESULT.read_text())['results']
        for name, n in [('exp1', 6781), ('exp2', 6447), ('pooled', 13228)]:
            r = results[name]
            self.assertTrue(r['optimizer_success'])
            self.assertEqual(r['retained_trials'], n)
            self.assertLess(abs(r['profile_derivative']), .001)
            self.assertGreater(r['profile_curvature'], 0)
            self.assertGreater(r['random_intercept_sd_ms'], 0)
        pooled = results['pooled']
        self.assertEqual(pooled['correct_trials'], 7581)
        reward = pooled['terms']['distractor_reward']
        self.assertAlmostEqual(reward['estimate_ms'], 12.29, delta=.01)
        self.assertAlmostEqual(reward['se_ms'], 5.78, delta=.01)
        self.assertAlmostEqual(pooled['exploratory_contrasts']['fast:reward_vs_selection']['estimate_ms'], 4.6861, delta=.001)

    @unittest.skipUnless(os.getenv('SHELAT_ARCHIVE_INTEGRATION') == '1', 'set SHELAT_ARCHIVE_INTEGRATION=1 with archives present')
    def test_recompute_from_archives(self):
        one = load(ROOT / '.arena/shelat2026/exp1.zip', 1)
        two = load(ROOT / '.arena/shelat2026/exp2.zip', 2)
        saved = json.loads(RESULT.read_text())['results']
        for name, data in [('exp1', one), ('exp2', two), ('pooled', {**one, **two})]:
            result = fit(data)
            self.assertEqual(result['retained_trials'], saved[name]['retained_trials'])
            for section in ('terms', 'exploratory_contrasts'):
                for term, stats in result[section].items():
                    for key in ('estimate_ms', 'se_ms', 'p_unadjusted_normal'):
                        self.assertAlmostEqual(stats[key], saved[name][section][term][key], delta=1e-5)


if __name__ == '__main__':
    unittest.main()
