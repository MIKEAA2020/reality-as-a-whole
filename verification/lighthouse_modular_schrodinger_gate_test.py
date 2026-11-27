"""Finite controls for LIGHTHOUSE_MODULAR_SCHRODINGER_ANALYTIC_GATE.md."""
import unittest
import numpy as np

X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
I = np.eye(2, dtype=complex)


def spectral_function(h, func):
    vals, vecs = np.linalg.eigh(h)
    return (vecs * func(vals)) @ vecs.conj().T


def unitary(h, t):
    return spectral_function(h, lambda e: np.exp(-1j * e * t))


def gibbs(h, beta):
    q = spectral_function(h, lambda e: np.exp(-beta * e))
    return q / np.trace(q)


def power(rho, s):
    return spectral_function(rho, lambda e: np.exp(1j * s * np.log(e)))


class ModularSchrodingerGate(unittest.TestCase):
    def setUp(self):
        self.h, self.v = 0.65 * Z, 0.8 * X
        self.eps, self.beta, self.hbar = 0.15, 1.2, 0.7
        self.he = self.h + self.eps * self.v
        self.r0, self.re = gibbs(self.h, self.beta), gibbs(self.he, self.beta)

    def cocycle(self, s):
        return power(self.re, s) @ power(self.r0, -s)

    def test_noncommuting(self):
        self.assertGreater(np.linalg.norm(self.h @ self.v - self.v @ self.h), 1)

    def test_exact_sign_and_cocycle(self):
        s, q = 0.37, -0.21
        alpha = lambda r, a: power(self.r0, r) @ a @ power(self.r0, -r)
        np.testing.assert_allclose(self.cocycle(s + q), self.cocycle(s) @ alpha(s, self.cocycle(q)), atol=1e-14)
        lhs = power(self.re, s) @ Y @ power(self.re, -s)
        t = -self.beta * self.hbar * s
        u = unitary(self.he, t / self.hbar)
        np.testing.assert_allclose(lhs, u.conj().T @ Y @ u, atol=1e-14)
        np.testing.assert_allclose(lhs, self.cocycle(s) @ alpha(s, Y) @ self.cocycle(s).conj().T, atol=1e-14)

    def test_cocycle_derivative(self):
        step = 1e-5
        approx = (self.cocycle(step) - self.cocycle(-step)) / (2 * step)
        z0 = np.trace(spectral_function(self.h, lambda x: np.exp(-self.beta*x))).real
        ze = np.trace(spectral_function(self.he, lambda x: np.exp(-self.beta*x))).real
        expected = -1j*self.beta*self.eps*self.v - 1j*np.log(ze/z0)*I
        np.testing.assert_allclose(approx, expected, atol=1e-10)

    def test_bound_and_reference_stationarity(self):
        r = (I + Y) / 2
        for t in [-3., -0.1, 0., 0.1, 3.]:
            u, ue = unitary(self.h, t/self.hbar), unitary(self.he, t/self.hbar)
            delta = ue @ r @ ue.conj().T - u @ r @ u.conj().T
            trace_distance = np.sum(np.abs(np.linalg.eigvalsh(delta))) / 2
            bound = abs(t*self.eps) * np.linalg.norm(self.v, 2) / self.hbar
            self.assertLessEqual(trace_distance, bound + 1e-14)
            obsdelta = ue.conj().T @ Y @ ue - u.conj().T @ Y @ u
            self.assertLessEqual(np.linalg.norm(obsdelta, 2), 2*bound + 1e-14)
            np.testing.assert_allclose(ue @ self.re @ ue.conj().T, self.re, atol=1e-14)
        self.assertGreater(np.linalg.norm(self.he @ r - r @ self.he), 0.1)

    def test_restriction_leaves_subalgebra(self):
        k, a = np.kron(X, X), np.kron(Z, I)
        u = unitary(k, 0.3)
        evolved = u.conj().T @ a @ u
        # Elements of M2 tensor I commute with I tensor Z.
        commutator = evolved @ np.kron(I, Z) - np.kron(I, Z) @ evolved
        self.assertGreater(np.linalg.norm(commutator), 1)


if __name__ == '__main__':
    unittest.main()
