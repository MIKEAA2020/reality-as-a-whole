import unittest
from itertools import product
from model import (subsets,joint_profile,all_families,compatible_families,
                   maximal_supports,overlap_amalgamates,amalgamation_closure,
                   is_partition,partitions,rename,type_projection,physical_joint_report)


class UnityTests(unittest.TestCase):
    def setUp(self):
        self.v=frozenset('abc')
        self.one=frozenset({self.v})
        self.pairs=frozenset(frozenset(x) for x in ('ab','ac','bc'))

    def test_01_single_and_pair_profiles_do_not_determine_triple(self):
        self.assertEqual(joint_profile(self.v,self.one,2),joint_profile(self.v,self.pairs,2))
        self.assertNotEqual(joint_profile(self.v,self.one,3),joint_profile(self.v,self.pairs,3))

    def test_02_maximality_does_not_remove_counterexample(self):
        self.assertEqual(maximal_supports(self.one),self.one)
        self.assertEqual(maximal_supports(self.pairs),self.pairs)

    def test_03_exact_enumeration_three_occurrence_families(self):
        self.assertEqual(len(tuple(all_families(self.v))),109)

    def test_04_two_maximal_families_match_complete_pair_data(self):
        observed=joint_profile(self.v,self.one,2)
        family=compatible_families(self.v,observed,2,maximal_only=True)
        self.assertEqual(set(family),{self.one,self.pairs})

    def test_05_triple_witness_selects_maximal_support_in_this_class(self):
        observed=joint_profile(self.v,self.one,3)
        family=compatible_families(self.v,observed,3,maximal_only=True)
        self.assertEqual(family,(self.one,))

    def test_06_full_joint_profile_recovers_only_maximal_supports(self):
        for f in all_families(self.v):
            profile=joint_profile(self.v,f,3)
            self.assertEqual(maximal_supports(profile),maximal_supports(f))

    def test_07_full_joint_profile_does_not_count_nested_episode_witnesses(self):
        nested=self.one|{frozenset('ab')}
        self.assertEqual(joint_profile(self.v,nested,3),joint_profile(self.v,self.one,3))
        self.assertNotEqual(len(nested),len(self.one))

    def test_08_pairwise_existence_relation_need_not_be_transitive(self):
        f=frozenset({frozenset('ab'),frozenset('bc')})
        p=joint_profile(self.v,f,2)
        self.assertIn(frozenset('ab'),p)
        self.assertIn(frozenset('bc'),p)
        self.assertNotIn(frozenset('ac'),p)

    def test_09_pairwise_clique_does_not_imply_joint_episode(self):
        self.assertTrue(all(s in joint_profile(self.v,self.pairs,2)
                            for s in subsets(self.v) if len(s)==2))
        self.assertNotIn(self.v,joint_profile(self.v,self.pairs,3))

    def test_10_transitive_partition_rule_is_an_additional_assumption(self):
        self.assertFalse(is_partition(self.v,self.pairs))
        self.assertTrue(is_partition(self.v,self.one))

    def test_11_partition_assumption_makes_pair_data_identifying(self):
        ps=tuple(partitions(self.v))
        self.assertEqual(len(ps),5)
        profiles=[joint_profile(self.v,p,2) for p in ps]
        self.assertEqual(len(set(profiles)),5)

    def test_12_amalgamation_fails_for_pair_triangle(self):
        self.assertFalse(overlap_amalgamates(self.pairs))
        self.assertTrue(overlap_amalgamates(self.one))

    def test_13_enforcing_amalgamation_manufactures_joint_support(self):
        closed=amalgamation_closure(self.pairs)
        self.assertIn(self.v,closed)
        self.assertEqual(maximal_supports(closed),self.one)

    def test_14_amalgamation_theorem_checked_on_all_three_vertex_families(self):
        checked=0
        for f in all_families(self.v):
            if overlap_amalgamates(f):
                self.assertTrue(is_partition(self.v,maximal_supports(f)))
                checked+=1
        self.assertGreater(checked,0)

    def test_15_amalgamation_theorem_checked_on_four_vertex_families(self):
        v=frozenset('abcd')
        checked=0
        for f in all_families(v):
            if overlap_amalgamates(f):
                self.assertTrue(is_partition(v,maximal_supports(f)))
                checked+=1
        self.assertGreater(checked,0)

    def test_16_every_partition_obeys_amalgamation(self):
        for p in partitions(frozenset('abcd')):
            self.assertTrue(overlap_amalgamates(p))

    def test_17_common_controller_can_force_false_amalgamation(self):
        v=frozenset('xyc')
        causal_supports=frozenset({frozenset('xc'),frozenset('yc')})
        self.assertEqual(maximal_supports(amalgamation_closure(causal_supports)),frozenset({v}))
        # This is the consequence of imposing closure, not evidence for one subject.

    def test_18_distinct_occurrences_with_same_types_are_not_renamings(self):
        f=frozenset({frozenset({'a1','b1'}),frozenset({'b2','c1'}),frozenset({'a2','c2'})})
        labels={'a1':'a','a2':'a','b1':'b','b2':'b','c1':'c','c2':'c'}
        self.assertEqual(type_projection(f,labels),self.pairs)
        self.assertTrue(is_partition(frozenset(labels),f))
        with self.assertRaises(ValueError):
            rename(f,labels)

    def test_19_duplicate_episodes_survive_occurrence_provenance(self):
        one=frozenset({frozenset({'a1','b1','c1'})})
        second=frozenset({'a2','b2','c2'})
        f=one|{second}
        labels={v:v[0] for e in f for v in e}
        self.assertEqual(type_projection(f,labels),self.one)
        self.assertEqual(len(f),2)

    def test_20_joint_report_does_not_depend_on_episode_interpretation(self):
        for state in product((0,1),repeat=3):
            # Same physical readout under both candidate episode assignments.
            self.assertEqual(physical_joint_report(state),state)
        self.assertNotEqual(self.one,self.pairs)

    def test_21_passive_renaming_preserves_joint_profile(self):
        mapping=dict(zip('abc','XYZ'))
        renamed=rename(self.pairs,mapping)
        self.assertEqual(joint_profile(frozenset('XYZ'),renamed,2),
                         rename(joint_profile(self.v,self.pairs,2),mapping))

    def test_22_adding_unobserved_episode_does_not_change_selected_profile(self):
        hidden=frozenset('uvw')
        f=self.one|{hidden}
        # Query restricted to old selected vertices; full population differs.
        observed=frozenset(s for s in joint_profile(self.v|hidden,f,3) if s.issubset(self.v))
        self.assertEqual(observed,joint_profile(self.v,self.one,3))
        self.assertEqual(len(f),2)

    def test_23_time_indexing_prevents_false_shared_content_occurrence(self):
        f=frozenset({frozenset({'a@0','b@0'}),frozenset({'b@1','c@1'})})
        self.assertTrue(overlap_amalgamates(f))
        self.assertEqual(maximal_supports(amalgamation_closure(f)),f)
        labels={v:v[0] for e in f for v in e}
        coarse=type_projection(f,labels)
        self.assertFalse(overlap_amalgamates(coarse))
        self.assertEqual(maximal_supports(amalgamation_closure(coarse)),self.one)

    def test_24_pair_data_do_not_supply_probability_weights(self):
        observed=joint_profile(self.v,self.one,2)
        family=compatible_families(self.v,observed,2,maximal_only=True)
        self.assertEqual(len(family),2)
        # Cardinality gives neither observer count nor a reason for 1/2 per model.
        self.assertEqual({len(f) for f in family},{1,3})

if __name__=='__main__':
    unittest.main(verbosity=2)
