"""Mirror-paired plenitude with zero charge and conditional sign balance.

Mirror symmetry, flag, Born weighting and any valence map are explicit inputs.
No subjective incidence, accessibility or objective energy is assumed.
"""
import math
import unittest
import numpy as np
from verification.zero_neutral_exchange_from_balance_test import (
    I16,P0,H,CHARGE,PG,XP,Qp,Qq,Qcorr,psi
)
from verification.zero_plenitude_coupling_clock_test import (
    whole,conditional,retrieve,expect_marginal
)

# Extend the neutral-sector involution to the whole original system.
S=H+(I16-P0)


def mirror_state(q,n,alpha=.5):
    labels,w,v=whole(q,n)
    # Coherent flag 0 with old history, flag 1 with S-transformed history.
    sv=np.einsum('ab,klb->kla',S,v,optimize=True)
    return labels,w,np.stack((math.sqrt(alpha)*v,math.sqrt(1-alpha)*sv),axis=2)


def mirror(v):
    return np.stack((np.einsum('ab,klb->kla',S,v[:,:,1]),
                     np.einsum('ab,klb->kla',S,v[:,:,0])),axis=2)


def ready_retrieved(v,labels):
    return np.stack([retrieve(v[:,:,f],labels) for f in range(2)],axis=1)


def effects(v,e):
    a=v.reshape(-1,2,16)
    out=np.zeros((2,2),complex)
    for f in range(2):
        for x,projector in enumerate((I16-Qp,Qp)):
            out[f,x]=np.einsum('ia,ij,ab,jb->',a[:,f].conj(),e,projector,a[:,f],optimize=True)
    return out.real


