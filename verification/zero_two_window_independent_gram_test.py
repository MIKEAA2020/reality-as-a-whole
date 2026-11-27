"""Cross-check the rational Gram certificate with separate complex polynomials."""
from fractions import Fraction as F
import math
import unittest

from verification.zero_two_window_independent_gram import (
    ZERO, ONE, certify, independent_remainder_bound, independent_overlap_bound,
    conditional_cursor_bounds, integral_monomial, action, inner, pi_enclosure)
from verification.zero_two_window_commutator_certificate import verify


class IndependentExactGramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate=certify()
        cls.gram=cls.certificate['gram']
        cls.original=verify()
        cls.eta=independent_remainder_bound()

    def test_every_complex_gram_entry_agrees_exactly(self):
        g,o=self.gram,self.original
        self.assertEqual(g[0][0],(o['diag0'],F(0)))
        self.assertEqual(g[1][1],(o['diag1'],F(0)))
        self.assertEqual(g[0][1],(o['cross_re'],o['cross_im']))
        self.assertEqual(g[1][0],(o['cross_re'],-o['cross_im']))

    def test_alternative_remainder_telescoping_preserves_refined_bound(self):
        eta=self.eta
        self.assertGreater(eta,0)
        self.assertLess(eta,F(1,10**11))
        g=self.gram
        self.assertLess(g[0][0][0],F(168294,10**6))
        self.assertLess(g[1][1][0],F(168294,10**6))
        self.assertLess(g[0][1][0]**2+g[0][1][1]**2,F(1071,10**6)**2)
        squared=(F(168294,10**6)+F(1071,10**6)+4*eta+2*eta**2)/F(9978,10000)
        self.assertLess(squared,F(412,1000)**2)
        lo,hi=pi_enclosure()
        self.assertLess(F(314,100),lo)
        self.assertLess(hi,F(22,7))

    def test_argument_reduced_overlap_upper_bound(self):
        bound=independent_overlap_bound()
        self.assertLess(bound,F(2176356,10**9))
        self.assertLess(bound,F(11,5000))
        value=abs(120*(-888*math.sin(15)-180*math.cos(15))/30**5)
        self.assertGreater(float(bound),value)
        self.assertLess(float(bound)-value,1e-8)
        self.assertEqual(self.certificate['amplitude'],F(12463,76440))

    def test_conditional_cursor_error_budget(self):
        bound=conditional_cursor_bounds()
        self.assertLess(bound['system_error'], F(15644,10**6))
        self.assertLess(bound['pulse_error'], F(2514,10**6))
        self.assertLess(bound['total_amplitude_upper'], F(1821,100000))
        self.assertLess(bound['probability_upper'], F(332,10**6))

    def test_simple_polynomial_kernel_moments_and_conjugation(self):
        # K(t,s)=t-s on f(s)=s produces the constant -1/12.
        result=action([ZERO,ONE],[ZERO,ONE])
        self.assertEqual(result,[(F(-1,12),F(0)),ZERO])
        self.assertEqual(integral_monomial(2),F(1,12))
        i=(F(0),F(1))
        self.assertEqual(inner([i],[ONE]),(F(0),F(-1)))
        self.assertEqual(inner([ONE],[i]),i)

if __name__ == '__main__': unittest.main()
