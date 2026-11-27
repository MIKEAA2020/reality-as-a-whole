"""Quantitative locality and physical-sector balance controls."""
import unittest
import numpy as np
import sympy as sp

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Z=np.diag([1.,-1.]).astype(complex)
P=(I+Z)/2
Q=P.copy()


class IncidenceBalanceRigorTests(unittest.TestCase):
    def test_original_pseudoinverse_and_exact_local_distance(self):
        pa=np.kron(P,I); pb=np.kron(I,Q); S=pa+pb
        vals,vecs=np.linalg.eigh(S)
        inv=np.zeros_like(vals)
        inv[vals>1e-12]=1/np.sqrt(vals[vals>1e-12])
        half=(vecs*inv)@vecs.conj().T
        global_effect=half@pa@half
        np.testing.assert_allclose(global_effect,np.kron(P,I-Q/2),atol=1e-14)
        optimum=np.kron(.75*P,I)
        self.assertAlmostEqual(np.linalg.norm(global_effect-optimum,2),.25)
        rng=np.random.default_rng(2026)
        for _ in range(100):
            raw=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
            f=(raw+raw.conj().T)/2
            self.assertGreaterEqual(np.linalg.norm(global_effect-np.kron(f,I),2),.25-1e-14)

    def test_product_state_remote_change(self):
        effect=np.kron(P,I-Q/2)
        a=np.diag([.8,.2]); b0=np.diag([.3,.7]); b1=np.diag([.9,.1])
        z0=np.trace(np.kron(a,b0)@effect).real
        z1=np.trace(np.kron(a,b1)@effect).real
        self.assertAlmostEqual(z0,.8*(1-.3/2))
        self.assertAlmostEqual(z1,.8*(1-.9/2))
        self.assertAlmostEqual(z1-z0,-.8*(.9-.3)/2)
        self.assertAlmostEqual(np.trace(a@P).real,.8)

    def test_full_space_zero_sum_requires_scalar_local_terms(self):
        # Exhaustive symbolic form of Hermitian qubit operators in Pauli basis.
        aa,ax,ay,az,bb,bx,by,bz=sp.symbols('aa ax ay az bb bx by bz',real=True)
        i=sp.eye(2); x=sp.Matrix([[0,1],[1,0]])
        y=sp.Matrix([[0,-sp.I],[sp.I,0]]); z=sp.diag(1,-1)
        A=aa*i+ax*x+ay*y+az*z; B=bb*i+bx*x+by*y+bz*z
        total=sp.kronecker_product(A,i)+sp.kronecker_product(i,B)
        solution=sp.linsolve(list(total),(aa,ax,ay,az,bb,bx,by,bz))
        self.assertEqual(solution,{(-bb,0,0,0,bb,0,0,0)})

    def test_sector_balance_coherence_and_admissible_operations(self):
        physical=(np.eye(4)+np.kron(Z,Z))/2
        total=np.kron(Z,I)-np.kron(I,Z)
        np.testing.assert_allclose(total@physical,np.zeros((4,4)),atol=1e-14)
        bell=np.array([1.,0.,0.,1.])/np.sqrt(2)
        np.testing.assert_allclose(physical@bell,bell,atol=1e-14)
        other=np.array([0.,1.,0.,0.])
        np.testing.assert_allclose(total@other,2*other,atol=1e-14)
        xb=np.kron(I,X); xaxb=np.kron(X,X); zb=np.kron(I,Z)
        self.assertGreater(np.linalg.norm((np.eye(4)-physical)@xb@physical),.9)
        np.testing.assert_allclose((np.eye(4)-physical)@xaxb@physical,np.zeros((4,4)),atol=1e-14)
        np.testing.assert_allclose((np.eye(4)-physical)@zb@physical,np.zeros((4,4)),atol=1e-14)


if __name__ == '__main__':
    unittest.main()
