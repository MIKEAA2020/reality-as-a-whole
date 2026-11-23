import math
import unittest
from fractions import Fraction as F
from verification.zero_sphere_asymmetric_closed_exchange import values, midpoint_summary


class AsymmetricClosedExchangeTests(unittest.TestCase):
    def test_completed_square_proves_rest_energy_positive(self):
        # H-U = p^2/2 + (q-q0)^T M(q-q0)/2 + 15/47.
        m=[[F(3,4),F(-1,8)],[F(-1,8),F(63,16)]]
        q0=[F(32,47),F(4,47)]
        self.assertEqual(m[0][0]*m[1][1]-m[0][1]**2,F(47,16))
        self.assertGreater(m[0][0],0)
        self.assertEqual([sum(m[i][j]*q0[j] for j in range(2)) for i in range(2)], [F(1,2),F(1,4)])
        for q1,q2,p1,p2 in [(F(0),F(0),F(0),F(0)),(F(2),F(-3),F(1),F(2))]:
            H=1+(q1*q1+p1*p1)/2+(p2*p2+4*q2*q2)/2
            U=(2+q1+q2/2)**2/8
            x=[q1-q0[0],q2-q0[1]]
            square=sum(x[i]*m[i][j]*x[j] for i in range(2) for j in range(2))/2
            self.assertEqual(H-U,(p1*p1+p2*p2)/2+square+F(15,47))

    def test_exact_extrema_and_unequal_duration(self):
        maxU=values(math.pi/3)[1]
        minU=values(5*math.pi/3)[1]
        self.assertAlmostEqual(maxU-minU,3*math.sqrt(3)/4)
        self.assertGreater(values(math.pi/6)[3],0)
        self.assertLess(values(math.pi/2)[3],0)
        self.assertLess(values(3*math.pi/2)[3],0)
        self.assertGreater(values(11*math.pi/6)[3],0)
        self.assertAlmostEqual(values(0)[1],values(2*math.pi)[1])

    def test_numerical_integral_and_fraction_converge(self):
        r=midpoint_summary(16384)
        self.assertAlmostEqual(r['negative_fraction'],F(2,3),delta=0.0002)
        self.assertAlmostEqual(r['positive_fraction'],F(1,3),delta=0.0002)
        self.assertAlmostEqual(r['positive_exchange'],3*math.sqrt(3)/4,delta=2e-7)
        self.assertAlmostEqual(r['negative_exchange'],-3*math.sqrt(3)/4,delta=2e-7)
        self.assertAlmostEqual(r['sum_exchange'],0,delta=1e-11)
        self.assertLess(r['max_total_error'],1e-12)
        self.assertGreater(r['min_part'],0)
        self.assertGreater(r['min_rest'],F(15,47))

    def test_mean_intensities_match_balance_and_frequencies(self):
        positive_integral=3*math.sqrt(3)/4
        mean_positive=positive_integral/(2*math.pi/3)
        mean_negative=positive_integral/(4*math.pi/3)
        self.assertAlmostEqual(mean_positive,2*mean_negative)
        self.assertAlmostEqual(F(1,3)*mean_positive,F(2,3)*mean_negative)

    def test_complement_energy_has_opposite_exchange(self):
        t=.7; eps=1e-6
        _,_,w1,_=values(t-eps)
        _,_,w2,h=values(t+eps)
        self.assertAlmostEqual((w2-w1)/(2*eps),-values(t)[3],delta=1e-9)


if __name__=='__main__': unittest.main()
