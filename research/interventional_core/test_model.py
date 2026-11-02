import unittest
from model import *


class InterventionalCoreTests(unittest.TestCase):
    def test_01_source_is_bijective(self):
        self.assertEqual({source(s) for s in states(2)},set(states(2)))

    def test_02_source_has_order_three(self):
        self.assertTrue(all(iterate(source,s,3)==s for s in states(2)))
        self.assertTrue(any(source(s)!=s for s in states(2)))
        self.assertTrue(any(iterate(source,s,2)!=s for s in states(2)))

    def test_03_cycle_structure(self):
        self.assertEqual(source((0,0)),(0,0))
        self.assertEqual(tuple(iterate(source,(0,1),i) for i in range(4)),
                         ((0,1),(1,1),(1,0),(0,1)))

    def test_04_monitor_matches_on_synchronous_domain(self):
        for s in states(2):
            result=circuit(s+s)
            self.assertEqual(result[:2],result[2:])
            self.assertEqual(result[:2],source(s))

    def test_05_every_initial_state_synchronizes_in_one_tick(self):
        for s in states(4):
            result=circuit(s)
            self.assertEqual(result[:2],result[2:])

    def test_06_source_projection_is_global_transition_abstraction(self):
        self.assertTrue(projection_commutes(circuit,lambda s:s[:2],source,4))

    def test_07_monitor_projection_is_not_global_transition_abstraction(self):
        self.assertFalse(projection_commutes(circuit,lambda s:s[2:],source,4))
        failures=[s for s in states(4) if circuit(s)[2:]!=source(s[2:])]
        self.assertEqual(len(failures),12)

    def test_08_same_monitor_state_can_have_different_futures(self):
        a,b=(0,0,0,0),(0,1,0,0)
        self.assertEqual(a[2:],b[2:])
        self.assertNotEqual(circuit(a)[2:],circuit(b)[2:])

    def test_09_monitor_interventions_do_not_change_source_future(self):
        for s in states(4):
            for i in (2,3):
                for horizon in (1,2,3):
                    changed=surgical(s,i,1-s[i])
                    self.assertEqual(iterate(circuit,s,horizon)[:2],iterate(circuit,changed,horizon)[:2])

    def test_10_monitor_override_is_erased_after_one_tick(self):
        for s in states(4):
            for i in (2,3):
                self.assertEqual(circuit(s),circuit(surgical(s,i,1-s[i])))

    def test_11_source_changes_propagate_to_source_and_monitor(self):
        for s in states(4):
            for i in (0,1):
                a,b=circuit(s),circuit(surgical(s,i,1-s[i]))
                self.assertNotEqual(a[:2],b[:2])
                self.assertNotEqual(a[2:],b[2:])

    def test_12_exact_influence_graph(self):
        self.assertEqual(influence_edges(circuit,4),frozenset({(0,1),(0,3),(1,0),(1,1),(1,2),(1,3)}))

    def test_13_exact_strong_components(self):
        self.assertEqual(strongly_connected(influence_edges(circuit,4),4),
                         frozenset({frozenset({0,1}),frozenset({2}),frozenset({3})}))

    def test_14_exact_autonomous_coordinate_sets(self):
        self.assertEqual(autonomous_sets(circuit,4),frozenset(map(frozenset,({0,1},{0,1,2},{0,1,3},{0,1,2,3}))))

    def test_15_source_no_independent_bit_factorization_under_any_static_encoding(self):
        self.assertEqual(factorization_encodings(source),())

    def test_16_square_has_same_irreducibility(self):
        self.assertEqual(factorization_encodings(lambda s:iterate(source,s,2)),())

    def test_17_identity_has_twenty_four_encodings(self):
        self.assertEqual(len(factorization_encodings(lambda s:s)),24)

    def test_18_three_tick_sampling_hides_integration(self):
        sampled=lambda s:iterate(source,s,3)
        self.assertEqual(influence_edges(sampled,2),frozenset({(0,0),(1,1)}))
        self.assertEqual(len(factorization_encodings(sampled)),24)

    def test_19_intermediate_intervention_is_not_inferred_from_sampled_identity(self):
        s=(0,1)
        actual=iterate(source,surgical(source(s),0,1-source(s)[0]),2)
        self.assertNotEqual(actual,s)

    def test_20_coordinate_renaming_transports_causal_graph(self):
        original=influence_edges(circuit,4)
        for order in permutations(range(4)):
            inverse={old:new for new,old in enumerate(order)}
            expected=frozenset((inverse[i],inverse[j]) for i,j in original)
            self.assertEqual(influence_edges(rename_coordinates(circuit,order),4),expected)

    def test_21_error_recoding_is_bijective(self):
        for s in states(4):
            self.assertEqual(from_error_coordinates(to_error_coordinates(s)),s)

    def test_22_mixed_encoding_changes_coordinate_graph(self):
        for s in states(4):
            self.assertEqual(error_coordinate_step(s),source(s[:2])+(0,0))
        self.assertNotEqual(influence_edges(error_coordinate_step,4),influence_edges(circuit,4))

    def test_23_two_independent_sources_have_two_cores(self):
        self.assertEqual(strongly_connected(influence_edges(paired_sources,4),4),
                         frozenset({frozenset({0,1}),frozenset({2,3})}))
        self.assertEqual(autonomous_sets(paired_sources,4),
                         frozenset(map(frozenset,({0,1},{2,3},{0,1,2,3}))))

    def test_24_time_dependent_coordinates_can_trivialize_bijective_dynamics(self):
        # z_t=A^(-t) s_t. The identity in z does not preserve the fixed
        # physical intervention labels. No clock-independent unity follows.
        for s in states(2):
            for t in range(9):
                evolved=iterate(source,s,t)
                z=iterate(source,evolved,(-t)%3)
                self.assertEqual(z,s)

if __name__=='__main__':
    unittest.main(verbosity=2)
