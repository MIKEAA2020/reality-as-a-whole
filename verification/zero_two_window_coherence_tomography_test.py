"""Tomography of the two-packet span from existing 32 history outcomes.

Calibration assumes known reference states and stable independent copies.
All matrices are finite-regulator model outputs, not measured lab data.
"""
import itertools
import math
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model, initial
from verification.zero_two_window_recorded_histories_test import root_data, history_branches, full_table
from verification.zero_two_window_operational_clock_calibration_test import (corrupt_first,
    coherent_counterexample, total_variation)

PAULI = (np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex))


def packet_basis(model):
    n=len(model[0]);u=initial(model).ravel(); v=initial(make_model(n,x0=15.)).ravel()
    v=v-np.vdot(u,v)*u;v=v/np.linalg.norm(v)
    return np.column_stack((u,v))


def effect_table(model, basis):
    """Compress all record effects onto the chosen orthonormal packet span."""
    n=len(model[0]); F=np.zeros((2,2,2,2,2,2,2),complex)
    for h in (0,1):
        values,V=root_data(model,h)
        branches=[history_branches(model,values,V,basis[:,i]) for i in (0,1)]
        for hist in itertools.product((0,1),repeat=3):
            vectors=[branches[i][hist].reshape(2,2,2,n) for i in (0,1)]
            for i in (0,1):
                for j in (0,1):
                    F[hist+(slice(None),slice(None),i,j)] += np.sum(vectors[i].conj()*vectors[j],axis=(0,3))/2
    return corrupt_first(F)


def bloch_map(F):
    effects=F.reshape(-1,2,2)
    c=np.trace(effects,axis1=1,axis2=2).real/2
    L=np.column_stack([np.trace(effects@s,axis1=1,axis2=2).real/2 for s in PAULI])
    return c,L


def unprobed_m1_effect(model,basis):
    """Final memory event under autonomous evolution without checkpoint probes."""
    n=len(model[0]); E=np.zeros((2,2),complex)
    for h in (0,1):
        vals,V=root_data(model,h)
        states=[(V@(np.exp(1j*np.sqrt(vals)*100)*(V.conj().T@basis[:,i]))).reshape(2,2,2,n)[:,1,:,:]
                for i in (0,1)]
        for i in (0,1):
            for j in (0,1): E[i,j]+=np.vdot(states[i],states[j])/2
    return E


def multinomial_e(n,alpha):
    """Dimension-free l2 concentration via expectation and McDiarmid."""
    return (1+math.sqrt(math.log(1/alpha)))/math.sqrt(n)


def frequency(counts):
    counts=np.asarray(counts)
    if counts.shape!=(32,) or np.any(counts<0) or counts.sum()==0: raise ValueError('invalid counts')
    return counts/counts.sum()


def calibrate_and_fit(counts, alpha=.05):
    """Counts order z+, z-, x+, y+, target. Return Bloch estimate/radius."""
    if len(counts)!=5 or not 0<alpha<1: raise ValueError('invalid calibration')
    obs=[frequency(a) for a in counts]
    zp,zm,xp,yp,target=obs
    c=(zp+zm)/2
    L=np.column_stack((xp-c,yp-c,(zp-zm)/2))
    sv=np.linalg.svd(L,compute_uv=False);s=sv[-1]
    if s < 1e-15: return None,2.,s
    r=np.linalg.lstsq(L,target-c,rcond=None)[0]
    norm=np.linalg.norm(r)
    if norm>1:r=r/norm
    eps=[multinomial_e(sum(a),alpha/5) for a in counts]
    # c error <= (ez+ + ez-)/2, x/y column <= e_ref+ec,
    # z column <= ec.  Frobenius then bounds spectral norm.
    ec=(eps[0]+eps[1])/2
    el=math.sqrt((eps[2]+ec)**2+(eps[3]+ec)**2+ec**2)
    radius=min(2.,(eps[4]+ec+el)/s)
    return r,radius,s


def coefficients(v, basis):
    z=basis.conj().T@v
    rho=np.outer(z,z.conj())
    return np.array([np.trace(rho@s).real for s in PAULI])


def distance_to_segment(r,a,b):
    d=b-a; w=np.clip(np.dot(r-a,d)/np.dot(d,d),0,1)
    return np.linalg.norm(r-(a+w*d))


class TwoWindowCoherenceTomographyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=make_model(40);cls.B=packet_basis(cls.model)
        cls.F=effect_table(cls.model,cls.B);cls.c,cls.L=bloch_map(cls.F)

    def test_povm_is_normalized_and_effects_positive(self):
        E=self.F.reshape(-1,2,2)
        np.testing.assert_allclose(E.sum(axis=0),np.eye(2),atol=2e-12)
        for x in E:
            self.assertLess(np.linalg.norm(x-x.conj().T),1e-12)
            self.assertGreater(np.linalg.eigvalsh(x).min(),-1e-12)
        self.assertLess(np.linalg.norm(self.L.sum(axis=0)),1e-12)

    def test_informational_completeness_and_refinement(self):
        np.testing.assert_allclose(self.B.conj().T@self.B,np.eye(2),atol=1e-12)
        sv=np.linalg.svd(self.L,compute_uv=False)
        self.assertGreater(sv[-1],.0014)
        self.assertGreater(sv[0]/sv[-1],280)
        model=make_model(80);_,L80=bloch_map(effect_table(model,packet_basis(model)))
        sv80=np.linalg.svd(L80,compute_uv=False)
        self.assertLess(np.max(abs(sv80-sv)),.00004)

    def test_all_probabilities_match_direct_complex_superposition(self):
        z=np.array([math.sqrt(.3),np.exp(.71j)*math.sqrt(.7)])
        v=self.B@z;r=coefficients(v,self.B)
        expected=corrupt_first(full_table(self.model,v)).ravel()
        np.testing.assert_allclose(self.c+self.L@r,expected,atol=1e-12)
        np.testing.assert_allclose(np.linalg.lstsq(self.L,expected-self.c,rcond=None)[0],r,atol=1e-11)

    def test_equal_click_witness_resolved_by_existing_records(self):
        pin=full_table(self.model,self.B[:,0])[1].sum()
        rec=initial(make_model(40,x0=15)).ravel()
        prec=full_table(self.model,rec)[1].sum()
        x,y=coherent_counterexample(self.model,pin,prec)
        a=corrupt_first(full_table(self.model,x));b=corrupt_first(full_table(self.model,y))
        self.assertAlmostEqual(a[1].sum(),b[1].sum(),places=11)
        self.assertGreater(abs(a[:,:,:,1,:].sum()-b[:,:,:,1,:].sum()),.015)
        self.assertGreater(total_variation(a,b),.025)
        endpoint_a=coefficients(self.B[:,0],self.B); endpoint_b=coefficients(rec,self.B)
        for v in (x,y):
            r=coefficients(v,self.B);np.testing.assert_allclose(self.c+self.L@r,
                           corrupt_first(full_table(self.model,v)).ravel(),atol=1e-12)
            self.assertGreater(distance_to_segment(r,endpoint_a,endpoint_b),.99)

    def test_simulated_calibration_and_high_probability_bound(self):
        n=10_000_000_000; rng=np.random.default_rng(4820)
        r=np.array([.31,-.42,.20]); refs=[np.array([0,0,1]),np.array([0,0,-1]),
              np.array([1,0,0]),np.array([0,1,0]),r]
        p=[self.c+self.L@x for x in refs]
        counts=[rng.multinomial(n,x/x.sum()) for x in p]
        estimate,rad,s=calibrate_and_fit(counts)
        self.assertLess(np.linalg.norm(estimate-r),rad)
        self.assertLess(rad,.12)
        self.assertGreater(s,.0014)
        self.assertLess(total_variation(self.c+self.L@estimate,self.c+self.L@r),
                        np.linalg.norm(estimate-r)/2+1e-12)
        E=unprobed_m1_effect(self.model,self.B)
        c=E.trace().real/2; row=np.array([np.trace(E@s).real/2 for s in PAULI])
        self.assertLessEqual(abs(row@(estimate-r)),rad/2+1e-12)
        self.assertTrue(0 <= c+row@estimate <= 1)

    def test_nearly_outside_span_is_not_detected_to_arbitrary_precision(self):
        outside=initial(make_model(40,x0=0)).ravel()
        outside-=self.B@(self.B.conj().T@outside);outside/=np.linalg.norm(outside)
        self.assertLess(np.linalg.norm(self.B.conj().T@outside),1e-12)
        pin=corrupt_first(full_table(self.model,self.B[:,0])).ravel()
        pout=corrupt_first(full_table(self.model,outside)).ravel()
        for lam in (.01,.001):
            observed=(1-lam)*pin+lam*pout
            self.assertLessEqual(np.linalg.norm(observed-pin),math.sqrt(2)*lam+1e-12)
            self.assertLessEqual(total_variation(observed,pin),lam+1e-12)

    def test_invalid_counts_and_aborted_fit(self):
        with self.assertRaises(ValueError):calibrate_and_fit([np.zeros(32)]*5)
        with self.assertRaises(ValueError):calibrate_and_fit([np.ones(32)]*4)
        r,rad,s=calibrate_and_fit([np.ones(32)]*5)
        self.assertIsNone(r);self.assertEqual(rad,2.)

if __name__=='__main__': unittest.main()
