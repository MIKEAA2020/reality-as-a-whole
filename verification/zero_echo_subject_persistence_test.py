"""Record, access, and ownership controls on the original coherent echo."""
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_coherent_signed_counterpart import exchange
from verification.zero_dressed_history_pair import encode_pair
from verification.zero_stationary_battery_bridge import STATES,PREFIX
from verification.zero_stationary_subject_incidence import stationary_flip
from verification.zero_quantum_angular_echo import mass,difference_mass
from verification.zero_joint_quality_incidence_root import counterpart,quality
from verification.zero_echo_subject_persistence import (
    TICKS,partitions,component_partitions,component_slots,same_owner,owner,refined_owner,shift_slot,shift_owner,table,best_guess,project_j,copy_initial_j,
    evolve_record,compare_j_masses,erase_record,record_fidelity,
)


class EchoSubjectPersistenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_hypothetical_ownership_relations_are_distinct_equivalence_relations(self):
        for rule in partitions():
            for a,b,c in product(TICKS,repeat=3):
                self.assertTrue(same_owner(rule,a,a))
                self.assertEqual(same_owner(rule,a,b),same_owner(rule,b,a))
                if same_owner(rule,a,b) and same_owner(rule,b,c):self.assertTrue(same_owner(rule,a,c))
        self.assertEqual([same_owner(r,7,10) for r in partitions()],[True,False,False])
        self.assertEqual([same_owner(r,7,13) for r in partitions()],[True,False,True])
        # Same physical law for each ownership extension; a conscious owner
        # and a faithful first-person identity report are not physical inputs.
        law=table()
        for rule in partitions():
            self.assertEqual(sum(law.values()),1)
            for row,p in law.items():self.assertEqual(p,F(1,8))

    def test_two_ownership_rules_are_clock_covariant_and_type_equivariant(self):
        for policy,t,x,factor in product(('worldline','momentary'),range(20),STATES,(1,2)):
            before=owner(policy,t,x,factor)
            self.assertEqual(owner(policy,*shift_slot(t,x,factor)),shift_owner(policy,before))
            flipped=stationary_flip(t,x)
            # A bijective type map cannot collapse two different seed owners.
            b,j,r,s=x
            signed=(b,j,r,-s)
            for y in STATES:
                same=owner(policy,t,x,factor)==owner(policy,t,y,factor)
                self.assertEqual(same,owner(policy,t,flipped,factor)==owner(policy,t,stationary_flip(t,y),factor))
                by,jy,ry,sy=y
                self.assertEqual(same,owner(policy,t,signed,factor)==owner(policy,t,(by,jy,ry,-sy),factor))
        for policy,seed,t,u,factor in product(('worldline','momentary'),STATES,range(20),range(20),(1,2)):
            x,y=PREFIX[t][seed],PREFIX[u][seed]
            same=owner(policy,t,x,factor)==owner(policy,u,y,factor)
            self.assertEqual(same,owner(policy,t,stationary_flip(t,x),factor)==owner(policy,u,stationary_flip(u,y),factor))
            bx,jx,rx,sx=x;by,jy,ry,sy=y
            self.assertEqual(same,owner(policy,t,(bx,jx,rx,-sx),factor)==owner(policy,u,(by,jy,ry,-sy),factor))
        seed=(1,1,1,1)
        states=[PREFIX[t][seed] for t in range(20)]
        self.assertEqual(len({owner('worldline',t,states[t],1) for t in range(20)}),1)
        self.assertEqual(len({owner('momentary',t,states[t],1) for t in range(20)}),20)
        # Clock covariance and physical type/sign symmetry do not pick one.

    def test_physical_refinement_is_not_automatically_subject_splitting(self):
        seed=(1,1,1,1)
        for policy in ('worldline','momentary'):
            for t in range(20):
                x=PREFIX[t][seed]
                fixed=[refined_owner(policy,t,x,1,tag) for tag in (0,1)]
                divided=[refined_owner(policy,t,x,1,tag,True) for tag in (0,1)]
                self.assertEqual(len(set(fixed)),1)
                self.assertEqual(len(set(divided)),2)
                # An independent fair physical tag partitions 1/8 into two
                # distinct outcomes, each 1/16; coarse mass is unchanged.
                self.assertEqual(sum((F(1,16),F(1,16))),F(1,8))
        # Both ownership extensions require separate constitutive premises.

    def test_pair_factors_do_not_select_subject_multiplicity(self):
        slots=component_slots()
        self.assertEqual(len(slots),6)
        candidates=component_partitions()
        self.assertEqual({k:len(set(v)) for k,v in candidates.items()},
                         {'composite':1,'two_persistent':2,'six_momentary':6})
        for rule,owners in candidates.items():
            self.assertEqual(len(owners),len(slots))
            for a,b,c in product(range(6),repeat=3):
                if owners[a]==owners[b] and owners[b]==owners[c]:
                    self.assertEqual(owners[a],owners[c])
        # Different cardinalities preclude identity-preserving relabeling.
        # Each is an explicit supplemental ontology, not evidence of subjects.

    def test_confined_sign_algebras_and_optimal_readout(self):
        self.assertEqual(best_guess(('j',),'now'),F(1,2))
        self.assertEqual(best_guess(('j','z'),'now'),F(1,2))
        self.assertEqual(best_guess(('s','j'),'now'),1)
        self.assertEqual(best_guess(('s','j'),'echo'),F(3,4))
        self.assertEqual(best_guess(('s','j','r'),'echo'),1)
        self.assertEqual(best_guess(('j',),'b'),F(3,4))
        self.assertEqual(best_guess(('j','z'),'b'),1)
        self.assertEqual(best_guess(('z',),'b'),F(3,4))
        # Scope is only the listed commuting, classical sign readouts. This
        # does not bound arbitrary quantum measurements on other degrees.

    def test_table_has_counterpart_pair_and_actual_comparison(self):
        for (i,s,z,b,j,r),w in table().items():
            self.assertEqual(j,z*b)
            self.assertEqual(r,b)
            self.assertEqual(quality(i,-s),tuple(-v for v in quality(i,s)))
            self.assertIn((i,-s,z,b,j,r),table())
            self.assertEqual(w,table()[i,-s,z,b,j,r])
            self.assertEqual(counterpart(i,s),(i,-s))

    def test_record_copies_real_echo_and_can_be_uncomputed(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            start=states[0];record=copy_initial_j(start)
            self.assertAlmostEqual(mass(record[1])/total,F(3,4),places=12)
            self.assertAlmostEqual(mass(record[-1])/total,F(1,4),places=12)
            anchor=evolve_record(record,('T','Q','T'))
            actual=compare_j_masses(anchor)
            for key,p in {(1,1):F(1,2),(1,-1):F(1,4),(-1,1):F(1,4),(-1,-1):F(0)}.items():
                self.assertAlmostEqual(actual[key]/total,p,places=12)
            self.assertAlmostEqual(record_fidelity(anchor,states[3]),F(5,8),places=12)
            # Uncomputing at tick 10 fails to reset the ready bit on B−.
            early=erase_record(anchor)
            self.assertAlmostEqual(mass(early[-1])/total,F(1,2),places=12)
            closed=evolve_record(anchor,('T','Q','T'))
            erased=erase_record(closed)
            self.assertLess(difference_mass(erased[1],start)/total,1e-23)
            self.assertLess(mass(erased[-1])/total,1e-23)
        # A ready ancilla and two controlled couplings are extra resources.

    def test_record_respects_clock_dressed_sign_counterpart(self):
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,p=quantum_echo_checkpoints(x,1,4)
            _,_,m=quantum_echo_checkpoints(x,-1,4)
            records=[copy_initial_j(p[0]),copy_initial_j(m[0])]
            ops=('T','Q','T','T','Q','T')
            for tick in range(7,14):
                for z in (1,-1):
                    mapped=exchange(records[0][z],tick)
                    other=tuple([-v for v in part] for part in records[1][z])
                    self.assertLess(difference_mass(mapped,other)/total,1e-23)
                if tick<13:records=[evolve_record(r,(ops[tick-7],)) for r in records]
        # S commutes with J, so the new memory is a spectator; phase(t) is
        # still essential on ticks 9,10,11. This is not subject identity.

    def test_anchor_pair_sign_and_saved_record_share_the_same_branches(self):
        for label,s in product((0,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            recorded=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            for z,rows in recorded.items():
                for i in range(4):
                    b=-1 if i<2 else 1
                    j=z*b
                    pair=rows[0][i],rows[1][i]
                    for (a,c,z1,z2),part in encode_pair(pair,i,s).items():
                        if sum(mass(((v,),)) for v in part)/total<1e-24:continue
                        self.assertEqual((a,c),(i,i))
                        self.assertEqual((z1,z2),(s*b*j,-s*b*j))
                        self.assertEqual(z1,s*z)

    def test_erasure_works_for_a_superposition_not_only_the_prepared_input(self):
        x=initial(relative_read(self.root,4,labels=(7,))[0])
        _,total,states=quantum_echo_checkpoints(x,-1,4)
        # Coherent branch combination with a relative complex phase. CNOT
        # and its inverse recover all of it, not just marginal probabilities.
        plus=project_j(states[0],1);minus=project_j(states[0],-1)
        y=tuple([a+1j*b for a,b in zip(p,q)] for p,q in zip(plus,minus))
        record=copy_initial_j(y)
        recovered=erase_record(evolve_record(record,('T','Q','T','T','Q','T')))
        self.assertLess(difference_mass(recovered[1],y)/total,1e-23)
        self.assertLess(mass(recovered[-1])/total,1e-23)

if __name__=='__main__':unittest.main()
