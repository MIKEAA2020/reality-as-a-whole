import unittest
from fractions import Fraction
from bakas_paper_consistency import run,star,mul,eye,add_scaled
class AuditTests(unittest.TestCase):
 def test_star(self):
  a=star();self.assertEqual(sum(sum(row) for row in a),10)
  self.assertTrue(all(not x for row in mul(a,a) for x in row))
 def test_product_and_inverse(self):
  a=star(); I=eye(14); self.assertEqual(mul(add_scaled(I,a,Fraction(-1,10)),add_scaled(I,a,Fraction(1,10))),I)
  r=run();self.assertEqual(r['literal_product_target_receive_before_positive_normalization'],-1.0)
  self.assertEqual(r['directed_resolvent_target_receive_before_positive_normalization'],3.0)
 def test_degrees_of_freedom(self):
  r=run(); self.assertEqual(r['within_sensor_expected_residual_df'],176397);self.assertEqual(r['across_sensor_expected_residual_df'],2469597);self.assertEqual(r['combined_feature_counts_times_trials'],2646000)
 def test_effect_size_conventions(self):
  r=run();self.assertAlmostEqual(r['conventional_f_from_reported_within_F_df'],0.00619053,places=7);self.assertAlmostEqual(r['paired_dz_if_N_is_number_of_pairs'],0.003805,places=6)
if __name__=='__main__':unittest.main()
