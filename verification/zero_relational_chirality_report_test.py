"""Invariant, balanced relational sign and a neutral report pointer.

A new charged singlet pair and control interaction are stipulated. The sign is
not a demonstrated experience or an exact readout of the prior j=Z_R Z_T.
"""
import math
import unittest
from functools import reduce
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I,full_state,relative_read
from verification.zero_all_sector_noncommuting_sphere_test import (
    active_base,compressed_spin_base,remainder_base,output
)
from verification.zero_relational_orientation_reference_test import (
    U8,U1,Jw,L,C1,C2,C3,with_reference
)
from verification.zero_invariant_all_history_record_clock_test import XL,ZL
from verification.zero_constitution_hamiltonian_phase_gate_test import X16,Z16,J16,P16
from verification.zero_reciprocal_subject_exchange_test import n
from verification.zero_five_ray_record_current_unification_test import q,ns,axis
from verification.zero_all_sector_branchwise_balance_test import Q8


def kron(*a):return reduce(np.kron,a)

pauli=(X,Y,Z)
eps=((0,1,2,1),(1,2,0,1),(2,0,1,1),(0,2,1,-1),(2,1,0,-1),(1,0,2,-1))
I16=np.eye(16,dtype=complex);I64=np.eye(64,dtype=complex)
A=[kron(x,I,I,I) for x in (U8,U1,Jw)]
D=[kron(I16,x,I) for x in pauli]
E=[kron(I16,I,x) for x in pauli]
C=[kron(c,I,I)+d+e for c,d,e in zip((C1,C2,C3),D,E)]
LL=kron(L,I,I)
CHI=sum(s*A[i]@D[j]@E[k] for i,j,k,s in eps)/(2*math.sqrt(3))
CHISQ=CHI@CHI
PP=(CHISQ+CHI)/2
PM=(CHISQ-CHI)/2
P0=I64-CHISQ
# Ready 0 -> positive or zero; negative -> ready 1.
GATE=kron(I64-PM,I)+kron(PM,X)
HREP=(math.pi/2)*kron(PM,I-X)
SWAP=kron(I16,(kron(I,I)+sum(kron(x,x) for x in pauli))/2)
MIRROR=kron(SWAP,X)
SING=np.array([[0,1],[-1,0]],complex)/math.sqrt(2)
J=kron(kron(kron(kron(Z,I),Z),I),I,I)


def apply64(op,v):
    assert v.shape[-6:]==(2,2,2,2,2,2)
    return np.einsum('xy,...y->...x',op,v.reshape(v.shape[:-6]+(64,)),optimize=True).reshape(v.shape)


def initial(v):
    return np.einsum('...f,de->...fde',with_reference(v),SING)


def outcome_tables(v):
    # v axes a,b,RA,CA,RB,CB,i,j,R,W,T,F,D,E.
    branches=[apply64(p,v) for p in (PP,PM)]
    tab=np.stack([np.sum(abs(x)**2,axis=(0,1,2,3,4,5,7,8,9,10,11,12,13))
                  for x in branches],axis=1)
    return branches,tab


