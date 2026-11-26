"""Selected-sector quality-bridge test on the original recorded echo."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_echo_quality_bridge_discrimination import (
    structural_value,selected_neutral_lower,compatible_report_ranges,
    finite_witness,calibrated_finite,synthetic_joint)
from verification.zero_joint_quality_incidence_root import R,weight,quality
from verification.zero_echo_joint_identity_balance import EVENTS
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_echo_subject_persistence import copy_initial_j,evolve_record
from verification.zero_ownership_report_bridge import comparison_report
from verification.zero_quantum_angular_echo import mass


def selected_probability(table,condition):
    den=sum(p for (i,s,h,y),p in table.items() if h==-1)
    num=sum(p for key,p in table.items() if key[2]==-1 and condition(*key))
    return num/den


class QualityBridgeDiscriminationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_two_bridges_share_physical_events_but_differ_on_negative_sector(self):
        categories={}
        for bridge in ('pointer','symmetric'):
            out={-1:F(0),0:F(0),1:F(0)}
            for i,s in EVENTS:
                val=structural_value(i,s,bridge)
                out[(val>0)-(val<0)]+=weight(i,s)
                if R[i]==1:
                    self.assertEqual(structural_value(i,s,'pointer'),
                                     structural_value(i,s,'symmetric'))
                else:
                    self.assertNotEqual(structural_value(i,s,'pointer'),0)
                    self.assertEqual(structural_value(i,s,'symmetric'),0)
            categories[bridge]=out
        self.assertEqual(categories['pointer'],{-1:F(1,2),0:F(0),1:F(1,2)})
        self.assertEqual(categories['symmetric'],{-1:F(1,4),0:F(1,2),1:F(1,4)})
        # Neutral here is a stipulated structural category, not absence of
        # experience or a claim that a physical sign is felt valence.

    def test_sector_report_and_bridge_categories_on_original_quantum_vectors(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            saved=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            report=comparison_report(saved)
            for z,h in product((1,-1),(1,-1)):
                rows=report[z,h]
                for i in range(4):
                    p=sum(mass(((part[i],),)) for part in rows)/total
                    if p<1e-24:continue
                    self.assertEqual(h,R[i])
                    self.assertEqual((structural_value(i,s,'symmetric')==0),h==-1)
                    self.assertNotEqual(structural_value(i,s,'pointer'),0)
            # The report is physical parity zJ; no first-person witness is
            # supplied by the circuit or certified by this test.

    def test_sector_lower_bound_is_sharp_and_monotone(self):
        self.assertAlmostEqual(selected_neutral_lower(.5,.1,.1),.9)
        for pl,em,ep in product((.2,.5,.8,1.),(.0,.1,.4),(.0,.1,.5)):
            bound=selected_neutral_lower(pl,em,ep)
            for p in (pl,(pl+1)/2,1.):
                for a,b in product((0.,em),(0.,ep)):
                    den=p*(1-a)+(1-p)*b
                    if den<=0:continue
                    actual=p*(1-a)/den
                    self.assertGreaterEqual(actual+1e-14,bound)
            if pl<1 and ep>0:
                self.assertAlmostEqual(pl*(1-em)/(pl*(1-em)+(1-pl)*ep),bound)
        self.assertEqual(selected_neutral_lower(0.,.1,.1),0.)
        self.assertEqual(selected_neutral_lower(.5,1.,0.),0.)
        with self.assertRaises(ValueError):selected_neutral_lower(.5,-.1,.1)

    def test_same_physical_table_and_synthetic_joint_channels(self):
        args=(F(1,10),)*4
        a=synthetic_joint('pointer',*args)
        b=synthetic_joint('symmetric',*args)
        self.assertEqual(sum(a.values()),1)
        self.assertEqual(sum(b.values()),1)
        for i,s,h in product(range(4),(1,-1),(1,-1)):
            self.assertEqual(sum(a[i,s,h,y] for y in (0,1)),
                             sum(b[i,s,h,y] for y in (0,1)))
        self.assertEqual(selected_probability(a,lambda i,s,h,y:y==1),F(1,10))
        self.assertEqual(selected_probability(b,lambda i,s,h,y:y==1),F(41,50))
        self.assertEqual(selected_probability(b,lambda i,s,h,y:R[i]==-1),F(9,10))
        bounds=compatible_report_ranges(.5,.1,.1,.1,.1)
        self.assertAlmostEqual(bounds['sector_lower'],.9)
        self.assertAlmostEqual(bounds['pointer_upper'],.1)
        self.assertAlmostEqual(bounds['symmetric_lower'],.81)

    def test_selection_can_destroy_separation_despite_informative_witness(self):
        # Bounds f=.81,g=.1 give f+g=.91<1, but sector lower=.9 makes
        # f = L(1-g), so conditional predictions can meet at q=.81.
        a=synthetic_joint('pointer',F(1,10),F(1,10),F(81,100),F(1,10))
        b=synthetic_joint('symmetric',F(1,10),F(1,10),F(0),F(1,10))
        qa=selected_probability(a,lambda i,s,h,y:y==1)
        qb=selected_probability(b,lambda i,s,h,y:y==1)
        self.assertEqual(qa,F(81,100));self.assertEqual(qb,qa)
        bounds=compatible_report_ranges(.5,.1,.1,.81,.1)
        self.assertAlmostEqual(bounds['pointer_upper'],bounds['symmetric_lower'])
        self.assertLess(.81+.1,1.)
        # Actual channels may have errors below bounds and can differ across
        # interpretations; physical marginal distributions remain identical.

    def test_six_way_calibration_confidence_budget(self):
        # Hypothetical balanced physical labels and four 10% error batches.
        cal={'p':(50000,100000),'e_minus':(10000,100000),
             'e_plus':(10000,100000),'f':(10000,100000),'g':(10000,100000)}
        a=calibrated_finite(86,1000,.05,cal)
        b=calibrated_finite(834,1000,.05,cal)
        self.assertGreater(a['calibration_bounds']['e_minus'],.1)
        self.assertLess(a['calibration_bounds']['p'],.5)
        self.assertTrue(a['reject_symmetric']);self.assertFalse(a['reject_pointer'])
        self.assertTrue(b['reject_pointer']);self.assertFalse(b['reject_symmetric'])
        self.assertAlmostEqual(a['total_delta'],.05)
        # Without an error-rate reference the protocol aborts; it does not
        # replace a missing calibration with an asserted perfect channel.
        with self.assertRaises(ValueError):calibrated_finite(1,10,.05,{'p':(1,2)})
        with self.assertRaises(ValueError):calibrated_finite(1,10,.05,{k:(0,0) for k in cal})

    def test_finite_shot_synthetic_examples_and_neither_candidate(self):
        for bridge,p,expected in (('pointer',.1,86),('symmetric',.82,834)):
            rng=np.random.default_rng(202711)
            k=int(rng.binomial(1000,p));self.assertEqual(k,expected)
            result=finite_witness(k,1000,.05,.5,.1,.1,.1,.1)
            self.assertEqual(result['reject_pointer'],bridge=='symmetric')
            self.assertEqual(result['reject_symmetric'],bridge=='pointer')
        both=finite_witness(400,1000,.05,.5,.1,.1,.1,.1)
        self.assertTrue(both['reject_pointer']);self.assertTrue(both['reject_symmetric'])
        with self.assertRaises(ValueError):finite_witness(1,0,.05,.5,.1,.1,.1,.1)
        # These are simulated outcomes conditional on synthetic error channels,
        # not observed reports or independent validation of their assumptions.

if __name__=='__main__':unittest.main()
