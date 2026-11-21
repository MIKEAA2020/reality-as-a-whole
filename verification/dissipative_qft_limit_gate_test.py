import unittest
from fractions import Fraction as F
from dissipative_qft_limit_gate import abel, channel, run


class DissipativeLimitTests(unittest.TestCase):
    def test_receipt_and_complete_positivity_checks(self):
        result = run()
        self.assertEqual(result['choi_principal_minors_checked'], 135)
        self.assertEqual(result['semigroup_q_pairs'], 81)

    def test_population_and_coherence(self):
        state = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
        self.assertEqual(channel(state, F(1, 2)),
                         [[F(7, 8), F(1, 4)], [F(1, 4), F(1, 8)]])

    def test_balanced_abel_path(self):
        self.assertEqual(abel(F(1, 101), F(1, 101)), F(1, 3))


if __name__ == '__main__':
    unittest.main()
