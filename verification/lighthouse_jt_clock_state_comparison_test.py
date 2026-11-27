#!/usr/bin/env python3
"""Finite numerical controls for the JT-inspired scalar clock state gate.

This checks the note's declared packet and auxiliary finite KMS example; it is
not a simulation of a gravitational or conformal-field-theory crossed product.
"""
import math
import unittest

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm

P0, DELTA, T = 1.5, 0.2, 10.0
BMIN, BMAX = 7.0, 8.0


def gauss_interval(a, b, count):
    x, w = leggauss(count)
    return (a+b)/2+(b-a)*x/2, (b-a)*w/2


def packet_bin_probabilities(S, nb=44, np_=80, nt=80):
    B, wb = gauss_interval(BMIN, BMAX, nb)
    wb = wb * 2*np.sin(np.pi*(B-7))**2
    p, wp = gauss_interval(P0-DELTA, P0+DELTA, np_)
    phi = np.cos(np.pi*(p-P0)/(2*DELTA))/np.sqrt(DELTA)
    energy = p[None, :]**2/(2*B[:, None])
    velocity = p[None, :]/B[:, None]
    v0 = P0/B
    bins = [(-T,-3),(-3,3),(3,T)]
    results = [[], []]
    for lo, hi in bins:
        t, wt = gauss_interval(lo, hi, nt)
        position = np.sqrt(v0)[:,None,None] * np.exp(
            1j*(v0[:,None,None]*t[None,:,None]*p[None,None,:]
                - S*energy[:,None,:]))
        clock_time = np.sqrt(velocity)[:,None,:] * np.exp(
            1j*(t[None,:,None]-S)*energy[:,None,:])
        for index, kernel in enumerate((position, clock_time)):
            amp = np.sum(kernel*(wp*phi)[None,None,:], axis=-1)/np.sqrt(2*np.pi)
            results[index].append(float(np.einsum('b,t,bt->',wb,wt,abs(amp)**2)))
    for row in results:
        row.append(1-sum(row))
    return np.array(results)


def analytic_tv_bound(B):
    lo, hi, v0 = (P0-DELTA)/B, (P0+DELTA)/B, P0/B
    factor = math.sqrt(2*DELTA/(2*math.pi))
    amplitude_sum = factor*(math.sqrt(hi)+math.sqrt(v0))
    difference = factor*(max(math.sqrt(v0)-math.sqrt(lo), math.sqrt(hi)-math.sqrt(v0))
                         + math.sqrt(v0)*T*DELTA**2/(2*B))
    return min(1.0, 2*T*amplitude_sum*difference)


def reading_lowers(max_s=4.0):
    scale = 2*T*8*DELTA/(math.pi**3)
    position_phase = (P0*DELTA*T+(P0*DELTA+DELTA**2/2)*max_s)/BMIN
    time_phase = (P0*DELTA+DELTA**2/2)*(T+max_s)/BMIN
    q_lower = scale*(P0/BMAX)*math.cos(position_phase)**2
    t_lower = scale*((P0-DELTA)/BMAX)*math.cos(time_phase)**2
    return q_lower, t_lower


