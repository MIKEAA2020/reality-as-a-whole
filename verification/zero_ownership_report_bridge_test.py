"""Actual echo reporting instrument, ownership bridges and negative controls."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_quantum_angular_echo import mass,difference_mass
from verification.zero_stationary_battery_bridge import STATES,PREFIX,advance
from verification.zero_sphere_angular_echo import magnitude
from verification.zero_joint_quality_incidence_root import ANGLES
from verification.zero_stationary_subject_incidence import stationary_flip
from verification.zero_dressed_history_pair import encode_pair
from verification.zero_dressed_sphere_rotations import build_frames
from verification.zero_echo_subject_persistence import (
    copy_initial_j,evolve_record,record_fidelity,
)
from verification.zero_ownership_report_bridge import (
    hybrid_owner,same_under,owner_census,comparison_report,type_swap_saved,sector_exchange_saved,noisy_bit_kraus,erase_saved_by_report,
    erase_b_report,noisy_joint,report_agreement,
)


class OwnershipReportBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_hybrid_rules_on_entire_reduced_clock_and_symmetries(self):
        for policy,t,seed,factor in product(('positive','negative'),range(20),STATES,(1,2)):
            x=PREFIX[t][seed];y=advance(t,x);u=(t+1)%20
            x_id=hybrid_owner(policy,t,x,factor)
            y_id=hybrid_owner(policy,u,y,factor)
            persistent=seed[0]==(1 if policy=='positive' else -1)
            self.assertEqual(x_id==y_id,persistent)
            # Reduced physical type and sign transformations keep B fixed.
            flipped=stationary_flip(t,x);next_flipped=stationary_flip(u,y)
            self.assertEqual(same_under(policy,t,flipped,u,next_flipped,factor),persistent)
            b,j,r,s=x;bb,jj,rr,ss=y
            self.assertEqual(same_under(policy,t,(b,j,r,-s),u,(bb,jj,rr,-ss),factor),persistent)
        for seed in STATES:
            x,y=PREFIX[7][seed],PREFIX[10][seed]
            self.assertNotEqual(same_under('positive',7,x,10,y),same_under('negative',7,x,10,y))

    def test_hypothetical_equal_subject_census_does_not_recover_physical_weights(self):
        expected={'positive':({1:2,-1:80},F(1,41)),
                  'negative':({1:40,-1:4},F(10,11))}
        for policy,(counts,fraction) in expected.items():
            c,w=owner_census(policy)
            self.assertEqual(c,counts)
            self.assertEqual(F(c[1],sum(c.values())),fraction)
            self.assertEqual(w,{1:F(1,2),-1:F(1,2)})
        # This census explicitly postulates simultaneous actual subjects for
        # all supported seed alternatives. It is not the Born event measure.

    def test_reversible_comparison_is_real_echo_R_and_B_report(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            record=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            report=comparison_report(record)
            distribution={r:sum(mass(report[z,r]) for z in (1,-1))/total for r in (1,-1)}
            self.assertAlmostEqual(distribution[1],.5,places=12)
            self.assertAlmostEqual(distribution[-1],.5,places=12)
            for (z,r),rows in report.items():
                for i in range(4):
                    b=-1 if i<2 else 1
                    for ri,old in zip((1,-1),rows):
                        p=mass(((old[i],),))/total
                        if p>1e-24:
                            self.assertEqual(r,b)
                            self.assertEqual(r,ri)
            # This report can also be obtained from existing R on support;
            # it is a physical comparison, not a subject-identity detector.

    def test_new_saved_record_breaks_bare_type_swap_but_dressing_repairs_it(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            saved=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            bare=type_swap_saved(saved,s,False)
            dressed=type_swap_saved(saved,s,True)
            self.assertGreater(sum(difference_mass(bare[z],saved[z]) for z in (1,-1))/total,.9)
            self.assertLess(sum(difference_mass(dressed[z],saved[z]) for z in (1,-1))/total,1e-22)
            bare_report=comparison_report(bare)
            dressed_report=comparison_report(dressed)
            self.assertAlmostEqual(sum(mass(bare_report[z,1]) for z in (1,-1))/total,1,places=12)
            self.assertAlmostEqual(sum(mass(dressed_report[z,1]) for z in (1,-1))/total,.5,places=12)
            original=comparison_report(saved)
            self.assertLess(sum(difference_mass(dressed_report[k],original[k]) for k in original)/total,1e-22)
        # Bare type symmetry loses the L--J correlation.  Flip L when R is
        # negative to repair this physical symmetry; do not erase signs.

    def test_active_sector_exchange_breaks_b_dependent_owner_covariance(self):
        shape,frames,_=build_frames()
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            saved=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            moved=sector_exchange_saved(saved,s,frames,shape)
            self.assertLess(sum(difference_mass(moved[z],saved[z]) for z in (1,-1))/total,1e-21)
            # Sector exchange maps the 0-bin B=- to the 2-bin B=+ and back.
            # Thus either B-dependent proposal changes whether the 7 and 10
            # slots have the same owner, even though this state is stabilized.
            minus=(-1,-1,1,s);plus=(1,1,1,s)
            for policy in ('positive','negative'):
                a=same_under(policy,7,PREFIX[7][minus],10,PREFIX[10][minus])
                b=same_under(policy,7,PREFIX[7][plus],10,PREFIX[10][plus])
                self.assertNotEqual(a,b)
        self.assertEqual(magnitude(ANGLES[0],'swap_invariant'),F(3,16))
        self.assertEqual(magnitude(ANGLES[2],'swap_invariant'),F(5,16))
        # The map changes B, magnitude and the report observable; requiring
        # it as identity-preserving is an additional physical assumption.

    def test_dressed_record_and_constrained_pair_transform_together(self):
        for label,s in product((0,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            saved=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            dressed=type_swap_saved(saved,s,True)
            for z,i in product((1,-1),range(4)):
                b=-1 if i<2 else 1
                newi=1-i if i<2 else i
                before=encode_pair((saved[z][0][i],saved[z][1][i]),i,s)
                after=encode_pair((dressed[b*z][0][newi],dressed[b*z][1][newi]),newi,s)
                for (a,c,z1,z2),part in before.items():
                    m=sum(mass(((v,),)) for v in part)/total
                    if m<1e-24:continue
                    target=(newi,newi,b*z1,b*z2)
                    self.assertIn(target,after)
                    self.assertAlmostEqual(sum(mass(((v,),)) for v in after[target])/total,m,places=12)
                    self.assertEqual(z1,s*z)
                    self.assertEqual(target[2],s*b*z)
        # Pair sign switches on R=-, while comparison bit stays fixed.

    def test_noise_channel_is_a_complete_physical_instrument(self):
        for eta in (F(1,2),F(9,10),F(1)):
            kraus=noisy_bit_kraus(eta)
            np.testing.assert_allclose(sum(k.T.conj()@k for k in kraus),np.eye(2),atol=1e-13)
            for bit in (0,1):
                rho=np.diag([1.,0.]) if bit==0 else np.diag([0.,1.])
                final=sum(k@rho@k.T.conj() for k in kraus)
                self.assertAlmostEqual(final[bit,bit],float(eta),places=13)
                self.assertAlmostEqual(final[1-bit,1-bit],float(1-eta),places=13)

    def test_retained_report_decoheres_b_then_full_unitary_reset_recovers_state(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            record=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            report=comparison_report(record)
            closed=evolve_record(report,('T','Q','T'))
            erased=erase_saved_by_report(closed)
            for r in (1,-1):self.assertLess(mass(erased[-1,r])/total,1e-23)
            kept={r:erased[1,r] for r in (1,-1)}
            self.assertAlmostEqual(record_fidelity(kept,states[0]),.5,places=12)
            reset=erase_b_report(kept)
            self.assertLess(mass(reset[-1])/total,1e-23)
            self.assertLess(difference_mass(reset[1],states[0])/total,1e-23)
        # Reset destroys the comparison report; neither operation proves
        # experiential ownership, and the report register is an extra input.

    def test_noisy_bridge_is_discriminating_only_with_a_truth_interface(self):
        for eta in (F(1,2),F(9,10),F(1)):
            plus=noisy_joint('positive',eta);minus=noisy_joint('negative',eta)
            self.assertEqual(sum(plus.values()),1)
            self.assertEqual(sum(minus.values()),1)
            self.assertEqual(report_agreement('positive',eta),eta)
            self.assertEqual(report_agreement('negative',eta),1-eta)
            for r in (1,-1):
                # Same physical report distribution under both bridges.
                self.assertEqual(sum(plus[a,r] for a in (False,True)),F(1,2))
                self.assertEqual(sum(minus[a,r] for a in (False,True)),F(1,2))
            # Both same-owner marginals are 1/2. At eta=1/2 even their
            # joint truth/report distributions coincide.
            for a in (False,True):
                self.assertEqual(sum(plus[a,r] for r in (1,-1)),F(1,2))
                self.assertEqual(sum(minus[a,r] for r in (1,-1)),F(1,2))
        self.assertEqual(noisy_joint('positive',F(1,2)),noisy_joint('negative',F(1,2)))
        self.assertNotEqual(noisy_joint('positive',F(9,10)),noisy_joint('negative',F(9,10)))

if __name__=='__main__':unittest.main()
