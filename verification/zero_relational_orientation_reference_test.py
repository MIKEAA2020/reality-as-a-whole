"""Relational orientation in the all-sector zero-balance circuit.

Adds one explicit two-level reference by an isometry. It is a stipulated
resource and does not establish a physical cosmological charge, preparation,
subjecthood or actuality. Both pre-existing lab sectors and all clock labels
are retained coherently.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import (
    X,Y,Z,I,Jactive,full_state,relative_read,i_r_m_table,reduced_work,density_frobenius_sq
)
from verification.zero_all_sector_sphere_clock_work_test import complement_state
from verification.zero_constitution_hamiltonian_phase_gate_test import rotate_work, X16, Z16, J16, P16
from verification.zero_reciprocal_subject_exchange_test import n
from verification.zero_all_sector_branchwise_balance_test import U8,L8,apply

I8=np.eye(8,dtype=complex)
I16=np.eye(16,dtype=complex)
U1=-np.kron(np.kron(Z,Z),X)
Jw=np.kron(np.kron(I,Jactive),I)
L=np.kron(L8,I)
U0F=np.kron(U8,I)
U1F=np.kron(U1,I)
Qori=np.kron(Jw,I)+np.kron(I8,Z)
C1=U0F-np.kron(I8,X)
C2=U1F-np.kron(I8,Y)
C3=Qori
S=(np.kron(U8,X)+np.kron(U1,Y))/2
Pzero=(I16-np.kron(Jw,Z))/2
Hcas=(C1@C1+C2@C2+C3@C3)/8
Psing=I16-Hcas


def with_reference(v):
    """Isometry |J=+>→|J=+>|F=−>, |J=−>→|J=−>|F=+>."""
    pplus=(I+Jactive)/2
    pminus=(I-Jactive)/2
    out=np.zeros(v.shape+(2,),complex)
    out[...,1]=np.einsum('wu,...rut->...rwt',pplus,v,optimize=True)
    out[...,0]=np.einsum('wu,...rut->...rwt',pminus,v,optimize=True)
    return out


def apply16(op,v):
    assert v.shape[-4:]==(2,2,2,2)
    a=v.reshape(v.shape[:-4]+(16,))
    return np.einsum('xy,...y->...x',op,a,optimize=True).reshape(v.shape)


def original_table(vs):
    # Keep Alice i, R and T. Sum both labs, four reference/clock factors,
    # Bob pointer, work, and the newly added F.
    return sum(np.sum(abs(v)**2,axis=(0,1,2,3,4,5,7,9,11)) for v in vs)


def ref_conditional(v,sign):
    """Project F onto |±X> and remove F; no preparation interpretation."""
    return (v[...,0]+sign*v[...,1])/math.sqrt(2)


class RelationalOrientationReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.states=(full_state(4),complement_state(4))
        cls.clocks=[relative_read(v,4,labels=tuple(range(16))) for v in cls.states]

    def test_reference_algebra_and_relative_observable_are_exact(self):
        A=(U8,U1,Jw)
        B=(-X,-Y,Z)
        C=(C1,C2,C3)
        for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
            np.testing.assert_allclose(A[i]@A[j]-A[j]@A[i],2j*A[k],atol=1e-14)
            np.testing.assert_allclose(B[i]@B[j]-B[j]@B[i],2j*B[k],atol=1e-14)
            np.testing.assert_allclose(C[i]@C[j]-C[j]@C[i],2j*C[k],atol=1e-14)
        np.testing.assert_allclose(S@Qori,Qori@S,atol=1e-14)
        np.testing.assert_allclose(S@S,Pzero,atol=1e-14)
        np.testing.assert_allclose(S@Pzero,S,atol=1e-14)
        np.testing.assert_allclose(Pzero@np.kron(U8,X)@Pzero,S,atol=1e-14)
        self.assertAlmostEqual(np.linalg.norm(S,2),1,places=13)
        # S is a joint record-work-target-reference effect. It is invariant
        # under common U(1) rotations, not a strictly R- or F-local report.

    def test_reference_algebra_extends_to_physical_work_and_respects_charges(self):
        ia=np.eye(64,dtype=complex)
        p=np.kron(np.kron(I,P16),I)
        aa=[-np.kron(np.kron(Z,X16),X),-np.kron(np.kron(Z,Z16),X),
            np.kron(np.kron(I,J16),I)]
        bb=[-X,-Y,Z]
        cc=[np.kron(x,I)+np.kron(p,y) for x,y in zip(aa,bb)]
        for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
            np.testing.assert_allclose(cc[i]@cc[j]-cc[j]@cc[i],2j*cc[k],atol=1e-14)
        pp=np.kron(p,I)
        h=np.eye(128)-pp+sum(c@c for c in cc)/8
        np.testing.assert_allclose(h@h,h,atol=1e-14)
        np.testing.assert_allclose(np.linalg.eigvalsh(h),[0]*4+[1]*124,atol=1e-12)
        numbers=np.asarray(n,complex)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            number=sum(numbers[k] for k in inds)
            charge=np.kron(np.kron(np.kron(I,number),I),I)
            for c in cc:
                np.testing.assert_allclose(c@charge,charge@c,atol=1e-14)
            np.testing.assert_allclose(h@charge,charge@h,atol=1e-14)
        # Inactive states are explicitly penalized. R, T and added F are
        # neutral in the old energy assignment; no physical cost is derived.

    def test_singlet_casimir_and_old_branch_balance_jointly_select_rank_two(self):
        np.testing.assert_allclose(Hcas@Hcas,Hcas,atol=1e-14)
        np.testing.assert_allclose(Hcas.conj().T,Hcas,atol=1e-14)
        self.assertAlmostEqual(np.trace(Psing).real,4,places=13)
        np.testing.assert_allclose(L@Hcas,Hcas@L,atol=1e-14)
        P=(I16+L)@Psing/2
        np.testing.assert_allclose(P@P,P,atol=1e-14)
        self.assertAlmostEqual(np.trace(P).real,2,places=13)
        np.testing.assert_allclose(C3@P,0,atol=1e-14)
        np.testing.assert_allclose(S@P,P,atol=1e-14)
        for C in (C1,C2,C3):np.testing.assert_allclose(C@P,0,atol=1e-14)
        # Three zero balances choose the invariant relative orientation
        # given these chosen representations; none is derived from 0 alone.

    def test_isometry_lifts_actual_whole_and_all_clock_labels_without_discard(self):
        for state,vs in zip(self.states,self.clocks):
            for v in [state]+vs:
                w=with_reference(v)
                self.assertAlmostEqual(np.linalg.norm(w),np.linalg.norm(v),places=13)
                for C in (C1,C2,C3):
                    np.testing.assert_allclose(apply16(C,w),0,atol=2e-14)
                np.testing.assert_allclose(apply16(L,w),w,atol=2e-14)
                np.testing.assert_allclose(apply16(S,w),w,atol=2e-14)
            np.testing.assert_allclose(original_table([with_reference(x) for x in vs]),
                                       i_r_m_table(vs),atol=1e-14)
        # Isometry acts only on W and added F, identically on both physical
        # lab-sector embeddings, so their coherent superposition is retained.

    def test_internal_reference_replaces_old_complementary_balance_with_relational_one(self):
        g2=np.kron(np.kron(I,X),I)+np.kron(np.kron(Z,I),X)
        g3=np.kron(np.kron(I,Z),I)-np.kron(np.kron(I,I),Y)
        for v in self.states:
            w=with_reference(v)
            self.assertAlmostEqual(np.vdot(w,apply16(U0F,w)).real,0,places=12)
            for g in (g2,g3):
                self.assertAlmostEqual(np.linalg.norm(apply16(np.kron(g,I),w))**2,2,places=12)
            for c in (C1,C2,C3):
                self.assertLess(np.linalg.norm(apply16(c,w)),1e-12)
        # This is a changed state and a new reference-relative set of zeros,
        # not preservation of the old U=+ and G2/G3=0 conditions globally.

    def test_relative_phase_is_observable_even_at_exact_zero_orientation_charge(self):
        for v,vs in zip(self.states,self.clocks):
            ref0=with_reference(v)
            for angle in (0,math.pi/3,math.pi):
                w=with_reference(rotate_work(v,angle))
                self.assertLess(np.linalg.norm(apply16(Qori,w)),1e-12)
                np.testing.assert_allclose(apply16(L,w),w,atol=2e-14)
                self.assertAlmostEqual(np.vdot(w,apply16(S,w)).real,math.cos(angle),places=12)
                if angle==math.pi:
                    self.assertAlmostEqual(abs(np.vdot(ref0,w)),0,places=12)
                xs=[with_reference(rotate_work(x,angle)) for x in vs]
                np.testing.assert_allclose(original_table(xs),
                                           original_table([with_reference(x) for x in vs]),atol=1e-13)
        # The joint witness is orientation-charge invariant. These phases
        # are not different absolute coordinate angles; they are relations
        # to F, provided S is an admissible physical observable.

    def test_phase_is_in_correlations_not_either_side_alone(self):
        for v in self.states:
            a=with_reference(v).reshape(-1,2)
            rho_f=a.T@a.conj()
            np.testing.assert_allclose(rho_f,I/2,atol=1e-13)
            for theta in (math.pi/3,math.pi):
                b=with_reference(rotate_work(v,theta)).reshape(-1,2)
                np.testing.assert_allclose(b.T@b.conj(),rho_f,atol=1e-13)
                self.assertLess(density_frobenius_sq(a,b),1e-12)
        # Both the F-only density and the entire rest density are unchanged.
        # The invariant S probes their joint correlation; no local subsystem
        # may be assumed to register it without the appropriate interface.

    def test_conditioning_reference_reading_recovers_old_plus_and_minus_interfaces(self):
        for state,vs in zip(self.states,self.clocks):
            for v in [state]+vs:
                w=with_reference(v)
                plus=ref_conditional(w,1)
                minus=ref_conditional(w,-1)
                self.assertAlmostEqual(np.linalg.norm(plus)**2,np.linalg.norm(v)**2/2,places=13)
                self.assertAlmostEqual(np.linalg.norm(minus)**2,np.linalg.norm(v)**2/2,places=13)
                np.testing.assert_allclose(plus,v/math.sqrt(2),atol=2e-14)
                np.testing.assert_allclose(apply(U8,plus),plus,atol=2e-14)
                np.testing.assert_allclose(apply(U8,minus),-minus,atol=2e-14)
                self.assertAlmostEqual(abs(np.vdot(plus,minus)),0,places=13)
        # This is a joint F readout and classical conditioning, not a
        # privileged report available to the confined R system.

    def test_blank_uncorrelated_reference_cannot_be_zeroed_by_charge_conserving_unitary(self):
        for vs in self.clocks:
            rho=reduced_work(vs)
            np.testing.assert_allclose(rho,I/2,atol=1e-13)
            self.assertAlmostEqual(np.trace(rho@Jactive).real,0,places=13)
        # For any independently prepared F state, J²=ZF²=1 and <J>=0, so
        # <(J+ZF)²>=2. A unitary commuting with Qori conserves this moment;
        # no such unitary on the same closed system can reach Qori=0.
        rho_w=I/2
        for f in (np.array([[1,0],[0,0]],complex),I/2,(I+X)/2,(I+Y)/2):
            rho=np.kron(rho_w,f)
            q=np.kron(Jactive,I)+np.kron(I,Z)
            self.assertAlmostEqual(np.trace(rho@q@q).real,2,places=13)
        # A charge-balanced starting resource, reservoir, or modified
        # account of preparation is needed; the isometry is not claimed free.

    def test_common_rotations_are_gauge_like_on_zero_charge_state(self):
        vals,vec=np.linalg.eigh(Qori)
        for angle in (.4,math.pi):
            rot=(vec*np.exp(-1j*angle*vals/2))@vec.conj().T
            np.testing.assert_allclose(rot@S@rot.conj().T,S,atol=1e-14)
            for state in self.states:
                w=with_reference(state)
                np.testing.assert_allclose(apply16(rot,w),w,atol=2e-14)
        # A relative work rotation does not have this property and changes S.

if __name__=='__main__':
    unittest.main()
