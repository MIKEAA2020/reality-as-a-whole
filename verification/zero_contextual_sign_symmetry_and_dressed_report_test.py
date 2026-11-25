"""History-preserving sign exchange and a conditional relational dressing.

The controlled D/E swap is a joint, stipulated interaction; its symmetry is
not automatically a gauge identification. The added R is neutral for the
modeled orientation but transforms under the newly defined Z2 action.
"""
import math
import unittest
from fractions import Fraction
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Y,Z,J,kron,bob_effects,active_base,output,relative_read
)
from verification.zero_relational_chirality_report_test import initial,apply64,C,LL,SWAP
from verification.zero_relative_gauge_invariant_report_test import V,VP,VM,G
from verification.zero_invariant_all_history_record_clock_test import XL,ZL
from verification.zero_spin_reversal_sign_selection_test import (
    p,vs,swap,t,lift_spin,physical_old_to_canonical
)
from verification.zero_conserving_sphere_handedness_report_test import bob_action,table_ij

SIG=(X,Y,Z)
eff=J.conj().T@bob_effects()[0]@J
B=sum(np.trace(eff@x).real*x for x in SIG)
Bp=(I+B)/2;Bm=(I-B)/2
ss=lift_spin(swap);spin_id=np.eye(64);big=np.eye(128)
U=kron(spin_id,Bp)-kron(ss,Bm)
pp=lift_spin(p);work=physical_old_to_canonical(LL)
valid=pp@(spin_id+work)/2
chir=lift_spin(vs)@valid
C0=kron(chir,I);C1=kron(chir,B);Pv=kron(valid,I)


def history_u(x):
    bx=bob_action(B,x)
    return (x+bx-apply64(SWAP,x-bx))/2


def vectors_dressed(x,sign):
    # R basis 0 uses C, basis 1 uses CB. R starts in |+>.
    a=(x+sign*apply64(V,x))/2
    b=(x+sign*apply64(V,bob_action(B,x)))/2
    return np.stack((a,b),axis=-1)/math.sqrt(2)


def dressed_u(x):
    return np.stack((history_u(x[...,1]),history_u(x[...,0])),axis=-1)


