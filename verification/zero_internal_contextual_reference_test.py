"""Reuse the old Bob sphere/record redundancy as a symmetry reference.

The reference is a logical qubit, not an extra one. The dressed readout
changes the old j register; recovering the former j requires sphere access.
The extended Z2 identification is stipulated and differs from bare U.
"""
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Y,Z,kron,active_base,output,relative_read
)
from verification.zero_relational_chirality_report_test import initial,apply64,C,LL,SWAP
from verification.zero_relative_gauge_invariant_report_test import V,G
from verification.zero_invariant_all_history_record_clock_test import XL,ZL
from verification.zero_conserving_sphere_handedness_report_test import bob_action,j_sign,table_ij
from verification.zero_spin_reversal_sign_selection_test import physical_old_to_canonical,lift_spin,t
from verification.zero_contextual_sign_symmetry_and_dressed_report_test import (
    B,Bp,Bm,U,chir,valid,ss,spin_id,history_u
)

# Operator order: encoded RWT/F/D/E (64), Bob sphere (2), j record (2).
eye=np.eye(256)
oldU=kron(U,I)
XR=kron(spin_id,B,Z)       # +1 on every old history
ZR=kron(spin_id,I,X)       # toggles the actual j record
Bs=kron(spin_id,B,I)
Zj=kron(spin_id,I,Z)
S=kron(ss,I,I)
P=kron(valid,I,I)
baseC=kron(chir,I,I)
baseCB=kron(chir,B,I)
Gint=oldU@XR
O=(baseC@(eye+ZR)+baseCB@(eye-ZR))/2


def jflip(x):return np.flip(x,axis=7)


def gauge_history(x):return history_u(bob_action(B,j_sign(x)))


def value_history(x):
    bx=bob_action(B,x)
    return apply64(V,(x+bx+jflip(x)-jflip(bx))/2)


