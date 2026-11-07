#!/usr/bin/env python3
"""Unregulated one-branch FRW clock likelihood; see FRW_INTERNAL_POVM.md.
Requires NumPy and SciPy. Quadrature is numerical evidence, not a novelty proof.
"""
import json
import unittest
from pathlib import Path

import numpy as np
from scipy.integrate import quad, quad_vec

KAPPA = 1/np.sqrt(6)
WIDTH = 0.8
BETA = 1.3


def psi(p):
    return 2*WIDTH**1.5*p*np.exp(-WIDTH*p)


def f(x):
    return 2*WIDTH**1.5 / np.sqrt(2*np.pi) / (WIDTH-1j*x)**2


def rho(x):
    return 2*WIDTH**3/(np.pi*(WIDTH**2+x**2)**2)


def cdf(x):
    return 0.5+(np.arctan(x/WIDTH)+WIDTH*x/(WIDTH**2+x**2))/np.pi


def scalar_frame(q, x):
    return psi(q/KAPPA)*np.exp(1j*q*x/KAPPA)/np.sqrt(KAPPA)


def scalar_phi_density(phi, x):
    return KAPPA*rho(x-KAPPA*phi)


def fourier_positive(x):
    ans, err = quad_vec(lambda p: psi(p)*np.exp(1j*p*x)/np.sqrt(2*np.pi),
                        0, np.inf, epsabs=1e-11, epsrel=1e-11)
    return ans


def fourier_scalar(phi, x):
    ans, err = quad_vec(lambda q: scalar_frame(q, x)*np.exp(-1j*q*phi)/np.sqrt(2*np.pi),
                        0, np.inf, epsabs=1e-11, epsrel=1e-11)
    return ans


class FRWInternalPOVM(unittest.TestCase):
    def test_fourier_and_normalizations(self):
        self.assertAlmostEqual(quad(lambda p: abs(psi(p))**2, 0, np.inf)[0], 1, places=11)
        self.assertAlmostEqual(quad(rho, -np.inf, np.inf)[0], 1, places=11)
        for x in [-2.2, -0.4, 0, 0.7, 1.9]:
            np.testing.assert_allclose(fourier_positive(x), f(x), atol=2e-10)
            self.assertAlmostEqual(abs(f(x))**2, rho(x), places=12)

    def test_frame_change_and_density_jacobian(self):
        for x in [-1.2, 0, 1.1]:
            self.assertAlmostEqual(quad(lambda q: abs(scalar_frame(q, x))**2, 0, np.inf)[0], 1, places=10)
            self.assertAlmostEqual(quad(lambda phi: scalar_phi_density(phi, x), -np.inf, np.inf)[0], 1, places=10)
            for phi in [-2.1, 0, 1.5]:
                scalar = fourier_scalar(phi, x)
                np.testing.assert_allclose(scalar, np.sqrt(KAPPA)*f(x-KAPPA*phi), atol=2e-10)
                self.assertAlmostEqual(abs(scalar)**2, KAPPA*rho(x-KAPPA*phi), places=10)

    def test_interval_and_relational_flow(self):
        lo, hi = -0.3, 1.4
        for phi in [-1.1, 0, 2.4]:
            integrated = quad(lambda x: rho(x-KAPPA*phi), lo, hi, epsabs=1e-12)[0]
            expected = cdf(hi-KAPPA*phi)-cdf(lo-KAPPA*phi)
            self.assertAlmostEqual(integrated, expected, places=11)
        # sigma_s^T = exp(-i βsH) A exp(i βsH) = alpha_{-βs}.
        # Its interval translates B+κβs, in the specified convention.
        nodes, weights = np.polynomial.legendre.leggauss(24)
        for s in [-1.0, 0.2, 1.3]:
            translate = KAPPA*BETA*s
            shifted = cdf(hi+translate)-cdf(lo+translate)
            rel = cdf(hi-KAPPA*(-BETA*s))-cdf(lo-KAPPA*(-BETA*s))
            # Compute U(βs)†ψ in momentum space, Fourier transform it and
            # integrate the result over the original interval independently.
            numeric = 0.0
            for node, weight in zip(nodes, weights):
                x = (lo+hi)/2 + (hi-lo)*node/2
                amp, _ = quad_vec(lambda p: psi(p)*np.exp(1j*p*x)*
                                  np.exp(1j*BETA*s*KAPPA*p)/np.sqrt(2*np.pi),
                                  0, np.inf, epsabs=1e-10, epsrel=1e-10)
                numeric += (hi-lo)*weight/2*abs(amp)**2
            self.assertAlmostEqual(shifted, rel, places=12)
            self.assertAlmostEqual(numeric, shifted, places=9)

    def test_finite_moments_and_constraint(self):
        variance_x = quad(lambda x: x*x*rho(x), -np.inf, np.inf)[0]
        self.assertAlmostEqual(variance_x, WIDTH**2, places=10)
        x = 1.0
        mean_phi = quad(lambda z: z*scalar_phi_density(z, x), -np.inf, np.inf)[0]
        var_phi = quad(lambda z: (z-x/KAPPA)**2*scalar_phi_density(z, x), -np.inf, np.inf)[0]
        self.assertAlmostEqual(mean_phi, x/KAPPA, places=9)
        self.assertAlmostEqual(var_phi, WIDTH**2/KAPPA**2, places=9)
        # Finite differences directly test (-i ∂_φ - i κ ∂_x) f(x-κφ)=0.
        step = 1e-5
        for x, phi in [(0.3, 0.7), (-0.6, 2.0), (1.2, -0.4)]:
            wave = lambda xx, tt: f(xx-KAPPA*tt)
            dx = (wave(x+step, phi)-wave(x-step, phi))/(2*step)
            dt = (wave(x, phi+step)-wave(x, phi-step))/(2*step)
            self.assertLess(abs(dt+KAPPA*dx), 1e-9)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(FRWInternalPOVM))
    data = {
        'model': 'positive-momentum scalar-clock FRW branch; unregulated reduced Hilbert space',
        'kappa': KAPPA, 'wavepacket_width_alpha': WIDTH,
        'geometric_clock_scalar_standard_deviation': WIDTH/KAPPA,
        'tests_run': result.testsRun, 'failures': len(result.failures),
        'errors': len(result.errors), 'all_pass': result.wasSuccessful(),
        'scope': 'Tests one normalized wavepacket and frame map, not full GR or modular-state identification.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(data, indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
