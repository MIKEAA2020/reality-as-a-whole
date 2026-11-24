"""Checks for the linked popular article and a directional-jet construction.

The jet and matrix model are formal analogies; no physical subject is assumed.
"""
import math
import unittest
import numpy as np
from verification.zero_five_ray_record_current_unification_test import q,ns,axis

I2=np.eye(2,dtype=complex);I4=np.eye(4,dtype=complex);I16=np.eye(16,dtype=complex)
b=np.eye(4,dtype=complex)
N=[np.outer(b[0],b[i].conj()) for i in range(1,4)]
X=[u+u.conj().T for u in N]
Q=[np.kron(x,I4)-np.kron(I4,x.T) for x in X]
C=sum(x@x for x in Q)
PHI=np.eye(4,dtype=complex).reshape(-1)/2
PAULIS=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.])]
# Transform first qubit on the second four-level factor to obtain a singlet.
V=np.kron(I4,np.kron(np.array([[0.,-1.],[1.,0.]]),I2))


def comm(A,B):return A@B-B@A


def sphere_outcomes():
    v=V@PHI;Cnew=V@C@V.conj().T
    Bop=sum(z*s for z,s in zip(axis,PAULIS))
    effects=[(I2+Bop)/2,(I2-Bop)/2]
    table=np.zeros((3,2));disturb=[]
    for i,(qi,n) in enumerate(zip(q,ns)):
        pi=(I2+sum(z*s for z,s in zip(n,PAULIS)))/2
        k=np.kron(np.kron(math.sqrt(2*qi)*pi,I2),I4)
        a=k@v;prob=np.vdot(a,a).real
        disturb.append(np.vdot(a,Cnew@a).real/prob)
        for j,e in enumerate(effects):
            E=np.kron(I4,np.kron(e,I2))
            table[i,j]=np.vdot(a,E@a).real
    return table,np.array(disturb)


class ZeroArticleJetDualPairTests(unittest.TestCase):
    def test_equal_values_at_origin_do_not_fix_derivatives(self):
        a=np.array([1.,-2.,3.]);v=np.array([.3,.2,-.4]);B=np.diag([3.,2.,-1.])
        def f(x):return a@x+x@B@x/2
        self.assertEqual(f(np.zeros(3)),0)
        self.assertNotEqual(float(a@v),0)
        for h in (1e-2,1e-3,1e-4):
            quotient=f(h*v)/h
            self.assertAlmostEqual(quotient-a@v,h*(v@B@v)/2,places=12)
        # The zero function has the same value f(0)=0 but directional
        # derivative 0, so the value alone does not determine the jet.

    def test_formal_nilpotent_jets_and_quantum_selfadjoint_obstruction(self):
        zero=np.zeros((4,4),complex)
        for a in N:
            for c in N:np.testing.assert_array_equal(a@c,zero)
            self.assertGreater(np.linalg.norm(a),0)
            self.assertGreater(np.linalg.norm(a.conj().T@a),0)
            self.assertGreater(np.linalg.norm(a-a.conj().T),0)
        # Self-adjoint A with A²=0 implies ||Aψ||²=<ψ,A²ψ>=0 for
        # every ψ, hence A=0. The N_i evade this by being non-Hermitian.
        for x in X:
            np.testing.assert_allclose(x,x.conj().T,atol=1e-14)
            self.assertGreater(np.linalg.norm(x@x),1)

    def test_directions_and_rotation_are_intrinsic_to_the_supplied_model(self):
        a=np.array([.3,.4,math.sqrt(.75)]);c=np.array([-.4,.3,math.sqrt(.75)])
        A=sum(z*x for z,x in zip(a,X));B=sum(z*x for z,x in zip(c,X))
        self.assertAlmostEqual(np.trace(A@B).real,2*(a@c),places=12)
        parity=np.diag([1.,-1.,-1.,-1.])
        np.testing.assert_allclose(parity@A@parity,-A,atol=1e-14)
        t=.42;R=np.array([[math.cos(t),-math.sin(t),0],[math.sin(t),math.cos(t),0],[0,0,1.]])
        U=np.eye(4);U[1:,1:]=R
        np.testing.assert_allclose(U@A@U.T,sum(z*x for z,x in zip(R@a,X)),atol=1e-14)
        np.testing.assert_allclose(np.kron(U,U.conj())@PHI,PHI,atol=1e-14)

    def test_three_balance_constraints_uniquely_fix_identity_pair(self):
        for v in Q:np.testing.assert_allclose(v@PHI,0,atol=1e-14)
        # Products of X_i generate all 16 matrix units, not just a
        # sample of an arbitrary numerical null-space solver.
        p0=(sum(x@x for x in X)-I4)/2
        np.testing.assert_allclose(p0,np.outer(b[0],b[0]),atol=1e-14)
        for i in range(3):
            np.testing.assert_allclose(X[i]@p0,np.outer(b[i+1],b[0]),atol=1e-14)
            for j in range(3):
                np.testing.assert_allclose(X[i]@p0@X[j],np.outer(b[i+1],b[j+1]),atol=1e-14)
        values=np.linalg.eigvalsh(C)
        np.testing.assert_allclose(values,[0]+[2]*11+[6]*3+[8],atol=1e-12)
        self.assertGreater(np.linalg.norm(comm(Q[0],Q[1])),1)
        # Noncommuting constraints can nevertheless share this unique zero.

    def test_directional_local_values_and_exact_pairwise_cancellation(self):
        n=np.array([.6,.8,0]);A=sum(z*x for z,x in zip(n,X));
        evals=np.linalg.eigvalsh(A)
        np.testing.assert_allclose(evals,[-1,0,0,1],atol=1e-14)
        Qn=np.kron(A,I4)-np.kron(I4,A.T)
        np.testing.assert_allclose(Qn@PHI,0,atol=1e-14)
        # The local Φ marginal is I/4; hence plus/minus occur with 1/4
        # each in the standard quantum readout, zero with 1/2.
        self.assertAlmostEqual(np.trace(PHI.reshape(4,4)@PHI.reshape(4,4).conj().T@A@A).real,.5)

    def test_same_state_recovers_actual_five_ray_born_table(self):
        table,_=sphere_outcomes()
        expected=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        np.testing.assert_allclose(table,expected,atol=1e-13)
        np.testing.assert_allclose(table.sum(axis=1),q,atol=1e-13)
        np.testing.assert_allclose(table.sum(axis=0),[.5,.5],atol=1e-13)
        # State/instrument/factorization and the Born rule are inputs.

    def test_naive_local_sphere_readout_leaves_balance_kernel(self):
        _,dist=sphere_outcomes()
        np.testing.assert_allclose(dist,[1,7/4,553/361],atol=1e-12)
        self.assertAlmostEqual(sum(qi*d for qi,d in zip(q,dist)),59/38,places=12)
        self.assertGreater(np.linalg.norm(comm(Q[0],np.kron(np.kron(PAULIS[0],I2),I4))),1)
        # Positive C expectation: cannot claim the unextended local
        # measurement conserves the three constraints.

    def test_zero_trace_is_not_whole_energy_or_experience(self):
        # Offset or rescaling does not follow from a matrix trace: this is a
        # finite algebraic control, not a definition of gravity or valence.
        A=X[0];self.assertAlmostEqual(np.trace(A).real,0)
        self.assertNotEqual(float(np.trace(A@A).real),0)
        self.assertAlmostEqual(np.vdot(PHI,np.kron(A,I4)@PHI).real,0)
        self.assertAlmostEqual(np.vdot(PHI,np.kron(A,I4)@np.kron(A,I4)@PHI).real,.5)

if __name__=='__main__':unittest.main()
