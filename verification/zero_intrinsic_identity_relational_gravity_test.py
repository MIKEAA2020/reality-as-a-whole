"""One compact two-scalar gravity model, with clock-relative distinctions.

Exact rational checks of the specified classical minisuperspace equations.
The zero constraint is not proven to be actual cosmic energy. Scalar signs,
observers, and model readouts are not evidence of subjects or experience.
"""
from fractions import Fraction as F
from itertools import product
import math
import unittest

K=F(6)


def constraint(a,pa,pf,pc):
    return -K*pa**2/(12*a)+(pf**2+pc**2)/(2*a**3)


def derivatives(a,pa,pf,pc):
    return (K*pa**2/(12*a**2)-3*(pf**2+pc**2)/(2*a**4),
            -K*pa/(6*a),pf/a**3,pc/a**3)


def alpha(a,pa,pf):
    return -K*a*pa/(6*pf)


def chi_at(phi,chi,pf,pc,tau):
    return chi+pc*(tau-phi)/pf


def target(phi,chi,pf,pc,tau,ref):
    return int(chi_at(phi,chi,pf,pc,tau)>=ref)


def bracket_alpha_C(a,pa,pf,pc):
    dCda,dCdpa,_,_=derivatives(a,pa,pf,pc)
    # ∂alpha/∂a ∂C/∂pa − ∂alpha/∂pa ∂C/∂a;
    # ∂C/∂phi=0, so ∂alpha/∂pφ has no contribution.
    return (-K*pa/(6*pf))*dCdpa-(-K*a/(6*pf))*dCda


def bracket_chi_at_C(a,pa,pf,pc):
    # C is independent of φ,χ; only coordinate derivatives contribute.
    _,_,dCdpf,dCdpc=derivatives(a,pa,pf,pc)
    return (-pc/pf)*dCdpf+dCdpc


class RelationalGravityIdentityTests(unittest.TestCase):
    def test_constraint_and_positive_density_on_exact_two_scalar_states(self):
        # κ=6 and (pφ,pχ)=(3,4); |a p_a|=5.
        for a,branch in product((F(1,2),F(1),F(2)),(-1,1)):
            pa=branch*F(5)/a
            grav=-K*pa**2/(12*a)
            matter=(F(3)**2+F(4)**2)/(2*a**3)
            rho=matter/a**3
            self.assertEqual(constraint(a,pa,F(3),F(4)),0)
            self.assertEqual(grav,-matter)
            self.assertGreater(rho,0)
            hubble2=(K*pa/(6*a**2))**2
            self.assertEqual(hubble2,K*rho/3)

    def test_relational_field_observable_has_zero_bracket_even_off_shell(self):
        for a,pa,pf,pc in product((F(1),F(2)),(F(-5),F(0),F(3)),
                                  (F(-3),F(2)),(F(-4),F(0),F(4))):
            self.assertEqual(bracket_chi_at_C(a,pa,pf,pc),0)

    def test_alpha_is_constant_on_shell_and_nontrivial_off_shell(self):
        for a,pa,pf,pc in product((F(1),F(2)),(F(-5),F(0),F(3)),
                                  (F(-3),F(2)),(F(-4),F(0),F(4))):
            c=constraint(a,pa,pf,pc)
            self.assertEqual(bracket_alpha_C(a,pa,pf,pc),-K*c/(2*pf))
            if c==0: self.assertEqual(bracket_alpha_C(a,pa,pf,pc),0)
        self.assertNotEqual(bracket_alpha_C(F(1),F(0),F(3),F(4)),0)

    def test_gauge_flow_leaves_clock_relative_reading_invariant(self):
        # Exact finite evolution in the branch, as a function of Δφ.
        # χ'=χ+(pχ/pφ) Δφ, pφ,pχ constant; a,p_a vary but cancel.
        for phi,chi,delta,tau in product((F(0),F(1)),(F(-1),F(2)),
                                         (F(-2),F(1,3)),(F(-1),F(2))):
            old=chi_at(phi,chi,F(3),F(4),tau)
            new=chi_at(phi+delta,chi+F(4,3)*delta,F(3),F(4),tau)
            self.assertEqual(old,new)
            self.assertEqual(int(old>=0),int(new>=0))

    def test_expanding_solution_and_two_distinct_supported_histories(self):
        # At φ=1: a=1, pa=-5, pφ=3, pχ=4, reference χ=0.
        a,pa,pf,pc=F(1),F(-5),F(3),F(4)
        self.assertEqual(constraint(a,pa,pf,pc),0)
        self.assertEqual(alpha(a,pa,pf),F(5,3))
        self.assertEqual((pf**2+pc**2)/(2*a**6),F(25,2))
        self.assertEqual((-K*pa/(6*a))/(pf/a**3),F(5,3))
        self.assertAlmostEqual(math.exp(float(-alpha(a,pa,pf))),math.exp(-5/3))
        results=[]
        for chi in (F(1,2),F(2)):
            x0=chi_at(F(1),chi,pf,pc,F(0))
            x1=chi_at(F(1),chi,pf,pc,F(1))
            q0=target(F(1),chi,pf,pc,F(0),F(0))
            q1=target(F(1),chi,pf,pc,F(1),F(0))
            results.append((x0,x1,q0,q1,(1-q0)*q1))
        self.assertEqual(results,[(F(-5,6),F(1,2),0,1,1),
                                  (F(2,3),F(2),1,1,0)])

    def test_common_field_and_reference_shift_is_a_redescription_of_threshold(self):
        for chi,ref,shift in product((F(-1),F(0),F(2)),(F(-2),F(0),F(3)),
                                     (F(-5),F(0),F(7))):
            q=target(F(1),chi,F(3),F(4),F(0),ref)
            self.assertEqual(q,target(F(1),chi+shift,F(3),F(4),F(0),ref+shift))
        # Holding the physical reference fixed while shifting χ changes q.
        self.assertNotEqual(target(F(1),F(0),F(3),F(4),F(1),F(1)),
                            target(F(1),F(2),F(3),F(4),F(1),F(1)))

    def test_clock_reference_shift_if_comparison_time_is_shifted_too(self):
        for phi,tau,offset in product((F(0),F(1)),(F(-1),F(2)),(F(-3),F(3))):
            self.assertEqual(chi_at(phi,F(2),F(3),F(4),tau),
                             chi_at(phi+offset,F(2),F(3),F(4),tau+offset))


if __name__=='__main__': unittest.main()
