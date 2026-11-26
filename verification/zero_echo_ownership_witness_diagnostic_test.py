"""Exact, conditional ownership-report diagnostics on the coherent echo."""
from fractions import Fraction as F
from itertools import product
import unittest
from verification.zero_echo_ownership_witness_diagnostic import (
    compatible_bridges,error_joint,modeled_joint,agreement_bounds,agreement,
)
from verification.zero_ownership_report_bridge import same_under
from verification.zero_stationary_battery_bridge import PREFIX,STATES


class EchoOwnershipWitnessDiagnosticTests(unittest.TestCase):
    def test_existing_bridges_are_opposite_for_every_clock_seed(self):
        for seed in STATES:
            for factor in (1,2):
                x,y=PREFIX[7][seed],PREFIX[10][seed]
                pos=same_under('positive',7,x,10,y,factor)
                neg=same_under('negative',7,x,10,y,factor)
                self.assertEqual(pos,seed[0]==1)
                self.assertEqual(neg,seed[0]==-1)
                self.assertNotEqual(pos,neg)

    def test_ideal_report_on_original_recorded_quantum_branches(self):
        from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
        from verification.zero_relational_chirality_report_test import initial
        from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
        from verification.zero_echo_subject_persistence import copy_initial_j,evolve_record
        from verification.zero_ownership_report_bridge import comparison_report
        from verification.zero_quantum_angular_echo import mass
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            recorded=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            reports=comparison_report(recorded)
            bmass={1:0.,-1:0.};err=0.
            for (z,h),rows in reports.items():
                for part in rows:
                    for i,vec in enumerate(part):
                        b=1 if i>=2 else -1
                        p=mass(((vec,),))/total
                        bmass[b]+=p
                        if h!=b:err+=p
            self.assertAlmostEqual(bmass[1],.5,places=12)
            self.assertAlmostEqual(bmass[-1],.5,places=12)
            self.assertLess(err,1e-22)
        # Neither ownership bridge is used by the physical report circuit.

    def test_compatibility_threshold_and_neither_bridge_control(self):
        f=g=F(1,10)
        self.assertEqual(compatible_bridges(F(9,10),F(1,10),f,g),
                         {'positive':True,'negative':False})
        self.assertEqual(compatible_bridges(F(1,10),F(9,10),f,g),
                         {'positive':False,'negative':True})
        self.assertEqual(compatible_bridges(F(9,10),F(9,10),f,g),
                         {'positive':False,'negative':False})
        for f,g,q in ((F(1,2),F(1,2),F(1,2)),(F(7,10),F(6,10),F(1,2))):
            self.assertGreaterEqual(f+g,1)
            self.assertEqual(compatible_bridges(q,q,f,g),{'positive':True,'negative':True})
        # For f+g<1 the two feasible rectangles are disjoint; for f+g>=1
        # any q in [1-g,f] gives an identical report law for both bridges.
        with self.assertRaises(ValueError):compatible_bridges(2,0,0,0)

    def test_conditional_report_means_do_not_create_the_calibration(self):
        pos=modeled_joint('positive',F(1,10),F(1,10),0)
        neg=modeled_joint('negative',F(1,10),F(1,10),0)
        for data in (pos,neg):
            self.assertEqual(sum(data.values()),1)
            for b,h in product((1,-1),repeat=2):
                marginal=sum(p for (bb,hh,w,o),p in data.items() if bb==b and hh==h)
                expected=F(9,20) if b==h else F(1,20)
                self.assertEqual(marginal,expected)
        # Same calibrated B-report (B,H), distinct hypothetical truth O.
        # W is an extra hypothetical truth-sensitive witness; its access
        # and error calibration are not supplied by (B,H).

    def test_joint_witness_bounds_are_sharp_without_error_independence(self):
        self.assertEqual(agreement_bounds(F(1,10),F(1,10)),(F(4,5),F(1,5)))
        for t in (F(0),F(1,20),F(1,10)):
            pos=modeled_joint('positive',F(1,10),F(1,10),t)
            neg=modeled_joint('negative',F(1,10),F(1,10),t)
            self.assertEqual(agreement(pos),F(4,5)+2*t)
            self.assertEqual(agreement(neg),F(1,5)-2*t)
            # Marginal physical and witness error probabilities are fixed.
            for j in (pos,neg):
                self.assertEqual(sum(p for (b,h,w,o),p in j.items() if h!=b),F(1,10))
                self.assertEqual(sum(p for (b,h,w,o),p in j.items() if w!=o),F(1,10))
        with self.assertRaises(ValueError):error_joint(F(1,10),F(1,10),F(1,5))

    def test_perfectly_correlated_repeat_errors_do_not_average_away(self):
        # In a run choose one shared witness-error bit once: wrong with 1/10,
        # correct with 9/10; all n reports share it. Each individual error
        # rate remains 1/10, yet majority error remains 1/10 for every n.
        for n in (1,3,9,99):
            run_distribution={(0,)*n:F(9,10),(1,)*n:F(1,10)}
            self.assertEqual(sum(p for errors,p in run_distribution.items() if errors[0]),F(1,10))
            self.assertEqual(sum(p for errors,p in run_distribution.items() if sum(errors)>n/2),F(1,10))
        # This does not challenge validity of genuinely independent trials.

if __name__=='__main__':unittest.main()
