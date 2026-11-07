import unittest
from model import *


class BoundaryIdentificationTests(unittest.TestCase):
    def test_01_no_data_full_parameter_domain(self):
        self.assertEqual(likelihood_support(0,0),Interval(0,1))

    def test_02_no_changes_preserves_zero_and_arbitrarily_small_positive(self):
        region=likelihood_support(0,1000)
        self.assertTrue(region.contains(0))
        self.assertTrue(region.contains(Fraction(1,10**12)))
        self.assertFalse(region.contains(1))

    def test_03_ideal_changes_exclude_zero(self):
        region=likelihood_support(1,10)
        self.assertFalse(region.contains(0))
        self.assertTrue(region.contains(Fraction(1,10**12)))
        self.assertFalse(region.contains(1))

    def test_04_all_changes_allow_one(self):
        self.assertEqual(likelihood_support(10,10),Interval(0,1,False,True))

    def test_05_support_agrees_with_exact_likelihood(self):
        for n in range(7):
            for k in range(n+1):
                for eta in (0,Fraction(1,100),Fraction(1,2)):
                    region=likelihood_support(k,n,eta)
                    for e in (0,Fraction(1,100),Fraction(1,2),1):
                        self.assertEqual(region.contains(e),likelihood(e,k,n,eta)>0)

    def test_06_non_detection_does_not_identify_exact_boundary(self):
        self.assertEqual(boundary_set(likelihood_support(0,1000)),frozenset({SPLIT,MERGED}))

    def test_07_ideal_positive_detection_identifies_physical_merged_boundary(self):
        self.assertEqual(boundary_set(likelihood_support(1,10)),frozenset({MERGED}))

    def test_08_known_positive_noise_preserves_zero_after_detections(self):
        region=likelihood_support(1,10,Fraction(1,100))
        self.assertTrue(region.contains(0))
        self.assertEqual(boundary_set(region),frozenset({SPLIT,MERGED}))

    def test_09_half_noise_erases_parameter_information(self):
        for k in range(6):
            for e in (0,Fraction(1,10),1):
                self.assertEqual(likelihood(e,k,5,Fraction(1,2)),Fraction(1,32))

    def test_10_structural_calibration_can_supply_exact_separation(self):
        parameters=compatible_parameters(Interval(0,0),0,10)
        self.assertEqual(boundary_set(parameters),frozenset({SPLIT}))

    def test_11_positive_lower_bound_supplies_merged_core(self):
        parameters=compatible_parameters(Interval(Fraction(1,100),Fraction(1,10)),0,10)
        self.assertEqual(boundary_set(parameters),frozenset({MERGED}))

    def test_12_inconsistent_model_rejected(self):
        parameters=compatible_parameters(Interval(0,0),1,10)
        self.assertIsNone(parameters)
        self.assertEqual(boundary_set(parameters),frozenset())
        with self.assertRaises(ValueError):
            link_bounds(boundary_set(parameters))

    def test_13_likelihood_inequality_does_not_change_positive_support(self):
        self.assertEqual(likelihood(0,0,10),1)
        self.assertEqual(likelihood(Fraction(1,2),0,10),Fraction(1,1024))
        self.assertTrue(likelihood_support(0,10).contains(Fraction(1,2)))

    def test_14_ambiguous_boundary_has_different_must_and_may_links(self):
        must,may=link_bounds((SPLIT,MERGED))
        self.assertEqual(must,frozenset({(0,0),(1,1)}))
        self.assertEqual(may,frozenset({(0,0),(0,1),(1,0),(1,1)}))

    def test_15_possible_links_need_not_be_transitive(self):
        a=frozenset({frozenset({0,1}),frozenset({2})})
        b=frozenset({frozenset({0}),frozenset({1,2})})
        must,may=link_bounds((a,b))
        self.assertTrue(is_transitive(must))
        self.assertFalse(is_transitive(may))
        self.assertNotIn((0,2),may)
        self.assertIn((0,2),closure(may))

    def test_16_neither_link_summary_need_be_a_compatible_partition(self):
        a=frozenset({frozenset({0,1}),frozenset({2})})
        b=frozenset({frozenset({0}),frozenset({1,2})})
        must,may=link_bounds((a,b))
        self.assertNotIn(must,(partition_links(a),partition_links(b)))
        self.assertNotIn(closure(may),(partition_links(a),partition_links(b)))

    def test_17_singleton_model_has_identical_link_bounds(self):
        must,may=link_bounds((MERGED,))
        self.assertEqual(must,may)

    def test_18_prior_zero_mass_cannot_be_created_by_non_detection(self):
        self.assertEqual(posterior_zero_atom(0,Fraction(1,2),0,10),0)

    def test_19_zero_atom_prior_yields_positive_posterior(self):
        self.assertEqual(posterior_zero_atom(Fraction(1,2),Fraction(1,2),0,10),Fraction(1024,1025))

    def test_20_prior_choice_changes_boundary_probability(self):
        a=posterior_zero_atom(Fraction(1,10),Fraction(1,2),0,1)
        b=posterior_zero_atom(Fraction(9,10),Fraction(1,2),0,1)
        self.assertEqual(a,Fraction(2,11))
        self.assertEqual(b,Fraction(18,19))

    def test_21_ideal_detection_removes_zero_prior_atom(self):
        self.assertEqual(posterior_zero_atom(Fraction(1,2),Fraction(1,10),1,10),0)

    def test_22_noisy_detection_need_not_remove_zero_prior_atom(self):
        p=posterior_zero_atom(Fraction(1,2),Fraction(1,10),1,10,Fraction(1,100))
        self.assertGreater(p,0)
        self.assertLess(p,1)

    def test_23_interval_intersections_respect_open_endpoints(self):
        self.assertIsNone(Interval(0,Fraction(1,2),True,False).intersection(Interval(Fraction(1,2),1)))
        self.assertEqual(Interval(0,Fraction(1,2)).intersection(Interval(Fraction(1,2),1)),Interval(Fraction(1,2),Fraction(1,2)))

    def test_24_invalid_inputs_and_incompatible_domains_rejected(self):
        with self.assertRaises(ValueError):
            Interval(0,0,False,True)
        with self.assertRaises(ValueError):
            likelihood_support(2,1)
        with self.assertRaises(ValueError):
            partition_links((frozenset({0,1}),frozenset({1,2})))
        with self.assertRaises(ValueError):
            link_bounds((SPLIT,frozenset({frozenset({2})})))
        with self.assertRaises(ValueError):
            posterior_zero_atom(1,Fraction(1,10),1,1)

if __name__=='__main__':
    unittest.main(verbosity=2)
