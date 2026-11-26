"""Typed content, relational clock, encoding and report controls."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_stationary_battery_bridge import (
    STATES,TICKS,advance,stationary_weights,expectation,
)
from verification.zero_typed_echo_process import (
    EFFECT,value,records,success,minimal_access,EchoContentProcess,joint_independent,
    record_components,joint_quality_slices,record_k_slices,uncompute_k_slices,
)
from verification.zero_echo_causal_subject_criterion import NAMES,ENC_NAMES,states,run,encode
from verification.zero_echo_causal_subject_criterion_test import index,permutation
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import mass,difference_mass
from verification.zero_coherent_signed_counterpart import exchange
from verification.zero_stationary_subject_incidence import stationary_flip
from verification.zero_stationary_battery_bridge import relational_effect
from verification.zero_dressed_history_pair import encode_pair
from verification.zero_dressed_sphere_rotations import build_frames,transport,old_exchange
from verification.zero_quantum_angular_echo import embed
from verification.zero_joint_quality_incidence_root import quality
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_echo_subject_persistence import copy_initial_j,evolve_record
from verification.zero_conserving_sphere_handedness_report_test import j_sign
from verification.zero_internal_reference_subject_valence_candidates_test import j_project


def subset(*x):return frozenset(x)


class TypedEchoProcessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_transported_content_is_stationary_on_entire_reduced_clock(self):
        for t,x in product(range(TICKS),STATES):
            self.assertEqual(value(t,x),value((t+1)%TICKS,advance(t,x)))
            b,j,r,s=x
            if t in (7,10,13):self.assertEqual(value(t,x),s*j*r)
            if t in (8,9,11,12):self.assertEqual(value(t,x),s*r)
            self.assertEqual(value(t,(b,j,r,-s)),-value(t,x))
        self.assertEqual(expectation(stationary_weights(),EFFECT),F(1,2))
        # The global relational effect is stationary; bare fixed-tick
        # projections are not the same operation or a fundamental clock.

    def test_active_type_operation_maps_content_to_another_candidate(self):
        other=relational_effect(10,lambda x:x[3]*x[1]==1)
        for t,x in product(range(TICKS),STATES):
            self.assertEqual(EFFECT[t][stationary_flip(t,x)],other[t][x])
        weights=stationary_weights()
        disagreement=sum((weights[10][x]*TICKS for x in STATES if EFFECT[10][x]!=other[10][x]),F(0))
        self.assertEqual(disagreement,F(1,2))
        # This is the reduced active type flip, not a gauge identity of the
        # two values. It maps the candidate K to the distinct transported J
        # candidate and preserves their differing physical signs.

    def test_access_changes_in_time_while_saved_logical_content_persists(self):
        expected={
          7:{subset('M','J'),subset('M','L')},
          8:{subset('M','J'),subset('M','L'),subset('M','R')},
          9:{subset('M','L'),subset('M','R'),subset('M','B','J')},
          10:{subset('M','L'),subset('M','B','J'),subset('M','J','R')},
          11:{subset('M','L'),subset('M','R'),subset('M','B','J')},
          12:{subset('M','J'),subset('M','L'),subset('M','R')},
          13:{subset('M','J'),subset('M','L')},
        }
        for t in range(7,14):
            self.assertEqual(minimal_access(t),expected[t])
            self.assertEqual(success(t,('B','J','R','L')),F(1,2))
            self.assertEqual(success(t,('M','L')),1)
            for row,p,k in records(t):
                self.assertEqual(row['M']*row['L'],k)
        # Access is a family of allowed sign algebras, not proof of an
        # actually performed observation or of a shared experience.

    def test_typed_candidate_and_relative_clock_window(self):
        spec=EchoContentProcess()
        self.assertTrue(spec.validate())
        self.assertFalse(EchoContentProcess(access=('J',)).validate())
        self.assertEqual(spec.physical_window_weights(),(F(7,40),F(7,40)))
        with self.assertRaises(ValueError):EchoContentProcess(access=('J',)).physical_window_weights()
        # A selected clock interval is not itself stationary. Twirling it over
        # cyclic shifts yields 7/20 I, losing the absolute tick selection.
        indicator=[int(t in spec.interval) for t in range(TICKS)]
        self.assertNotEqual(indicator,indicator[1:]+indicator[:1])
        self.assertEqual([sum(F(indicator[(t-k)%TICKS],TICKS) for k in range(TICKS))
                          for t in range(TICKS)],[F(7,20)]*TICKS)
        # Born weights over clock alternatives do not count actual subjects.

    def test_ownership_is_not_fixed_by_a_maintained_logical_algebra(self):
        # Same exact process can be provisionally assigned one persistent
        # subject across time or distinct subjects at distinct ticks.
        persistent=lambda t:0
        momentary=lambda t:t
        for t,u in product(range(7,14),repeat=2):
            self.assertTrue(persistent(t)==persistent(u))
            self.assertEqual(momentary(t)==momentary(u),t==u)
            self.assertEqual(success(t,('M','L')),success(u,('M','L')))
        # The owner rule is an additional interpretation, not a POVM effect.

    def test_original_complex_history_carries_the_content_at_every_tick(self):
        operations=('T','Q','T','T','Q','T')
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,ticks=quantum_echo_checkpoints(x,s,4)
            saved=copy_initial_j(ticks[0])
            for t in range(7,14):
                for z,rows in saved.items():
                    for r,part in zip((1,-1),rows):
                        for vec in part:
                            action=s*r*(j_sign(vec) if t in (7,10,13) else vec)
                            self.assertLess(norm2(action-s*z*vec)/total,1e-23)
                if t<13:saved=evolve_record(saved,(operations[t-7],))
        # L has actually been coupled in this model. Discarding it or erasing
        # it changes the accessibility claim; it is not an external observer.

    def test_full_logical_encoding_transports_every_checkpoint(self):
        old=NAMES+('M',);new=ENC_NAMES+('M',)
        v=np.zeros((128,64),complex)
        for row in states(old):
            encoded=encode({k:row[k] for k in NAMES})|{'M':row['M']}
            v[index(new,encoded),index(old,row)]=1
        np.testing.assert_allclose(v.conj().T@v,np.eye(64),atol=1e-14)
        # The copy is already present. Save J, T, Q (two physical gates), T.
        stages=((('J','L'),), (('J','R'),), (('B','J'),), (('J','R'),))
        stages2=((('J2','L'),), (('J1','R'),), (('B','J1'),('B','J2')), (('J1','R'),))
        u=np.eye(64,dtype=complex);up=np.eye(128,dtype=complex)
        for k,(a,b) in enumerate(zip(stages,stages2)):
            u=permutation(old,a)@u;up=permutation(new,b)@up
            np.testing.assert_allclose(up@v,v@u,atol=1e-14)
            fields=('M','R') if k in (1,2) else ('M','J','R')
            encoded_fields=tuple('J1' if name=='J' else name for name in fields)
            d=np.diag([(-1)**sum(row[f] for f in fields) for row in states(old)])
            dp=np.diag([(-1)**sum(row[f] for f in encoded_fields) for row in states(new)])
            np.testing.assert_allclose(dp@v,v@d,atol=1e-14)
        # Intermediates inside the two physical Q subgates are not claimed
        # to preserve the code: only the grouped logical checkpoints do.

    def test_original_quantum_k_report_is_coherent_and_reversible(self):
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            components=record_components(x);total=norm2(x)
            self.assertAlmostEqual(sum(mass(p) for p in components.values())/total,1,places=12)
            record=record_k_slices(components)
            p={k:sum(mass(rows) for (s,z,c),rows in record.items() if c==k)/total for k in (1,-1)}
            self.assertAlmostEqual(p[1],.5,places=12);self.assertAlmostEqual(p[-1],.5,places=12)
            # The reduced pre-report M/L/old state fidelity after ignoring C
            # is sum of squared K-sector weights, not a free readout.
            self.assertAlmostEqual(p[1]**2+p[-1]**2,.5,places=12)
            undone=uncompute_k_slices(record)
            for (s,z,c),rows in undone.items():
                self.assertEqual(c,1)
                self.assertLess(difference_mass(rows,components[s,z])/total,1e-23)
            for (s,z,c),rows in record.items():
                mapped=exchange(rows,10)
                target=record[-s,z,-c]
                target_neg=tuple([-v for v in part] for part in target)
                self.assertLess(difference_mass(mapped,target_neg)/total,1e-23)
        # The report flip C->-C and old clock phase are both required by
        # the sign counterpart; physical symmetry != experiential measure.

    def test_typed_k_is_the_existing_constrained_pair_value(self):
        for label in (0,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            components=record_components(x);total=norm2(x)
            for (s,z),rows in components.items():
                for i in range(4):
                    encoded=encode_pair((rows[0][i],rows[1][i]),i,s)
                    for (a,b,z1,z2),part in encoded.items():
                        if sum(norm2(v) for v in part)/total<1e-24:continue
                        self.assertEqual((a,b),(i,i))
                        self.assertEqual((z1,z2),(s*z,-s*z))
        # The encoded pair remains an isometry: two signs are not by
        # themselves two actual experiencers.

    def test_two_qualities_jointly_report_on_the_same_actual_carrier(self):
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            total=norm2(x);components=record_components(x);parts=joint_quality_slices(components)
            cells={(a,b):0. for a,b in product((1,-1),repeat=2)}
            for (s,z,b,n,k),rows in parts.items():
                # Projecting by the actually controlled M*J report gives
                # the same vectors as grouping by the formal B slice.
                direct=tuple([j_project(v,s*n) for v in part] for part in components[s,z])
                self.assertLess(difference_mass(rows,direct)/total,1e-23)
                self.assertEqual(k,s*z)
                cells[n,k]+=mass(rows)/total
            for p in cells.values():self.assertAlmostEqual(p,.25,places=12)
            # Two separate physical parity report bits have four orthogonal
            # outcomes. Tracing them dephases all four joint sectors.
            self.assertAlmostEqual(sum(p*p for p in cells.values()),.25,places=12)
            for k in (1,-1):
                self.assertAlmostEqual(sum(cells[n,k] for n in (1,-1)),.5,places=12)
            # Sharing M/L and encoding opposite signs does not prove the
            # two structural coordinates are a unified felt experience.

    def test_independent_controls_on_the_actual_fixed_z_subspace(self):
        shape,frames,_=build_frames()
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            u,v,rows=embed(x,s,4);_,_,other=embed(x,-s,4);total=norm2(v)
            for i,j in ((1,2),(2,1)):
                source=(rows[0][i],rows[1][i])
                moved=transport(source,frames,shape,float(u[i]),float(u[j]),s)
                target=(rows[0][j],rows[1][j])
                self.assertLess(sum(norm2(a-b) for a,b in zip(moved,target))/total,1e-22)
                n,k=quality(i,s);n2,k2=quality(j,s)
                self.assertEqual((n2,k2),(-n,k))
                opposite=old_exchange(moved)
                target_other=(other[0][j],other[1][j])
                self.assertLess(sum(norm2(a-b) for a,b in zip(opposite,target_other))/total,1e-22)
                n3,k3=quality(j,-s)
                self.assertEqual((n3,k3),(n,-k))
        # Valid only on this explicitly z=+ two-bin sector and at the anchor.
        # The state-adapted transfer and sign flip are not proven local,
        # gauge-sector-preserving or freely available in the full history.

    def test_independent_interacting_sign_is_not_a_duplicate_record(self):
        z=np.diag([1.,-1.]);i=np.eye(2)
        k=np.kron(z,i);x=np.kron(i,z)
        span=np.stack([np.eye(4).reshape(-1),k.reshape(-1),x.reshape(-1),(k@x).reshape(-1)],axis=1)
        self.assertEqual(np.linalg.matrix_rank(span),4)
        self.assertEqual(np.linalg.matrix_rank(span[:,:2]),2)
        # |+>_K |+>_X |0>_Y, followed by X-controlled CNOT to Y.
        state=np.zeros(8,complex)
        for a,b in product(range(2),repeat=2):state[4*a+2*b+b]=.5
        self.assertAlmostEqual(np.vdot(state,state).real,1.)
        probabilities={(1-2*a,1-2*b):sum(abs(state[4*a+2*b+c])**2 for c in range(2))
                       for a,b in product(range(2),repeat=2)}
        self.assertEqual(probabilities,{k:float(v) for k,v in joint_independent().items()})
        # X->Y is a genuine additional interaction and independent content;
        # one composite vs two subjects are still additional rules.

if __name__=='__main__':unittest.main()
