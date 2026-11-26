"""Explicit alternative two-packet interferometric POVM and support flag.

This is a different, stipulated nonlocal-mode instrument, not a passive clock
switch or a local autonomous detector. Simulations are not experiments.
"""
import math
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model, initial
from verification.zero_two_window_recorded_histories_test import full_table
from verification.zero_two_window_operational_clock_calibration_test import corrupt_first, total_variation
from verification.zero_two_window_coherence_tomography_test import (PAULI, packet_basis, effect_table,
    bloch_map, coefficients, multinomial_e, calibrate_and_fit)

TETRA=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/math.sqrt(3)


def effects(error=.05):
    if not 0<=error<=1: raise ValueError('invalid bit-confusion probability')
    ideal=np.array([(np.eye(2)+sum(x*s for x,s in zip(v,PAULI)))/4 for v in TETRA])
    return (1-error)*ideal+(error/3)*(ideal.sum(axis=0)-ideal)


def readout(r,error=.05,leakage=0.):
    F=effects(error); rho=(np.eye(2)+sum(x*s for x,s in zip(r,PAULI)))/2
    p=np.array([np.trace(x@rho).real for x in F])
    return np.r_[(1-leakage)*p,leakage]


def leakage_upper(outcomes,total,alpha=.05):
    if total<=0 or not 0<=outcomes<=total or not 0<alpha<1: raise ValueError('invalid counts')
    hoeff=min(1.,outcomes/total+math.sqrt(math.log(12/alpha)/(2*total)))
    # Each of the two bounds gets failure budget alpha/12, jointly alpha/6.
    no_hit=-math.expm1(math.log(alpha/12)/total) if outcomes==0 else 1.
    return min(hoeff,no_hit)


def fit(counts,alpha=.05):
    """4 calibrated inside references and 1 target, each 5 reported outcomes."""
    if len(counts)!=5 or not 0<alpha<1: raise ValueError('invalid calibration')
    batch=[];sizes=[]
    for i,entry in enumerate(counts):
        x=np.asarray(entry)
        if x.shape!=(5,) or np.any(x<0) or x.sum()==0: raise ValueError('invalid counts')
        if i<4 and x[4]!=0: raise ValueError('reference leaked under perfect-flag premise')
        inside=x[:4].sum()
        if inside==0: return None,2.,1.,0.
        sizes.append(int(inside));batch.append(x[:4]/inside)
    zp,zm,xp,yp,target=batch;c=(zp+zm)/2
    L=np.column_stack((xp-c,yp-c,(zp-zm)/2))
    s=np.linalg.svd(L,compute_uv=False)[-1]
    if s<1e-15:return None,2.,1.,s
    r=np.linalg.lstsq(L,target-c,rcond=None)[0]; nr=np.linalg.norm(r)
    if nr>1:r=r/nr
    e=[multinomial_e(n,alpha/6) for n in sizes]
    ec=(e[0]+e[1])/2
    el=math.sqrt((e[2]+ec)**2+(e[3]+ec)**2+ec**2)
    R=min(2.,(e[4]+ec+el)/s)
    target_counts=np.asarray(counts[-1]);N=int(target_counts.sum())
    upper=leakage_upper(int(target_counts[4]),N,alpha)
    return r,R,upper,s


def sqrt_2x2(a):
    w,v=np.linalg.eigh(a)
    if w.min() < -1e-12: raise ValueError('not positive')
    return (v*np.sqrt(np.clip(w,0,None)))@v.conj().T


def sample_batches(r,n,rng,leakage=0.):
    refs=(np.array([0,0,1]),np.array([0,0,-1]),np.array([1,0,0]),np.array([0,1,0]))
    return [rng.multinomial(n,readout(x)) for x in refs]+[rng.multinomial(n,readout(r,leakage=leakage))]


class SupportEraserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=make_model(40);cls.B=packet_basis(cls.model)

    def test_tetra_povm_has_balanced_bloch_sensitivity(self):
        F=effects();np.testing.assert_allclose(F.sum(axis=0),np.eye(2),atol=1e-14)
        for e in F:self.assertGreater(np.linalg.eigvalsh(e).min(),-1e-14)
        c=np.trace(F,axis1=1,axis2=2).real/2
        L=np.column_stack([np.trace(F@s,axis1=1,axis2=2).real/2 for s in PAULI])
        expected=(1-4*.05/3)/(2*math.sqrt(3))
        np.testing.assert_allclose(np.linalg.svd(L,compute_uv=False),expected,atol=1e-14)
        _,old=bloch_map(effect_table(self.model,self.B))
        self.assertGreater(expected/np.linalg.svd(old,compute_uv=False)[-1],180)
        np.testing.assert_allclose(c,.25,atol=1e-14)

    def test_full_five_outcome_instrument_and_dilation_isometry(self):
        B=self.B;dim=B.shape[0];Q=np.eye(dim)-B@B.conj().T
        Ks=[B@sqrt_2x2(e)@B.conj().T for e in effects()]+[Q]
        isometry=np.vstack(Ks)
        self.assertLess(np.linalg.norm(isometry.conj().T@isometry-np.eye(dim)),1e-11)
        self.assertGreater(np.linalg.norm(Q),1.)

    def test_finite_calibration_without_leakage(self):
        r=np.array([.31,-.42,.20]); counts=sample_batches(r,100000,np.random.default_rng(9387))
        estimate,R,upper,s=fit(counts)
        self.assertEqual(counts[-1][4],0)
        self.assertGreater(s,.25)
        self.assertLess(R,.25)
        self.assertLess(np.linalg.norm(estimate-r),R)
        self.assertLess(math.sqrt(upper)+R/2,.14)

    def test_equal_budget_previous_detector_control(self):
        c,L=bloch_map(effect_table(self.model,self.B)); rng=np.random.default_rng(9387)
        refs=(np.array([0,0,1]),np.array([0,0,-1]),np.array([1,0,0]),
              np.array([0,1,0]),np.array([.31,-.42,.20]))
        samples=[rng.multinomial(100000,(c+L@r)/(c+L@r).sum()) for r in refs]
        _,R,_=calibrate_and_fit(samples)
        self.assertEqual(R,2.)  # This confidence certificate is uninformative.

    def test_coherent_leakage_and_original_record_prediction(self):
        z=np.array([math.sqrt(.3),np.exp(.71j)*math.sqrt(.7)])
        inside=self.B@z; r=coefficients(inside,self.B)
        outside=initial(make_model(40,x0=0)).ravel()
        outside-=self.B@(self.B.conj().T@outside);outside/=np.linalg.norm(outside)
        lam=.01; actual=math.sqrt(1-lam)*inside+math.sqrt(lam)*outside
        counts=sample_batches(r,100000,np.random.default_rng(804),leakage=lam)
        estimate,R,upper,s=fit(counts)
        self.assertGreater(counts[-1][4],0);self.assertGreaterEqual(upper,lam)
        self.assertLess(np.linalg.norm(r-estimate),R)
        a=corrupt_first(full_table(self.model,actual)).ravel()
        # The 32-outcome prediction on separate copies, not after the new POVM.
        F=effect_table(self.model,self.B);c,L=bloch_map(F); b=c+L@estimate
        self.assertLessEqual(total_variation(a,b),math.sqrt(upper)+R/2+1e-12)
        exact=corrupt_first(full_table(self.model,inside)).ravel()
        self.assertLessEqual(total_variation(a,exact),math.sqrt(lam)+1e-12)

    def test_new_measurement_physically_disturbs_later_history(self):
        v=self.B[:,0];F=effects();original=full_table(self.model,v)
        post=sum(full_table(self.model,self.B@sqrt_2x2(e)@(self.B.conj().T@v)) for e in F)
        self.assertAlmostEqual(post.sum(),1.,places=11)
        self.assertGreater(total_variation(original,post),.01)

    def test_perfect_flag_is_an_essential_assumption(self):
        # If every outside event were misreported as inside, observed zero
        # flags could coexist with true leakage 1%; the ideal-flag bound fails.
        self.assertLess(leakage_upper(0,100000),.01)
        true_leakage=.01; outside_false_negative=1.
        self.assertEqual(true_leakage*(1-outside_false_negative),0.)

    def test_abort_and_support_guard(self):
        with self.assertRaises(ValueError):leakage_upper(2,1)
        refs=[np.array([25,25,25,25,0]) for _ in range(4)]
        self.assertEqual(fit(refs+[np.array([0,0,0,0,100])])[0],None)
        refs[0][4]=1
        with self.assertRaises(ValueError):fit(refs+[np.array([25,25,25,25,0])])

if __name__=='__main__':unittest.main()
