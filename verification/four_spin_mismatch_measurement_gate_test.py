import unittest
from fractions import Fraction as F
from itertools import product
from four_spin_mismatch_measurement_gate import dist, majority_failure, posterior, run
from integrated_subject_horizon_audit import kernel, mismatch


class TestFourSpinMismatchMeasurement(unittest.TestCase):
    def test_same_physical_spin_sector(self):
        data = run()
        self.assertEqual(data['conditional_cross_product_odds'], ['9'] * 4)
        self.assertEqual(data['selective_gate_aligned_fractions'], {'A': '1/2', 'B': '9/10'})

    def test_majority_rule_both_orientations(self):
        self.assertEqual(majority_failure(19), F(611828695, 68719476736))
        self.assertLess(majority_failure(19), F(1, 100))
        self.assertGreater(majority_failure(17), F(1, 100))

    def test_posterior_independent_direct_enumeration(self):
        p, k = dist(F(1, 2)), kernel(F(1, 4))
        spin_error, calibration_error = F(1, 20), majority_failure(19)
        observed = numerator = F(0)
        for s in p:
            for v, transition in k[s].items():
                for wrong_pref in (0, 1):
                    pc = calibration_error if wrong_pref else 1-calibration_error
                    for errors in product((0, 1), repeat=4):
                        pe = pc
                        for bit in errors:
                            pe *= spin_error if bit else 1-spin_error
                        h0 = mismatch(s) ^ errors[0] ^ errors[1] ^ wrong_pref
                        h1 = mismatch(v) ^ errors[2] ^ errors[3] ^ wrong_pref
                        if h0 == h1 == 1:
                            weight = p[s] * transition * pe
                            observed += weight
                            if (mismatch(s), mismatch(v)) != (1, 1):
                                numerator += weight
        joint = {(0, 0): F(295,448), (0,1): F(41,448),
                 (1,0): F(41,448), (1,1): F(71,448)}
        self.assertEqual((observed, numerator/observed),
                         posterior(joint, F(19,200), calibration_error))


if __name__ == '__main__':
    unittest.main()
