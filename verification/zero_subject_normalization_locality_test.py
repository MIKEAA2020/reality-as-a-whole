"""Locality and simultaneous-subject controls for incidence normalization.

These are finite quantum algebra checks, not evidence that qubits are subjects,
or a derivation of actual phenomenal values, quantum gravity, or global zero.
"""
from fractions import Fraction as F
from itertools import product
import unittest


def diag(vals):
    return [[v if i==j else F(0) for j in range(len(vals))]
            for i,v in enumerate(vals)]


def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(t,a): return [[t*x for x in row] for row in a]
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def trace(a): return sum(a[i][i] for i in range(len(a)))
def kron(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))]
            for i in range(len(a)*len(b))]
def expectation(rho,op): return trace(mm(rho,op))


I=diag([F(1),F(1)])
P0=diag([F(1),F(0)])
P1=diag([F(0),F(1)])
PA=kron(P0,I)
PB=kron(I,P0)
N=add(PA,PB)
# S^(-1/2) normalization in computational basis, including uncovered outcome.
EA=diag([F(1,2),F(1),F(0),F(0)])
EB=diag([F(1,2),F(0),F(1),F(0)])
EEMPTY=diag([F(0),F(0),F(0),F(1)])
RHO00=kron(P0,P0)
RHO01=kron(P0,P1)


class SubjectNormalizationLocalityTests(unittest.TestCase):
    def test_frame_effects_sum_to_one_and_track_covered_sector(self):
        self.assertEqual(add(add(EA,EB),EEMPTY),diag([F(1)]*4))
        self.assertEqual(add(EA,EB),diag([1,1,1,0]))
        self.assertEqual([expectation(rho,EA) for rho in (RHO00,RHO01)],
                         [F(1,2),F(1)])

    def test_remote_unitary_changes_frame_share_not_local_a_state(self):
        # B bit flip takes |00> to |01>; A's density operator remains P0.
        X=[[F(0),F(1)],[F(1),F(0)]]
        U=kron(I,X)
        self.assertEqual(mm(mm(U,RHO00),U),RHO01)
        self.assertEqual(expectation(RHO00,PA),1)
        self.assertEqual(expectation(RHO01,PA),1)
        self.assertNotEqual(expectation(RHO00,EA),expectation(RHO01,EA))

    def test_ea_is_not_an_a_local_observable(self):
        # Any A-local F⊗I has identical A=0 diagonal entries for B=0 and B=1.
        self.assertNotEqual(EA[0][0],EA[1][1])
        self.assertEqual(PA[0][0],PA[1][1])

    def test_frame_effect_fails_remote_unitary_invariance(self):
        X=[[F(0),F(1)],[F(1),F(0)]]
        U=kron(I,X)
        self.assertNotEqual(mm(mm(U,EA),U),EA)
        self.assertEqual(mm(mm(U,PA),U),PA)

    def test_local_subject_counts_can_both_be_one(self):
        self.assertEqual(expectation(RHO00,PA),1)
        self.assertEqual(expectation(RHO00,PB),1)
        self.assertEqual(expectation(RHO00,N),2)
        self.assertEqual(expectation(RHO01,N),1)
        # Count operators are not probabilities and need not be ≤1.

    def test_no_two_exclusive_locally_determined_effects_cover_all_states(self):
        # For diagonal local effects, f(a)+g(b)=1 for all a,b forces both
        # functions constant. Constants cannot realize the availability rule.
        # Equalities follow independently of the discrete grid below.
        grid=(F(0),F(1,2),F(1))
        solutions=[]
        for f0,f1,g0,g1 in product(grid,repeat=4):
            if all(f+g==1 for f in (f0,f1) for g in (g0,g1)):
                solutions.append((f0,f1,g0,g1))
        self.assertTrue(solutions)
        self.assertTrue(all(f0==f1 and g0==g1 for f0,f1,g0,g1 in solutions))

    def test_local_undercounting_povm_has_residual_outcome(self):
        # E_A=PA/2, E_B=PB/2; the leftover is positive, but nonzero
        # even in a state where exactly one candidate is present.
        ea=scale(F(1,2),PA); eb=scale(F(1,2),PB)
        empty=add(diag([F(1)]*4),scale(-1,add(ea,eb)))
        self.assertEqual(empty,diag([0,F(1,2),F(1,2),1]))
        self.assertEqual(expectation(RHO01,empty),F(1,2))

    def test_distinct_local_signed_values_need_not_be_normalized(self):
        va=PA
        vb=scale(-1,PB)
        q=add(va,vb)
        self.assertEqual(expectation(RHO00,va),1)
        self.assertEqual(expectation(RHO00,vb),-1)
        self.assertEqual(expectation(RHO00,q),0)
        self.assertEqual(expectation(RHO01,q),1)
        # This is a stipulated assignment; no physical-experiential identity follows.


if __name__ == '__main__': unittest.main()
