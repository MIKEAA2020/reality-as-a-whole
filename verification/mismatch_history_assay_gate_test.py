import unittest
from fractions import Fraction as F
from mismatch_history_assay_gate import CELLS, check, compositions, metrics, quality


class TestHistoryAssayGate(unittest.TestCase):
    def test_exhaustive_budget_grid(self):
        result = check()
        self.assertEqual(result['grid_joint_tables'], 330)
        self.assertEqual(result['grid_rule_and_error_budget_cases'], 50)

    def test_known_mixtures_have_sharp_interval_on_rational_grid(self):
        n = 4
        for counts in compositions(n, len(CELLS)):
            mixture = [F(i, n) for i in counts]
            tables = [t for t in compositions(n, 8)
                      if all(t[2*i] + t[2*i+1] == counts[i] for i in range(4))]
            for rule in ('level', 'onset'):
                base = sum(p * quality(rule, c) for p, c in zip(mixture, CELLS))
                for eta in (F(i, n) for i in range(n+1)):
                    rates = [metrics(rule, t, n)[2] for t in tables
                             if metrics(rule, t, n)[1] <= eta]
                    self.assertEqual(min(rates), max(F(0), base-eta))
                    self.assertEqual(max(rates), min(F(1), base+eta))

    def test_global_budget_example(self):
        self.assertEqual(F(check()['global_budget_example']['conditional_sum_upper_bound']), F(784, 1775))


if __name__ == '__main__':
    unittest.main()
