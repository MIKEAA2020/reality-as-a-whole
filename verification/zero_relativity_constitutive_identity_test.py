"""Relativistic geometry as a constitutive analogy, not a foundation proof."""
from fractions import Fraction as F
from itertools import product
import unittest
import sympy as sp

from verification.zero_joint_quality_incidence_root import R,quality,twin_vectors,weight
from verification.zero_echo_quality_bridge_discrimination import structural_value


class RelativityConstitutiveIdentityTests(unittest.TestCase):
    def test_worldtube_and_simultaneous_endpoint_events(self):
        # Units c=1. The rod is at rest at x'=0,L0; S' moves at beta in S.
        beta=sp.symbols('beta',real=True)
        L0=sp.symbols('L0',positive=True)
        t=sp.symbols('t',real=True)
        inv_gamma=sp.sqrt(1-beta**2)
        gamma=1/inv_gamma
        boost=lambda time,x:(sp.simplify(gamma*(time-beta*x)),
                            sp.simplify(gamma*(x-beta*time)))
        left=boost(t,beta*t)
        right=boost(t,beta*t+L0*inv_gamma)
        self.assertEqual(left[1],0)
        self.assertEqual(right[1],L0)
        self.assertEqual(sp.simplify(right[0]-left[0]),-beta*L0)
        delta_t_prime=sp.simplify(right[0]-left[0])
        delta_x_prime=sp.simplify(right[1]-left[1])
        # Same two events have invariant separation L0²(1-beta²);
        # the proper length uses a different, S'-simultaneous event pair.
        interval_prime=sp.simplify(delta_x_prime**2-delta_t_prime**2)
        self.assertEqual(interval_prime,sp.simplify(L0**2*(1-beta**2)))
        proper_interval=L0**2
        self.assertNotEqual(sp.simplify(proper_interval-interval_prime),0)
        self.assertEqual(sp.simplify((right[0]-left[0]).subs(beta,0)),0)

    def test_longitudinal_and_transverse_distances_and_sign(self):
        for b in (F(3,5),F(-3,5)):
            beta=sp.Rational(b.numerator,b.denominator)
            inv_gamma=sp.sqrt(1-beta**2)
            self.assertEqual(inv_gamma,sp.Rational(4,5))
            # Simultaneous S separation (ct,x,y,z) of fixed rest-x endpoints.
            d=sp.Matrix([0,inv_gamma,0,0])
            g=1/inv_gamma
            transform=sp.Matrix([[g,-g*beta,0,0],[-g*beta,g,0,0],
                                 [0,0,1,0],[0,0,0,1]])
            eta=sp.diag(-1,1,1,1)
            self.assertEqual(sp.simplify(transform.T*eta*transform),eta)
            dp=transform*d
            self.assertEqual(dp[1],1)
            self.assertEqual(dp[0],-beta)
            self.assertEqual((dp.T*eta*dp)[0],sp.Rational(16,25))
            # A purely transverse endpoint separation at equal times remains 1.
            transverse=sp.Matrix([0,0,1,0])
            self.assertEqual(transform*transverse,transverse)

    def test_same_echo_support_has_identities_and_unfixed_quality_rules(self):
        negative=F(0)
        for i,s in product(range(4),(1,-1)):
            n,k=quality(i,s)
            self.assertEqual(n*k,R[i])
            a,b=twin_vectors(i,s)
            self.assertEqual(tuple(x+y for x,y in zip(a,b)),(0,0))
            p=structural_value(i,s,'pointer')
            q=structural_value(i,s,'symmetric')
            if R[i]==1:self.assertEqual(p,q)
            else:
                self.assertNotEqual(p,0)
                self.assertEqual(q,0)
                negative+=weight(i,s)
        self.assertEqual(negative,F(1,2))
        # R and the zero pair are model identities on this support. Neither
        # mathematically identifies either proposed scalar with feeling.

if __name__=='__main__':unittest.main()