class LighthouseScalarStateComparisonTests(unittest.TestCase):
    def test_packet_and_distribution_are_normalized(self):
        B, wb = gauss_interval(BMIN, BMAX, 60)
        p, wp = gauss_interval(P0-DELTA, P0+DELTA, 60)
        bnorm = np.sum(wb*2*np.sin(np.pi*(B-7))**2)
        pnorm = np.sum(wp*np.cos(np.pi*(p-P0)/(2*DELTA))**2/DELTA)
        self.assertAlmostEqual(bnorm, 1.0, places=13)
        self.assertAlmostEqual(pnorm, 1.0, places=13)
        for s in (0,4):
            probabilities = packet_bin_probabilities(s)
            np.testing.assert_allclose(probabilities.sum(axis=1), 1, atol=1e-13)
            self.assertGreater(probabilities.min(), 0)

    def test_full_four_outcome_numbers_and_common_no_reading(self):
        expected = np.array([[.07127560060391325,.06190250318215062,.07127560060391328,.7955462956100229],
                             [.071213802486105,.06185018259014293,.07121380248610502,.7957222124376471]])
        np.testing.assert_allclose(packet_bin_probabilities(0), expected, atol=2e-12)
        probs = packet_bin_probabilities(4)
        self.assertGreater(probs[0,3], .796)
        self.assertGreater(probs[1,3], .796)

    def test_quadrature_convergence(self):
        low = packet_bin_probabilities(4, nb=30, np_=48, nt=48)
        high = packet_bin_probabilities(4, nb=54, np_=100, nt=100)
        np.testing.assert_allclose(low, high, atol=2e-11)

    def test_rigorous_tv_and_conditional_reading_bounds(self):
        max_bound = analytic_tv_bound(BMIN)
        self.assertLess(max_bound, .055)
        for B in np.linspace(BMIN, BMAX, 101):
            self.assertLessEqual(analytic_tv_bound(B), max_bound+1e-14)
        qmin, tmin = reading_lowers()
        self.assertGreater(qmin, .129)
        self.assertGreater(tmin, .107)
        for s in (0,4):
            p = packet_bin_probabilities(s)
            total = 0.5*np.sum(abs(p[0]-p[1]))
            cond = p[:,:3]/p[:,:3].sum(axis=1)[:,None]
            cond_tv = .5*np.sum(abs(cond[0]-cond[1]))
            self.assertLess(total, .000177)
            self.assertLess(total, max_bound)
            self.assertGreaterEqual(min(p[:,:3].sum(axis=1)), min(qmin,tmin))
            self.assertLess(cond_tv, max_bound/min(qmin,tmin))

    def test_time_covariance_with_wavepacket(self):
        B = 7.5
        p, wp = gauss_interval(P0-DELTA, P0+DELTA, 80)
        phi = np.cos(np.pi*(p-P0)/(2*DELTA))/np.sqrt(DELTA)
        energy = p*p/(2*B)
        for t in (-2,0,3):
            S = 4.0
            evolved_state = np.exp(-1j*S*energy)*phi
            amp1 = np.sum(wp*np.sqrt(p/B)*np.exp(1j*t*energy)*evolved_state)
            amp2 = np.sum(wp*np.sqrt(p/B)*np.exp(1j*(t-S)*energy)*phi)
            self.assertAlmostEqual(abs(amp1-amp2), 0.0, places=13)

    def test_two_level_gibbs_kms_and_stationary_purification(self):
        beta, gap = 2.0, .7
        h = np.diag([0.,gap])
        rho = expm(-beta*h); rho /= np.trace(rho)
        A = np.array([[0.,1.],[0.,0.]])
        B = A.T
        alpha_i_beta_B = expm(-beta*h)@B@expm(beta*h)
        self.assertAlmostEqual(np.trace(rho@A@alpha_i_beta_B), np.trace(rho@B@A))
        omega = np.array([math.sqrt(rho[0,0]),0,0,math.sqrt(rho[1,1])])
        L = np.kron(h,np.eye(2))-np.kron(np.eye(2),h)
        np.testing.assert_allclose(L@omega, 0, atol=1e-14)
        for S in (0,.5,2):
            np.testing.assert_allclose(expm(-1j*L*S)@omega,omega,atol=1e-14)

    def test_positive_branch_not_kms_on_full_circle_algebra(self):
        beta, B, R = 2., 7.5, 3.
        energies = np.array([1/(2*B*R*R),1/(2*B*R*R)])
        rho = np.diag([1.,0.])  # ordered |+1>, |-1>
        a = np.array([[0.,1.],[0.,0.]])
        b = a.T
        h = np.diag(energies)
        lhs = np.trace(rho@a@expm(-beta*h)@b@expm(beta*h))
        rhs = np.trace(rho@b@a)
        self.assertAlmostEqual(lhs, 1.)
        self.assertAlmostEqual(rhs, 0.)

    def test_compact_target_recurrence_and_uniform_gibbs_reading(self):
        B, R, beta = 7.5, 3., 2.
        n = np.arange(1, 40)
        E = n*n/(2*B*R*R)
        period = 4*np.pi*B*R*R
        np.testing.assert_allclose(np.exp(-1j*E*period), np.ones(len(n)), atol=3e-12)
        w = np.exp(-beta*E); w /= w.sum()
        for theta in (0.,.7,2.2):
            # diagonal rho gives uniform positive-branch angle density
            density = np.sum(w*np.abs(np.exp(-1j*n*theta))**2)/(2*np.pi)
            self.assertAlmostEqual(density, 1/(2*np.pi), places=14)

    def test_compact_time_effects_integrate_to_identity(self):
        B, R = 7.5, 3.0
        n = np.arange(1, 6)
        period = 4*np.pi*B*R*R
        t, wt = gauss_interval(0., period, 140)
        energy = n*n/(2*B*R*R)
        kets = np.exp(-1j*t[:,None]*energy[None,:])/np.sqrt(period)
        effects = np.einsum('t,ti,tj->ij', wt, kets, kets.conj())
        np.testing.assert_allclose(effects, np.eye(len(n)), atol=2e-13)

    def test_abstract_rigging_scaffold_with_auxiliary_energies(self):
        # Spectral change k+lambda=c makes the group-average factor independent
        # of lambda, including signed Liouville energies.
        a = .7
        for lam in (-3.,0.,2.4):
            k, wk = gauss_interval(-10-lam, 10-lam, 600)
            density = np.exp(-(k+lam)**2/a**2)/np.sqrt(np.pi*a*a)
            for eps in (.04,.01):
                norm = np.sum(wk*density*np.sqrt(np.pi/eps)*np.exp(-(k+lam)**2/(4*eps)))
                expected = 2*np.sqrt(np.pi)/np.sqrt(a*a+4*eps)
                self.assertAlmostEqual(norm,expected,places=10)


if __name__ == '__main__':
    unittest.main()
