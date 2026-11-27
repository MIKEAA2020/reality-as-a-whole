"""Finite controls for the source-target crosswalk; not a gravity proof."""
import unittest
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
P0 = (I+Z)/2
P1 = (I-Z)/2


def gibbs(beta, e):
    return np.diag([1., np.exp(-beta*e)]) / (1+np.exp(-beta*e))


def power(rho, s):
    vals, vecs = np.linalg.eigh(rho)
    return (vecs*np.exp(1j*s*np.log(vals))) @ vecs.conj().T


class CrosswalkChecks(unittest.TestCase):
    def test_cocycle_but_distinct_states(self):
        e, b1, b2, s = 1.3, .4, 1.7, .71
        r1, r2 = gibbs(b1,e), gibbs(b2,e)
        cocycle = power(r2,s) @ power(r1,-s)
        flow1 = power(r1,s) @ X @ power(r1,-s)
        flow2 = power(r2,s) @ X @ power(r2,-s)
        np.testing.assert_allclose(flow2, cocycle @ flow1 @ cocycle.conj().T, atol=1e-14)
        self.assertGreater(abs(np.trace((r1-r2)@P0)), .1)
        self.assertGreater(np.linalg.norm(np.linalg.eigvalsh(r1)-np.linalg.eigvalsh(r2)), .1)
        self.assertAlmostEqual(np.trace(r1@P0).real, 1/(1+np.exp(-b1*e)))

    def test_instruments_same_probabilities_different_posts(self):
        rho = P0
        for p in (P0,P1):
            k1, k2 = p, X@p
            np.testing.assert_allclose(k1.conj().T@k1, k2.conj().T@k2, atol=0)
            self.assertAlmostEqual(np.trace(k1@rho@k1.conj().T).real,
                                   np.trace(k2@rho@k2.conj().T).real)
        np.testing.assert_allclose(P0@rho@P0, P0, atol=0)
        np.testing.assert_allclose(X@P0@rho@P0@X, P1, atol=0)

    def test_chsh_singlet(self):
        singlet = np.array([0,1,-1,0],dtype=complex)/np.sqrt(2)
        b0, b1 = (Z+X)/np.sqrt(2), (Z-X)/np.sqrt(2)
        operator = np.kron(Z,b0)+np.kron(Z,b1)+np.kron(X,b0)-np.kron(X,b1)
        self.assertAlmostEqual(np.vdot(singlet,operator@singlet).real, -2*np.sqrt(2))
        np.testing.assert_allclose(np.kron(Z,I)@np.kron(I,b0), np.kron(I,b0)@np.kron(Z,I), atol=0)

    def test_null_contractions_fix_symmetric_tensor_up_to_metric(self):
        # Algebraic 3+1 dimensional check: enough null vectors give rank 9
        # among the 10 real symmetric components, with metric as kernel.
        directions = []
        for axis in range(3):
            v = np.zeros(3); v[axis] = 1
            directions.extend((v, -v))
        for a in range(3):
            for b in range(a+1,3):
                for sa in (-1,1):
                    for sb in (-1,1):
                        v=np.zeros(3); v[a]=sa/np.sqrt(2); v[b]=sb/np.sqrt(2)
                        directions.append(v)
        pairs=[(i,j) for i in range(4) for j in range(i,4)]
        rows=[]
        for d in directions:
            k=np.r_[1.,d]
            rows.append([k[i]*k[j]*(1 if i==j else 2) for i,j in pairs])
        mat=np.array(rows)
        self.assertEqual(np.linalg.matrix_rank(mat, tol=1e-10), 9)
        metric=np.diag([-1.,1.,1.,1.])
        vec=np.array([metric[i,j] for i,j in pairs])
        np.testing.assert_allclose(mat@vec, np.zeros(len(rows)), atol=1e-14)


if __name__ == '__main__':
    unittest.main()