class ContextualSignSymmetryAndDressedReportTests(unittest.TestCase):
    def test_full_source_weight_ledger(self):
        valid=Fraction(72,256);inactive=1-valid
        self.assertEqual((valid/4,valid/4,valid/2,inactive),
                         (Fraction(9,128),Fraction(9,128),Fraction(9,64),Fraction(23,32)))
        self.assertEqual(valid/4+valid/4+valid/2+inactive,1)
        self.assertEqual((valid/2,valid/2,inactive),
                         (Fraction(9,64),Fraction(9,64),Fraction(23,32)))

    def test_explicit_unitary_preserves_old_constraints_and_exchanges_signs(self):
        np.testing.assert_allclose(U,U.conj().T,atol=1e-13)
        np.testing.assert_allclose(U@U,big,atol=1e-13)
        h=math.pi/2*(big-U)
        val,evec=np.linalg.eigh(h)
        np.testing.assert_allclose((evec*np.exp(-1j*val))@evec.conj().T,U,atol=1e-12)
        np.testing.assert_allclose(U@C0@U,C1,atol=1e-13)
        np.testing.assert_allclose(U@C1@U,C0,atol=1e-13)
        for op in (ss,physical_old_to_canonical(G),work,
                   *[physical_old_to_canonical(kron(c,I,I)) for c in (XL,ZL)],
                   *[physical_old_to_canonical(c) for c in C]):
            op=kron(op,I)
            np.testing.assert_allclose(U@op-op@U,0,atol=1e-13)
        np.testing.assert_allclose(U@kron(spin_id,B)-kron(spin_id,B)@U,0,atol=1e-13)
        # Reversal is a specified mathematical antiunitary, not established
        # as physical time reversal of the apparatus.
        _,u=np.linalg.eigh(B);tb=u@u.T;theta=kron(lift_spin(t),tb)
        np.testing.assert_allclose(theta@U.conj()@theta.conj().T,U,atol=1e-13)
        # U is not the identity on the entire physical sector.
        self.assertGreater(np.linalg.norm((U-big)@Pv),1)
        # The D/E exchange changes the local orientation even though it
        # preserves its total. This is a joint, not a local-neutral, gate.
        from verification.zero_spin_reversal_sign_selection_test import a,d
        local=lift_spin(a[0]+d[0])
        self.assertGreater(np.linalg.norm(U@kron(local,I)-kron(local,I)@U),1)

    def test_no_sharp_invariant_sign_in_old_restricted_class(self):
        # Previous theorem gives candidates C(a I+b B). U exchanges the two
        # coefficients. The only fixed operators have a=b, and square to
        # 2a² P(I+B), which vanishes on B=-1 rather than being identity.
        for a,b in ((1,0),(0,1),(.3,-.7),(.4,.4)):
            o=a*C0+b*C1
            np.testing.assert_allclose(U@o@U,b*C0+a*C1,atol=1e-13)
            np.testing.assert_allclose(o@o,(a*a+b*b)*Pv+2*a*b*kron(valid,B),atol=1e-13)
        ternary=(C0+C1)/2
        np.testing.assert_allclose(U@ternary@U,ternary,atol=1e-13)
        np.testing.assert_allclose(ternary@ternary,kron(valid,Bp),atol=1e-13)
        self.assertGreater(np.linalg.norm(ternary@ternary-Pv),1)

    def test_actual_histories_and_sign_gate_branches_are_related(self):
        state=output(active_base())
        expected=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0])
            mass=np.linalg.norm(x)**2
            np.testing.assert_allclose(history_u(x),x,atol=1e-13)
            for sign,q in ((1,VP),(-1,VM)):
                old=apply64(q,x)
                new=(x+sign*apply64(V,bob_action(B,x)))/2
                np.testing.assert_allclose(history_u(old),new,atol=1e-13)
                np.testing.assert_allclose(table_ij(new)/mass,expected/2,atol=1e-13)
                for c in C:np.testing.assert_allclose(apply64(c,new),0,atol=1e-13)
            # With a fixed physical sign pointer the two coherent output
            # states differ, even though their pointer/i/j tables agree.
            oldp=apply64(VP,x);oldm=apply64(VM,x)
            newp=(x+apply64(V,bob_action(B,x)))/2
            newm=(x-apply64(V,bob_action(B,x)))/2
            overlap=(np.vdot(oldp,newp)+np.vdot(oldm,newm))/mass
            self.assertAlmostEqual(overlap.real,.5,places=12)
            self.assertAlmostEqual(overlap.imag,0,places=12)
            self.assertAlmostEqual(abs(overlap)**2,.25,places=12)
            # The invariant ternary sign has support exactly at B=+1:
            # ± each have one quarter of mass, zero has one half.
            plus=apply64(VP,(x+bob_action(B,x))/2)
            minus=apply64(VM,(x+bob_action(B,x))/2)
            zero=(x-bob_action(B,x))/2
            for v,prob in ((plus,.25),(minus,.25),(zero,.5)):
                self.assertAlmostEqual(np.linalg.norm(v)**2/mass,prob,places=12)

    def test_reference_dressed_sign_is_sharp_and_invariant(self):
        p0=(I+Z)/2;p1=(I-Z)/2
        dressed=kron(C0,p0)+kron(C1,p1)
        gauge=kron(U,X);pv=kron(Pv,I)
        np.testing.assert_allclose(gauge@gauge,np.eye(256),atol=1e-13)
        np.testing.assert_allclose(gauge@dressed@gauge,dressed,atol=1e-13)
        np.testing.assert_allclose(dressed@dressed,pv,atol=1e-13)
        for op in (physical_old_to_canonical(LL),
                   *[physical_old_to_canonical(c) for c in C],
                   *[physical_old_to_canonical(kron(c,I,I)) for c in (XL,ZL)]):
            op=kron(op,I,I)
            np.testing.assert_allclose(op@dressed-dressed@op,0,atol=1e-13)
            np.testing.assert_allclose(op@gauge-gauge@op,0,atol=1e-13)
        # Complete pointer gate, zero sector flagged separately. Since its
        # projector is a polynomial in pv and dressed, it commutes with gauge.
        pm=(pv-dressed)/2
        np.testing.assert_allclose(pm@pm,pm,atol=1e-13)
        read=kron(np.eye(256)-pm,I)+kron(pm,X)
        np.testing.assert_allclose(read.conj().T@read,np.eye(512),atol=1e-13)
        np.testing.assert_allclose(read@kron(gauge,I),kron(gauge,I)@read,atol=1e-13)
        # The bare C pointer would not commute with the old U gauge action.
        self.assertGreater(np.linalg.norm(U@C0-C0@U),1)

    def test_dressed_branch_actual_16_clock_histories_with_symmetric_reference(self):
        state=output(active_base())
        expected=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0])
            mass=np.linalg.norm(x)**2
            source=np.stack((x,x),axis=-1)/math.sqrt(2)
            np.testing.assert_allclose(dressed_u(source),source,atol=1e-13)
            for sign in (1,-1):
                branch=vectors_dressed(x,sign)
                np.testing.assert_allclose(dressed_u(branch),branch,atol=1e-13)
                self.assertAlmostEqual(np.linalg.norm(branch)**2/mass,.5,places=12)
                np.testing.assert_allclose(table_ij(branch).sum(axis=-1)/mass,expected/2,atol=1e-13)
                for k in (0,1):
                    for c in C:np.testing.assert_allclose(apply64(c,branch[...,k]),0,atol=1e-13)
                    np.testing.assert_allclose(apply64(LL,branch[...,k]),branch[...,k],atol=1e-13)
                    np.testing.assert_allclose(apply64(G,branch[...,k]),branch[...,k],atol=1e-13)
        # R is stipulated; a symmetric |+> preparation avoids assuming a
        # definite R=0/1 calibration, but does not derive a subject or valence.

if __name__=='__main__':unittest.main()
