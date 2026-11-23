"""Controls for adaptation/area identities; no empirical or ontological claims."""
import math
import unittest


def midpoint(f, start, end, n=10000):
    dt = (end-start)/n
    return sum(f(start+(i+0.5)*dt) for i in range(n))*dt


def unit_step_response(t, tau, a=1, b=1):
    return 0.0 if t < 0 else -a+b*(1-math.exp(-t/tau))


def pulse_response(t, tau, duration, a=1, b=1):
    return unit_step_response(t, tau, a, b)-unit_step_response(t-duration, tau, a, b)


def rprime(t, tau=1.0, duration=1.0, amp=1.0):
    if t < 0:
        return 0.0
    if t < duration:
        return amp*math.exp(-t/tau)/tau
    return -amp*(1-math.exp(-duration/tau))*math.exp(-(t-duration)/tau)/tau


def nonlinear(t, tau=1.0, duration=1.0, c=0.5, amp=1.0):
    p = rprime(t, tau, duration, amp)
    return -p+c*tau*p*p


class AdaptationBalanceTests(unittest.TestCase):
    def test_step_adapts_only_for_equal_gains(self):
        for tau in (0.2, 1, 4):
            self.assertAlmostEqual(unit_step_response(1000, tau, 2, 2), 0)
            self.assertAlmostEqual(unit_step_response(1000, tau, 2, 3), 1)

    def test_pulse_zero_for_multiple_shapes_and_mixtures(self):
        # Three different rectangular pulses, including overlap and signed input;
        # a stable mixture of two exponentially decaying response components.
        intervals = [(0, 1, 1), (0.5, 3, -0.4), (4, 5.2, 0.7)]
        def output(t):
            return sum(amp*(0.3*pulse_response(t-start, 0.5, end-start)
                            +0.7*pulse_response(t-start, 2, end-start))
                       for start, end, amp in intervals)
        breaks = (0, 0.5, 1, 3, 4, 5.2, 80)
        area = sum(midpoint(output, a, b, 5000) for a, b in zip(breaks, breaks[1:]))
        self.assertAlmostEqual(area, 0, delta=5e-6)

    def test_partial_adaptation_pulse_has_nonzero_area(self):
        a, b, duration, tau = 1, 0.6, 2, 1.3
        area = (midpoint(lambda t: pulse_response(t, tau, duration, a, b), 0, duration)
                + midpoint(lambda t: pulse_response(t, tau, duration, a, b), duration, 60))
        self.assertAlmostEqual(area, (b-a)*duration, delta=1e-6)
        self.assertAlmostEqual(unit_step_response(100, tau, a, b), b-a)

    def test_persistent_step_output_area_is_nonzero(self):
        tau, a = 2.0, 3.0
        area = midpoint(lambda t: unit_step_response(t, tau, a, a), 0, 80)
        self.assertAlmostEqual(area, -a*tau, delta=1e-5)
        self.assertAlmostEqual(unit_step_response(80, tau, a, a), 0, delta=1e-14)

    def test_nonlinear_perfect_step_adaptation(self):
        for tau in (0.5, 2.0):
            for amp in (0.25, 1, 3):
                t = 100*tau
                p = amp*math.exp(-t/tau)/tau
                v = -p+0.5*tau*p*p
                self.assertAlmostEqual(v, 0, delta=1e-35)

    def test_nonlinear_pulse_reverses_and_has_nonzero_area(self):
        for tau, duration, c in ((1, 1, 0.5), (0.5, 2, 0.2), (2, 0.3, 0.9)):
            with self.subTest(tau=tau, duration=duration, c=c):
                for t in (0, duration/2, duration*0.999):
                    self.assertLess(nonlinear(t, tau, duration, c), 0)
                self.assertGreater(nonlinear(duration, tau, duration, c), 0)
                area = (midpoint(lambda t: nonlinear(t, tau, duration, c), 0, duration)
                        + midpoint(lambda t: nonlinear(t, tau, duration, c), duration, duration+60*tau, 30000))
                self.assertAlmostEqual(area, c*(1-math.exp(-duration/tau)), delta=2e-6)

    def test_nonlinear_excess_scales_quadratically(self):
        tau, duration, c = 1, 1, 0.5
        def area(amp):
            return (midpoint(lambda t: nonlinear(t, tau, duration, c, amp), 0, duration)
                    + midpoint(lambda t: nonlinear(t, tau, duration, c, amp), duration, 60))
        self.assertAlmostEqual(area(0.25), area(1)*0.25**2, delta=1e-6)

    def test_baseline_is_distinct_from_zero_perturbation_area(self):
        baseline, observation_time = -0.1, 50
        area = (midpoint(lambda t: pulse_response(t, 1, 1), 0, 1)
                + midpoint(lambda t: pulse_response(t, 1, 1), 1, observation_time))
        self.assertAlmostEqual(area, 0, delta=1e-6)
        self.assertAlmostEqual(area+baseline*observation_time, -5, delta=1e-6)


if __name__ == '__main__':
    unittest.main()