class InternalContextualReferenceTests(unittest.TestCase):
    def test_general_unreferenced_obstruction_beyond_previous_ansatz(self):
        # On B=-, U=-S; an exchange-odd operator commuting with B is U-odd
        # on that entire block, even with arbitrary U-neutral ancillas.
        rng=np.random.default_rng(83041)
        m=rng.normal(size=(64,64))+1j*rng.normal(size=(64,64))
        m=(m+m.conj().T)/2
        m=valid@m@valid
        odd=(m-ss@m@ss)/2
        self.assertGreater(np.linalg.norm(odd),1)
        minus_block=kron(odd,Bm,I)
        self.assertGreater(np.linalg.norm(minus_block),1)
        np.testing.assert_allclose(S@minus_block@S,-minus_block,atol=1e-12)
        np.testing.assert_allclose(oldU@minus_block@oldU,-minus_block,atol=1e-12)
        np.testing.assert_allclose((minus_block+oldU@minus_block@oldU)/2,0,atol=1e-12)
        for z in ((I+Z)/2,(I-Z)/2):
            sector=kron(odd,Bm,z)
            np.testing.assert_allclose(Zj@sector-sector@Zj,0,atol=1e-12)
            np.testing.assert_allclose(Gint@sector@Gint,-sector,atol=1e-12)
        # The internal extension also forces S-odd operators which preserve
        # j to vanish on B=-. This random witness accompanies the exact
        # projector proof in the report, not a universal proof by sampling.

    def test_encoded_reference_is_a_real_qubit_and_source_stabilizer(self):
        for x in (XR,ZR):np.testing.assert_allclose(x@x,eye,atol=1e-13)
        np.testing.assert_allclose(XR@ZR+ZR@XR,0,atol=1e-13)
        np.testing.assert_allclose(XR@Bs-Bs@XR,0,atol=1e-13)
        np.testing.assert_allclose(ZR@Bs-Bs@ZR,0,atol=1e-13)
        np.testing.assert_allclose(oldU@XR-XR@oldU,0,atol=1e-13)
        np.testing.assert_allclose(oldU@ZR-ZR@oldU,0,atol=1e-13)
        np.testing.assert_allclose(Gint@Gint,eye,atol=1e-13)
        for name,op in [('B',Bs),('j',Zj),('C',baseC),('S',S)]:
            # Bare U and its internal-reference extension act identically
            # on the old diagonal-record/core observable algebra.
            np.testing.assert_allclose(Gint@op@Gint,oldU@op@oldU,atol=1e-13,err_msg=name)
        self.assertGreater(np.linalg.norm(Gint@ZR@Gint-oldU@ZR@oldU),1)

    def test_reused_reference_makes_sharp_invariant_gate_without_added_R(self):
        np.testing.assert_allclose(O@O,P,atol=1e-13)
        np.testing.assert_allclose(Gint@O@Gint,O,atol=1e-13)
        np.testing.assert_allclose(S@O@S,-O,atol=1e-13)
        _,ub=np.linalg.eigh(B);theta=kron(lift_spin(t),ub@ub.T,I)
        np.testing.assert_allclose(theta@O.conj()@theta.conj().T,-O,atol=1e-13)
        np.testing.assert_allclose(theta@Gint.conj()@theta.conj().T,Gint,atol=1e-13)
        np.testing.assert_allclose(Bs@O-O@Bs,0,atol=1e-13)
        self.assertGreater(np.linalg.norm(Zj@O-O@Zj),1)
        self.assertGreater(np.linalg.norm(oldU@O@oldU-O),1)
        for op in (physical_old_to_canonical(LL),physical_old_to_canonical(G),
                   *[physical_old_to_canonical(c) for c in C],
                   *[physical_old_to_canonical(kron(c,I,I)) for c in (XL,ZL)]):
            x=kron(op,I,I)
            np.testing.assert_allclose(x@O-O@x,0,atol=1e-13)
            np.testing.assert_allclose(x@Gint-Gint@x,0,atol=1e-13)
        neg=(P-O)/2
        np.testing.assert_allclose(neg@neg,neg,atol=1e-13)
        gate=kron(eye-neg,I)+kron(neg,X)
        np.testing.assert_allclose(gate.conj().T@gate,np.eye(512),atol=1e-13)
        np.testing.assert_allclose(gate@kron(Gint,I),kron(Gint,I)@gate,atol=1e-13)
        np.testing.assert_allclose(gate@kron(Bs,I),kron(Bs,I)@gate,atol=1e-13)
        self.assertGreater(np.linalg.norm(gate@kron(Zj,I)-kron(Zj,I)@gate),1)

    def test_all_16_histories_exact_source_sign_and_record_tradeoff(self):
        state=output(active_base())
        expected=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        new=np.column_stack((expected[:,0]+expected[:,1]/2,expected[:,1]/2))
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=np.linalg.norm(x)**2
            np.testing.assert_allclose(bob_action(B,j_sign(x)),x,atol=1e-13)
            np.testing.assert_allclose(gauge_history(x),x,atol=1e-13)
            np.testing.assert_allclose(table_ij(x)/mass,expected,atol=1e-13)
            ax=value_history(x)
            np.testing.assert_allclose(value_history(ax),x,atol=1e-13)
            branches=[(x+ax)/2,(x-ax)/2]
            for branch in branches:
                self.assertAlmostEqual(np.linalg.norm(branch)**2/mass,.5,places=12)
                np.testing.assert_allclose(gauge_history(branch),branch,atol=1e-13)
                np.testing.assert_allclose(apply64(LL,branch),branch,atol=1e-13)
                np.testing.assert_allclose(apply64(G,branch),branch,atol=1e-13)
                for c in C:np.testing.assert_allclose(apply64(c,branch),0,atol=1e-13)
            tab=sum(table_ij(y) for y in branches)/mass
            np.testing.assert_allclose(tab,new,atol=1e-13)
            # B remains a perfect record of pre-readout j, despite the
            # changed physical j register. Its joint i,B table is unchanged.
            old_b=[];new_b=[]
            for sign in (1,-1):
                old_b.append(table_ij((x+sign*bob_action(B,x))/2).sum(axis=1))
                new_b.append(sum(table_ij((y+sign*bob_action(B,y))/2).sum(axis=1) for y in branches))
            np.testing.assert_allclose(np.stack(old_b,axis=1)/mass,expected,atol=1e-13)
            np.testing.assert_allclose(np.stack(new_b,axis=1)/mass,expected,atol=1e-13)
            # Probability that the final physical j disagrees with the old
            # sphere-based j is exactly 1/4 after discarding sign pointer M.
            wrong=0.
            for y in branches:
                mismatch=(y-bob_action(B,j_sign(y)))/2
                wrong+=np.linalg.norm(mismatch)**2
            self.assertAlmostEqual(wrong/mass,.25,places=12)

if __name__=='__main__':unittest.main()
