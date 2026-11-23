"""Checks bounded classical evolution, not experiential identity or quantum gravity."""
import math
import unittest

from verification import evolve_covariant_zero_initial_data as ev


class CovariantZeroEvolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs = [ev.evolve(n, end=.25, kappa=.02) for n in (32, 64, 128)]

    def test_fourth_order_constraints_converge_on_refinement(self):
        for key in ('ham_rms', 'mom_rms', 'gauss_rms', 'clock_gradient_rms'):
            errors = [run[0]['final'][key] for run in self.runs]
            with self.subTest(key=key, errors=errors):
                self.assertGreater(errors[0]/errors[1], 10)
                self.assertGreater(errors[1]/errors[2], 10)

    def test_local_charge_and_clock_change_with_neutral_total(self):
        run, _ = self.runs[-1]
        self.assertGreater(run['initial']['proper_charge_density_at_x0'], .99)
        self.assertLess(run['final']['proper_charge_density_at_x0'], .7)
        self.assertGreater(run['final']['clock_at_x0'], .4)
        self.assertGreater(run['sampled_min_clock_timelike_margin'], 0)
        self.assertGreater(run['sampled_min_marker_clock_rate_per_proper_time'], 0)
        self.assertLess(run['sampled_max_abs_total_charge'], 1e-10)

    def test_local_changing_field_is_grid_convergent(self):
        values = [r[0]['final']['proper_charge_density_at_x0'] for r in self.runs]
        self.assertGreater(abs(values[0]-values[1])/abs(values[1]-values[2]), 10)

    def test_uniform_lapse_redescription_is_same_evolution(self):
        a, state_a = ev.evolve(32, end=.25, kappa=.02, lapse=1)
        b, state_b = ev.evolve(32, end=.125, kappa=.02, lapse=2)
        self.assertEqual(a['steps'], b['steps'])
        for name in ev.NAMES:
            with self.subTest(field=name):
                self.assertLess(max(abs(x-y) for x, y in zip(state_a[name], state_b[name])), 1e-13)

    def test_initial_charge_evolution_matches_matter_equations(self):
        n, kappa = 128, .02
        h = 2*math.pi/n
        s = ev.initial(n, kappa)
        ds = ev.rhs(s, h, kappa)
        for i in (0, 7, 32, 64, 96):
            qdot = (ds['p2'][i]*s['c1'][i]+s['p2'][i]*ds['c1'][i]
                    -ds['p1'][i]*s['c2'][i]-s['p1'][i]*ds['c2'][i])
            self.assertAlmostEqual(qdot, -math.cos(i*h), delta=5e-7)

    def test_charge_conjugation_reverses_charge_without_geometry(self):
        n, h, kappa = 32, 2*math.pi/32, .02
        s = ev.initial(n, kappa)
        s = ev.step(s, .03, h, kappa)
        odd = {'c2', 'p2', 'ax', 'E'}
        conjugate = {name: [(-x if name in odd else x) for x in values]
                     for name, values in s.items()}
        a, b = ev.rhs(s, h, kappa), ev.rhs(conjugate, h, kappa)
        for name in ev.NAMES:
            with self.subTest(field=name):
                sign = -1 if name in odd else 1
                self.assertLess(max(abs(y-sign*x) for x, y in zip(a[name], b[name])), 1e-13)
        da, db = ev.diagnostics(s, h, kappa), ev.diagnostics(conjugate, h, kappa)
        self.assertAlmostEqual(da['charge_at_x0'], -db['charge_at_x0'])
        self.assertAlmostEqual(da['ham_rms'], db['ham_rms'])

    def test_matched_clock_lapse_redescription(self):
        a, sa = ev.evolve_to_clock(32, target=.3, lapse=1)
        b, sb = ev.evolve_to_clock(32, target=.3, lapse=2)
        self.assertAlmostEqual(a['coordinate_time'], 2*b['coordinate_time'], delta=1e-14)
        for name in ev.NAMES:
            self.assertLess(max(abs(x-y) for x,y in zip(sa[name],sb[name])), 1e-13)

    def test_known_flat_flrw_free_scalar_solution(self):
        # Independently known homogeneous solution in synchronous time.
        n, kappa, end, steps = 32, .06, .5, 100
        h=2*math.pi/n
        s={name:[0.0]*n for name in ev.NAMES}
        h0=math.sqrt(kappa/6)
        s['kx']=[-h0]*n
        s['ky']=[-h0]*n
        s['pT']=[1.0]*n
        for _ in range(steps):
            s=ev.step(s, end/steps, h, kappa)
        a=(1+3*h0*end)**(1/3)
        t_clock=math.log(1+3*h0*end)/(3*h0)
        self.assertAlmostEqual(math.exp(s['u'][0]), a, delta=1e-11)
        self.assertAlmostEqual(math.exp(s['v'][0]), a, delta=1e-11)
        self.assertAlmostEqual(s['T'][0], t_clock, delta=1e-11)
        self.assertLess(ev.diagnostics(s, h, kappa)['ham_rms'], 1e-11)

    def test_same_clock_gravity_and_fixed_metric_predictions_differ(self):
        gravity, _ = ev.evolve_to_clock(64, target=1, kappa=.02)
        fixed, _ = ev.evolve_to_clock(64, target=1, kappa=0)
        g, f = gravity['diagnostics'], fixed['diagnostics']
        self.assertAlmostEqual(g['clock_at_x0'], 1, delta=1e-10)
        self.assertAlmostEqual(f['clock_at_x0'], 1, delta=1e-10)
        self.assertAlmostEqual(f['area_factor_at_x0'], 1, delta=1e-13)
        self.assertGreater(g['area_factor_at_x0'], 1.1)
        self.assertGreater(abs(g['proper_charge_density_at_x0']
                               -f['proper_charge_density_at_x0']), .1)
        self.assertLess(abs(g['total_charge']), 1e-10)
        self.assertLess(abs(f['total_charge']), 1e-10)


if __name__ == '__main__':
    unittest.main()
