#!/usr/bin/env python3
"""Finite control for the same York/scalar event instrument.

The continuum construction and all scope limits appear in the accompanying
note. This discrete periodic model tests the shift and instrument bookkeeping;
it is not a convergence proof or an autonomous apparatus.
"""
import unittest

import numpy as np


def setup_model():
    n, gap = 5, 2
    lam_size = n+gap
    # York reduced coordinates (E,j) -> scalar reduced (lambda=E+h_j,j).
    V = np.zeros((2*lam_size, 2*n), dtype=complex)
    for e in range(n):
        for j in range(2):
            V[2*(e+gap*j)+j, 2*e+j] = 1
    projector = V@V.conj().T
    clock_state = np.ones(n,dtype=complex)/np.sqrt(n)
    click = np.outer(clock_state,clock_state.conj())
    effects = [click, np.eye(n)-click]
    X = np.array([[0,1],[1,0]],dtype=complex)
    outcomes = [(np.eye(2)+X)/2,(np.eye(2)-X)/2]
    Ks = [np.kron(e,p) for e in effects for p in outcomes]
    # t is a scalar clock conditioning parameter. R acts only on the support.
    t=.73
    phase = np.zeros(2*lam_size,dtype=complex)
    for l in range(lam_size):
        for j in range(2):
            e=l-gap*j
            if 0<=e<n:
                phase[2*l+j]=np.exp(1j*e*t)
    R=np.diag(phase)
    D=R@V
    return n,gap,lam_size,V,projector,R,D,effects,outcomes,Ks


def random_density(n,seed):
    rng=np.random.default_rng(seed)
    psi=rng.normal(size=n)+1j*rng.normal(size=n)
    psi/=np.linalg.norm(psi)
    return np.outer(psi,psi.conj())


class JTCommonEventFrameSwitchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (cls.n,cls.gap,cls.lam_size,cls.V,cls.P,cls.R,cls.D,
         cls.effects,cls.outcomes,cls.Ks)=setup_model()

    def test_shift_map_and_correct_support(self):
        np.testing.assert_allclose(self.V.conj().T@self.V,np.eye(2*self.n),atol=1e-14)
        np.testing.assert_allclose(self.V@self.V.conj().T,self.P,atol=1e-14)
        np.testing.assert_allclose(self.P@self.P,self.P,atol=1e-14)
        # High-energy spin state has no valid lambda below its energy gap.
        self.assertEqual(self.P[1,1],0)
        self.assertEqual(self.P[2*self.gap+1,2*self.gap+1],1)
        self.assertEqual(self.P[2*(self.lam_size-1),2*(self.lam_size-1)],0)
        np.testing.assert_allclose(self.D.conj().T@self.D,np.eye(2*self.n),atol=1e-14)
        np.testing.assert_allclose(self.D@self.D.conj().T,self.P,atol=1e-14)

    def test_complete_instrument_and_constraint_sector(self):
        np.testing.assert_allclose(sum(k.conj().T@k for k in self.Ks),np.eye(2*self.n),atol=1e-14)
        Knew=[self.D@k@self.D.conj().T for k in self.Ks]
        np.testing.assert_allclose(sum(k.conj().T@k for k in Knew),self.P,atol=2e-14)
        for k in Knew:
            np.testing.assert_allclose(self.P@k@self.P,k,atol=1e-14)

    def test_constraint_commuting_finite_kinematic_dilation(self):
        # York energy lambda, scalar energy e, and qubit energy j*gap.
        dimension=self.lam_size*self.n*2
        J=np.zeros((dimension,2*self.n),complex)
        diag=np.zeros(dimension)
        for l in range(self.lam_size):
            for e in range(self.n):
                for j in range(2):
                    row=(l*self.n+e)*2+j
                    diag[row]=-l+e+self.gap*j
                    if l==e+self.gap*j:
                        J[row,2*e+j]=1
        C=np.diag(diag)
        np.testing.assert_allclose(C@J,0,atol=1e-14)
        np.testing.assert_allclose(J.conj().T@J,np.eye(2*self.n),atol=1e-14)
        Jp=J@J.conj().T
        transformed=[J@k@J.conj().T for k in self.Ks]
        for k in transformed:
            np.testing.assert_allclose(C@k-k@C,0,atol=1e-14)
        # A ninth outcome only completes the artificial off-constraint sector.
        off=np.eye(dimension)-Jp
        np.testing.assert_allclose(sum(k.conj().T@k for k in transformed)+off,
                                   np.eye(dimension),atol=1e-14)

    def test_same_poststates_with_entangled_reference(self):
        # Arbitrary preparation entangled with a two-level reference.
        rho=random_density(2*self.n*2,706)
        Dr=np.kron(self.D,np.eye(2)); transformed=Dr@rho@Dr.conj().T
        for k in self.Ks:
            kr=np.kron(k,np.eye(2))
            kp=self.D@k@self.D.conj().T
            kpr=np.kron(kp,np.eye(2))
            actual=kpr@transformed@kpr.conj().T
            expected=Dr@kr@rho@kr.conj().T@Dr.conj().T
            np.testing.assert_allclose(actual,expected,atol=2e-14)
            self.assertAlmostEqual(np.trace(actual).real,np.trace(kr@rho@kr.conj().T).real,places=13)

    def test_full_joint_later_record_equality(self):
        rho=random_density(2*self.n*2,221)
        Dr=np.kron(self.D,np.eye(2)); transformed=Dr@rho@Dr.conj().T
        # A later outcome on system+reference is transported, not guessed.
        g=random_density(2*self.n*2,45)
        gr=Dr@g@Dr.conj().T
        all_p=0
        for k in self.Ks:
            kr=np.kron(k,np.eye(2)); kp=Dr@kr@Dr.conj().T
            old=kr@rho@kr.conj().T; new=kp@transformed@kp.conj().T
            p_old=np.trace(g@old).real; p_new=np.trace(gr@new).real
            self.assertAlmostEqual(p_old,p_new,places=13)
            all_p+=np.trace(old).real
        self.assertAlmostEqual(all_p,1.,places=13)

    def test_system_flip_shifts_york_energy(self):
        # X transforms (lambda,j) -> (lambda +/- gap, 1-j).
        X=np.array([[0,1],[1,0]],complex)
        converted=self.V@np.kron(np.eye(self.n),X)@self.V.conj().T
        for e in range(self.n):
            src=np.zeros(2*self.lam_size);src[2*e]=1
            dst=np.zeros(2*self.lam_size);dst[2*(e+self.gap)+1]=1
            np.testing.assert_allclose(converted@src,dst,atol=1e-14)
        # An unsupported naive same-lambda flip fails even to preserve sector.
        naive=np.kron(np.eye(self.lam_size),X)
        self.assertGreater(np.linalg.norm((np.eye(len(self.P))-self.P)@naive@self.P),.5)

    def test_event_energy_backreaction_without_clock_reading(self):
        phi=np.array([1,2,3,2,1],dtype=complex);phi/=np.linalg.norm(phi)
        psi=np.kron(phi,np.array([1.,0.]))
        rho=np.outer(psi,psi.conj())
        nr=sum(np.kron(np.eye(self.n),p)@rho@np.kron(np.eye(self.n),p)
               for p in self.outcomes)
        clockE=np.kron(np.diag(np.arange(self.n)),np.eye(2))
        Hsys=np.kron(np.eye(self.n),np.diag([0.,float(self.gap)]))
        oldE=np.trace(clockE@rho).real;newE=np.trace(clockE@nr).real
        oldH=np.trace(Hsys@rho).real;newH=np.trace(Hsys@nr).real
        self.assertAlmostEqual(newE,oldE,places=13)
        self.assertAlmostEqual(newH-oldH,self.gap/2,places=13)
        lam=np.kron(np.diag(np.arange(self.lam_size)),np.eye(2))
        old_lam=np.trace(lam@self.V@rho@self.V.conj().T).real
        new_lam=np.trace(lam@self.V@nr@self.V.conj().T).real
        self.assertAlmostEqual(new_lam-old_lam,self.gap/2,places=13)

    def test_later_york_reading_and_spin_interference(self):
        # On the scalar frame, compress a periodic York-time/spin POVM to P.
        L=self.lam_size
        phi=np.array([1.,2.,3.,2.,1.],complex);phi/=np.linalg.norm(phi)
        psi=np.kron(phi,np.array([1.,0.],complex))
        t=.73
        total=0.
        for b,F in enumerate(self.effects):
            fb=F@phi
            for m,pm in ((1,self.outcomes[0]),(-1,self.outcomes[1])):
                physical=np.kron(F,pm)@psi
                branch=self.D@physical
                branch_weight=np.vdot(branch,branch).real
                self.assertAlmostEqual(branch_weight,np.vdot(fb,fb).real/2,places=13)
                for l in range(L):
                    s=2*np.pi*l/L
                    york=np.exp(1j*np.arange(L)*s)/np.sqrt(L)
                    york_effect=np.outer(york,york.conj())
                    amp=np.sum(fb*np.exp(-1j*np.arange(self.n)*(s-t)))/np.sqrt(L)
                    for mp,Pm in ((1,self.outcomes[0]),(-1,self.outcomes[1])):
                        Q=self.P@np.kron(york_effect,Pm)@self.P
                        measured=np.vdot(branch,Q@branch).real
                        expected=abs(amp)**2*(1+m*mp*np.cos(self.gap*s))/4
                        self.assertAlmostEqual(measured,expected,places=13)
                        total+=measured
        self.assertAlmostEqual(total,1.,places=13)

    def test_effects_do_not_determine_the_instrument(self):
        # Unitarly feed back one qubit outcome without changing its effect.
        X=np.array([[0,1],[1,0]],complex)
        Z=np.diag([1.,-1.])
        original=self.Ks[0]
        altered=np.kron(np.eye(self.n),Z)@original
        np.testing.assert_allclose(altered.conj().T@altered,original.conj().T@original,atol=1e-14)
        phi=np.ones(self.n)/np.sqrt(self.n)
        psi=np.kron(phi,np.array([1.,0.]))
        self.assertGreater(np.linalg.norm(np.outer(original@psi,(original@psi).conj())-
                                          np.outer(altered@psi,(altered@psi).conj())),.5)


if __name__=='__main__':
    unittest.main()
