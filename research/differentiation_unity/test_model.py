import unittest
from model import *


class DifferentiationUnityTests(unittest.TestCase):
    def test_01_full_content_combinability(self):
        self.assertEqual(set(STATES),set(product((0,1),repeat=2)))

    def test_02_resets_prepare_every_content_combination(self):
        for initial in STATES:
            prepared={reset(reset(initial,0,x),1,y) for x,y in STATES}
            self.assertEqual(prepared,set(STATES))

    def test_03_current_content_resets_commute(self):
        for s in STATES:
            for x,y in STATES:
                self.assertEqual(reset(reset(s,0,x),1,y),reset(reset(s,1,y),0,x))

    def test_04_reset_changes_only_selected_current_feature(self):
        for s in STATES:
            for i in (0,1):
                result=reset(s,i,1-s[i])
                self.assertEqual(result[1-i],s[1-i])

    def test_05_independent_state_preparation_does_not_make_dynamics_product(self):
        self.assertEqual(product_dynamics(source),())

    def test_06_identity_dynamics_do_factor(self):
        self.assertEqual(product_dynamics(lambda s:s),(((0,1),(0,1)),))

    def test_07_uniform_distribution_is_independent(self):
        uniform={s:Fraction(1,4) for s in STATES}
        self.assertTrue(statistically_independent(uniform))

    def test_08_irreducible_dynamics_preserve_uniform_independence(self):
        distribution={s:Fraction(1,4) for s in STATES}
        for _ in range(9):
            distribution=pushforward(distribution,source)
            self.assertTrue(statistically_independent(distribution))

    def test_09_product_dynamics_can_preserve_statistical_dependence(self):
        correlated={s:Fraction(1,2) if s[0]==s[1] else Fraction(0) for s in STATES}
        self.assertFalse(statistically_independent(pushforward(correlated,lambda s:s)))

    def test_10_inverse_is_exact(self):
        for s in STATES:
            self.assertEqual(inverse(source(s)),s)
            self.assertEqual(source(inverse(s)),s)

    def test_11_four_native_and_four_transported_resets(self):
        self.assertEqual(len(set(native_resets())),4)
        self.assertEqual(len(set(transported_resets())),4)

    def test_12_future_transported_resets_are_not_native_local_resets(self):
        self.assertFalse(set(native_resets())&set(transported_resets()))

    def test_13_transported_operations_remain_idempotent(self):
        for table in transported_resets():
            for s in STATES:
                self.assertEqual(map_value(table,map_value(table,s)),map_value(table,s))

    def test_14_original_commuting_operations_still_commute_after_transport(self):
        tables=transported_resets()
        for a in tables[:2]:
            for b in tables[2:]:
                for s in STATES:
                    self.assertEqual(map_value(a,map_value(b,s)),map_value(b,map_value(a,s)))

    def test_15_eight_distinct_content_square_maps(self):
        self.assertEqual(len(set(square_maps())),8)

    def test_16_all_maps_preserve_content_distance(self):
        for h in square_maps():
            for s,t in product(STATES,repeat=2):
                self.assertEqual(sum(a!=b for a,b in zip(s,t)),
                                 sum(a!=b for a,b in zip(map_value(h,s),map_value(h,t))))

    def test_17_temporal_structure_uniquely_selects_content_map(self):
        self.assertEqual(dynamic_matches(source,source),(STATES,))

    def test_18_identity_dynamics_leave_eight_content_maps(self):
        self.assertEqual(len(dynamic_matches(lambda s:s,lambda s:s)),8)

    def test_19_incompatible_target_dynamics_reject_all_content_maps(self):
        self.assertEqual(dynamic_matches(source,lambda s:s),())

    def test_20_joint_and_split_descriptions_have_same_marginals(self):
        for s in STATES:
            self.assertEqual(marginal_evidence(describe(s,joint=True)),marginal_evidence(describe(s,joint=False)))

    def test_21_incidence_distinguishes_descriptions(self):
        for s in STATES:
            joint=describe(s,joint=True)
            split=describe(s,joint=False)
            a,b=sorted(joint.contents,key=lambda c:c.feature)
            self.assertTrue(joint.co_present(a,b))
            self.assertFalse(split.co_present(a,b))
            self.assertNotEqual(joint.supports,split.supports)

    def test_22_unique_content_mapping_does_not_remove_incidence_ambiguity(self):
        self.assertEqual(len(dynamic_matches(source,source)),1)
        for s in STATES:
            self.assertEqual(len(compatibility_from_marginals(s)),2)

    def test_23_content_tokens_preserve_time_and_run_provenance(self):
        a=describe((0,1),joint=True,run='a',tick=0)
        b=describe((0,1),joint=True,run='a',tick=1)
        c=describe((0,1),joint=True,run='b',tick=0)
        self.assertFalse(a.contents&b.contents)
        self.assertFalse(a.contents&c.contents)
        self.assertEqual(a.values(),b.values())

    def test_24_invalid_probabilities_and_unknown_supports_rejected(self):
        with self.assertRaises(ValueError):
            statistically_independent({s:Fraction(1,3) for s in STATES})
        d=describe((0,1),joint=True)
        unknown=ContentOccurrence('elsewhere',0,0,0)
        with self.assertRaises(ValueError):
            EpisodeDescription(d.contents,frozenset({frozenset({unknown})}))

if __name__=='__main__':
    unittest.main(verbosity=2)
