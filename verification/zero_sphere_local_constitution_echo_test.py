"""Local-state quality candidates and a sphere-reservoir echo.

The two subject boundaries and the phenomenal rules are hypotheses. The
physical pulse and neutral blank are stipulated resources, not a physical
implementation of a cosmic energy or an actual observer.
"""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Z,kron,active_base,output,relative_read,
)
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_contextual_reference_test import (
    B,Bs,Zj,Gint,P,eye,value_history,
)
from verification.zero_internal_reference_subject_valence_candidates_test import (
    b_project,j_project,reduced,born_table,
)
from verification.zero_conserving_sphere_handedness_report_test import bob_action,j_sign
from verification.zero_persistent_sphere_subject_selection_test import Q,norm2
from verification.zero_dynamic_subject_memory_echo_test import jwrite
from verification.zero_clock_finite_reservoir_reuse_test import BITS3, FORWARD, energy, Q as THERMAL
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import (
    advance, distribution, words,
)
from verification.zero_sphere_reuse_experiential_access_test import outputs, guess_score


def normalized_reduced(v,axis):
    return reduced(v,axis)/norm2(v)


def pulse_labels(b,z,r,op):
    # Only the simultaneous Z-label transport, not the full quantum unitary.
    if op=='T':return z,r^z
    if op=='Q':return z^b,r
    raise ValueError(op)


def twenty_tick_path(b,x,f,e,cols,z,r=0):
    """The appended apparatus and commuting j/echo labels on valid support."""
    k=len(e); state=(b,x,(0,)+f,3,e,k); states=[(state,z,r)]
    for op in FORWARD:
        state=advance(state,op,cols);states.append((state,z,r))
    for op in ('T','Q','T','T','Q','T'):
        z,r=pulse_labels(b,z,r,op);states.append((state,z,r))
    for op in reversed(FORWARD):
        state=advance(state,op,cols,reverse=True);states.append((state,z,r))
    return states


