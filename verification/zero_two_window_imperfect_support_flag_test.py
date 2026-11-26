"""Support-flag error bounds and an undetectable outside-direction control.

Finite-dimensional detector simulations and an analytic confidence bound; no
claim that the assumed uniform detector error bound is physically calibrated.
"""
import math
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model, initial
from verification.zero_two_window_recorded_histories_test import full_table
from verification.zero_two_window_operational_clock_calibration_test import corrupt_first, total_variation
from verification.zero_two_window_coherence_tomography_test import (PAULI, packet_basis, effect_table,
    bloch_map, coefficients, multinomial_e)
from verification.zero_two_window_support_eraser_test import readout, leakage_upper, fit as perfect_fit, effects


def observed(r, leakage, false_positive, false_negative, outside_labels):
    """Block-diagonal flag with arbitrary distribution for missed Q events."""
    if not (0<=leakage<=1 and 0<=false_positive<=1 and 0<=false_negative<=1): raise ValueError('bad error rates')
    labels=np.asarray(outside_labels,dtype=float)
    if labels.shape!=(4,) or (labels<0).any() or not np.isclose(labels.sum(),1): raise ValueError('bad labels')
    return np.r_[(1-leakage)*(1-false_positive)*readout(r)[:4]
                 +leakage*false_negative*labels,
                 (1-leakage)*false_positive+leakage*(1-false_negative)]


def fit_imperfect(counts, beta_max, f_min=0., alpha=.05):
    """Bound accepted-state contamination with an assumed uniform FN bound."""
    if len(counts)!=5 or not 0<alpha<1 or not 0<=f_min<1 or not 0<=beta_max<=1:
        raise ValueError('bad parameters')
    samples=[];sizes=[]
    for x in counts:
        x=np.asarray(x)
        if x.shape!=(5,) or np.any(x<0) or x.sum()==0: raise ValueError('bad counts')
        if x[:4].sum()==0: return None,2.,1.,1.,0.
        sizes.append(int(x[:4].sum()));samples.append(x[:4]/x[:4].sum())
    zp,zm,xp,yp,target=samples;c=(zp+zm)/2
    L=np.column_stack((xp-c,yp-c,(zp-zm)/2));s=np.linalg.svd(L,compute_uv=False)[-1]
    if s<1e-15:return None,2.,1.,1.,s
    target_counts=np.asarray(counts[-1]);N=int(target_counts.sum())
    qu=leakage_upper(int(target_counts[4]),N,alpha)
    # If qu<f_min the uniform-f_min model is inconsistent on the confidence
    # event; abort rather than claim the source has zero leakage.
    if qu < f_min:return None,2.,1.,1.,s
    slope=1-beta_max-f_min
    lam=1. if slope<=0 else min(1.,max(0.,(qu-f_min)/slope))
    gamma=1. if qu>=1 else min(1.,beta_max*lam/(1-qu))
    e=[multinomial_e(n,alpha/6) for n in sizes];ec=(e[0]+e[1])/2
    el=math.sqrt((e[2]+ec)**2+(e[3]+ec)**2+ec**2)
    R=min(2.,(e[4]+ec+el+math.sqrt(2)*gamma)/s)
    r=np.linalg.lstsq(L,target-c,rcond=None)[0];norm=np.linalg.norm(r)
    if norm>1:r=r/norm
    return r,R,lam,gamma,s


def batches(r,n,rng,lam=.01,f=.005,beta=.08):
    refs=(np.array([0,0,1]),np.array([0,0,-1]),np.array([1,0,0]),np.array([0,1,0]))
    labels=np.array([.7,.1,.1,.1])
    return [rng.multinomial(n,observed(x,0,f,beta,labels)) for x in refs]+[
            rng.multinomial(n,observed(r,lam,f,beta,labels))]


def outside_modes(model,B):
    n=len(model[0])
    def orth(x0,existing):
        x=initial(make_model(n,x0=x0)).ravel();x-=B@(B.conj().T@x)
        for v in existing:x-=v*np.vdot(v,x)
        return x/np.linalg.norm(x)
    x=orth(0,[]);y=orth(30,[x]);return x,y


class ImperfectSupportFlagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=make_model(40);cls.B=packet_basis(cls.model)

    def test_noisy_flag_calibration_and_prediction_bound(self):
        z=np.array([math.sqrt(.3),np.exp(.71j)*math.sqrt(.7)]);inside=self.B@z
        r=coefficients(inside,self.B);x,_=outside_modes(self.model,self.B);lam=.01
        actual=math.sqrt(1-lam)*inside+math.sqrt(lam)*x
        counts=batches(r,100000,np.random.default_rng(9824),lam=lam)
        est,R,upper,gamma,s=fit_imperfect(counts,beta_max=.10,f_min=.005)
        self.assertLess(np.linalg.norm(est-r),R)
        self.assertGreaterEqual(upper,lam)
        q=observed(r,lam,.005,.08,[.7,.1,.1,.1])[4]
        true_gamma=.08*lam/(1-q)
        self.assertGreaterEqual(gamma,true_gamma)
        c,L=bloch_map(effect_table(self.model,self.B))
        a=corrupt_first(full_table(self.model,actual)).ravel();p=c+L@est
        self.assertLessEqual(total_variation(a,p),min(1.,math.sqrt(upper)+R/2)+1e-12)

    def test_perfect_flag_case_reduces_to_previous_bound(self):
        r=np.array([.31,-.42,.20]);rng=np.random.default_rng(9387);n=100000
        refs=(np.array([0,0,1]),np.array([0,0,-1]),np.array([1,0,0]),np.array([0,1,0]),r)
        counts=[rng.multinomial(n,readout(x)) for x in refs]
        a,R,lam,gamma,s=fit_imperfect(counts,beta_max=0,f_min=0)
        b,R0,lam0,s0=perfect_fit(counts)
        np.testing.assert_allclose(a,b,atol=1e-12)
        self.assertAlmostEqual(R,R0,places=12);self.assertAlmostEqual(lam,lam0,places=12)
        self.assertEqual(gamma,0.)

    def test_no_uniform_detection_bound_means_trivial_support_bound(self):
        counts=batches(np.array([.31,-.42,.2]),100000,np.random.default_rng(72))
        _,R,lam,gamma,_=fit_imperfect(counts,beta_max=1.)
        self.assertEqual(lam,1.)
        self.assertEqual(R,2.)

    def test_wrong_false_negative_bound_can_hide_large_leakage(self):
        r=np.array([.31,-.42,.2]);rng=np.random.default_rng(322);n=100000
        refs=(np.array([0,0,1]),np.array([0,0,-1]),np.array([1,0,0]),np.array([0,1,0]))
        labels=readout(r)[:4]
        samples=[rng.multinomial(n,observed(x,0,0,1,labels)) for x in refs]
        samples.append(rng.multinomial(n,observed(r,.2,0,1,labels)))
        _,_,claimed,_,_=fit_imperfect(samples,beta_max=0.)
        self.assertLess(claimed,.001)
        self.assertGreater(.2,claimed)  # The premise beta_max=0 was false.
        _,_,honest,_,_=fit_imperfect(samples,beta_max=1.)
        self.assertEqual(honest,1.)

    def test_hidden_outside_direction_evades_finite_calibrations(self):
        B=self.B;dim=B.shape[0];u=B[:,0];x,y=outside_modes(self.model,B)
        self.assertLess(np.linalg.norm(B.conj().T@x),1e-12)
        self.assertLess(np.linalg.norm(B.conj().T@y),1e-12)
        self.assertLess(abs(np.vdot(x,y)),1e-12)
        E=effects();p=readout(np.array([0,0,1]))[:4]
        # Any of the four inside labels can be emitted on the hidden mode x;
        # known test mode y is detected perfectly. These effects are positive
        # and normalized on the entire finite space.
        xx=np.outer(x,x.conj());Q=np.eye(dim)-B@B.conj().T
        G=[B@e@B.conj().T+p[i]*xx for i,e in enumerate(E)]
        H=Q-xx
        np.testing.assert_allclose(sum(G)+H,np.eye(dim),atol=2e-12)
        self.assertGreater(np.linalg.eigvalsh(H).min(),-2e-12)
        probs=lambda v: np.array([np.vdot(v,g@v).real for g in G]+[np.vdot(v,H@v).real])
        np.testing.assert_allclose(probs(u),probs(x),atol=1e-12)
        self.assertAlmostEqual(probs(y)[-1],1,places=11)
        a=corrupt_first(full_table(self.model,u));b=corrupt_first(full_table(self.model,x))
        self.assertGreater(total_variation(a,b),.42)

    def test_invalid_and_inconsistent_assumptions_abort(self):
        with self.assertRaises(ValueError):fit_imperfect([],beta_max=0.)
        with self.assertRaises(ValueError):observed(np.zeros(3),0,0,0,[1,0,0,2])
        counts=[np.array([25,25,25,25,0]) for _ in range(5)]
        result=fit_imperfect(counts,beta_max=.1,f_min=.9)
        self.assertIsNone(result[0])

if __name__=='__main__': unittest.main()
