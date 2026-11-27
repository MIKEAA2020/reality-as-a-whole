"""Retained-clock instrument ambiguity: finite cyclic control.

Uses the actual two-window packet projector Q, but replaces Ω/cursor dynamics
with a separately specified cyclic gate. The continuum operator construction
and its different physical assumptions are in the accompanying report.
"""
import unittest
import numpy as np
from scipy.integrate import quad
from verification.zero_two_window_autonomous_support_dynamics_test import system


def dist(a,b):
    x=a-b;x=(x+x.conj().T)/2
    return float(np.sum(np.abs(np.linalg.eigvalsh(x)))/2)


def build():
    _,B,P,Q,_,_=system(2,0)
    n=4; d=len(P); eye=np.eye(d); x=np.array([[0.,1.],[1.,0.]])
    shift=np.roll(np.eye(n),1,axis=0)
    step=np.kron(np.kron(P,np.eye(2))+np.kron(Q,x),shift)
    clock=np.zeros((n,n));clock[0,0]=1
    pieces=[]
    for m in (0,1):
        mem=np.diag([int(i==m) for i in (0,1)])
        a=np.kron(np.kron(eye,mem),clock)
        row=[]
        for t in range(n):
            u=np.linalg.matrix_power(step,t)
            row.append(u.conj().T@a@u)
        pieces.append(row)
    effects=[sum(row) for row in pieces]
    feedback=np.kron(np.kron(eye,np.eye(2)),shift)
    beta=np.array([1.,0.,1.,0.])/np.sqrt(2)
    state=np.kron(np.kron(B[:,0],np.array([1.,0.])),beta)
    rho=np.outer(state,state.conj())
    return step,pieces,effects,feedback,state,rho


class RetainedClockInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.step,cls.parts,cls.effects,cls.feedback,cls.psi,cls.rho=build()

    def test_normalized_clock_neutral_effects_and_covariant_feedback(self):
        U=self.step;effects=self.effects
        np.testing.assert_allclose(np.linalg.matrix_power(U,4),np.eye(len(U)),atol=1e-12)
        np.testing.assert_allclose(sum(effects),np.eye(len(U)),atol=1e-12)
        for E in effects:
            np.testing.assert_allclose(E@U,U@E,atol=1e-12)
            np.testing.assert_allclose(E@E,E,atol=1e-12)
        np.testing.assert_allclose(self.feedback@U,U@self.feedback,atol=1e-12)

    def test_hidden_time_and_coherent_luders_have_identical_effects(self):
        for m in (0,1):
            E=self.effects[m]
            fine=sum((p.conj().T@p for p in self.parts[m]))
            np.testing.assert_allclose(fine,E,atol=1e-12)
            # In this cyclic projective control F is a projector, so sqrt(F)=F.
            np.testing.assert_allclose(E.conj().T@E,E,atol=1e-12)
            p1=np.trace(E@self.rho@E).real
            p2=sum(np.trace(p@self.rho@p).real for p in self.parts[m])
            self.assertAlmostEqual(p1,p2,places=12)

    def test_same_certainty_different_retained_clock_poststates(self):
        E=self.effects[0]
        coherent=E@self.rho@E
        fine=sum((p@self.rho@p for p in self.parts[0]))
        self.assertAlmostEqual(np.trace(coherent).real,1.,places=12)
        self.assertAlmostEqual(np.trace(fine).real,1.,places=12)
        self.assertAlmostEqual(dist(coherent,fine),.5,places=12)
        # An outcome-dependent unitary feedback has identical m probability
        # and can alter the retained clock even more dramatically.
        shifted=self.feedback@coherent@self.feedback.conj().T
        self.assertAlmostEqual(np.trace(shifted).real,1.,places=12)
        self.assertAlmostEqual(dist(coherent,shifted),1.,places=12)

    def test_continuous_clock_preparation_can_be_shifted_to_orthogonality(self):
        # The earlier cosine-band initial clock wavefunction has |β|²
        # proportional to cos²(πx/2), x∈[-1,1]. The momentum-generated
        # shift s=2π/b has zero overlap with that initial state. This is not
        # a numerical calculation of the event-conditioned continuum state.
        re=quad(lambda x:np.cos(np.pi*x/2)**2*np.cos(2*np.pi*x),-1,1)[0]
        im=quad(lambda x:np.cos(np.pi*x/2)**2*np.sin(2*np.pi*x),-1,1)[0]
        self.assertAlmostEqual(re,0.,places=13)
        self.assertAlmostEqual(im,0.,places=13)

    def test_mixed_hidden_time_not_coherent(self):
        # Direct check: hidden-time map is idempotent in this finite control.
        fine=sum((p@self.rho@p for p in self.parts[0]))
        again=sum((p@fine@p for p in self.parts[0]))
        np.testing.assert_allclose(fine,again,atol=1e-13)
        self.assertAlmostEqual(dist(fine,self.rho),.5,places=12)


if __name__=='__main__':unittest.main()
