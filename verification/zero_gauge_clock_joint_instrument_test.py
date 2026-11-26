"""Operational finite-clock instrument, statistics and countercontrols."""
import math
import unittest
import numpy as np
from scipy.integrate import quad

from verification.zero_gauge_clock_joint_instrument import (sensor_unitary,clock_model,
    clock_residuals,chi_unitary,correlation,conditional_x_probabilities,hoeffding_radius,
    epsilon_interval,pure_shift_distance,conditional_drift_bound)
from verification.zero_noncyclic_chirality_clock import window_history,shifted_window
from verification.zero_three_frame_chirality import gauge_loop,invariants,loop_observables
from verification.zero_spherical_invariant_echo import rodrigues,unit


class JointInstrumentTests(unittest.TestCase):
    def test_detector_unitaries_kraus_and_gauge_invariance(self):
        for p in (0.,.05,.5,.9,1.):
            u=sensor_unitary(p);np.testing.assert_allclose(u.T@u,np.eye(2),atol=4e-16)
            self.assertAlmostEqual(u[1,0]**2,p,places=14)
        for chi in (-1.,-.2,0.,2.,3.):
            u=chi_unitary(chi);np.testing.assert_allclose(u.T@u,np.eye(2),atol=4e-16)
            self.assertAlmostEqual(u[0,0]**2-u[1,0]**2,chi/3,places=14)
        rng=np.random.default_rng(191)
        for _ in range(40):
            ds=tuple(unit(rng.normal(size=3)) for _ in range(3))
            ls=tuple(rodrigues(rng.normal(size=3),rng.uniform(-3,3)) for _ in range(3))
            rs=tuple(rodrigues(rng.normal(size=3),rng.uniform(-3,3)) for _ in range(3))
            original=loop_observables(ds,*ls)[0];new=gauge_loop(ds,*ls,rs)
            transformed=loop_observables(*new)[0]
            np.testing.assert_allclose(chi_unitary(original),chi_unitary(transformed),atol=1e-14)
            np.testing.assert_allclose(invariants(ds,ls[0],ls[1]),invariants(*new[:3]),atol=1e-14)

    def test_exact_clock_probability_and_coherence_cost(self):
        n=40;alpha=.05;beta=.1
        f,r,p,w=clock_model(n,alpha,beta);out=clock_residuals(n,alpha,beta)
        self.assertAlmostEqual(p,alpha*sum(f[:10]**2)+(1-beta)*sum(f[10:]**2),places=14)
        self.assertAlmostEqual(w,(1-beta)*sum(f[10:]**2)/p,places=14)
        gamma=math.sqrt((1-alpha)*beta)+math.sqrt(alpha*(1-beta))
        expected=out['bare']**2+2*f[9]*f[10]*(1-gamma)
        self.assertAlmostEqual(out['coherent']**2,expected,places=14)
        self.assertGreater(out['coherent'],out['bare'])
        self.assertAlmostEqual(out['bare']**2,2-2*math.cos(math.pi/(n+1)),places=13)
        self.assertGreater(out['late'],out['bare'])
        # If the sensor carries no threshold info, its overlap is one and
        # it need not increase the constraint residual.
        equal=clock_residuals(n,.2,.8)
        self.assertAlmostEqual(equal['bare'],equal['coherent'],places=13)
        self.assertAlmostEqual(equal['bare'],equal['late'],places=13)

    def test_full_reduced_coherent_clock_detector_residual(self):
        n=40;alpha=.05;beta=.1;h=.4;q=1
        v=window_history(n,q,h);f,r,_,_=clock_model(n,alpha,beta)
        sensor=np.column_stack((np.sqrt(1-r),np.sqrt(r)))
        augmented=v[...,None]*sensor[:,None,None,None,:]
        shifted=np.stack([shifted_window(augmented[...,i],q,h) for i in (0,1)],axis=-1)
        padded=np.zeros_like(shifted);padded[:n]=augmented
        self.assertAlmostEqual(np.linalg.norm(shifted-padded),clock_residuals(n,alpha,beta)['coherent'],places=13)
        post=v*np.sqrt(r)[:,None,None,None];post/=math.sqrt(clock_model(n,alpha,beta)[2])
        out=shifted_window(post,q,h);padded=np.zeros_like(out);padded[:n]=post
        self.assertAlmostEqual(np.linalg.norm(out-padded),clock_residuals(n,alpha,beta)['late'],places=13)

    def test_joint_sensor_correlation_and_null_counterexample(self):
        # Quadrature with nonflat-loop density ρ=1+ε tχ/3.
        nodes,weights=np.polynomial.legendre.leggauss(40)
        u=nodes[:,None,None];v=nodes[None,:,None];theta=(nodes[None,None,:]+1)*math.pi/2
        t=np.sqrt(1-u*u)*v;chi=1+2*np.cos(theta)
        measure=(weights[:,None,None]/2)*(weights[None,:,None]/2)*(weights[None,None,:]*np.sin(theta/2)**2)
        eps=.8;lam=.9;kappa=.7;pb=.05;pc=.1
        rho=1+eps*t*chi/3
        integrand=lam*t*kappa*chi/3*(1-2*pb)*(1-2*pc)
        real=float(np.sum(measure*rho*integrand))
        self.assertAlmostEqual(real,correlation(eps,lam,kappa,pb,pc,1.),places=13)
        self.assertEqual(correlation(0,lam,kappa,pb,pc,1.),0.)
        self.assertAlmostEqual(float(np.sum(measure*rho*t)),0,places=13)
        self.assertAlmostEqual(float(np.sum(measure*rho*chi)),0,places=13)

    def test_joint_distribution_sampling_and_conditional_confidence(self):
        _,_,p,w=clock_model(40,.05,.1)
        eps=.8;lam=1.;kappa=1.;pb=.05;pc=.1;m=100000;delta=.05
        probs=conditional_x_probabilities(eps,lam,kappa,pb,pc,w)
        np.testing.assert_allclose(probs.sum(),1.,atol=1e-15)
        self.assertAlmostEqual(probs[0]-probs[2],correlation(eps,lam,kappa,pb,pc,w),places=14)
        self.assertAlmostEqual(probs[1],1-w,places=14)
        counts=np.random.default_rng(13047).multinomial(m,probs)
        mean=float((counts[0]-counts[2])/m)
        lo,hi=epsilon_interval(mean,m,delta,lam,kappa,pb,pc,w)
        self.assertGreater(lo,0.)
        self.assertLessEqual(lo,eps);self.assertGreaterEqual(hi,eps)
        self.assertGreaterEqual(hoeffding_radius(m,delta),abs(mean-correlation(eps,lam,kappa,pb,pc,w)))
        self.assertGreater(m/p,m)
        with self.assertRaises(ValueError):epsilon_interval(mean,m,delta,lam,kappa,.5,pc,w)
        # This fixed-seed draw is one illustration; the bound is a repeated-
        # sampling statement under iid/model/calibration assumptions.

    def test_exact_pure_state_drift_and_safe_conditioning_bound(self):
        r=clock_residuals(40,.05,.1);d=pure_shift_distance(r['coherent'])
        v=window_history(40,1,.4);_,readout,p,_=clock_model(40,.05,.1)
        sensor=np.column_stack((np.sqrt(1-readout),np.sqrt(readout)))
        a=v[...,None]*sensor[:,None,None,None,:]
        b=np.stack([shifted_window(a[...,i],1,.4) for i in (0,1)],axis=-1)
        aa=np.zeros_like(b);aa[:40]=a
        overlap=np.vdot(aa,b)
        self.assertAlmostEqual(d,math.sqrt(max(0,1-abs(overlap)**2)),places=13)
        self.assertGreater(conditional_drift_bound(p,d),abs(correlation(.8,1,1,.05,.1,r['w'])))
        self.assertEqual(conditional_drift_bound(.1,.2),2.)
        # This is only a generic one-step conditional bound, not closeness to
        # a normalizable exactly stationary state or an operational guarantee
        # for arbitrary conditioning on extremely rare events.

if __name__=='__main__':unittest.main()
