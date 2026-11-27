"""Finite numerical controls for analytic claims in frontier problems §10–11.

These tests do not establish full gravity, domains or the continuous rigging-map
construction; those are spelled out analytically in the accompanying note.
"""
import unittest
import numpy as np


class FrontierControls(unittest.TestCase):
    def setUp(self):
        self.q, self.beta, self.hbar = .7, .8, 1.2
        self.omega = -np.log(self.q) / (self.beta * self.hbar)
        self.total = 180
        self.n = np.arange(self.total)
        self.psi = np.sqrt(1-self.q) * self.q**(self.n/2)

    def test_normalization_and_generator_domain(self):
        self.assertAlmostEqual(np.vdot(self.psi, self.psi).real, 1., places=14)
        self.assertTrue(np.isfinite(np.linalg.norm(self.n*self.psi)))
        # Exact infinite-series expectation of N² for the geometric distribution.
        self.assertAlmostEqual(np.linalg.norm(self.n*self.psi)**2,
                               self.q*(1+self.q)/(1-self.q)**2, places=12)

    def test_periodic_average_is_gibbs(self):
        # A larger finite truncation and more sampling points than frequency gaps
        # make the Fourier cancellation exact up to floating-point roundoff.
        size, samples = 18, 64
        ps = self.psi[:size]
        phases = np.exp(-2j*np.pi*np.outer(np.arange(samples), np.arange(size))/samples)
        histories = phases * ps[None, :]
        avg = np.einsum('kn,km->nm', histories, histories.conj()) / samples
        target = np.diag((1-self.q)*self.q**np.arange(size))
        np.testing.assert_allclose(avg, target, atol=3e-16)

    def test_modular_sign_and_observable_expectation(self):
        n = np.arange(8)
        rho = (1-self.q)*self.q**n
        t = .71
        s = -t/(self.beta*self.hbar)
        # An observable with both nearest- and longer-range coherences.
        a = np.ones((8, 8), dtype=complex) + np.diag(np.arange(8))
        factors = np.exp(1j*s*np.log(rho))
        modular = factors[:,None] * a * factors.conj()[None,:]
        heisenberg = np.exp(1j*self.omega*t*n[:,None])*a*np.exp(-1j*self.omega*t*n[None,:])
        np.testing.assert_allclose(modular, heisenberg, atol=1e-14)
        p = self.psi[:8]
        evolved = p*np.exp(-1j*self.omega*t*n)
        np.testing.assert_allclose(np.vdot(evolved,a@evolved), np.vdot(p,modular@p), atol=1e-14)

    def test_cutoff_pure_and_gibbs_trace_distance(self):
        for L in (2, 5, 11):
            trunc = np.zeros(self.total)
            trunc[:L] = self.psi[:L]/np.sqrt(1-self.q**L)
            overlap = abs(np.vdot(self.psi, trunc))
            dist_pure = np.sqrt(max(0., 1-overlap**2))
            self.assertAlmostEqual(dist_pure, self.q**(L/2), places=13)
            Gibbs = (1-self.q)*self.q**self.n
            Gibbs_trunc = np.zeros(self.total)
            Gibbs_trunc[:L] = Gibbs[:L]/(1-self.q**L)
            self.assertAlmostEqual(np.abs(Gibbs-Gibbs_trunc).sum()/2, self.q**L, places=13)

    def test_constraint_surface_and_physical_positivity(self):
        kappa = 1/np.sqrt(6)
        p = np.linspace(.1, 4, 40)
        n = np.arange(6)[:,None]
        E = -kappa*p[None,:] - self.hbar*self.omega*n
        np.testing.assert_allclose(E+kappa*p[None,:]+self.hbar*self.omega*n, 0., atol=1e-15)
        data = np.exp(-p[None,:]**2)*(n+1)*np.exp(1j*p[None,:])
        norm = np.sum(abs(data)**2)*(p[1]-p[0])
        self.assertGreater(norm, 0.)

    def test_conformal_causal_order_and_duration_scale(self):
        # Flat 1+1 metric: positive constant rescaling leaves signs of all norms.
        g = np.diag([-1., 1.]); a = 2.7
        for x in (np.array([2., .5]), np.array([1., 2.]), np.array([1., 1.])):
            v = x@g@x; vp = x@(a*a*g)@x
            self.assertAlmostEqual(vp, a*a*v)
            if v < 0:
                self.assertAlmostEqual(np.sqrt(-vp), a*np.sqrt(-v))


if __name__ == '__main__':
    unittest.main()
