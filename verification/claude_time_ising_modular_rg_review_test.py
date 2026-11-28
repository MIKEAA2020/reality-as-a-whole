"""Exact three-site Ising decimation versus modular flow and instruments.

This is a finite effective spin model, not a derivation of spacetime, zero
energy, subjects, modular physical time, or a general quantum-field RG theorem.
"""
import math
import unittest
import numpy as np
import sympy as sp
from scipy.linalg import expm

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)

def k3(a,b,c): return np.kron(np.kron(a,b),c)
def partial2(A): return np.einsum('abcdbf->acdf',A.reshape([2]*6)).reshape(4,4)
def embed13(A): return np.einsum('acdf,be->abcdef',A.reshape([2]*4),I).reshape(8,8)
def adjoint_L(H,A): return -1j*(H@A-A@H)
def modular(rho,A,s):
    d=np.diag(rho).real
    unit=np.diag(np.exp(1j*s*np.log(d)))
    return unit@A@unit.conj().T

def build(K):
    A=k3(Z,Z,I)+k3(I,Z,Z)
    H=-K*A
    rho=expm(-H); rho=rho/np.trace(rho)
    red=partial2(rho); Kp=.5*np.log(np.cosh(2*K)); Hred=-Kp*np.kron(Z,Z)
    sq=np.diag(np.sqrt(np.diag(rho).real)); inv=np.diag(1/np.sqrt(np.diag(red).real))
    R=lambda B: inv@partial2(sq@B@sq)@inv
    return H,rho,red,Kp,Hred,R

