"""Finite controls for the SAME probe in scalar and R-time representations.

The continuum construction and scope are in
ZERO_SAME_PROBE_CLOCK_REPRESENTATION.md. The finite periodic clock is not the
old massive cursor or the semibounded continuum model.
"""
import unittest
import numpy as np
from scipy.linalg import expm
from verification.zero_factorized_clock_probe_test import budgets


def trace_dist(a,b):
    d=a-b;return np.abs(np.linalg.eigvalsh((d+d.conj().T)/2)).sum()/2


def root(a):
    vals,V=np.linalg.eigh((a+a.conj().T)/2)
    return (V*np.sqrt(np.clip(vals,0,None)))@V.conj().T


def make():
    n=8; u=2*np.pi*np.arange(n)/n;k=np.arange(n)
    F=np.exp(-1j*np.outer(u,k))/np.sqrt(n)
    # Restrict clock operation to an energy band and use two clock outcomes.
    P=np.diag([0,1,1,1,1,1,1,0]);time_bin=np.diag([1,1,0,0,0,0,0,0])
    E=P@F.conj().T@time_bin@F@P
    Hx=np.diag([0.,1.]);sigma_x=np.array([[0,1],[1,0]],complex)
    W=np.zeros((2*n,2*n),complex)
    for j,t in enumerate(u):W[2*j:2*j+2,2*j:2*j+2]=expm(-1j*Hx*t)
    D=W@np.kron(F,np.eye(2))
    Ks=[]
    for c in (0,1):
        ec=E if c else np.eye(n)-E
        for m in (0,1):
            pm=np.diag([1-m,m]);Ks.append(np.kron(root(ec),pm))
    return n,u,k,F,P,E,Hx,sigma_x,W,D,Ks


class SameProbeClockRepresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (cls.n,cls.u,cls.k,cls.F,cls.P,cls.E,cls.Hx,cls.X,
         cls.W,cls.D,cls.Ks)=make()

    def test_unitary_encoded_switch_and_common_preparation(self):
        D=self.D
        np.testing.assert_allclose(D.conj().T@D,np.eye(len(D)),atol=2e-14)
        rng=np.random.default_rng(89)
        # Clock and X are correlated; the identity makes no product assumption.
        psi=rng.normal(size=16)+1j*rng.normal(size=16);psi/=np.linalg.norm(psi)
        rho=np.outer(psi,psi.conj());rel=D@rho@D.conj().T
        np.testing.assert_allclose(D.conj().T@rel@D,rho,atol=2e-14)
        np.testing.assert_allclose(sum(K.conj().T@K for K in self.Ks),np.eye(16),atol=1e-13)
        self.assertAlmostEqual(sum(np.trace(K@rho@K.conj().T).real for K in self.Ks),1.,places=12)
        for K in self.Ks:
            Kr=D@K@D.conj().T
            np.testing.assert_allclose(Kr@rel@Kr.conj().T,D@K@rho@K.conj().T@D.conj().T,atol=2e-14)

    def test_same_four_outcomes_and_later_conditional_observables(self):
        rng=np.random.default_rng(2026)
        psi=rng.normal(size=16)+1j*rng.normal(size=16);psi/=np.linalg.norm(psi)
        rho=np.outer(psi,psi.conj());rel=self.D@rho@self.D.conj().T
        # A later time-bin, followed by a time-dependent X measurement.
        times=(1,2,5);obs=(np.eye(2)+self.X)/2
        old=[];new=[]
        for K in self.Ks:
            a=K@rho@K.conj().T
            b=self.D@a@self.D.conj().T
            Kr=self.D@K@self.D.conj().T
            np.testing.assert_allclose(b,Kr@rel@Kr.conj().T,atol=2e-14)
            time_a=np.kron(self.F,np.eye(2))@a@np.kron(self.F.conj().T,np.eye(2))
            p1=p2=0.
            for j in times:
                R=expm(-1j*self.Hx*self.u[j])
                scalar_observable=R.conj().T@obs@R
                p1+=np.trace(scalar_observable@time_a[2*j:2*j+2,2*j:2*j+2]).real
                p2+=np.trace(obs@b[2*j:2*j+2,2*j:2*j+2]).real
            old.append(p1);new.append(p2)
        np.testing.assert_allclose(old,new,atol=1e-13)
        self.assertGreater(sum(old),0.)

    def test_free_clock_translation_and_band_constraint(self):
        dt=2*np.pi/self.n
        Ufree=np.kron(np.diag(np.exp(1j*self.k*dt)),expm(1j*self.Hx*dt))
        shift=np.roll(np.eye(self.n),1,axis=0)
        np.testing.assert_allclose(self.D@Ufree@self.D.conj().T,
                                   np.kron(shift,np.eye(2)),atol=4e-14)
        # This constraint is a correlated subspace, not all time functions.
        q=self.D@np.kron(self.P,np.eye(2))@self.D.conj().T
        self.assertAlmostEqual(np.trace(q).real,12.,places=12)
        np.testing.assert_allclose(q@q,q,atol=2e-14)
        original_time=np.kron(self.F@self.P@self.F.conj().T,np.eye(2))
        self.assertGreater(np.linalg.norm(q-original_time),.1)
        # A sharp time-bin projector does not preserve the valid band range.
        binop=np.kron(np.diag([1,0,0,0,0,0,0,0]),np.eye(2))
        self.assertGreater(np.linalg.norm((np.eye(16)-q)@binop@q),.1)

    def test_interaction_remains_nonlocal_in_r_coordinate(self):
        vals,V=np.linalg.eigh((self.E+self.E.conj().T)/2)
        theta=(V*np.arcsin(np.sqrt(np.clip(vals,0,1))))@V.conj().T
        Vrel=self.D@np.kron(theta,self.X)@self.D.conj().T
        diagonal=np.zeros_like(Vrel)
        for j in range(self.n):diagonal[2*j:2*j+2,2*j:2*j+2]=Vrel[2*j:2*j+2,2*j:2*j+2]
        self.assertGreater(np.linalg.norm(Vrel-diagonal),.1)
        p_rel=self.D@np.kron(self.P,np.eye(2))@self.D.conj().T
        np.testing.assert_allclose(Vrel@p_rel,p_rel@Vrel,atol=2e-14)

    def test_continuum_shift_and_robust_recovery_obstruction_constants(self):
        # Two equal-width disjoint momentum packets differ in time only by a
        # phase, so every time-bin density and the X-conditional state match.
        for u in (0.,.00003,.0004,.02,.2):
            base=np.sqrt(100/(2*np.pi))*np.sinc(50*u/np.pi)*np.exp(-1j*7050*u)
            shifted=np.sqrt(100/(2*np.pi))*np.sinc(50*u/np.pi)*np.exp(-1j*9050*u)
            self.assertAlmostEqual(abs(base)**2,abs(shifted)**2,places=12)
            self.assertAlmostEqual(abs(shifted-np.exp(-1j*2000*u)*base),0.,places=12)
        impulse,disp,*_=budgets();delta=impulse+disp
        kappa=(1-1/(2*np.pi))/2
        e=2*delta/kappa
        self.assertGreater(1-2*e,.9955)
        self.assertLess(2*e,.00444)
        self.assertGreater((1-4*e)/2,.4955)

    def test_time_reading_loses_clock_energy_coherence(self):
        # The no-bin clock comparator can produce either of two orthogonal
        # band states by choosing the input via its invertible no-bin Kraus op.
        g1=np.zeros(self.n,complex);g1[1:3]=1/np.sqrt(2)
        g2=np.zeros(self.n,complex);g2[4:6]=1/np.sqrt(2)
        self.assertAlmostEqual(abs(np.vdot(g1,g2)),0.,places=14)
        A0=root(np.eye(self.n)-self.E)
        inputs=[]
        for g in (g1,g2):
            x=np.linalg.solve(A0,g);x/=np.linalg.norm(x);inputs.append(x)
            y=A0@x;y/=np.linalg.norm(y)
            np.testing.assert_allclose(y,g,atol=1e-13)
        self.assertGreater(min(np.linalg.norm(A0@x)**2 for x in inputs),.04)
        # Identical every-time probabilities and X conditional states, but
        # orthogonal full clock outputs, including after the R-relative W.
        np.testing.assert_allclose(abs(self.F@g1)**2,abs(self.F@g2)**2,atol=1e-14)
        x=np.array([1.,1j])/np.sqrt(2)
        full=[self.D@np.kron(g,x) for g in (g1,g2)]
        self.assertAlmostEqual(abs(np.vdot(full[0],full[1])),0.,places=13)
        for j in range(self.n):
            a=full[0][2*j:2*j+2];b=full[1][2*j:2*j+2]
            np.testing.assert_allclose(np.outer(a,a.conj()),np.outer(b,b.conj()),atol=2e-14)
        # Different conserved energy measurements distinguish the states.
        energy_test=np.diag([0,1,1,0,0,0,0,0])
        self.assertAlmostEqual(np.vdot(g1,energy_test@g1).real,1.,places=13)
        self.assertAlmostEqual(np.vdot(g2,energy_test@g2).real,0.,places=13)


if __name__=='__main__':unittest.main()
