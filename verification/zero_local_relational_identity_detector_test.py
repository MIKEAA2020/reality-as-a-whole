"""Controls for a localized relational detector in the existing GR-matter model.

These exact algebra checks assume the action and short-time response derived in
RELATIONAL_MATTER_DETECTOR_GRAVITY.md. They do not solve Einstein evolution,
construct a durable record or physical reference, or demonstrate experience.
"""
from fractions import Fraction as F
from itertools import product
import unittest


def hconstraint(psi, psidd, alpha, eps, c, sign, f=F(1,2), tau=F(3,2),
                p=F(1), b=F(2), quartic=F(1)):
    """Exact initial Hamiltonian constraint in the original ansatz.

    c=cos(z), psi>0; psi and psidd need not solve the constraint for
    the algebraic equality between opposite preparations to hold.
    """
    signal=sign*eps*b*c
    return (8*psi**(-5)*psidd-F(3,2)*alpha**2+F(3,2)*f**2*psi**(-4)
            +tau**2*psi**(-12)/2+eps**2*p**2*(1+c)**2*psi**(-12)/2
            +eps**2*b**2*(1-c*c)*psi**(-4)/2+quartic*signal**4)


def response(sign, coupling, eps, b, window, c, psi, tau):
    """Interaction-induced relational acceleration at T=0."""
    return -sign*coupling*eps*b*window*c*psi**12/tau**2


def normalized_contrast(sign, field_orientation):
    """Dimensionless calibrated sign: orientation is a proposed reference."""
    return sign*field_orientation


class LocalRelationalIdentityDetectorTests(unittest.TestCase):
    def test_full_initial_constraint_same_for_signal_signs(self):
        for psi,psidd,alpha,eps,c in product((F(1),F(3,2)),(F(-1,3),F(0)),
                                             (F(-1),F(1)),(F(1,10),F(1,50)),
                                             (F(-1),F(0),F(1,2),F(1))):
            self.assertEqual(hconstraint(psi,psidd,alpha,eps,c,1),
                             hconstraint(psi,psidd,alpha,eps,c,-1))

    def test_interaction_acceleration_differences(self):
        for eps,window,c,psi in product((F(1,100),F(1,10)),(F(0),F(1),F(1,3)),
                                        (F(-1),F(0),F(1,2),F(1)),(F(1),F(3,2))):
            plus=response(1,F(1),eps,F(2),window,c,psi,F(3,2))
            minus=response(-1,F(1),eps,F(2),window,c,psi,F(3,2))
            self.assertEqual(plus,-minus)
            self.assertEqual(plus-minus,-F(16,9)*eps*window*c*psi**12)
            if window==0 or c==0: self.assertEqual(plus-minus,0)
        # psi=1 is the zeroth-order background, not the exact perturbed metric.
        self.assertEqual(response(1,F(1),F(1,100),F(2),F(1),F(1),F(1),F(3,2)),F(-2,225))
        self.assertEqual(response(1,F(1),F(1,100),F(2),F(1),F(1),F(1),F(3,2))-
                         response(-1,F(1),F(1,100),F(2),F(1),F(1),F(1),F(3,2)),F(-4,225))

    def test_locality_and_turning_off_coupling_controls(self):
        for sign in (-1,1):
            self.assertEqual(response(sign,F(0),F(1,10),F(2),F(1),F(1),F(1),F(3,2)),0)
            self.assertEqual(response(sign,F(1),F(1,10),F(2),F(0),F(1),F(1),F(3,2)),0)
            self.assertNotEqual(response(sign,F(1),F(1,10),F(2),F(1),F(1),F(1),F(3,2)),0)

    def test_signal_only_flip_not_the_simultaneous_symmetry_for_nonzero_pointer_momentum(self):
        # Data tuple (Phi,Pphi,chi,Pchi); pchi at z=0 is nonzero.
        x=(F(1,5),F(0),F(0),F(1,5))
        flip_signal=(-x[0],-x[1],x[2],x[3])
        symmetry=tuple(-v for v in x)
        self.assertNotEqual(flip_signal,symmetry)
        self.assertEqual(flip_signal[3],x[3])
        self.assertNotEqual(symmetry[3],x[3])
        self.assertEqual(tuple(-v for v in symmetry),x)

    def test_calibration_covariance_is_not_a_built_reference(self):
        for sign,orientation in product((-1,1),repeat=2):
            self.assertEqual(normalized_contrast(sign,orientation),
                             normalized_contrast(-sign,-orientation))
            self.assertEqual(normalized_contrast(-sign,orientation),
                             -normalized_contrast(sign,orientation))

    def test_common_initial_energy_does_not_choose_signal_sign(self):
        # At initial chi=0, signal momentum=0: signal gradient and quartic
        # potential are even under sign reversal. p_chi stays fixed.
        for eps,c,psi in product((F(1,100),F(1,10)),(F(-1),F(0),F(1,2),F(1)),
                                 (F(1),F(2))):
            terms=[]
            for sign in (-1,1):
                potential=(sign*eps*2*c)**4
                gradient=eps**2*F(2)**2*(1-c*c)*psi**(-4)/2
                detector_momentum=eps**2*(1+c)**2*psi**(-12)/2
                terms.append((potential,gradient,detector_momentum))
            self.assertEqual(terms[0],terms[1])


if __name__=='__main__': unittest.main()
