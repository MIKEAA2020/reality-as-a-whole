#!/usr/bin/env python3
"""Finite-window stress test for the regulated FRW clock; see accompanying note."""
import json
from pathlib import Path
import unittest

import numpy as np

KAPPA = 1 / np.sqrt(6)
BETA = 2.0
N = 4
LENGTH = 2*np.pi
OMEGA = KAPPA*2*np.pi/LENGTH
ENERGIES = OMEGA*np.arange(1, N+1)
PERIOD = 2*np.pi/OMEGA
P = np.exp(-BETA*ENERGIES)
P /= P.sum()
PSI = np.sqrt(P)
RHO0 = np.outer(PSI, PSI)
TAU = np.diag(P)


def unitary(t, energies=ENERGIES):
    return np.diag(np.exp(-1j*energies*t))


def window_state(width, weights=P, energies=ENERGIES):
    gap = energies[:, None] - energies[None, :]
    return np.sqrt(np.outer(weights, weights))*np.sinc(gap*width/(2*np.pi))


def gaussian_state(width):
    gap = ENERGIES[:, None] - ENERGIES[None, :]
    return np.sqrt(np.outer(P, P))*np.exp(-0.5*(gap*width)**2)


def quadrature_state(width):
    # Independent numerical integration of unitary-conjugated initial state.
    x, w = np.polynomial.legendre.leggauss(100)
    answer = np.zeros((N, N), dtype=complex)
    for xi, wi in zip(x, w):
        u = unitary(xi*width/2)
        answer += wi/2 * (u @ RHO0 @ u.conj().T)
    return answer


def sigma(a, rho, s):
    eig, basis = np.linalg.eigh(rho)
    if eig.min() <= 0:
        raise ValueError('modular state must be faithful')
    v = (basis * np.exp(1j*s*np.log(eig))) @ basis.conj().T
    return v @ a @ v.conj().T


def mismatch(rho, t):
    a_t = unitary(t).conj().T @ rho @ unitary(t)
    return float(np.real(np.trace(rho @ rho) - np.trace(rho @ a_t)))


def pair_bound(width, t):
    return float(2*P[0]*P[1]*np.sinc(OMEGA*width/(2*np.pi))**2*(1-np.cos(OMEGA*t)))


def hs_bound_squared(width):
    delta = ENERGIES[:, None]-ENERGIES[None, :]
    off = ~np.eye(N, dtype=bool)
    return float(np.sum((4*np.outer(P, P)[off]) / ((delta[off]*width)**2)))


class FiniteWindow(unittest.TestCase):
    def test_sinc_against_independent_quadrature(self):
        for fraction in (0.125, 0.25, 0.5, 0.75, 1.0):
            rho = window_state(fraction*PERIOD)
            np.testing.assert_allclose(rho, quadrature_state(fraction*PERIOD), atol=2e-14)
            self.assertGreater(np.linalg.eigvalsh(rho).min(), 0)
            self.assertAlmostEqual(np.trace(rho).real, 1)

    def test_modular_invariance_and_positive_mismatch(self):
        t = np.pi/OMEGA
        for fraction in (0.125, 0.25, 0.5, 0.75):
            width = fraction*PERIOD
            rho = window_state(width).astype(complex)
            for s in (-11, -1.7, 0, 0.8, 7):
                np.testing.assert_allclose(sigma(rho, rho, s), rho, atol=2e-12)
            d = mismatch(rho, t)
            bound = pair_bound(width, t)
            self.assertGreater(bound, 0)
            self.assertGreaterEqual(d + 1e-13, bound)
            gaps = ENERGIES[:, None] - ENERGIES[None, :]
            spectral_d = np.sum(np.abs(rho)**2 * (1-np.cos(gaps*t)))
            np.testing.assert_allclose(d, spectral_d, atol=1e-13)

    def test_period_restores_gibbs_and_error_bound(self):
        np.testing.assert_allclose(window_state(PERIOD), TAU, atol=1e-14)
        for fraction in (0.125, 0.25, 0.5, 0.75, 1.0):
            width = PERIOD*fraction
            hs_error = np.linalg.norm(window_state(width)-TAU, 'fro')**2
            self.assertLessEqual(hs_error, hs_bound_squared(width)+1e-12)
        self.assertAlmostEqual(mismatch(window_state(PERIOD), np.pi/OMEGA), 0, places=13)

    def test_gaussian_window_never_exact_at_finite_width(self):
        t = np.pi/OMEGA
        for ratio in (0.1, 0.25, 0.5, 1.0):
            width = ratio*PERIOD
            rho = gaussian_state(width)
            self.assertGreater(np.linalg.eigvalsh(rho).min(), 0)
            bound = 4*P[0]*P[1]*np.exp(-(OMEGA*width)**2)
            self.assertGreater(bound, 0)
            self.assertGreaterEqual(mismatch(rho, t)+1e-14, bound)
            # Fourier transform of the Gaussian checked via Gauss-Hermite quadrature.
            x, w = np.polynomial.hermite.hermgauss(256)
            quad = np.zeros((N, N), dtype=complex)
            for xi, wi in zip(x, w):
                u = unitary(np.sqrt(2)*width*xi)
                quad += wi/np.sqrt(np.pi) * (u @ RHO0 @ u.conj().T)
            np.testing.assert_allclose(rho, quad, atol=2e-13)

    def test_fixed_window_large_box_does_not_dephase(self):
        width = 3.0
        for length in (1000, 10000):
            energies = KAPPA*2*np.pi/length*np.arange(1, N+1)
            p = np.exp(-BETA*energies); p /= p.sum()
            r = window_state(width, p, energies)
            pure = np.outer(np.sqrt(p), np.sqrt(p))
            self.assertLess(np.linalg.norm(r-pure, 'fro'), 0.0001)
            self.assertGreater(np.linalg.norm(r-np.diag(p), 'fro'), 0.8)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(FiniteWindow))
    t = np.pi/OMEGA
    examples = []
    for frac in (0.125, 0.25, 0.5, 0.75, 1.0):
        width = frac*PERIOD
        rho = window_state(width)
        examples.append({'fraction_of_period': frac, 'width': width,
                         'min_eigenvalue': float(np.linalg.eigvalsh(rho).min()),
                         'witness_mismatch': mismatch(rho, t),
                         'analytic_lower_bound': pair_bound(width, t)})
    output = {'examples': examples, 'beta': BETA, 'omega': OMEGA,
              'tests_run': result.testsRun, 'failures': len(result.failures),
              'errors': len(result.errors), 'all_pass': result.wasSuccessful(),
              'scope': 'Finite regulated, selected-state window model only; no general gravity or novelty claim.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
