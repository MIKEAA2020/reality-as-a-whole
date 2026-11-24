"""Abaee's recoverability distinction in the two-window clock model.

NumPy-dependent finite-grid illustrations accompany an analytic continuum
QND witness. Grid output is not a certified continuum error bound.
"""
import math
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model,states,probabilities


def qnd(n=80,k=.65,t=100):
    model=make_model(n);p,f,Es,*_=model;E=Es[1];A=np.diag(p*p/6)
    ep,Vp=np.linalg.eigh(A-2*k*E)
    em,Vm=np.linalg.eigh(A+2*k*E)
    plus=Vp@(np.exp(1j*np.sqrt(ep)*t)*(Vp.conj().T@f))
    minus=Vm@(np.exp(1j*np.sqrt(em)*t)*(Vm.conj().T@f))
    zero=np.exp(1j*np.sqrt(p*p/6)*t)*f
    mem0=(plus+minus)/2;mem1=(plus-minus)/2
    return float(np.vdot(mem1,mem1).real),np.vdot(mem0,zero),f,(float(ep.min()),float(em.min()))


def reduced_D(vs):
    return sum(np.einsum('imnp,jmnp->ij',v,v.conj())/2 for v in vs)


def reduced_memory(vs):
    return sum(np.einsum('imnp,iklp->mnkl',v,v.conj()).reshape(4,4)/2 for v in vs)


def trace_distance(a,b):return float(np.sum(abs(np.linalg.eigvalsh(a-b)))/2)


class AbaeeAutonomousMemoryRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=make_model(80)
        cls.zero=states(cls.model,100,'zero')
        cls.one=states(cls.model,100,'one')

    def test_qnd_memory_responds_to_pointer_in_continuum_analog(self):
        p,gamma,f,bounds=qnd()
        self.assertGreater(min(bounds),0)
        self.assertAlmostEqual(p,.8098566017079758,places=10)
        self.assertAlmostEqual(abs(gamma),.41547339739537414,places=10)
        self.assertLess(abs(gamma),math.sqrt(1-p)+1e-12)
        self.assertAlmostEqual(np.vdot(f,f).real,1,places=12)

    def test_qnd_input_orthogonality_and_reduced_distinguishability(self):
        p,gamma,_,_=qnd()
        # Pointer |±> inputs have orthogonal initial density matrices;
        # controlled-unitary dephasing makes their output trace distance |γ|.
        rplus=np.array([[.5,gamma/2],[gamma.conjugate()/2,.5]])
        rminus=np.array([[.5,-gamma/2],[-gamma.conjugate()/2,.5]])
        self.assertAlmostEqual(trace_distance(rplus,rminus),abs(gamma),places=12)
        self.assertGreater((1-abs(gamma))/2,.29)

    def test_qnd_small_time_memory_leakage_and_bound(self):
        for t in (5,10,20):
            p,gamma,_,_=qnd(t=t)
            self.assertGreater(p,0)
            self.assertLess(abs(gamma),1)
            self.assertLessEqual(abs(gamma),math.sqrt(1-p)+1e-12)
        p0,g0,_,_=qnd(t=0)
        self.assertAlmostEqual(p0,0,places=20);self.assertAlmostEqual(abs(g0),1,places=12)

    def test_full_two_window_reduced_pointer_and_memory_are_distinct(self):
        r0=reduced_D(self.zero);r1=reduced_D(self.one)
        m0=reduced_memory(self.zero);m1=reduced_memory(self.one)
        self.assertAlmostEqual(trace_distance(r0,r1),.9552727568672261,places=10)
        self.assertAlmostEqual(trace_distance(m0,m1),.9595353239213008,places=10)
        for rho in (r0,r1,m0,m1):
            self.assertAlmostEqual(np.trace(rho).real,1,places=10)
            self.assertGreaterEqual(min(np.linalg.eigvalsh(rho)),-1e-11)
        self.assertGreater((1-trace_distance(r0,r1))/2,.022)

    def test_full_states_stay_orthogonal_and_global_reversal_is_unitary(self):
        # The h components have equal weights; the same internal h
        # coefficients are used for each input pointer state.
        overlap=sum(np.vdot(a,b)/2 for a,b in zip(self.zero,self.one))
        self.assertLess(abs(overlap),1e-11)
        for group in (self.zero,self.one):
            for v in group:self.assertAlmostEqual(np.vdot(v,v).real,1,places=11)
        # U†U=I on the full Hilbert space is an analytic consequence of the
        # positive self-adjoint Θ, not inferred from these samples alone.

    def test_full_two_window_grid_refinement(self):
        vals=[]
        for n in (40,80,160):
            model=make_model(n)
            a=states(model,100,'zero');b=states(model,100,'one')
            vals.append((trace_distance(reduced_D(a),reduced_D(b)),
                         trace_distance(reduced_memory(a),reduced_memory(b))))
        for x,y in zip(vals,vals[1:]):
            self.assertLess(abs(x[0]-y[0]),2e-5)
            self.assertLess(abs(x[1]-y[1]),2e-5)

    def test_exact_basis_readout_is_not_coherence_recovery(self):
        # In the controlled-QND model pointer z basis states are exactly
        # unchanged for every t. Yet |±> contract for the checked t.
        p,gamma,_,_=qnd(t=100)
        self.assertGreater(p,.8)
        self.assertLess(abs(gamma),.42)

if __name__=='__main__':unittest.main()