class MirrorBalancedPlenitudeTests(unittest.TestCase):
    def test_involution_preserves_constraints_and_flips_three_agreeing_readouts(self):
        np.testing.assert_allclose(S@S,I16,atol=1e-14)
        np.testing.assert_allclose(S@CHARGE,CHARGE@S,atol=1e-14)
        np.testing.assert_allclose(S@PG,PG@S,atol=1e-14)
        np.testing.assert_allclose(S@H,H@S,atol=1e-14)
        sector=P0@PG
        for b in (Qp,Qq,Qcorr):
            np.testing.assert_allclose((S@b@S-(I16-b))@sector,0,atol=1e-14)
        # S is a physical symmetry only if these specified readouts and the
        # added flag are physically available; it is not assumed subjecthood.

    def test_unique_balanced_relative_seed_without_selecting_a_coupling(self):
        eig,vec=np.linalg.eigh(P0@PG)
        vv=vec[:,eig>.5]
        h=vv.conj().T@S@vv
        z=vv.conj().T@XP@vv
        fX=np.array([[0,1],[1,0]],complex)
        fZ=np.diag([1,-1])
        T=np.kron(fX,h)
        condition=np.kron(fZ,z)
        id4=np.eye(4)
        np.testing.assert_allclose(T@T,id4,atol=1e-14)
        np.testing.assert_allclose(T@condition,condition@T,atol=1e-14)
        penalty=(id4-T)/2+(id4-condition)/2
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(penalty))<1e-10),1)
        # Conditions select a symmetric relative seed on each k, but k's
        # amplitudes remain unconstrained. Both conditions are inputs.

    def test_one_constraint_has_exactly_one_paired_history_per_coupling(self):
        # Finite invariant/neutral logical reduction; full embedding to the
        # prior 16-dimensional system is checked by the other tests.
        x=np.array([[0,1],[1,0]],complex)
        z=np.diag([1,-1])
        i2=np.eye(2);i4=np.eye(4)
        labels=np.arange(-2,3);m=len(labels)
        v=np.zeros((m*m*4,m*4),complex)
        c=np.zeros((m*m*4,m*m*4),complex)
        pplus=(i2+x)/2;pminus=(i2-x)/2
        for a,k in enumerate(labels):
            for b,l in enumerate(labels):
                block=(a*m+b)*4
                c[block:block+4,block:block+4]=k*np.kron(i2,x)-l*i4
            for f in range(2):
                for s in range(2):
                    col=a*4+2*f+s
                    for b,p in ((k+2,pplus),(-k+2,pminus)):
                        for t in range(2):v[(a*m+b)*4+2*f+t,col]+=p[t,s]
        np.testing.assert_allclose(v.conj().T@v,np.eye(m*4),atol=1e-14)
        np.testing.assert_allclose(c@v,0,atol=1e-14)
        mirrorpen=np.kron(np.eye(m*m),(i4-np.kron(x,x))/2)
        relpen=np.kron(np.eye(m),(i4-np.kron(z,z))/2)
        whole=c@c+mirrorpen+v@relpen@v.conj().T
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(whole))<1e-10),m)
        # Exactly one invariant paired history per retained k; amplitudes over
        # distinct k remain free, so this is not a measure selection.

    def test_coherent_whole_satisfies_mirror_neutrality_and_clock(self):
        for q in (.5,.8):
            labels,w,v=mirror_state(q,5)
            self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
            np.testing.assert_allclose(mirror(v),v,atol=1e-14)
            hv=np.einsum('ab,klfb->klfa',H,v,optimize=True)
            constraint=labels[:,None,None,None]*hv-labels[None,:,None,None]*v
            self.assertLess(np.linalg.norm(constraint),1e-13)
            for op in (CHARGE,I16-PG):
                self.assertLess(np.linalg.norm(np.einsum('ab,klfb->klfa',op,v,optimize=True)),1e-13)
            r=ready_retrieved(v,labels)
            self.assertLess(np.linalg.norm(np.einsum('ab,kb->ka',Qp,r[:,0])),1e-13)
            self.assertLess(np.linalg.norm(np.einsum('ab,kb->ka',I16-Qp,r[:,1])),1e-13)
            # Whole is pure; the coherent off-diagonal flag block is not
            # removed by tracing or dephasing the flag.
            blocks=np.einsum('klfa,klga->fg',v,v.conj(),optimize=True)
            np.testing.assert_allclose(blocks,np.eye(2)/2,atol=1e-14)
            # The whole density's off-diagonal flag block is an outer
            # product with Frobenius norm ||v0|| ||v1||, not zero.
            self.assertAlmostEqual(np.linalg.norm(v[:,:,0])*np.linalg.norm(v[:,:,1]),.5,places=13)

    def test_sign_balance_for_every_clock_and_coupling_effect(self):
        labels,w,v=mirror_state(.8,3)
        rng=np.random.default_rng(20261031)
        dim=len(labels)**2
        for _ in range(4):
            m=rng.normal(size=(dim,5))+1j*rng.normal(size=(dim,5))
            e=m@m.conj().T
            e/=np.linalg.norm(e,2)
            t=effects(v,e)
            self.assertGreater(t.sum(),1e-4)
            self.assertAlmostEqual(t[0,0],t[1,1],places=13)
            self.assertAlmostEqual(t[0,1],t[1,0],places=13)
            self.assertAlmostEqual(t[:,0].sum(),t[:,1].sum(),places=13)
        # E may mix clock and coupling coherently but ignores the mirror flag
        # and system, so E commutes with the stipulated mirror involution.

    def test_balanced_signs_do_not_freeze_record_history(self):
        for q in (.5,.8):
            labels,w,v=mirror_state(q,5)
            for t in (0,math.pi/4,math.pi/2):
                c=np.stack([conditional(v[:,:,f],labels,t) for f in range(2)],axis=1)
                self.assertAlmostEqual(expect_marginal(c,XP),0,places=13)
                self.assertAlmostEqual(expect_marginal(c,Qp@(I16-Qq)),0,places=13)
                self.assertAlmostEqual(expect_marginal(c,Qp@(I16-Qcorr)),0,places=13)
                # The mirror-flag / P agreement changes despite equal sign margins.
                agreement=(expect_marginal(c[:,0],I16-Qp)+expect_marginal(c[:,1],Qp))
                expected=sum(wi*math.cos(k*t)**2 for k,wi in zip(labels,w))
                self.assertAlmostEqual(agreement,expected,places=13)
            self.assertAlmostEqual(sum(wi*math.cos(k*0)**2 for k,wi in zip(labels,w)),1,places=13)
            self.assertLess(sum(wi*math.cos(k*math.pi/2)**2 for k,wi in zip(labels,w)),.8)

    def test_zero_and_plenitude_without_mirror_do_not_force_equal_signs(self):
        alpha=.8
        labels,w,v=mirror_state(.5,4,alpha)
        self.assertGreater(np.linalg.norm(v-mirror(v)),.2)
        self.assertLess(np.linalg.norm(np.einsum('ab,klfb->klfa',CHARGE,v)),1e-13)
        c=np.stack([conditional(v[:,:,f],labels,0) for f in range(2)],axis=1)
        self.assertAlmostEqual(expect_marginal(c,XP),2*alpha-1,places=13)
        # Every coupling still has nonzero weight, but mirror invariance is lost.

    def test_signed_valence_cancellation_is_a_conditional_bridge(self):
        # On any mirror-paired incidence space, an odd integrable signed score
        # cancels with a symmetric measure. This finite discrete example tests
        # the algebra, not existence, assignment or actual incidence.
        weights=np.array([.02,.13,.35,.35,.13,.02])
        signed=np.array([-3.,-2.,-1.,1.,2.,3.])
        self.assertAlmostEqual(float(weights@signed),0,places=14)
        self.assertTrue(np.all(signed[:3]<0))
        # Multiplying all scores by −1 preserves cancellation and all physical
        # premises, so sign orientation cannot be inferred from zero alone.
        self.assertAlmostEqual(float(weights@(-signed)),0,places=14)

if __name__=='__main__':unittest.main()
