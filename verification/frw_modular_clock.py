#!/usr/bin/env python3
"""Finite regulated massless-scalar FRW branch; see FRW_MODULAR_CLOCK.md."""
import json
from pathlib import Path
import unittest

import numpy as np

# 8πG = ħ = 1; finite system and periodic clock regulators are explicit.
KAPPA = 1 / np.sqrt(6)
LENGTH = 2 * np.pi
DELTA = 2 * np.pi / LENGTH
OMEGA = KAPPA * DELTA
N = 4
M = N + 1
BETA = 2.0
ENERGIES = OMEGA * np.arange(1, N + 1)
TIMES = np.arange(M) * (2*np.pi / OMEGA) / M
WEIGHTS = np.exp(-BETA * ENERGIES)
WEIGHTS /= WEIGHTS.sum()
H = np.diag(ENERGIES).astype(complex)
CLOCK_MODES = -np.arange(M)
F = np.exp(1j * np.outer(TIMES * OMEGA, CLOCK_MODES)) / np.sqrt(M)
PC = F @ np.diag(OMEGA * CLOCK_MODES) @ F.conj().T
K = np.kron(PC, np.eye(N)) + np.kron(np.eye(M), H)
K2 = np.kron(PC @ PC, np.eye(N)) - np.kron(np.eye(M), H @ H)


def u(t):
    return np.diag(np.exp(-1j * ENERGIES * t))


def heisenberg(a, t):
    return u(t).conj().T @ a @ u(t)


def modular(a, p, s):
    d = np.diag(np.exp(1j*s*np.log(p)))
    return d @ a @ d.conj().T


def history_map():
    return np.vstack([u(t) for t in TIMES]) / np.sqrt(M)


J = history_map()


def marginal(v):
    return sum(np.outer(b, b.conj()) for b in v.reshape(M, N))


def condition(v, j):
    b = v.reshape(M, N)[j]
    probability = np.vdot(b, b).real
    return probability, np.outer(b, b.conj()) / probability


class ScalarClockFRW(unittest.TestCase):
    def test_clock_fourier_and_constraints(self):
        np.testing.assert_allclose(F.conj().T @ F, np.eye(M), atol=1e-12)
        np.testing.assert_allclose(PC, PC.conj().T, atol=1e-12)
        np.testing.assert_allclose(J.conj().T @ J, np.eye(N), atol=1e-12)
        np.testing.assert_allclose(K @ J, 0, atol=1e-12)
        np.testing.assert_allclose(K2 @ J, 0, atol=1e-12)
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(K)) < 1e-10), N)

    def test_conditional_history_and_reference_marginal(self):
        psi = np.sqrt(WEIGHTS).astype(complex)
        rho0 = np.outer(psi, psi.conj())
        v = J @ psi
        self.assertAlmostEqual(np.vdot(v, v).real, 1.0)
        for j, t in enumerate(TIMES):
            prob, rho = condition(v, j)
            self.assertAlmostEqual(prob, 1/M)
            np.testing.assert_allclose(rho, u(t) @ rho0 @ u(t).conj().T, atol=1e-12)
        np.testing.assert_allclose(marginal(v), np.diag(WEIGHTS), atol=1e-12)
        self.assertGreater(np.linalg.norm(condition(v, 1)[1]-rho0), 0.1)

    def test_relational_modular_agreement_and_dirac_representative(self):
        psi = np.sqrt(WEIGHTS).astype(complex)
        v = J @ psi
        for t in [*TIMES, 0.731, 3.141]:
            for n in range(N):
                for m in range(N):
                    a = np.zeros((N, N), dtype=complex)
                    a[n, m] = 1
                    evolved = heisenberg(a, t)
                    np.testing.assert_allclose(modular(a, WEIGHTS, -t/BETA), evolved, atol=1e-12)
                    observable = J @ evolved @ J.conj().T
                    np.testing.assert_allclose(K @ observable - observable @ K, 0, atol=1e-12)
                    np.testing.assert_allclose(np.vdot(v, observable @ v),
                                               np.vdot(psi, evolved @ psi), atol=1e-12)

    def test_nonthermal_initial_state_not_automatically_modular(self):
        q = np.array([0.4, 0.3, 0.2, 0.1])
        np.testing.assert_allclose(marginal(J @ np.sqrt(q)), np.diag(q), atol=1e-12)
        beta_first = np.log(q[0]/q[1]) / OMEGA
        a = np.zeros((N, N), dtype=complex)
        a[1, 2] = 1
        self.assertGreater(np.linalg.norm(modular(a, q, -1/beta_first) - heisenberg(a, 1)), 0.1)

    def test_box_partition_growth(self):
        # Infinite momentum tower n>=1, with L=2π/Δ; no claim that a finite
        # test proves the noncompact-operator theorem in the document.
        lengths = 2*np.pi * np.array([1, 2, 4, 8, 16], dtype=float)
        x = BETA * KAPPA * 2*np.pi / lengths
        z = 1 / np.expm1(x)
        self.assertTrue(np.all(np.diff(z) > 0))
        self.assertAlmostEqual(z[-1]/lengths[-1], 1/(2*np.pi*BETA*KAPPA), delta=0.005)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ScalarClockFRW))
    output = {
        'model': 'regulated massless-scalar flat FRW branch, periodic log-scale and scalar clock',
        'N_system_modes': N, 'M_clock_readings': M,
        'kappa': KAPPA, 'beta': BETA, 'energies': ENERGIES.tolist(),
        'system_marginal_probabilities': WEIGHTS.tolist(),
        'tests_run': result.testsRun, 'failures': len(result.failures),
        'errors': len(result.errors), 'all_pass': result.wasSuccessful(),
        'scope': 'Regulated minisuperspace calculation only; no full GR, normal continuum Gibbs state, Shlaer mapping, or UV-completion claim.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2) + '\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
