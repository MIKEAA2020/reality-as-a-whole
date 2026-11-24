"""Bound multiplicity bounds and full-state slice transport checks.

The analytic continuum claims are in ZERO_TWO_WINDOW_FULL_SLICE_CLOCK.md.
Finite matrices are illustrations and do not prove continuum estimates.
"""
import math
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model,states,probabilities
from verification.zero_two_window_continuum_slice_test import SY,P1,kernel

L0=math.sqrt(28/3)/math.pi
L5=math.sqrt(328/3)/math.pi
HS2_BOUND=(2*L5**2+(1.3*(L0+L5))**2)/4
C_BOUND=(14/3-71/60+185/756)/(2*math.pi)
M=(1.3+math.sqrt(1.3**2+1))/2
EDGE_MARGIN=2-2*C_BOUND*M


def channel_matrix(model,m1,m2,h=0):
    p,_,E,*_=model
    return (np.kron(np.eye(2),np.diag(p*p/6-2*h))
            -np.kron(SY,E[0])-1.3*np.kron(P1,m1*E[1]+m2*E[2]))


def constraint_kernel(p):
    n=len(p);Q=np.zeros((4,2*n),complex)
    Q[0,:n]=np.exp(-5j*p)
    Q[1,n:]=np.exp(-5j*p)
    Q[2,n:]=1
    Q[3,n:]=np.exp(5j*p)
    _,s,vh=np.linalg.svd(Q,full_matrices=True)
    rank=np.count_nonzero(s>1e-10)
    return vh[rank:].conj().T


def finite_slice_roundtrip(n=32,phi=100):
    """Sample every discrete mode, transport its amplitudes and z observables.

    This finite-grid example keeps all 4 memory-y channels and both h labels;
    it doesn't model continuum integration or certify the 13-slice theorem.
    """
    model=make_model(n);p,f,*_=model
    alphas=np.linspace(-.7,.7,13);betas=np.linspace(2,4,13)
    y={m:np.array([1,1j*m])/math.sqrt(2) for m in (-1,1)}
    pointer=np.array([1,1j])/math.sqrt(2)
    init=np.einsum('i,p->ip',pointer,f).reshape(-1)/2
    direct=[];rebuilt=[]
    for h in (0,1):
        full=np.zeros((2,2,2,n),complex);full_rebuilt=np.zeros_like(full)
        for m1 in (-1,1):
            for m2 in (-1,1):
                ev,U=np.linalg.eigh(channel_matrix(model,m1,m2,h))
                coeff=U.conj().T@(init*(1j if h else 1))
                omega=np.sqrt(ev)
                spatial=U.reshape(2,n,2*n)
                # Discrete counterpart of <a_alpha|eigenvector>/sqrt(2Ω).
                def samples(xs):
                    phase=np.exp(1j*np.outer(xs,p))/math.sqrt(n*2*math.pi)
                    return np.einsum('ap,ipk->aik',phase,spatial)/np.sqrt(2*omega)[None,None,:]
                A=samples(alphas);B=samples(betas)
                data=A*coeff[None,None,:]
                recovered=np.sum(A.conj()*data,axis=(0,1))/np.sum(abs(A)**2,axis=(0,1))
                beta_data=B*recovered[None,None,:]
                recovered_beta=np.sum(B.conj()*beta_data,axis=(0,1))/np.sum(abs(B)**2,axis=(0,1))
                direct_v=(U@(coeff*np.exp(1j*phi*omega))).reshape(2,n)
                rebuilt_v=(U@(recovered_beta*np.exp(1j*phi*omega))).reshape(2,n)
                full+=np.einsum('ip,j,k->ijkp',direct_v,y[m1],y[m2])
                full_rebuilt+=np.einsum('ip,j,k->ijkp',rebuilt_v,y[m1],y[m2])
        direct.append(full);rebuilt.append(full_rebuilt)
    return model,direct,rebuilt


class FullSliceTests(unittest.TestCase):
    def test_analytic_bound_constants(self):
        self.assertAlmostEqual(C_BOUND,.5933363645637538,places=12)
        self.assertGreater(EDGE_MARGIN,.25)
        self.assertLess(HS2_BOUND,14)
        self.assertGreater(HS2_BOUND,13)

    def test_edge_controls_on_discrete_constraint_subspace(self):
        model=make_model(48);p=model[0];Q=constraint_kernel(p)
        self.assertEqual(Q.shape[1],2*len(p)-4)
        for m1 in (-1,1):
            for m2 in (-1,1):
                H=channel_matrix(model,m1,m2)
                levels=np.linalg.eigvalsh(H)
                self.assertLessEqual(np.count_nonzero(levels<6),4)
                self.assertLessEqual(np.count_nonzero(levels>49/6),4)
                for edge,sign in ((-6,1),(-7,-1)):
                    dist=np.tile(abs(p-edge),2)
                    shifted=sign*(H-(edge**2/6)*np.eye(2*len(p)))-EDGE_MARGIN*np.diag(dist)
                    eig=np.linalg.eigvalsh(Q.conj().T@shifted@Q)
                    self.assertGreater(eig[0],-1e-10)

    def test_divided_difference_hs_bound(self):
        n=80;p,_,_,*_=make_model(n);dp=1/n
        for k in (-7,-6.79,-6.503,-6.21,-6):
            for m1 in (-1,1):
                for m2 in (-1,1):
                    d=(kernel(p,p,m1,m2)-kernel(np.array([k]),p,m1,m2))/((p*p-k*k)/6)[:,None,None,None]
                    hs2=dp*dp*np.sum(abs(d)**2)
                    self.assertLess(hs2,HS2_BOUND)

    def test_transport_full_grid_state_and_memory_statistics(self):
        model,direct,rebuilt=finite_slice_roundtrip()
        reference=states(model,100)
        reference[1]*=1j  # logical (|0>+i|1>)/sqrt(2), weights handled below
        for actual,r,expected in zip(direct,rebuilt,reference):
            self.assertLess(np.linalg.norm(actual-r),2e-13)
            self.assertLess(np.linalg.norm(actual-expected),5e-12)
        self.assertLess(np.max(abs(probabilities(direct)-probabilities(rebuilt))),1e-13)
        self.assertAlmostEqual(probabilities(rebuilt).sum(),1,places=11)

    def test_degenerate_spinor_example_needs_multiple_slices(self):
        # f1=(1,0), f2=(p,0), f3=(0,1) are independent band states.
        # At one slice both f1,f2 have the same spin direction; each slice
        # outputs only two components, but two distinct values resolve all 3.
        x,w=np.polynomial.legendre.leggauss(100);p=-6.5+x/2;w=w/2
        def F(alpha):
            z=w*np.exp(1j*p*alpha)
            return np.array([[sum(z),sum(z*p),0],[0,0,sum(z)]])
        A=F(0);B=np.vstack((A,F(1)))
        self.assertEqual(np.linalg.matrix_rank(A),2)
        self.assertEqual(np.linalg.matrix_rank(B),3)

if __name__=='__main__':unittest.main()
