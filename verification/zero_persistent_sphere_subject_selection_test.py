"""Carrier-sector persistence and conditional sign selection on one history.

Subject incidence and experience are explicit hypotheses, not outputs of the
unitary. The added operation is a physical intervention, not a gauge map.
"""
from itertools import product
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Z,kron,active_base,output,relative_read
)
from verification.zero_relational_chirality_report_test import initial,apply64,C,LL,SWAP
from verification.zero_relative_gauge_invariant_report_test import G
from verification.zero_invariant_all_history_record_clock_test import XL,ZL
from verification.zero_spin_reversal_sign_selection_test import physical_old_to_canonical
from verification.zero_internal_contextual_reference_test import (
    B,value_history,gauge_history,Gint,Bs,Zj,S,P,O,eye
)
from verification.zero_conserving_sphere_handedness_report_test import bob_action,j_sign
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project


# Q acts after the sign measurement with M left untouched. The same O was
# the sign observable in the original gate; Q extends it unitarily outside P.
Q=eye-P+O
N=(P-O)/2
W=kron(eye-N,I)+kron(N,X)
Pext=kron(P,I)
Qext=kron(Q,I)
Vb=kron(Bs,Z)
Vj=kron(Zj,Z)


def norm2(x):return np.vdot(x,x).real


def known_b_s_reduced(v,s):
    # For a state conditioned on pointer outcome s, take the B reduced
    # density matrix and attach the corresponding one-dimensional M flag.
    a=np.moveaxis(v,1,0).reshape(2,-1)
    flag=np.diag([int(s==1),int(s==-1)])
    return kron(a@a.conj().T,flag)


