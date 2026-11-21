import math
import unittest
from ottinger_scalar_regulator_gate import sum_cutoff


class ScalarRegulatorTest(unittest.TestCase):
    def test_zero_external_momentum_cancels(self):
        value = sum_cutoff(2, 0.4, (0, 0, 0))
        self.assertEqual(value['time_cutoff'], 0)
        self.assertEqual(value['gap'], 0)

    def test_inversion_symmetry(self):
        plus = sum_cutoff(2, 0.5, (1, 0, 0))
        minus = sum_cutoff(2, 0.5, (-1, 0, 0))
        for key in plus:
            self.assertAlmostEqual(plus[key], minus[key], places=11)

    def test_zero_epsilon_same_finite_sum(self):
        value = sum_cutoff(2, 0.0)
        self.assertEqual(value['gap'], 0)
        self.assertEqual(value['time_cutoff'], value['common_exponential'])

    def test_gap_and_mode_sum_growth(self):
        small = sum_cutoff(2, 0.5)
        larger = sum_cutoff(4, 0.5)
        self.assertGreater(small['gap'], 0)
        self.assertGreater(larger['gap'], small['gap'])
        self.assertTrue(math.isclose(larger['common_exponential']-larger['time_cutoff'],
                                     larger['gap'], abs_tol=1e-11))

    def test_radial_cancellation(self):
        # Equation (7), after r=t*tan(theta), with Simpson quadrature.
        def simpson(f):
            n = 1024
            h = math.pi/(2*n)
            return h/3*(f(0)+f(math.pi/2)
                        + 4*sum(f(i*h) for i in range(1, n, 2))
                        + 2*sum(f(i*h) for i in range(2, n, 2)))
        x2 = 4*math.pi/3*simpson(lambda a: math.sin(a)**4)
        t2 = 4*math.pi*simpson(lambda a: math.sin(a)**2*math.cos(a)**2)
        self.assertAlmostEqual(x2, math.pi**2/4, places=12)
        self.assertAlmostEqual(t2, math.pi**2/4, places=12)

    def test_shell_lower_bound_example(self):
        c = 2*math.sqrt(13)+7
        lower_bound = math.exp(-c)/(91*c*c*2**6)
        # eps=1, h=m=1: the shell p_i,q_i∈{1,2} fits inside N=4.
        self.assertGreater(sum_cutoff(4, 1.0)['gap'], lower_bound)

    def test_time_integral_representation(self):
        # Independent numerical Laplace integration of the finite N=1 sums.
        from itertools import product
        pts = list(product(range(-1, 2), repeat=3))
        terms = {0: [], 1: []}
        for p in pts:
            wp = math.sqrt(1+sum(x*x for x in p))
            for q in pts:
                wq = math.sqrt(1+sum(x*x for x in q))
                for target in (0, 1):
                    r = (target-p[0]-q[0], -p[1]-q[1], -p[2]-q[2])
                    if max(map(abs, r)) > 1:
                        continue
                    wr = math.sqrt(1+sum(x*x for x in r))
                    terms[target].append((wp+wq+wr, 1/(wp*wq*wr)))
        def integrand(t):
            a0 = sum(weight*math.exp(-omega*t) for omega, weight in terms[0])
            ak = sum(weight*math.exp(-omega*t) for omega, weight in terms[1])
            return a0-ak-t*t*a0/2
        start, end, n = 0.5, 14.5, 1400
        step = (end-start)/n
        numeric = step/3*(integrand(start)+integrand(end)
            + 4*sum(integrand(start+i*step) for i in range(1, n, 2))
            + 2*sum(integrand(start+i*step) for i in range(2, n, 2)))
        self.assertAlmostEqual(numeric, sum_cutoff(1, start)['time_cutoff'], places=7)

    def test_invalid(self):
        for n, eps, m in ((-1, 1, 1), (1, -1, 1), (1, 1, 0)):
            with self.assertRaises(ValueError):
                sum_cutoff(n, eps, mass=m)


if __name__ == '__main__':
    unittest.main()
