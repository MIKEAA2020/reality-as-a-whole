"""Tests a new autonomous implementation of a selected relational effect.

The continuum argument is in ZERO_AUTONOMOUS_CLOCK_EVENT_READOUT.md.
This finite cyclic/Fourier-grid test is not a simulation of the full old
massive-cursor + semibounded clock event effect.
"""
import math
import unittest
import numpy as np
from scipy.linalg import expm
from verification.zero_two_window_autonomous_support_dynamics_test import system


def finite_event():
    _,B,P,Q,_,_=system(2,0)
    q=Q[:,np.argmax(np.linalg.norm(Q,axis=0))];q/=np.linalg.norm(q)
    Z=np.column_stack((B[:,0],q));p=Z.conj().T@P@Z;q=Z.conj().T@Q@Z
    X=np.array([[0,1],[1,0]],complex)
    gate=np.kron(p,np.eye(2))+np.kron(q,X)
    S=np.roll(np.eye(4),1,axis=0);U=np.kron(gate,S)
    # An unsharp cyclic clock effect of trace two; its four translates sum 2I.
    E=np.diag([.8,.2,.6,.4]);pi1=np.diag([0,1]);a=np.kron(np.kron(np.eye(2),pi1),E)
    F=sum(np.linalg.matrix_power(U,t).conj().T@a@np.linalg.matrix_power(U,t) for t in range(4))/2
    # H is a positive cyclic Hamiltonian, U=exp(iH).
    H=np.zeros_like(U,dtype=complex)
    for k in range(4):
        proj=sum(np.exp(-2j*np.pi*k*j/4)*np.linalg.matrix_power(U,j) for j in range(4))/4
        H+=(np.pi*k/2)*proj
    F=(F+F.conj().T)/2;H=(H+H.conj().T)/2
    values,vec=np.linalg.eigh(F)
    theta=(vec*np.arcsin(np.sqrt(np.clip(values,0,1))))@vec.conj().T
    return U,H,F,theta,values


def packet(x,a=.3):
    z=x/a
    return np.sqrt(315/(256*a))*np.where(abs(z)<=1,(1-z*z)**2,0.)


def pulse(x,b=.3):
    z=x/b
    return 15/(16*b)*np.where(abs(z)<=1,(1-z*z)**2,0.)


def budget(T=1.7,a=.3,b=.3,mass=1e6):
    k=math.pi/2
    d1=k*15/(8*b)
    d2=k*10/(math.sqrt(3)*b*b)+d1*d1
    K=math.sqrt(63/2)/a**2+2*math.sqrt(3)/a*d1+d2
    return T*K/(2*mass)


def split_evolve(theta,mass=1e6,steps=1700,n=2048,T=1.7,drift=-1.,crossed=True):
    # Envelope dynamics with +i Ht, p=-i∂x: negative carrier velocity
    # coefficient -vp translates the packet to the right. Periodic grid is
    # a numerical approximation; continuum control is analytical.
    length=8.;dx=length/n;x=np.arange(n)*dx-length/2
    k=2*np.pi*np.fft.fftfreq(n,d=dx);dt=T/steps
    states=np.zeros((2,n),complex);states[0]=packet(x+1.)
    kick=np.exp(1j*(drift*k+k*k/(2*mass))*dt/2)
    c=np.cos(theta*pulse(x)*dt);s=np.sin(theta*pulse(x)*dt)
    for _ in range(steps):
        states=np.fft.ifft(np.fft.fft(states,axis=1)*kick,axis=1)
        z0=c*states[0]+s*states[1]; z1=-s*states[0]+c*states[1]
        states=np.stack((z0,z1))
        states=np.fft.ifft(np.fft.fft(states,axis=1)*kick,axis=1)
    angle=theta if crossed else 0.
    target=np.stack((math.cos(angle)*packet(x+1+drift*T),-math.sin(angle)*packet(x+1+drift*T)))
    err=math.sqrt(dx*np.sum(abs(states-target)**2))
    return err,dx*np.sum(abs(states)**2),states,x,dx


class AutonomousClockReadoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.U,cls.H,cls.F,cls.theta,cls.lambdas=finite_event()

    def test_event_is_valid_and_commutes_with_hamiltonian(self):
        np.testing.assert_allclose(expm(1j*self.H),self.U,atol=1e-12)
        self.assertGreaterEqual(self.lambdas.min(),-1e-12)
        self.assertLessEqual(self.lambdas.max(),1+1e-12)
        # The P sector contains sharp 0/1 eigenvalues; Q supplies genuinely
        # unsharp eigenvalues, rather than treating the whole effect as sharp.
        self.assertGreater(np.count_nonzero((self.lambdas>.01)&(self.lambdas<.99)),0)
        np.testing.assert_allclose(np.unique(np.round(self.lambdas,8)),[0,.3,.7,1],atol=1e-12)
        np.testing.assert_allclose(self.H@self.F,self.F@self.H,atol=1e-12)
        np.testing.assert_allclose(self.H@self.theta,self.theta@self.H,atol=1e-12)

    def test_pointer_hamiltonian_realizes_luders_instrument(self):
        sy=np.array([[0,-1j],[1j,0]])
        W=expm(1j*np.kron(self.theta,sy))
        k0=W[0::2,0::2];k1=W[1::2,0::2]
        vals,V=np.linalg.eigh(self.F)
        root1=(V*np.sqrt(np.clip(vals,0,1)))@V.conj().T
        root0=(V*np.sqrt(np.clip(1-vals,0,1)))@V.conj().T
        np.testing.assert_allclose(k0,root0,atol=1e-12)
        np.testing.assert_allclose(k1,-root1,atol=1e-12)
        np.testing.assert_allclose(k0.conj().T@k0+k1.conj().T@k1,np.eye(len(self.F)),atol=1e-12)

    def test_same_effect_different_time_label_discarding_instrument(self):
        # Same event, but the earlier orbit-label-discarding operation is not
        # the newly implemented coherent square-root operation.
        E=np.diag([.8,.2,.6,.4]);sE=np.sqrt(E)
        rng=np.random.default_rng(87)
        v=rng.normal(size=16)+1j*rng.normal(size=16);v/=np.linalg.norm(v)
        rho=np.outer(v,v.conj());total_distance=0.
        vals,V=np.linalg.eigh(self.F)
        for m in (0,1):
            A=np.kron(np.kron(np.eye(2),np.diag([1-m,m])),sE)
            f=(np.eye(16)-self.F) if m==0 else self.F
            root=(V*np.sqrt(np.clip((1-vals) if m==0 else vals,0,1)))@V.conj().T
            old=np.zeros((16,16),complex);effect=np.zeros_like(old)
            for t in range(4):
                u=np.linalg.matrix_power(self.U,t);K=u.conj().T@A@u/np.sqrt(2)
                old+=K@rho@K.conj().T;effect+=K.conj().T@K
            coherent=root@rho@root
            np.testing.assert_allclose(effect,f,atol=1e-12)
            self.assertAlmostEqual(np.trace(old).real,np.trace(coherent).real,places=13)
            total_distance+=np.sum(abs(np.linalg.eigvalsh(old-coherent)))/2
        self.assertGreater(total_distance,.1)

    def test_corrected_cursor_orientation(self):
        # In +iHt convention, e^(+i a p) translates a packet LEFT.
        n=1024;L=8.;dx=L/n;x=np.arange(n)*dx-L/2
        k=2*np.pi*np.fft.fftfreq(n,dx);psi=packet(x+1)
        for sign in (-1,1):
            shifted=np.fft.ifft(np.exp(1j*sign*k*.25)*np.fft.fft(psi))
            target=packet(x+1+sign*.25)
            self.assertLess(math.sqrt(dx*np.sum(abs(shifted-target)**2)),2e-6)
            mean=dx*np.sum(x*abs(shifted)**2)
            self.assertAlmostEqual(mean,-1-sign*.25,places=6)

    def test_massive_cursor_against_ideal_gate(self):
        self.assertLess(budget(),.000318)
        for lam in (.3,.7,1.):
            theta=math.asin(math.sqrt(lam))
            err,norm,_,_,_=split_evolve(theta)
            self.assertLess(err,budget()+3e-5)
            self.assertAlmostEqual(norm,1.,places=7)

    def test_old_wrong_direction_misses_and_has_small_tail_bound(self):
        # Old parameters: the entire chiral packet stays left of the reader.
        a=b=1e-6;t0=math.pi/200;T=math.pi/100;mass=1e16
        self.assertLess(-t0+a,-b)
        amplitude=T*math.sqrt(63/2)/a**2/(2*mass)
        self.assertLess(amplitude,8.817e-6)
        self.assertLess(amplitude**2,7.773e-11)
        # Separate moderate-scale Fourier control, with a nonzero coupling.
        err,norm,states,x,dx=split_evolve(math.pi/2,drift=1.,crossed=False)
        self.assertLess(dx*np.sum(abs(states[1])**2),1e-8)
        self.assertLess(err,budget()+3e-5)

    def test_uncoupled_pointer_no_record(self):
        err,norm,states,x,dx=split_evolve(0.)
        self.assertLess(dx*np.sum(abs(states[1])**2),1e-22)
        self.assertLess(err,budget()+3e-5)


if __name__=='__main__':unittest.main()
