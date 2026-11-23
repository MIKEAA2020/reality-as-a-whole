"""Conservation-derived steering, full experience distributions and no-signalling.

These tests concern conditional quantum models and stipulated toy incidence;
none establishes that spin outcomes are experiences or physically fundamental.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_sphere_conservation_born_bridge_test import bridge, ray


def distribution(labels, weights):
    out = Counter()
    for label, weight in zip(labels, weights):
        out[label] += weight
    return out


def fixed_record(setting, seed):
    """Exactly reproduce one pair/triple vs Bob-axis context with 24 seeds."""
    if setting not in ('pair','triple') or not 0 <= seed < 24:
        raise ValueError('invalid setting or seed')
    if setting == 'pair':
        i = seed % 2
        return i, (-1 if i == 0 else 1)
    i, rank = seed % 3, seed // 3
    return i, (1 if rank < (6,3,3)[i] else -1)


class ExperienceSteeringNoSignallingTests(unittest.TestCase):
    def setUp(self):
        rays = [ray(0),ray(2),ray(1),ray(0,1),ray(0,-1)]
        self.relation, self.q, self.dot = bridge(rays)
        self.axis = self.relation['pair'][0]

    def test_prior_signed_zero_does_not_give_full_distribution_no_signalling(self):
        pair = self.relation['pair']
        triple = self.relation['triple']
        values = [-self.dot[self.axis][i] for i in range(5)]
        pair_dist = distribution([values[i] for i in pair], [self.q[i] for i in pair])
        triple_dist = distribution([values[i] for i in triple], [self.q[i] for i in triple])
        self.assertEqual(pair_dist, {F(-1):F(1,2),F(1):F(1,2)})
        self.assertEqual(triple_dist, {F(1,2):F(1,3),F(-1,4):F(2,3)})
        for dist in (pair_dist,triple_dist):
            self.assertEqual(sum(x*p for x,p in dist.items()), 0)
        self.assertTrue(set(pair_dist).isdisjoint(set(triple_dist)))

    def test_generic_triple_weights_forbid_any_half_subset(self):
        for rays in ([ray(0),ray(2),ray(1),ray(0,1),ray(0,-1)],
                     [ray(0),ray(1),ray(3),ray(0,1),ray(0,2)]):
            relation,q,_ = bridge(rays)
            triple = [q[i] for i in relation['triple']]
            self.assertEqual([q[i] for i in relation['pair']], [F(1,2)]*2)
            self.assertEqual(sum(triple),1)
            self.assertTrue(all(0 < w < F(1,2) for w in triple))
            self.assertTrue(all(sum(w for w,include in zip(triple,mask) if include) != F(1,2)
                                for mask in product((False,True),repeat=3)))

    def test_equal_pushforwards_force_constant_labels_on_all_five(self):
        # Exhaustive check for two generic examples; theorem works for arbitrary labels.
        for ws in ([F(1,3)]*3,[F(1,8),F(2,5),F(19,40)]):
            solutions=[]
            for labels in product((-1,0,1),repeat=5):
                if distribution(labels[:2],[F(1,2)]*2) == distribution(labels[2:],ws):
                    solutions.append(labels)
            self.assertEqual(solutions,[(-1,)*5,(0,)*5,(1,)*5])

    def test_single_outcome_probabilities_not_conditional_expectations(self):
        # Bob measures σ along pair axis: P(y=+1|i)=(1−a·n_i)/2.
        triple=self.relation['triple']
        pplus=[(1-self.dot[self.axis][i])/2 for i in triple]
        self.assertEqual(pplus,[F(3,4),F(3,8),F(3,8)])
        self.assertEqual(sum(self.q[i]*p for i,p in zip(triple,pplus)),F(1,2))
        # A definite spin outcome is ±1, not its conditional mean.
        self.assertTrue(all(p not in (0,1) for p in pplus))

    def test_fixed_contextual_records_match_both_joint_distributions(self):
        p = Counter(fixed_record('pair',s) for s in range(24))
        t = Counter(fixed_record('triple',s) for s in range(24))
        self.assertEqual(p,Counter({(0,-1):12,(1,1):12}))
        self.assertEqual(t,Counter({(0,1):6,(0,-1):2,(1,1):3,(1,-1):5,
                                    (2,1):3,(2,-1):5}))
        for counts in (p,t):
            bob=Counter()
            for (_,y),count in counts.items(): bob[y]+=count
            self.assertEqual(bob,Counter({1:12,-1:12}))

    def test_context_dependence_and_seed_access_are_visible(self):
        self.assertEqual(fixed_record('pair',0)[1],-1)
        self.assertEqual(fixed_record('triple',0)[1],1)
        # No-signalling is only at the specified unconditioned seed measure.

    def test_average_zero_is_not_lack_of_negative_local_values(self):
        values=[fixed_record('triple',s)[1] for s in range(24)]
        self.assertEqual(values.count(-1),12)
        self.assertEqual(values.count(1),12)
        self.assertEqual(sum(values),0)


if __name__ == '__main__':
    unittest.main()
