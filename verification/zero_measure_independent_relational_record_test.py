"""Measure-independent record identities and coupling-weight tomography.

All results are conditional on prior Hilbert spaces, group action and charge.
Joint readouts are not assumed accessible to subjects or objective cosmic energy.
"""
import math
import unittest
import numpy as np
from verification.zero_neutral_exchange_from_balance_test import (
    I16,P0,H,CHARGE,PG,Qp,Qq,Qcorr,psi,GROUP,theta
)
from verification.zero_plenitude_coupling_clock_test import whole,conditional,expect_marginal

J=1j*(H@Qp-Qp@H)
Isect=P0@PG


def asymmetric_whole(n=5):
    labels,w,v=whole(.65,n)
    target=np.array([(.65**abs(int(k)))*math.exp(.25*int(k)) for k in labels])
    target/=target.sum()
    phases=np.exp(.47j*labels**2+.23j*labels)
    v=v*(np.sqrt(target/w)*phases)[:,None,None]
    return labels,target,v


def postselected(v,e,op):
    a=v.reshape(-1,16)
    return np.einsum('ia,ij,ab,jb->',a.conj(),e,op,a,optimize=True)


class MeasureIndependentRecordTests(unittest.TestCase):
    def test_record_equalities_are_operator_consequences_of_sector(self):
        np.testing.assert_allclose(P0@PG,PG@P0,atol=1e-14)
        np.testing.assert_allclose(Isect@Isect,Isect,atol=1e-14)
        self.assertAlmostEqual(np.trace(Isect).real,2,places=12)
        np.testing.assert_allclose((Qp-Qq)@P0,0,atol=1e-14)
        # The reference–spin correlation follows from symmetry alone;
        # neutrality is only needed to add the compensator sign.
        np.testing.assert_allclose((Qp-Qcorr)@PG,0,atol=1e-14)
        np.testing.assert_allclose((Qp-Qcorr)@Isect,0,atol=1e-14)
        for q in (Qp,Qq,Qcorr):
            np.testing.assert_allclose(q@Isect,Isect@q,atol=1e-14)
            self.assertAlmostEqual(np.trace(Isect@q).real,1,places=12)
        # These equalities require neither psi, a clock, H nor any measure.

    def test_holds_for_all_invariant_neutral_states_not_just_seed(self):
        vals,vecs=np.linalg.eigh(Isect)
        basis=vecs[:,vals>.5]
        self.assertEqual(basis.shape,(16,2))
        for v in (basis[:,0],basis[:,1],(basis[:,0]+1j*basis[:,1])/math.sqrt(2)):
            for a,b in ((Qp,Qq),(Qp,Qcorr)):
                self.assertLess(np.linalg.norm(a@(I16-b)@v),1e-14)
                self.assertLess(np.linalg.norm((I16-a)@b@v),1e-14)
            self.assertLess(np.linalg.norm(CHARGE@v),1e-14)
        # Mixed states and entanglement with external registers follow by
        # linearity; the sector alone does not force both probabilities > 0.

    def test_coherent_clock_coupling_postselections_cannot_break_agreement(self):
        labels,w,v=asymmetric_whole(3)
        self.assertAlmostEqual(np.linalg.norm(v),1,places=13)
        rng=np.random.default_rng(1024)
        dim=len(labels)**2
        for _ in range(3):
            x=rng.normal(size=(dim,5))+1j*rng.normal(size=(dim,5))
            e=x@x.conj().T
            e/=np.linalg.norm(e,2)
            probability=postselected(v,e,I16).real
            self.assertGreater(probability,1e-4)
            for a,b in ((Qp,Qq),(Qp,Qcorr)):
                self.assertLess(abs(postselected(v,e,a@(I16-b))),1e-13)
                self.assertLess(abs(postselected(v,e,(I16-a)@b)),1e-13)
        # E may coherently mix coupling and clock labels. It acts only on
        # those factors, not as an intervention on the internal system.

    def test_sign_current_is_invariant_and_exactly_resolves_direction(self):
        np.testing.assert_allclose(J,J.conj().T,atol=1e-14)
        np.testing.assert_allclose(J@CHARGE,CHARGE@J,atol=1e-14)
        np.testing.assert_allclose(theta(J),-J,atol=1e-14)
        for u in GROUP:np.testing.assert_allclose(J@u,u@J,atol=1e-14)
        for t in (.2,-.2,math.pi/4):
            v=math.cos(t)*psi-1j*math.sin(t)*H@psi
            self.assertAlmostEqual(np.vdot(v,J@v).real,math.sin(2*t),places=12)
        # J is a derived joint observable, not a physical arrow or subject.

    def test_time_fourier_tomography_recovers_asymmetric_weights(self):
        labels,w,v=asymmetric_whole(5)
        # M>4N gives exact discrete Fourier orthogonality for this cutoff.
        m=64
        times=np.pi*np.arange(m)/m
        p=[];j=[]
        for t in times:
            c=conditional(v,labels,t)
            p.append(expect_marginal(c,Qp))
            j.append(expect_marginal(c,J))
        p=np.array(p);j=np.array(j)
        restored={0:1-2*p.mean()}
        for n in range(1,6):
            s=-4*np.mean(p*np.cos(2*n*times))
            d=2*np.mean(j*np.sin(2*n*times))
            restored[n]=(s+d)/2
            restored[-n]=(s-d)/2
        np.testing.assert_allclose([restored[int(k)] for k in labels],w,atol=2e-14)
        self.assertGreater(abs(restored[1]-restored[-1]),.01)
        # Full k-coherence phases do not enter these coupling-diagonal
        # readouts; reconstructing them requires additional observables.

    def test_exact_plenitude_gives_strict_but_not_uniform_bounds(self):
        # p_k=(1−ε)δ_{k,0}+ε q_k and similarly k=±1, where q has
        # positive symmetric support everywhere, satisfy full support.
        for epsilon in (.1,.001,1e-7):
            q=.5
            odd=2*q/(1+q)**2
            low=epsilon*odd
            high=(1-epsilon)+epsilon*odd
            self.assertGreater(low,0)
            self.assertLess(high,1)
            self.assertLess(low,epsilon)
            self.assertLess(1-high,epsilon)
        # At t not in πZ, p1>0 forces P>0 and p0>0 forces P<1.
        # This does not imply actual outcomes or a uniform lower bound.

if __name__=='__main__':unittest.main()
