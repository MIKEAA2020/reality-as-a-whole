import unittest
from dataclasses import replace
from model import (KINDS,InputEvent,Protocol,simulate,baseline,label_report,identify,
                   minimal_temporal_designs,report_identification,passive_relabel,identify_uncertain)


class EpisodeReconstructionTests(unittest.TestCase):
    def setUp(self):
        self.protocol=baseline()
        self.traces={kind:simulate(kind,self.protocol) for kind in KINDS}
        self.A=frozenset({'A@input'})
        self.AB=frozenset({'A@input','B@input'})
        self.ABC=self.AB|{'C@input'}

    def test_01_identical_aggregate_reports(self):
        self.assertEqual({t.report for t in self.traces.values()},{self.ABC})

    def test_02_persistent_prediction_retains_joint_content(self):
        self.assertEqual(self.traces['persistent'].source_profile(),(self.A,self.AB,self.ABC,self.ABC))

    def test_03_sequential_prediction_has_no_earlier_joint_support(self):
        self.assertEqual(self.traces['sequential'].source_profile(),
                         (self.A,frozenset({'B@input'}),frozenset({'C@input'}),frozenset()))

    def test_04_late_replay_has_no_retroactive_jointness(self):
        trace=self.traces['late_replay']
        self.assertEqual(trace.presentation[1].sources,frozenset({'B@input'}))
        self.assertEqual(trace.presentation[3].sources,self.ABC)

    def test_05_final_report_alone_retains_all_candidates(self):
        self.assertEqual(set(report_identification(self.traces.values(),self.ABC)),set(KINDS))

    def test_06_early_joint_observation_selects_persistent_conditionally(self):
        self.assertEqual(identify(self.traces.values(),{1:self.AB}),('persistent',))

    def test_07_late_joint_observation_leaves_persistent_and_replay(self):
        self.assertEqual(set(identify(self.traces.values(),{3:self.ABC})),{'persistent','late_replay'})

    def test_08_two_temporal_observations_can_select_replay(self):
        self.assertEqual(identify(self.traces.values(),{1:frozenset({'B@input'}),3:self.ABC}),('late_replay',))

    def test_09_two_temporal_observations_can_select_sequential(self):
        self.assertEqual(identify(self.traces.values(),{1:frozenset({'B@input'}),3:frozenset()}),('sequential',))

    def test_10_exact_minimal_designs(self):
        self.assertEqual(set(minimal_temporal_designs(self.traces.values())),{(1,3),(2,3)})

    def test_11_workspace_reset_changes_candidate_presentation_not_report(self):
        p=replace(self.protocol,clear_workspace_before=frozenset({2}))
        t=simulate('persistent',p)
        self.assertEqual(t.presentation[2].sources,frozenset({'C@input'}))
        self.assertEqual(t.report,self.ABC)

    def test_12_record_reset_changes_report_not_persistent_candidate(self):
        p=replace(self.protocol,clear_record_before=frozenset({2}))
        t=simulate('persistent',p)
        self.assertEqual(t.presentation[2].sources,self.ABC)
        self.assertEqual(t.report,frozenset({'C@input'}))

    def test_13_record_reset_changes_late_replay(self):
        p=replace(self.protocol,clear_record_before=frozenset({2}))
        t=simulate('late_replay',p)
        self.assertEqual(t.presentation[3].sources,frozenset({'C@input'}))

    def test_14_record_write_block_does_not_erase_persistent_candidate(self):
        p=replace(self.protocol,skip_record_at=frozenset({2}))
        t=simulate('persistent',p)
        self.assertEqual(t.presentation[2].sources,self.ABC)
        self.assertEqual(t.report,self.AB)

    def test_15_emission_block_is_not_a_test_of_experience_by_itself(self):
        p=replace(self.protocol,suppress_emission=True)
        for kind in KINDS:
            t=simulate(kind,p)
            self.assertIsNone(t.report)
            self.assertEqual(t.source_profile(),self.traces[kind].source_profile())

    def test_16_later_presentation_uses_new_tokens_not_old_phenomenal_identity(self):
        t=self.traces['persistent']
        earlier=t.presentation[0].occurrence_tokens()
        later=t.presentation[1].occurrence_tokens()
        self.assertFalse(earlier&later)
        self.assertTrue(t.presentation[0].sources.issubset(t.presentation[1].sources))

    def test_17_source_recurrence_is_not_token_reuse(self):
        t=self.traces['late_replay']
        self.assertFalse(t.presentation[0].occurrence_tokens()&t.presentation[3].occurrence_tokens())
        self.assertTrue(t.presentation[0].sources.issubset(t.presentation[3].sources))

    def test_18_duplicate_runs_have_distinct_occurrence_tokens(self):
        a=simulate('persistent',self.protocol,run='first')
        b=simulate('persistent',self.protocol,run='second')
        self.assertEqual(a.source_profile(),b.source_profile())
        self.assertFalse(a.presentation[2].occurrence_tokens()&b.presentation[2].occurrence_tokens())

    def test_19_passive_source_renaming_transports_predictions(self):
        mapping={e.key:'new/'+e.key for row in self.protocol.inputs for e in row}
        p=passive_relabel(self.protocol,mapping)
        for kind in KINDS:
            t=simulate(kind,p)
            expected=tuple(frozenset(mapping[s] for s in support) for support in self.traces[kind].source_profile())
            self.assertEqual(t.source_profile(),expected)

    def test_20_repeated_quality_labels_do_not_identify_source_occurrences(self):
        p=Protocol(((InputEvent('a1','A'),),(InputEvent('a2','A'),)),2)
        t=simulate('persistent',p)
        self.assertEqual(len(t.report),2)
        self.assertEqual(label_report(t.report,p),frozenset({'A'}))

    def test_21_reused_source_occurrence_rejected(self):
        with self.assertRaises(ValueError):
            Protocol(((InputEvent('a','A'),),(InputEvent('a','A'),)),2)

    def test_22_simultaneous_input_cannot_separate_early_presentation_modes(self):
        p=Protocol(((InputEvent('a','A'),InputEvent('b','B'),InputEvent('c','C')),),1)
        traces=[simulate(k,p) for k in KINDS]
        self.assertEqual(len({t.presentation[0].sources for t in traces}),1)
        self.assertEqual(len(minimal_temporal_designs(traces)),0)
        # Persistent and replay are identical over this restricted protocol.

    def test_23_inconsistent_episode_observation_rejects_all_candidates(self):
        self.assertEqual(identify(self.traces.values(),{1:frozenset({'C@input'})}),())

    def test_24_no_observations_yields_no_spurious_selection(self):
        self.assertEqual(set(identify(self.traces.values(),{})),set(KINDS))
        ambiguous={1:frozenset({self.AB,frozenset({'B@input'})})}
        self.assertEqual(set(identify_uncertain(self.traces.values(),ambiguous)),set(KINDS))
        impossible={1:frozenset({frozenset({'C@input'})})}
        self.assertEqual(identify_uncertain(self.traces.values(),impossible),())

if __name__=='__main__':
    unittest.main(verbosity=2)
