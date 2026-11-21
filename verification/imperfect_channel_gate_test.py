import unittest
from fractions import Fraction as F
from math import atanh, exp, log
from imperfect_channel_gate import calc, coef_box, conditional_cells, odds, odds_box


class TestImperfectChannelGate(unittest.TestCase):
    def test_exact_odds_and_bounds(self):
        result = calc()
        self.assertEqual(result['exact_conditional_odds'], {'baseline': '9', 'A_gate': '1', 'B_gate': '81'})
        for t in (F(0), F(1, 2), F(4, 5)):
            cells = conditional_cells(t)
            lo, hi = odds_box(cells, F(1, 50))
            self.assertLess(lo, odds(cells))
            self.assertGreater(hi, odds(cells))
            self.assertAlmostEqual(log(float(odds(cells)))/4, atanh(float(t)))
        self.assertLess(result['simultaneous_Hoeffding_failure_bound'], .05)

    def test_bounds_for_negative_and_crossing_zero(self):
        self.assertEqual(coef_box(F(-1), F(-1, 2), F(1, 4), F(1, 2), F(1)),
                         (F(-5, 2), F(-1, 4)))
        self.assertEqual(coef_box(F(-1, 4), F(1, 4), F(1, 4), F(1, 2), F(1)),
                         (F(-1), F(1)))

    def test_opposite_sign_models(self):
        models = calc()['nonselective_opposite_target_counterexample']['models']
        self.assertGreater(F(models[0]['target_J']), 0)
        self.assertLess(F(models[1]['target_J']), 0)
        self.assertTrue(all(abs(F(m['residual_drift'])) <= F(2, 5) for m in models))


if __name__ == '__main__':
    unittest.main()
