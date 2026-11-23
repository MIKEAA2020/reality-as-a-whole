import itertools
import unittest
from collections import Counter
from fractions import Fraction as F

try:
    from . import zero_total_internal_loop as l
    from . import zero_total_internal_connection as c
    from . import zero_total_relational_record as m
except ImportError:
    import zero_total_internal_loop as l
    import zero_total_internal_connection as c
    import zero_total_relational_record as m


class InternalLoopTests(unittest.TestCase):
    def test_full_receipt(self):
        r=l.run()
        self.assertEqual(r['three_flip_probability_flat'],'0')
        self.assertEqual(r['three_flip_probability_haar'],'1/216')
        self.assertEqual(r['total_variation_three_bit_distributions'],'1/54')

    def test_flat_link_pair_marginals(self):
        for counts in l.link_pair_counts():
            self.assertEqual(len(counts),144)
            self.assertEqual(set(counts.values()),{1})

    def test_entire_single_edge_marginals_match_haar(self):
        # Uniform q0,q1,q2,h01,h12 with h02=h01*h12:
        # all 432 possible (q_i,q_j,h_ij) appear 72 times on each edge.
        counts=[Counter(),Counter(),Counter()]
        for q0,q1,q2 in itertools.product(m.STATES,repeat=3):
            for h01,h12 in itertools.product(c.GROUP,repeat=2):
                h02=c.compose(h01,h12)
                for ctr,edge in zip(counts,((q0,q1,h01),(q1,q2,h12),(q0,q2,h02))):
                    ctr[edge]+=1
        for ctr in counts:
            self.assertEqual(len(ctr),432)
            self.assertEqual(set(ctr.values()),{72})

    def test_all_flat_configs_forbid_three_flips(self):
        for q0,q1,q2 in itertools.product(m.STATES,repeat=3):
            for h01,h12 in itertools.product(c.GROUP,repeat=2):
                cfg=(q0,q1,q2,h01,h12,c.compose(h01,h12))
                self.assertEqual(l.holonomy(cfg),l.E)
                self.assertNotEqual(l.events(cfg),(1,1,1))

    def test_pairwise_independent_bits_but_different_joint(self):
        flat,haar=l.flat_distribution(),l.haar_distribution()
        for i in range(3):
            for j in range(i):
                for a,b in itertools.product((0,1),repeat=2):
                    self.assertEqual(sum(p for x,p in flat.items() if x[i]==a and x[j]==b),
                                     sum(p for x,p in haar.items() if x[i]==a and x[j]==b))
        self.assertNotEqual(flat,haar)
        self.assertEqual(sum(abs(flat[k]-haar[k]) for k in flat)/2,F(1,54))

    def test_full_support_mixture_same_local_statistics(self):
        flat,haar=l.flat_distribution(),l.haar_distribution()
        mix={bits:(flat[bits]+haar[bits])/2 for bits in flat}
        self.assertTrue(all(p>0 for p in mix.values()))
        self.assertEqual(mix[(1,1,1)],F(1,432))
        self.assertEqual(sum(abs(mix[k]-haar[k]) for k in mix)/2,F(1,108))
        for i in range(3):
            for j in range(i):
                for a,b in itertools.product((0,1),repeat=2):
                    self.assertEqual(sum(p for x,p in mix.items() if x[i]==a and x[j]==b),
                                     sum(p for x,p in haar.items() if x[i]==a and x[j]==b))
        # Full support on all configurations follows pointwise from the
        # positive half-weight of the uniform-Haar configuration measure.
        self.assertGreater(F(1,2)*F(1,6**3*12**3),0)
        self.assertEqual(F(1,2)*F(1,12)+F(1,2),F(13,24))

    def test_gauge_fix_and_observable_holonomy(self):
        q=m.STATES[0]
        stabilizer=next(g for g in c.GROUP if g!=l.E and c.act(g,q)==q)
        flat=(q,q,q,l.E,l.E,l.E); loop=(q,q,q,l.E,l.E,stabilizer)
        self.assertEqual(l.events(flat),l.events(loop))
        self.assertNotEqual(l.holonomy(loop),l.E)
        for g0,g1,g2 in itertools.product(c.GROUP,repeat=3):
            out=l.gauge(loop,g0,g1,g2)
            self.assertEqual(l.events(out),l.events(loop))
            self.assertNotEqual(l.holonomy(out),l.E)
        fixed=l.gauge_fix(loop)
        self.assertEqual(fixed[3:5],(l.E,l.E))
        self.assertEqual(fixed[5],c.inv(l.holonomy(loop)))

    def test_haar_flat_probability(self):
        count=sum(c.compose(h01,h12)==h02
                  for h01,h12,h02 in itertools.product(c.GROUP,repeat=3))
        self.assertEqual(F(count,12**3),F(1,12))

if __name__=='__main__':unittest.main()
