import math
import unittest
from itertools import product
import numpy as np
from ottinger_scalar_universal_gap import a0_fft, gap_fft
from ottinger_scalar_regulator_gate import sum_cutoff


class UniversalGapTest(unittest.TestCase):
    def test_fft_against_independent_finite_sum(self):
        n, t = 2, 0.7
        points = list(product(range(-n, n+1), repeat=3))
        total = 0.0
        for p in points:
            wp = math.sqrt(1+sum(x*x for x in p))
            for q in points:
                r = tuple(-a-b for a, b in zip(p, q))
                if any(abs(x) > n for x in r):
                    continue
                wq = math.sqrt(1+sum(x*x for x in q))
                wr = math.sqrt(1+sum(x*x for x in r))
                total += math.exp(-t*(wp+wq+wr))/(wp*wq*wr)
        self.assertAlmostEqual(a0_fft(n, t), total, places=11)

    def test_transformed_integral_matches_closed_form(self):
        for n in (1, 2, 4):
            for eps in (0.5, 1.0):
                self.assertAlmostEqual(gap_fft(n, eps, points=48),
                                       sum_cutoff(n, eps)['gap'], places=8)

    def test_universal_integral_numerical(self):
        # Integrate the two transformed radial integrals independently.
        x, w = np.polynomial.legendre.leggauss(32)
        theta = (x+1)*math.pi/4
        radial = sum(w*np.sin(theta)**2*np.cos(theta)**2)*math.pi/4
        z = (x+1)/2
        regulator = sum(w*(1-z/2))/2
        self.assertAlmostEqual(4*math.pi*radial, math.pi**2/4, places=13)
        self.assertAlmostEqual(regulator, 3/4, places=14)
        c = 1/(2*math.pi**2)
        self.assertAlmostEqual(regulator*c**3*4*math.pi*radial,
                               3/(128*math.pi**4), places=16)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            a0_fft(1, 0)
        with self.assertRaises(ValueError):
            gap_fft(1, 0.0)


if __name__ == '__main__':
    unittest.main()
