import itertools
import math
import unittest
from fractions import Fraction as F

try:
    from . import zero_total_symmetry_measure as z
    from . import zero_total_relational_record as m
except ImportError:
    import zero_total_symmetry_measure as z
    import zero_total_relational_record as m


class SymmetryMeasureTests(unittest.TestCase):
    def test_receipt(self):
        r=z.run()
        self.assertEqual(r['fine_uniform_flip_probability'],'1/6')
        self.assertEqual(r['orbit_uniform_flip_probability'],'1/4')
        self.assertEqual(r['ordered_pair_orbit_sizes'],{'stay':6,'flip':6,'move':12,'both_moved':12})
        self.assertEqual(r['stay_probabilities_maxentropy_and_rival'],
                         [str(z.FIXED_F_MAX[0]),str(z.FIXED_F_RIVAL[0])])

    def test_flip_needs_shared_relational_identification(self):
        q=m.STATES[0]; r=m.negative(q)
        self.assertEqual(m.category(q,r),'flip')
        transformed=next(m.symmetry(r,p,1) for p in m.PERMS if m.symmetry(r,p,1)==q)
        self.assertEqual(m.category(q,transformed),'stay')
        for p,s in itertools.product(m.PERMS,(-1,1)):
            self.assertEqual(m.category(m.symmetry(q,p,s),m.symmetry(r,p,s)),'flip')

    def test_fine_joint_is_exactly_uniform(self):
        for q,r in itertools.product(m.STATES,repeat=2):
            self.assertEqual(F(1,6)*m.kernel(q,r,z.FINE),F(1,36))

    def test_orbit_classes_are_uniform(self):
        for cat in z.CATS:
            total=sum(F(1,6)*m.kernel(q,r,z.ORBIT)
                      for q,r in itertools.product(m.STATES,repeat=2)
                      if m.category(q,r)==cat)
            self.assertEqual(total,F(1,4))

    def test_same_full_support_and_symmetries(self):
        for q,r in itertools.product(m.STATES,repeat=2):
            self.assertGreater(m.kernel(q,r,z.FINE),0)
            self.assertGreater(m.kernel(q,r,z.ORBIT),0)
            for perm,sgn in itertools.product(m.PERMS,(-1,1)):
                for w in (z.FINE,z.ORBIT):
                    self.assertEqual(m.kernel(q,r,w),m.kernel(m.symmetry(q,perm,sgn),m.symmetry(r,perm,sgn),w))

    def test_entropy_is_coarse_graining_dependent(self):
        self.assertAlmostEqual(z.entropy(z.conditional_distribution(z.FINE)),math.log(6))
        self.assertAlmostEqual(z.entropy(z.ORBIT),math.log(4))
        self.assertGreater(z.entropy(z.conditional_distribution(z.FINE)),z.entropy(z.conditional_distribution(z.ORBIT)))
        self.assertGreater(z.entropy(z.ORBIT),z.entropy(z.FINE))

    def test_fixed_flip_max_entropy_over_rational_grid(self):
        # A grid is a numerical check, not the analytic uniqueness proof.
        for p in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            maximum=z.entropy(z.conditional_distribution(z.fixed_flip_max(p)))
            for i in range(9):
                for j in range(9-i):
                    a=(1-p)*F(i,8); c=(1-p)*F(j,8); d=1-p-a-c
                    w=(a,p,c,d)
                    self.assertLessEqual(z.entropy(z.conditional_distribution(w)),maximum+1e-12)

    def test_flip_record_law_not_identifying_full_kernel(self):
        for n in range(5):
            for word in itertools.product((0,1),repeat=n):
                self.assertEqual(z.flip_word_probability(z.FIXED_F_MAX,word),F(1,2**n))
                self.assertEqual(z.flip_word_probability(z.FIXED_F_RIVAL,word),F(1,2**n))
        self.assertNotEqual(z.FIXED_F_MAX[0],z.FIXED_F_RIVAL[0])

    def test_input_bounds(self):
        with self.assertRaises(ValueError): z.fixed_flip_max(F(6,5))
        with self.assertRaises(ValueError): z.entropy([F(2),F(-1)])
        with self.assertRaises(ValueError): z.flip_word_probability(z.FINE,[2])

if __name__=='__main__':unittest.main()
