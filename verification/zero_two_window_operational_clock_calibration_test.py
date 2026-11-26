"""Finite-shot calibration for a restricted two-window preparation family.

Simulated copies, detector error model and model-predicted history tables.
No real experiment, clock-controlled apparatus or continuum error is assumed.
"""
import math
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model, initial
from verification.zero_two_window_recorded_histories_test import (full_table, history_branches,
                                                                  root_data)


def total_variation(a,b):
    return np.sum(abs(a-b))/2


def empirical_fit(clicks, trials, zero_clicks, zero_trials, one_clicks, one_trials, alpha=.05):
    """Hoeffding confidence bound with independent endpoint calibration batches."""
    if not 0 < alpha < 1 or min(trials,zero_trials,one_trials) < 1:
        raise ValueError('invalid confidence or number of trials')
    for c,n in ((clicks,trials),(zero_clicks,zero_trials),(one_clicks,one_trials)):
        if not 0 <= c <= n: raise ValueError('invalid count')
    y=clicks/trials; a=zero_clicks/zero_trials; b=one_clicks/one_trials
    gap=b-a
    if gap == 0: return None, 1.
    est=float(np.clip((y-a)/gap,0,1))
    e=lambda n: math.sqrt(math.log(6/alpha)/(2*n))
    radius=min(1., (e(trials)+max(e(zero_trials),e(one_trials)))/abs(gap))
    return est, radius


def noisy_click(p, false_positive=.03, false_negative=.05):
    return false_positive+(1-false_positive-false_negative)*p


def corrupt_first(table, false_positive=.03, false_negative=.05):
    """Classically misreport the first bit; keep its physical backaction."""
    out=np.empty_like(table)
    out[0]=(1-false_positive)*table[0]+false_negative*table[1]
    out[1]=false_positive*table[0]+(1-false_negative)*table[1]
    return out


def coherent_counterexample(model, pin, prec):
    """Two pure preparations with same early click but different 000 rates."""
    v0=initial(model).ravel();v1=initial(make_model(len(model[0]),x0=15.)).ravel()
    v1=v1-np.vdot(v0,v1)*v0; v1=v1/np.linalg.norm(v1)
    basis=np.stack((v0,v1),axis=1)
    F=np.zeros((2,2),complex); G=np.zeros((2,2),complex)
    for h in (0,1):
        vals,V=root_data(model,h)
        hit=[history_branches(model,vals,V,basis[:,i],times=(30,))[(1,)] for i in (0,1)]
        no=[history_branches(model,vals,V,basis[:,i])[(0,0,0)] for i in (0,1)]
        for i in (0,1):
            for j in (0,1):
                F[i,j]+=np.vdot(hit[i],hit[j])/2
                G[i,j]+=np.vdot(no[i],no[j])/2
    pauli=(np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1]))
    fv=np.array([np.trace(F@s).real/2 for s in pauli]); gv=np.array([np.trace(G@s).real/2 for s in pauli])
    axis=fv/np.linalg.norm(fv); target=(pin+prec)/2
    c=(target-np.trace(F).real/2)/np.linalg.norm(fv)
    direction=gv-np.dot(gv,axis)*axis
    if abs(c)>1 or np.linalg.norm(direction)<1e-14: raise ValueError('no witness in this span')
    direction/=np.linalg.norm(direction)
    result=[]
    for sign in (-1,1):
        n=c*axis+sign*math.sqrt(max(0,1-c*c))*direction
        _,U=np.linalg.eigh(sum(x*s for x,s in zip(n,pauli)))
        result.append(basis@U[:,-1])
    return result


class OperationalClockCalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=make_model(40);cls.incident=initial(cls.model).ravel()
        cls.receding=initial(make_model(40,x0=15.)).ravel()
        cls.p1=full_table(cls.model,cls.incident);cls.p0=full_table(cls.model,cls.receding)
        cls.q1=cls.p1[1].sum();cls.q0=cls.p0[1].sum()

    def test_restricted_family_and_noisy_click_separation(self):
        self.assertAlmostEqual(self.p0.sum(),1,places=11)
        self.assertAlmostEqual(self.p1.sum(),1,places=11)
        self.assertAlmostEqual(self.q1,.35065193532925637,places=10)
        self.assertAlmostEqual(self.q0,.0004144328825809096,places=10)
        self.assertGreater(noisy_click(self.q1)-noisy_click(self.q0),.32)
        w=.37; model=(1-w)*self.p0+w*self.p1
        self.assertAlmostEqual(model[1].sum(),(1-w)*self.q0+w*self.q1,places=12)
        self.assertAlmostEqual(total_variation(model,self.p0),w*total_variation(self.p1,self.p0),places=12)

    def test_simulated_calibration_and_prediction_error(self):
        rng=np.random.default_rng(72849); n=10000; w=.37
        p0=corrupt_first(self.p0);p1=corrupt_first(self.p1)
        a=p0[1].sum();b=p1[1].sum();p=(1-w)*a+w*b
        self.assertAlmostEqual(a,noisy_click(self.q0),places=12)
        self.assertAlmostEqual(b,noisy_click(self.q1),places=12)
        c0=rng.binomial(n,a);c1=rng.binomial(n,b);c=rng.binomial(n,p)
        estimate,rad=empirical_fit(c,n,c0,n,c1,n)
        self.assertLessEqual(abs(estimate-w),rad)
        predicted=(1-estimate)*p0+estimate*p1
        actual=(1-w)*p0+w*p1
        self.assertLessEqual(total_variation(predicted,actual),rad*total_variation(p1,p0)+1e-14)
        self.assertLess(rad,.11)

    def test_independent_validation_of_a_no_click_event(self):
        rng=np.random.default_rng(137); n=10000; w=.37
        p0=corrupt_first(self.p0);p1=corrupt_first(self.p1)
        a=p0[1].sum();b=p1[1].sum();q=(1-w)*a+w*b
        c0=rng.binomial(n,a);c1=rng.binomial(n,b);c=rng.binomial(n,q)
        est,rad=empirical_fit(c,n,c0,n,c1,n)
        true=((1-w)*p0+w*p1)[0,0,0].sum()
        predicted=((1-est)*p0+est*p1)[0,0,0].sum()
        observed=rng.binomial(n,true)/n
        sampling=math.sqrt(math.log(2/.05)/(2*n))
        self.assertLessEqual(abs(observed-predicted), sampling+rad*total_variation(p0,p1))

    def test_fully_random_readout_erases_separation(self):
        self.assertAlmostEqual(noisy_click(self.q0,.4,.6),noisy_click(self.q1,.4,.6))
        self.assertAlmostEqual(total_variation(corrupt_first(self.p0,.4,.6),
                                                 corrupt_first(self.p1,.4,.6)),
                               total_variation(self.p0.sum(axis=0),self.p1.sum(axis=0)),places=12)
        # Other records can still distinguish the states; only the first bit is lost.

    def test_calibration_bound_algebra_for_every_grid_point(self):
        # On the three declared concentration events the deterministic bound
        # must hold, including clipping and either sign of the measured gap.
        for a in np.linspace(.05,.8,8):
            for b in np.linspace(.15,.95,9):
                if abs(a-b)<.05: continue
                for w in np.linspace(0,1,11):
                    for da,db,dy in ((.01,-.01,.02),(-.01,.01,-.02),(.01,.01,-.02)):
                        ah=a+da;bh=b+db; yh=(1-w)*a+w*b+dy
                        est=np.clip((yh-ah)/(bh-ah),0,1)
                        bound=(abs(dy)+max(abs(da),abs(db)))/abs(bh-ah)
                        self.assertLessEqual(abs(est-w),bound+1e-12)

    def test_exact_equal_calibrations_abort_and_errors_are_checked(self):
        self.assertEqual(empirical_fit(5,10,2,10,2,10),(None,1.))
        with self.assertRaises(ValueError):empirical_fit(11,10,2,10,3,10)
        with self.assertRaises(ValueError):empirical_fit(1,10,2,10,3,10,alpha=0)

    def test_coherent_preparations_undetectable_by_early_click(self):
        x,y=coherent_counterexample(self.model,self.q1,self.q0)
        self.assertAlmostEqual(np.linalg.norm(x),1,places=11)
        self.assertAlmostEqual(np.linalg.norm(y),1,places=11)
        a=full_table(self.model,x);b=full_table(self.model,y)
        self.assertAlmostEqual(a[1].sum(),b[1].sum(),places=11)
        self.assertAlmostEqual(a[1].sum(),(self.q1+self.q0)/2,places=11)
        self.assertAlmostEqual(corrupt_first(a)[1].sum(),corrupt_first(b)[1].sum(),places=11)
        self.assertGreater(abs(a[0,0,0].sum()-b[0,0,0].sum()),.008)
        self.assertGreater(abs(a[:,:,:,1,:].sum()-b[:,:,:,1,:].sum()),.01)
        self.assertGreater(total_variation(a,b),.02)

    def test_regulator_refinement_for_endpoints(self):
        model=make_model(80)
        for vector,reference in ((initial(model).ravel(),self.p1),
                 (initial(make_model(80,x0=15.)).ravel(),self.p0)):
            refined=full_table(model,vector)
            self.assertLess(np.max(abs(refined-reference)),.0002)

if __name__=='__main__': unittest.main()