class PersistentSphereSubjectSelectionTests(unittest.TestCase):
    def test_real_intervention_and_transported_carrier_projectors(self):
        np.testing.assert_allclose(Q.conj().T@Q,eye,atol=1e-13)
        np.testing.assert_allclose(W.conj().T@W,np.eye(512),atol=1e-13)
        for a in (P,Gint,Bs):
            np.testing.assert_allclose(Q@a-a@Q,0,atol=1e-13)
            np.testing.assert_allclose(W@kron(a,I)-kron(a,I)@W,0,atol=1e-13)
        for old in (LL,G,*C,kron(XL,I,I),kron(ZL,I,I)):
            a=kron(physical_old_to_canonical(old),I,I)
            np.testing.assert_allclose(Q@a-a@Q,0,atol=1e-13)
            np.testing.assert_allclose(W@kron(a,I)-kron(a,I)@W,0,atol=1e-13)
        for b in (-1,1):
            sector=P@(eye+b*Bs)/2
            np.testing.assert_allclose(sector@sector,sector,atol=1e-13)
            self.assertGreater(np.trace(sector).real,0)
            for u in (Q,):np.testing.assert_allclose(u@sector@u.conj().T,sector,atol=1e-13)
            sec=kron(sector,I)
            np.testing.assert_allclose(W@sec@W.conj().T,sec,atol=1e-13)
        # On the active sector Q is exchange odd, so its channel, unlike
        # its state-vector phase, is covariant under the counterpart map.
        np.testing.assert_allclose(S@O@S,-O,atol=1e-13)
        np.testing.assert_allclose(Qext@Vb@Qext.conj().T,Vb,atol=1e-13)
        self.assertGreater(np.linalg.norm(Pext@(Qext@Vj@Qext.conj().T-Vj)),1)

    def test_added_first_record_is_a_compatible_qnd_measurement(self):
        # R is a fresh neutral pointer, not assumed available to an observer.
        n=(eye-Zj)/2
        np.testing.assert_allclose(n@n,n,atol=1e-13)
        for a in (P,Gint,Bs,Zj):
            np.testing.assert_allclose(n@a-a@n,0,atol=1e-13)
        for old in (LL,G,*C,kron(XL,I,I),kron(ZL,I,I)):
            a=kron(physical_old_to_canonical(old),I,I)
            np.testing.assert_allclose(n@a-a@n,0,atol=1e-13)
        np.testing.assert_allclose((eye-n)@(eye-n)+n@n,eye,atol=1e-13)
        np.testing.assert_allclose(n@(eye-n),0,atol=1e-13)
        # But writing z disturbs O coherence: not an unmodified trajectory.
        self.assertGreater(np.linalg.norm(n@O-O@n),1)

    def test_original_16_histories_projected_branch_transport(self):
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=norm2(x)
            flipped=0.;total=0.
            for s,b,z in product((1,-1),repeat=3):
                branch=(x+s*value_history(x))/2
                # Before an intervening j measurement the s branch is an
                # O eigenstate: Q alone only contributes the phase s.
                np.testing.assert_allclose(value_history(branch),s*branch,atol=1e-13)
                # This is a sequential experiment: a QND read/dephasing of
                # j has occurred before Q. It is not a hidden trajectory.
                before=j_project(b_project(branch,b),z)
                weight=norm2(before)/mass
                if weight<1e-15:continue
                # Every retained component is already in the valid sector.
                after=value_history(before)
                np.testing.assert_allclose(bob_action(B,after),b*after,atol=1e-13)
                np.testing.assert_allclose(j_sign(after),(z if b==1 else -z)*after,atol=1e-13)
                np.testing.assert_allclose(gauge_history(after),after,atol=1e-13)
                np.testing.assert_allclose(apply64(LL,after),after,atol=1e-13)
                np.testing.assert_allclose(apply64(G,after),after,atol=1e-13)
                for c in C:np.testing.assert_allclose(apply64(c,after),0,atol=1e-13)
                # The full local B+M state, conditional on this definite b,s,
                # is identical; no such claim for a coherent b superposition.
                np.testing.assert_allclose(known_b_s_reduced(before,s),known_b_s_reduced(after,s),atol=1e-13)
                total+=weight
                if b==-1:flipped+=weight
            self.assertAlmostEqual(total,1,places=12)
            self.assertAlmostEqual(flipped,.5,places=12)

    def test_exact_selection_theorem_and_off_support_freedom(self):
        # Functions f(b,z) take ±1. Sign quality is s*f(b,z).
        # Fix matching to b on both populated input labels and require
        # invariance under Q, which maps z -> b*z for fixed b.
        labels=list(product((1,-1),repeat=2));fits=[];initial_only=[]
        for bits in product((1,-1),repeat=4):
            f=dict(zip(labels,bits))
            if any(f[b,b]!=b for b in (1,-1)):continue
            initial_only.append(f)
            if any(f[b,z]!=f[b,b*z] for b,z in labels):continue
            fits.append(f)
        self.assertEqual(len(initial_only),4)
        self.assertEqual(len(fits),2)
        for f in fits:
            for b,z in ((1,1),(-1,1),(-1,-1)):
                self.assertEqual(f[b,z],b)
        self.assertEqual({f[1,-1] for f in fits},{1,-1})
        # Actual sign-gate output and Q transport never occupy (+,-).
        self.assertTrue(all(f[-1,1]==-1 for f in fits))

    def test_quality_parity_operator_witnesses_are_not_the_same_law(self):
        # On B=-, Q toggles j; on B=+ it leaves j fixed.
        # So it transports Vj to B*Vj, and preserves Vb.
        expected=kron(Bs@Zj,Z)
        np.testing.assert_allclose(Pext@Qext@Vj@Qext@Pext,Pext@expected@Pext,atol=1e-13)
        np.testing.assert_allclose(Pext@Qext@Vb@Qext@Pext,Pext@Vb@Pext,atol=1e-13)
        # Both are legitimate gauge-compatible observables; persistence of
        # b is therefore insufficient to impose one phenomenological law.
        gg=kron(Gint,I)
        for v in (Vj,Vb):np.testing.assert_allclose(gg@v@gg,v,atol=1e-13)

    def test_memory_extended_rival_survives_persistence_and_Q_invariance(self):
        # The fresh R pointer writes r=z at the intermediate QND readout.
        # Alternative quality is s*b*r; R is unchanged by Q. It agrees with
        # s*b initially when R is ready in r=+1. It is counterpart odd and
        # gauge invariant since R is neutral. Q preserves both s*b and r.
        from verification.zero_internal_reference_subject_valence_candidates_test import born_table
        tab=born_table()
        self.assertEqual(sum(w for (i,b,z,s),w in tab.items() if z==-1).numerator,1)
        self.assertEqual(sum(w for (i,b,z,s),w in tab.items() if z==-1).denominator,4)
        for b0 in (1,-1):
            self.assertEqual(sum(w*s*b*z for (i,b,z,s),w in tab.items() if b==b0),0)
        np.testing.assert_allclose(Qext@Vb@Qext,Vb,atol=1e-13)
        # R's neutral Z commutes with the disjoint Q and gauge factors.
        # Thus no enlarged 1024x1024 matrix is needed to prove commutation.

    def test_per_carrier_mirror_balance_is_an_incidence_assumption(self):
        # Within either b sector, the actual Born table pairs s at each z.
        # If this is also the actual subject incidence measure, both signed
        # candidates sum to zero separately per b; no such bridge is derived.
        from verification.zero_internal_reference_subject_valence_candidates_test import born_table
        tab=born_table()
        for b0 in (1,-1):
            p=sum(w for (i,b,z,s),w in tab.items() if b==b0)
            self.assertEqual(p.numerator,1);self.assertEqual(p.denominator,2)
            for f in (lambda b,z:b,lambda b,z:z):
                self.assertEqual(sum(w*s*f(b,z) for (i,b,z,s),w in tab.items() if b==b0),0)
                for i,b,z,s in tab:
                    if b==b0:self.assertEqual(tab[i,b,z,s],tab[i,b,z,-s])

if __name__=='__main__':unittest.main()
