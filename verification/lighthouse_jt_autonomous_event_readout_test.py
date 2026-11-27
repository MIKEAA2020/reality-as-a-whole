#!/usr/bin/env python3
"""Finite controls for the JT-inspired eight-outcome autonomous event probe.

The accompanying note derives the continuum Duhamel bound.  This uses a
compressed finite cyclic clock, not the continuum scalar-clock effects.
"""
import math
import unittest

import numpy as np
from scipy.linalg import expm


def root(a):
    a=(a+a.conj().T)/2
    v,u=np.linalg.eigh(a)
    if v.min() < -1e-11:
        raise ValueError('not positive')
    return (u*np.sqrt(np.maximum(v,0)))@u.conj().T


def make_effects():
    full, d=8,5
    # First five energy modes of a finite cyclic clock, with four time bins.
    U=np.exp(-2j*np.pi*np.outer(np.arange(full),np.arange(full))/full)/np.sqrt(full)
    U=U[:,:d]
    groups=[[5,6,7],[0,1],[2,3],[4]]  # outcome 0 is outside
    return [U[g,:].conj().T@U[g,:] for g in groups]


def clock_gate(effects):
    d=len(effects[0]); I=np.eye(d)
    roots=[root(f) for f in effects]
    basis=np.eye(4,dtype=complex)
    J=np.kron(I,basis[:,0:1])
    Wperp=sum(np.kron(roots[i],basis[:,i:i+1]) for i in range(1,4))
    hit=sum(effects[1:]); vals,vec=np.linalg.eigh((hit+hit.conj().T)/2)
    vals=np.clip(vals,0,1)
    inv=np.zeros_like(vals); mask=vals>1e-12; inv[mask]=1/np.sqrt(vals[mask])
    V=Wperp@(vec*inv)@vec.conj().T
    theta=(vec*np.arcsin(np.sqrt(vals)))@vec.conj().T
    K=1j*(V@theta@J.conj().T-J@theta@V.conj().T)
    return K,J,V,theta,roots


def budget(a=.3,b=.3,T=1.7,M=1e6,v=1.):
    A1=math.pi*15/(8*b)
    A2=math.pi*10/(math.sqrt(3)*b*b)+A1*A1
    k2=math.sqrt(63/2)/a**2+2*math.sqrt(3)/a*A1+A2
    return k2,T*k2/(2*M),1+math.pi*v*15/(16*b),M*v*v/2+3/(2*M*a*a)


class JTAutonomousEventReadoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.effects=make_effects()
        cls.d=len(cls.effects[0])
        cls.Kc,cls.Jc,cls.V,cls.theta,cls.roots=clock_gate(cls.effects)
        X=np.array([[0,1],[1,0]],complex)
        Y=np.array([[0,-1j],[1j,0]],complex)
        cls.pm=[(np.eye(2)+X)/2,(np.eye(2)-X)/2]
        cls.Ks=np.kron((math.pi/2)*cls.pm[1],Y)
        cls.Js=np.kron(np.eye(2),np.array([[1.],[0.]]))
        cls.G=np.kron(cls.Kc,np.eye(4))+np.kron(np.eye(4*cls.d),cls.Ks)
        cls.J=np.kron(cls.Jc,cls.Js)

    def test_four_effects_are_noncommuting_and_complete(self):
        np.testing.assert_allclose(sum(self.effects),np.eye(self.d),atol=2e-14)
        for f in self.effects:
            self.assertGreater(np.linalg.eigvalsh(f).min(),-1e-12)
            self.assertLess(np.linalg.eigvalsh(f).max(),1+1e-12)
        self.assertGreater(np.linalg.norm(self.effects[1]@self.effects[2]-
                                          self.effects[2]@self.effects[1]),.05)

    def test_polar_isometry_and_exact_four_bin_luders_gate(self):
        vals,vec=np.linalg.eigh(sum(self.effects[1:])); P=(vec*(vals>1e-12))@vec.conj().T
        np.testing.assert_allclose(self.V.conj().T@self.V,P,atol=1e-12)
        np.testing.assert_allclose(self.Jc.conj().T@self.V,0,atol=1e-14)
        np.testing.assert_allclose(self.Kc,self.Kc.conj().T,atol=1e-14)
        self.assertLessEqual(np.linalg.norm(self.Kc,2),math.pi/2+1e-12)
        expected=sum(np.kron(self.roots[i],np.eye(4)[:,i:i+1]) for i in range(4))
        np.testing.assert_allclose(expm(-1j*self.Kc)@self.Jc,expected,atol=1e-12)

    def test_zero_hit_support_has_no_inverse_failure(self):
        d=3
        # A zero eigenvalue is explicitly present in F_hit.
        hit=np.diag([0.,.3,.8]); parts=[(np.eye(d)-hit),hit*.2,hit*.3,hit*.5]
        K,J,V,theta,roots=clock_gate(parts)
        expected=sum(np.kron(roots[i],np.eye(4)[:,i:i+1]) for i in range(4))
        np.testing.assert_allclose(expm(-1j*K)@J,expected,atol=1e-12)
        self.assertAlmostEqual(np.linalg.norm(K@J[:,0]),0.,places=13)

    def test_eight_luders_kraus_operators(self):
        W=(expm(-1j*self.G)@self.J).reshape(self.d,4,2,2,self.d,2)
        for b in range(4):
            for m in range(2):
                actual=W[:,b,:,m,:,:].reshape(2*self.d,2*self.d)
                expected=np.kron(self.roots[b],self.pm[m])
                np.testing.assert_allclose(actual,expected,atol=1e-12)
        self.assertLessEqual(np.linalg.norm(self.G,2),math.pi+1e-12)

    def test_same_branch_poststates_with_reference(self):
        W=(expm(-1j*self.G)@self.J).reshape(self.d,4,2,2,self.d,2)
        rng=np.random.default_rng(147)
        n=4*self.d; x=rng.normal(size=n)+1j*rng.normal(size=n);x/=np.linalg.norm(x)
        rho=np.outer(x,x.conj());total=0.
        for b in range(4):
            for m in range(2):
                actual=np.kron(W[:,b,:,m,:,:].reshape(2*self.d,2*self.d),np.eye(2))
                target=np.kron(np.kron(self.roots[b],self.pm[m]),np.eye(2))
                out=actual@rho@actual.conj().T
                np.testing.assert_allclose(out,target@rho@target.conj().T,atol=1e-12)
                total+=np.trace(out).real
        self.assertAlmostEqual(total,1.,places=12)

    def test_dressing_is_essential_when_hamiltonian_does_not_commute(self):
        H=np.kron(np.diag(np.arange(self.d)),np.eye(4*4))
        H+=np.kron(np.eye(4*self.d),np.kron(np.diag([0.,2.]),np.eye(2)))
        comm=H@self.G-self.G@H
        self.assertGreater(np.linalg.norm(comm),1.)
        S=.37; U=expm(-1j*H*S)
        dressed=U@self.G@U.conj().T
        np.testing.assert_allclose(U.conj().T@dressed@U,self.G,atol=1e-12)
        derivative=-1j*(H@dressed-dressed@H)
        np.testing.assert_allclose(-1j*derivative+H@dressed-dressed@H,0,atol=1e-12)
        self.assertGreater(np.linalg.norm(dressed-self.G),.1)

    def test_selected_massive_cursor_fourier_control(self):
        # Positive carrier and exp(-i H S) move the packet right.
        N,L,a,b,T,M,steps=2048,8.,.3,.3,1.7,1e6,1700
        dx=L/N; x=np.arange(N)*dx-L/2
        k=2*np.pi*np.fft.fftfreq(N,d=dx);dt=T/steps
        def packet(z):
            return np.sqrt(315/(256*a))*np.where(abs(z/a)<=1,(1-(z/a)**2)**2,0.)
        profile=15/(16*b)*np.where(abs(x/b)<=1,(1-(x/b)**2)**2,0.)
        kinetic=np.exp(-1j*(k+k*k/(2*M))*dt/2)
        for strength in (0.,.7,math.pi):
            psi=packet(x+1).astype(complex)
            kick=np.exp(-1j*strength*profile*dt)
            for _ in range(steps):
                psi=np.fft.ifft(np.fft.fft(psi)*kinetic)
                psi*=kick
                psi=np.fft.ifft(np.fft.fft(psi)*kinetic)
            target=np.exp(-1j*strength)*packet(x+1-T)
            err=np.sqrt(dx*np.sum(abs(psi-target)**2))
            self.assertLess(err,budget()[1]+3e-5)
            self.assertAlmostEqual(dx*np.sum(abs(psi)**2),1.,places=7)

    def test_resource_bound_and_no_reading_probability(self):
        K2,epsilon,shift,energy=budget()
        self.assertLess(K2,876.151)
        self.assertLess(epsilon,.000745)
        self.assertAlmostEqual(shift,10.817477042468104)
        self.assertAlmostEqual(energy,500000.00001666666)
        # Original continuum packet's analytically bounded success probability.
        self.assertLess(2*epsilon/.135, .0111)
        self.assertGreater(.79572221-epsilon,.794)


if __name__=='__main__':unittest.main()
