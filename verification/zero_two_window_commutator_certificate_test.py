"""Independent checks for the exact-rational continuum commutator certificate."""
import math
import unittest
from fractions import Fraction as F

from verification.zero_two_window_commutator_certificate import verify, pi_interval, atan_interval


class ContinuumCommutatorCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=verify()

    def test_exact_certificate_and_thresholds(self):
        r=self.result
        self.assertLess(r['commutator_squared_upper'],F(419,1000)**2)
        self.assertLess(r['eta'],F(1,10**11))
        self.assertEqual(r['flag_amplitude_upper'],F(50699,305760))
        self.assertLess(r['flag_error_upper'],F(28,1000))
        self.assertLess(r['flag_error_upper'],F(275,10000))

    def test_arctangent_interval_and_rational_pi(self):
        for n in (1,2,3,24):
            a,b=atan_interval(5,n)
            self.assertLess(a,b)
            # The exact interval nesting is checked without evaluating atan.
            x,y=atan_interval(5,n+1)
            self.assertGreaterEqual(x,a)
            self.assertLessEqual(y,b)
        lo,hi=pi_interval()
        self.assertLess(F(314,100),lo)
        self.assertLess(hi,F(22,7))
        self.assertLess(hi-lo,F(1,10**34))

    def test_continuum_support_bound_for_previous_sample(self):
        # q_U is rounded UP from 0.019484694... . sqrt(q_U)<0.14.
        q_upper=F(19485,10**6)
        self.assertLess(q_upper,F(7,50)**2)
        bound=(F(7,50)+self.result['flag_amplitude_upper'])**2
        self.assertLess(bound,F(94,1000))

    def test_nystrom_residual_control_not_the_continuum_proof(self):
        import numpy as np
        from verification.zero_autonomous_two_window_records_test import make_model,theta_apply
        n=80;model=make_model(n);p=model[0];t=p+6.5;x=t+.5
        envelope=np.sqrt(30)*x*(1-x)/np.sqrt(n)
        residual=[]
        for phase in (1,-1):
            f=envelope*np.exp(phase*15j*t)
            v=np.zeros((2,2,2,n),complex)
            v[0,0,0]=f/np.sqrt(2);v[1,0,0]=1j*f/np.sqrt(2)
            residual.append((theta_apply(model,v,0)-7.046*v).ravel())
        gram=np.array([[np.vdot(a,b) for b in residual] for a in residual])
        exact=self.result
        reference=np.array([[float(exact['diag0']),complex(float(exact['cross_re']),float(exact['cross_im']))],
                            [complex(float(exact['cross_re']),-float(exact['cross_im'])),float(exact['diag1'])]])
        self.assertLess(np.max(abs(gram-reference)),.00001)

if __name__=='__main__':unittest.main()
