"""Unique constrained stationary history, conditional on stipulated projectors.

This selects a state as a kernel, not by relaxation from a nonzero-C seed.
The extracted old-environment qubit is a state-dependent, nonlocal encoding.
No objective cosmic energy, locality, subjecthood or actuality is asserted.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I,full_state
from verification.zero_all_sector_sphere_clock_work_test import complement_state
from verification.zero_relational_orientation_reference_test import C1,C2,C3,L,S,with_reference
from verification.zero_invariant_all_history_record_clock_test import (
    XL,ZL,H,PPLUS,PMINUS,NU,OMEGA,G,kron
)

I16=np.eye(16,dtype=complex)
I32=np.eye(32,dtype=complex)
I64=np.eye(64,dtype=complex)
I128=np.eye(128,dtype=complex)
# System order B,R,W,T,F,M. Clock is prepended in the whole.
W=np.vstack([kron(I,PPLUS),kron(I,PMINUS)])
Cclock=kron(I,I,H)-kron(NU*Z,I,I32)
Qclock=Cclock@Cclock/(4*NU**2)
Hcas=(C1@C1+C2@C2+C3@C3)/8
K=(I16-Hcas)@(I16+L)/2
Qbalance=kron(I,I,Hcas,I)
Qbranch=kron(I,I,(I16-L)/2,I)
A1=kron(Z,ZL,I)
A3=kron(I,I16,Z)


def family(phi):
    a2=kron(math.cos(phi)*X+math.sin(phi)*Y,XL,I)
    selectors=[W@((I64-a)/2)@W.conj().T for a in (A1,a2,A3)]
    return a2,selectors,Qbalance+Qbranch+Qclock+sum(selectors)


def seed():
    # Select an arbitrary representative of the one-dimensional Z_L=+1
    # subspace of the common complementary-zero and L=+1 kernel.
    p=K@(I16+ZL)/2
    k=int(np.argmax(np.linalg.norm(p,axis=0)))
    e0=p[:,k]/np.linalg.norm(p[:,k])
    e1=XL@e0
    m0=np.array([1,0],complex)
    b0=np.array([1,0],complex);b1=np.array([0,1],complex)
    v=(kron(b0,e0,m0)+kron(b1,e1,m0))/math.sqrt(2)
    return e0,e1,v


def reduced_record_memory(v):
    # v is system B,R,W,T,F,M, M measured in X basis.
    a=v.reshape(2,2,2,2,2,2)
    had=np.array([[1,1],[1,-1]],complex)/math.sqrt(2)
    a=np.einsum('mn,brwtfn->brwtfm',had,a)
    return np.sum(abs(a)**2,axis=(0,2,3,4))


class UniqueStationaryWholeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e0,cls.e1,cls.v=seed()
        cls.whole=W@cls.v
        cls.a2,cls.rs,cls.total=family(0)

    def test_constructed_operators_are_mutually_commuting_projectors(self):
        np.testing.assert_allclose(W.conj().T@W,I64,atol=1e-14)
        np.testing.assert_allclose(Cclock@W,0,atol=1e-14)
        ps=[Qbalance,Qbranch,Qclock]+self.rs
        for p in ps:
            np.testing.assert_allclose(p,p.conj().T,atol=1e-14)
            np.testing.assert_allclose(p@p,p,atol=1e-14)
        for i,p in enumerate(ps):
            for q in ps[i+1:]:np.testing.assert_allclose(p@q,q@p,atol=2e-14)
        for c in (C1,C2,C3):
            cwhole=kron(I,I,c,I)
            for p in ps:np.testing.assert_allclose(p@cwhole,cwhole@p,atol=2e-14)

    def test_exact_unique_zero_and_nonzero_gap(self):
        # The old balances plus the clock leave eight states, not one. Each
        # of the three stipulated binary relational selectors halves the kernel.
        progressive=Qbalance+Qbranch+Qclock
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(progressive))<1e-10),8)
        for selector,rank in zip(self.rs,(4,2,1)):
            progressive=progressive+selector
            self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(progressive))<1e-10),rank)
        eig=np.linalg.eigvalsh(self.total)
        self.assertEqual(np.count_nonzero(abs(eig)<1e-10),1)
        self.assertAlmostEqual(eig[1],1,places=12)
        np.testing.assert_allclose(self.total@self.whole,0,atol=2e-14)
        for c in (C1,C2,C3):
            np.testing.assert_allclose(kron(I,I,c,I)@self.whole,0,atol=1e-14)
        np.testing.assert_allclose(kron(I,I,L,I)@self.whole,self.whole,atol=1e-14)
        np.testing.assert_allclose(kron(I,I,S,I)@self.whole,self.whole,atol=1e-14)
        np.testing.assert_allclose(Cclock@self.whole,0,atol=1e-14)

    def test_conditional_history_and_clock_relative_correlations(self):
        for theta in (0,math.pi/4,math.pi/2,math.pi):
            bra=np.array([np.exp(-1j*theta),np.exp(1j*theta)])/math.sqrt(2)
            raw=kron(bra.reshape(1,2),I64)@self.whole
            expected=kron(I,math.cos(theta)*I32-1j*math.sin(theta)*H/NU)@self.v
            np.testing.assert_allclose(raw,expected/math.sqrt(2),atol=1e-14)
            for c in (C1,C2,C3):
                np.testing.assert_allclose(kron(I,c,I)@expected,0,atol=1e-14)
            contrast=G/NU*math.sin(2*theta)
            table=np.array([[(1+contrast)/4,(1-contrast)/4],[(1-contrast)/4,(1+contrast)/4]])
            np.testing.assert_allclose(reduced_record_memory(expected),table,atol=1e-14)

    def test_phase_family_and_opposite_constraints_retain_equal_zero_status(self):
        for phi in (0,math.pi/3,math.pi):
            a2,rs,total=family(phi)
            rb=math.cos(phi/2)*I-1j*math.sin(phi/2)*Z
            v=kron(rb,I32)@self.v
            whole=W@v
            self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(total))<1e-10),1)
            np.testing.assert_allclose(total@whole,0,atol=2e-14)
            self.assertAlmostEqual(abs(np.vdot(self.whole,whole))**2,math.cos(phi/2)**2,places=12)
            self.assertAlmostEqual(np.vdot(v,kron(X,XL,I)@v).real,math.cos(phi),places=12)
            self.assertAlmostEqual(np.vdot(v,kron(Y,XL,I)@v).real,math.sin(phi),places=12)
            np.testing.assert_allclose(a2@v,v,atol=1e-14)
        # If a fixed B phase reference makes both joint witnesses observable,
        # φ labels physically distinguishable inputs, not uniqueness from zero.

    def test_recover_actual_coherent_all_sector_state_by_environment_isometry(self):
        # Include a sector flag coherently; no physical old clock label is dropped.
        # The flag is a direct-sum representation of the two physical sectors.
        c=with_reference(full_state(4)).reshape(-1,16)
        d=with_reference(complement_state(4)).reshape(-1,16)
        for alpha,beta in ((1,0),(0,1),(1/math.sqrt(2),1j/math.sqrt(2)),
                           (math.sqrt(1/128),math.sqrt(127/128))):
            a=np.concatenate((alpha*c,beta*d),axis=0)
            f0=math.sqrt(2)*a@self.e0.conj()
            f1=math.sqrt(2)*a@self.e1.conj()
            self.assertAlmostEqual(np.vdot(f0,f0).real,1,places=12)
            self.assertAlmostEqual(np.vdot(f1,f1).real,1,places=12)
            self.assertLess(abs(np.vdot(f0,f1)),1e-12)
            np.testing.assert_allclose(a,(np.outer(f0,self.e0)+np.outer(f1,self.e1))/math.sqrt(2),atol=2e-14)
            # Thus V|0>=f0,V|1>=f1 is an isometry. The dressed selector
            # V A V† depends on this full selected old state and is nonlocal.

    def test_unselected_reference_zero_does_not_authorize_relaxation(self):
        # A unitary commuting with C1 preserves its squared norm, regardless
        # of whether its generator happens to have a unique ground state.
        cwhole=kron(I,I,C1,I)
        self.assertGreater(np.linalg.norm(cwhole),0)
        np.testing.assert_allclose(self.total@cwhole,cwhole@self.total,atol=2e-14)
        vals,vecs=np.linalg.eigh(cwhole)
        v=vecs[:,np.argmax(abs(vals))]
        energy, basis=np.linalg.eigh(self.total)
        evolved=basis@(np.exp(-.731j*energy)*(basis.conj().T@v))
        self.assertAlmostEqual(np.linalg.norm(cwhole@v),np.linalg.norm(cwhole@evolved),places=12)
        self.assertGreater(np.linalg.norm(cwhole@v),1)

if __name__=='__main__':unittest.main()
