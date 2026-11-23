"""Analytical controls, not empirical validation of experiential valence."""
import math
import unittest


def pulse_value(t, b, duration=1.0, tau=1.0, a=1.0):
    if t < 0 or duration <= 0 or tau <= 0:
        raise ValueError("nonnegative time and positive duration/tau required")
    if t < duration:
        return -a + b * (1 - math.exp(-t / tau))
    return b * (1 - math.exp(-duration / tau)) * math.exp(-(t - duration) / tau)


def pulse_area_to(t, b, duration=1.0, tau=1.0, a=1.0):
    if t < 0 or duration <= 0 or tau <= 0:
        raise ValueError("nonnegative time and positive duration/tau required")
    during = min(t, duration)
    area = (b - a) * during - b * tau * (1 - math.exp(-during / tau))
    if t > duration:
        area += (b * (1 - math.exp(-duration / tau)) * tau
                 * (1 - math.exp(-(t - duration) / tau)))
    return area


class OpponentControls(unittest.TestCase):
    def test_three_gains_produce_opposite_signs_but_different_areas(self):
        for b, area in ((0.5, -0.5), (1.0, 0.0), (1.5, 0.5)):
            with self.subTest(b=b):
                for t in (0, 0.25, 0.5, 0.999999):
                    self.assertLess(pulse_value(t, b), 0)
                self.assertGreater(pulse_value(1.0, b), 0)
                self.assertGreater(pulse_value(3.0, b), 0)
                self.assertAlmostEqual(pulse_area_to(100, b), area)

    def test_incomplete_tail_is_not_complete_integral(self):
        self.assertLess(pulse_area_to(1, 1), 0)
        self.assertLess(pulse_area_to(2, 1), 0)
        self.assertAlmostEqual(pulse_area_to(100, 1), 0)

    def test_general_duration_and_time_constant(self):
        for duration, tau, a, b in ((2, 0.5, 3, 1), (0.2, 5, 1, 2), (5, 2, 1, 1)):
            with self.subTest(duration=duration, tau=tau):
                expected = (b-a) * duration
                self.assertAlmostEqual(pulse_area_to(duration + 100*tau, b, duration, tau, a), expected)
                eps = 1e-5 * min(duration, tau)
                for t in (duration/2, duration+tau):
                    numerical = (pulse_area_to(t+eps, b, duration, tau, a)
                                 - pulse_area_to(t-eps, b, duration, tau, a))/(2*eps)
                    self.assertAlmostEqual(numerical, pulse_value(t, b, duration, tau, a), places=8)

    def test_relaxation_is_independent_of_zero_integral(self):
        for b in (0.5, 1, 1.5):
            self.assertAlmostEqual(pulse_value(100, b), 0)
        self.assertNotAlmostEqual(pulse_area_to(100, 0.5), 0)

    def test_ordinal_recoding_preserves_order_but_not_sum(self):
        x = (2, -1, -1)
        f = lambda v: v if v >= 0 else 2*v
        y = tuple(map(f, x))
        self.assertEqual(sum(x), 0)
        self.assertEqual(sum(y), -2)
        for left in x:
            for right in x:
                self.assertEqual(left < right, f(left) < f(right))

    def test_zero_perturbation_area_does_not_make_baseline_zero(self):
        baseline, t = -0.2, 20
        perturbation = pulse_area_to(t, 1)
        self.assertLess(abs(perturbation), 1e-7)
        self.assertAlmostEqual(baseline*t + perturbation, -4, places=6)


if __name__ == '__main__':
    unittest.main()
