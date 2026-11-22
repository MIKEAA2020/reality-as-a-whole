import itertools
import unittest
from fractions import Fraction as F
from positive_experience_witness_gate import lower_witness_prevalence, arbitrary_dependence_tail, independent_tail


class WitnessTests(unittest.TestCase):
    def test_positive_only_bound_and_attainment(self):
        a=F(1,10); p=F(2,3); q=p+(1-p)*a
        self.assertEqual(q,F(7,10))
        self.assertEqual(lower_witness_prevalence(q,a),p)
        self.assertEqual(lower_witness_prevalence(F(1,20),a),0)
        self.assertEqual(lower_witness_prevalence(1,a),1)

    def test_endpoint_grid_all_channels(self):
        # Exhaust finite rational distributions; false-negative rates are unrestricted.
        for p, a, s, f in itertools.product((F(0),F(1,4),F(1,2),F(3,4),F(1)),
                                             (F(0),F(1,4),F(1,2),F(3,4)),
                                             (F(0),F(1,2),F(1)),
                                             (F(0),F(1,4),F(1,2),F(3,4),F(1))):
            if f>a: continue
            q=p*s+(1-p)*f
            self.assertLessEqual(lower_witness_prevalence(q,a),p)

    def test_sharp_dependent_witness(self):
        # Enumerate a smaller exact version: n=6, k=4, alpha=1/6.
        n,k=6,4; a=F(1,6); p=arbitrary_dependence_tail(n,k,a)
        choices=list(itertools.combinations(range(n),k))
        self.assertEqual(p,F(1,4))
        for i in range(n):
            self.assertEqual(sum((p/F(len(choices)) for c in choices if i in c),F()),a)
        self.assertEqual(sum((p/F(len(choices)) for _ in choices),F()),p)
        self.assertEqual(arbitrary_dependence_tail(30,16,F(1,10)),F(3,16))

    def test_saturation_and_independent_bound(self):
        self.assertEqual(arbitrary_dependence_tail(4,2,F(3,4)),1)
        self.assertEqual(independent_tail(3,2,F(1,2)),F(1,2))
        self.assertLess(independent_tail(30,16,F(1,10)),F(1,100000000))

    def test_bad_inputs(self):
        with self.assertRaises(ValueError): lower_witness_prevalence(1,1)
        with self.assertRaises(ValueError): arbitrary_dependence_tail(5,6,F(1,10))
        with self.assertRaises(ValueError): independent_tail(5,2,F(-1,10))

if __name__=='__main__': unittest.main()