class IsingModularRGTests(unittest.TestCase):
    def test_decimation_and_independent_transfer_matrix(self):
        for K in (.01,.5,1.2,2.):
            _,rho,red,Kp,_,_=build(K)
            expected=expm(Kp*np.kron(Z,Z));expected/=np.trace(expected)
            np.testing.assert_allclose(red,expected,atol=1e-14)
            self.assertAlmostEqual(np.tanh(Kp),np.tanh(K)**2,places=13)
            T=np.array([[np.exp(K),np.exp(-K)],[np.exp(-K),np.exp(K)]])
            eig=np.linalg.eigvalsh(T)
            self.assertAlmostEqual(eig[0]/eig[1],np.tanh(K),places=13)
            self.assertLess(Kp,K)

    def test_continuous_interpolation_and_derived_beta(self):
        def flow(K,l): return np.arctanh(np.tanh(K)**np.exp(l))
        def beta(K):return np.sinh(K)*np.cosh(K)*np.log(np.tanh(K))
        for K in (.2,.5,1.2):
            self.assertAlmostEqual(flow(K,np.log(2)),.5*np.log(np.cosh(2*K)),places=13)
            self.assertAlmostEqual(flow(flow(K,.3),.5),flow(K,.8),places=13)
            h=1e-5;diff=(flow(K,h)-flow(K,-h))/(2*h)
            self.assertAlmostEqual(diff,beta(K),places=9)
            self.assertLess(beta(K),0)

    def test_natural_embedding_generator_mismatch_exact(self):
        for K in (.1,.5,1.):
            H,_,_,Kp,Hred,_=build(K)
            full=adjoint_L(H,k3(X,I,I)); coarse=embed13(adjoint_L(Hred,np.kron(X,I)))
            discrepancy=full-coarse
            expected=-2*K*k3(Y,Z,I)+2*Kp*k3(Y,I,Z)
            np.testing.assert_allclose(discrepancy,expected,atol=1e-14)
            self.assertAlmostEqual(np.linalg.norm(discrepancy,2),2*(K+Kp),places=12)

    def test_state_preserving_cp_coarse_map_and_generators(self):
        K=.5;H,rho,red,Kp,Hred,R=build(K)
        self.assertTrue(np.all(np.linalg.eigvalsh(rho)>0))
        np.testing.assert_allclose(R(np.eye(8)),np.eye(4),atol=1e-14)
        rng=np.random.default_rng(731)
        for _ in range(10):
            a=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8));a=a@a.conj().T
            self.assertGreaterEqual(np.linalg.eigvalsh(R(a)).min(),-1e-12)
            self.assertAlmostEqual(np.trace(red@R(a)).real,np.trace(rho@a).real,places=11)
        # Explicit Kraus operators for complete positivity and unitality.
        sq=np.diag(np.sqrt(np.diag(rho).real));inv=np.diag(1/np.sqrt(np.diag(red).real));ks=[]
        for b in (0,1):
            embed=np.zeros((8,4),complex)
            for a in (0,1):
                for c in (0,1):embed[4*a+2*b+c,2*a+c]=1
            ks.append(sq@embed@inv)
        np.testing.assert_allclose(sum(k.conj().T@k for k in ks),np.eye(4),atol=1e-14)
        for A in (k3(X,I,I),k3(Y,Z,I)):
            np.testing.assert_allclose(R(A),sum(k.conj().T@A@k for k in ks),atol=1e-14)
        c=np.cosh(K)/np.sqrt(np.cosh(2*K));d=np.sinh(K)/np.sqrt(np.cosh(2*K))
        np.testing.assert_allclose(R(k3(X,I,I)),c*np.kron(X,I),atol=1e-14)
        np.testing.assert_allclose(R(k3(Y,Z,I)),d*np.kron(Y,Z),atol=1e-14)
        mismatch=R(adjoint_L(H,k3(X,I,I)))-adjoint_L(Hred,R(k3(X,I,I)))
        expected=-2*(K*d-Kp*c)*np.kron(Y,Z)
        np.testing.assert_allclose(mismatch,expected,atol=1e-14)
        self.assertAlmostEqual(np.linalg.norm(mismatch,2),.0257225671266,places=12)

    def test_finite_modular_flow_exact_and_nonuniform_limit(self):
        for K,s in ((.2,.4),(.5,1.1),(1.,-.7)):
            H,rho,red,Kp,Hred,R=build(K)
            A=k3(X,I,I); c=np.cosh(K)/np.sqrt(np.cosh(2*K)); d=np.sinh(K)/np.sqrt(np.cosh(2*K))
            observed=R(modular(rho,A,s))-modular(red,R(A),s)
            aa=c*(np.cos(2*K*s)-np.cos(2*Kp*s))
            bb=-d*np.sin(2*K*s)+c*np.sin(2*Kp*s)
            np.testing.assert_allclose(observed,aa*np.kron(X,I)+bb*np.kron(Y,Z),atol=1e-13)
            self.assertAlmostEqual(np.linalg.norm(observed,2),np.hypot(aa,bb),places=12)
        norms=[]
        for K in (.1,.05,.025):
            _,rho,red,_,_,R=build(K);A=k3(X,I,I);s=1.
            norms.append(np.linalg.norm(R(modular(rho,A,s))-modular(red,R(A),s),2))
        self.assertLess(norms[-1],norms[-2]);self.assertLess(norms[-2],norms[-3])
        # Pointwise high-temperature convergence is not uniform over all s.
        K=.01;_,rho,red,_,_,R=build(K);A=k3(X,I,I);s=np.pi/(2*K)
        self.assertGreater(np.linalg.norm(R(modular(rho,A,s))-modular(red,R(A),s),2),1.99)

    def test_linear_modular_reparameterization_cannot_intertwine(self):
        # Cosine matching requires q=±K/Kp; then the sine amplitude is wrong.
        for K in (.1,.5,1.):
            _,rho,red,Kp,_,R=build(K);A=k3(X,I,I)
            for q in (K/Kp,-K/Kp):
                s=.31
                defect=R(modular(rho,A,s))-modular(red,R(A),q*s)
                self.assertGreater(np.linalg.norm(defect,2),1e-5)
            # Matching only first derivatives with a different q still fails at finite s.
            q=K*np.tanh(K)/Kp
            s=.31
            defect=R(modular(rho,A,s))-modular(red,R(A),q*s)
            self.assertGreater(np.linalg.norm(defect,2),1e-6)

    def test_positive_infinitesimal_defect_analytic_control(self):
        k=sp.symbols('k',real=True)
        f=k*sp.tanh(k)-sp.log(sp.cosh(2*k))/2
        target=sp.sech(k)**2*(k-sp.tanh(k)/(1+sp.tanh(k)**2))
        self.assertEqual(sp.simplify(sp.diff(f,k)-target),0)
        self.assertEqual(sp.limit(f/k**4,k,0),sp.Rational(1,3))
        self.assertEqual(sp.limit(2*sp.cosh(k)/sp.sqrt(sp.cosh(2*k))*f/k**4,k,0),sp.Rational(2,3))
        for K in (.001,.1,.5,1.,4.):self.assertGreater(K*np.tanh(K)-.5*np.log(np.cosh(2*K)),0)

    def test_classical_modular_triviality_but_rg_is_nontrivial(self):
        for K in (.2,.5,1.):
            _,rho,red,Kp,_,R=build(K)
            diag=np.diag(np.arange(8,dtype=float))
            for s in (-1.,.3,2.):
                np.testing.assert_allclose(modular(rho,diag,s),diag,atol=1e-13)
                np.testing.assert_allclose(modular(red,R(diag),s),R(diag),atol=1e-13)
            self.assertNotAlmostEqual(K,Kp,places=8)

    def test_coarse_channel_does_not_determine_instrument(self):
        K=.5;_,rho,red,_,_,_=build(K)
        def instrument(state,P):
            p=k3(I,P,I)
            return partial2(p@state@p)
        zproj=[(I+Z)/2,(I-Z)/2];xproj=[(I+X)/2,(I-X)/2]
        for ps in (zproj,xproj):
            np.testing.assert_allclose(sum(instrument(rho,p) for p in ps),red,atol=1e-14)
        pz=instrument(rho,zproj[0]);px=instrument(rho,xproj[0]); obs=np.kron(Z,I)
        self.assertAlmostEqual(np.trace(pz).real,.5,places=13)
        self.assertAlmostEqual(np.trace(px).real,.5,places=13)
        self.assertAlmostEqual((np.trace(pz@obs)/np.trace(pz)).real,np.tanh(K),places=13)
        self.assertAlmostEqual((np.trace(px@obs)/np.trace(px)).real,0.,places=13)
        rng=np.random.default_rng(17)
        v=rng.normal(size=8)+1j*rng.normal(size=8);v/=np.linalg.norm(v);other=np.outer(v,v.conj())
        for ps in (zproj,xproj):
            np.testing.assert_allclose(sum(instrument(other,p) for p in ps),partial2(other),atol=1e-13)

if __name__=='__main__':unittest.main()