class RelationalChiralityReportTests(unittest.TestCase):
    def test_relational_observable_and_record_are_exactly_conserving(self):
        np.testing.assert_allclose(CHI,CHI.conj().T,atol=1e-14)
        np.testing.assert_allclose(CHI@CHI@CHI,CHI,atol=1e-13)
        np.testing.assert_allclose(PP@PP,PP,atol=1e-13)
        np.testing.assert_allclose(PM@PM,PM,atol=1e-13)
        np.testing.assert_allclose(PP@PM,0,atol=1e-13)
        np.testing.assert_allclose(GATE.conj().T@GATE,np.eye(128),atol=1e-13)
        val,vec=np.linalg.eigh(HREP)
        np.testing.assert_allclose((vec*np.exp(-1j*val))@vec.conj().T,GATE,atol=1e-13)
        blocks=GATE.reshape(64,2,64,2)
        np.testing.assert_allclose(blocks[:,0,:,0],I64-PM,atol=1e-13)
        np.testing.assert_allclose(blocks[:,1,:,0],PM,atol=1e-13)
        for c in C:
            np.testing.assert_allclose(CHI@c-c@CHI,0,atol=1e-13)
            np.testing.assert_allclose(HREP@kron(c,I)-kron(c,I)@HREP,0,atol=1e-13)
            np.testing.assert_allclose(GATE@kron(c,I)-kron(c,I)@GATE,0,atol=1e-13)
        np.testing.assert_allclose(CHI@LL-LL@CHI,0,atol=1e-13)
        np.testing.assert_allclose(SWAP@CHI@SWAP,-CHI,atol=1e-13)
        np.testing.assert_allclose(MIRROR@GATE@MIRROR,
                                   kron(P0,I)+kron(PP,X)+kron(PM,I),atol=1e-13)
        for c in C:np.testing.assert_allclose(SWAP@c-c@SWAP,0,atol=1e-13)
        # χ is a relational pseudoscalar; the neutral pointer records it.

    def test_exchange_algebra_and_clock_compatibility(self):
        swap_ad=(I64+sum(a@d for a,d in zip(A,D)))/2
        swap_ae=(I64+sum(a@e for a,e in zip(A,E)))/2
        np.testing.assert_allclose(CHI,-1j*(swap_ad@swap_ae-swap_ae@swap_ad)/math.sqrt(3),atol=1e-13)
        for op in (swap_ad,swap_ae):
            np.testing.assert_allclose(op@op,I64,atol=1e-13)
            for c in C:np.testing.assert_allclose(op@c-c@op,0,atol=1e-13)
        # Existing later clock Hamiltonian acts on RWT F and its own memory;
        # both its generators commute with the new relational readout.
        for t in (XL,ZL):
            op=kron(t,I,I)
            np.testing.assert_allclose(op@CHI-CHI@op,0,atol=1e-13)
            np.testing.assert_allclose(op@PP-PP@op,0,atol=1e-13)
            np.testing.assert_allclose(op@PM-PM@op,0,atol=1e-13)
            for c in C:np.testing.assert_allclose(op@c-c@op,0,atol=1e-13)
        # χ is built from exchange commutators; this does not derive the
        # physical control Hamiltonian or resources from the whole.

    def test_actual_states_and_all_old_clock_labels(self):
        states=[full_state(4),output(active_base()),output(compressed_spin_base(3)),
                output(compressed_spin_base(9)),output(remainder_base())]
        for state in states:
            for old in relative_read(state,4,labels=tuple(range(16))):
                v=initial(old);mass=np.linalg.norm(v)**2
                self.assertAlmostEqual(mass,1/16,places=12)
                for c in C:self.assertLess(np.linalg.norm(apply64(c,v)),1e-12)
                np.testing.assert_allclose(apply64(LL,v),v,atol=1e-13)
                np.testing.assert_allclose(apply64(CHISQ,v),v,atol=1e-13)
                plusminus,tab=outcome_tables(v)
                np.testing.assert_allclose(tab,np.array(q)[:,None]*mass/2*np.ones((1,2)),atol=1e-13)
                d=np.array(ns)@np.array(axis)
                self.assertAlmostEqual(tab[d<0].sum()/mass,3/5,places=12)
                self.assertAlmostEqual(np.einsum('is,s->',tab,[1,-1]),0,places=13)
                self.assertAlmostEqual(np.einsum('is,i,s->',tab,np.sign(d),[1,-1]),0,places=13)
                for sign,x in zip((1,-1),plusminus):
                    self.assertAlmostEqual(np.linalg.norm(x)**2,mass/2,places=12)
                    np.testing.assert_allclose(apply64(CHI,x),sign*x,atol=1e-13)
                    np.testing.assert_allclose(apply64(LL,x),x,atol=1e-13)
                    self.assertLess(np.linalg.norm(apply64(kron(Q8,I,I,I),x)),1e-12)
                    for c in C:self.assertLess(np.linalg.norm(apply64(c,x)),1e-12)
                # Swapping D,E reverses the two nonzero branches (input is
                # antisymmetric), paired with X on the pointer.
                np.testing.assert_allclose(apply64(SWAP,plusminus[0]),-plusminus[1],atol=1e-13)
                np.testing.assert_allclose(apply64(SWAP,plusminus[1]),-plusminus[0],atol=1e-13)

    def test_new_sign_is_not_the_prior_j(self):
        # Strong operator statement on the actual old kernel times DE singlet.
        from verification.zero_relational_orientation_reference_test import Psing
        old=(np.eye(16)+L)@Psing/2
        dep=np.outer(SING.reshape(4),SING.reshape(4).conj())
        source=kron(old,dep)
        self.assertAlmostEqual(np.trace(source).real,2,places=12)
        for p in (PP,PM):
            for sign in (1,-1):
                op=source@p@((I64+sign*J)/2)@p@source
                np.testing.assert_allclose(op,source/4,atol=1e-13)
                joint=np.trace(op).real/2
                self.assertAlmostEqual(joint,.25,places=12)
        # A sequential hypothetical sharp J after the new measurement gives
        # j=± with equal probability in either χ branch. It is not a claim
        # that measuring J preserves the total constraints.
        for c in (C1,C2,C3):
            oldc=kron(c,I,I)
            np.testing.assert_allclose(source@PP@oldc@oldc@PP@source,2*source/3,atol=1e-13)
            np.testing.assert_allclose(source@PM@oldc@oldc@PM@source,2*source/3,atol=1e-13)
            val=np.trace(source@PP@oldc@oldc@PP).real/np.trace(source@PP).real
            self.assertAlmostEqual(val,4/3,places=12)
        # Original orientation zero is redistributed into D,E; only the
        # enlarged total C=0 is guaranteed after the interaction.

    def test_full_physical_work_operators_and_declared_energy(self):
        # R2 W16 T2 F2 D2 E2. Inactive work is left untouched by χ.
        aa=[-kron(Z,X16,X),-kron(Z,Z16,X),kron(I,J16,I)]
        support=kron(I,P16,I)
        b=[-X,-Y,Z]
        af=[kron(a,I,I,I) for a in aa]
        dd=[kron(np.eye(64),I,x,I) for x in pauli]
        ee=[kron(np.eye(64),I,I,x) for x in pauli]
        cf=[kron(a,I,I,I)+kron(support,z,I,I)+d+e for a,z,d,e in zip(aa,b,dd,ee)]
        chi=sum(s*af[i]@dd[j]@ee[k] for i,j,k,s in eps)/(2*math.sqrt(3))
        for c in cf:np.testing.assert_allclose(chi@c-c@chi,0,atol=2e-13)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            number=sum(np.asarray(n[k]) for k in inds)
            energy=kron(I,number,I,I,I,I)
            np.testing.assert_allclose(chi@energy-energy@chi,0,atol=1e-13)
        active=kron(support,I,I,I)
        np.testing.assert_allclose(chi@(np.eye(512)-active),0,atol=1e-13)
        # Polynomial projector and controlled pointer unitary inherit these
        # commutators. No cost for the new spins/control is derived.

if __name__=='__main__':unittest.main()
