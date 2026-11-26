"""Causal controls for the prior instrument's observable and calibration."""
import unittest
import numpy as np
from verification.zero_gauge_clock_joint_instrument import clock_model,clock_residuals,correlation
from verification.zero_gauge_clock_meta_root import (selected_weight,shifted_correlation,
    target_post_mu,counterfeit_a,adversarial_output,target_output,coherent_sensor_window,
    move_window,measured_fixed_fiber,calibration_context_bound,systematic_sign_margin)

class GaugeClockMetaRootTests(unittest.TestCase):
    def test_observable_exact_shift_one_and_many_steps(self):
        n=40;alpha=.05;beta=.1;eps=.8
        f,r,p,w=clock_model(n,alpha,beta)
        post=correlation(eps,1,1,.05,.1,1.)
        self.assertAlmostEqual(selected_weight(n,alpha,beta,0),w,places=14)
        one=shifted_correlation(n,alpha,beta,1,eps)-shifted_correlation(n,alpha,beta,0,eps)
        self.assertAlmostEqual(one,post*alpha*f[9]**2/p,places=14)
        self.assertAlmostEqual(one,0.00002040018826289,places=14)
        self.assertAlmostEqual(shifted_correlation(n,alpha,beta,10,eps),post,places=14)
        self.assertAlmostEqual(shifted_correlation(n,alpha,beta,-30,eps),0.,places=14)
        self.assertLess(abs(one),.000021)
        self.assertGreater(clock_residuals(n,alpha,beta)['coherent'],.17)

    def test_explicit_coherent_sensor_shift_both_directions(self):
        n=40;alpha=.05;beta=.1;h=.43;chi=.7;q=1;pb=.05;pc=.1
        original=coherent_sensor_window(n,q,h,alpha,beta)
        for steps in (0,1,5,10,-1,-5,-30):
            shifted=move_window(original,q,h,steps)
            p,mean=measured_fixed_fiber(shifted,chi,1,1,pb,pc)
            expected=selected_weight(n,alpha,beta,steps)*(1-2*pb)*(1-2*pc)*h*chi/3
            self.assertAlmostEqual(p,clock_model(n,alpha,beta)[2],places=13)
            self.assertAlmostEqual(mean,expected,places=13)
        # Sensor memory is a fixed spectator under the tested W shifts.

    def test_direct_detector_error_changes_leakage_not_invariance_of_full_state(self):
        f,r,p,w=clock_model(40,0.,.1)
        self.assertAlmostEqual(w,1.,places=14)
        for k in (0,1,5,30):self.assertAlmostEqual(selected_weight(40,0.,.1,k),1.,places=14)
        self.assertLess(selected_weight(40,0.,.1,-1),1.)
        self.assertGreater(clock_residuals(40,0.,.1)['coherent'],.1)
        # Perfect false-late rejection eliminates this particular forward
        # signal drift, not the full-state disturbance or backward drift.

    def test_null_with_contextual_readout_mimics_correlated_signal(self):
        eps=.8;lam=kappa=1.;pb=.05;pc=.1
        for q in (0.,5/36,11/36,2/9,1/3):
            a=counterfeit_a(q,eps,lam,kappa,pb)
            actual,err_b,err_c=adversarial_output(pb,pc,a)
            expected=target_output(target_post_mu(q,eps,lam,kappa,pb,pc))
            for key in actual:self.assertAlmostEqual(actual[key],expected[key],places=14)
            self.assertAlmostEqual(err_b,pb,places=14)
            self.assertAlmostEqual(err_c,pc,places=14)
            self.assertGreaterEqual(pb-abs(a),0)
            self.assertLessEqual(pb+abs(a),1)
        # The joint-context dependence violates the assumed B error channel.
        # Measuring only separate marginals and average error rates cannot
        # identify which of the two stipulated models generated the table.

    def test_conditional_single_sign_calibration_does_not_reveal_context(self):
        pb=.05;pc=.1;a=counterfeit_a(2/9,.8,1,1,pb)
        for fixed_b in (1,-1):
            self.assertAlmostEqual(sum((pb+a*fixed_b*c)/2 for c in (1,-1)),pb,places=15)
        for fixed_c in (1,-1):
            self.assertAlmostEqual(sum((pb+a*b*fixed_c)/2 for b in (1,-1)),pb,places=15)
        self.assertNotAlmostEqual(pb+a,pb-a,places=5)
        self.assertAlmostEqual(a,-.008888888888888889,places=14)
        # Joint sign-resolved calibration can distinguish pb+a from pb−a.

    def test_context_calibration_bound_and_error_budget(self):
        estimate,radius=calibration_context_bound(5000,5000,100000,.025)
        self.assertEqual(estimate,0.)
        self.assertAlmostEqual(radius,.005037446682216015,places=15)
        w=clock_model(40,.05,.1)[3]
        margin=systematic_sign_margin(.01769,100000,.025,5000,5000,100000,.025,w,.1)
        self.assertAlmostEqual(margin,.0003161951090371543,places=14)
        # An observed contextual asymmetry of the counterfeit scale makes the
        # conservative positive-sign certificate fail, rather than confirming it.
        self.assertLess(systematic_sign_margin(.01769,100000,.025,4111,5889,100000,.025,w,.1),0.)
        with self.assertRaises(ValueError):calibration_context_bound(1,0,0,.05)
        with self.assertRaises(ValueError):systematic_sign_margin(0,100,.05,0,0,10,.05,2,.1)

    def test_context_bias_formula_with_nonzero_true_correlation(self):
        pb=.05;pc=.1;a=-.008;true_mu=.12
        observed=0.
        for b in (1,-1):
            for c in (1,-1):
                mass=(1+b*c*true_mu)/4
                observed+=mass*b*c*(1-2*(pb+a*b*c))*(1-2*pc)
        self.assertAlmostEqual(observed,(1-2*pc)*((1-2*pb)*true_mu-2*a),places=15)

    def test_invalid_counterfeit_and_original_zero_gain_controls(self):
        with self.assertRaises(ValueError):adversarial_output(.01,.1,-.02)
        self.assertEqual(shifted_correlation(40,.05,.1,1,0.),0.)
        self.assertEqual(target_post_mu(2/9,.8,1,1,.5,.1),0.)

if __name__=='__main__':unittest.main()
