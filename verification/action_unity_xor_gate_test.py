import unittest
from fractions import Fraction as F
from itertools import product

from action_unity_xor_gate import distribution, local_oracle, local_strategies, run


class ActionUnityXorTest(unittest.TestCase):
    def test_balanced_and_biased_bounds(self):
        balanced = dict.fromkeys(product((0, 1), repeat=2), F(1, 4))
        for side in (0, 1):
            self.assertEqual(local_oracle(balanced, side), F(1, 2))
            self.assertEqual(local_oracle(distribution(), side), F(3, 4))
            self.assertEqual(len(local_strategies(balanced, side)), 4)

    def test_receipt(self):
        result = run()
        self.assertTrue(result['action_changes_under_either_input_flip_for_all_four_inputs'])
        self.assertTrue(result['balanced_action_independent_of_either_input_marginally'])


if __name__ == '__main__':
    unittest.main()
