"""Join intrinsic five-ray conservation to the existing all-sector history.

The complement's q-weighted instrument, references and Hamiltonian are
stipulated. Conditional incidence and valence examples do not prove subjects,
phenomenal identity, spacetime locality or objective whole energy.
"""
from fractions import Fraction as F
import math
import unittest
import numpy as np
from verification.zero_sphere_conservation_born_bridge_test import bridge,ray
from verification.zero_energy_sphere_work_incidence_test import full_state,relative_read,i_r_m_table,X,I
from verification.zero_all_sector_sphere_clock_work_test import complement_state,weighted_table
from verification.zero_all_sector_branchwise_balance_test import U8,Q8
from verification.zero_relational_orientation_reference_test import with_reference,C1,C2,C3,L,S
from verification.zero_invariant_all_history_record_clock_test import (
    attach_memory,evolve,apply32,H,W,PPLUS,PMINUS,kron
)

q=np.array([1/8,2/5,19/40])
d=np.array([-1/5,1/2,-7/19])
rf=kron(U8,X) # R,W,T,F: U₀ X_F, fixes the reference singlet.
rfm=kron(rf,I)
q32=kron(Q8,I,I)


def table(v):
    # i=axis 6, R=axis 8, old target T=axis 10, F and new memory summed.
    return np.sum(abs(v)**2,axis=(0,1,2,3,4,5,7,9,11,12))


