"""Matrix and cutoff controls for the foundations audit, not type-III proofs."""
import unittest
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)


def hermitian_exp(h, coefficient):
    vals, vectors = np.linalg.eigh(h)
    return (vectors * np.exp(coefficient*vals)) @ vectors.conj().T


def hermitian_log(rho):
    vals, vectors = np.linalg.eigh(rho)
    assert np.all(vals > 0)
    return (vectors*np.log(vals))@vectors.conj().T


def flow(h, a, t, hbar=1.):
    u = hermitian_exp(h, 1j*t/hbar)
    return u@a@u.conj().T


def opnorm(a):
    return np.linalg.norm(a, ord=2)


class FoundationsAudit(unittest.TestCase):
    def test_modular_fixed_point_is_not_state_selection(self):
        # On Hilbert-Schmidt space, tracial rho gives Delta = identity.
        r = np.array([.5, .5])
        delta = np.array([r[i]/r[j] for i in range(2) for j in range(2)])
        np.testing.assert_allclose(delta, np.ones(4))
        for p in (.1, .3, .5, .8):
            eigens = np.array([p, 1-p])
            omega = np.sqrt(eigens)
            np.testing.assert_allclose((eigens/eigens)*omega, omega)
            self.assertGreater(np.linalg.det(np.diag(eigens)), 0)
        # Unequal Schmidt coefficients are faithful but not maximally entangled.
        self.assertNotAlmostEqual(.1, .9)

    def test_inequivalent_abelian_states_have_same_trivial_flow(self):
        p, q = .2, .3
        # C² has exactly identity and swap as unital star automorphisms.
        self.assertNotAlmostEqual(p, q)
        self.assertNotAlmostEqual(p, 1-q)
        for s in (-2., .8):
            for r in (np.diag([p,1-p]),np.diag([q,1-q])):
                u=hermitian_exp(hermitian_log(r), 1j*s)
                np.testing.assert_allclose(u@Z@u.conj().T, Z, atol=1e-14)

    def test_closability_bad_boundedness_step(self):
        # Finite cutoffs sample a fixed infinite-dimensional construction.
        c=1/np.sqrt(np.pi**2/6)
        norms=[]
        for n in (4, 8, 16, 32):
            # lambda_n = 3/4 * 4^-n; a_n=(n+1)|n><n|.
            norm_a_omega=(n+1)*np.sqrt(.75)*2**(-n)
            # b=|v><0|; v_n=c/(n+1).
            norm_a_b_omega=(n+1)*(c/(n+1))*np.sqrt(.75)
            norms.append(norm_a_omega)
            self.assertAlmostEqual(norm_a_b_omega,c*np.sqrt(.75))
        self.assertLess(norms[-1], 1e-7)
        # a_n is self-adjoint, so the starred sequence also tends to zero.

    def test_removing_a_decorated_ancilla_for_a_specific_channel(self):
        gamma=.37
        k0=np.diag([1., np.sqrt(1-gamma)]).astype(complex)
        k1=np.array([[0,np.sqrt(gamma)],[0,0]],dtype=complex)
        rho=(I+.4*X+.2*Z)/2
        ancilla=(I+.25*Z)/2
        kraus=(k0,k1)
        np.testing.assert_allclose(sum(k.conj().T@k for k in kraus), I)
        target=sum(k@rho@k.conj().T for k in kraus)
        joint=np.kron(rho,ancilla)
        decorated=sum(np.kron(k,I)@joint@np.kron(k,I).conj().T for k in kraus)
        reduced=np.einsum('aibi->ab',decorated.reshape(2,2,2,2))
        np.testing.assert_allclose(reduced,target,atol=1e-14)
        self.assertGreater(opnorm(target-rho), .01)

    def test_exact_calibration_and_tracial_obstruction(self):
        h = .7*X + .3*Z
        beta=1.3
        rho=hermitian_exp(h,-beta)
        rho=rho/np.trace(rho)
        g=-hermitian_log(rho)/beta
        for t in (-2., .4, 3.):
            np.testing.assert_allclose(flow(g,Z,t),flow(h,Z,t), atol=1e-14)
        tracial=I/2
        g0=-hermitian_log(tracial)/beta
        self.assertGreater(opnorm(flow(g0,Z,.8)-flow(h,Z,.8)), .5)

    def test_noncommuting_mismatch_bound(self):
        h=.6*X + .4*Z
        rho=(I+.3*Z)/2
        beta=1.2; hbar=.9
        log_rho=hermitian_log(rho)
        g=-log_rho/beta
        d=log_rho+beta*h
        vals=np.linalg.eigvalsh(d)
        midpoint=(vals[0]+vals[-1])/2
        distance=opnorm(d-midpoint*I)
        self.assertGreater(opnorm(rho@h-h@rho), .1)
        for t in (-1., -.1, 0, .2, .9):
            error=opnorm(flow(g,Z,t,hbar)-flow(h,Z,t,hbar))
            bound=2*abs(t)*opnorm(Z)*distance/(beta*hbar)
            self.assertLessEqual(error,bound+1e-13)

    def test_exact_commuting_matrix_unit_error(self):
        beta, hbar, t=1.3, .8, .7
        r=np.array([.3,.7]); e=np.array([.2,1.1])
        rho=np.diag(r); h=np.diag(e)
        g=-hermitian_log(rho)/beta
        a=np.array([[0,1],[0,0]],dtype=complex)
        d=np.log(r)+beta*e
        expected=2*abs(np.sin(t*(d[0]-d[1])/(2*beta*hbar)))
        self.assertAlmostEqual(opnorm(flow(g,a,t,hbar)-flow(h,a,t,hbar)),expected)
        self.assertGreater(expected,.1)


if __name__ == '__main__':
    unittest.main()
