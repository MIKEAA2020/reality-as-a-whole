"""Full-clock and constrained-pair extension of record-dressed rotations."""
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_internal_reference_subject_valence_candidates_test import b_project
from verification.zero_internal_contextual_reference_test import value_history
from verification.zero_relational_chirality_report_test import apply64
from verification.zero_dressed_history_pair import _PHYSICAL_VALID,full_q
from verification.zero_clock_finite_reservoir_reuse_test import BITS3,Q
from verification.zero_sphere_angular_echo import magnitude
from fractions import Fraction
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import words
from verification.zero_coherent_clock_angular_history import apparatus_path,apparatus_weight,quantum_echo_checkpoints,checkpoint_at
from verification.zero_dressed_sphere_rotations import build_frames,transport
from verification.zero_dressed_history_pair import (
    gate,to_anchor,from_anchor,move_tick,apparatus_prefix,apparatus_retarget,
    bin_at,encode_pair,decode_pair,pair_permutation,move_encoded_component,
)


def diff(a,b):return sum(norm2(x-y) for x,y in zip(a,b))
def size(a):return sum(norm2(x) for x in a)
def from_bin(rows,i):return rows[0][i],rows[1][i]


class DressedHistoryPairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shape,cls.frames,cls.info=build_frames()
        cls.root=output(active_base())
        cls.cols=((1,),(0,))

    @classmethod
    def tearDownClass(cls):
        del cls.frames,cls.root

    def test_full_q_extension_is_necessary_outside_valid_sector(self):
        rng=np.random.default_rng(151)
        v=rng.normal(size=self.shape)+1j*rng.normal(size=self.shape)
        invalid=v-apply64(_PHYSICAL_VALID,v)
        total=norm2(invalid)
        self.assertGreater(total,1.)
        self.assertLess(norm2(full_q(invalid)-invalid)/total,1e-22)
        # value_history was only the right O on supported vectors, not the
        # full involution: its unprojected use is not a valid full-space Q.
        self.assertGreater(norm2(value_history(invalid)-invalid)/total,.1)
        self.assertLess(norm2(full_q(full_q(v))-v)/norm2(v),1e-22)

    def test_echo_checkpoint_transport_all_ticks_and_both_signs(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            for t in range(20):
                rows=states[checkpoint_at(t)]
                for u,i in ((-.75,0),(-.25,1),(.25,2),(.75,3)):
                    pair=from_bin(rows,i)
                    self.assertLess(diff(to_anchor(pair,t),from_bin(states[3],i))/total,1e-23)
                    self.assertLess(diff(from_anchor(to_anchor(pair,t),t),pair)/total,1e-23)
                for target,i in ((-.75,0),(-.25,1),(.75,3)):
                    moved=move_tick(from_bin(rows,2),t,.25,target,s,self.frames,self.shape)
                    self.assertLess(diff(moved,from_bin(rows,i))/total,1e-21)

    def test_tick_transport_cocycle_and_unitarity_on_arbitrary_vectors(self):
        rng=np.random.default_rng(15)
        pair=tuple(rng.normal(size=self.shape)+1j*rng.normal(size=self.shape) for _ in range(2))
        total=size(pair)
        for t,s in product((0,7,8,9,10,11,12,13,19),(1,-1)):
            a=move_tick(pair,t,.2,-.7,s,self.frames,self.shape)
            b=move_tick(move_tick(pair,t,.2,-.2,s,self.frames,self.shape),t,-.2,-.7,s,self.frames,self.shape)
            self.assertLess(diff(a,b)/total,1e-21)
            self.assertAlmostEqual(size(a)/total,1,places=12)
            self.assertLess(diff(from_anchor(to_anchor(pair,t),t),pair)/total,1e-22)

    def test_each_echo_step_intertwines_dressed_transfers(self):
        rng=np.random.default_rng(150)
        pair=tuple(rng.normal(size=self.shape)+1j*rng.normal(size=self.shape) for _ in range(2))
        total=size(pair);steps={7:'T',8:'Q',9:'T',10:'T',11:'Q',12:'T'}
        for t in range(20):
            nxt=(t+1)%20
            def step(z):return gate(z,steps[t]) if t in steps else z
            lhs=step(move_tick(pair,t,.25,-.75,1,self.frames,self.shape))
            rhs=move_tick(step(pair),nxt,.25,-.75,1,self.frames,self.shape)
            self.assertLess(diff(lhs,rhs)/total,1e-21)

    def test_apparatus_actual_gate_prefixes_and_bidirectional_retarget(self):
        # All 256 coherent purifier/reference components for either physical B.
        for b,x,f,e in product((0,1),BITS3,BITS3,words(1)):
            path=apparatus_path(b,x,f,e,self.cols)
            for t in range(21):
                actual=apparatus_prefix(path[0],t,self.cols)
                self.assertEqual(actual,path[t])
                self.assertEqual(apparatus_prefix(actual,t,self.cols,True),path[0])
                other=apparatus_retarget(actual,t,1-b,self.cols)
                self.assertEqual(other,apparatus_path(1-b,x,f,e,self.cols)[t])
                self.assertEqual(apparatus_retarget(other,t,b,self.cols),actual)
        # The matching path map preserves coherent complex amplitudes on each
        # orthogonal reference/purifier sector; it is not a measured trajectory.

    def test_naive_old_record_transfer_fails_on_reservoir(self):
        def overlap(t):
            return sum(float(apparatus_weight(f,e,Q)) for x,f,e in product(BITS3,BITS3,words(1))
                       if apparatus_path(0,x,f,e,self.cols)[t][1:]==apparatus_path(1,x,f,e,self.cols)[t][1:])
        self.assertAlmostEqual(overlap(0),1.,places=12)
        self.assertAlmostEqual(overlap(7),0.,places=12)
        self.assertAlmostEqual(overlap(10),0.,places=12)
        self.assertAlmostEqual(overlap(20),1.,places=12)
        # At tick 10 bare old-record dressing maps the B state but leaves the
        # orthogonal B-dependent apparatus unchanged: fixed-state fidelity 0.

    def test_pair_encoding_isometry_and_zero_charge_actual_records(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            for u,i in ((-.75,0),(-.25,1),(.25,2),(.75,3)):
                self.assertEqual(bin_at(u),i)
                pair=from_bin(states[3],i);encoded=encode_pair(pair,i,s)
                self.assertLess(diff(decode_pair(encoded,i,s,pair[0]),pair)/total,1e-23)
                self.assertAlmostEqual(sum(size(z) for z in encoded.values())/size(pair),1.,places=12)
                for a,b,z1,z2 in encoded:
                    self.assertEqual((a,b),(i,i))
                    self.assertEqual(z1+z2,0)
                for v,j in ((-.75,0),(-.25,1),(.25,2),(.75,3)):
                    other=transport(pair,self.frames,self.shape,u,v,s)
                    lifted=encode_pair(other,j,s)
                    target=encode_pair(from_bin(states[3],j),j,s)
                    self.assertLess(sum(diff(lifted[k],target[k]) for k in target)/total,1e-21)

    def test_joint_physical_pair_echo_and_purified_apparatus_transfer(self):
        for label,s in product((0,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            for t in (0,7,8,10,11,19):
                # Encode at anchor, then move to the specified clock block.
                anchor=encode_pair(from_bin(states[3],2),2,s)
                source={k:from_anchor(v,t) for k,v in anchor.items()}
                a=apparatus_path(0,(1,0,1),(0,1,0),(1,),self.cols)[t]
                for u,i in ((-.75,0),(-.25,1)):
                    result,apparatus=move_encoded_component(source,a,t,.25,u,s,
                                                           self.frames,self.shape,self.cols)
                    target={k:from_anchor(v,t) for k,v in
                            encode_pair(from_bin(states[3],i),i,s).items()}
                    self.assertEqual(set(result),set(target))
                    self.assertLess(sum(diff(result[k],target[k]) for k in target)/total,1e-21)
                    self.assertEqual(apparatus,apparatus_path(1,(1,0,1),(0,1,0),(1,),self.cols)[t])
                    self.assertTrue(all(key[0]==i and key[1]==i and key[2]+key[3]==0
                                        for key in result))

    def test_pair_extension_is_permutation_on_full_pair_basis(self):
        for i,s,r,j,a,b,z1,z2 in product(range(4),(1,-1),(1,-1),(1,-1),range(4),range(4),(1,-1),(1,-1)):
            v=pair_permutation(i,s,r,j,a,b,z1,z2)
            self.assertEqual(pair_permutation(i,s,r,j,*v,inverse=True),(a,b,z1,z2))
            self.assertEqual(pair_permutation(i,s,r,j,0,0,1,1),(i,i,s*r*j,-s*r*j))

    def test_local_magnitude_is_not_invariant_under_dressed_rotation(self):
        source=Fraction(1,4);target=Fraction(-3,4)
        for kind in ('absolute','swap_invariant'):
            gs=magnitude(source,kind);gt=magnitude(target,kind)
            self.assertNotEqual(gs*gs,gt*gt)
            # On the physical pair, H1²=g(u)² I, so a transfer connecting
            # these angles cannot commute with the individual charge squared.
            self.assertNotEqual((gs*gs-gt*gt),0)
        # Nevertheless H1+H2 is identically zero on the constrained sector.

    def test_pair_projector_rejects_invalid_sector(self):
        x=initial(relative_read(self.root,4,labels=(0,))[0])
        _,total,states=quantum_echo_checkpoints(x,1,4)
        pair=from_bin(states[3],2)
        invalid={(2,2,1,1):pair,(0,2,-1,1):pair}
        projected=decode_pair(invalid,2,1,pair[0])
        self.assertLess(size(projected)/total,1e-25)
        # Physical-sector action is W_target U W_source†. The full-basis
        # permutation supplies an extension without equating opposite signs.

if __name__=='__main__':unittest.main()
