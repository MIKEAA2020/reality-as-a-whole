"""All integer coupling histories in one exactly constrained stationary whole.

The allowed lattice, clock, coupling register and amplitudes are inputs.
Full mathematical support and Born weights are not actual-subject incidence.
Finite tests use explicitly normalized truncations with analytic tail bounds.
"""
import math
import unittest
import numpy as np
from verification.zero_neutral_exchange_from_balance_test import (
    I16,P0,H,CHARGE,PG,Qp,Qq,Qcorr,psi
)

PLUS=(P0+H)/2
MINUS=(P0-H)/2


def geom_prob(q,k):return (1-q)/(1+q)*q**abs(k)

def tail(q,n):return 2*q**(n+1)/(1+q)

def whole(q,n):
    """Finite normalized |coupling k, clock l, system> vector."""
    labels=np.arange(-n,n+1)
    weights=np.array([geom_prob(q,int(k)) for k in labels])
    weights/=weights.sum()
    v=np.zeros((len(labels),len(labels),16),complex)
    for i,k in enumerate(labels):
        v[i,k+n]+=math.sqrt(weights[i])*(PLUS@psi)
        v[i,-k+n]+=math.sqrt(weights[i])*(MINUS@psi)
    return labels,weights,v


def conditional(v,labels,t):
    return np.einsum('l,kla->ka',np.exp(-1j*labels*t),v,optimize=True)


def expect_marginal(v,op):
    return np.einsum('...a,ab,...b->',v.conj(),op,v,optimize=True).real


def retrieve(v,labels):
    n=(len(labels)-1)//2
    return np.stack([PLUS@v[i,k+n]+MINUS@v[i,-k+n] for i,k in enumerate(labels)])


class ZeroPlenitudeCouplingClockTests(unittest.TestCase):
    def test_two_full_support_sign_symmetric_normalized_weights(self):
        for q in (.5,.8):
            for k in range(60):
                self.assertGreater(geom_prob(q,k),0)
                self.assertEqual(geom_prob(q,k),geom_prob(q,-k))
            for n in (0,4,20,80):
                partial=sum(geom_prob(q,k) for k in range(-n,n+1))
                self.assertAlmostEqual(1-partial,tail(q,n),places=13)
        self.assertNotAlmostEqual(geom_prob(.5,0),geom_prob(.8,0),places=5)
        # Each sequence has full support, including the frozen k=0 history.

    def test_full_clock_constraint_all_old_zeros_and_ready_condition(self):
        for q in (.5,.8):
            labels,w,v=whole(q,5)
            self.assertAlmostEqual(np.linalg.norm(v),1,places=13)
            # H_sys=K⊗H, H_clock|l>=l|l>; each k branch is stationary.
            hv=np.einsum('ab,klb->kla',H,v,optimize=True)
            constraint=labels[:,None,None]*hv-labels[None,:,None]*v
            self.assertLess(np.linalg.norm(constraint),1e-13)
            for op in (CHARGE,I16-PG):
                self.assertLess(np.linalg.norm(np.einsum('ab,klb->kla',op,v,optimize=True)),1e-13)
            np.testing.assert_allclose(retrieve(v,labels),np.sqrt(w)[:,None]*psi,atol=1e-14)
            self.assertLess(np.linalg.norm(np.einsum('ab,kb->ka',Qp,retrieve(v,labels))),1e-13)
            # The physical V embedding retains the older C_i and L,S
            # conditions as checked in the earlier covariance verifier.

    def test_single_zero_constraint_has_independent_plenitude_amplitudes(self):
        labels,w,v=whole(.5,4)
        # The k-register makes the nine vectors orthogonal, all satisfying
        # the same zero constraint, the same symmetry and the same ready condition.
        for i,k in enumerate(labels):
            z=np.zeros_like(v);z[i]=v[i]/math.sqrt(w[i])
            hv=np.einsum('ab,klb->kla',H,z,optimize=True)
            self.assertLess(np.linalg.norm(labels[:,None,None]*hv-labels[None,:,None]*z),1e-13)
            self.assertAlmostEqual(np.linalg.norm(z),1,places=13)
        _,_,v2=whole(.8,4)
        self.assertLess(abs(np.vdot(v,v2)),.999)
        # All group-label histories remain coherent; no branch is projected away.

    def test_fixed_independent_clock_reading_distinguishes_weights(self):
        for q,exact in ((.5,4/9),(.8,40/81)):
            labels,w,v=whole(q,40)
            c=conditional(v,labels,math.pi/2)
            self.assertAlmostEqual(np.linalg.norm(c),1,places=13)
            observed=expect_marginal(c,Qp)
            explicit=sum(wi*math.sin(k*math.pi/2)**2 for k,wi in zip(labels,w))
            self.assertAlmostEqual(observed,explicit,places=13)
            self.assertLessEqual(abs(observed-exact),tail(q,40)+1e-14)
            for a,b in ((Qp,Qq),(Qp,Qcorr)):
                self.assertAlmostEqual(expect_marginal(c,a@(I16-b)),0,places=13)
                self.assertAlmostEqual(expect_marginal(c,(I16-a)@b),0,places=13)
        # Same zero charges and support, different record predictions.

    def test_clock_unselected_also_depends_on_weight(self):
        for q,exact in ((.5,1/3),(.8,4/9)):
            labels,w,v=whole(q,40)
            observed=expect_marginal(v,Qp)
            self.assertLessEqual(abs(observed-exact),tail(q,40)+1e-14)
            self.assertAlmostEqual(expect_marginal(v,Qp@(I16-Qq)),0,places=13)
            self.assertAlmostEqual(expect_marginal(v,Qp@(I16-Qcorr)),0,places=13)

    def test_phase_povm_density_and_zero_coupling_branch(self):
        labels,w,v=whole(.5,6)
        for t in (0,.13,math.pi/2,math.pi,2*math.pi-.1):
            c=conditional(v,labels,t)
            self.assertAlmostEqual(np.linalg.norm(c),1,places=13)
            for i,k in enumerate(labels):
                expected=math.sqrt(w[i])*(math.cos(k*t)*psi-1j*math.sin(k*t)*H@psi)
                np.testing.assert_allclose(c[i],expected,atol=1e-14)
            self.assertLess(np.linalg.norm(c[6]-math.sqrt(w[6])*psi),1e-14)
        # Canonical clock phase density is 1/(2π); this is a POVM density,
        # not an orthogonal exact-time outcome or a fundamental external time.

    def test_shift_symmetry_on_history_family_has_no_normalizable_uniform_state(self):
        # S shifts k by one and clock energy by +1 or −1 conditional on
        # H=±1. It maps each constrained history to the next, including k=0.
        labels,w,v=whole(.5,4)
        n=4
        for k in (-3,-1,0,1,3):
            old=v[k+n]/math.sqrt(w[k+n])
            shifted=np.zeros_like(old)
            for j,l in enumerate(labels):
                if l+1<=n:shifted[l+1+n]+=PLUS@old[j]
                if l-1>=-n:shifted[l-1+n]+=MINUS@old[j]
            expected=v[k+1+n]/math.sqrt(w[k+1+n])
            np.testing.assert_allclose(shifted,expected,atol=1e-14)
        # Equal nonzero probabilities for every integer are not summable.
        # This finite identity plus the countable-additivity proof in the
        # report establishes the example, not that S is physical gauge.

if __name__=='__main__':unittest.main()
