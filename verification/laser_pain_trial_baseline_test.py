import tempfile
import unittest
from pathlib import Path
from laser_pain_trial_baseline import audit

class LaserReadinessTests(unittest.TestCase):
    def run_fixture(self,contents):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.csv';p.write_text(contents);return audit(p,verify=False)
    def test_field_diagnostics_and_suffix(self):
        x=self.run_fixture('ID,Trial_Num,laser_power,Painrating\n1,1,2.5,3.5\n1,2,0,0\n2,1,2,NaN\n2,2,3,4\n')
        self.assertEqual(x['rows'],4);self.assertEqual(x['distinct_ids'],2)
        self.assertEqual(x['field_flags']['fractional_rating'],1)
        self.assertEqual(x['field_flags']['nonfinite_rating'],1)
        self.assertEqual(x['field_flags']['zero_energy'],1)
        self.assertEqual(x['zero_energy_ids_with_suffix_only'],1)
        self.assertTrue(x['score_status'].startswith('suppressed'))
    def test_nonsuffix(self):
        x=self.run_fixture('ID,Trial_Num,laser_power,Painrating\n1,1,0,0\n1,2,3,4\n')
        self.assertEqual(x['zero_energy_ids_with_suffix_only'],0)
    def test_duplicate_fails(self):
        with self.assertRaises(ValueError):self.run_fixture('ID,Trial_Num,laser_power,Painrating\n1,1,2.5,3\n1,1,3,4\n')
    def test_bad_hash_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.csv';p.write_text('ID,Trial_Num,laser_power,Painrating\n')
            with self.assertRaises(ValueError):audit(p)
    def test_range_fails(self):
        with self.assertRaises(ValueError):self.run_fixture('ID,Trial_Num,laser_power,Painrating\n1,1,2,11\n')
if __name__=='__main__':unittest.main()
