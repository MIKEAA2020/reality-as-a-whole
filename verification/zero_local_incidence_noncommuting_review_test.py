"""Finite controls for the exact support-split review (not a theory proof)."""
import unittest
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
P = (I + Z) / 2
Q = I - P
R = (I + X) / 2


def comm(a, b):
    return a @ b - b @ a


class IncidenceSupportReview(unittest.TestCase):
    def test_sharp_split_has_exact_norm_distance(self):
        j = 2 * Y
        pinched = P @ j @ P + Q @ j @ Q
        off = P @ j @ Q
        bound = np.linalg.norm(off, 2)
        self.assertAlmostEqual(bound, 2)
        self.assertAlmostEqual(np.linalg.norm(j - pinched, 2), bound)
        # Arbitrary real diagonal matrices include every supported Hermitian split.
        for a in (-5, -1, 0, 2, 7):
            for b in (-3, 0, 1, 6):
                candidate = a * P + b * Q
                self.assertGreaterEqual(np.linalg.norm(j - candidate, 2) + 1e-12, bound)

    def test_symmetric_allocation_zero_mean_nonzero_variance(self):
        j = 2 * Y
        assigned = (P @ j + j @ P) / 2
        absent = np.array([0, 1], dtype=complex)
        mean = np.vdot(absent, assigned @ absent)
        second = np.vdot(absent, assigned @ assigned @ absent)
        self.assertAlmostEqual(abs(mean), 0)
        self.assertAlmostEqual(second.real - abs(mean) ** 2, 1)
        self.assertGreater(np.linalg.norm(assigned - P @ assigned @ P), 0)

    def test_overlap_solvable_despite_noncommutation(self):
        j = P - R
        self.assertGreater(np.linalg.norm(comm(P, R)), 0)
        self.assertGreater(np.linalg.norm(comm(j, P)), 0)
        self.assertGreater(np.linalg.norm(comm(j, R)), 0)
        np.testing.assert_allclose(P @ P @ P, P)
        np.testing.assert_allclose(R @ (-R) @ R, -R)
        np.testing.assert_allclose(P - R, j)
        # The two supported one-dimensional Hermitian spaces span exactly P,R.
        self.assertEqual(np.linalg.matrix_rank(np.column_stack((P.ravel(), R.ravel()))), 2)
        # Y annihilates both compressions, so Tr(YJ') != 0 excludes J'=Y.
        np.testing.assert_allclose(P @ Y @ P, 0, atol=1e-14)
        np.testing.assert_allclose(R @ Y @ R, 0, atol=1e-14)
        self.assertAlmostEqual(np.trace(Y @ Y).real, 2)
        self.assertAlmostEqual(np.trace(Y @ j).real, 0)

    def test_energy_rate_realization_and_balance(self):
        energy = (I + (X + Z) / np.sqrt(2)) / 2
        h = Y / np.sqrt(2)
        j = 1j * comm(h, energy)
        np.testing.assert_allclose(j, P - R, atol=1e-14)
        np.testing.assert_allclose(1j * comm(h, I - energy), -j, atol=1e-14)
        np.testing.assert_allclose(energy @ energy, energy, atol=1e-14)

if __name__ == '__main__':
    unittest.main()
