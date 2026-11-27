"""Finite controls of selection and modular claims; not proofs for type III."""
import unittest
import numpy as np

I = np.eye(2, dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
E01 = np.array([[0, 1], [0, 0]], dtype=complex)


def pow_i(rho, s):
    vals, vecs = np.linalg.eigh(rho)
    return (vecs * np.exp(1j*s*np.log(vals))) @ vecs.conj().T


def entropy(p):
    return -p*np.log(p)-(1-p)*np.log(1-p)


def dephase(a):
    return (a+Z@a@Z)/2


def d_t(a, t, gamma):
    return dephase(a)+np.exp(-gamma*t)*(a-dephase(a))


class ModularSelectionAudit(unittest.TestCase):
    def test_three_criteria_leave_inequivalent_states(self):
        for p in (1/8, 1/4, 3/4, 7/8):
            rho = np.diag([p, 1-p])
            self.assertLessEqual(entropy(p), entropy(1/4)+1e-15)
            for s in (-1.1, .7):
                u = pow_i(rho, s)
                np.testing.assert_allclose(u@Z@u.conj().T, Z, atol=1e-14)
                np.testing.assert_allclose(u@E01@u.conj().T,
                    np.exp(1j*s*np.log(p/(1-p)))*E01, atol=1e-14)
            np.testing.assert_allclose(d_t(rho, 3, .8), rho, atol=1e-14)
        self.assertNotAlmostEqual(2*(1/8)-1, 2*(1/4)-1)
        self.assertGreater(abs(np.exp(1j*.7*np.log((1/8)/(7/8)))-1), .1)

    def test_dephasing_is_random_unitary_semigroup(self):
        # Random-unitary Kraus weights demonstrate complete positivity.
        a = np.array([[1, 2+3j], [2-3j, 4]], dtype=complex)
        t, u, gamma = .7, 1.1, .8
        lam = np.exp(-gamma*t)
        kraus = (np.sqrt((1+lam)/2)*I, np.sqrt((1-lam)/2)*Z)
        np.testing.assert_allclose(sum(k.conj().T@k for k in kraus), I)
        np.testing.assert_allclose(sum(k.conj().T@a@k for k in kraus), d_t(a,t,gamma))
        np.testing.assert_allclose(d_t(d_t(a,t,gamma),u,gamma), d_t(a,t+u,gamma))
        np.testing.assert_allclose(d_t(a,t,gamma)[0,1], np.exp(-gamma*t)*a[0,1])

    def test_full_generator_sign_and_stationary_vector(self):
        p = .2
        r = np.array([p, 1-p])
        # Matrix units E_ij diagonalize left-right log difference.
        k = np.array([-np.log(r[i])+np.log(r[j]) for i in range(2) for j in range(2)])
        np.testing.assert_allclose(np.sort(k), [-np.log(4), 0, 0, np.log(4)])
        self.assertGreater(np.min(-np.log(r)), 0)  # subsystem -log rho is different
        rho = np.diag(r)
        root = np.diag(np.sqrt(r))
        for s in (-1, 2):
            np.testing.assert_allclose(pow_i(rho,s)@root@pow_i(rho,-s), root, atol=1e-14)

    def test_cyclic_separating_vector_decomposes_and_restricts_mixed(self):
        p = .3
        omega = np.array([np.sqrt(p), 0, 0, np.sqrt(1-p)])
        # A⊗I applied to omega is an invertible linear map from A entries
        # to vectors when both Schmidt coefficients are nonzero.
        basis = [np.eye(2)[[i]].T @ np.eye(2)[[j]] for i in range(2) for j in range(2)]
        matrix = np.column_stack([np.kron(e,I)@omega for e in basis])
        self.assertGreater(abs(np.linalg.det(matrix)), 0)
        partial = omega.reshape(2,2)@omega.reshape(2,2).conj().T
        np.testing.assert_allclose(partial, np.diag([p,1-p]))
        self.assertLess(np.trace(partial@partial).real, 1)

    def test_natural_cone_not_preserved_by_arbitrary_left_action(self):
        a = 1j*I
        v = a@I
        self.assertFalse(np.allclose(v,v.conj().T))
        # Difference of positive matrices must be self-adjoint, so iI is excluded.
        self.assertFalse(np.allclose(v, v.conj().T))

    def test_cocycle_triangle_noncommuting(self):
        x=np.array([[0,1],[1,0]],dtype=complex)
        y=np.array([[0,-1j],[1j,0]],dtype=complex)
        states=[(I+.4*z)/2 for z in (x,y,Z)]
        a,b,c=states; s=.71
        self.assertGreater(np.linalg.norm(a@b-b@a), .01)
        coc=lambda r,q: pow_i(r,s)@pow_i(q,-s)
        np.testing.assert_allclose(coc(c,b)@coc(b,a)@coc(a,c),I,atol=1e-14)


if __name__ == '__main__':
    unittest.main()
