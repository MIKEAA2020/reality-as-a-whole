"""An integrated, retrospective sphere-echo battery bridge candidate.

Uses the existing state and gates.  Checks physical claim/target statistics,
not a human assertion, a public experiment, or actual phenomenal incidence.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base, output, relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_contextual_reference_test import value_history
from verification.zero_internal_reference_subject_valence_candidates_test import b_project, j_project
from verification.zero_dynamic_subject_memory_echo_test import jwrite
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_internal_connection_flag_access_balance_test import ensemble
from verification.zero_clock_finite_reservoir_reuse_test import BITS3, Q as THERMAL
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path


def table(t, q=F(0)):
    out=defaultdict(F)
    for b,z,s,x,f,e,st,zz,r,w in ensemble(t,q):
        out[(b, (-1)**r, s, (-1)**zz)] += w
    return out


def public_table(t, q=F(0), claim_flip=False, target_flip=False):
    # Both conventions are explicit. A target flip is an adversarial change
    # of target but NOT an accompanying physical coordinate re-expression.
    out=defaultdict(F)
    for (b,r,s,j),w in table(t,q).items():
        claim= -r if claim_flip else r
        target= -b if target_flip else b
        out[(claim,target)]+=w
    return dict(out)


def match(tab):
    return sum((w for (c,b),w in tab.items() if c==b),F(0))


class SphereBatteryBridgeCandidateTests(unittest.TestCase):
    def test_physical_target_and_echo_claim_on_existing_clock(self):
        expected=[F(1,2)]*8+[F(3,4)]*2+[F(1)]+[F(3,4)]*2+[F(1,2)]*8
        for q in (F(0),THERMAL):
            for t,p in enumerate(expected):
                tab=public_table(t,q)
                self.assertEqual(sum(tab.values()),1)
                self.assertEqual(match(tab),p)
                self.assertEqual(sum(w for (c,b),w in tab.items() if b==1),F(1,2))
                self.assertEqual(sum(w for (c,b),w in tab.items() if b==-1),F(1,2))
        self.assertEqual(public_table(10),{(1,1):F(1,2),(-1,-1):F(1,2)})

    def test_fixed_reference_decoder_and_target_shift_controls(self):
        for q in (F(0),THERMAL):
            for t in (7,8,10,11,13):
                p=match(public_table(t,q))
                self.assertEqual(match(public_table(t,q,claim_flip=True)),1-p)
                self.assertEqual(match(public_table(t,q,target_flip=True)),1-p)
            self.assertEqual(match(public_table(10,q,claim_flip=True)),0)
            self.assertEqual(match(public_table(10,q,target_flip=True)),0)
        # A passive relabeling changes BOTH representation and target; unlike
        # a decoder-only flip it preserves the match relation.
        tab=public_table(10)
        self.assertEqual(match({(-c,-b):w for (c,b),w in tab.items()}),match(tab))

    def test_independent_target_from_actual_coherent_quantum_state(self):
        # Independently derive the target-and-record Born statistics from the
        # old quantum amplitudes rather than inserting b into the label ledger.
        state=output(active_base())
        for label in range(16):
            v=initial(relative_read(state,4,labels=(label,))[0]);mass=norm2(v)
            a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
            seen={}
            for r,u in ((1,a),(-1,c)):
                for b in (1,-1):
                    seen[(r,b)]=norm2(b_project(u,b))/mass
            for key in product((1,-1),repeat=2):
                self.assertAlmostEqual(seen[key],.5 if key[0]==key[1] else 0,places=12)
            # Project target B before the pulse and then apply it: the
            # comparison does not depend on measuring the target afterwards.
            for b in (1,-1):
                vb=b_project(v,b)
                x,y=jwrite(vb,0*vb);x,y=value_history(x),value_history(y);x,y=jwrite(x,y)
                np.testing.assert_allclose(x,b_project(a,b),atol=1e-13)
                np.testing.assert_allclose(y,b_project(c,b),atol=1e-13)

    def test_ready_state_is_a_necessary_protocol_input_not_a_free_label(self):
        # On every explicit coarse input, initializing R to 1 flips the
        # record's sign: the unchanged decoder now predicts the wrong target.
        for b,x,f,e,z in product((0,1),BITS3,BITS3,((0,),(1,)),(0,1)):
            ready=twenty_tick_path(b,x,f,e,((1,),(0,)),z,r=0)
            dirty=twenty_tick_path(b,x,f,e,((1,),(0,)),z,r=1)
            self.assertEqual(ready[10][2],b)
            self.assertEqual(dirty[10][2],1^b)
            self.assertEqual(ready[20][2],0)
            self.assertEqual(dirty[20][2],1)

    def test_same_candidate_quality_and_physical_measure(self):
        # Both candidate valuations use the SAME proposed M-j-E boundary,
        # at tick 10 with the SAME joint quantum record. No person inferred.
        tab=table(10)
        self.assertEqual(sum(tab.values()),1)
        self.assertEqual(sum(w for (b,r,s,j),w in tab.items() if s*j != s*j*r),F(1,2))
        for selector in (lambda b,r,s,j:s*j,lambda b,r,s,j:s*j*r):
            self.assertEqual(sum((w*selector(*k) for k,w in tab.items()),F(0)),0)
        # Reweighted incidence hypothesis has unchanged support and signed
        # balance, but different disagreement. This is not a Born law.
        alt={k:w*(F(3,2) if k[0]==1 else F(1,2)) for k,w in tab.items()}
        self.assertEqual(sum(alt.values()),1)
        self.assertEqual(sum(w for (b,r,s,j),w in alt.items() if s*j != s*j*r),F(1,4))
        for selector in (lambda b,r,s,j:s*j,lambda b,r,s,j:s*j*r):
            self.assertEqual(sum((w*selector(*k) for k,w in alt.items()),F(0)),0)

if __name__=='__main__':unittest.main()
