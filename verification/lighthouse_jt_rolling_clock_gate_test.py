#!/usr/bin/env python3
"""Scoped numerical controls for the closed-Milne scalar-clock gate.

The accompanying note proves the identities and states their physical limits.
This file checks selected parameters; it is not a JT gravity or CFT simulation.
"""
import unittest

import numpy as np
import sympy as sp
from scipy.integrate import quad


class RollingClockGateTests(unittest.TestCase):
    def test_metric_reduction_and_scalar_rescaling(self):
        # From L=ell*qdot**2/(2N), P=ell*qdot/N, H=N*P**2/(2ell).
        B, S, P, N = 7.5, 0.8, 1.4, 1.3
        ell = B / np.cosh(S)
        qdot = N * P / ell
        lagrangian = ell * qdot**2 / (2 * N)
        hamiltonian = P * qdot - lagrangian
        self.assertAlmostEqual(hamiltonian, N * P**2 / (2 * ell))
        self.assertAlmostEqual(hamiltonian / (N * np.cosh(S)), P**2 / (2 * B))

    def test_source_coordinate_and_constraint_sign(self):
        # Source definitions: S=asinh(k/ell), H=-p*k-ell*Phi,
        # p=-i*d_ell and Phi=+i*d_k. Apply H to f(S).
        ell, k = sp.symbols('ell k', real=True, positive=True)
        S = sp.asinh(k/ell)
        coefficient = sp.simplify(k*sp.diff(S, ell)-ell*sp.diff(S, k))
        self.assertEqual(sp.simplify(coefficient + sp.sqrt(ell**2+k**2)/ell), 0)
        # H = i*(k*d_ell-ell*d_k) = -i*cosh(S)*d_S.
        self.assertEqual(sp.simplify(sp.cosh(S)-sp.sqrt(ell**2+k**2)/ell), 0)

    def test_source_poisson_brackets(self):
        ell, k, p, phi = sp.symbols('ell k p phi', real=True, positive=True)
        B = sp.sqrt(ell**2+k**2)
        S = sp.asinh(k/ell)
        K = (-p*k-ell*phi)*ell/B
        P = (ell*p-k*phi)/B
        variables = [ell, p, phi, k]
        J = sp.Matrix([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]])
        def bracket(a, b):
            da = sp.Matrix([sp.diff(a, x) for x in variables])
            db = sp.Matrix([sp.diff(b, x) for x in variables])
            return sp.simplify((da.T*J*db)[0])
        self.assertEqual(bracket(S, K), 1)
        self.assertEqual(bracket(B, P), 1)
        self.assertEqual(bracket(S, P), 0)
        self.assertEqual(bracket(B, K), 0)

    def test_normalized_control_packet_and_energy(self):
        # w(B,p)=2 sin(pi(B-7)) sin(pi(p-1)) on (7,8)x(1,2).
        norm_b = quad(lambda B: 2*np.sin(np.pi*(B-7))**2, 7, 8)[0]
        norm_p = quad(lambda p: 2*np.sin(np.pi*(p-1))**2, 1, 2)[0]
        self.assertAlmostEqual(norm_b * norm_p, 1.0)
        mean_p = quad(lambda p: p * 2*np.sin(np.pi*(p-1))**2, 1, 2)[0]
        self.assertAlmostEqual(mean_p, 1.5)
        self.assertGreater(1/(2*8), 0)  # strictly positive support energy

    def test_gaussian_group_average(self):
        # g(c)=(pi*a**2)^(-1/4) exp[-c**2/(2a**2)].
        a = 0.7
        for eps in (0.5, 0.03, 0.002):
            integral = quad(
                lambda c: np.exp(-c*c/a**2)/np.sqrt(np.pi*a*a)
                * np.sqrt(np.pi/eps)*np.exp(-c*c/(4*eps)),
                -10, 10, epsabs=1e-11,
            )[0]
            self.assertAlmostEqual(integral, 2*np.sqrt(np.pi)/np.sqrt(a*a+4*eps), places=10)
        limit = 2*np.sqrt(np.pi)/a
        self.assertAlmostEqual(limit, 2*np.pi/(np.sqrt(np.pi)*a))
        self.assertLess(abs(2*np.sqrt(np.pi)/np.sqrt(a*a+4e-8)-limit), 1e-6)

    def test_conditional_sign_and_velocity(self):
        # The source's written +i*d_S gives exp(+iHS) and decreasing q.
        # Its original constraint instead gives -i*d_S, exp(-iHS), increasing q.
        B, S = 7.5, 1.2
        p = np.linspace(1, 2, 20001)
        a = np.sqrt(2)*np.sin(np.pi*(p-1))
        aprime = np.sqrt(2)*np.pi*np.cos(np.pi*(p-1))
        H = p*p/(2*B)
        psi = a*np.exp(1j*S*H)
        derivative = (aprime + 1j*S*p/B*a)*np.exp(1j*S*H)
        mean_q = np.trapezoid(np.conj(psi)*1j*derivative, p)
        self.assertAlmostEqual(mean_q.real, -S*1.5/B, places=8)
        self.assertAlmostEqual(mean_q.imag, 0.0, places=8)
        psi = a*np.exp(-1j*S*H)
        derivative = (aprime - 1j*S*p/B*a)*np.exp(-1j*S*H)
        mean_q = np.trapezoid(np.conj(psi)*1j*derivative, p)
        self.assertAlmostEqual(mean_q.real, S*1.5/B, places=8)
        self.assertAlmostEqual(mean_q.imag, 0.0, places=8)

    def test_q_phase_label_has_reversed_sign(self):
        # q=i*d_p. Positive exp(+ip*tau) is eigenvalue -tau.
        tau, p = 0.9, 1.3
        state = np.exp(1j*p*tau)
        q_on_state = 1j*(1j*tau)*state
        self.assertAlmostEqual(abs(q_on_state + tau*state), 0.0)

    def test_position_povm_not_time_covariant(self):
        B, delta = 7.5, 2.0
        p = np.array([1.0, 1.4, 1.8])
        E = p*p/(2*B)
        gaps = p[:, None]-p[None, :]
        gaps_E = E[:, None]-E[None, :]
        # Match the first pair's effective speed; another pair does not match.
        v = (p[0]+p[1])/(2*B)
        evolved = np.exp(-1j*delta*gaps_E)
        shifted_position = np.exp(-1j*delta*v*gaps)
        self.assertAlmostEqual(abs(evolved[0,1]-shifted_position[0,1]), 0.0, places=12)
        self.assertGreater(abs(evolved[1,2]-shifted_position[1,2]), 0.01)

    def test_energy_time_povm_covariance_and_jacobian(self):
        B, t, a = 7.5, 0.7, 1.3
        p = np.array([1.0, 1.4, 1.8])
        E, v = p*p/(2*B), p/B
        ket = np.sqrt(v)*np.exp(-1j*E*t)/np.sqrt(2*np.pi)
        evolved_ket = np.exp(-1j*E*a)*ket
        target = np.sqrt(v)*np.exp(-1j*E*(t+a))/np.sqrt(2*np.pi)
        np.testing.assert_allclose(evolved_ket, target, atol=1e-14)
        # dE=(p/B)dp is exactly what makes L2(dp) -> L2(dE) unitary.
        integrand_p = lambda x: 2*np.sin(np.pi*(x-1))**2
        norm_p = quad(integrand_p, 1, 2)[0]
        norm_E = quad(lambda E_: integrand_p(np.sqrt(2*B*E_))*B/np.sqrt(2*B*E_),
                      1/(2*B), 4/(2*B))[0]
        self.assertAlmostEqual(norm_E, norm_p, places=10)

    def test_noncompact_scalar_thermal_box_diverges(self):
        # Compact target length 2*pi*R -> p=n/R; Z_R~R*sqrt(2*pi*B/beta).
        B, beta = 7.5, 2.0
        asymptote = np.sqrt(2*np.pi*B/beta)
        for R in (3, 7, 15):
            n = np.arange(-5000, 5001)
            Z = np.exp(-beta*(n/R)**2/(2*B)).sum()
            self.assertAlmostEqual(Z/R, asymptote, places=10)


if __name__ == '__main__':
    unittest.main()
