import unittest
from fractions import Fraction as F
from direct_stimulation_affect_audit import ROWS,audit,oracle

class DirectStimulationTests(unittest.TestCase):
 def test_supplement_counts_and_direct_formula(self):
  r=audit();self.assertEqual((r['paired_rows'],r['cells'],r['affected_rows'],r['discrepant_cells']),(15,30,4,8))
  self.assertEqual({x['printed_over_formula'] for x in r['differences']},{'2','5','6'})
  rows={(x['subject'],x['frequency_hz'],x['duration_seconds'],x['printed_trial_uC']):x['formula_trial_uC'] for x in r['differences']}
  self.assertEqual(rows[('10',10,5,'250')],'50');self.assertEqual(rows[('12',2,1,'14.4')],'12/5')
 def test_duplicate_settings(self):
  r=audit()['different_displayed_trial_charge_for_same_listed_settings']
  self.assertEqual(len(r),2)
  self.assertEqual({(x['subject'],x['frequency_hz'],tuple(x['different_printed_trial_uC'])) for x in r}, {('10',10,('250','50')),('12',5,('36','6'))})
 def test_two_level_oracle_known_result(self):
  r=oracle();self.assertEqual(r['assignments_examined'],16);self.assertEqual(F(r['minimum_mean_squared_error']),F(125,2))
  self.assertEqual(F(r['minimum_mean_absolute_error']),F(15,2));self.assertEqual(F(r['minimum_max_absolute_error']),10)
 def test_two_values_fit_and_permutation_invariant(self):
  self.assertEqual(F(oracle((1,1,3,3))['minimum_mean_squared_error']),0)
  self.assertEqual(oracle((60,10,40,20))['minimum_mean_squared_error'],oracle()['minimum_mean_squared_error'])
 def test_reject_empty(self):
  with self.assertRaises(ValueError):oracle(())
if __name__=='__main__':unittest.main()
