"""Algebraic controls for the zero-energy research review; not a cosmology fit."""
from fractions import Fraction as F
import math
import unittest


class ZeroEnergyResearchTests(unittest.TestCase):
    def test_newtonian_kinetic_and_binding_ratio(self):
        # G=M=R=1; impose H²=2GM/(ΩR³).
        for omega in (F(1, 2), F(1), F(2)):
            kinetic = F(3, 10) * 2 / omega
            binding = -F(3, 5)
            self.assertEqual(binding / kinetic, -omega)
            self.assertEqual(kinetic + binding, kinetic * (1 - omega))

    def test_newtonian_thirty_percent_is_not_rest_energy_cancellation(self):
        mc2 = F(1)
        kinetic, binding = F(3, 10), -F(3, 10)
        self.assertEqual(kinetic + binding, 0)
        self.assertEqual(mc2 + kinetic + binding, mc2)

    def test_flat_dust_lambda_constraint_at_three_scale_factors(self):
        for a in (F(1, 2), F(1), F(2)):
            matter, vacuum = F(1), F(7, 10) * a**3
            h2 = (1 / a**3 + F(7, 10)) / 3
            gravity = -3 * a**3 * h2
            self.assertEqual(matter + vacuum + gravity, 0)

    def test_cosmological_constant_is_not_fixed_by_zero_constraint(self):
        a = F(3, 2)
        for cosmological_constant in (F(0), F(1, 10), F(7, 10), F(10)):
            h2 = (1 / a**3 + cosmological_constant) / 3
            self.assertEqual(-3*a**3*h2 + 1 + cosmological_constant*a**3, 0)

    def test_positive_misner_sharp_energy_with_zero_constraint(self):
        # κ=1 means G=1/(8π). Spatially flat FLRW, areal sphere R=1.
        grav_constant, radius = 1/(8*math.pi), 1.0
        for a in (.5, 1., 2.):
            rho = a**-3 + .7
            h2 = rho / 3
            constraint = -3*a**3*h2 + a**3*rho
            energy_geometry = h2*radius**3/(2*grav_constant)
            energy_density = 4*math.pi*radius**3*rho/3
            self.assertAlmostEqual(constraint, 0)
            self.assertGreater(energy_geometry, 0)
            self.assertAlmostEqual(energy_geometry, energy_density)

    def test_local_flrw_continuity_for_dust_radiation_and_vacuum(self):
        # Independently differentiate E(a)=ρ₀ a^(-3w), then compare -p dV/da.
        a, eps, rho0 = 2.0, 1e-5, 3.0
        for w in (0.0, 1/3, -1.0):
            energy = lambda x: rho0 * x**(-3*w)
            derivative = (energy(a+eps)-energy(a-eps))/(2*eps)
            rho = rho0 * a**(-3*(1+w))
            self.assertAlmostEqual(derivative, -3*w*rho*a*a, delta=1e-8)


if __name__ == '__main__':
    unittest.main()
