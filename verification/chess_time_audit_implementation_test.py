"""Checks for CHESS_TIME_AUDIT_STEELMAN_AND_IMPLEMENTATION.md."""
import unittest
import numpy as np

X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
I = np.eye(2, dtype=complex)


def fun(h, f):
    vals, vecs = np.linalg.eigh(h)
    return (vecs * f(vals)) @ vecs.conj().T


def u(h, t, hbar=1.):
    return fun(h, lambda e: np.exp(-1j*e*t/hbar))


def gibbs(h, beta):
    rho = fun(h, lambda e: np.exp(-beta*e))
    return rho / np.trace(rho)


def rho_power(rho, s):
    return fun(rho, lambda x: np.exp(1j*s*np.log(x)))


def modular(rho, s, a):
    v = rho_power(rho, s)
    return v @ a @ v.conj().T


def heisenberg(h, t, a, hbar):
    v = u(h, t, hbar)
    return v.conj().T @ a @ v


class ChessTimeAudit(unittest.TestCase):
    def test_sampled_modular_exact(self):
        hbar, beta, delta = .7, 1.3, .11
        h = .6*Z + .2*X
        rho = gibbs(h, beta)
        step = u(h, delta, hbar)
        for n in range(12):
            v = np.linalg.matrix_power(step, n)
            actual = v.conj().T @ Y @ v
            np.testing.assert_allclose(actual, modular(rho, -n*delta/(beta*hbar), Y), atol=1e-13)

    def test_uniform_bound_with_reference_ancilla(self):
        hbar, eps, T = .7, .13, 2.
        h, v = .6*Z, .8*X
        a = np.kron(Y, Z)
        rho = np.outer(np.array([1., 0., 0., 1.])/np.sqrt(2), np.array([1., 0., 0., 1.])/np.sqrt(2))
        for delta in (.2, .08, .025):
            for t in np.linspace(0, T, 41):
                n = int(np.floor(t/delta))
                r = n*delta
                e = u(h+eps*v, r, hbar)
                ref = u(h, t, hbar)
                a1 = np.kron(e.conj().T, I) @ a @ np.kron(e, I)
                a0 = np.kron(ref.conj().T, I) @ a @ np.kron(ref, I)
                b = (T*abs(eps)*np.linalg.norm(v, 2) + delta*np.linalg.norm(h, 2))/hbar
                self.assertLessEqual(np.linalg.norm(a1-a0, 2), 2*b + 1e-12)
                re = np.kron(e, I) @ rho @ np.kron(e.conj().T, I)
                r0 = np.kron(ref, I) @ rho @ np.kron(ref.conj().T, I)
                self.assertLessEqual(np.sum(np.abs(np.linalg.eigvalsh(re-r0)))/2, b + 1e-12)

    def test_same_order_different_calibrations(self):
        h = .6*Z
        a = X
        # Same label n=3, but calibrated readings are different and so are predictions.
        self.assertGreater(np.linalg.norm(heisenberg(h, 3*.1, a, 1)-heisenberg(h, 3*.2, a, 1), 2), .1)

    def test_common_restriction_does_not_restrict_flow(self):
        beta, s = .9, .31
        xx = np.kron(X, X)
        rho = gibbs(xx, beta)
        marginal = np.trace(rho.reshape(2, 2, 2, 2), axis1=1, axis2=3)
        np.testing.assert_allclose(marginal, I/2, atol=1e-14)
        a = np.kron(Z, I)
        expected = np.cos(2*beta*s)*a - np.sin(2*beta*s)*np.kron(Y, X)
        np.testing.assert_allclose(modular(rho, s, a), expected, atol=1e-14)
        self.assertGreater(np.linalg.norm(expected @ np.kron(I,Z) - np.kron(I,Z) @ expected), .1)
        np.testing.assert_allclose(modular(marginal, s, Z), Z, atol=1e-14)
        np.testing.assert_allclose(rho_power(marginal,s) @ rho_power(marginal,-s), I, atol=1e-14)

    def test_diagonal_clocks_commute_even_in_superposition(self):
        cw, cb = np.diag([.2, 1., 1.5]), np.diag([2., .1, .4])
        np.testing.assert_allclose(cw@cb-cb@cw, np.zeros((3,3)), atol=0)
        state = np.ones(3)/np.sqrt(3)
        self.assertAlmostEqual(np.linalg.norm((cw@cb-cb@cw)@state), 0.)


if __name__ == '__main__':
    unittest.main()
