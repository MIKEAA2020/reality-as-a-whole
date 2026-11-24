"""Exact locally invariant encoded five-ray instrument for three charges.

Four four-level constituents form one local lab. A two-dimensional code is
contained in the joint kernel of all three additive directional generators.
This is an encoded alternative, not a dilation of the previous bare state.
"""
import math
import unittest
import numpy as np
from verification.zero_article_jet_dual_pair_test import X, PAULIS
from verification.zero_five_ray_record_current_unification_test import q, ns, axis

I4 = np.eye(4, dtype=complex)
I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)
I256 = np.eye(256, dtype=complex)
OMEGA = np.diag([1., -1., -1., -1.]).astype(complex) / 2
S1 = np.einsum('ab,cd->abcd', OMEGA, OMEGA).reshape(256)
S2 = np.einsum('ac,bd->abcd', OMEGA, OMEGA).reshape(256)
CODE = np.column_stack((S1, (4*S2-S1)/math.sqrt(15)))
PCODE = CODE @ CODE.conj().T
SINGLET = np.array([[0., 1.], [-1., 0.]], dtype=complex) / math.sqrt(2)


def kron_all(parts):
    out = np.array([[1.]], dtype=complex)
    for part in parts:
        out = np.kron(out, part)
    return out


def local_charges():
    return [sum(kron_all([x if k == j else I4 for k in range(4)])
                for j in range(4)) for x in X]


def effects():
    return [qi * (I2 + sum(c*s for c, s in zip(n, PAULIS)))
            for qi, n in zip(q, ns)]


def kraus():
    # Each effect is rank one with eigenvalue 2 q_i.
    return [f / math.sqrt(2*qi) for f, qi in zip(effects(), q)]


def readout_unitary():
    """Complete the specified 2 -> 2x3 isometry to a 6x6 unitary."""
    K = kraus()
    U = np.zeros((6, 6), dtype=complex)
    columns = []
    for a in range(2):
        v = np.array([K[i][b, a] for b in range(2) for i in range(3)])
        U[:, 3*a] = v
        columns.append(v)
    vacant = [1, 2, 4, 5]
    for k in range(6):
        v = np.eye(6, dtype=complex)[:, k].copy()
        for _ in range(2):
            for c in columns:
                v -= c * np.vdot(c, v)
        if np.linalg.norm(v) > 1e-10:
            v /= np.linalg.norm(v)
            U[:, vacant.pop(0)] = v
            columns.append(v)
            if not vacant:
                break
    if vacant:
        raise RuntimeError('unitary completion failed')
    return U


def correlations():
    bob = sum(c*s for c, s in zip(axis, PAULIS))
    bob_effects = [(I2+bob)/2, (I2-bob)/2]
    rho = np.outer(SINGLET.reshape(-1), SINGLET.reshape(-1).conj())
    return np.array([[np.trace(rho @ np.kron(f, b)).real
                      for b in bob_effects] for f in effects()])


def reduced_first_site(encoded_state):
    psi = (CODE @ encoded_state).reshape(4, -1)
    return psi @ psi.conj().T


class ThreeBalanceEncodedSphereRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G = local_charges()
        cls.U = readout_unitary()

    def test_constituent_pair_has_nontrivial_exact_balance(self):
        v = OMEGA.reshape(-1)
        for x in X:
            np.testing.assert_allclose((np.kron(x, I4)+np.kron(I4, x))@v,
                                       0, atol=1e-14)
            self.assertAlmostEqual(np.vdot(v, np.kron(x@x, I4)@v).real, .5)
        # Parity transforms the second +X into -X^T and omega into Phi_4.
        p = np.diag([1., -1., -1., -1.])
        np.testing.assert_allclose(OMEGA @ p, np.eye(4)/2, atol=1e-14)
        for x in X:
            np.testing.assert_allclose(p @ x @ p, -x.T, atol=1e-14)

    def test_two_explicit_distinct_local_kernel_vectors(self):
        self.assertAlmostEqual(np.vdot(S1, S2).real, .25)
        np.testing.assert_allclose(CODE.conj().T @ CODE, I2, atol=1e-14)
        for g in self.G:
            np.testing.assert_allclose(g @ CODE, 0, atol=1e-14)
            np.testing.assert_allclose(g @ PCODE, PCODE @ g, atol=1e-14)
        # Neither local invariant direction is a single classical point.
        np.testing.assert_allclose(reduced_first_site([1, 0]), I4/4, atol=1e-14)
        np.testing.assert_allclose(reduced_first_site([0, 1]), I4/4, atol=1e-14)

    def test_arbitrary_logical_operations_are_exactly_conserving(self):
        # E L E†, and its projector complement, commute with every G_i:
        # this is an operator identity on all 4^4 states, not just an average.
        for s in PAULIS:
            physical = CODE @ s @ CODE.conj().T
            for g in self.G:
                np.testing.assert_allclose(g@physical - physical@g, 0, atol=1e-14)
        for g in self.G:
            np.testing.assert_allclose(g @ (I256-PCODE) - (I256-PCODE) @ g,
                                       0, atol=1e-14)

    def test_neutral_pointer_has_explicit_unitary_and_kraus_operators(self):
        U = self.U
        np.testing.assert_allclose(U.conj().T @ U, np.eye(6), atol=1e-13)
        for i, k in enumerate(kraus()):
            np.testing.assert_allclose(U.reshape(2, 3, 2, 3)[:, i, :, 0], k,
                                       atol=1e-14)
        np.testing.assert_allclose(sum(k.conj().T@k for k in kraus()), I2, atol=1e-14)
        # Full 768x768 physical U: (I-P)⊗I3+(E⊗I3)U(E†⊗I3).
        # The tested G E=0 and [G,P]=0 prove commutation with G⊗I3
        # for every entry of U, including its arbitrary unitary completion.

    def test_five_ray_and_second_lab_table_is_exact(self):
        expected = np.array([[3/40, 1/20], [1/10, 3/10], [13/40, 3/20]])
        np.testing.assert_allclose(correlations(), expected, atol=1e-14)
        np.testing.assert_allclose(correlations().sum(axis=1), q, atol=1e-14)
        np.testing.assert_allclose(correlations().sum(axis=0), [.5, .5], atol=1e-14)

    def test_every_record_branch_obeys_all_six_lab_balances(self):
        # For each pointer i, the post-interaction state is (K_i⊗I)|singlet>
        # in the encoded labs. Mapping to either four-constituent code E
        # leaves each of the three local G generators exactly zero.
        for k in kraus():
            branch = k @ SINGLET
            physical = CODE @ branch @ CODE.T
            for g in self.G:
                np.testing.assert_allclose(g @ physical, 0, atol=1e-14)
                np.testing.assert_allclose(physical @ g.T, 0, atol=1e-14)
        # Thus their sum and every difference are also zero, outcome by outcome.

    def test_constituent_pair_imbalances_are_compensated_not_absent(self):
        first = [kron_all([x, I4, I4, I4]) + kron_all([I4, x, I4, I4])
                 for x in X]
        second = [kron_all([I4, I4, x, I4]) + kron_all([I4, I4, I4, x])
                  for x in X]
        c12 = sum(g@g for g in first)
        np.testing.assert_allclose(CODE.conj().T @ c12 @ CODE,
                                   np.diag([0., 16/5]), atol=1e-13)
        for g, h in zip(first, second):
            np.testing.assert_allclose((g+h) @ CODE, 0, atol=1e-14)
        for k, qi in zip(kraus(), q):
            branch = k @ SINGLET
            rho_a = branch @ branch.conj().T / qi
            self.assertAlmostEqual(np.trace(rho_a @ CODE.conj().T @ c12 @ CODE).real,
                                   8/5, places=12)
        # First-pair imbalance has nonzero variance on every readout branch,
        # while the second pair cancels it as an exact vector identity.

    def test_unread_alice_record_cannot_signal_to_bob(self):
        # Explicit partial trace after the complete Alice instrument.
        rho_b = np.zeros((2, 2), complex)
        for k in kraus():
            a = k @ SINGLET
            rho_b += a.T @ a.conj()
        np.testing.assert_allclose(rho_b, I2/2, atol=1e-14)
        # Conditional Bob states are allowed to differ; the record is not
        # accessible to Bob without an independent communication channel.
        conditional = [((k @ SINGLET).T @ (k @ SINGLET).conj())/qi
                       for k, qi in zip(kraus(), q)]
        self.assertGreater(np.linalg.norm(conditional[0]-conditional[1]), .1)

    def test_symmetry_alone_does_not_select_the_encoded_state(self):
        other = CODE @ np.array([1., 0.])
        for g in self.G:
            np.testing.assert_allclose(g @ other, 0, atol=1e-14)
        # Every logical state and every two-lab logical entangled state lies in
        # the same local kernel; the singlet requires a further input.
        alt = np.array([[1., 0.], [0., 0.]], dtype=complex)
        self.assertAlmostEqual(np.vdot(alt, SINGLET).real, 0)

if __name__ == '__main__':
    unittest.main()
