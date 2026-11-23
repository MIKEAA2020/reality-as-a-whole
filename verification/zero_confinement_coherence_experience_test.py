"""Four-connection conditional test on the existing five-ray system.

A static family of quantum states; optional experienced-quality mappings and
report rules are postulates. No established realm ontology, human data,
subject, selected outcome, common subjective scale or physical clock.
"""
import math
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
from verification.zero_spin_constitution_test import close, inner


def phase_state(v,theta):
    w=phase_flip(v)
    return [math.cos(theta)*a+1j*math.sin(theta)*b for a,b in zip(v,w)]


def k_mean(v):
    jv=apply_work(v,J[0]); total=0j
    for a,b,i,r,w in product(range(2),range(2),range(5),range(4),range(16)):
        k=index(a,b,i,r,w)
        total+=v[k].conjugate()*(1-2*((r>>1)&1))*jv[k]
    return total


def work_projection(v,label):
    # Work basis a=0110=6, b=1001=9; a dephased mixture is the SUM
    # of the two unnormalized projected density matrices, not their vector sum.
    return [x if k%16==label else 0j for k,x in enumerate(v)]


def report_probabilities(theta,r):
    # Only a stipulated binary yes/no observation model; not measured reports.
    v_phase=r*math.cos(2*theta)
    v_constant=r
    return (1+v_phase)/2,(1+v_constant)/2


class ConfinementCoherenceExperienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t=joint_state('triple'); cls.p=joint_state('pair')
        cls.thetas=(0,math.pi/8,math.pi/4,3*math.pi/8,math.pi/2)

    def test_unchanged_confined_subsystem_at_every_phase(self):
        base=subject_density(self.t)
        for theta in self.thetas:
            v=phase_state(self.t,theta)
            self.assertAlmostEqual(norm2(v),1)
            close(self,subject_density(v),base)
        # No claim that these qubits are conscious or a physical world.

    def test_actual_asymmetric_sphere_record_table_never_changes(self):
        expected=[(F(3,40),F(1,20)),(F(1,10),F(3,10)),(F(13,40),F(3,20))]
        for theta in self.thetas:
            p=probabilities(phase_state(self.t,theta))
            for i,(plus,minus) in enumerate(expected):
                self.assertAlmostEqual(p[(i,1)],float(plus))
                self.assertAlmostEqual(p[(i,2)],float(minus))

    def test_coherent_joint_relation_varies_while_restriction_stays_fixed(self):
        for theta in self.thetas:
            v=phase_state(self.t,theta)
            self.assertAlmostEqual(k_mean(v).real,math.cos(2*theta))
            self.assertAlmostEqual(k_mean(v).imag,0)
            self.assertAlmostEqual(branch_current(v,0),math.cos(2*theta))
            self.assertAlmostEqual(branch_current(v,1),-math.cos(2*theta))

    def test_interference_effect_disappears_under_full_work_basis_dephasing(self):
        for theta in self.thetas:
            v=phase_state(self.t,theta)
            va=work_projection(v,6); vb=work_projection(v,9)
            self.assertAlmostEqual(norm2(va)+norm2(vb),1)
            # K is off-diagonal in |a>, |b>; dephasing is a mixture.
            self.assertAlmostEqual(abs(k_mean(va)+k_mean(vb)),0)
            self.assertAlmostEqual((1+(k_mean(va)+k_mean(vb)).real)/2,.5)
            # Both retain the same full confined reduced density matrix.
            da=subject_density(va); db=subject_density(vb)
            mix=[[x+y for x,y in zip(rowa,rowb)] for rowa,rowb in zip(da,db)]
            close(self,mix,subject_density(v))
        self.assertAlmostEqual((1+k_mean(phase_state(self.t,0)).real)/2,1)

    def test_k_outcome_probabilities_are_born_probabilities_not_experience(self):
        for theta in self.thetas:
            v=phase_state(self.t,theta)
            # Project (I ± K)/2. Original support obeys K^2=I.
            jv=apply_work(v,J[0]); kv=[]
            for a,b,i,r,w in product(range(2),range(2),range(5),range(4),range(16)):
                k=index(a,b,i,r,w)
                kv.append((1-2*((r>>1)&1))*jv[k])
            plus=[(x+y)/2 for x,y in zip(v,kv)]
            minus=[(x-y)/2 for x,y in zip(v,kv)]
            self.assertAlmostEqual(norm2(plus),math.cos(theta)**2)
            self.assertAlmostEqual(norm2(minus),math.sin(theta)**2)
            self.assertAlmostEqual(norm2(plus)+norm2(minus),1)

    def test_full_receiver_state_and_joint_statistics_preserve_no_signalling(self):
        for theta in self.thetas:
            v=phase_state(self.t,theta); w=phase_state(self.p,theta)
            close(self,local_density(v),local_density(w))
            for ra in (0,1):
                self.assertAlmostEqual(branch_current(v,ra),branch_current(w,ra))
            self.assertAlmostEqual(k_mean(v).real,k_mean(w).real)
        # Equal receiver states are for the declared pair and triple choices.

    def test_counterfactual_experience_rules_differ_on_same_physical_family(self):
        # P and Q are stipulations: e1=+r cos(2θ), e2=-e1 versus
        # e1=+r, e2=-e1. r is a conditional recorded sign, not an outcome rule.
        for theta,r in product(self.thetas,(-1,1)):
            x=r*math.cos(2*theta); rival=r
            self.assertAlmostEqual(x + (-x),0)
            self.assertEqual(rival+(-rival),0)
        self.assertAlmostEqual(math.cos(0),1)
        self.assertAlmostEqual(math.cos(math.pi),-1)

    def test_postulated_report_bridge_separates_the_candidates(self):
        # p_yes=(1+v/kappa)/2, assumed calibrated separately.
        self.assertEqual(report_probabilities(0,1),(1,1))
        p,r=report_probabilities(math.pi/2,1)
        self.assertAlmostEqual(p,0); self.assertAlmostEqual(r,1)
        # Same underlying physical model: no claim actual reports were measured.

    def test_unequal_subject_incidence_breaks_eventwise_pair_balance(self):
        for m1,m2 in ((F(1),F(1)),(F(1),F(2)),(F(2),F(1))):
            for v in (F(-1),F(-1,2),F(0),F(1)):
                total=m1*v+m2*(-v)
                self.assertEqual(total,(m1-m2)*v)
                if v and m1!=m2: self.assertNotEqual(total,0)

    def test_no_time_or_history_derived_from_a_static_parameter_family(self):
        # Endpoints distinguish richer relations while reduced state is equal;
        # calling a particular ordering actual is an independent assumption.
        self.assertNotAlmostEqual(k_mean(phase_state(self.t,0)).real,
                                  k_mean(phase_state(self.t,math.pi/2)).real)
        close(self,subject_density(phase_state(self.t,0)),
              subject_density(phase_state(self.t,math.pi/2)))

if __name__=='__main__': unittest.main()
