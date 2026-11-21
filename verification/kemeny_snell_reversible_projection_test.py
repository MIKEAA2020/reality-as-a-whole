import hashlib
import unittest
from fractions import Fraction as F
from pathlib import Path
from kemeny_snell_reversible_projection import mm, powm, regular_power, stationary_projected, book_example, run

class KemenySnellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=run()
    def test_supplied_pdf_hash(self):
        source=Path('sources/uploads/Kemeny_Snell_Finite_Markov_Chains.pdf')
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),'8380bc85e6740a4baac5ad811fc0ad81db625e430511d300e856869d08350537')
    def test_model_assumptions(self):
        self.assertTrue(all(self.r['assumptions'].values()))
    def test_weak_lumpability_contrasts(self):
        p=self.r['projections']
        for key in ('pair_state','left_q','left_middle_q','left_right_q','any_mismatch'):
            self.assertEqual(p[key]['homogeneous_markov_for_some_initial_distribution'],'no')
            self.assertGreater(F(p[key]['stationary_Q2_vs_actual_two_step']['max_block_gap']),0)
        self.assertEqual(p['edge_qs']['homogeneous_markov_for_some_initial_distribution'],'yes')
        self.assertEqual(p['edge_qs']['stationary_Q2_vs_actual_two_step']['max_block_gap'],'0')
    def test_two_step_witness(self):
        z=self.r['projections']['left_q']['stationary_Q2_vs_actual_two_step']
        self.assertEqual(abs(F(z['actual_two_step'])-F(z['square_one_step'])),F(5,2352))
    def test_book_counterexample(self):
        e=book_example()
        self.assertEqual(e['regular_power'],2)
        self.assertFalse(e['reversible'])
        self.assertTrue(e['stationary_block_conditionals_preserved'])
        self.assertEqual(e['stationary_two_step']['max_block_gap'],'0')
    def test_matrix_multiplication_and_power(self):
        p=[[F(1,2),F(1,2)],[F(1,4),F(3,4)]]
        self.assertEqual(mm(p,p),powm(p,2))
        self.assertEqual(regular_power(p),1)
        self.assertEqual(stationary_projected(p,[F(1,3),F(2,3)],[0,1])['max_block_gap'],'0')
if __name__=='__main__':unittest.main()
