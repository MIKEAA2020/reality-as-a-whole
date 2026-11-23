import math
import unittest
from fractions import Fraction as F


def inner(a,b): return sum(x*y for x,y in zip(a,b))


def primitive_poly(coeff, x):
    return sum((F(c)*x**(i+1)/F(i+1) for i,c in enumerate(coeff)), F(0))


def interval(coeff, lo, hi): return primitive_poly(coeff,hi)-primitive_poly(coeff,lo)


class ZeroPointBlowupTests(unittest.TestCase):
    def test_spherical_shapes_survive_normalization_not_raw_collapse(self):
        n=(1.,0.,0.); m=(0.,1.,0.)
        for r in (1.,.1,.001):
            raw=math.sqrt(sum((r*x-r*y)**2 for x,y in zip(n,m)))
            self.assertAlmostEqual(raw/r,math.sqrt(2))
            self.assertAlmostEqual(raw,math.sqrt(2)*r)
        self.assertEqual(tuple(0*x for x in n),tuple(0*x for x in m))

    def test_joint_rotation_preserves_relational_signed_value(self):
        # A common quarter-turn in three-space, not an external preferred axis.
        R=lambda a:(-a[1],a[0],a[2])
        n=(1.,0.,0.); m=(.6,.8,0.)
        self.assertAlmostEqual(inner(n,m),inner(R(n),R(m)))
        self.assertAlmostEqual(inner(tuple(-x for x in n),m),-inner(n,m))

    def test_isotropic_density_not_sufficient_for_balance(self):
        # Under uniform directions for fixed m, t=n·m is uniform on [-1,1].
        # A jointly rotation-invariant density 1+epsilon*t has mean epsilon/3.
        eps=F(1,2)
        density=[F(1),eps]
        mean=interval([0,*density],F(-1),F(1))/2
        pneg=interval(density,F(-1),F(0))/2
        self.assertEqual(mean,eps/3)
        self.assertEqual(pneg,F(1,2)-eps/4)

    def test_zero_balance_does_not_force_equal_sign_incidence(self):
        # rho(t)=1+t^3-3t/5 is positive on [-1,1].
        density=[F(1),-F(3,5),F(0),F(1)]
        self.assertEqual(interval(density,F(-1),F(1))/2,1)
        self.assertEqual(interval([0,*density],F(-1),F(1))/2,0)
        self.assertEqual(interval(density,F(-1),F(0))/2,F(21,40))
        self.assertGreater(min(1+t**3-F(3,5)*t for t in [F(-1),F(0),F(1)]),0)
        # Interior extrema of t^3 - 3t/5 are ± 2/(5 sqrt 5).
        self.assertGreater(1-2/(5*math.sqrt(5)),0)


if __name__=='__main__': unittest.main()
