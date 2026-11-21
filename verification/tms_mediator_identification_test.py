import unittest
from fractions import Fraction as F
from tms_mediator_identification import mediator, outcome, observed, quantities


class RandomizedMediationTests(unittest.TestCase):
    def test_hand_derived_observable_table_and_full_support(self):
        expected = [
            {(0, 0): F(9, 16), (0, 1): F(3, 16), (1, 0): F(1, 16), (1, 1): F(3, 16)},
            {(0, 0): F(3, 16), (0, 1): F(1, 16), (1, 0): F(3, 16), (1, 1): F(9, 16)}]
        for t in (0, 1):
            self.assertEqual(observed('A', t), expected[t])
            self.assertEqual(observed('B', t), expected[t])
            self.assertEqual(sum(expected[t].values()), 1)
            self.assertTrue(all(x > 0 for x in expected[t].values()))

    def test_hand_derived_effects(self):
        for model, nie, nde in (('A', F(1, 4), F(0)), ('B', F(0), F(1, 4))):
            q = quantities(model)
            self.assertEqual((q['mean_y_t0'], q['mean_y_t1'], q['ate']), (F(3, 8), F(5, 8), F(1, 4)))
            self.assertEqual((q['total_natural_indirect_effect'], q['pure_natural_direct_effect']), (nie, nde))
            self.assertEqual(nie + nde, q['ate'])

    def test_separately_intervening_on_mediator(self):
        a, b = quantities('A'), quantities('B')
        self.assertEqual((a['do_m0_given_t1'], a['do_m1_given_t1']), (F(1, 4), F(3, 4)))
        self.assertEqual((b['do_m0_given_t1'], b['do_m1_given_t1']), (F(5, 8), F(5, 8)))
        for u in range(4):
            for e in (0, 1):
                self.assertEqual(outcome('A', 1, mediator(1, u), u, e), outcome('B', 1, mediator(1, u), u, e))

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            mediator(2, 0)
        with self.assertRaises(ValueError):
            outcome('C', 0, 0, 0, 0)


if __name__ == '__main__':
    unittest.main()
