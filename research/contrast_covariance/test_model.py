import unittest
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from model import (ContrastGraph, cycle, admissible_maps, report_distribution,
                   total_variation, optimal_binary_accuracy, content_step, joint_step,
                   feedback_step, moving_readout, ring_step, RoleCertificate,
                   occurrence_key, occurrence_count, shared_step)


class ContrastCovarianceTests(unittest.TestCase):
    def setUp(self):
        self.p = cycle(range(4))
        self.e = cycle('ABCD')  # Synthetic first-person-side constraints, not human measurements.
        self.role = RoleCertificate((frozenset({'a0'}), frozenset({'a1'})),
                                    (0, 1, 2), ('site0', 'site1'))

    def test_01_unanchored_correspondence_has_eight_maps(self):
        self.assertEqual(len(admissible_maps(self.p, self.e)), 8)

    def test_02_one_calibration_leaves_reflection_ambiguity(self):
        self.assertEqual(len(admissible_maps(self.p, self.e, ((0, 'A'),))), 2)

    def test_03_two_adjacent_calibrations_select_one(self):
        self.assertEqual(len(admissible_maps(self.p, self.e, ((0, 'A'), (1, 'B')))), 1)

    def test_04_two_opposite_calibrations_do_not_select_orientation(self):
        self.assertEqual(len(admissible_maps(self.p, self.e, ((0, 'A'), (2, 'C')))), 2)

    def test_05_calibration_can_refute_model(self):
        self.assertEqual(admissible_maps(self.p, self.e, ((0, 'A'), (1, 'C'))), [])

    def test_06_nonisomorphic_phenomenal_graph_refutes_exact_bridge(self):
        path = ContrastGraph(tuple('ABCD'), frozenset(frozenset(e) for e in ('AB','BC','CD')))
        self.assertEqual(admissible_maps(self.p, path), [])

    def test_07_all_candidate_maps_preserve_shortest_paths(self):
        for mapping in admissible_maps(self.p, self.e):
            for a, b in product(range(4), repeat=2):
                self.assertEqual(self.p.distance(a,b), self.e.distance(mapping[a],mapping[b]))

    def test_08_held_out_distance_from_two_calibrations(self):
        mapping, = admissible_maps(self.p,self.e,((0,'A'),(1,'B')))
        self.assertEqual(mapping[2], 'C')
        self.assertEqual(mapping[3], 'D')
        self.assertEqual(self.p.distance(0,2), 2)

    def test_09_physical_relabeling_transports_maps(self):
        rename = {i: 10+i for i in range(4)}
        new = self.p.renamed(rename)
        self.assertEqual(len(admissible_maps(new,self.e)),8)
        for m in admissible_maps(self.p,self.e):
            self.assertIn({rename[k]:v for k,v in m.items()},admissible_maps(new,self.e))

    def test_10_phenomenal_labels_do_not_pick_unique_absolute_quality(self):
        new = self.e.renamed(dict(zip('ABCD','WXYZ')))
        self.assertEqual(len(admissible_maps(self.p,new)),8)

    def test_11_channel_normalization_and_positivity(self):
        for q, eta in product(range(4), (F(0),F(1,4),F(1,2),F(1))):
            d=report_distribution(q,eta)
            self.assertEqual(sum(d.values()),1)
            self.assertTrue(all(v>=0 for v in d.values()))

    def test_12_report_distinguishability_exact_formula(self):
        for eta in (F(0),F(1,4),F(1,2),F(1)):
            for a,b in product(range(4),repeat=2):
                expected = F(0) if a==b else 1-eta
                self.assertEqual(total_variation(report_distribution(a,eta),report_distribution(b,eta)),expected)

    def test_13_report_accuracy_decreases_without_changing_content_graph(self):
        values=[]
        for eta in (F(0),F(1,4),F(1,2),F(1)):
            values.append(optimal_binary_accuracy(report_distribution(0,eta),report_distribution(1,eta)))
            self.assertEqual(self.p.distance(0,1),1)
        self.assertEqual(values,[F(1),F(7,8),F(3,4),F(1,2)])

    def test_14_no_feedback_commuting_projection(self):
        for q,eta,action in product(range(4),(F(0),F(1,2),F(1)),(-1,0,1)):
            self.assertEqual(joint_step((q,eta),action)[0],content_step(q,action))

    def test_15_longer_interventions_preserve_nuisance_independence(self):
        for initial in range(4):
            for actions in product((-1,0,1),repeat=5):
                a,b=(initial,F(0)),(initial,F(1))
                for action in actions:
                    a,b=joint_step(a,action),joint_step(b,action)
                    self.assertEqual(a[0],b[0])

    def test_16_feedback_countermodel_breaks_nuisance_assumption(self):
        self.assertNotEqual(feedback_step((0,0),0)[0],feedback_step((0,1),0)[0])

    def test_17_noise_can_erase_all_report_information_not_intrinsic_identification(self):
        self.assertEqual(report_distribution(0,1),report_distribution(2,1))
        self.assertNotEqual(0,2)  # A model distinction, not a direct measurement of experience.

    def test_18_same_certificate_described_twice_adds_no_role(self):
        self.assertEqual(occurrence_count([self.role,self.role]),1)

    def test_19_emulation_description_alone_adds_no_role(self):
        self.assertEqual(occurrence_count([self.role,replace(self.role,layer='host/emulator/target')]),1)

    def test_20_separate_duplicate_preserves_two_supplied_occurrences(self):
        duplicate=self.role.transported(lambda e:'copy/'+e)
        self.assertEqual(occurrence_count([self.role,duplicate]),2)

    def test_21_redescription_requires_transported_provenance_not_same_names(self):
        renamed=self.role.transported(lambda e:'new/'+e)
        provenance={'new/'+e:e for block in self.role.anchors for e in block}
        self.assertEqual(occurrence_key(renamed,provenance),occurrence_key(self.role))

    def test_22_invisible_duplicate_changes_total_list_not_local_profile(self):
        duplicate=self.role.transported(lambda e:'hidden/'+e)
        self.assertEqual(self.role.values,duplicate.values)
        self.assertEqual(occurrence_count([self.role,duplicate]),2)

    def test_23_same_values_do_not_identify_distinct_event_anchors(self):
        duplicate=self.role.transported(lambda e:'separate/'+e)
        self.assertNotEqual(occurrence_key(self.role),occurrence_key(duplicate))

    def test_24_moving_storage_transports_content_without_changing_readout(self):
        for storage in product(range(4),repeat=3):
            current=storage
            for time in range(10):
                self.assertEqual(moving_readout(current,time),storage[0])
                current=ring_step(current)

    def test_25_shared_control_preserves_distinct_supplied_roles(self):
        second=self.role.transported(lambda e:'sibling/'+e)
        for x,y,c in product(range(4),range(4),(0,1)):
            self.assertEqual(shared_step(x,y,c)[:2],((x+c)%4,(y+c)%4))
        self.assertEqual(occurrence_count([self.role,second]),2)

    def test_26_split_continuation_not_equivalence(self):
        links={('p','a'),('p','b')}
        self.assertNotIn(('a','b'),links)
        # Equivalence closure WOULD identify a and b; do not use it as continuation.
        eq={('p','p'),('a','a'),('b','b')} | links | {(b,a) for a,b in links}
        for _ in range(3):
            eq |= {(a,d) for a,b in eq for c,d in eq if b==c}
        self.assertIn(('a','b'),eq)

    def test_27_temporal_sampling_changes_accessible_graph(self):
        # Endpoints of two primitive +/-1 moves have same parity; full cycle lost.
        two_step={((q+a+b)%4) for a,b in product((-1,1),repeat=2) for q in (0,)}
        self.assertEqual(two_step,{0,2})
        self.assertEqual(len(self.p.vertices),4)

    def test_28_grain_is_explicit_not_silently_invariant(self):
        grouped=RoleCertificate((frozenset({'a0','a1'}),),(0,2),('joint',))
        self.assertNotEqual(occurrence_key(grouped),occurrence_key(self.role))

    def test_29_occurrence_reuse_is_rejected(self):
        with self.assertRaises(ValueError):
            RoleCertificate((frozenset({'e'}),frozenset({'e'})),(0,1,2),('s','s'))

    def test_30_noninjective_passive_transport_is_rejected(self):
        with self.assertRaises(ValueError):
            self.role.transported(lambda e:'same')


if __name__=='__main__':
    unittest.main(verbosity=2)
