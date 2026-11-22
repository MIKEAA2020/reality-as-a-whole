#!/usr/bin/env python3
import itertools
import unittest
from lewtas_fusion_nested_observation_gate import supports,states,quantities,record,trace,target_initial_locals_persist_with_global,lower_gap


class FusionNestedTest(unittest.TestCase):
    def test_same_conserved_amount_types_and_subject_count(self):
        for mode in (0,1):
            f=quantities(supports('selected_fusion',mode));p=quantities(supports('private_copy',mode))
            self.assertEqual(f,p)
            self.assertEqual((f['total'],f['by_type']),(4,{'red':2,'blue':2}))
            self.assertEqual(f['subjects'],4 if mode==0 else 3)

    def test_subject_persistence_not_inferred_from_content_type(self):
        fusion=states('selected_fusion',[0,1,0]);private=states('private_copy',[0,1,0])
        a=frozenset('a');b=frozenset('b')
        self.assertFalse(target_initial_locals_persist_with_global(fusion[:2]))
        self.assertTrue(target_initial_locals_persist_with_global(private[:2]))
        self.assertNotEqual(fusion[0][a],fusion[2][a])
        self.assertNotEqual(fusion[0][b],fusion[2][b])
        self.assertEqual(private[0][a],private[1][a]);self.assertEqual(private[1][a],private[2][a])

    def test_all_short_public_records_equal(self):
        alphabet=list(itertools.product((0,1),repeat=3))
        for sequence in itertools.product(alphabet,repeat=3):
            self.assertEqual(trace('selected_fusion',sequence)[1],trace('private_copy',sequence)[1])

    def test_assay_bound_and_no_guarantee_without_quality(self):
        self.assertAlmostEqual(lower_gap(.1,.2),.7)
        self.assertLessEqual(lower_gap(.6,.4),0)
        with self.assertRaises(ValueError):lower_gap(-0.01,0.2)
        with self.assertRaises(ValueError):record(0,2,1)
        with self.assertRaises(ValueError):supports('unknown',1)


if __name__=='__main__':unittest.main()
