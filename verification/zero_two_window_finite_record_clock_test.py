"""Finite-data obstruction and transported instrument in the two-window model.

Regulated test only. Requires NumPy, e.g. PYTHONPATH=.arena/python-deps:.
The DFT is a finite unitary coordinate change, not a continuum slice clock.
"""
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model, theta_apply, initial


def root_data(model, h):
    n = len(model[0]); dim = 8*n
    eye = np.eye(dim, dtype=complex)
    theta = np.column_stack([theta_apply(model, eye[:, j].reshape(2, 2, 2, n), h).ravel()
                             for j in range(dim)])
    vals, vecs = np.linalg.eigh(theta)
    assert vals.min() > 0
    return vals, vecs


def propagator(vals, vecs, t):
    return (vecs * np.exp(1j*t*np.sqrt(vals))) @ vecs.conj().T


def sample_map(model, vals, vecs, times=(0, 40, 100)):
    """One alpha=0 slice, all 8 internal amplitudes; KG weight retained."""
    n = len(model[0]); omega = np.sqrt(vals)
    A = np.kron(np.eye(8), np.ones((1, n))/np.sqrt(2*np.pi*n))
    return np.vstack([(A @ vecs * (np.exp(1j*omega*t)/np.sqrt(2*omega))) @ vecs.conj().T
                      for t in times])


def invisible_pair(model, vals, vecs):
    R = sample_map(model, vals, vecs)
    _, s, vh = np.linalg.svd(R, full_matrices=True)
    rank = np.count_nonzero(s > s[0]*1e-10)
    K = vh[rank:].conj().T
    n = len(model[0]); U = propagator(vals, vecs, 100)
    mask = np.broadcast_to(np.arange(2)[None, :, None, None], (2, 2, 2, n)).ravel()
    B = mask[:, None] * (U @ K)
    ev, V = np.linalg.eigh(B.conj().T @ B)
    visible = vh[0].conj()
    return R, rank, (visible + K @ V[:, 0])/np.sqrt(2), (visible + K @ V[:, -1])/np.sqrt(2), ev


def sqrt_effect(E):
    vals, vecs = np.linalg.eigh(E)
    assert vals.min() > -1e-12 and vals.max() < 1+1e-12
    return (vecs * np.sqrt(np.clip(vals, 0, 1))) @ vecs.conj().T


def instrument(model, vals, vecs, state):
    """Lüders geometry-window hit/no-hit at 40, two memory z reads at 100."""
    n = len(model[0]); I = np.eye(n); E = model[2][1]
    ks = [np.kron(np.eye(8), sqrt_effect(I-E)), np.kron(np.eye(8), sqrt_effect(E))]
    u40 = propagator(vals, vecs, 40); u60 = propagator(vals, vecs, 60)
    # Full unitary change of regulator coordinates, not a single-slice map.
    F = np.fft.fft(np.eye(n), axis=0, norm='ortho')
    Q = np.kron(np.eye(8), F)
    masks = [np.broadcast_to(((np.arange(2)[:, None] == a) &
                              (np.arange(2)[None, :] == b))[None, :, :, None],
                             (2, 2, 2, n)).ravel() for a in (0, 1) for b in (0, 1)]
    probs = np.zeros((2, 2, 2)); changed = np.zeros_like(probs); errors = []
    for z, k in enumerate(ks):
        phi = u60 @ k @ u40 @ state
        phi_q = (Q @ u60 @ Q.conj().T) @ (Q @ k @ Q.conj().T) @ (Q @ u40 @ state)
        for j, mask in enumerate(masks):
            a, b = divmod(j, 2)
            post = mask * phi
            post_q = (Q @ np.diag(mask) @ Q.conj().T) @ phi_q
            probs[z, a, b] = np.vdot(post, post).real
            changed[z, a, b] = np.vdot(post_q, post_q).real
            errors.append(np.linalg.norm(post_q-Q@post))
    return probs, changed, max(errors)


class FiniteRecordClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = make_model(24)
        cls.spectra = [root_data(cls.model, h) for h in (0, 1)]

    def test_invisible_finite_complex_samples_and_distinct_records(self):
        vals, vecs = self.spectra[0]
        R, rank, x, y, ev = invisible_pair(self.model, vals, vecs)
        self.assertEqual(rank, 24)
        self.assertGreater(len(x)-rank, 0)
        self.assertAlmostEqual(np.linalg.norm(x), 1, places=12)
        self.assertAlmostEqual(np.linalg.norm(y), 1, places=12)
        self.assertGreater(np.linalg.norm(R@x), .01)
        self.assertLess(np.linalg.norm(R@(x-y)), 1e-12)
        self.assertLess(ev[0], 1e-11); self.assertGreater(ev[-1], 1-1e-11)
        n = len(self.model[0]); mask = np.broadcast_to(np.arange(2)[None,:,None,None], (2,2,2,n)).ravel()
        U = propagator(vals, vecs, 100)
        px = np.linalg.norm(mask*(U@x))**2
        py = np.linalg.norm(mask*(U@y))**2
        self.assertAlmostEqual(abs(px-py), .5, places=10)
        # Even when the same intervening geometry instrument is actually applied,
        # the two preparations give very different later M1 statistics.
        ax, _, _ = instrument(self.model, vals, vecs, x)
        ay, _, _ = instrument(self.model, vals, vecs, y)
        self.assertGreater(abs(ax[:,1,:].sum()-ay[:,1,:].sum()), .49)

    def test_same_transported_instrument_states_and_all_outcomes(self):
        v = initial(self.model).ravel()
        for vals, vecs in self.spectra:
            a, b, err = instrument(self.model, vals, vecs, v)
            self.assertAlmostEqual(a.sum(), 1, places=11)
            self.assertLess(np.max(abs(a-b)), 1e-12)
            self.assertLess(err, 1e-12)
            self.assertTrue(np.all(a >= 0))
            self.assertGreater(a[0].sum(), .05); self.assertGreater(a[1].sum(), .05)

    def test_intermediate_measurement_changes_the_records(self):
        v = initial(self.model).ravel(); changes = []
        for vals, vecs in self.spectra:
            a, _, _ = instrument(self.model, vals, vecs, v)
            n = len(self.model[0])
            without = (propagator(vals, vecs, 100) @ v).reshape(2,2,2,n)
            p0 = np.sum(abs(without[:,1,:,:])**2)
            changes.append(abs(a[:,1,:].sum()-p0))
        self.assertGreater(sum(changes)/2, .001)

    def test_preparation_and_instrument_grid_refinement(self):
        tables = []
        for n in (24, 40):
            model = make_model(n); v = initial(model).ravel()
            entries = []
            for h in (0, 1):
                vals, vecs = root_data(model, h)
                a, _, _ = instrument(model, vals, vecs, v)
                entries.append(a)
            tables.append(sum(entries)/2)
        self.assertLess(np.max(abs(tables[0]-tables[1])), .0003)
        self.assertAlmostEqual(tables[-1][1].sum(), .15956, places=4)

    def test_finite_sample_kernel_survives_refinement(self):
        for n in (16, 32):
            model = make_model(n); vals, vecs = root_data(model, 0)
            R, rank, x, y, _ = invisible_pair(model, vals, vecs)
            self.assertEqual(rank, 24)
            self.assertEqual(8*n-rank, 8*n-24)
            self.assertLess(np.linalg.norm(R@(x-y)), 1e-12)
            self.assertGreater(np.linalg.norm(x-y), .9)

if __name__ == '__main__':
    unittest.main()
