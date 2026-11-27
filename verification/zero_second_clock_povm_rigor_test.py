"""Controls for semibounded clock POVM, tail, and centered clock smearing."""
import math
import unittest
from fractions import Fraction as F
from scipy.integrate import quad

from verification.zero_two_window_independent_gram import pi_enclosure
from verification.zero_cursor_domain_instrument_review_test import conditioned_clock_bound


def rational_tail_bound():
    # Y=25*pi/2 - 0.255, pi in (3.14, 22/7).
    lo,hi=pi_enclosure()
    if not F(314,100)<lo<hi<F(22,7): raise ArithmeticError('pi enclosure')
    y=F(7799,200)  # 38.995 < Y
    p=F(22,7)
    if not y > p/2: raise ArithmeticError('tail denominator')
    return p/(3*y**3*(1-(p/(2*y))**2)**2)*(F(1,2)+F(3,2*y))


def refined_clock_comparison():
    # Existing bound uses omega*sigma and tau=0.0000177. Replace only these
    # by the centered second-moment estimate and new tail upper bound.
    omega=F(3251,1000);sigma=F(316,10**6)
    return (conditioned_clock_bound()-omega*sigma+omega**2*sigma**2
            -F(177,10**7)+F(955,10**8))


def compact_packet_overlap(u):
    u=abs(u)
    if u>=2:return 0.
    return (1-u/2)*math.cos(math.pi*u/2)+math.sin(math.pi*u/2)/math.pi


class SecondClockPovmRigorTests(unittest.TestCase):
    def test_rational_tail_and_improved_channel_budget(self):
        tail=rational_tail_bound()
        self.assertLess(tail,F(955,10**8))
        self.assertLess(F(332,10**6)+F(955,10**8),F(3416,10**7))
        bound=refined_clock_comparison()
        self.assertLess(bound,F(3777,100000))

    def test_oscillatory_tail_vs_numerical_integral(self):
        y=12.5*math.pi-.255
        f=lambda x:math.pi*math.cos(x)**2/(x*x-(math.pi/2)**2)**2
        partial=quad(f,y,500,limit=1000,epsabs=1e-13)[0]
        # Beyond 500, the original absolute-cosine bound is a remainder.
        remaining=math.pi/(3*500**3*(1-(math.pi/1000)**2)**2)
        self.assertLess(partial+remaining,float(rational_tail_bound()))

    def test_covariant_weak_bin_twirl_for_exponential_clock(self):
        # psi(k)=sqrt(2)e^-k, whose time density is 1/[pi*(1+r²)].
        width=.7
        def g(t):
            return (math.atan(width/2-t)-math.atan(-width/2-t))/math.pi
        total=quad(g,-math.inf,math.inf,epsabs=1e-10)[0]
        self.assertAlmostEqual(total,width,places=10)
        # e^(iKt) shifts the density to r-t, not r+t.
        self.assertGreater(1/(math.pi*(1+(2-2)**2)),1/(math.pi*(1+(2+2)**2)))

    def test_finite_bin_compression_is_not_a_projection(self):
        # W psi(r)=1/(sqrt(pi)*(1+i r)); truncate to B=[-1,1].
        # A nonzero negative-frequency Fourier component proves this compact
        # truncation leaves the positive-frequency subspace. This is a
        # numerical control of the analytic argument in the report.
        k=-.5
        func=lambda r: complex(math.cos(k*r),math.sin(k*r))/(1+1j*r)
        real=quad(lambda r:func(r).real,-1,1)[0]
        imag=quad(lambda r:func(r).imag,-1,1)[0]
        self.assertGreater(abs(complex(real,imag)/(math.pi*math.sqrt(2))),.1)

    def test_exact_clock_packet_autocorrelation_control(self):
        for u in (0.,.4,1.,1.4,2.,2.2):
            numerical=quad(lambda x:math.cos(math.pi*x/2)*math.cos(math.pi*(x+u)/2),
                           -1,1-u)[0] if u<2 else 0.
            self.assertAlmostEqual(numerical,compact_packet_overlap(u),places=12)
        self.assertAlmostEqual(compact_packet_overlap(1),1/math.pi,places=14)
        self.assertEqual(compact_packet_overlap(2),0.)
        # Finite bin multiplies the characteristic by sinc(delta*ell/2).
        z=.25
        self.assertLess(compact_packet_overlap(1)*math.sin(z)/z,1/math.pi)

    def test_centered_second_order_bound_and_biased_control(self):
        # Qubit Omega=diag(-1,1), input |+>, symmetric reading shifts ±s.
        # Trace distance to the sharp output is (1-cos(2s))/2 <= s².
        for s in (.01,.1,.4):
            distance=(1-math.cos(2*s))/2
            self.assertLessEqual(distance,s*s)
        # For an uncentered single shift, distance is |sin(s)| ~ s;
        # the quadratic centered estimate cannot be used indiscriminately.
        s=.01
        self.assertGreater(abs(math.sin(s)),s*s)

if __name__=='__main__':unittest.main()
