"""Realm restriction on the five-ray state; conditional pair-balance theorem.

Static-state comparison, no holding mechanism, no claim of actual subjects,
real physical planes, felt signs, objective global zero or a selected outcome.
"""
import unittest
from fractions import Fraction as F
from itertools import product
from verification.zero_five_ray_record_current_unification_test import (
    joint_state, probabilities, local_density, apply_work, index, norm2
)
from verification.zero_sphere_mismatch_experience_comparison_test import (
    subject_density, phase_flip, branch_current
)
from verification.zero_reciprocal_subject_exchange_test import J
from verification.zero_spin_constitution_test import close,inner


def pair_totals(mu1,mu2,plus,minus):
    return mu1*plus+mu2*minus, mu1*minus+mu2*plus


def phase_density_comparison(a,b):
    return max(abs(x-y) for rowa,rowb in zip(a,b) for x,y in zip(rowa,rowb))


class RealmPhysicalZeroIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t=joint_state('triple'); cls.p=joint_state('pair')
        cls.tf=phase_flip(cls.t); cls.pf=phase_flip(cls.p)

    def test_two_full_states_orthogonal_not_a_global_phase(self):
        for v,w in ((self.t,self.tf),(self.p,self.pf)):
            self.assertAlmostEqual(norm2(v),1)
            self.assertAlmostEqual(norm2(w),1)
            self.assertAlmostEqual(abs(inner(v,w)),0)

    def test_entire_candidate_subsystem_restriction_is_identical(self):
        # This includes both reference blocks and both records, not just means.
        for v,w in ((self.t,self.tf),(self.p,self.pf)):
            close(self,subject_density(v),subject_density(w))
        close(self,subject_density(self.t),subject_density(self.p))

    def test_five_ray_triple_joint_record_table_is_identical(self):
        expected=[(F(3,40),F(1,20)),(F(1,10),F(3,10)),(F(13,40),F(3,20))]
        for v in (self.t,self.tf):
            p=probabilities(v)
            for i,(a,b) in enumerate(expected):
                self.assertAlmostEqual(p[(i,1)],float(a))
                self.assertAlmostEqual(p[(i,2)],float(b))

    def test_current_sharp_on_every_record_phase_and_sphere_branch(self):
        for v,phase in ((self.t,1),(self.tf,-1),(self.p,1),(self.pf,-1)):
            j1=apply_work(v,J[0]); j2=apply_work(v,J[2])
            for a,b,i,r,w in product(range(2),range(2),range(5),range(4),range(16)):
                k=index(a,b,i,r,w)
                rsign={0:0,1:1,2:-1,3:0}[r]
                self.assertAlmostEqual(abs(j1[k]-phase*rsign*v[k]),0)
                self.assertAlmostEqual(abs(j2[k]+phase*rsign*v[k]),0)

    def test_full_receiver_differs_between_states_but_not_alice_settings(self):
        original=local_density(self.t); changed=local_density(self.tf)
        self.assertGreater(phase_density_comparison(original,changed),1e-3)
        close(self,local_density(self.t),local_density(self.p))
        close(self,local_density(self.tf),local_density(self.pf))
        for ra,sign in ((0,1),(1,-1)):
            self.assertAlmostEqual(branch_current(self.t,ra),sign)
            self.assertAlmostEqual(branch_current(self.tf,ra),-sign)

    def test_richer_record_current_correlator_detects_the_difference(self):
        # Neither unconditional record mean nor unconditional current mean
        # detects the phase: the joint record/current correlation does.
        for v,want in ((self.t,1),(self.tf,-1),(self.p,1),(self.pf,-1)):
            jv=apply_work(v,J[0])
            corr=0j
            for a,b,i,r,w in product(range(2),range(2),range(5),range(4),range(16)):
                k=index(a,b,i,r,w); z=1-2*((r>>1)&1)
                corr+=v[k].conjugate()*z*jv[k]
                self.assertAlmostEqual(abs(z*jv[k]-want*v[k]),0)
            self.assertAlmostEqual(corr.real,want)
            self.assertAlmostEqual(corr.imag,0)
            self.assertAlmostEqual(inner(v,jv).real,0)

    def test_pairwise_zero_for_all_signs_forces_odd_response_and_equal_weights(self):
        # Exact exhaustive bounded rational grid, supplementing the analytic
        # determinant proof. Weights are positive and fixed across both signs.
        vals=[F(-1),F(-1,2),F(0),F(1,2),F(1)]
        ws=[F(1,2),F(1),F(2)]
        for m1,m2,up,down in product(ws,ws,vals,vals):
            zero=pair_totals(m1,m2,up,down)==(0,0)
            characterized=(up==0 and down==0) or (m1==m2 and up==-down)
            self.assertEqual(zero,characterized)

    def test_zero_subject_pair_is_a_stronger_claim_than_global_zero(self):
        # Same two nonzero negative local values can be globally balanced by
        # a further +2 contribution; this is an explicit possible ledger,
        # not evidence that such a contribution exists or that pain disappears.
        self.assertEqual(sum((F(-1),F(-1),F(2))),0)
        self.assertNotEqual(sum((F(-1),F(-1))),0)

    def test_unconditional_zero_can_hide_unbalanced_record_events(self):
        plus,minus=F(1),F(-1)
        for m1,m2 in ((F(1),F(2)),(F(2),F(1))):
            b0,b1=pair_totals(m1,m2,plus,minus)
            self.assertNotEqual(b0,0); self.assertNotEqual(b1,0)
            self.assertEqual((b0+b1)/2,0)

    def test_state_dependent_positive_incidence_evades_fixed_weight_theorem(self):
        # Valid pair zero despite opposite non-odd response if weights are
        # allowed to change with the sign; an extra burden, not a refutation.
        up,down=F(1),F(-2)
        event_plus=F(2)*up+F(1)*down
        event_minus=F(1)*down+F(2)*up
        self.assertEqual((event_plus,event_minus),(0,0))
        self.assertNotEqual(up,-down)

    def test_current_sphere_constraints_do_not_fix_response_magnitude(self):
        for k in (F(1,2),F(1),F(2),F(100)):
            self.assertEqual(pair_totals(F(1),F(1),k,-k),(0,0))

if __name__=='__main__': unittest.main()
