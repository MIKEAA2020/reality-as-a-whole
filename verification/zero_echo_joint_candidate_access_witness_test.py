"""Access, sampling and witness controls for the joint echo candidate."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_echo_joint_candidate_access_witness import (
    fields_at,record,target,best_guess,minimal_supports,quality_frequency,
    access_failure_bound,ownership_witness)
from verification.zero_echo_joint_identity_balance import EVENTS,physical_ledger,candidate_slot
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints,dot_rows
from verification.zero_echo_subject_persistence import copy_initial_j,evolve_record
from verification.zero_quantum_angular_echo import mass


def trace_out_first(rho,d1,d2):
    return np.trace(rho.reshape(d1,d2,d1,d2),axis1=0,axis2=2)


def trace_out_second(rho,d1,d2):
    return np.trace(rho.reshape(d1,d2,d1,d2),axis1=1,axis2=3)


def distance(rho,sigma):
    return float(np.sum(abs(np.linalg.eigvalsh(rho-sigma)))/2)


class JointCandidateAccessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_minimal_content_and_ledger_access_on_each_checkpoint(self):
        expected=[{frozenset(x) for x in (('M','G','J'),('M','G','L'))},
                  {frozenset(x) for x in (('M','G','J'),('M','G','R'),('M','G','L'))},
                  {frozenset(x) for x in (('M','G','J'),('M','G','R'),('M','G','L'))},
                  {frozenset(x) for x in (('M','G','J'),('M','G','L'))}]
        for t in range(4):
            for name in ('event','content','ledger'):
                actual={frozenset(x) for x in minimal_supports(t,name)}
                self.assertEqual(actual,expected[t])
            self.assertEqual(best_guess(tuple(f for f in fields_at(t) if f!='M'),t,'pointer'),F(1,2))
            self.assertEqual(best_guess(tuple(f for f in fields_at(t) if f!='M'),t,'event'),F(1,2))
            self.assertEqual(best_guess(tuple(f for f in fields_at(t) if f!='G'),t,'event'),F(3,4))
            self.assertEqual(best_guess(('M','G'),t,'event'),F(3,4))
        # These are sign/magnitude algebras on the prepared support; access,
        # preparation and off-support behavior are not established.

    def test_anchor_extra_report_does_not_supply_pointer_or_full_ledger(self):
        t=3
        for i,s in EVENTS:
            data=record(i,s,t)
            self.assertEqual(data['H'],data['B'])
            self.assertEqual(data['L']*data['J'],data['B'])
        self.assertEqual(best_guess(('J','R','L','B','H','G'),t,'pointer'),F(1,2))
        self.assertEqual(best_guess(('M','G','J'),t,'ledger'),1)
        self.assertEqual(best_guess(('M','G','L'),t,'ledger'),1)
        # H is an extra physical report, not an independently calibrated
        # identity witness and not available before its stipulated write.
        with self.assertRaises(ValueError):best_guess(('H',),0,'pointer')

    def test_matched_access_error_union_bound(self):
        self.assertAlmostEqual(access_failure_bound(.04,(.01,.02,.03)),.1)
        self.assertEqual(access_failure_bound(.4,(.3,.3,.3)),1.)
        with self.assertRaises(ValueError):access_failure_bound(.1,(.2,-.1))
        # Disjoint off-support and readout error events saturate the sum;
        # the formula makes no independence assumption.
        disjoint=[.04,.01,.02,.03]
        self.assertAlmostEqual(sum(disjoint),access_failure_bound(disjoint[0],disjoint[1:]))

    def test_sampling_changes_conditional_quality_not_the_proposed_owner(self):
        uniform=(F(1,4),)*4
        skew=(F(1,10),F(2,10),F(3,10),F(4,10))
        self.assertEqual(quality_frequency(0,1,uniform),F(1,2))
        self.assertEqual(quality_frequency(0,1,skew),F(7,10))
        for i,s in EVENTS:
            for pi in (uniform,skew):
                rows=[candidate_slot(i,s,t,pi) for t in range(4)]
                self.assertEqual(len({r['owner'] for r in rows}),1)
                self.assertEqual(sum(r['weight'] for r in rows),F(1,8))
        # π is a chosen sampling law, not a derived ontology of experiences.

    def test_actual_two_bin_recorded_vectors_admit_phase_control(self):
        # At tick 10, bins 0 and 1 have M=+ and G=3/16, but distinct J and L.
        # Start from actual saved-J recorded vectors, then condition on these
        # two bins. A phase flip of one bin is a new stipulated intervention.
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,1,4)
            rec=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            def only(rows,i):
                return tuple([v if k==i else 0*v for k,v in enumerate(part)] for part in rows)
            a=only(rec[-1],0);b=only(rec[1],1)
            self.assertAlmostEqual(mass(a)/total,.25,places=12)
            self.assertAlmostEqual(mass(b)/total,.25,places=12)
            self.assertLess(abs(dot_rows(a,b))/total,1e-14)
            self.assertEqual(record(0,1,3)['L'],-1)
            self.assertEqual(record(1,1,3)['L'],1)
            self.assertEqual(record(0,1,3)['G'],record(1,1,3)['G'])
        # Isometric 2x2 representation of these actual orthogonal branches.
        plus=np.array([1,0,0,1],complex)/np.sqrt(2)
        minus=np.array([1,0,0,-1],complex)/np.sqrt(2)
        rho=np.outer(plus,plus.conj());sigma=np.outer(minus,minus.conj())
        self.assertAlmostEqual(distance(trace_out_first(rho,2,2),trace_out_first(sigma,2,2)),0.)
        self.assertAlmostEqual(distance(trace_out_second(rho,2,2),trace_out_second(sigma,2,2)),0.)
        self.assertAlmostEqual(distance(rho,sigma),1.)
        self.assertAlmostEqual(float(np.trace(rho@rho).real),1.)
        self.assertAlmostEqual(float(np.trace(rho@sigma).real),0.)
        # Each side can read the copied classical sign, but neither reduced
        # state identifies the relative phase; a joint effect can.

    def test_persistence_truth_is_not_in_the_unchanged_physical_table(self):
        # O=1 for a persistent owner and O=0 for a momentary owner at two
        # distinct checkpoints. Both have the same actual physical records.
        for i,s,t in product(range(4),(1,-1),range(4)):
            persistent=record(i,s,t).copy();momentary=record(i,s,t).copy()
            self.assertEqual(persistent,momentary)
            self.assertEqual(target(i,s,t,'ledger'),physical_ledger(i,s))
        # A witness whose law depends on O would be an additional bridge.

    def test_calibrated_witness_and_neither_candidate_control(self):
        result=ownership_witness(950,1000,.05,.1,.1)
        self.assertAlmostEqual(result['radius'],.04294694083467376)
        self.assertTrue(result['reject_momentary'])
        self.assertFalse(result['reject_persistent'])
        neither=ownership_witness(500,1000,.05,.1,.1)
        self.assertTrue(neither['reject_momentary'])
        self.assertTrue(neither['reject_persistent'])
        ambiguous=ownership_witness(600,1000,.05,.6,.4)
        self.assertFalse(ambiguous['reject_momentary'])
        self.assertFalse(ambiguous['reject_persistent'])
        with self.assertRaises(ValueError):ownership_witness(1001,1000,.05,.1,.1)
        with self.assertRaises(ValueError):ownership_witness(1,2,0.,.1,.1)
        # The counts and identity-error bounds are hypothetical, not data.

if __name__=='__main__':unittest.main()
