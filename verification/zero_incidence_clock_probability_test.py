import math
import unittest
from verification.zero_incidence_clock_probability import sample, conditional_balance, admissible_ratio


class ZeroIncidenceClockProbabilityTests(unittest.TestCase):
    def test_actual_density_fraction_and_zero(self):
        out=sample()
        self.assertAlmostEqual(out['signed_total'],0,places=11)
        self.assertAlmostEqual(out['total'],2*math.pi,places=10)
        self.assertAlmostEqual(out['positive_fraction'],0.5+0.5/math.pi,places=8)
        self.assertAlmostEqual(out['negative_fraction'],0.5-0.5/math.pi,places=8)

    def test_conditioning_changes_mean_and_fraction(self):
        out=sample()
        self.assertAlmostEqual(out['selected_mean'],2/9,places=10)
        self.assertAlmostEqual(out['selected_positive'],0.5+8/(9*math.pi),places=8)

    def test_repartition_does_not_change_measure(self):
        a=sample(cells=1000,split=1)
        b=sample(cells=1000,split=4)
        for key in a:
            self.assertAlmostEqual(a[key],b[key],places=11)

    def test_equal_accounting_and_sampling_is_an_assumption(self):
        # Weighting B by K rather than integrating B itself breaks balance.
        out=sample()
        self.assertAlmostEqual(out['signed_total'],0,places=11)
        self.assertAlmostEqual(out['naive_weighted_total'],math.pi/2,places=11)
        # Distinct self-location weights need not have zero mean.
        self.assertAlmostEqual(out['selected_mean'],2/9,places=10)

    def test_zero_balance_probability_relation_with_neutral(self):
        self.assertAlmostEqual(conditional_balance(0.0,1,2),1/3)
        self.assertAlmostEqual(conditional_balance(0.25,1,2),1/4)
        with self.assertRaises(ValueError): conditional_balance(0,0,2)

    def test_support_is_not_silently_extended(self):
        self.assertIsNone(admissible_ratio(0,0))
        with self.assertRaises(ValueError): admissible_ratio(0,1)
        with self.assertRaises(ValueError): admissible_ratio(-1,1)
        self.assertEqual(admissible_ratio(2,-1),-0.5)

    def test_inputs(self):
        for args in ({'b':1},{'ell':1.1},{'cells':0},{'split':0}):
            with self.assertRaises(ValueError): sample(**args)


if __name__=='__main__': unittest.main()
