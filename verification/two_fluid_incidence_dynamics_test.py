import math
import unittest
import numpy as np
from verification import two_fluid_incidence_dynamics as model


class TwoFluidIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs=[model.run(n) for n in (64,128,256)]

    def test_initial_gauss_and_analytic_asymmetric_incidence(self):
        last=self.runs[-1]['initial']
        self.assertLess(last['gauss_rms'],1e-12)
        self.assertAlmostEqual(last['incidence'],4*math.pi,places=11)
        self.assertAlmostEqual(last['negative_species_fraction'],.5,places=12)
        expected=.5-.5/math.pi
        self.assertLess(abs(last['negative_fraction_interpolated']-expected),4e-5)
        self.assertAlmostEqual(last['naive_weighted_total'],.1*math.pi,places=12)

    def test_conservation_and_positive_densities(self):
        for r in self.runs:
            before,after=r['initial'],r['final']
            self.assertLess(abs(after['net_charge']),1e-12)
            self.assertLess(after['gauss_rms'],1e-12)
            self.assertAlmostEqual(after['incidence'],before['incidence'],places=11)
            self.assertGreater(after['min_species_density'],.4)
            self.assertLess(after['max_abs_velocity'],.04)
            self.assertAlmostEqual(after['signed_total'],after['net_charge'],places=12)

    def test_distinct_incidence_interpretations(self):
        end=self.runs[-1]['final']
        self.assertAlmostEqual(end['negative_species_fraction'],.5,places=12)
        self.assertLess(end['negative_fraction_interpolated'],.46)
        self.assertGreater(end['negative_fraction_interpolated'],.42)
        self.assertGreater(abs(end['naive_weighted_total']),.04)

    def test_smooth_diagnostic_fourth_order(self):
        a,b,c=[r['final']['naive_weighted_total'] for r in self.runs]
        self.assertGreater(abs((a-b)/(b-c)),12)
        self.assertLess(abs((a-b)/(b-c)),20)
        drifts=[abs(r['final']['electrostatic_plus_kinetic_energy']-
                    r['initial']['electrostatic_plus_kinetic_energy']) for r in self.runs]
        self.assertGreater(drifts[0]/drifts[1],12)
        self.assertGreater(drifts[1]/drifts[2],12)
        residuals=[r['final']['valence_transport_residual_rms'] for r in self.runs]
        self.assertGreater(residuals[0]/residuals[1],12)
        self.assertGreater(residuals[1]/residuals[2],12)

    def test_small_amplitude_plasma_oscillation(self):
        n=256; amplitude=0.0001
        y=model.evolve(n, amplitude=amplitude, modulation=0)['final']
        x=2*np.pi*(np.arange(n)+.5)/n
        relative_amplitude=2*np.mean((y[0]-y[1])*np.cos(2*x))/amplitude
        self.assertAlmostEqual(relative_amplitude,math.cos(math.sqrt(2)),places=7)

    def test_charge_conjugation_of_equations(self):
        y=model.initial(64); dx=2*math.pi/64
        z=y[[1,0,3,2,4]].copy(); z[4]*=-1
        fy=model.rhs(y,dx); fz=model.rhs(z,dx)
        mapped=fy[[1,0,3,2,4]].copy(); mapped[4]*=-1
        np.testing.assert_allclose(fz,mapped,atol=1e-14)

    def test_partition_interpolation_converges_initial(self):
        target=.5-.5/math.pi
        errors=[abs(r['initial']['negative_fraction_interpolated']-target) for r in self.runs]
        self.assertGreater(errors[0]/errors[1],3.5)
        self.assertGreater(errors[1]/errors[2],3.5)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError): model.initial(8)
        with self.assertRaises(ValueError): model.initial(64,amplitude=2)
        with self.assertRaises(ValueError): model.evolve(64,mass=0)


if __name__=='__main__': unittest.main()
