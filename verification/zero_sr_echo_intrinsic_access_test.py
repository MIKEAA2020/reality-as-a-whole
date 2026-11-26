"""Operational distinguishability and a clock-invariant unsharp echo readout.

The two-level records are an isometric representation of selected echo
branches. The 20-tick pointer is a reduced global construction, not proof of
physical locality, subject access, consciousness or a phenomenal metric.
"""
import math
import unittest
import numpy as np

from verification.zero_echo_mode_clock_transport import (
    INDEX, forward, uniform_history, clock_shift, anchored_history_projector)
from verification.zero_echo_joint_identity_balance import magnitude
from verification.zero_sr_echo_constitution_test import candidate_quality


def density(p, c):
    """Two-record state [[p,c],[c*,1-p]], validating positivity."""
    if not 0 <= p <= 1 or abs(c)**2 > p*(1-p) + 1e-12:
        raise ValueError('invalid density matrix')
    return np.array([[p, c], [np.conjugate(c), 1-p]], dtype=complex)


def trace_distance(a, b):
    return float(np.abs(np.linalg.eigvalsh(a-b)).sum()/2)


def t_distance(a, b):
    return float(abs(a[0,0]-b[0,0]))


def optimal_effect(a, b):
    vals, vecs = np.linalg.eigh(a-b)
    active = vecs[:, vals > 1e-12]
    return active @ active.conj().T


def success(a, b, effect):
    return float((np.trace(effect@a).real +
                  np.trace((np.eye(len(a))-effect)@b).real)/2)


def clock_pair():
    """Stationary T=+ and T=- branch histories on the reduced echo."""
    plus = np.zeros(8); minus = np.zeros(8)
    plus[INDEX[-1, 1, -1]] = 1
    minus[INDEX[-1, -1, -1]] = 1
    inverse = forward(10).T
    return uniform_history(inverse@plus), uniform_history(inverse@minus)


def stationary_write(r):
    """Write two possibly overlapping output states, orthogonal to ready."""
    if not 0 <= r <= 1:
        raise ValueError('overlap must be in [0,1]')
    u = math.sqrt(1-r*r)
    swap = np.array([[0.,1.,0.], [1.,0.,0.], [0.,0.,1.]])
    rotation = np.array([[1.,0.,0.], [0.,r,-u], [0.,u,r]])
    vplus, vminus = swap, rotation@swap
    pplus = anchored_history_projector(1, 'fine', (0, 1))
    pminus = anchored_history_projector(1, 'fine', (0, -1))
    return (np.eye(480) + np.kron(pplus, vplus-np.eye(3)) +
            np.kron(pminus, vminus-np.eye(3)))


def pointer_density(r, minus):
    v = np.array([0.,r,math.sqrt(1-r*r)]) if minus else np.array([0.,1.,0.])
    return np.outer(v, v)


