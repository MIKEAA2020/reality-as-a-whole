import unittest
from itertools import product
from model import (STATES,ACTIONS,step,content,rich_target,thin_target,physical_reports,
                   project,target_factors,factorization_witnesses,minimal_sufficient_supports,
                   target_partition,history,realized_profiles,satisfies_current_data)


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.a = (0,0,0,0)
        self.b = (0,1,0,0)

    def test_01_full_state_and_intervention_closure(self):
        self.assertEqual(len(STATES),32)
        self.assertTrue(all(step(s,a) in STATES for s,a in product(STATES,ACTIONS)))

    def test_02_local_content_commutes_under_all_interventions(self):
        # Actions on context are invisible to this complete content interface.
        for s,t,a in product(STATES,STATES,ACTIONS):
            if content(s)==content(t):
                self.assertEqual(content(step(s,a)),content(step(t,a)))

    def test_03_context_extension_preserves_complete_local_history(self):
        for word in product(ACTIONS,repeat=4):
            self.assertEqual(history(self.a,word,content),history(self.b,word,content))

    def test_04_local_content_fails_rich_phenomenal_factorization(self):
        self.assertFalse(target_factors(STATES,content,rich_target))
        self.assertIn((self.a,self.b),factorization_witnesses(STATES,content,rich_target))

    def test_05_same_local_content_suffices_for_thin_interpretation(self):
        self.assertTrue(target_factors(STATES,content,thin_target))

    def test_06_context_sensitive_repair_has_exactly_one_minimal_coordinate_support(self):
        self.assertEqual(minimal_sufficient_supports(STATES,rich_target),((0,1),))

    def test_07_report_and_hidden_memory_need_not_enter_support(self):
        for q,v,r,z in STATES:
            self.assertEqual(rich_target((q,v,r,z)),(q,v))
        self.assertTrue(target_factors(STATES,lambda s:project(s,(0,1)),rich_target))

    def test_08_both_interpretations_agree_on_original_context_slice(self):
        # Original datum characterizes content contrasts at v=0, not every quality.
        data=[((q,0,0,0),(r,0,0,0),q!=r) for q,r in product(range(4),repeat=2)]
        self.assertTrue(satisfies_current_data(thin_target,data))
        self.assertTrue(satisfies_current_data(rich_target,data))

    def test_09_new_experiential_contrast_refutes_content_only_conditionally(self):
        data=[(self.a,self.b,True)]  # Supplied hypothetical first-person contrast.
        self.assertFalse(satisfies_current_data(thin_target,data))
        self.assertTrue(satisfies_current_data(rich_target,data))

    def test_10_rich_phenomenal_model_does_not_alter_physical_report_function(self):
        # Identical physical machine; interpretation not an input to its reports.
        for s in STATES:
            self.assertEqual(physical_reports(s),(s[0],s[1],s[2]))

    def test_11_equal_reports_alone_do_not_select_a_phenomenal_interpretation(self):
        for word in product(ACTIONS,repeat=3):
            reports_for_Hq=history(self.a,word,physical_reports)
            reports_for_Hqv=history(self.a,word,physical_reports)
            self.assertEqual(reports_for_Hq,reports_for_Hqv)
        self.assertNotEqual(thin_target(self.a)!=thin_target(self.b),rich_target(self.a)!=rich_target(self.b))

    def test_12_future_phenomenal_congruence_rich_has_eight_classes(self):
        p,_=target_partition(STATES,ACTIONS,rich_target,step)
        self.assertEqual(len(set(p)),8)

    def test_13_future_content_congruence_thin_has_four_classes(self):
        p,_=target_partition(STATES,ACTIONS,thin_target,step)
        self.assertEqual(len(set(p)),4)

    def test_14_future_relevance_depends_on_coupling(self):
        p,_=target_partition(STATES,ACTIONS,content,lambda s,a:step(s,a,feedback=True))
        self.assertEqual(len(set(p)),8)

    def test_15_episode_horizon_is_substantive(self):
        now,_=target_partition(STATES,ACTIONS,content,lambda s,a:step(s,a,feedback=True),horizon=0)
        future,_=target_partition(STATES,ACTIONS,content,lambda s,a:step(s,a,feedback=True),horizon=1)
        self.assertEqual((len(set(now)),len(set(future))),(4,8))

    def test_16_context_intervention_need_not_affect_old_content(self):
        for s in STATES:
            self.assertEqual(content(step(s,'flip_v')),content(s))
            self.assertNotEqual(rich_target(step(s,'flip_v')),rich_target(s))

    def test_17_report_intervention_leaves_both_candidate_targets_unchanged(self):
        for s in STATES:
            self.assertNotEqual(physical_reports(step(s,'flip_r')),physical_reports(s))
            self.assertEqual(thin_target(step(s,'flip_r')),thin_target(s))
            self.assertEqual(rich_target(step(s,'flip_r')),rich_target(s))

    def test_18_restricted_domains_can_hide_missing_constitution(self):
        fixed=tuple(s for s in STATES if s[1]==0)
        self.assertTrue(target_factors(fixed,content,rich_target))
        self.assertFalse(target_factors(STATES,content,rich_target))

    def test_19_synchronized_duplicate_does_not_shrink_supplied_occurrence_list(self):
        occurrences=realized_profiles([self.a,self.a],rich_target)
        self.assertEqual(len(occurrences),2)
        self.assertEqual(occurrences[0][1],occurrences[1][1])
        self.assertNotEqual(occurrences[0][0],occurrences[1][0])

    def test_20_local_profile_does_not_count_hidden_copy(self):
        one=realized_profiles([self.a],rich_target)
        two=realized_profiles([self.a,self.a],rich_target)
        self.assertEqual(one[0][1],two[0][1])
        self.assertNotEqual(len(one),len(two))

    def test_21_passive_renaming_preserves_partition(self):
        original,_=target_partition(STATES,ACTIONS,rich_target,step)
        labels={s:('renamed',i) for i,s in enumerate(STATES)}
        inverse={v:k for k,v in labels.items()}
        moved,_=target_partition(tuple(labels[s] for s in STATES),ACTIONS,
                                 lambda s:rich_target(inverse[s]),
                                 lambda s,a:labels[step(inverse[s],a)])
        self.assertEqual(original,moved)

    def test_22_full_explanatory_profile_not_just_current_state(self):
        self.assertEqual(content(self.a),content(self.b))
        self.assertNotEqual(content(step(self.a,'hold',feedback=True)),
                            content(step(self.b,'hold',feedback=True)))

    def test_23_no_observer_weights_are_derived(self):
        # Supplied role profiles are not a normalized observer distribution.
        self.assertEqual(realized_profiles([self.a,self.a,self.b],rich_target),
                         ((0,(0,0)),(1,(0,0)),(2,(0,1))))

    def test_24_report_boundary_does_not_follow_from_variable_name(self):
        # If the proposed target includes r, it becomes relevant by that new premise.
        target=lambda s:(s[0],s[1],s[2])
        self.assertEqual(minimal_sufficient_supports(STATES,target),((0,1,2),))
        self.assertFalse(target_factors(STATES,lambda s:project(s,(0,1)),target))

if __name__=='__main__':
    unittest.main(verbosity=2)
