import itertools
import unittest
from fractions import Fraction as F

try:
    from . import zero_total_internal_connection as c
    from . import zero_total_relational_record as m
    from . import zero_total_symmetry_measure as z
except ImportError:
    import zero_total_internal_connection as c
    import zero_total_relational_record as m
    import zero_total_symmetry_measure as z


class InternalConnectionTests(unittest.TestCase):
    def test_full_receipt(self):
        r=c.run()
        self.assertEqual(r['linked_triples'],432)
        self.assertEqual(r['flip_event_fine'],'1/6')
        self.assertEqual(r['flip_event_orbit_uniform'],'1/4')
        self.assertGreater(r['orbit_measure_three_way_total_correlation_nats'],0)

    def test_gauge_fixing_and_residual_diagonal(self):
        for q,r,h in c.TRIPLES:
            fixed=c.transform((q,r,h),c.IDENTITY,h)
            self.assertEqual(fixed,(q,c.act(h,r),c.IDENTITY))
            for g in c.GROUP:
                diagonal=c.transform(fixed,g,g)
                self.assertEqual(diagonal[2],c.IDENTITY)
            for g,k in itertools.product(c.GROUP,repeat=2):
                if c.transform(fixed,g,k)[2]==c.IDENTITY:self.assertEqual(g,k)

    def test_independent_relabelling_invariant_record(self):
        for t in c.TRIPLES:
            for g,k in itertools.product(c.GROUP,repeat=2):
                tt=c.transform(t,g,k)
                self.assertEqual(c.event_class(t),c.event_class(tt))
                self.assertEqual(c.record(t,0)[1],c.record(tt,0)[1])

    def test_link_controls_relative_event(self):
        q=m.STATES[0];r=m.negative(q)
        flip=(q,r,c.IDENTITY)
        signflip=(q,r,((0,1,2),-1))
        self.assertEqual(c.event_class(flip),'flip')
        self.assertEqual(c.event_class(signflip),'stay')
        # These triples have the same labelled endpoints but different
        # gauge-invariant relative content, so not the same gauge orbit.
        self.assertNotIn(signflip,{c.transform(flip,g,k) for g,k in itertools.product(c.GROUP,repeat=2)})

    def test_same_pairwise_marginals_different_triple_event(self):
        first,cf=c.marginals(z.FINE)
        second,co=c.marginals(z.ORBIT)
        self.assertTrue(all(x>0 for x in first.values()))
        self.assertTrue(all(x>0 for x in second.values()))
        self.assertEqual(cf['flip'],F(1,6));self.assertEqual(co['flip'],F(1,4))
        self.assertEqual(sum(first.values()),1);self.assertEqual(sum(second.values()),1)

    def test_record_is_involution_and_bad_input(self):
        for t in c.TRIPLES:
            for b in (0,1):self.assertEqual(c.record(*c.record(t,b)),(t,b))
        with self.assertRaises(ValueError):c.record(c.TRIPLES[0],2)

    def test_all_probability_family_invariant(self):
        for w in (z.FINE,z.ORBIT,z.FIXED_F_MAX,z.FIXED_F_RIVAL):
            for t in c.TRIPLES:
                for g,k in ((c.GROUP[0],c.GROUP[1]),(c.GROUP[3],c.GROUP[7])):
                    self.assertEqual(c.weight(t,w),c.weight(c.transform(t,g,k),w))
            c.marginals(w)

if __name__=='__main__':unittest.main()
