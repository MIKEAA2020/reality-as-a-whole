"""Check a factorwise-probe versus old-instrument poststate obstruction.

Continuum bound and assumptions are in ZERO_CLOCK_PROBE_POSTSTATE_OBSTRUCTION.md.
Finite periodic-clock controls do not simulate the original massive cursors.
"""
import math
import unittest
import numpy as np
from scipy.linalg import expm


def positive_root(E):
    vals,V=np.linalg.eigh(E)
    if vals.min()<-2e-12 or vals.max()>1+2e-12:raise ValueError('effect out of range')
    return (V*np.sqrt(np.clip(vals,0,1)))@V.conj().T


def continuum_lower():
    # Certified by the rectangle and edge estimates detailed in the report.
    ell=1e-4;b=5000.;d=3.5;L=1000.
    cross=L*ell/(2*math.pi)*math.sin(.15)/.15
    edge=math.sqrt(ell*d/math.pi)
    beta_min_sq=math.sin(math.pi*d/(2*b))**2/b
    lower=2*math.pi/ell*beta_min_sq*((cross-edge)/2)**2
    return cross,edge,beta_min_sq,lower


def cyclic_clock(n=33,steps=200):
    # Periodic clock with levels 0..n-1, bin [-ell/2,ell/2],
    # and band of seven modes. ell*half-bandwidth=1/2.
    ell=1/7;k=np.arange(n);diff=k[:,None]-k[None,:]
    E=ell/(2*np.pi)*np.sinc(diff*ell/(2*np.pi))
    A=positive_root(E)
    idx=np.arange(n//2-3,n//2+4)
    P=np.zeros((n,n));P[idx,idx]=1
    beta=np.zeros(n);beta[idx]=np.cos(np.pi*(np.arange(7)-3)/7)
    beta/=np.linalg.norm(beta)
    A_band=positive_root(P@E@P)
    hit=A_band@beta;hitprob=np.vdot(hit,hit).real
    state_hit=np.outer(hit,hit.conj())/hitprob
    twirled=np.zeros((n,n),complex)
    for t in 2*np.pi*np.arange(steps)/steps:
        z=np.exp(-1j*k*t)*(A@(np.exp(1j*k*t)*beta))
        twirled+=(2*np.pi/(ell*steps))*np.outer(z,z.conj())
    return k,E,A,P,beta,twirled,state_hit,hitprob


def distance(a,b):
    d=a-b;d=(d+d.conj().T)/2
    return np.abs(np.linalg.eigvalsh(d)).sum()/2


class ClockPoststateObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.k,cls.E,cls.A,cls.P,cls.beta,cls.old,cls.new,cls.hit=cyclic_clock()

    def test_explicit_continuum_bound_constants(self):
        cross,edge,beta_sq,lower=continuum_lower()
        self.assertGreater(cross,.01585)
        self.assertLess(edge,.01056)
        self.assertGreater(beta_sq,2.41e-10)
        self.assertGreater(lower,1.06e-10)
        # The restricted rectangle lies inside the central band on one side
        # and outside on the other, with |(k-k')ell/2| <= .15.
        self.assertLess(3.5,1000.)
        self.assertAlmostEqual(3000*1e-4/2,.15)

    def test_complete_orbit_average_and_clock_band_leakage(self):
        Q=np.eye(len(self.k))-self.P
        self.assertAlmostEqual(np.trace(self.old).real,1.,places=12)
        self.assertGreaterEqual(np.linalg.eigvalsh((self.old+self.old.conj().T)/2).min(),-1e-12)
        leak=np.trace(Q@self.old).real
        self.assertAlmostEqual(leak,.72811616,places=6)
        self.assertAlmostEqual(np.trace(Q@self.new).real,0.,places=13)
        self.assertGreaterEqual(distance(self.old,self.new)+1e-12,leak)
        self.assertAlmostEqual(distance(self.old,self.new),.83518897,places=6)

    def test_equal_memory_statistics_do_not_fix_clock_poststate(self):
        # Take a memory with zero Hamiltonian and input sqrt(.3)|0> +
        # sqrt(.7)|1>. Both procedures record its same m, while their clock
        # poststates above differ. The hit is explicitly conditioned only in
        # the probe description; the distinct interventions are not confused.
        probs=np.array([.3,.7])
        old=[p*self.old for p in probs];new=[p*self.new for p in probs]
        np.testing.assert_allclose([np.trace(x).real for x in old],probs,atol=1e-12)
        np.testing.assert_allclose([np.trace(x).real for x in new],probs,atol=1e-12)
        self.assertGreater(sum(distance(x,y) for x,y in zip(old,new)),.83)
        self.assertAlmostEqual(self.hit,.13065924,places=7)

    def test_band_projector_commutes_with_factorwise_clock_gate(self):
        # Exact conservation under the finite analogue of K_R+f(x)Θ_R σ_y.
        E=self.P@self.E@self.P;vals,V=np.linalg.eigh(E)
        theta=(V*np.arcsin(np.sqrt(np.clip(vals,0,1))))@V.conj().T
        y=np.array([[0.,-1j],[1j,0.]])
        H=np.kron(np.diag(self.k),np.eye(2))+.8*np.kron(theta,y)
        P=np.kron(self.P,np.eye(2))
        np.testing.assert_allclose(H@P,P@H,atol=1e-13)
        U=expm(1j*H*.4)
        np.testing.assert_allclose(U@P,P@U,atol=2e-12)
        np.testing.assert_allclose((np.eye(len(P))-P)@U@P,0,atol=2e-12)

    def test_without_compression_both_instruments_are_not_identical(self):
        # Compression is a real change in the instrument's clock effect on
        # arbitrary states, even though it preserves the bin probability for β.
        Eband=self.P@self.E@self.P
        self.assertAlmostEqual(np.vdot(self.beta,Eband@self.beta).real,
                               np.vdot(self.beta,self.E@self.beta).real,places=13)
        outside=np.zeros(len(self.k));outside[0]=1
        self.assertGreater(np.vdot(outside,self.E@outside).real,0.)
        self.assertAlmostEqual(np.vdot(outside,Eband@outside).real,0.,places=14)


if __name__=='__main__':unittest.main()
