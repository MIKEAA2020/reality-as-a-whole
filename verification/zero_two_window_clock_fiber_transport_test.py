"""Finite cyclic control for the retained-output fiber identity.

Uses P/Q sectors selected from the old two-window grid, but a different
cyclic gate and clock, not the massive-cursor continuum Hamiltonian.
"""
import unittest
import numpy as np
from verification.zero_two_window_autonomous_support_dynamics_test import system


def ptr_clock(rho, a=4, n=8, ref=2):
    return np.einsum('irxjry->ixjy',rho.reshape(a,n,ref,a,n,ref)).reshape(a*ref,a*ref)


def product_ar_clock(rho_ar, clock, a=4, n=8, ref=2):
    return np.einsum('ixjy,rs->irxjsy',rho_ar.reshape(a,ref,a,ref),clock).reshape(a*n*ref,a*n*ref)


def density(v):return np.outer(v,v.conj())


def distance(a,b):
    delta=(a-b+(a-b).conj().T)/2
    return float(np.abs(np.linalg.eigvalsh(delta)).sum()/2)


def setup():
    _,B,P,Q,_,_=system(2,0)
    # Pick one vector from each actual orthogonal grid sector.
    q=Q[:,np.argmax(np.linalg.norm(Q,axis=0))];q=q/np.linalg.norm(q)
    basis=np.column_stack((B[:,0],q))
    p=basis.conj().T@P@basis; q=basis.conj().T@Q@basis
    X=np.array([[0,1],[1,0]],complex); h=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
    gate=(np.kron(p,np.eye(2))+np.kron(q,X))@np.kron(h,np.eye(2))
    n=8;S=np.roll(np.eye(n),1,axis=0)
    U=np.kron(np.kron(gate,S),np.eye(2))
    A=[np.kron(np.kron(np.eye(2),np.diag([1-m,m])),np.diag([1]+[0]*7)) for m in (0,1)]
    # Memory and reference are nontrivially entangled with the system.
    ar=np.zeros(8,complex);ar[0]=np.sqrt(.55);ar[5]=1j*np.sqrt(.45)
    beta=np.sqrt(np.array([.30,.20,.15,.12,.08,.06,.05,.04]))
    rho=product_ar_clock(density(ar),density(beta))
    return gate,S,U,A,ar,beta,rho,p,q


class FiberTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate,cls.S,cls.U,cls.A,cls.ar,cls.beta,cls.rho,cls.p,cls.q=setup()

    def test_model_and_complete_instrument(self):
        np.testing.assert_allclose(self.p,np.diag([1,0]),atol=1e-12)
        np.testing.assert_allclose(self.q,np.diag([0,1]),atol=1e-12)
        np.testing.assert_allclose(np.linalg.matrix_power(self.U,8),np.eye(64),atol=1e-12)
        f=sum((np.linalg.matrix_power(self.U,t).conj().T@np.kron(a,np.eye(2))@
               np.linalg.matrix_power(self.U,t) for a in self.A for t in range(8)))
        np.testing.assert_allclose(f,np.eye(64),atol=1e-12)

    def test_exact_full_fiber_identity_and_all_outcome_probabilities(self):
        # Two descriptions of the identical labeled joint branch, including R
        # and a reference, related by the fiber unitary U(t).
        psi=np.einsum('ix,r->irx',self.ar.reshape(4,2),self.beta).reshape(-1)
        prob=0.
        for m in (0,1):
            a=np.kron(self.A[m],np.eye(2))
            for t in range(8):
                u=np.linalg.matrix_power(self.U,t)
                anchored=u.conj().T@a@u@psi
                sliced=a@u@psi
                np.testing.assert_allclose(u@anchored,sliced,atol=2e-14)
                # A later projector is transformed along with the state.
                z=np.zeros(64,complex); z[0]=1
                obs=density(z)
                lhs=np.vdot(anchored,(u.conj().T@obs@u)@anchored).real
                rhs=np.vdot(sliced,obs@sliced).real
                self.assertAlmostEqual(lhs,rhs,places=13)
                prob+=np.vdot(anchored,anchored).real
        self.assertAlmostEqual(prob,1.,places=13)

    def test_product_preparation_recovers_smeared_reduced_instrument(self):
        oldrho=density(self.ar)
        summed=[np.zeros((8,8),complex) for _ in range(2)]
        expected=[np.zeros((8,8),complex) for _ in range(2)]
        uncorrected=[np.zeros((8,8),complex) for _ in range(2)]
        for m in (0,1):
            A=np.kron(self.A[m],np.eye(2))
            mem=np.kron(np.eye(2),np.diag([1-m,m]))
            mem_ref=np.kron(mem,np.eye(2))
            for t in range(8):
                U=np.linalg.matrix_power(self.U,t)
                K=U.conj().T@A@U
                branch=K@self.rho@K.conj().T
                uncorrected[m]+=ptr_clock(branch)
                summed[m]+=ptr_clock(U@branch@U.conj().T)
                v=np.kron(np.linalg.matrix_power(self.gate,t),np.eye(2))
                qt=abs((np.linalg.matrix_power(self.S,t)@self.beta)[0])**2
                expected[m]+=qt*mem_ref@v@oldrho@v.conj().T@mem_ref
            np.testing.assert_allclose(summed[m],expected[m],atol=1e-13)
        self.assertAlmostEqual(sum(np.trace(x).real for x in summed),1.,places=13)
        self.assertGreater(sum(distance(a,b) for a,b in zip(summed,uncorrected)),.1)

    def test_correlated_clock_does_not_factorize(self):
        # |P,mem0,R0,ref0> + |Q,mem0,R1,ref0>.
        psi=np.zeros((4,8,2),complex);psi[0,0,0]=1/np.sqrt(2);psi[2,1,0]=1/np.sqrt(2)
        rho=density(psi.reshape(-1));marginal=ptr_clock(rho)
        weights=[];conditional=[]
        for t in range(8):
            v=np.linalg.matrix_power(self.S,t)
            e=v.conj().T@np.diag([1]+[0]*7)@v
            c=np.kron(np.kron(np.eye(4),e),np.eye(2))
            a=ptr_clock(c@rho@c)
            weights.append(np.trace(a).real);conditional.append(a)
        np.testing.assert_allclose(sum(conditional),marginal,atol=1e-13)
        self.assertAlmostEqual(sum(weights),1.,places=13)
        t=int(np.argmax(weights))
        self.assertGreater(distance(conditional[t],weights[t]*marginal),.2)

    def test_dropping_orbit_record_loses_a_recoverable_coherence(self):
        # P, blank memory; coherently different signs between clock labels 0,2.
        vs=[]
        for sign in (1,-1):
            v=np.zeros((4,8,2),complex);v[0,0,0]=1/np.sqrt(2);v[0,2,0]=sign/np.sqrt(2)
            vs.append(v.reshape(-1))
        # Retain the outcome register and the coherent orbit-label dilation.
        full=[];reduced=[]
        for psi in vs:
            pieces=[]
            for m in (0,1):
                for t in range(8):
                    u=np.linalg.matrix_power(self.U,t);a=np.kron(self.A[m],np.eye(2))
                    pieces.append(u.conj().T@a@u@psi)
            full.append(np.concatenate(pieces))
            reduced.append([sum(density(x) for x in pieces[8*m:8*m+8]) for m in (0,1)])
        self.assertAlmostEqual(abs(np.vdot(full[0],full[1])),0.,places=13)
        # Even if m has been read (and its coherence lost), the retained t
        # environment distinguishes the signs with trace distance 1/sqrt(2).
        block_distance=sum(distance(density(full[0][64*8*m:64*8*(m+1)]),
                                    density(full[1][64*8*m:64*8*(m+1)])) for m in (0,1))
        self.assertAlmostEqual(block_distance,1/np.sqrt(2),places=13)
        for x,y in zip(*reduced):np.testing.assert_allclose(x,y,atol=1e-13)
        # Orthogonal full states versus identical reduced instrument output:
        # no deterministic (or universal probabilistic) map can infer the sign.


if __name__=='__main__':unittest.main()
