import unittest
from model import *


class WeakCouplingTests(unittest.TestCase):
    def test_01_normalized_nonnegative_kernels(self):
        for e in (0,Fraction(1,1000),Fraction(1,2),1):
            for s in STATES:
                k=kernel(e,s)
                self.assertEqual(sum(k.values()),1)
                self.assertTrue(all(p>=0 for p in k.values()))

    def test_02_zero_is_identity(self):
        for s in STATES:
            self.assertEqual(kernel(0,s)[s],1)

    def test_03_one_is_previous_source(self):
        for s in STATES:
            self.assertEqual(kernel(1,s)[source(s)],1)

    def test_04_one_step_distance_exactly_epsilon(self):
        for e in (0,Fraction(1,10**6),Fraction(1,2),1):
            self.assertEqual(kernel_distance(e),e)

    def test_05_cross_influences_are_epsilon(self):
        for e in (0,Fraction(1,1000),Fraction(1,2),1):
            self.assertEqual(influence(e,0,1),e)
            self.assertEqual(influence(e,1,0),e)

    def test_06_self_influences(self):
        for e in (0,Fraction(1,1000),Fraction(1,2),1):
            self.assertEqual(influence(e,0,0),1-e)
            self.assertEqual(influence(e,1,1),1)

    def test_07_zero_has_separate_components(self):
        self.assertEqual(strongly_connected(influence_edges(0),2),frozenset({frozenset({0}),frozenset({1})}))

    def test_08_any_tested_positive_coupling_merges_components(self):
        for e in (Fraction(1,10**9),Fraction(1,2),1):
            self.assertEqual(strongly_connected(influence_edges(e),2),frozenset({frozenset({0,1})}))

    def test_09_zero_has_twenty_four_product_encodings(self):
        self.assertEqual(len(product_encodings(0)),24)

    def test_10_positive_kernels_do_not_factor(self):
        for e in (Fraction(1,10**6),Fraction(1,3),Fraction(1,2),1):
            self.assertEqual(product_encodings(e),())

    def test_11_uniform_stationary_distribution(self):
        for e in (0,Fraction(1,1000),1):
            for t in STATES:
                self.assertEqual(sum(Fraction(1,4)*kernel(e,s)[t] for s in STATES),Fraction(1,4))

    def test_12_zero_horizon_no_detection(self):
        for e in (0,Fraction(1,2),1):
            self.assertEqual(path_detection(e,0),0)

    def test_13_path_detection_exact_small_case(self):
        self.assertEqual(path_detection(Fraction(1,2),3),Fraction(7,8))

    def test_14_union_bound(self):
        for e in (Fraction(1,1000),Fraction(1,10),Fraction(1,2)):
            for t in (0,1,2,3,10):
                self.assertLessEqual(path_detection(e,t),min(1,t*e))

    def test_15_positive_coupling_shares_null_path_probability(self):
        for e in (Fraction(1,1000),Fraction(1,2)):
            self.assertLess(path_detection(e,10),1)
            self.assertGreater(path_detection(e,10),0)

    def test_16_endpoint_formula_matches_direct_propagation(self):
        for e in (Fraction(1,4),Fraction(1,2),1):
            for t in range(7):
                distribution=propagate(e,(0,1),t)
                self.assertEqual(endpoint_detection(e,t),1-distribution[(0,1)])

    def test_17_endpoint_can_hide_every_intermediate_change(self):
        self.assertEqual(path_detection(1,3),1)
        self.assertEqual(endpoint_detection(1,3),0)

    def test_18_endpoint_never_beats_full_path(self):
        for e in (0,Fraction(1,10),Fraction(1,2),1):
            for t in range(7):
                self.assertLessEqual(endpoint_detection(e,t),path_detection(e,t))

    def test_19_fixed_initial_state_never_detects_coupling(self):
        for e in (0,Fraction(1,2),1):
            self.assertEqual(propagate(e,(0,0),5)[(0,0)],1)

    def test_20_repeated_independent_paths_use_total_exposure(self):
        e,t,n=Fraction(1,100),3,5
        self.assertEqual(1-(1-path_detection(e,t))**n,path_detection(e,t*n))

    def test_21_resolution_depends_on_exposure(self):
        e=Fraction(1,1000)
        self.assertLess(path_detection(e,10),Fraction(1,100))
        self.assertGreater(path_detection(e,1000),Fraction(3,5))

    def test_22_two_cores_merge_with_any_admitted_reciprocal_bridge(self):
        self.assertEqual(threshold_components(0,0),frozenset({frozenset({0,1}),frozenset({2,3})}))
        self.assertEqual(threshold_components(Fraction(1,10**9),0),frozenset({frozenset(range(4))}))

    def test_23_threshold_changes_verdict_by_convention(self):
        e=Fraction(1,1000)
        separate=frozenset({frozenset({0,1}),frozenset({2,3})})
        self.assertEqual(threshold_components(e,e),separate)
        self.assertEqual(threshold_components(e,e/2),frozenset({frozenset(range(4))}))
        self.assertEqual(threshold_components(e,1),frozenset(frozenset({i}) for i in range(4)))

    def test_24_invalid_protocol_parameters_rejected(self):
        for e in (Fraction(-1,10),Fraction(11,10)):
            with self.assertRaises(ValueError):
                kernel(e,(0,1))
        for t in (-1,Fraction(1,2)):
            with self.assertRaises(ValueError):
                path_detection(Fraction(1,2),t)

if __name__=='__main__':
    unittest.main(verbosity=2)
