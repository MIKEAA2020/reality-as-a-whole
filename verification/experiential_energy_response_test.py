#!/usr/bin/env python3
"""Canonical response controls; no claim of actual experiential identity."""
from fractions import Fraction as F
from math import exp, log, sqrt
import unittest


def canonical(energies, beta):
    raw = [exp(-beta * e) for e in energies]
    z = sum(raw)
    return [x/z for x in raw]


def moments(p, energies):
    mean = sum(w*e for w, e in zip(p, energies))
    variance = sum(w*(e-mean)**2 for w, e in zip(p, energies))
    return mean, variance


class EnergyResponseTests(unittest.TestCase):
    def test_exact_positive_energy_signed_response(self):
        p = list(map(F, [F(4, 7), F(2, 7), F(1, 7)]))
        energy = list(map(F, (1, 2, 3)))
        mean, variance = moments(p, energy)
        score = [mean-e for e in energy]
        self.assertEqual(mean, F(11, 7))
        self.assertEqual(variance, F(26, 49))
        self.assertEqual(score, [F(4, 7), F(-3, 7), F(-10, 7)])
        self.assertEqual(sum(w*s for w, s in zip(p, score)), 0)
        self.assertTrue(all(e > 0 for e in energy))
        self.assertTrue(any(s > 0 for s in score) and any(s < 0 for s in score))
        self.assertNotEqual(sorted(score), sorted(-s for s in score))
        u = [float(s)/sqrt(float(variance)) for s in score]
        self.assertAlmostEqual(sum(float(w)*x*x for w, x in zip(p, u)), 1)
        for got, want in zip(canonical([1, 2, 3], log(2)), p):
            self.assertAlmostEqual(got, float(want))

    def test_score_is_log_probability_derivative(self):
        energy, beta, h = [1.0, 2.0, 3.0], log(2), 1e-5
        p = canonical(energy, beta)
        mean, _ = moments(p, energy)
        plus, minus = canonical(energy, beta+h), canonical(energy, beta-h)
        for i, e in enumerate(energy):
            numerical = (log(plus[i])-log(minus[i]))/(2*h)
            self.assertAlmostEqual(numerical, mean-e, places=8)

    def test_shift_and_unit_rescaling(self):
        energy, beta = [1.0, 2.0, 3.0], log(2)
        p = canonical(energy, beta)
        mu, var = moments(p, energy)
        normalized = [(mu-e)/sqrt(var) for e in energy]
        for es, bs in [([e+17 for e in energy], beta), ([7*e for e in energy], beta/7)]:
            ps = canonical(es, bs)
            ms, vs = moments(ps, es)
            for a, b in zip(p, ps):
                self.assertAlmostEqual(a, b)
            for a, b in zip(normalized, [(ms-e)/sqrt(vs) for e in es]):
                self.assertAlmostEqual(a, b)

    def test_single_actual_outcome_need_not_have_zero_score(self):
        p, energy = [F(4, 7), F(2, 7), F(1, 7)], list(map(F, (1, 2, 3)))
        mean, _ = moments(p, energy)
        score = [mean-e for e in energy]
        self.assertEqual(sum(w*s for w, s in zip(p, score)), 0)
        self.assertEqual(score[0], F(4, 7))
        self.assertNotEqual(score[0], 0)

    def test_uniform_scores_can_be_reverse_engineered(self):
        target = [F(2), F(-1), F(-1)]
        p = [F(1, 3)]*3
        energy = [F(4)-s for s in target]
        mean, variance = moments(p, energy)
        self.assertTrue(all(e > 0 for e in energy))
        self.assertEqual([mean-e for e in energy], target)
        self.assertEqual(variance, 2)

    def test_equal_energy_predicts_equal_score(self):
        p, energy = [F(1, 3)]*3, list(map(F, (1, 4, 4)))
        mean, variance = moments(p, energy)
        score = [mean-e for e in energy]
        self.assertGreater(variance, 0)
        self.assertEqual(score[1], score[2])

    def test_constant_energy_has_no_normalized_score(self):
        p, energy = [F(1, 2), F(1, 2)], [F(3), F(3)]
        _, variance = moments(p, energy)
        self.assertEqual(variance, 0)
        with self.assertRaises(ZeroDivisionError):
            _ = F(0) / sqrt(float(variance))


if __name__ == '__main__':
    unittest.main()
