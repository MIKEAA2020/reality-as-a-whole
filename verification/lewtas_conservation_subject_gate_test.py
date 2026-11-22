#!/usr/bin/env python3
import unittest
from lewtas_conservation_subject_gate import Scenario, audit


class ConservationGateTest(unittest.TestCase):
    def test_same_inventory_can_have_one_or_two_subjects(self):
        a,b=frozenset({'a'}),frozenset({'b'});ab=a|b
        fused=audit(Scenario(ab,(ab,),'red-yellow',('same record',)))
        split=audit(Scenario(ab,(a,b),'red-yellow',('same record',)))
        self.assertEqual(fused['distinct_ingredient_mass'],split['distinct_ingredient_mass'])
        self.assertEqual(fused['sum_of_support_masses'],split['sum_of_support_masses'])
        self.assertEqual((fused['represented_subjects'],split['represented_subjects']),(1,2))
        self.assertEqual(fused['record'],split['record'])

    def test_nested_distinguishes_two_amount_definitions(self):
        a,b=frozenset({'a'}),frozenset({'b'});ab=a|b
        nested=audit(Scenario(ab,(a,b,ab),'mixed',()))
        self.assertEqual(nested['distinct_ingredient_mass'],2)
        self.assertEqual(nested['sum_of_support_masses'],4)
        self.assertFalse(nested['exclusive_ownership'])

    def test_quality_not_chosen_by_accounting(self):
        ab=frozenset({'a','b'})
        x=audit(Scenario(ab,(ab,),'orange',('same record',)))
        y=audit(Scenario(ab,(ab,),'violet',('same record',)))
        self.assertEqual(x['distinct_ingredient_mass'],y['distinct_ingredient_mass'])
        self.assertNotEqual(x['quality'],y['quality'])

    def test_bad_support_rejected(self):
        with self.assertRaises(ValueError):audit(Scenario(frozenset({'a','b'}),(frozenset({'a'}),),'',()))
        with self.assertRaises(ValueError):audit(Scenario(frozenset({'a'}),(frozenset({'b'}),),'',()))


if __name__=='__main__':unittest.main()
