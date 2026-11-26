"""Joint single-incidence quality candidate on the actual coherent echo."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed,apply_swap
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_dressed_sphere_rotations import old_exchange
from verification.zero_dressed_history_pair import encode_pair
from verification.zero_joint_quality_incidence_root import (
    ANGLES,R,J,PORTS,event,value,quality,swap,counterpart,weight,measure,echo_checkpoints,
    scalar_after_alias,twin_vectors,joint_law,expanded_type_weights,
)


def components(rows,i):return rows[0][i],rows[1][i]
def difference(a,b):return sum(norm2(x-y) for x,y in zip(a,b))


class JointQualityIncidenceRootTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_joint_law_is_not_two_independent_incidence_censuses(self):
        self.assertEqual(joint_law(),{(a,b):F(1,4) for a,b in product((1,-1),repeat=2)})
        all_labels=[(i,s,p) for i in range(4) for s in (1,-1) for p in PORTS]
        self.assertEqual(len(all_labels),16)
        self.assertEqual(measure(all_labels),1)
        self.assertEqual(measure([(0,1,'now'),(0,1,'echo')]),F(1,8))
        self.assertEqual(measure([(0,1,'now'),(1,1,'echo')]),F(1,4))
        for i,s in product(range(4),(1,-1)):
            if R[i]==1:self.assertEqual(scalar_after_alias(i,s),value(i,s,'now'))
            else:
                with self.assertRaises(ValueError):scalar_after_alias(i,s)
        # One incidence per joint event is a hypothesis. Two unequal scalar
        # values cannot both descend to one scalar on one unchanged event.

    def test_disjoint_type_model_is_a_real_alternative_not_an_alias(self):
        for alpha in (F(1,10),F(1,2),F(9,10)):
            w=expanded_type_weights(alpha)
            self.assertEqual(sum(w.values()),1)
            for i,s in product(range(4),(1,-1)):
                self.assertEqual(sum(w[i,s,p] for p in PORTS),weight(i,s))
            # At event (0,+), now=+ and echo=-; distinct type weights
            # make a conditional typed-sign prediction depend on alpha.
            self.assertEqual(value(0,1,'now'),1)
            self.assertEqual(value(0,1,'echo'),-1)
            self.assertEqual(w[0,1,'now']/weight(0,1),alpha)
        # Physical marginal and sign-exchange balance alone do not fix alpha.

    def test_joint_value_covariances_and_zero_as_a_vector(self):
        for i,s in product(range(4),(1,-1)):
            a,b=quality(i,s)
            self.assertEqual(quality(*swap(i,s)),(b,a))
            self.assertEqual(quality(*counterpart(i,s)),(-a,-b))
            for kind in ('absolute','swap_invariant'):
                p,m=twin_vectors(i,s,kind)
                self.assertEqual(tuple(x+y for x,y in zip(p,m)),(0,0))
                self.assertEqual(p,tuple(-v for v in m))
            self.assertEqual(twin_vectors(*swap(i,s))[0],
                             tuple(reversed(twin_vectors(i,s)[0])))
        # For |u|, the previous type map changes magnitudes in negative bins.
        self.assertNotEqual(twin_vectors(0,1,'absolute')[0],
                            tuple(reversed(twin_vectors(*swap(0,1),'absolute')[0])))

    def test_pairwise_zero_does_not_force_asymmetric_incidence_balance(self):
        for i,s in product(range(4),(1,-1)):
            positive,negative=twin_vectors(i,s)
            # Local pair sum is exactly zero, but a hypothetical incidence
            # counting one component twice does not preserve that cancellation.
            weighted=tuple(2*a+b for a,b in zip(positive,negative))
            self.assertEqual(weighted,positive)
            self.assertNotEqual(weighted,(0,0))
        # Even with one component per event, an incidence measure biased
        # toward s=+1 is not invariant under the physical sign counterpart.
        plus,minus=quality(0,1),quality(0,-1)
        mean=tuple(F(3,4)*a+F(1,4)*b for a,b in zip(plus,minus))
        self.assertEqual(mean,(F(1,2),F(-1,2)))
        self.assertEqual(tuple(F(1,2)*a+F(1,2)*b for a,b in zip(plus,minus)),(0,0))

    def test_16_actual_complex_histories_give_the_joint_cells(self):
        for label in range(16):
            x=initial(relative_read(self.root,4,labels=(label,))[0]);total=norm2(x)
            cells={(a,b):0. for a,b in product((1,-1),repeat=2)}
            for s in (1,-1):
                _,_,rows=embed(x,s,4)
                for i in range(4):
                    pair=components(rows,i)
                    mass=sum(norm2(v) for v in pair)/total
                    self.assertAlmostEqual(mass,1/8,places=12)
                    expected_r=0 if R[i]==1 else 1
                    self.assertLess(norm2(pair[1-expected_r])/total,1e-23)
                    self.assertLess(norm2(j_project(pair[expected_r],J[i])-pair[expected_r])/total,1e-23)
                    cells[quality(i,s)]+=mass
            for p in cells.values():self.assertAlmostEqual(p,1/4,places=12)

    def test_original_type_and_counterpart_act_on_joint_vector(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0]);total=norm2(x)
            _,_,rows=embed(x,s,4);_,_,other=embed(x,-s,4)
            for i in range(4):
                piece=tuple([v if k==i else 0*v for k,v in enumerate(part)] for part in rows)
                transformed=apply_swap(piece,s);j=swap(i,s)[0]
                self.assertLess(difference(components(transformed,j),components(rows,j))/total,1e-22)
                self.assertLess(difference(old_exchange(components(rows,i)),components(other,i))/total,1e-23)
                before=encode_pair(components(rows,i),i,s)
                after=encode_pair(components(transformed,j),j,s)
                for (a,b,z1,z2),part in before.items():
                    if sum(norm2(v) for v in part)/total<1e-24:continue
                    target=(j,j,R[i]*z1,R[i]*z2)
                    self.assertIn(target,after)
                    self.assertAlmostEqual(sum(norm2(v) for v in part)/total,
                                           sum(norm2(v) for v in after[target])/total,places=12)
                # The sector-controlled operation and the genuine old S
                # act on complex vectors, not just on a relabeled table.
                self.assertEqual(quality(j,s),tuple(reversed(quality(i,s))))
                self.assertEqual(quality(i,-s),tuple(-v for v in quality(i,s)))

    def test_actual_pair_encodes_both_coordinates_with_no_extra_sign_choice(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0]);total=norm2(x)
            _,_,rows=embed(x,s,4)
            for i in range(4):
                pair=components(rows,i);encoded=encode_pair(pair,i,s)
                qnow,qecho=quality(i,s)
                for (a,b,z1,z2),parts in encoded.items():
                    mass=sum(norm2(p) for p in parts)/total
                    if mass<1e-24:continue
                    self.assertEqual((a,b),(i,i))
                    self.assertEqual(z1,qecho)
                    self.assertEqual(R[i]*z1,qnow)
                    self.assertEqual(z2,-z1)
                    self.assertEqual((R[i]*z1+R[i]*z2,z1+z2),(0,0))
        # These are operator identities on the specified constrained sector;
        # they are not evidence that either pair component feels the value.

    def test_actual_echo_distinguishes_persistent_subject_from_static_quality(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            for i in range(4):
                path=echo_checkpoints(i,s)
                for t,(j,r,now,echo) in enumerate(path):
                    part=components(states[t],i);ri=0 if r==1 else 1
                    self.assertLess(norm2(part[1-ri])/total,1e-23)
                    self.assertLess(norm2(j_project(part[ri],j)-part[ri])/total,1e-23)
                    self.assertEqual((now,echo),(s*j,s*j*r))
                self.assertEqual(path[0][3],path[3][3])
                self.assertEqual(path[3][2:],quality(i,s))
                if i<2:self.assertNotEqual(path[0][2],path[3][2])
        # A constant full-echo scalar is one component; the richer vector
        # can change. Subject persistence is not itself a quality equation.

    def test_same_joint_state_can_have_different_scalar_readouts(self):
        # In a disagreement event, now and echo are both well-defined,
        # incompatible scalar answers to the question 'the one value' if
        # incorrectly treated as aliases without specifying the coordinate.
        for i,s in product((0,1),(1,-1)):
            self.assertEqual(value(i,s,'now'),-value(i,s,'echo'))
            with self.assertRaises(ValueError):scalar_after_alias(i,s)
        # Joint vector retains the difference without postulating two subjects.
        self.assertEqual(sum(weight(i,s) for i,s in product((0,1),(1,-1))),F(1,2))

if __name__=='__main__':unittest.main()
