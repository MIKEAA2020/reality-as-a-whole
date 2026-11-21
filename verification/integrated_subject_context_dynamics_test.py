import unittest
from fractions import Fraction as F
from coupled_subject_boundary_gate import STATES, stationary
from integrated_subject_horizon_audit import kernel
from integrated_subject_context_dynamics import q,projected_row,maximal_discrepancy,stationary_stats

class ContextDynamicsTest(unittest.TestCase):
 def test_witness_same_left_physical_state(self):
  k=kernel(F(1,4));a=(-1,-1,-1,-1);b=(-1,-1,1,-1)
  self.assertEqual(a[:2],b[:2]); self.assertEqual(q(a,0),q(b,0))
  self.assertEqual(projected_row(k,a,'left_q')[(1,)],F(5,48))
  self.assertEqual(projected_row(k,b,'left_q')[(1,)],F(17,112))
  self.assertEqual(F(17,112)-F(5,48),F(1,21))
 def test_exact_controls_and_relational_repair(self):
  k0=kernel(F(0));k=kernel(F(1,4))
  for name in ('pair_state','left_q','left_right_q','edge_qs'):
   self.assertEqual(maximal_discrepancy(k0,name)[0],0)
  self.assertEqual(maximal_discrepancy(k,'pair_state')[0],F(1,21))
  self.assertEqual(maximal_discrepancy(k,'left_q')[0],F(1,21))
  self.assertEqual(maximal_discrepancy(k,'left_middle_q')[0],F(5,42))
  self.assertEqual(maximal_discrepancy(k,'left_right_q')[0],F(2,21))
  self.assertEqual(maximal_discrepancy(k,'edge_qs')[0],0)
 def test_global_flip_symmetry(self):
  k=kernel(F(1,4))
  for s in STATES:
   neg=tuple(-x for x in s)
   for u,p in k[s].items():self.assertEqual(k[neg][tuple(-x for x in u)],p)
 def test_stationary_three_point_independent_dense_product(self):
  # Dense matrix multiplication after initial filtering, rather than the
  # production routine's nested transition enumeration.
  k=kernel(F(1,4)); pi=stationary(F(1,4),(None,)*4)
  K=[[k[x].get(y,F(0)) for y in STATES] for x in STATES]
  advance=lambda vec:[sum(vec[i]*K[i][j] for i in range(16)) for j in range(16)]
  _,hist=stationary_stats(F(1,4))
  for a in (0,1):
   v=advance([pi[s] if q(s,0)==a else F(0) for s in STATES])
   for b in (0,1):
    filt=[v[i] if q(s,0)==b else F(0) for i,s in enumerate(STATES)]
    denom=sum(filt);z=advance(filt)
    calc=sum(z[i] for i,s in enumerate(STATES) if q(s,0)==1)/denom
    self.assertEqual(calc,F(hist[f'previous={a},current={b}']))
  self.assertEqual(F(hist['previous=1,current=0'])-F(hist['previous=0,current=0']),F(12,2419))
  self.assertEqual(F(hist['previous=1,current=1'])-F(hist['previous=0,current=1']),F(20,8733))
 def test_invalid_projection(self):
  with self.assertRaises(ValueError):projected_row(kernel(F(1,4)),STATES[0],'bad')
if __name__=='__main__':unittest.main()
