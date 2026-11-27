"""Finite autonomous readout window on the existing support detector.

The continuum certificate is a derived bound on a deliberately changed
constraint and a supplied global Q coupling, not a local apparatus, perfect
latch, or a proof of a clock-switch theorem. Finite-grid evolution is a control.
"""
from fractions import Fraction as F
import math
import unittest
import numpy as np

from verification.zero_two_window_autonomous_support_dynamics_test import system
from verification.zero_two_window_commutator_certificate import verify

N=8
G=100.
SHIFT=N*G


def collective_y(n):
    """Sum of n Pauli-Y operators on the permutation-symmetric spin subspace.

    Basis state k is the normalized symmetric state with k spins up/flagged.
    A^dagger|k> = sqrt((k+1)(n-k)) |k+1>.
    """
    s=np.zeros((n+1,n+1),complex)
    for k in range(n):
        v=math.sqrt((k+1)*(n-k))
        s[k+1,k]=1j*v
        s[k,k+1]=-1j*v
    return s


def d_bound(n=N,g=G,multiplier=3):
    # t=multiplier*pi/(4g); c<0.419/(2*1.3), pi<22/7.
    c=F(419,1000)/(2*F(13,10))
    return F(n)*multiplier**2*F(22,7)**2*c/(32*F(g))


def physical_matrices(grid,h,n=N,g=G):
    # Reuse the original two-window regulated root and packet projection.
    _,B,P,Q,O,_=system(grid,h)
    S=collective_y(n)
    # Identity shift is omitted numerically (only a common phase); it is
    # included when specifying the positive root in the accompanying report.
    H=np.kron(O,np.eye(n+1))+g*np.kron(Q,S)
    vals,V=np.linalg.eigh(H)
    return B,P,Q,O,vals,V


def flag_probability(data,psi,t,n=N):
    vals,V=data[-2:]
    init=np.kron(psi,np.eye(n+1)[:,0])
    out=V@(np.exp(1j*vals*t)*(V.conj().T@init))
    blocks=out.reshape(-1,n+1)
    return float(np.sum(np.abs(blocks[:,1:])**2))


class RedundantFlagHoldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=[physical_matrices(8,h) for h in (0,1)]

    def test_certificate_constants_and_positivity(self):
        cert=verify()
        self.assertLess(cert['commutator_squared_upper'],F(419,1000)**2)
        D=d_bound()
        self.assertLess(D,F(36,1000))
        self.assertLess((F(1,16)+D)**2,F(97,10000))
        self.assertLess(D**2,F(13,10000))
        self.assertLess(d_bound(multiplier=4)**2,F(41,10000))
        self.assertEqual(SHIFT,N*G)
        # Ω≥1.3, H=Ω+SHIFT+gQ sum Y ≥1.3.
        self.assertGreater(F(13,10)+F(SHIFT)-F(N)*F(G),0)

    def test_collective_operator_has_correct_spectrum(self):
        S=collective_y(N)
        np.testing.assert_allclose(S,S.conj().T,atol=1e-14)
        np.testing.assert_allclose(np.linalg.eigvalsh(S),np.arange(-N,N+1,2),atol=1e-12)
        vals,V=np.linalg.eigh(S);ready=np.eye(N+1)[:,0]
        for theta in (0.,math.pi/4,math.pi/2,3*math.pi/4,math.pi):
            state=V@(np.exp(1j*theta*vals)*(V.conj().T@ready))
            self.assertAlmostEqual(abs(state[0])**2,math.cos(theta)**(2*N),places=12)

    def test_grid_internal_dynamics_against_continuum_bound(self):
        D=float(d_bound());c=float(F(419,1000)/(2*F(13,10)))
        for B,P,Q,O,vals,V in self.data:
            self.assertLess(np.linalg.norm(Q@O@B,2),c)
            rng=np.random.default_rng(476)
            raw=rng.normal(size=len(Q))+1j*rng.normal(size=len(Q))
            outside=Q@raw; outside/=np.linalg.norm(outside)
            inside=B[:,0]
            for theta in np.linspace(math.pi/4,3*math.pi/4,13):
                t=theta/G
                pin=flag_probability((B,P,Q,O,vals,V),inside,t)
                pout=flag_probability((B,P,Q,O,vals,V),outside,t)
                self.assertLessEqual(pin,D**2+1e-11)
                self.assertLessEqual(1-pout,(1/16+D)**2+1e-11)
            for psi in (inside,outside,(inside+outside)/math.sqrt(2)):
                p=flag_probability((B,P,Q,O,vals,V),psi,math.pi/G)
                self.assertLessEqual(p,float(d_bound(multiplier=4))**2+1e-11)

    def test_coherent_leakage_inference_at_sampled_times(self):
        D=float(d_bound()); smin=math.sqrt(255/256)
        for B,P,Q,O,vals,V in self.data:
            raw=np.arange(1,len(Q)+1,dtype=float)+1j*np.arange(len(Q),0,-1)
            x=Q@raw;x/=np.linalg.norm(x)
            psi=math.sqrt(.9)*B[:,0]+1j*math.sqrt(.1)*x
            lam=np.linalg.norm(Q@psi)**2
            for theta in (math.pi/4,math.pi/2,3*math.pi/4):
                p=flag_probability((B,P,Q,O,vals,V),psi,theta/G)
                self.assertLessEqual(math.sqrt(lam),(math.sqrt(p)+D)/smin+1e-10)
                self.assertGreaterEqual(lam,0.)
                self.assertAlmostEqual(lam,.1,places=11)


if __name__=='__main__': unittest.main()
