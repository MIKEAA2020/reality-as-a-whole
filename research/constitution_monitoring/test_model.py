import unittest
from model import *


class MonitoringAuditTests(unittest.TestCase):
    def setUp(self):
        self.baseline=filter_evidence(CANDIDATES,baseline_evidence())
        self.s01=physical(Intervention(0,m=1))
        self.s10=physical(Intervention(1,m=0))

    def test_01_sixteen_binary_candidates(self):
        self.assertEqual(len(set(CANDIDATES)),16)

    def test_02_thirty_six_interventions(self):
        self.assertEqual(len(set(interventions())),36)

    def test_03_all_public_signatures_identical(self):
        signatures={public_signature(f,interventions()) for f in CANDIDATES}
        self.assertEqual(len(signatures),1)

    def test_04_default_monitor_copies_source(self):
        for x in (0,1):
            s=physical(Intervention(x))
            self.assertEqual((s.c,s.m,s.r),(x,x,x))

    def test_05_monitor_intervention_preserves_source_and_report(self):
        for x in (0,1):
            for m in (0,1):
                s=physical(Intervention(x,m=m))
                self.assertEqual((s.c,s.r),(x,x))
                self.assertEqual(s.m,m)

    def test_06_source_intervention_changes_default_monitor_and_report(self):
        s=physical(Intervention(0,c=1))
        self.assertEqual((s.c,s.m,s.r),(1,1,1))

    def test_07_monitor_clamp_cuts_copy_edge(self):
        self.assertEqual((self.s01.c,self.s01.m,self.s01.r),(0,1,0))

    def test_08_baseline_leaves_four_candidates(self):
        self.assertEqual(set(self.baseline),{SOURCE,MONITOR,CONJUNCTION,DISJUNCTION})

    def test_09_baseline_does_not_select_source(self):
        self.assertNotEqual(self.baseline,(SOURCE,))

    def test_10_one_discordant_contrast_leaves_two(self):
        result=filter_evidence(self.baseline,((self.s01,frozenset({0})),))
        self.assertEqual(set(result),{SOURCE,CONJUNCTION})

    def test_11_other_discordant_contrast_leaves_two(self):
        result=filter_evidence(self.baseline,((self.s10,frozenset({1})),))
        self.assertEqual(set(result),{SOURCE,DISJUNCTION})

    def test_12_both_contrasts_select_source_conditionally(self):
        evidence=((self.s01,frozenset({0})),(self.s10,frozenset({1})))
        self.assertEqual(filter_evidence(self.baseline,evidence),(SOURCE,))

    def test_13_opposite_evidence_selects_monitor(self):
        evidence=((self.s01,frozenset({1})),(self.s10,frozenset({0})))
        self.assertEqual(filter_evidence(self.baseline,evidence),(MONITOR,))

    def test_14_zero_discordants_select_conjunction(self):
        evidence=((self.s01,frozenset({0})),(self.s10,frozenset({0})))
        self.assertEqual(filter_evidence(self.baseline,evidence),(CONJUNCTION,))

    def test_15_one_discordants_select_disjunction(self):
        evidence=((self.s01,frozenset({1})),(self.s10,frozenset({1})))
        self.assertEqual(filter_evidence(self.baseline,evidence),(DISJUNCTION,))

    def test_16_exact_minimal_design(self):
        self.assertEqual(minimal_contrast_designs(self.baseline),(((0,1),(1,0)),))

    def test_17_all_candidates_need_all_four_states(self):
        self.assertEqual(minimal_contrast_designs(CANDIDATES),(((0,0),(0,1),(1,0),(1,1)),))

    def test_18_assuming_report_faithfulness_selects_source(self):
        evidence=tuple((physical(p),frozenset({physical(p).r})) for p in interventions() if p.emit)
        self.assertEqual(filter_evidence(CANDIDATES,evidence),(SOURCE,))
        # This is a consequence of SUPPLIED E=R, not independent experience data.

    def test_19_no_report_does_not_select_an_annotation(self):
        protocols=tuple(p for p in interventions() if not p.emit)
        self.assertTrue(all(s.r is None for s in public_signature(SOURCE,protocols)))
        self.assertEqual(len({public_signature(f,protocols) for f in CANDIDATES}),1)

    def test_20_ambiguous_evidence_preserves_candidates(self):
        evidence=((self.s01,frozenset({0,1})),(self.s10,frozenset({0,1})))
        self.assertEqual(filter_evidence(self.baseline,evidence),self.baseline)

    def test_21_inconsistent_evidence_rejects_all(self):
        s=physical(Intervention(0))
        self.assertEqual(filter_evidence(self.baseline,((s,frozenset({1})),)),())

    def test_22_coordinate_support_is_target_relative(self):
        self.assertEqual(essential_coordinates(SOURCE),frozenset({'C'}))
        self.assertEqual(essential_coordinates(MONITOR),frozenset({'M'}))
        self.assertEqual(essential_coordinates(CONJUNCTION),frozenset({'C','M'}))
        self.assertEqual(essential_coordinates(DISJUNCTION),frozenset({'C','M'}))
        self.assertEqual(essential_coordinates(Candidate((0,0,0,0))),frozenset())

    def test_23_restricted_interventions_hide_off_diagonal_differences(self):
        diagonal=tuple(physical(Intervention(x,c=c)) for x in (0,1) for c in (None,0,1))
        self.assertEqual(len({tuple(f.evaluate(s) for s in diagonal) for f in self.baseline}),1)

    def test_24_repeated_simulation_does_not_add_information(self):
        evidence=baseline_evidence()*100
        self.assertEqual(filter_evidence(CANDIDATES,evidence),self.baseline)
        with self.assertRaises(ValueError):
            Candidate((0,1))
        with self.assertRaises(ValueError):
            Intervention(3)

if __name__=='__main__':
    unittest.main(verbosity=2)
