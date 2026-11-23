#!/usr/bin/env python3
"""Damped-response controls, not measurements of experience or cosmology."""
from fractions import Fraction as F
from math import cos, exp, sin, sqrt
import unittest


def step_critical(t):
    return 0.0 if t < 0 else 1-(1+t)*exp(-t)


def step_relative(t):
    if t < 0:
        return 0.0
    w = sqrt(2)
    return (1-exp(-t)*(cos(w*t)+sin(w*t)/w))/3


def pulse(step, t, duration=1.0):
    return step(t)-step(t-duration)


def simpson(f, end, n=20000):
    if n % 2:
        raise ValueError('even number of intervals required')
    h = end/n
    return (f(0)+f(end)+4*sum(f(i*h) for i in range(1, n, 2))
            +2*sum(f(i*h) for i in range(2, n, 2)))*h/3


def integrated_two_site(x1, x2):
    """Inverse of I+L for kappa=1 and a single edge."""
    y1, y2 = (2*x1+x2)/3, (x1+2*x2)/3
    return (y1, y2), (x1-y1, x2-y2)


class CausalRelaxationTests(unittest.TestCase):
    def test_critical_damping_solution_and_local_equation(self):
        for t in (0.0, 0.2, 0.5, 1.0, 2.0):
            y = 1-(1+t)*exp(-t)
            yp = t*exp(-t)
            ypp = (1-t)*exp(-t)
            q = 1-y
            self.assertAlmostEqual(q, ypp+2*yp)
            self.assertGreater(q, 0)

    def test_finite_pulse_equal_positive_and_negative_areas(self):
        for duration in (0.2, 1.0, 3.0):
            expected = 2-(duration+2)*exp(-duration)
            positive = simpson(lambda t: (1+t)*exp(-t), duration, 2000)
            tail = simpson(lambda u: ((1+u)*exp(-u)
                                       -(1+u+duration)*exp(-(u+duration))), 40.0, 20000)
            self.assertGreater(expected, 0)
            self.assertAlmostEqual(positive, expected, delta=1e-8)
            self.assertAlmostEqual(tail, expected, delta=1e-8)
            for u in (0.0, 0.5, 2.0, 10.0):
                self.assertGreater(pulse(step_critical, duration+u, duration), 0)

    def test_persistent_input_has_nonzero_complete_integral(self):
        total = simpson(lambda t: (1+t)*exp(-t), 40.0, 20000)
        self.assertAlmostEqual(total, 2, delta=1e-8)
        # At late time y tends to 1 and y' to zero, yielding boundary 2.
        self.assertAlmostEqual(step_critical(40.0), 1, delta=1e-12)

    def test_two_site_areas_exact(self):
        y, q = integrated_two_site(F(1), F(0))
        self.assertEqual(y, (F(2, 3), F(1, 3)))
        self.assertEqual(q, (F(1, 3), F(-1, 3)))
        self.assertEqual(sum(q), 0)
        for a in map(F, range(-2, 3)):
            for b in map(F, range(-2, 3)):
                y, q = integrated_two_site(a, b)
                self.assertEqual((2*y[0]-y[1], -y[0]+2*y[1]), (a, b))
                self.assertEqual(sum(q), 0)

    def test_two_site_time_domain_matches_exact_areas(self):
        def y1(t):
            return (pulse(step_critical, t)+pulse(step_relative, t))/2
        def y2(t):
            return (pulse(step_critical, t)-pulse(step_relative, t))/2
        area1 = simpson(y1, 40.0)
        area2 = simpson(y2, 40.0)
        self.assertAlmostEqual(area1, 2/3, delta=1e-7)
        self.assertAlmostEqual(area2, 1/3, delta=1e-7)
        q1, q2 = 1-area1, -area2  # unit area input to site 1, none to site 2
        self.assertAlmostEqual(q1, 1/3, delta=1e-7)
        self.assertAlmostEqual(q2, -1/3, delta=1e-7)
        self.assertAlmostEqual(q1+q2, 0, delta=1e-7)

    def test_single_pulse_cutoff_misses_after_response(self):
        t = 1.0
        at_cutoff = t*exp(-t) + 2*step_critical(t)
        self.assertAlmostEqual(at_cutoff, 2-3*exp(-1))
        self.assertGreater(at_cutoff, 0)
        self.assertAlmostEqual(pulse(step_critical, 40.0), 0, delta=1e-12)


if __name__ == '__main__':
    unittest.main()
