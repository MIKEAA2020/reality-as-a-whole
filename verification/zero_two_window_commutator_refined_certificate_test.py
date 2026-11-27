"""Tests for the sharpened continuum certificate and independent controls."""
import math
import unittest
from fractions import Fraction as F
import numpy as np
from verification.zero_two_window_commutator_refined_certificate import (
    check, trig_enclosures_at_15)
from verification.zero_autonomous_two_window_records_test import make_model, theta_apply


class RefinedContinuumCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = check()

    def test_exact_rational_bounds(self):
        r = self.result
        self.assertLess(r['overlap_upper'], F(11,5000))
        self.assertLess(r['comm_squared_upper'], F(412,1000)**2)
        self.assertEqual(r['amplitude_upper'], F(12463,76440))
        self.assertLess(r['probability_upper'], F(266,10000))
        # A prior illustrative binomial upper limit, not an experimental result.
        sqrt_q_upper = F(13959,100000)
        self.assertGreater(sqrt_q_upper**2, F(19485,10**6))
        self.assertLess((sqrt_q_upper+r['amplitude_upper'])**2, F(916,10000))

    def test_taylor_bounds_and_overlap_independent_quadrature_control(self):
        (s,es),(c,ec) = trig_enclosures_at_15()
        # Ordinary floating point is a control, not a check of 80-digit enclosure.
        self.assertAlmostEqual(float(s), math.sin(15), places=14)
        self.assertAlmostEqual(float(c), math.cos(15), places=14)
        self.assertGreater(es,0); self.assertGreater(ec,0)
        self.assertLess(es,F(1,10**20)); self.assertLess(ec,F(1,10**20))
        points,weights = np.polynomial.legendre.leggauss(64)
        x = (points+1)/2
        overlap = np.dot(weights/2,30*x*x*(1-x)**2*np.exp(30j*(x-.5)))
        formula = 120*(-888*math.sin(15)-180*math.cos(15))/30**5
        self.assertAlmostEqual(overlap.real, formula, places=13)
        self.assertLess(abs(overlap.imag),1e-14)
        self.assertLess(abs(overlap), float(self.result['overlap_upper'])+1e-13)

    def test_independent_regulated_offdiagonal_and_h_shift(self):
        # Directly construct an orthonormal basis of the sampled span; no
        # polynomial-Gram helpers from the exact certificate are used here.
        n=120
        model=make_model(n); p=model[0]; t=p+6.5
        samples=[]
        for phase in (1,-1):
            f=np.sqrt(30)*(0.25-t*t)*np.exp(phase*15j*t)/np.sqrt(n)
            v=np.zeros((2,2,2,n),complex)
            v[0,0,0]=f/np.sqrt(2); v[1,0,0]=1j*f/np.sqrt(2)
            samples.append(v.ravel())
        b,_=np.linalg.qr(np.column_stack(samples))
        off=[]
        for h in (0,1):
            theta_b=np.column_stack([theta_apply(model,b[:,j].reshape(2,2,2,n),h).ravel()
                                     for j in range(2)])
            off.append(theta_b-b@(b.conj().T@theta_b))
        self.assertLess(np.linalg.norm(off[0]-off[1]),1e-12)
        norm=np.linalg.norm(off[0],2)
        self.assertGreater(norm,.40)
        self.assertLess(norm,.412)
        # A mesh alone is not a continuum certificate.

if __name__ == '__main__': unittest.main()
