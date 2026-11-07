import unittest
from fractions import Fraction as F
import model as m

class ClosureTests(unittest.TestCase):
    def test_01_rod_example(self):self.assertEqual(m.rod_length(10,F(3,5),F(5,4)),8)
    def test_02_rational_boost_family(self):
        for beta,gamma in ((0,1),(F(3,5),F(5,4)),(F(-3,5),F(5,4)),(F(5,13),F(13,12)),(F(8,17),F(17,15))):
            self.assertEqual(m.rod_length(7,beta,gamma),F(7)/gamma)
    def test_03_interval_invariant(self):
        for dt,dx in ((2,3),(0,10),(5,1)):
            t,x=m.boost(dt,dx,F(3,5),F(5,4));self.assertEqual(t*t-x*x,dt*dt-dx*dx)
    def test_04_simultaneity_changes(self):
        t,_=m.boost(0,10,F(3,5),F(5,4));self.assertNotEqual(t,0)
    def test_05_recover_proper_length(self):self.assertEqual(m.rod_length(10,F(3,5),F(5,4))*F(5,4),10)
    def test_06_conditional_posterior(self):self.assertEqual(m.posterior((('u','T',2,F(1,2)),('v','B',3,1)),'T'),F(1,4))
    def test_07_weight_scale_invariance(self):
        a=(('u','T',2,F(1,2)),('v','B',3,1));b=tuple((u,k,7*w,l) for u,k,w,l in a)
        self.assertEqual(m.posterior(a,'T'),m.posterior(b,'T'))
    def test_08_bijective_token_renaming(self):
        a=(('u','T',2,1),('v','B',3,1));b=tuple((u+'new',k,w,l) for u,k,w,l in a)
        self.assertEqual(m.posterior(a,'T'),m.posterior(b,'T'))
    def test_09_measure_preserving_refinement(self):
        a=(('u','T',2,F(1,2)),('v','B',3,1));b=m.refine(a,'u',(F(1,3),F(2,3)))
        self.assertEqual(m.posterior(a,'T'),m.posterior(b,'T'))
    def test_10_zero_evidence_rejected(self):
        with self.assertRaises(ValueError):m.posterior((('u','T',1,0),),'T')
    def test_11_raw_abundance_insufficient(self):self.assertEqual(m.posterior((('many','T',100,F(1,10000)),('few','B',1,1)),'T'),F(1,101))
    def test_12_evidence_mass_dominance(self):
        for a,b in ((1,2),(2,1),(1,1),(0,1)):
            self.assertEqual(m.posterior((('u','T',a,1),('v','B',b,1)),'T')>F(1,2),a>b)
    def test_13_factorization_exists(self):self.assertEqual(m.factor_map({'u':'O','v':'O','w':'P'},{'u':'a','v':'a','w':'b'}),{'O':'a','P':'b'})
    def test_14_factorization_failure(self):
        with self.assertRaises(ValueError):m.factor_map({'u':'O','v':'O'},{'u':'a','v':'b'})
    def test_15_two_material_tags_can_share_factorized_type(self):
        # Logical compatibility witness, not empirical proof of multiple realizability.
        self.assertEqual(m.factor_map({'material_A_token':'O','material_B_token':'O'},{'material_A_token':'a','material_B_token':'a'}),{'O':'a'})
    def test_16_validation(self):
        for call in (lambda:m.boost(0,1,F(3,5),1),lambda:m.rod_length(0,0,1),lambda:m.posterior((('u','T',1,1),('u','T',1,1)),'T'),lambda:m.refine((('u','T',1,1),),'u',(F(1,2),)),lambda:m.factor_map({'u':'O'},{})):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
