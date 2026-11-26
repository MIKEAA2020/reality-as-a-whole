"""Sharp one-sided witness and plural-subject controls on the actual echo."""
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_echo_positive_unity_witness import (
    SIGNS,CELLS,lower_prevalence,cell_bounds,weighted_lower,report_table,
    uncalibrated_no_witness,observable_marginal,fields,
)
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_typed_echo_process import record_components,joint_quality_slices
from verification.zero_quantum_angular_echo import mass
from verification.zero_persistent_sphere_subject_selection_test import norm2

Q={(1,1):F(4,5),(1,-1):F(3,5),(-1,1):F(1,5),(-1,-1):F(2,5)}
FPR=F(1,10)
WEIGHTS={c:F(1,4) for c in CELLS}


def prevalence(table,c=None):
    return sum((p for (cell,e,y),p in table.items() if e==1 and (c is None or c==cell)),F(0))


def false_positive_joint(table,c):return table[c,0,1]

def absent(table,c):return sum((table[c,0,y] for y in (0,1)),F(0))


class EchoPositiveUnityWitnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_one_sided_bound_is_sharp_and_has_no_false_negative_premise(self):
        grid=[F(i,10) for i in range(11)]
        for q,f,p in product(grid,repeat=3):
            bound=lower_prevalence(q,f)
            if q<=p+f*(1-p):self.assertGreaterEqual(p,bound)
        self.assertEqual(lower_prevalence(F(7,10),F(1,10)),F(2,3))
        self.assertEqual(lower_prevalence(F(1,20),F(1,10)),0)
        self.assertEqual(lower_prevalence(1,1),0)
        self.assertEqual(lower_prevalence(1,0),1)
        # q=0 still allows p=1 with an always-nonpositive report.
        zeros={c:F(0) for c in CELLS}
        self.assertEqual(prevalence(report_table(zeros,0,'all')),1)
        self.assertEqual(prevalence(report_table(zeros,0,'minimal')),0)

    def test_constructive_tables_across_boundary_values(self):
        grid=(F(0),F(1,10),F(1,2),F(9,10),F(1))
        for f in grid:
            for values in product(grid,repeat=4):
                q=dict(zip(CELLS,values))
                for mode in ('minimal','symmetric','all'):
                    table=report_table(q,f,mode)
                    self.assertEqual(sum(table.values()),1)
                    for c in CELLS:
                        self.assertEqual(sum(table[c,e,1] for e in (0,1)),q[c]/4)
                        self.assertLessEqual(false_positive_joint(table,c),f*absent(table,c))
                        self.assertGreaterEqual(min(table[c,e,y] for e in (0,1) for y in (0,1)),0)
                    expected={'minimal':sum(cell_bounds(q,f).values(),F(0))/4,
                              'symmetric':max(cell_bounds(q,f).values()),'all':F(1)}[mode]
                    self.assertEqual(prevalence(table),expected)

    def test_hypothetical_cellwise_bounds_and_symmetric_control(self):
        lb=cell_bounds(Q,FPR)
        self.assertEqual(lb,{(1,1):F(7,9),(1,-1):F(5,9),(-1,1):F(1,9),(-1,-1):F(1,3)})
        self.assertEqual(weighted_lower(Q,FPR,WEIGHTS),F(4,9))
        self.assertEqual(lower_prevalence(sum(Q.values(),F(0))/4,FPR),F(4,9))
        # If latent prevalence is separately assumed invariant across all
        # four cells, the sharp common lower bound is their maximum.
        self.assertEqual(max(lb.values()),F(7,9))
        models={m:report_table(Q,FPR,m) for m in ('minimal','symmetric','all')}
        self.assertEqual(prevalence(models['minimal']),F(4,9))
        self.assertEqual(prevalence(models['symmetric']),F(7,9))
        self.assertEqual(prevalence(models['all']),1)
        for m in models.values():
            self.assertEqual(sum(m.values()),1)
            self.assertEqual(observable_marginal(m),observable_marginal(models['minimal']))
            for c in CELLS:
                self.assertEqual(sum(m[c,e,1] for e in (0,1)),Q[c]/4)
                self.assertLessEqual(false_positive_joint(m,c),FPR*absent(m,c))
        for c in CELLS:self.assertEqual(prevalence(models['symmetric'],c),F(7,36))
        # A symmetric latent prevalence with asymmetric reports requires
        # context-dependent report channels; full report symmetry is not
        # imposed by this particular example.

    def test_stratification_can_improve_the_one_sided_bound(self):
        sparse={c:(F(4,5) if c==(1,1) else F(0)) for c in CELLS}
        self.assertEqual(sum(sparse.values(),F(0))/4,F(1,5))
        self.assertEqual(lower_prevalence(F(1,5),FPR),F(1,9))
        self.assertEqual(weighted_lower(sparse,FPR,WEIGHTS),F(7,36))
        table=report_table(sparse,FPR,'minimal')
        self.assertEqual(prevalence(table),F(7,36))
        self.assertEqual(observable_marginal(table),observable_marginal(report_table(sparse,FPR,'all')))
        # This improvement requires bounds in each cell and an identified
        # reporter population; physical Born weights alone do not provide it.

    def test_without_calibration_same_observables_allow_no_witness(self):
        calibrated=report_table(Q,FPR,'minimal')
        no=uncalibrated_no_witness(Q)
        self.assertEqual(observable_marginal(calibrated),observable_marginal(no))
        self.assertEqual(prevalence(no),0)
        for c in CELLS:self.assertGreater(false_positive_joint(no,c),FPR*absent(no,c))
        # This is an underdetermination construction, not a claim that a
        # real person falsely reports all their experiences.

    def test_physical_cell_weights_are_from_original_complex_echo(self):
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0]);total=norm2(x)
            parts=joint_quality_slices(record_components(x))
            observed={c:0. for c in CELLS}
            for (_,_,_,n,k),rows in parts.items():observed[n,k]+=mass(rows)/total
            for c in CELLS:self.assertAlmostEqual(observed[c],float(WEIGHTS[c]),places=12)
        # The reported Q table is hypothetical; no human experience or
        # physiological response has been extracted from these vectors.

    def test_reporter_witness_does_not_census_private_fields(self):
        for e in (False,True):
            simple=fields('reporter_only',e);nested=fields('nested_private',e)
            self.assertEqual(simple['reporter'],nested['reporter'])
            self.assertEqual(len(simple),1);self.assertEqual(len(nested),3)
            self.assertEqual('K_r' in simple['reporter'],e)
            self.assertTrue(all(a.isdisjoint(b) for a,b in product(nested.values(),repeat=2) if a!=b))
        # Additional tokens and their existence are formal hypotheses;
        # the same reporter's witness need not detect them.

    def test_invalid_weights_and_probability_inputs_are_rejected(self):
        with self.assertRaises(ValueError):lower_prevalence(F(-1,10),FPR)
        with self.assertRaises(ValueError):lower_prevalence(F(1,2),F(11,10))
        with self.assertRaises(ValueError):weighted_lower(Q,FPR,{c:F(1,5) for c in CELLS})
        with self.assertRaises(ValueError):report_table(Q,FPR,'unknown')

if __name__=='__main__':unittest.main()
