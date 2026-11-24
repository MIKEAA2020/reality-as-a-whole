"""All-sector extension of the encoded sphere, clock and work construction.

Uses the prior two-dimensional code and an explicit commuting two-sector
instrument on its 254-dimensional complement. The latter is a fixed-setting
classical surrogate, not the original sharp quantum sphere instrument.
"""
import math
import unittest
import numpy as np
from verification.zero_three_balance_encoded_sphere_record_test import (
    CODE, PCODE, I256, local_charges, SINGLET
)
from verification.zero_encoded_sphere_clock_work_bridge_test import (
    HA, HB, logical_sphere_unitary, lab_apply, local_energy_apply
)
from verification.zero_five_ray_record_current_unification_test import q, ns, axis
from verification.zero_dual_pair_sphere_energy_instrument_test import bob_effects
from verification.zero_energy_sphere_work_incidence_test import (
    embed_records_and_work, target_memory, full_state, relative_read, project_h,
    h_memory_table, i_r_m_table, reduced_record, reduced_work, record_work,
    Jactive, Z, density_frobenius_sq, lab_vector
)

L = 4
D = I256-PCODE
idx = np.arange(256).reshape((4,4,4,4))
SWAP12 = I256[idx.transpose(1,0,2,3).ravel()]
SWAP23 = I256[idx.transpose(0,2,1,3).ravel()]
T = D@SWAP12@D
# T has eigenvalues -1, -1/5, 0 (code), 1. This polynomial is the
# projector onto its +1 eigenspace, without relying on eigenvector gauges.
PLUS = T@(T+I256)@(5*T+I256)/12
MINUS = D-PLUS
RANK = np.array([158., 96.])
FWEIGHTS = RANK/254
DOT = np.array(ns)@np.array(axis)
Q = np.array(q)
# Alice's two classical conditional response vectors. Row i averages to q_i.
FA = np.array([Q*(1-FWEIGHTS[1]*DOT), Q*(1+FWEIGHTS[0]*DOT)])
# Bob is unbiased overall, but his result is correlated with the sector.
B0 = np.array([.5+FWEIGHTS[1]/2, .5-FWEIGHTS[0]/2])
FB = np.stack([B0, 1-B0],axis=1)


def pointer_rotation(amplitudes):
    a = np.asarray(amplitudes,complex)
    e = np.eye(len(a),dtype=complex)[:,0]
    d = e-a
    if np.linalg.norm(d)<1e-14:
        return np.eye(len(a),dtype=complex)
    d /= np.linalg.norm(d)
    return np.eye(len(a),dtype=complex)-2*np.outer(d,d.conj())


def apply_local(v,U,roots_plus,roots_minus):
    """Apply sector-block unitary to a (lab, reference, pointer) tensor."""
    l,nout=v.shape[1:]
    code=np.einsum('xa,xrp->arp',CODE.conj(),v)
    code=(U@code.reshape(-1)).reshape(2,l,nout)
    out=np.einsum('xa,arp->xrp',CODE,code)
    for P,root in ((PLUS,roots_plus),(MINUS,roots_minus)):
        O=pointer_rotation(root)
        out+=np.einsum('xy,yrp,qp->xrq',P,v,O,optimize=True)
    return out


def complement_state(L=4,tau=math.pi/2, alice=FA):
    """Exact sector-compressed complement state; axes match old circuit.

    The two orthogonal labels stand for |Phi_PLUS> and |Phi_MINUS>, which
    are entangled 256x256 physical lab states. This is a global compression,
    not an assertion that either lab is a two-dimensional system.
    """
    base=np.zeros((2,2,L,L,L,L,3,2),complex)
    ref=np.eye(L)/math.sqrt(L)
    clocks=np.einsum('ac,bd->acbd',ref,ref)
    for s in range(2):
        for i in range(3):
            for j in range(2):
                base[s,s,:,:,:,:,i,j] = math.sqrt(FWEIGHTS[s]*alice[s,i]*FB[s,j])*clocks
    return target_memory(embed_records_and_work(base),tau)


def weighted_table(clock_code,clock_comp):
    return (i_r_m_table(clock_code)/128 + 127*i_r_m_table(clock_comp)/128)


def plus_state():
    return PLUS/math.sqrt(158)


def minus_state():
    return MINUS/math.sqrt(96)


class AllSectorSphereClockWorkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G=local_charges()
        cls.code=full_state(4)
        cls.comp=complement_state(4)
        cls.cc=relative_read(cls.code,4)
        cls.cf=relative_read(cls.comp,4)

    def test_complement_is_exact_invariant_sector_decomposition(self):
        np.testing.assert_allclose(PCODE+PLUS+MINUS,I256,atol=1e-13)
        for p,rank in ((PLUS,158),(MINUS,96)):
            np.testing.assert_allclose(p,p.conj().T,atol=1e-13)
            np.testing.assert_allclose(p@p,p,atol=1e-13)
            self.assertAlmostEqual(np.trace(p).real,rank,places=10)
            np.testing.assert_allclose(PCODE@p,0,atol=1e-13)
            for g in self.G: np.testing.assert_allclose(g@p-p@g,0,atol=1e-13)
            for H in (HA,HB): np.testing.assert_allclose(H@p-p@H,0,atol=1e-13)
        np.testing.assert_allclose(PLUS@MINUS,0,atol=1e-13)
        C=sum(g@g for g in self.G)
        self.assertAlmostEqual(np.trace(PLUS@C).real/158,528/79,places=12)
        self.assertAlmostEqual(np.trace(MINUS@C).real/96,5,places=12)
        eig=np.linalg.eigvalsh(T)
        np.testing.assert_allclose(eig,[-1]*95+[-.2]+[0]*2+[1]*158,atol=1e-12)
        # The complement is not generally classical: other invariant
        # compressed swaps fail to commute. The chosen interface below is.
        U=D@SWAP23@D
        self.assertGreater(np.linalg.norm(T@U-U@T),20)
        for g in self.G: np.testing.assert_allclose(g@U-U@g,0,atol=1e-13)

    def test_unselected_input_splits_coherently_without_discard(self):
        R=np.array([[0.,-1.],[1.,0.]])
        V=CODE@R@CODE.T+D
        M=V.T/16
        code=CODE@SINGLET@CODE.T/math.sqrt(128)
        complement=(math.sqrt(158)*plus_state()+math.sqrt(96)*minus_state())/16
        np.testing.assert_allclose(M,code+complement,atol=1e-14)
        self.assertAlmostEqual(np.linalg.norm(code)**2,1/128,places=13)
        self.assertAlmostEqual(np.linalg.norm(complement)**2,127/128,places=13)
        for part in (code,plus_state(),minus_state()):
            for g in self.G: np.testing.assert_allclose(g@part-part@g.T,0,atol=1e-13)
            np.testing.assert_allclose(HA@part+part@HB.T,0,atol=1e-13)
        self.assertGreater(np.linalg.norm(self.G[0]@plus_state()),.01)
        # For |Phi_P>, (G_A-G_B)|Phi_P>=0, but G_A alone need not vanish.

    def test_full_local_instruments_are_unitary_and_conserve_both_charges(self):
        rng=np.random.default_rng(230)
        for F,H in ((None,HA),(bob_effects(),HB)):
            U=logical_sphere_unitary(L,F)
            probs=FA if F is None else FB
            n=probs.shape[1]
            for s in range(2):
                self.assertAlmostEqual(sum(probs[s]),1,places=13)
                self.assertGreater(np.min(probs[s]),0)
                O=pointer_rotation(np.sqrt(probs[s]))
                np.testing.assert_allclose(O.conj().T@O,np.eye(n),atol=1e-13)
                np.testing.assert_allclose(O[:,0],np.sqrt(probs[s]),atol=1e-13)
            v=rng.normal(size=(256,L,n))+1j*rng.normal(size=(256,L,n))
            v/=np.linalg.norm(v)
            out=apply_local(v,U,np.sqrt(probs[0]),np.sqrt(probs[1]))
            self.assertAlmostEqual(np.linalg.norm(out),1,places=12)
            np.testing.assert_allclose(local_energy_apply(H,out),
                apply_local(local_energy_apply(H,v),U,np.sqrt(probs[0]),np.sqrt(probs[1])),atol=1e-13)
            for g in self.G:
                np.testing.assert_allclose(lab_apply(g,out),
                    apply_local(lab_apply(g,v),U,np.sqrt(probs[0]),np.sqrt(probs[1])),atol=1e-13)
        # Block unitarity and full operator commutators follow from the
        # orthogonal projectors and the separately tested energy-block U.

    def test_each_complement_pointer_pair_preserves_global_directional_balance(self):
        M=D/math.sqrt(254)
        for i in range(3):
            A=math.sqrt(FA[0,i])*PLUS+math.sqrt(FA[1,i])*MINUS
            for j in range(2):
                B=math.sqrt(FB[0,j])*PLUS+math.sqrt(FB[1,j])*MINUS
                branch=A@M@B.T
                for g in self.G:
                    np.testing.assert_allclose(g@branch-branch@g.T,0,atol=1e-13)
                np.testing.assert_allclose(HA@branch+branch@HB.T,0,atol=1e-13)
                self.assertGreater(np.linalg.norm(branch),.01)
        # No pointer branch requires a vanishing individual lab generator.

    def test_every_sector_has_finite_clock_and_work_target_record(self):
        for v,vs in ((self.code,self.cc),(self.comp,self.cf)):
            self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
            p=sum(np.vdot(a,a).real for a in vs)
            self.assertAlmostEqual(p,3/16,places=12)
            np.testing.assert_allclose(h_memory_table(vs)/p,[[.5,0],[0,.5]],atol=1e-12)
            table=i_r_m_table(vs)/p
            np.testing.assert_allclose(table[:,:,0],table[:,:,1],atol=1e-12)
            np.testing.assert_allclose(table.sum(axis=(0,2)),[.5,.5],atol=1e-12)
            for h in (0,1):
                hv=[project_h(a,h) for a in vs]; ph=sum(np.vdot(a,a).real for a in hv)
                np.testing.assert_allclose(reduced_record(hv)/ph,np.eye(2)/2,atol=1e-12)
                np.testing.assert_allclose(reduced_work(hv)/ph,np.eye(2)/2,atol=1e-12)
                K=np.kron(Z,Jactive)
                np.testing.assert_allclose(record_work(hv)/ph,
                    (np.eye(4)+(1-2*h)*K)/4,atol=1e-12)
        # Both sectors reach the same record/work relation, not just the
        # previously selected 1/128 code sector.

    def test_complement_statistics_and_unselected_whole(self):
        actual=i_r_m_table(self.cf).sum(axis=2)/(3/16)
        predicted=np.einsum('s,si,sj->ij',FWEIGHTS,FA,FB)
        np.testing.assert_allclose(actual,predicted,atol=1e-13)
        eta=3792/16129
        target=np.array([[qi*(1-eta*d)/2,qi*(1+eta*d)/2] for qi,d in zip(Q,DOT)])
        np.testing.assert_allclose(actual,target,atol=1e-13)
        all_table=weighted_table(self.cc,self.cf).sum(axis=2)/(3/16)
        np.testing.assert_allclose(all_table.sum(axis=1),Q,atol=1e-13)
        np.testing.assert_allclose(all_table.sum(axis=0),[.5,.5],atol=1e-13)
        self.assertGreater(np.linalg.norm(actual-np.outer(Q,[.5,.5])),.03)
        event=(weighted_table(self.cc,self.cf)[:,0,1]).sum()
        self.assertAlmostEqual(event,3/64,places=12)
        self.assertAlmostEqual(event/128,3/8192,places=13)
        # The event is no longer restricted to the encoded flag. The full
        # branch state has orthogonal flags, with no postselection assumed.

    def test_zero_energy_for_all_clock_branches_and_directional_pairing(self):
        # Complement: lab energies are zero, reference clocks remain paired,
        # work energy 2 cancels the clock's -2 offset on every component.
        energy=(np.arange(L)[:,None,None,None]-np.arange(L)[None,:,None,None]
                +np.arange(L)[None,None,:,None]-np.arange(L)[None,None,None,:])
        for a in [self.comp]+self.cf:
            self.assertLess(np.linalg.norm(a*energy[None,None,:,:,:,:,None,None,None,None,None]),1e-12)
        for physical in (plus_state(),minus_state()):
            for g in self.G:
                np.testing.assert_allclose(g@physical-physical@g.T,0,atol=1e-13)
            np.testing.assert_allclose(HA@physical+physical@HB.T,0,atol=1e-13)
        # Encoded branch Q=0 was verified as an operator-intertwining result
        # by the bridge verifier; no common lab-zero claim is made for D.

    def test_alice_setting_no_signal_even_after_clock_window(self):
        # Alternate complement Alice POVM: q_i I on each sector. Both
        # instruments are complete; the pre-existing Bob reduced state is
        # unchanged by either nonselective local operation.
        M=D/math.sqrt(254)
        rho=M.T@M.conj()
        for f in (FA,np.stack([Q,Q])):
            rhs=np.zeros_like(rho)
            for i in range(3):
                A=math.sqrt(f[0,i])*PLUS+math.sqrt(f[1,i])*MINUS
                a=A@M;rhs+=a.T@a.conj()
            np.testing.assert_allclose(rhs,rho,atol=1e-13)
        alt=complement_state(4,alice=np.stack([Q,Q]))
        np.testing.assert_allclose(i_r_m_table(relative_read(alt,4)).sum(axis=(0,2))/(3/16),
                                   [.5,.5],atol=1e-12)
        from verification.zero_dual_pair_sphere_energy_instrument_test import axis, SIGMA, I
        op=sum(x*s for x,s in zip(axis,SIGMA)); pair=np.array([(I+op)/2,(I-op)/2])
        x=np.concatenate([lab_vector(v) for v in self.cc],axis=1)
        y=np.concatenate([lab_vector(v) for v in relative_read(full_state(4,FA=pair),4)],axis=1)
        self.assertLess(density_frobenius_sq(x,y),1e-12)
        # Alice's flag and pointer are traced; a joint clock window is an
        # explicitly retained B+clock interface, not an automatic local report.

if __name__=='__main__':
    unittest.main()