def q_from_vector_zero():
    # n_i=(x_i,sqrt(3)*y_i,0); multiply y row by 1/sqrt(3).
    a=[[F(1),F(1),F(1),F(1)],
       [F(1),F(1,2),F(-13,19),F(0)],
       [F(0),F(1,2),F(-8,19),F(0)]]
    for col in range(3):
        pivot=next(i for i in range(col,3) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        p=a[col][col];a[col]=[x/p for x in a[col]]
        for i in range(3):
            if i!=col:
                p=a[i][col];a[i]=[x-p*y for x,y in zip(a[i],a[col])]
    return [row[3] for row in a]


def signed_record(tab):
    # tab indexed i, r, t; sign r=+1,-1, t labels old target.
    return float(np.einsum('i,irt,r->',d,tab,np.array([1.,-1.])))


def signed_work(tab):
    # L=+1: J=r Z_T, where t=0,1 has Z_T=+1,-1.
    return float(np.einsum('i,irt,r,t->',d,tab,np.array([1.,-1.]),np.array([1.,-1.])))


class GeometryAllHistoryIncidenceBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original=(full_state(4),complement_state(4))
        cls.oldclock=[relative_read(v,4,labels=tuple(range(16))) for v in cls.original]
        cls.ref=[[attach_memory(with_reference(x)) for x in vs] for vs in cls.oldclock]

    def test_exact_geometry_unique_normalized_vector_balance_and_unequal_counting(self):
        rays=[ray(0),ray(1),ray(3),ray(0,1),ray(0,2)]
        result,weights,dots=bridge(rays)
        self.assertEqual(result['triple'],[0,1,4])
        axis=result['pair'][0]
        self.assertEqual([weights[i] for i in result['triple']],[F(1,8),F(2,5),F(19,40)])
        self.assertEqual([dots[axis][i] for i in result['triple']],[F(-1,5),F(1,2),F(-7,19)])
        self.assertEqual(q_from_vector_zero(),[F(1,8),F(2,5),F(19,40)])
        qq=q_from_vector_zero();dd=[F(-1,5),F(1,2),F(-7,19)]
        self.assertEqual(sum(a*b for a,b in zip(qq,dd)),0)
        self.assertEqual(sum(a*abs(b) for a,b in zip(qq,dd)),F(2,5))
        self.assertEqual(sum(a*b*b for a,b in zip(qq,dd)),F(161,950))
        self.assertEqual(sum(dd)/3,F(-13,570))
        # Unique q applies if the normalized incidence weights themselves
        # satisfy the assumed full vector-zero condition, not from zero alone.

    def test_extended_pairing_commutes_with_history_and_intertwines_clock(self):
        np.testing.assert_allclose(rfm@rfm,np.eye(32),atol=1e-14)
        np.testing.assert_allclose(rfm@H,H@rfm,atol=1e-14)
        np.testing.assert_allclose(kron(I,rfm)@W,W@rfm,atol=1e-14)
        np.testing.assert_allclose(rfm@q32@rfm,-q32,atol=1e-14)
        for c in (C1,C2,C3):
            op=kron(c,I)
            sign=1 if c is C1 else -1
            np.testing.assert_allclose(rfm@op@rfm,sign*op,atol=1e-14)
        for op in (L,S):
            a=kron(op,I);np.testing.assert_allclose(rfm@a,a@rfm,atol=1e-14)
        # The mirror flips two constraints but preserves their zero kernels.

    def test_every_old_clock_sector_and_new_phase_keeps_geometry_and_pairing(self):
        ds=d.reshape((1,1,1,1,1,1,3,1,1,1,1,1,1))
        for histories in self.ref:
            for v in histories:
                for theta in (0,math.pi/4,math.pi/2):
                    z=evolve(v,theta)
                    mass=np.linalg.norm(z)**2
                    self.assertAlmostEqual(mass,1/16,places=12)
                    p=table(z)
                    np.testing.assert_allclose(p.sum(axis=(1,2))/mass,q,atol=2e-13)
                    np.testing.assert_allclose(p[:,:,0],p[:,:,1],atol=2e-14)
                    self.assertAlmostEqual(signed_work(p),0,places=13)
                    self.assertAlmostEqual(np.dot(d,p.sum(axis=(1,2))),0,places=13)
                    self.assertLess(np.linalg.norm(apply32(q32,ds*z)),1e-12)
                    np.testing.assert_allclose(apply32(rfm,ds*z),ds*z,atol=2e-14)
                    for c in (C1,C2,C3):
                        self.assertLess(np.linalg.norm(apply32(kron(c,I),z)),1e-12)
        # Involution commutation proves the result for all θ; sampled θ and
        # all 16 old labels exercise the actual states and memory interaction.

    def test_geometric_record_and_work_candidates_disagree_on_actual_cells(self):
        for histories in self.ref:
            for v in histories:
                for theta in (0,math.pi/4,math.pi/2):
                    p=table(evolve(v,theta))
                    signs=np.array([1.,-1.])
                    # sign(d*r) and sign(d*j), with j=r*(1−2h), differ
                    # exactly at target h=1. All d_i are nonzero.
                    mismatch=0.
                    for i in range(3):
                        for r in range(2):
                            for t in range(2):
                                vr=np.sign(d[i])*signs[r]
                                vj=vr*signs[t]
                                if vr!=vj:mismatch+=p[i,r,t]
                    self.assertAlmostEqual(mismatch/p.sum(),.5,places=12)
                    self.assertAlmostEqual(signed_work(p),0,places=13)
        # The prior h-target coupling makes the contrast operationally
        # explicit if its joint interface is available; it does not prove
        # that either candidate is experienced.

    def test_new_clock_unselected_preserves_geometry_and_paired_work(self):
        for histories in self.ref:
            for v in histories:
                pieces=[apply32(p,v) for p in (PPLUS,PMINUS)]
                p=sum(table(x) for x in pieces)
                self.assertAlmostEqual(p.sum(),1/16,places=13)
                np.testing.assert_allclose(p.sum(axis=(1,2))/p.sum(),q,atol=1e-13)
                np.testing.assert_allclose(p[:,:,0],p[:,:,1],atol=1e-14)
                for x in pieces:np.testing.assert_allclose(apply32(rfm,x),x,atol=2e-14)

    def test_new_clock_unselected_has_distinct_nonzero_record_correlator(self):
        sector=[]
        for histories in self.ref:
            p=sum(table(apply32(proj,v)) for v in histories for proj in (PPLUS,PMINUS))
            sector.append(p)
        combined=(sector[0]+127*sector[1])/128
        self.assertAlmostEqual(signed_record(combined),-38157/1206500,places=12)
        self.assertAlmostEqual(signed_work(combined),0,places=12)
        np.testing.assert_allclose(combined.sum(axis=(1,2)),q,atol=1e-13)
        # The additional stationary clock is traced, not postselected.

    def test_geometric_zero_does_not_imply_zero_record_correlation(self):
        tables=[sum(i_r_m_table(vs) for _ in [0]) for vs in self.oldclock]
        # Code contribution of d*R averages to zero over all old clock labels;
        # complement is nonzero under its specified fixed-setting instrument.
        self.assertAlmostEqual(signed_record(tables[0]),0,places=12)
        self.assertAlmostEqual(signed_record(tables[1]),-305256/7661275,places=12)
        total=(tables[0]+127*tables[1])/128
        self.assertAlmostEqual(signed_record(total),-38157/965200,places=12)
        self.assertAlmostEqual(signed_work(total),0,places=12)
        self.assertAlmostEqual(np.dot(d,total.sum(axis=(1,2))),0,places=12)
        self.assertAlmostEqual(total[:,0,:].sum()-total[:,1,:].sum(),0,places=12)
        # D and R separately have zero mean, but D*R does not. J pairing is
        # a separate within-sector symmetry, not a consequence of q·d=0.

    def test_new_relational_dynamics_changes_record_correlation_not_zero_pair(self):
        for histories in self.ref:
            fulls=[sum((table(evolve(v,t)) for v in histories)) for t in (0,math.pi/4,math.pi/2)]
            initial=signed_record(fulls[0])
            for tab,factor in zip(fulls,(1,.8,.6)):
                self.assertAlmostEqual(signed_record(tab),factor*initial,places=12)
                self.assertAlmostEqual(signed_work(tab),0,places=12)
                np.testing.assert_allclose(tab.sum(axis=(1,2)),q,atol=1e-13)
        # Relative evolution uses ω=1/2,g=1, so sign-flip probability is
        # (ω²/ν²)sin²θ = (1/5)sin²θ.

    def test_equal_geometry_marginals_and_mirror_do_not_fix_joint_incidence(self):
        full=(i_r_m_table(self.oldclock[0])+127*i_r_m_table(self.oldclock[1]))/128
        independent=np.broadcast_to(q[:,None,None]/4,(3,2,2)).copy()
        for tab in (full,independent):
            np.testing.assert_allclose(tab.sum(axis=(1,2)),q,atol=1e-13)
            np.testing.assert_allclose(tab[:,:,0],tab[:,:,1],atol=1e-13)
            self.assertAlmostEqual(tab[:,0,:].sum(),.5,places=13)
            self.assertAlmostEqual(signed_work(tab),0,places=13)
        self.assertAlmostEqual(signed_record(independent),0,places=13)
        self.assertAlmostEqual(signed_record(full),-38157/965200,places=12)
        # The independent table is an alternative stipulated incidence rule,
        # not a preparation claimed genuinely possible or physically actual.

if __name__=='__main__':unittest.main()
