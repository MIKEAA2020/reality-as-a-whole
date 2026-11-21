import unittest
from klinge_causal_emergence_interface import closed_control, emergent_step, receipt


class CausalInterfaceTests(unittest.TestCase):
    def test_natural_records_match(self):
        for b in (0, 1):
            self.assertEqual(emergent_step(b, b), closed_control(b, b))

    def test_surgery_changes_only_emergent_model(self):
        for b in (0, 1):
            self.assertNotEqual(emergent_step(b, 0), emergent_step(b, 1))
            self.assertEqual(closed_control(b, 0), closed_control(b, 1))

    def test_immediate_disposition_determines_outcome(self):
        for b in (0, 1):
            for e in (0, 1):
                d, y = emergent_step(b, e)
                self.assertEqual(d, y)

    def test_invalid_bits_rejected(self):
        for model in (emergent_step, closed_control):
            for pair in ((-1, 0), (2, 1), (0, None), (True, 1)):
                with self.subTest(model=model.__name__, pair=pair), self.assertRaises(ValueError):
                    model(*pair)

    def test_receipt_includes_qualification(self):
        self.assertEqual(receipt()['surgical_opposite_macro_settings_with_different_outputs'], 2)
        self.assertIn('not established', receipt()['counterfactual_qualification'])


if __name__ == '__main__':
    unittest.main()
