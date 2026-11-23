"""Conditional normalized incidence and noncommuting-effect controls.

No mathematical normalization identifies a real subject, a phenomenal value,
a physical incidence measure, or the constitution of zero.
"""
from fractions import Fraction as F
from math import sqrt
import unittest


def incidence(n,subjects):
    # (support, positive actual-incidence weight); candidate physical inputs.
    m=[sum(a for support,a in subjects if i in support) for i in range(n)]
    shares=[[a/m[i] if i in support and m[i] else F(0)
             for i in range(n)] for support,a in subjects]
    return m,shares


def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(t,a): return [[t*x for x in row] for row in a]
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def trace(a): return sum(a[i][i] for i in range(len(a)))


class SubjectIncidenceFrameTests(unittest.TestCase):
    def setUp(self):
        self.subjects=[({0,1,2},F(1)),({1,2,3},F(1))]
        self.m,self.shares=incidence(4,self.subjects)
        self.h=[F(-1,2),F(1,2),F(0),F(0)]

    def test_normalization_derived_from_equal_response_and_local_accounting(self):
        self.assertEqual(self.m,[1,2,2,1])
        self.assertEqual(self.shares,[[1,F(1,2),F(1,2),0],
                                      [0,F(1,2),F(1,2),1]])
        self.assertEqual([sum(s[i] for s in self.shares) for i in range(4)],[1]*4)
        self.assertEqual([sum(s[i]*h for i,h in enumerate(self.h)) for s in self.shares],
                         [F(-1,4),F(1,4)])

    def test_weighted_individual_response_is_unique_when_equal(self):
        subjects=[({0,1},F(2)),({1,2},F(1))]
        m,shares=incidence(3,subjects)
        self.assertEqual(m,[2,3,1])
        self.assertEqual(shares[0][1],F(2,3))
        self.assertEqual(shares[1][1],F(1,3))
        # Each incidence is assigned h/m; each weighted contribution is a_s*h/m.
        h=F(6)
        individual=h/m[1]
        self.assertEqual(sum(a*individual for support,a in subjects if 1 in support),h)
        self.assertEqual(individual,2)

    def test_coverage_gap_remains_a_boundary_term(self):
        subjects=[({0,1},F(1))]
        m,shares=incidence(4,subjects)
        h=[F(0),F(-1),F(1),F(0)]
        self.assertEqual(sum(h),0)
        covered=sum(shares[0][i]*h[i] for i in range(4))
        self.assertEqual(covered,-1)
        self.assertEqual(covered,-sum(h[i] for i in range(4) if not m[i]))

    def test_non_equal_phenomenal_response_not_fixed_by_efficiency(self):
        # w1=2,w2=1, h=6: (2,2) and (3,0) both respect 2v1+v2=6.
        self.assertEqual(2*F(2)+F(2),6)
        self.assertEqual(2*F(3)+F(0),6)

    def test_conserved_sphere_weights_reproduce_normalized_frame_povm(self):
        from verification.zero_sphere_conservation_born_bridge_test import bridge, ray
        from verification.zero_sphere_singlet_fixed_records_test import TRINE, effects
        result,q,_ = bridge([ray(0),ray(2),ray(1),ray(0,1),ray(0,-1)])
        weights=[q[i] for i in result['triple']]
        self.assertEqual(weights,[F(1,3)]*3)
        S=[[0j,0j],[0j,0j]]
        for weight,n in zip(weights,TRINE): S=add(S,scale(float(weight),effects(n)))
        for i in range(2):
            for j in range(2): self.assertAlmostEqual(S[i][j].real,.5 if i==j else 0)
        # Since S=I/2, S^(-1/2)=√2 I; E_i=2q_i Π_i.
        total=[[0j,0j],[0j,0j]]
        for weight,n in zip(weights,TRINE): total=add(total,scale(2*float(weight),effects(n)))
        for i in range(2):
            for j in range(2): self.assertAlmostEqual(total[i][j].real,1 if i==j else 0)

    def test_quantum_jordan_product_not_a_probability_effect(self):
        px=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
        pz=[[F(1),F(0)],[F(0),F(0)]]
        jordan=scale(F(1,2),add(mm(px,pz),mm(pz,px)))
        self.assertEqual(jordan,[[F(1,2),F(1,4)],[F(1,4),0]])
        a=1+sqrt(2); norm=1+a*a
        v=(1/sqrt(norm),-a/sqrt(norm))
        value=sum(v[i]*float(jordan[i][j])*v[j] for i in range(2) for j in range(2))
        self.assertAlmostEqual(value,(1-sqrt(2))/4)
        self.assertLess(value,0)

    def test_luders_incidence_measurement_can_disturb_original_signed_value(self):
        plus=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
        minus=[[F(1,2),F(-1,2)],[F(-1,2),F(1,2)]]
        Z=[[F(1),F(0)],[F(0),F(-1)]]
        rho=[[F(1),F(0)],[F(0),F(0)]]
        disturbed=add(mm(mm(plus,Z),plus),mm(mm(minus,Z),minus))
        self.assertEqual(disturbed,[[0,0],[0,0]])
        self.assertEqual(trace(mm(rho,Z)),1)
        self.assertEqual(trace(mm(rho,disturbed)),0)

    def test_two_nonorthogonal_rank_one_supports_cannot_both_cover_identity(self):
        pz=[[F(1),F(0)],[F(0),F(0)]]
        px=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
        # E1=a Pz, E2=b Px: off-diagonal b/2 must be 0, but the
        # (1,1) entry b/2 must be 1. No coefficients satisfy both.
        self.assertEqual(px[0][1],px[1][1])
        self.assertEqual(pz[0][1],0)
        self.assertEqual(pz[1][1],0)

    def test_canonical_noncommuting_normalization_changes_support(self):
        pz=[[1.,0.],[0.,0.]]
        px=[[.5,.5],[.5,.5]]
        S=add(pz,px)
        d=sqrt(.5)
        A=add(S,scale(d,eye(2)))
        determinant=A[0][0]*A[1][1]-A[0][1]*A[1][0]
        inverse=[[A[1][1]/determinant,-A[0][1]/determinant],
                 [-A[1][0]/determinant,A[0][0]/determinant]]
        B=scale(sqrt(2+2*d),inverse) # S^(-1/2) for this positive S
        ez=mm(mm(B,pz),B)
        ex=mm(mm(B,px),B)
        total=add(ez,ex)
        for i in range(2):
            for j in range(2): self.assertAlmostEqual(total[i][j],1 if i==j else 0)
        self.assertGreater(ez[1][1],0) # support is no longer inside range(Pz)

    def test_nonorthogonal_trine_can_be_supported_and_normalized(self):
        # Represent trine Bloch vectors in XZ plane; sum of projectors = 3I/2.
        # n0=(0,0,1), n1=(√3/2,0,-1/2), n2=(−√3/2,0,-1/2).
        p0=[[1,0],[0,0]]
        p1=[[.25,sqrt(3)/4],[sqrt(3)/4,.75]]
        p2=[[.25,-sqrt(3)/4],[-sqrt(3)/4,.75]]
        total=scale(2/3,add(add(p0,p1),p2))
        for i in range(2):
            for j in range(2): self.assertAlmostEqual(total[i][j],1 if i==j else 0)


if __name__ == '__main__': unittest.main()
