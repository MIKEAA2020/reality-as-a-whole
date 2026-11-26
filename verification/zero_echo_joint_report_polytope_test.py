"""Full joint report relaxation; all truth labels are hypothetical."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_echo_joint_report_polytope import STATES,assess,calibrated_assessment,model
from verification.zero_echo_quality_ownership_joint import (
    calibrated_joint,positive_joint_lower,selected_table,synthetic_joint)


def target_statistics(p):
    def mass(test):return sum(v for v,s in zip(p,STATES) if test(*s))
    intervals={key:(v,v) for key,v in {
        'y':mass(lambda d,o,y,w:y),
        'w':mass(lambda d,o,y,w:w),
        'both':mass(lambda d,o,y,w:y and w)}.items()}
    def rate(condition,error):
        den=mass(condition)
        return mass(lambda d,o,y,w:condition(d,o,y,w) and error(d,o,y,w))/den if den else 0.
    bounds=(rate(lambda d,o,y,w:not d,lambda d,o,y,w:y),
            rate(lambda d,o,y,w:d,lambda d,o,y,w:not y),
            rate(lambda d,o,y,w:not o,lambda d,o,y,w:w),
            rate(lambda d,o,y,w:o,lambda d,o,y,w:not w),
            rate(lambda d,o,y,w:d and o,lambda d,o,y,w:not(y and w)))
    truth=mass(lambda d,o,y,w:d and o)
    return intervals,bounds,truth


class JointReportPolytopeTests(unittest.TestCase):
    def test_stronger_joint_constraint_rejects_what_marginals_pass(self):
        cal={k:((50000 if k=='p' else 10000),100000)
             for k in ('p','em','ep','fy','gy','fw','gw','h')}
        counts=(7200,1000,1800,0)
        new=calibrated_assessment(counts,.05,cal)
        old=calibrated_joint(counts,.05,{k:v for k,v in cal.items() if k!='h'})
        self.assertTrue(old['survive']['symmetric','persistent'])
        result=new['candidates']['symmetric','persistent']
        self.assertEqual(result['status'],'rejected')
        self.assertGreater(result['slack'],.016)
        b=new['calibration_bounds']; L=new['sector_lower']
        self.assertAlmostEqual(new['radius'],np.sqrt(np.log(22/.05)/(2*sum(counts))))
        self.assertAlmostEqual(b['h'],.1+np.sqrt(np.log(11/.05)/(2*100000)))
        self.assertGreater(L*(1-b['h']),new['intervals']['both'][1])
        # Without the independently warranted joint calibration the very same
        # three-rate confidence region admits a B/P table.
        free=assess(new['intervals'],b['fy'],b['gy'],b['fw'],b['gw'],1.,L,('symmetric','persistent'))
        self.assertEqual(free['status'],'feasible')
        self.assertEqual(new['general']['status'],'feasible')

    def test_no_extra_candidate_separation_from_correlation_alone(self):
        # Fix exact marginals meeting each candidate's necessary bounds, then
        # sweep the entire Fréchet range of possible observed joint reports.
        for candidate,qy,qw in ((('pointer','persistent'),.08,.92),
                                 (('pointer','momentary'),.08,.08),
                                 (('symmetric','persistent'),.82,.92),
                                 (('symmetric','momentary'),.82,.08)):
            lo=max(0.,qy+qw-1);hi=min(qy,qw)
            for both in np.linspace(lo,hi,11):
                intervals={k:(v,v) for k,v in {'y':qy,'w':qw,'both':both}.items()}
                out=assess(intervals,.1,.1,.1,.1,1.,.9,candidate)
                self.assertEqual(out['status'],'feasible',(candidate,both))

    def test_compatible_correlated_physical_echo_channel(self):
        table=synthetic_joint('symmetric','persistent',*[F(1,10)]*6,F(1))
        sel=selected_table(table)
        self.assertEqual([sel[k] for k in ((1,1),(1,0),(0,1),(0,0))],
                         [F(41,50),F(0),F(2,25),F(1,10)])
        # For neutral D=1, both affirmative with probability .9: h=.1.
        # Do not assume bin ordering; derive neutral sector from actual R.
        from verification.zero_joint_quality_incidence_root import R
        den=sum(p for (i,s,h,y,w),p in table.items() if h==-1 and R[i]==-1)
        fail=sum(p for (i,s,h,y,w),p in table.items()
                 if h==-1 and R[i]==-1 and not(y and w))
        self.assertEqual(fail/den,F(1,10))
        probs=[float(sel[k]) for k in ((1,1),(1,0),(0,1),(0,0))]
        counts=tuple(map(int,np.random.default_rng(204204).multinomial(10000,probs)))
        self.assertEqual(counts,(8198,0,826,976))
        cal={k:((50000 if k=='p' else 10000),100000)
             for k in ('p','em','ep','fy','gy','fw','gw','h')}
        out=calibrated_assessment(counts,.05,cal)
        self.assertEqual([k for k,v in out['candidates'].items() if v['status']=='feasible'],
                         [('symmetric','persistent')])
        self.assertAlmostEqual(out['candidates']['symmetric','persistent']['joint_min'],
                               out['sector_lower'])

    def test_sharper_joint_prevalence_and_witness_constraints(self):
        intervals={k:(v,v) for k,v in {'y':.82,'w':.9,'both':.77}.items()}
        result=assess(intervals,.1,1.,.1,1.,1.)
        self.assertEqual(result['status'],'feasible')
        self.assertAlmostEqual(result['joint_min'],F(133,180))
        self.assertGreater(result['joint_min'],positive_joint_lower(.77,.1,.1))
        # Exact dual certificate for fy=fw=1/10, valid for every atom.
        # E[e_y], E[e_w] <= 0 by the false-positive assumptions.
        for d,o,y,w in STATES:
            ey=(1-d)*(y-F(1,10));ew=(1-o)*(w-F(1,10))
            certificate=(F(d*o-y*w)-F(y+w-2,9)+F(10,9)*(ey+ew))
            self.assertGreaterEqual(certificate,0)
        # Thus t >= q11 + (qy+qw-2)/9 = 133/180. The following
        # rational distribution attains it and saturates both error bounds.
        rational={(0,0,0,0):F(1,20),(0,1,0,1):F(13,100),
                  (0,1,1,1):F(1,50),(1,0,1,0):F(1,20),
                  (1,0,1,1):F(1,90),(1,1,1,1):F(133,180)}
        self.assertEqual(sum(rational.values()),1)
        def total(test):return sum(v for s,v in rational.items() if test(*s))
        self.assertEqual(total(lambda d,o,y,w:y),F(41,50))
        self.assertEqual(total(lambda d,o,y,w:w),F(9,10))
        self.assertEqual(total(lambda d,o,y,w:y and w),F(77,100))
        self.assertEqual(total(lambda d,o,y,w:not d and y),
                         F(1,10)*total(lambda d,o,y,w:not d))
        self.assertEqual(total(lambda d,o,y,w:not o and w),
                         F(1,10)*total(lambda d,o,y,w:not o))
        self.assertEqual(total(lambda d,o,y,w:d and o),F(133,180))
        a,b=model(intervals,.1,1.,.1,1.,1.)
        x=result['witness']
        self.assertLessEqual(np.max(a@x-b),1e-8)
        self.assertAlmostEqual(sum(x),1.)
        self.assertTrue(np.all(x>=-1e-9))
        self.assertAlmostEqual(sum(v for v,(d,o,y,w) in zip(x,STATES) if d and o),
                               result['joint_min'])

    def test_arbitrary_latent_tables_are_never_excluded_by_true_bounds(self):
        rng=np.random.default_rng(73224)
        for _ in range(100):
            p=rng.dirichlet(np.ones(16))
            intervals,bounds,truth=target_statistics(p)
            result=assess(intervals,*bounds)
            self.assertEqual(result['status'],'feasible')
            self.assertLessEqual(result['joint_min'],truth+1e-8)
            self.assertGreaterEqual(result['joint_min']+1e-8,
                                    positive_joint_lower(intervals['both'][0],bounds[0],bounds[2]))

    def test_nonidentical_independent_trials_target_pooled_population(self):
        # Ten deterministic, hence independent, but nonidentical trials. Their
        # pooled table, not each individual conditional rate, is the target.
        chosen=[(1,1,1,1)]*6+[(1,1,0,0)]+[(0,1,0,1)]*2+[(0,0,1,0)]
        p=np.array([chosen.count(s)/len(chosen) for s in STATES])
        intervals,bounds,truth=target_statistics(p)
        result=assess(intervals,*bounds)
        self.assertEqual(result['status'],'feasible')
        self.assertLessEqual(result['joint_min'],truth+1e-9)
        # Within-trial Y and W are allowed arbitrary dependence. Reference
        # means must still transfer to these pooled conditional target errors.

    def test_edge_cases_and_validation(self):
        I={k:(0.,1.) for k in ('y','w','both')}
        for q,o in product(('pointer','symmetric'),('persistent','momentary')):
            self.assertEqual(assess(I,0.,0.,0.,0.,0.,.9,(q,o))['status'],'feasible')
        # A vacuous joint reference condition is not an error.
        self.assertEqual(assess({'y':(0.,0.),'w':(0.,0.),'both':(0.,0.)},
                                0.,0.,0.,0.,0.,.9,('pointer','momentary'))['status'],'feasible')
        with self.assertRaises(ValueError):assess(I,0.,0.,0.,0.,-1.)
        with self.assertRaises(ValueError):assess(I,0.,0.,0.,0.,0.,candidate=('missing','persistent'))
        with self.assertRaises(ValueError):assess({'y':(0.,1.)},0.,0.,0.,0.,0.)
        with self.assertRaises(ValueError):calibrated_assessment((1,2,3,4),.05,{})

if __name__=='__main__':unittest.main()