class SphereLocalConstitutionEchoTests(unittest.TestCase):
    def test_both_local_parities_are_gauge_valid_and_counterpart_odd(self):
        from verification.zero_internal_contextual_reference_test import S
        for op in (Zj,Bs):
            np.testing.assert_allclose(op@Gint-Gint@op,0,atol=1e-13)
            np.testing.assert_allclose(op@P-P@op,0,atol=1e-13)
            np.testing.assert_allclose(S@op@S,op,atol=1e-13)
        # Pointer sign M is flipped by X_M; multiplying either local sign
        # by Z_M makes the bridge odd under S X_M.
        for op in (Zj,Bs):
            v=kron(op,Z); counter=kron(S,X); gauge=kron(Gint,I)
            np.testing.assert_allclose(counter@v@counter,-v,atol=1e-13)
            np.testing.assert_allclose(gauge@v@gauge,v,atol=1e-13)

    def test_actual_local_states_collide_for_the_opposite_bridges(self):
        # Branches are simultaneous b,z and already-registered M sign;
        # conditioning is a specified operational comparison, not a hidden
        # trajectory in an unmeasured history.
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0])
            for s in (1,-1):
                v=(x+s*value_history(x))/2
                branches={(b,z):j_project(b_project(v,b),z)
                          for b,z in ((1,1),(-1,1),(-1,-1))}
                self.assertTrue(all(norm2(w)>1e-12 for w in branches.values()))
                # j+M sees the same state for B+ vs B- when j=+.
                np.testing.assert_allclose(normalized_reduced(branches[1,1],7),
                                           normalized_reduced(branches[-1,1],7),atol=1e-13)
                # B+M sees the same state for j+ vs j- when B=-.
                np.testing.assert_allclose(normalized_reduced(branches[-1,1],1),
                                           normalized_reduced(branches[-1,-1],1),atol=1e-13)
                self.assertNotEqual(s, -s)
        # Source/reference trace leaves the apparatus in the same state for
        # b=+ and b=-; therefore tensoring that apparatus onto either local
        # boundary does not distinguish the colliding states.
        for cols,q in [(((),()),THERMAL),(((1,),(0,)),F(0)),(((1,1),(0,0)),THERMAL)]:
            self.assertEqual(outputs(cols,q,0),outputs(cols,q,1))
            self.assertEqual(guess_score(cols,q),F(3,4))

    def test_echo_operator_transport_and_gauge(self):
        t=kron((eye+Zj)/2,I)+kron((eye-Zj)/2,X)
        qr=kron(Q,I);e=t@qr@t;valid=kron(P,I)
        np.testing.assert_allclose(e@e,np.eye(512),atol=1e-13)
        for a in (P,Bs,Gint):
            np.testing.assert_allclose(e@kron(a,I),kron(a,I)@e,atol=1e-13)
        # Exact commuting-observable Heisenberg transports on valid support.
        for before,after in ((kron(eye,Z),kron(Bs,Z)),
                             (kron(Zj,I),kron(Bs@Zj,I)),
                             (kron(Zj,Z),kron(Zj,Z))):
            np.testing.assert_allclose(valid@e@before@e@valid,valid@after@valid,atol=1e-13)
        # E commutes with each source/B controlled gate: it commutes with B
        # and acts only on old degrees + its separate neutral echo memory.
        # Q and T do not act on the two added signed-charge registers.

    def test_echo_on_actual_coherent_histories_and_inverse(self):
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]); mass=norm2(x)
            for s,b in product((1,-1),repeat=2):
                v=b_project((x+s*value_history(x))/2,b)
                self.assertAlmostEqual(norm2(v)/mass,.25,places=12)
                a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
                if b==1:
                    np.testing.assert_allclose(a,value_history(v),atol=1e-13)
                    np.testing.assert_allclose(c,0,atol=1e-13)
                    out=a
                else:
                    np.testing.assert_allclose(c,value_history(v),atol=1e-13)
                    np.testing.assert_allclose(a,0,atol=1e-13)
                    out=c
                # j_final = b*j_initial, in operator form, including
                # coherent z components; echo R final = b.
                np.testing.assert_allclose(j_sign(out),b*value_history(j_sign(v)),atol=1e-13)
                np.testing.assert_allclose(bob_action(B,out),b*out,atol=1e-13)
                aa,cc=jwrite(a,c);aa,cc=value_history(aa),value_history(cc);aa,cc=jwrite(aa,cc)
                np.testing.assert_allclose(aa,v,atol=1e-13)
                np.testing.assert_allclose(cc,0,atol=1e-13)

    def test_twenty_tick_ledger_and_composed_permutations(self):
        cols=((1,),(0,)); k=1
        for b,x,f,e,z,r in product((0,1),BITS3,BITS3,words(k),(0,1),(0,1)):
            p=twenty_tick_path(b,x,f,e,cols,z,r)
            self.assertEqual(len(p),21)
            for (bb,y,m,n,c,d),zz,rr in p:
                self.assertEqual(bb,b)
                self.assertEqual(energy(m,n,f),0)
                self.assertEqual(d-k+sum(c)-sum(e),0)
            # At t=10, the echo writes r XOR b, not necessarily a blank.
            self.assertEqual(p[10][1:],(z^b,r^b))
            self.assertEqual(p[13],p[7])
            self.assertEqual(p[20],p[0])
        # Physical old Q/T are separately checked as unitaries; this label
        # enumeration alone is not presented as the full quantum pulse.

    def test_echo_reconstructs_both_initial_physical_parities(self):
        # A fresh echo memory starts +; after TQT it has r=b and j'=b*z.
        # Current sj' and transported pre-echo sj are distinct notions.
        tab=born_table();mismatch=F(0)
        for (i,b,z,s),w in tab.items():
            r=b;jfinal=b*z
            old_hb=s*b;old_hj=s*z
            self.assertEqual(s*r,old_hb)
            self.assertEqual(s*r*jfinal,old_hj)
            self.assertEqual(s*jfinal,s*b*z)
            if old_hb!=old_hj:mismatch+=w
        self.assertEqual(mismatch,F(1,4))
        # Output state includes a real new record r; it is not an F reference.

    def test_returned_clock_is_stationary_and_charge_balanced_by_construction(self):
        # Gate sequence F, TQT, TQT, reversed(F). All F gates have explicit
        # inverses; T and Q are involutions. The full quantum cycle is I,
        # so its controlled cyclic shift D is a unitary with D^20=I and
        # H=20^-1/2 sum_t |t> U_t|input> obeys D|H>=|H>.
        # Check separately that the actual apparatus gate steps do not
        # depend on z or r and cannot supply an implicit off-realm interface.
        self.assertEqual(len(FORWARD),7)
        for b,x,f,e in product((0,1),BITS3,BITS3,words(1)):
            left=twenty_tick_path(b,x,f,e,((1,),(0,)),0)
            right=twenty_tick_path(b,x,f,e,((1,),(0,)),1)
            self.assertTrue(all(a[0]==c[0] for a,c in zip(left,right)))
            self.assertEqual(left[20],left[0]);self.assertEqual(right[20],right[0])
        # This algebraic stationary-history proof does not construct a full
        # tensor amplitude over all 16 old histories and all clock states.

if __name__=='__main__':unittest.main()
