"""Conditional audit of Koch–Riahinia–Rincon q-desic idea in a toy model.

Diagonal qutrit metric operators are stipulated, not solutions of quantum GR.
The test uses their connection-averaging prescription, the project's actual
sphere-record vectors, and an independent norm-preservation diagnostic.
"""
import math
import unittest
from fractions import Fraction as F

from verification.zero_five_ray_record_current_unification_test import joint_state,probabilities
from verification.zero_sphere_mismatch_experience_comparison_test import phase_flip,subject_density
from verification.zero_spin_constitution_test import close,inner

EPS=F(1,4)


def lapse(q,r,eps=EPS):
    return 1+eps*r*q


def gamma_t(q,r,eps=EPS):
    # ds²=A(r)dt²-dr²-r²dΩ²; Γ^t_tr=A'/(2A).
    return eps*q/(2*lapse(q,r,eps))


def gamma_rtt(q,r,eps=EPS):
    return eps*q/2


def mean_of(fn,weights):
    return sum(w*fn(q) for q,w in weights.items())


def qgamma(r,eps=EPS):
    return -eps*eps*r/(2*(1-eps*eps*r*r))


def q_tdot(r,r0,tdot0,eps=float(EPS)):
    return tdot0*math.sqrt((1-eps*eps*r0*r0)/(1-eps*eps*r*r))


def q_coordinate_t(r,r0,tdot0,vr,eps=float(EPS)):
    factor=tdot0*math.sqrt(1-eps*eps*r0*r0)/(eps*vr)
    return factor*(math.asin(eps*r)-math.asin(eps*r0))


class QDesicSphereClockConnectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sphere=joint_state('triple');cls.sphere_alt=phase_flip(cls.sphere)
        cls.equal={-1:F(1,2),1:F(1,2)}
        cls.nofluct={0:F(1)}

    def test_actual_confined_record_restrictions_equal(self):
        self.assertAlmostEqual(abs(inner(self.sphere,self.sphere_alt)),0)
        close(self,subject_density(self.sphere),subject_density(self.sphere_alt))
        for k,v in probabilities(self.sphere).items():
            self.assertAlmostEqual(v,probabilities(self.sphere_alt)[k])

    def test_mean_metric_same_but_connection_differs(self):
        for r in (F(0),F(1,2),F(1),F(2),F(3)):
            self.assertGreater(lapse(-1,r),0)
            self.assertEqual(mean_of(lambda q:lapse(q,r),self.equal),1)
            self.assertEqual(mean_of(lambda q:lapse(q,r),self.nofluct),1)
            self.assertEqual(mean_of(lambda q:gamma_t(q,r),self.equal),qgamma(r))
            self.assertEqual(mean_of(lambda q:gamma_t(q,r),self.nofluct),0)
            self.assertEqual(mean_of(lambda q:gamma_rtt(q,r),self.equal),0)
        self.assertEqual(qgamma(F(1)),F(-1,30))

    def test_mean_inverse_metric_is_not_inverse_of_mean(self):
        r=F(1)
        inv=mean_of(lambda q:1/lapse(q,r),self.equal)
        inverse_mean=1/mean_of(lambda q:lapse(q,r),self.equal)
        self.assertEqual(inv,F(16,15))
        self.assertEqual(inverse_mean,1)
        self.assertNotEqual(inv,inverse_mean)

    def test_metric_lapse_and_connection_covariance_decomposition(self):
        for r in (F(1,2),F(1),F(2)):
            inv=mean_of(lambda q:1/lapse(q,r),self.equal)
            deriv_mean=mean_of(lambda q:EPS*q,self.equal)
            sym_product=mean_of(lambda q:(1/lapse(q,r))*EPS*q,self.equal)
            covariance=sym_product-inv*deriv_mean
            inverse_correction=(inv-1)*deriv_mean
            self.assertEqual(qgamma(r),(covariance+inverse_correction)/2)
            self.assertEqual(inverse_correction,0)

    def test_zero_covariance_alone_does_not_fix_connection_of_mean_metric(self):
        # A±(r)=1+κr±δ: A' is a c-number, so covariance vanishes,
        # but <A^-1> differs from <A>^-1.
        k=F(1,4);delta=F(1,4);r=F(1)
        a=lambda q:1+k*r+q*delta
        inv=mean_of(lambda q:1/a(q),self.equal)
        avg=mean_of(a,self.equal)
        cov=mean_of(lambda q:k/a(q),self.equal)-k*inv
        corr=k*(inv-1/avg)/2
        self.assertEqual(cov,0)
        self.assertEqual(corr,F(1,240))
        self.assertEqual(mean_of(lambda q:k/(2*a(q)),self.equal)-k/(2*avg),corr)

    def test_weyl_order_and_quantum_coherence_control(self):
        # The stipulated A and A' are diagonal in q: they commute, and a
        # coherent superposition of ± has the same expectations as a mixture.
        for r in (F(1),F(2)):
            states={q:gamma_t(q,r) for q in (-1,1)}
            mixture=(states[-1]+states[1])/2
            coherent=(states[-1]+states[1])/2
            self.assertEqual(coherent,mixture)
            self.assertEqual(coherent,qgamma(r))
        # Thus this exhibits quantum-state sensitivity, not interference.

    def test_radial_qdesic_and_coordinate_comparison(self):
        r0=1.;r1=2.;vr=.5;tdot0=math.sqrt(5)/2
        t_q=q_coordinate_t(r1,r0,tdot0,vr)
        t_mean=(tdot0/vr)*(r1-r0)
        self.assertAlmostEqual(t_q,2.3462232107078087)
        self.assertAlmostEqual(t_mean,math.sqrt(5))
        self.assertGreater(t_q-t_mean,.1)
        for r in (1.,1.4,1.8,2.):
            v=q_tdot(r,r0,tdot0)
            eps=float(EPS);acc=(eps*eps*r/(1-eps*eps*r*r))*v*vr
            dr=1e-5
            derivative=(q_tdot(r+dr,r0,tdot0)-q_tdot(r-dr,r0,tdot0))/(2*dr)*vr
            self.assertAlmostEqual(derivative,acc,places=9)

    def test_affine_timing_and_mean_metric_norm_conflict(self):
        # r=1, dr/dlambda=1/2, dt/dlambda=sqrt5/2, N=1.
        r=F(1);vr=F(1,2);ut2=F(5,4)
        factor=EPS*EPS*r/(1-EPS*EPS*r*r)
        # t''=factor*t'*r'; r''=0; dN/dλ=2 factor (t')² r'.
        norm_derivative=2*factor*ut2*vr
        self.assertEqual(norm_derivative,F(1,12))
        self.assertEqual(qgamma(r),F(-1,30))

    def test_nonaffine_timelike_fix_does_not_fix_null_drift(self):
        r=F(1);factor=EPS*EPS*r/(1-EPS*EPS*r*r)
        drift=2*factor*F(5,4)*F(1,2)
        norm=F(1)
        kappa=-drift/(2*norm)
        self.assertEqual(kappa,F(-1,24))
        self.assertEqual(drift+2*kappa*norm,0)
        # For a null tangent ut=ur=1, N=0. Adding kappa*u to
        # the acceleration cannot cancel the nonzero derivative of N.
        null_drift=2*factor
        self.assertEqual(null_drift,F(2,15))
        self.assertNotEqual(null_drift+2*kappa*0,0)

    def test_classical_and_zero_radial_velocity_controls(self):
        for r in (F(1),F(2)):
            self.assertEqual(qgamma(r,eps=F(0)),0)
            factor=EPS*EPS*r/(1-EPS*EPS*r*r)
            self.assertEqual(2*factor*F(5,4)*0,0)
        # The diagnostic does not show any inconsistency for all possible
        # motions, only for the stated radial initial data.

if __name__=='__main__':unittest.main()
