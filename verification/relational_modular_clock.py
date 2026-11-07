#!/usr/bin/env python3
"""Finite relational/modular-clock example; no claim about quantum gravity.

The analytic statement, assumptions, sign convention and scope are in
RELATIONAL_MODULAR_CLOCK.md. Execute from any directory with Python and NumPy.
"""
import json
from pathlib import Path
import unittest

import numpy as np

N = 3
ENERGIES = np.array([0.0, 1.0, 2.0])
TIMES = 2 * np.pi * np.arange(N) / N
BETA = 1.0
P = np.exp(-BETA * ENERGIES)
P /= P.sum()
TAU = np.diag(P).astype(complex)
PSI = np.sqrt(P).astype(complex)
RHO0 = np.outer(PSI, PSI.conj())
I = np.eye(N, dtype=complex)


def U(t):
    return np.diag(np.exp(-1j * ENERGIES * t))


def heisenberg(a, t):
    u = U(t)
    return u.conj().T @ a @ u


def modular(a, probabilities, s):
    """sigma_s(A) = rho^(is) A rho^(-is), for diagonal faithful rho."""
    phase = np.diag(np.exp(1j * s * np.log(probabilities)))
    return phase @ a @ phase.conj().T


def history(psi=PSI):
    return np.concatenate([U(t) @ psi for t in TIMES]) / np.sqrt(N)


def constraint():
    """Path graph propagation C=sum D_e^*D_e, clock first."""
    result = np.zeros((N*N, N*N), dtype=complex)
    for j in range(N - 1):
        d = np.zeros((N, N*N), dtype=complex)
        d[:, j*N:(j+1)*N] = -U(TIMES[j+1] - TIMES[j])
        d[:, (j+1)*N:(j+2)*N] = I
        result += d.conj().T @ d
    return result


def condition(v, j):
    block = v[j*N:(j+1)*N]
    weight = np.vdot(block, block).real
    return weight, np.outer(block, block.conj()) / weight


def system_marginal(v):
    blocks = v.reshape(N, N)
    return sum(np.outer(b, b.conj()) for b in blocks)


def matrix_units():
    for j in range(N):
        for k in range(N):
            a = np.zeros((N, N), dtype=complex)
            a[j, k] = 1
            yield a


class RelationalModularClock(unittest.TestCase):
    def test_constraint_and_stationarity(self):
        c, v = constraint(), history()
        self.assertAlmostEqual(np.vdot(v, v).real, 1.0)
        np.testing.assert_allclose(c @ v, 0, atol=1e-12)
        self.assertGreaterEqual(np.linalg.eigvalsh(c).min(), -1e-12)
        rh = np.outer(v, v.conj())
        np.testing.assert_allclose(c @ rh - rh @ c, 0, atol=1e-12)

    def test_conditioned_schrodinger_evolution_and_marginal(self):
        v = history()
        for j, t in enumerate(TIMES):
            weight, rho = condition(v, j)
            self.assertAlmostEqual(weight, 1/N)
            np.testing.assert_allclose(rho, U(t) @ RHO0 @ U(t).conj().T, atol=1e-12)
        np.testing.assert_allclose(system_marginal(v), TAU, atol=1e-12)
        self.assertGreater(np.linalg.norm(condition(v, 1)[1] - RHO0), 0.1)

    def test_constraint_compatible_relational_observables(self):
        a = np.array([[0, 1, 0], [1, 0, 1j], [0, -1j, 0]], dtype=complex)
        c, v = constraint(), history()
        for j, t in enumerate(TIMES):
            observable = np.zeros((N*N, N*N), dtype=complex)
            for w, tw in enumerate(TIMES):
                transport = U(tw - t)
                observable[w*N:(w+1)*N, w*N:(w+1)*N] = transport @ a @ transport.conj().T
            np.testing.assert_allclose(c @ observable - observable @ c, 0, atol=1e-12)
            _, rho = condition(v, j)
            np.testing.assert_allclose(np.vdot(v, observable @ v), np.trace(rho @ a), atol=1e-12)

    def test_modular_equals_heisenberg_after_rescaling(self):
        # All matrix units span M_3, hence the check exercises a full basis.
        for t in [0.0, 0.37, *TIMES, 4.1]:
            for a in matrix_units():
                np.testing.assert_allclose(modular(a, P, -t/BETA), heisenberg(a, t), atol=1e-12)
        # Clock-conditioned expectations, at actual clock readings.
        a = np.array([[0, 1, 0], [1, 0, 1j], [0, -1j, 0]], dtype=complex)
        for j, t in enumerate(TIMES):
            _, rho = condition(history(), j)
            np.testing.assert_allclose(np.trace(rho @ a), np.trace(RHO0 @ modular(a, P, -t/BETA)), atol=1e-12)

    def test_non_gibbs_reference_is_counterexample(self):
        # Equal energy gaps require equal log-probability gaps for any single
        # scaling of modular parameter. Here those log gaps are unequal.
        q = np.array([0.5, 0.3, 0.2])
        self.assertGreater(abs((np.log(q[0])-np.log(q[1])) -
                               (np.log(q[1])-np.log(q[2]))), 0.1)
        v = history(np.sqrt(q))
        np.testing.assert_allclose(system_marginal(v), np.diag(q), atol=1e-12)
        # Match the 0-1 frequency; then 1-2 necessarily fails even locally.
        beta_fit = np.log(q[0]/q[1])
        a = np.zeros((N, N), dtype=complex)
        a[1, 2] = 1
        t = 0.7
        discrepancy = np.linalg.norm(modular(a, q, -t/beta_fit) - heisenberg(a, t))
        self.assertGreater(discrepancy, 0.1)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(RelationalModularClock)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    output = {
        'model': 'finite three-level path-history clock; faithful Gibbs system marginal',
        'energies': ENERGIES.tolist(), 'beta': BETA, 'clock_times': TIMES.tolist(),
        'gibbs_probabilities': P.tolist(), 'tests_run': result.testsRun,
        'failures': len(result.failures), 'errors': len(result.errors),
        'all_pass': result.wasSuccessful(),
        'scope': 'Finite-dimensional example and analytic statement only; not a proof of quantum-gravitational time or Shlaer equivalence.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2) + '\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
