"""Integrated semantic test on the existing mirror-paired physical history.

Countermodels grant actual incidence and a physical–experience law as explicit
hypotheses. They are not claims about real subjects, genuine metaphysical
possibilities, the sufficiency of zero, or objective energy.
"""
import math
import unittest
import numpy as np
from verification.zero_mirror_balanced_plenitude_subject_test import mirror_state
from verification.zero_plenitude_coupling_clock_test import conditional
from verification.zero_neutral_exchange_from_balance_test import I16,Qp

SIGNS=np.array([1.,-1.]) # index 0 means +, index 1 means −


def incidence_distribution():
    # Existing whole: k in {-1,0,1}, geometric q=1/2, flags F and parity P.
    # Condition on a finite phase window centered π/4 with half-width π/8.
    # The clock is uniform on [0,2π), so this window has probability 1/8.
    labels,weights,v=mirror_state(.5,1)
    nodes,ws=np.polynomial.legendre.leggauss(24)
    table=np.zeros((len(labels),2,2))
    for node,w in zip(nodes,ws):
        t=math.pi/4+math.pi*node/8
        c=np.stack([conditional(v[:,:,f],labels,t) for f in range(2)],axis=1)
        for k in range(len(labels)):
            for f in range(2):
                for s,op in enumerate((I16-Qp,Qp)):
                    table[k,f,s]+=w/2*np.vdot(c[k,f],op@c[k,f]).real
    return labels,weights,table


def conditional_expect(tab,values,k_index):
    row=tab[k_index]
    return float(np.sum(row*values[k_index])/np.sum(row))


class IntegratedExperienceNecessityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.labels,cls.weights,cls.mu=incidence_distribution()
        cls.s=np.broadcast_to(SIGNS[None,None,:],cls.mu.shape)
        cls.f=np.broadcast_to(SIGNS[None,:,None],cls.mu.shape)

    def test_both_valence_bridges_fit_same_physical_state_and_actual_incidence_set(self):
        self.assertAlmostEqual(self.mu.sum(),1,places=13)
        np.testing.assert_allclose(self.mu,self.mu[:,::-1,::-1],atol=1e-14)
        self.assertEqual(np.count_nonzero(self.mu>1e-12),10)
        # Conditional semantic assumption: every positive-support triple is
        # an actual subject incidence and μ is its Born self-location weight.
        actual=self.mu>1e-12
        v1=self.s.copy();v2=self.f.copy()
        for v in (v1,v2):
            np.testing.assert_allclose(v[:,::-1,::-1],-v,atol=1e-14)
            self.assertAlmostEqual(float(np.sum(self.mu*v)),0,places=13)
            self.assertTrue(np.all(np.abs(v[actual])==1))
            self.assertTrue(np.any(v[actual]<0))
            self.assertTrue(np.any(v[actual]>0))
        # Same physical facts, incidences, measure, mirror and signed total,
        # but different physical–experiential relative correlation at k=1.
        self.assertAlmostEqual(conditional_expect(self.mu,self.s*v1,2),1,places=13)
        self.assertAlmostEqual(conditional_expect(self.mu,self.s*v2,2),0,places=13)
        self.assertAlmostEqual(conditional_expect(self.mu,(v1!=v2).astype(float),2),.5,places=13)

    def test_valence_difference_is_not_a_global_sign_renaming(self):
        v1=self.s;v2=self.f
        # Under v→−v or s→−s, absolute relative correlations are invariant.
        corr1=abs(conditional_expect(self.mu,self.s*v1,2))
        corr2=abs(conditional_expect(self.mu,self.s*v2,2))
        self.assertAlmostEqual(corr1,1,places=13)
        self.assertAlmostEqual(corr2,0,places=13)
        self.assertTrue(np.any((v1!=v2)&(self.mu>1e-12)))
        self.assertTrue(np.any((v1!=-v2)&(self.mu>1e-12)))

    def test_unit_counting_is_canonical_if_finite_incidence_labels_are_exact(self):
        # If each of the ten labels is exactly one actual incidence and each
        # counts once, normalized counting is fixed, rather than arbitrary.
        present=self.mu>1e-12
        counting=present.astype(float)/present.sum()
        self.assertEqual(present.sum(),10)
        self.assertAlmostEqual(counting[1].sum(),1/5,places=13)
        np.testing.assert_allclose(counting,counting[:,::-1,::-1],atol=1e-14)
        for v in (self.s,self.f):
            self.assertAlmostEqual(float(np.sum(counting*v)),0,places=13)
        # That fixed rule disagrees with Born self-location in this example;
        # neither incidence identification nor rule choice follows from C=0.

    def test_full_support_and_mirror_do_not_fix_actual_incidence_weights(self):
        # Same physical state and same incidences. μ2 is an alternative
        # stipulated self-location measure, not the physical Born rule.
        multiplier=np.where(self.labels[:,None,None]==0,2.,1.)
        other=self.mu*multiplier
        other/=other.sum()
        np.testing.assert_array_equal(self.mu>1e-12,other>1e-12)
        np.testing.assert_allclose(other,other[:,::-1,::-1],atol=1e-14)
        self.assertAlmostEqual(self.mu[1].sum(),.5,places=13)
        self.assertAlmostEqual(other[1].sum(),2/3,places=13)
        for v in (self.s,self.f):
            self.assertAlmostEqual(float(np.sum(self.mu*v)),0,places=13)
            self.assertAlmostEqual(float(np.sum(other*v)),0,places=13)
        # If the incidence measure must equal Born weights, this comparison
        # is excluded by that extra premise; it is not derived here.

    def test_conditional_plenitude_of_both_bridges_still_does_not_select_measure(self):
        # Stronger hypothetical: both bridge types are actual in distinct
        # labelled incidences. The physical meaning of λ must be justified.
        v1=self.s;v2=self.f
        for gamma in (.25,.75):
            measure=np.stack((gamma*self.mu,(1-gamma)*self.mu))
            vals=np.stack((v1,v2))
            sign=np.stack((self.s,self.s))
            self.assertTrue(np.all(measure[:,self.mu>1e-12]>0))
            np.testing.assert_allclose(measure,measure[:,:,::-1,::-1],atol=1e-14)
            self.assertAlmostEqual(float(np.sum(measure*vals)),0,places=13)
            selected=measure[:,2,:,:]
            self.assertAlmostEqual(float(np.sum(selected*sign[:,2]*vals[:,2])/selected.sum()),gamma,places=13)
        # Both include all labelled incidences; different γ gives different
        # relational statistics. This does not prove λ is genuinely possible.

    def test_fixed_truthful_report_would_distinguish_the_bridges(self):
        # Conditional report assumption: an actual subject has access to P
        # and an independently validated truthful report outputs s=Xp.
        report=self.s
        for v,expected in ((self.s,0.),(self.f,.5)):
            discrepancy=(report!=v).astype(float)
            self.assertAlmostEqual(conditional_expect(self.mu,discrepancy,2),expected,places=13)
        # This operational control does not establish a real subject, report
        # accuracy, spacetime-local access to F, or a phenomenal law.

    def test_negative_local_valence_is_not_removed_by_zero_total(self):
        for v in (self.s,self.f):
            negative=self.mu[v<0].sum()
            positive=self.mu[v>0].sum()
            self.assertAlmostEqual(negative,.5,places=13)
            self.assertAlmostEqual(positive,.5,places=13)
            self.assertAlmostEqual(float(np.sum(self.mu*v)),0,places=13)
            self.assertGreater(negative,0)
        # A signed sum being zero does not imply no negative incidence.

if __name__=='__main__':unittest.main()
