#!/usr/bin/env python3
import cmath
import itertools
import math
import random
import unittest
from fractions import Fraction

import phase_observation_preference_gate as gate


class PhaseObservationTests(unittest.TestCase):
    def test_binary_exact_law_and_intervention(self):
        states = list(itertools.product((-1, 1), repeat=3))
        w = {s: Fraction(1, 2**gate.cost(s)) for s in states}
        z = sum(w.values())
        p = {s: w[s]/z for s in states}
        self.assertEqual(z, Fraction(13, 4))
        self.assertEqual([sum(p[s]*s[i]*s[j] for s in states)
                          for i,j in gate.PAIRS], [Fraction(-3, 13)]*3)
        for v in itertools.product((-1, 1), repeat=2):
            self.assertEqual(w[(1,)+v]/sum(w[s] for s in states if s[0] == 1),
                             p[(1,)+v]/sum(p[s] for s in states if s[0] == 1))
        self.assertEqual(sum(p[s] for s in states if s[1:] == (1,1)), Fraction(5,26))

    def test_holonomy_bound_for_common_weighted_samples(self):
        rng = random.Random(731)
        for _ in range(300):
            samples = [[rng.uniform(-math.pi, math.pi) for _ in range(3)]
                       for _ in range(rng.randint(2, 25))]
            weights = [rng.random() for _ in samples]
            z = sum(weights)
            cs = [sum(w*cmath.exp(1j*(p[i]-p[j])) for w,p in zip(weights,samples))/z
                  for i,j in gate.PAIRS]
            u = math.prod(c/abs(c) for c in cs)
            lhs = abs(1-u)
            rhs = sum(math.sqrt(2*max(0,1-abs(c))) for c in cs)
            self.assertLessEqual(lhs, rhs + 1e-12)

    def test_antiphase_energy_identity(self):
        rng = random.Random(7)
        for _ in range(100):
            p = [rng.uniform(-math.pi,math.pi) for _ in range(3)]
            energy = sum(1+math.cos(p[i]-p[j]) for i,j in gate.PAIRS)
            identity = 1.5 + abs(sum(cmath.exp(1j*x) for x in p))**2/2
            self.assertAlmostEqual(energy, identity, places=12)


if __name__ == '__main__':
    unittest.main()
