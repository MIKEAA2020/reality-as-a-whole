"""Joint bridge, positive-witness and correlated-error controls."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_echo_quality_ownership_joint import (
    positive_joint_lower,calibrated_positive,joint_rates,calibrated_joint,
    coupled_bernoulli,synthetic_joint,selected_table,selected_truth_errors)
from verification.zero_echo_quality_bridge_discrimination import structural_value
from verification.zero_joint_quality_incidence_root import R


class JointQualityOwnershipTests(unittest.TestCase):
    def test_correlated_witnesses_same_marginals_different_joint_rate(self):
        tables=[]
        for c in (F(0),F(1,2),F(1)):
            source=synthetic_joint('symmetric','persistent',*[F(1,10)]*6,c)
            self.assertEqual(sum(source.values()),1)
            table=selected_table(source);tables.append(table)
            self.assertEqual(table[1,1]+table[1,0],F(41,50))
            self.assertEqual(table[1,1]+table[0,1],F(9,10))
        self.assertEqual(tables[0][1,1],F(18,25))
        self.assertEqual(tables[-1][1,1],F(41,50))
        # Fréchet-extreme dependence is realized within each actual latent
        # sector. No independence between witnesses is assumed in the bound.

    def test_all_four_joint_bridges_keep_same_physical_source_law(self):
        tables={}
        for q,o in product(('pointer','symmetric'),('persistent','momentary')):
            table=synthetic_joint(q,o,*[F(1,10)]*6,F(1,2))
            tables[q,o]=table
            neutral_same=sum(p for (i,s,h,y,w),p in table.items()
                             if h==-1 and structural_value(i,s,q)==0 and o=='persistent')
            accepted=sum(p for (i,s,h,y,w),p in table.items() if h==-1)
            self.assertEqual(neutral_same/accepted,
                             F(9,10) if (q,o)==('symmetric','persistent') else 0)
        first=tables['pointer','momentary']
        for table in tables.values():
            for i,s,h in product(range(4),(1,-1),(1,-1)):
                self.assertEqual(sum(first[i,s,h,y,w] for y,w in product((0,1),repeat=2)),
                                 sum(table[i,s,h,y,w] for y,w in product((0,1),repeat=2)))
        # Extra correlated witness outputs can depend on bridge assumptions;
        # the state and physical selector do not establish those truth labels.

    def test_positive_lower_bound_for_many_joint_distributions(self):
        rng=np.random.default_rng(511)
        for _ in range(1500):
            # An arbitrary table of true D,O and correlated Y,W. No witness
            # independence or restricted candidate family is assumed.
            p=rng.dirichlet(np.ones(16)).reshape(2,2,2,2)
            p_joint=float(p[1,1,:,:].sum())
            q11=float(p[:,:,1,1].sum())
            d0=float(p[0,:,:,:].sum());o0=float(p[:,0,:,:].sum())
            fy=float(p[0,:,1,:].sum()/d0)
            fw=float(p[:,0,:,1].sum()/o0)
            self.assertLessEqual(positive_joint_lower(q11,fy,fw),p_joint+1e-12)
            qy=float(p[:,:,1,:].sum());qw=float(p[:,:,:,1].sum())
            dy=max(0.,(qy-fy)/(1-fy)) if fy<1 else 0.
            do=max(0.,(qw-fw)/(1-fw)) if fw<1 else 0.
            self.assertLessEqual(max(0.,dy+do-1),p_joint+1e-12)
        self.assertAlmostEqual(positive_joint_lower(.77,.1,.1),.7125)
        self.assertEqual(positive_joint_lower(.9,.6,.4),0.)
        with self.assertRaises(ValueError):positive_joint_lower(1.1,.1,.1)

    def test_same_physical_bypass_does_not_validate_quality_truth(self):
        # A physical channel controlled by R produces this report table. It
        # fits the symmetric truth calibration, but the identical table under
        # the pointer truth has an 82% false-neutral rate after selection.
        channel=synthetic_joint('symmetric','persistent',*[F(1,10)]*6,F(1,2))
        b=selected_truth_errors(channel,'symmetric','persistent')
        a=selected_truth_errors(channel,'pointer','persistent')
        self.assertEqual(b['y_false'],F(1,10))
        self.assertEqual(b['y_miss'],F(1,10))
        self.assertEqual(a['y_false'],F(41,50))
        self.assertIsNone(a['y_miss'])
        # Using a false .1 calibration would incorrectly certify a positive
        # joint prevalence even though pointer/P has no neutral true events.
        q=selected_table(channel)[1,1]
        self.assertEqual(q,F(77,100))
        self.assertGreater(positive_joint_lower(float(q),.1,.1),.7)
        self.assertNotEqual(a['y_false'],F(1,10))
        # Actual first-person evidence or independently warranted reference
        # labels can constrain the bridge; the physical channel cannot alone.

    def test_same_reporter_is_a_required_joint_premise(self):
        # A neutral subject A and a different persistent subject B can each
        # give a true affirmative report, while no one has both properties.
        subjects={'A':{'neutral':True,'same':False},
                  'B':{'neutral':False,'same':True}}
        quality_reporter='A';identity_reporter='B'
        self.assertTrue(subjects[quality_reporter]['neutral'])
        self.assertTrue(subjects[identity_reporter]['same'])
        self.assertFalse(any(v['neutral'] and v['same'] for v in subjects.values()))
        self.assertEqual(positive_joint_lower(1.,0.,0.),1.)
        # Applying that bound here would be invalid: the two target truths do
        # not refer to the same subject and same aligned protocol/window.

    def test_calibrated_four_candidate_examples_and_positive_one_sided(self):
        cal={k:((50000 if k=='p' else 10000),100000)
             for k in ('p','em','ep','fy','gy','fw','gw')}
        expected={('pointer','persistent'):(43,44,862,51),
                  ('pointer','momentary'):(43,44,51,862),
                  ('symmetric','persistent'):(753,54,134,59),
                  ('symmetric','momentary'):(43,767,54,136)}
        for candidate,counts_expected in expected.items():
            table=selected_table(synthetic_joint(*candidate,*[F(1,10)]*6,F(1,2)))
            probabilities=[float(table[k]) for k in ((1,1),(1,0),(0,1),(0,0))]
            counts=tuple(map(int,np.random.default_rng(204204).multinomial(1000,probabilities)))
            self.assertEqual(counts,counts_expected)
            result=calibrated_joint(counts,.05,cal)
            self.assertEqual([c for c,v in result['survive'].items() if v],[candidate])
            if candidate==('symmetric','persistent'):
                self.assertAlmostEqual(result['joint_truth_lower'],.6179169445267578)
                self.assertGreater(result['direct_joint_lower'],result['frechet_joint_lower'])
        # Positive-only procedure uses no miss-rate or selector calibration.
        p=calibrated_positive(753,1000,.05,{'fy':(10000,100000),'fw':(10000,100000)})
        self.assertAlmostEqual(p['joint_truth_lower'],.6305134719802424)
        self.assertGreater(p['joint_truth_lower'],0.)
        # These samples and calibration counts are hypothetical/synthetic;
        # their truth-label premises are not validated by this code.

    def test_validation_and_neither_candidate(self):
        for values in product((F(0),F(1,5),F(1,2),F(1)),repeat=3):
            py,pw,c=values;law=coupled_bernoulli(py,pw,c)
            self.assertEqual(sum(law.values()),1)
            self.assertEqual(law[1,1]+law[1,0],py)
            self.assertEqual(law[1,1]+law[0,1],pw)
            self.assertTrue(all(v>=0 for v in law.values()))
        neither=joint_rates(250,250,250,250,.05,.5,.1,.1,.1,.1,.1,.1)
        self.assertFalse(any(neither['survive'].values()))
        with self.assertRaises(ValueError):calibrated_joint((1,2),.05,{})
        with self.assertRaises(ValueError):calibrated_positive(1,10,.05,{'fy':(1,2)})
        with self.assertRaises(ValueError):joint_rates(0,0,0,0,.05,.5,.1,.1,.1,.1,.1,.1)

if __name__=='__main__':unittest.main()
