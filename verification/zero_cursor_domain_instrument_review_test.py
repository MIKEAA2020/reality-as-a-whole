"""Exact controls for cursor Sobolev constants and instrument bounds."""
import unittest
from fractions import Fraction as F
from verification.zero_two_window_independent_gram import pi_enclosure


def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def derivative(a):
    return [i*a[i] for i in range(1,len(a))] or [F(0)]


def integral_minus1_to1(a):
    return sum((2*c/F(i+1) for i,c in enumerate(a) if i%2==0),F(0))


def constants():
    pi_upper=F(3927,1250)
    sqrt3_upper=F(1732051,10**6)
    invsqrt3_upper=F(577351,10**6)
    sqrt315_upper=F(561249,100000)
    a=b=F(1,10**6)
    kappa=pi_upper/2
    a1=kappa*F(15,8)/b
    a2=kappa*10*invsqrt3_upper/(b*b)+a1*a1
    k2=sqrt315_upper/(a*a)+2*sqrt3_upper/a*a1+a2
    return pi_upper,k2


def full_state_bound():
    pi,k2=constants()
    c=F(412,1000)/(2*F(13,10))
    T=pi/100
    ds=400*c*T*T
    pulse=pi*800*F(1,10**6)
    disp=T*k2/(2*10**16)
    env=F(2,10**31) # > sqrt(2)*10^(-31)
    return ds+pulse+disp+env


def conditioned_clock_bound():
    pi,k2=constants()
    c=F(412,1000)/(2*F(13,10))
    T_end=pi/200+F(1,500000)
    r=(T_end+pi/100)/2
    sigma=F(316,10**6)
    variance=pi*pi/(4*5000**2)+F(1,10000)**2/12
    assert variance<sigma*sigma
    omega=F(3251,1000)
    assert omega*omega>F(49,6)+F(36,5)/3
    pulse=pi*800*F(1,10**6)
    return (400*c*(r*r+sigma*sigma)+pulse+k2*(r+sigma)/(2*10**16)
            +F(2,10**31)+omega*sigma+F(177,10**7))


class CursorDomainInstrumentReviewTests(unittest.TestCase):
    def test_exact_packet_and_derivative_integrals(self):
        envelope=[F(1),F(0),F(-2),F(0),F(1)]
        first=derivative(envelope);second=derivative(first)
        c2=F(315,256)
        self.assertEqual(c2*integral_minus1_to1(multiply(envelope,envelope)),1)
        self.assertEqual(c2*integral_minus1_to1(multiply(first,first)),3)
        self.assertEqual(c2*integral_minus1_to1(multiply(second,second)),F(63,2))
        # The zero extension has continuous value and first derivative at ±1.
        for x in (-1,1):
            self.assertEqual(sum(c*x**i for i,c in enumerate(envelope)),0)
            self.assertEqual(sum(c*x**i for i,c in enumerate(first)),0)

    def test_exact_profile_total_variation(self):
        # h(u) = 15/16*(1-u²)², monotone on each side of zero.
        h=[F(15,16),F(0),F(-30,16),F(0),F(15,16)]
        hp=derivative(h)
        self.assertEqual(2*h[0],F(15,8))  # L1 norm of h'
        # h'' changes sign at ±u with u²=1/3; h'(u)=−(5/2)u.
        root_squared=F(1,3)
        slope_coeff=hp[1]+hp[3]*root_squared
        self.assertEqual(slope_coeff,F(-5,2))
        # Total variation of h' is 4*|h'(u)|; its squared norm is 100/3.
        self.assertEqual((4*slope_coeff)**2*root_squared,F(100,3))

    def test_rational_radical_upper_bounds_and_cursor_dispersion(self):
        self.assertGreater(F(1732051,10**6)**2,3)
        self.assertGreater(F(577351,10**6)**2,F(1,3))
        self.assertGreater(F(561249,100000)**2,F(63,2))
        pi,k2=constants()
        lo,hi=pi_enclosure()
        self.assertGreater(lo,3)
        self.assertLess(hi,pi)
        self.assertLess(k2,F(3356*10**10))
        self.assertLess((pi/100)*k2/(2*10**16),F(528,10**7))

    def test_full_recorded_instrument_budget_and_backaction(self):
        delta=full_state_bound()
        self.assertLess(delta,F(6513,100000))
        self.assertGreater(F(1,2)-delta,F(43487,100000))
        self.assertLess(2*delta,F(13026,100000))

    def test_clock_smearing_bound_is_conditional_on_old_tail_estimate(self):
        self.assertLess(conditioned_clock_bound(),F(388,10000))

    def test_sharp_conditional_branch_bound(self):
        # Two-outcome classical recorded channels, with subnormalized branch
        # state (1/4,0) vs (1/5,1/20), same complementary branch (3/4).
        ideal=[F(1,4),F(0),F(3,4),F(0)]
        actual=[F(1,5),F(1,20),F(3,4),F(0)]
        d=sum(abs(x-y) for x,y in zip(ideal,actual))/2
        q=sum(ideal[:2]);p=sum(actual[:2])
        conditional=sum(abs(actual[i]/p-ideal[i]/q) for i in (0,1))/2
        self.assertEqual((p,q,d),(F(1,4),F(1,4),F(1,20)))
        self.assertEqual(conditional,d/q)  # demonstrates sharpness
        # q=δ permits a zero-probability actual branch; no normalization.
        q=F(1,10)
        ideal=[q,F(0),1-q,F(0)]
        actual=[F(0),F(0),F(1),F(0)]
        d=sum(abs(x-y) for x,y in zip(ideal,actual))/2
        self.assertEqual(d,q)
        self.assertEqual(sum(actual[:2]),0)

if __name__=='__main__':unittest.main()
