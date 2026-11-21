import unittest
from fractions import Fraction as F
from coupled_subject_boundary_gate import STATES
from integrated_subject_horizon_audit import kernel
from chalmers_structural_alternatives import qs,outer,any_q,graph,max_discrepancy,run

class StructuralAlternativesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.k=kernel(F(1,4))
    def test_selected_counts(self):
        r=run()['graphs']
        self.assertEqual([(r[x]['vertices'],r[x]['edges']) for x in ('fine_spins','all_edges','outer_edges','any_mismatch')],[(16,32),(8,16),(4,4),(2,1)])
    def test_global_flip_does_not_change_edge_bits(self):
        for s in STATES:self.assertEqual(qs(s),qs(tuple(-x for x in s)))
    def test_discrepancies(self):
        self.assertEqual(max_discrepancy(self.k,qs),0)
        self.assertEqual(max_discrepancy(self.k,outer),F(2,21))
        self.assertEqual(max_discrepancy(self.k,any_q),F(5,24))
    def test_support_excludes_loops(self):
        for p in (qs,outer,any_q):
            _,edges,_=graph(self.k,p)
            self.assertTrue(all(len(e)==2 for e in edges))
    def test_constant_projection_trivially_lumpable(self):
        self.assertEqual(max_discrepancy(self.k,lambda s:0),0)
if __name__=='__main__':unittest.main()
