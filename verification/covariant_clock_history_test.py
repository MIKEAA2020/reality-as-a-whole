"""Tests for covariant current/clock accounting, not tests of felt experience."""
import math
import unittest
from verification import covariant_clock_history_balance as balance


class ClockHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs = [balance.clock_slices(n) for n in (32, 64, 128)]

    def test_full_evolution_clock_slice_balance_and_local_differences(self):
        for run in self.runs:
            for sl in run['slices']:
                self.assertLess(abs(sl['charge']), 1e-10)
                self.assertLess(sl['min_local_slice_flux_density'], -.25)
                self.assertGreater(sl['max_local_slice_flux_density'], .25)
                self.assertGreater(sl['sampled_min_clock_scale'], 1.2)
                self.assertGreater(sl['tilt_flux_rms'], .02)

    def test_weighted_incidence_changes_balance(self):
        for sl in self.runs[-1]['slices']:
            self.assertGreater(sl['weighted_incidence_integrand'], 15)
            self.assertLess(abs(sl['charge']), 1e-10)

    def test_slice_observable_converges(self):
        # Linear clock-crossing interpolation is second order, not fourth.
        values = [r['slices'][0]['weighted_incidence_integrand'] for r in self.runs]
        self.assertLess(abs(values[2]-values[1]), abs(values[1]-values[0]))

    def test_invalid_clock_slab_rejected(self):
        with self.assertRaises(ValueError):
            balance.clock_slices(32, targets=(.01,))
        with self.assertRaises(ValueError):
            balance.clock_slices(32, targets=(.6,.3))

    def test_moving_current_tilt_term_cannot_be_dropped(self):
        # J=(cos(x-t),cos(x-t)); T=t+ε cos(x). Exact flux is
        # d/dx sin(x-τ+ε cos(x)), so its periodic integral vanishes.
        n, epsilon, tau = 4096, .4, .7
        h=2*math.pi/n
        q=[]; flux=[]
        for i in range(n):
            x=i*h
            phase=x-tau+epsilon*math.cos(x)
            value=math.cos(phase)
            q.append(value)
            flux.append(value*(1-epsilon*math.sin(x)))
        self.assertAlmostEqual(h*sum(flux), 0, delta=1e-12)
        self.assertAlmostEqual(h*sum(q), .79346444561624, delta=1e-11)

    def test_local_clock_rate_is_necessary_in_generic_example(self):
        # Flat cylinder: J=(cos(2x),0), T=t+ε sin x. The current
        # is conserved and neutral, but ∫ρ_T differs from ∫sρ_T.
        n, epsilon = 8192, .6
        h=2*math.pi/n
        raw, scaled, weighted=0.0,0.0,0.0
        for i in range(n):
            x=i*h
            q=math.cos(2*x)
            s=math.sqrt(1-epsilon**2*math.cos(x)**2)
            rho=q/s
            raw+=rho
            scaled+=s*rho
            weighted+=(1+.5*math.cos(2*x))*s*rho
        self.assertAlmostEqual(h*raw, .38966053204873, delta=1e-10)
        self.assertAlmostEqual(h*scaled, 0, delta=1e-12)
        self.assertAlmostEqual(h*weighted, .5*math.pi, delta=1e-12)

    def test_changing_clock_rate_changes_intensity_not_sign(self):
        # τ=f(T)=T+T² for T>0 has positive rate: J·dτ=f' J·dT.
        for t in (.2,.8,2):
            for jdot in (-2.,1.):
                self.assertGreater((1+2*t)*jdot*jdot, 0)
                self.assertNotEqual((1+2*t)*jdot, jdot)


if __name__ == '__main__':
    unittest.main()
