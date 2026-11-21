import unittest
from paingen_prompt_order_control import enumerate_orders, exact_summary


class PromptOrderControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.counts = enumerate_orders()
        cls.summary = exact_summary(cls.counts)

    def test_hand_counts_and_symmetry(self):
        expected = [1, 64, 784, 3136, 4900, 3136, 784, 64, 1]
        self.assertEqual([self.counts[k] for k in range(9)], expected)
        self.assertEqual(sum(expected), 12870)
        self.assertEqual(expected, expected[::-1])

    def test_mean_and_variance(self):
        self.assertEqual(self.summary['mean'], '4')
        self.assertEqual(self.summary['variance'], '16/15')
        self.assertEqual(self.summary['independent_fair_coin_variance'], '2')

    def test_tail_and_balance(self):
        self.assertEqual(self.summary['prob_exactly_four'], '490/1287')
        self.assertEqual(self.summary['prob_three_to_five'], '1862/2145')
        self.assertEqual(self.summary['prob_all_same'], '1/6435')
        self.assertEqual(self.summary['independent_fair_coin_prob_all_same'], '1/128')


if __name__ == '__main__':
    unittest.main()