class SREchoIntrinsicAccessTests(unittest.TestCase):
    def test_valid_two_record_states_and_trace_distance_formula(self):
        states = [(0.5, 0.0), (0.5, 0.3j), (0.5, -0.5),
                  (0.25, 0.25), (0.75, -0.25j)]
        for p, c in states:
            a = density(p, c)
            self.assertAlmostEqual(np.trace(a).real, 1.)
            self.assertGreaterEqual(float(np.linalg.eigvalsh(a).min()), -1e-12)
            for q, d in states:
                b = density(q, d)
                expected = math.sqrt((p-q)**2 + abs(c-d)**2)
                self.assertAlmostEqual(trace_distance(a, b), expected)
                self.assertLessEqual(t_distance(a, b), expected+1e-12)
                effect = optimal_effect(a, b)
                self.assertAlmostEqual(success(a, b, effect), (1+expected)/2)
        with self.assertRaises(ValueError): density(.5, .6)

    def test_phase_information_is_invisible_to_S_and_T_statistics(self):
        plus, minus = density(.5, .5), density(.5, -.5)
        self.assertEqual(t_distance(plus, minus), 0.)
        self.assertAlmostEqual(trace_distance(plus, minus), 1.)
        e = optimal_effect(plus, minus)
        self.assertAlmostEqual(success(plus, minus, e), 1.)
        # Coarse S=0 and both T probabilities are the same; the ideal
        # optimal interference effect requires access to the full coherence.
        np.testing.assert_allclose(np.diag(plus), np.diag(minus))

    def test_different_T_bias_and_maximal_physical_access(self):
        a, b = density(.8, 0), density(.2, 0)
        self.assertAlmostEqual(t_distance(a, b), .6)
        self.assertAlmostEqual(trace_distance(a, b), .6)
        self.assertAlmostEqual(success(a, b, optimal_effect(a, b)), .8)

    def test_distance_is_basis_invariant_and_a_readout_is_contracting(self):
        a, b = density(.5, .5), density(.5, -.5)
        phase = np.array([[1,0],[0,1j]])
        aa, bb = phase@a@phase.conj().T, phase@b@phase.conj().T
        self.assertAlmostEqual(trace_distance(aa, bb), trace_distance(a, b))
        # T dephasing destroys this pair's distinguishability.
        self.assertAlmostEqual(trace_distance(np.diag(np.diag(a)), np.diag(np.diag(b))), 0.)

    def test_actual_sector_and_candidate_coordinate_relabel(self):
        self.assertEqual(magnitude(0), magnitude(1))
        self.assertEqual(float(magnitude(0)), 3/16)
        for k in (-2, -1, 1, 2):
            qplus = candidate_quality(0, 1, k)
            qminus = candidate_quality(1, 1, k)
            self.assertEqual(qplus[0], 0)
            self.assertEqual(qminus[0], 0)
            self.assertEqual(qplus[1], -qminus[1])
            self.assertNotEqual(qplus, qminus)
        self.assertEqual(candidate_quality(0, 1, 0), candidate_quality(1, 1, 0))
        # T-basis record distributions remain physically orthogonal regardless
        # of coordinate names; no phenomenological interpretation is assumed.
        self.assertAlmostEqual(trace_distance(density(1,0), density(0,0)), 1.)

    def test_stationary_histories_and_pointer_unitary(self):
        plus, minus = clock_pair()
        w = clock_shift()
        pplus = anchored_history_projector(1, 'fine', (0,1))
        pminus = anchored_history_projector(1, 'fine', (0,-1))
        for vec, proj in ((plus,pplus),(minus,pminus)):
            np.testing.assert_allclose(w@vec, vec, atol=1e-14)
            np.testing.assert_allclose(proj@vec, vec, atol=1e-14)
        self.assertAlmostEqual(abs(np.vdot(plus,minus)), 0.)
        u = stationary_write(.6)
        np.testing.assert_allclose(u.T@u, np.eye(480), atol=1e-14)
        np.testing.assert_allclose(np.kron(w,np.eye(3))@u,
                                   u@np.kron(w,np.eye(3)), atol=1e-14)
        with self.assertRaises(ValueError): stationary_write(1.1)

    def test_unsharp_access_coherence_and_held_constraint(self):
        plus, minus = clock_pair()
        history = (plus+minus)/np.sqrt(2)
        ready = np.array([1., 0., 0.])
        w = clock_shift()
        for r in (0., .6, 1.):
            unitary = stationary_write(r)
            out = (unitary@np.kron(history,ready)).reshape(160,3)
            np.testing.assert_allclose(w@out, out, atol=1e-14)
            self.assertAlmostEqual(float(np.linalg.norm(out[:,0])), 0.)
            reduced = out@out.conj().T
            coherence = np.vdot(plus,reduced@minus)
            fidelity = np.vdot(history,reduced@history).real
            self.assertAlmostEqual(coherence.real, r/2)
            self.assertAlmostEqual(fidelity, (1+r)/2)
            a, b = pointer_density(r,False), pointer_density(r,True)
            for branch, expected in ((plus,a), (minus,b)):
                joint = (unitary@np.kron(branch,ready)).reshape(160,3)
                np.testing.assert_allclose(joint.T@joint.conj(), expected, atol=1e-14)
            d = trace_distance(a,b)
            self.assertAlmostEqual(d, math.sqrt(1-r*r))
            self.assertAlmostEqual(success(a,b,optimal_effect(a,b)), (1+d)/2)
            self.assertAlmostEqual(d*d + (2*abs(coherence))**2, 1.)
        # Example r=3/5: pointer success 9/10, retained visibility 3/5,
        # nonselective record/history fidelity 4/5, for these states only.
        self.assertAlmostEqual(success(pointer_density(.6,False),pointer_density(.6,True),
                         optimal_effect(pointer_density(.6,False),pointer_density(.6,True))), .9)

    def test_pointer_data_do_not_decide_owner_hypotheses(self):
        plus, minus = clock_pair()
        ready = np.array([1.,0.,0.])
        out = (stationary_write(.6)@np.kron((plus+minus)/np.sqrt(2),ready)).reshape(160,3)
        observed = out.T@out.conj()
        # The alternative momentary/persistent labels do not enter U or the
        # state; they generate exactly the same specified pointer density.
        reports = {'persistent': observed.copy(), 'momentary': observed.copy()}
        np.testing.assert_allclose(reports['persistent'], reports['momentary'])
        self.assertAlmostEqual(float(np.trace(observed).real), 1.)
        # This is an intentionally restricted formal extension, not proof of
        # indistinguishable complete physical–phenomenal worlds.


if __name__ == '__main__':
    unittest.main()
