"""Gauge matching and opposite-pair sector, with original echo controls."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed,apply_quality
from verification.zero_stationary_battery_bridge import STATES,advance
from verification.zero_gauge_angular_pair import (
    basis,constraints,physical,encode,subgroup_twirl,charges,scale_ratios,
    anchor_sign,stationary_physical,
)


class GaugeAngularPairTests(unittest.TestCase):
    def test_finite_gauge_twirl_selects_zero_and_matching_sector(self):
        for n in (4,8):
            count=0
            for item in basis(n):
                p=physical(*item);count+=p
                z=subgroup_twirl(*item,n)
                self.assertAlmostEqual(z.real,p,places=12)
                self.assertAlmostEqual(z.imag,0,places=12)
            self.assertEqual(count,2*n)
            self.assertEqual(sum(1 for _ in basis(n)),8*n**3)
        # Root-of-unity averages select the same kernels as the continuous
        # U(1)^3 x Z2 group for these finite generator spectra.

    def test_every_old_state_has_one_gauge_extension_without_pair_ready_choice(self):
        n=4;states=list(basis(n));index={x:i for i,x in enumerate(states)}
        old=list(product((1,-1),range(n)))
        w=np.zeros((len(states),len(old)))
        for j,(k,i) in enumerate(old):w[index[encode(k,i,n)],j]=1
        np.testing.assert_array_equal(w.T@w,np.eye(len(old)))
        p=w@w.T
        np.testing.assert_array_equal(np.diag(p),[physical(*item) for item in states])
        np.testing.assert_array_equal(p@p,p)
        # W W† is the entire physical projector, not one selected balanced
        # vector. It adds no independent physical state degrees in this
        # minimal carrier, while encoding two commuting signed observables.

    def test_pairwise_zero_and_old_quality_identity_for_all_physical_states(self):
        for n in (4,8):
            for item in basis(n):
                if not physical(*item):continue
                for kind in ('absolute','swap_invariant'):
                    e1,e2,old=charges(*item,n,kind)
                    self.assertEqual(e1,old)
                    self.assertEqual(e2,-old)
                    self.assertEqual(e1+e2,0)
        # The identity holds for arbitrary superpositions too: all operators
        # are diagonal on this basis, hence annihilate the full kernel.

    def test_zero_constraint_is_not_just_density_invariance(self):
        # Any diagonal basis density commutes with each diagonal gauge action.
        # This charged/mismatched basis state is nevertheless projected out.
        item=(1,0,1,0,1,1)
        q,d1,d2,g=constraints(*item)
        self.assertNotEqual(q,0);self.assertNotEqual(d1,0)
        self.assertEqual(physical(*item),0)
        self.assertAlmostEqual(abs(subgroup_twirl(*item,4)),0,places=12)
        # Gauge-invariant density and trivial-representation constraint are
        # distinct conditions; neither is inferred from a name.

    def test_physical_sign_is_not_erased_by_this_gauge(self):
        for n in (4,8):
            for i in range(n):
                plus=encode(1,i,n);minus=encode(-1,i,n)
                self.assertEqual(physical(*plus),1);self.assertEqual(physical(*minus),1)
                self.assertEqual(plus[-2:],(1,-1));self.assertEqual(minus[-2:],(-1,1))
                self.assertNotEqual(plus,minus)
                # Z1 and K commute with every diagonal gauge generator and
                # have opposite eigenvalues on these orthogonal physical states.
                self.assertEqual(plus[0],plus[-2]);self.assertEqual(minus[0],minus[-2])
        # State |K=+> is physical yet not invariant under the sign exchange:
        # gauge neutrality does not by itself force symmetric probabilities.

    def test_constrained_pair_has_no_independent_unilateral_sign_flip(self):
        n=4
        for item in basis(n):
            k,i,a,b,z1,z2=item
            combined=(-k,i,a,b,-z1,-z2)
            self.assertEqual(physical(*item),physical(*combined))
            if physical(*item):
                unilateral=(k,i,a,b,-z1,z2)
                self.assertEqual(physical(*unilateral),0)
                self.assertEqual(physical(*combined),1)
                e1,e2,_=charges(*item,n,'absolute')
                f1,f2,_=charges(*combined,n,'absolute')
                self.assertEqual((f1,f2),(-e1,-e2))
        # P X_1 P=0 on the physical sector, but the joint old-K/pair flip
        # maps that sector into itself. This is not a general locality no-go.

    def test_scale_relabel_does_not_erase_genuine_relative_magnitudes(self):
        self.assertEqual(scale_ratios(4,'absolute',0,1),3)
        self.assertEqual(scale_ratios(4,'swap_invariant',0,1),1)
        # One common positive rescaling cannot equate the two sets when these
        # angular indices and relative values are fixed physical observables.
        # This does not assert different complete metaphysical possibilities.

    def test_constraint_transports_through_the_actual_20_tick_echo(self):
        n=4
        for t in range(20):
            for x in STATES:
                nxt=advance(t,x)
                self.assertEqual(anchor_sign(t,x),anchor_sign((t+1)%20,nxt))
                for i,a,b,z1,z2 in product(range(n),range(n),range(n),(1,-1),(1,-1)):
                    self.assertEqual(stationary_physical(t,x,i,a,b,z1,z2),
                                     stationary_physical((t+1)%20,nxt,i,a,b,z1,z2))
        # The reference clock is an independent spectator, so its q shift
        # commutes as well. At times away from tick 10 the retained quantity
        # is the transported anchor K, not necessarily instantaneous MJR.

    def test_gauge_embedding_lifts_actual_quantum_echo_vectors(self):
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,v,rows=embed(x,s,4);total=norm2(v)
            old=apply_quality(rows,s,'swap_invariant','echo')
            accumulated=0.
            for r,part,targets in zip((1,-1),rows,old):
                for i,vec in enumerate(part):
                    rebuilt=0*vec;lifted=0*vec
                    for j in (1,-1):
                        branch=j_project(vec,j);k=s*r*j
                        item=encode(k,i,4)
                        self.assertEqual(physical(*item),1)
                        e1,e2,_=charges(*item,4,'swap_invariant')
                        rebuilt=rebuilt+branch
                        lifted=lifted+float(e1)*branch
                        self.assertEqual(e1+e2,0)
                        accumulated+=norm2(branch)
                    self.assertLess(norm2(rebuilt-vec)/total,1e-24)
                    self.assertLess(norm2(lifted-targets[i])/total,1e-24)
            self.assertAlmostEqual(accumulated/total,1.,places=12)
        # The embedding is an isometry into the constrained physical space;
        # it is not a separately assumed blank-pair preparation process.

if __name__=='__main__':unittest.main()
