"""Finite controls for cross-field leads, not BC or FUP proofs."""
import math
import unittest
import numpy as np


class CrossfieldControls(unittest.TestCase):
    def test_arithmetic_cutoff_and_tail(self):
        beta, n = 2., 5000
        z = math.pi**2/6
        weights = np.arange(1, n+1, dtype=float)**(-beta)
        zn = weights.sum()
        self.assertLessEqual(z-zn, n**(1-beta)/(beta-1))
        # TV between full and zero-extended cutoff normalized distribution.
        tv = (np.abs(weights/z - weights/zn).sum() + (z-zn)/z)/2
        self.assertAlmostEqual(tv, (z-zn)/z, places=13)
        for p in (2, 3, 5):
            prob = weights[p-1::p].sum()/zn
            # Finite-cutoff TV controls each event probability.
            self.assertLessEqual(abs(prob-p**(-beta)), tv+1e-13)
        joint = weights[5::6].sum()/zn
        self.assertLessEqual(abs(joint-6**(-beta)), tv+1e-13)

    def test_modular_phase_arithmetic(self):
        beta, hbar, t = 1.4, .7, 1.3
        ns = np.arange(1, 10, dtype=float)
        weights = ns**(-beta); weights /= weights.sum()
        s = -t/(beta*hbar)
        modular = np.exp(1j*s*(np.log(weights[2])-np.log(weights[6])))
        heisenberg = np.exp(1j*t*(np.log(3)-np.log(7))/hbar)
        np.testing.assert_allclose(modular, heisenberg, atol=1e-14)

    def test_fractal_product_norm_and_sharpness(self):
        j = np.arange(5)
        f = np.exp(-2j*np.pi*np.outer(j,j)/5)/np.sqrt(5)
        restricted = f[np.ix_([0, 1], [0, 1])]
        u, singular, vh = np.linalg.svd(restricted)
        lam = math.sqrt((2+2*math.cos(math.pi/5))/5)
        self.assertAlmostEqual(singular[0], lam)
        delta = -math.log(lam)/math.log(5)
        self.assertGreater(delta, 0)
        product = np.kron(np.kron(restricted, restricted), restricted)
        vector = np.kron(np.kron(vh[0].conj(), vh[0].conj()), vh[0].conj())
        self.assertAlmostEqual(np.linalg.norm(product, 2), lam**3)
        self.assertAlmostEqual(np.linalg.norm(product@vector), lam**3)
        self.assertAlmostEqual(lam**3, 125**(-delta))

    def test_subgroup_control(self):
        j = np.arange(5)
        f = np.exp(-2j*np.pi*np.outer(j,j)/5)/np.sqrt(5)
        ft = np.kron(f, f)
        # H={(a,0)}; annihilator H-perp={(0,b)} in the product group.
        h = np.array([0,5,10,15,20]); hp = np.arange(5)
        v = np.ones(5)/np.sqrt(5)
        output = ft[np.ix_(hp,h)] @ v
        self.assertAlmostEqual(np.linalg.norm(output), 1.)
        self.assertAlmostEqual(np.linalg.norm(ft[np.ix_(hp,h)], 2), 1.)


if __name__ == '__main__':
    unittest.main()
