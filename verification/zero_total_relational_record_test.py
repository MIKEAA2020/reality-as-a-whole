import itertools
import unittest
from fractions import Fraction as F

try:
    from . import zero_total_relational_record as m
except ImportError:
    import zero_total_relational_record as m


class ZeroTotalRelationalRecordTests(unittest.TestCase):
    def test_receipt(self):
        r=m.run()
        self.assertEqual(r['total_charge_all_states'],0)
        self.assertEqual(r['comparison']['move']['record_one_probability'],'0')
        self.assertEqual(r['comparison']['flip']['record_one_probability'],'1')
        self.assertEqual(r['comparison']['mixture']['record_one_probability'],'2/5')

    def test_exactly_four_pair_orbits(self):
        # Starting with any representative, its orbit equals its category.
        for q,r in itertools.product(m.STATES,repeat=2):
            orbit={(m.symmetry(q,p,s),m.symmetry(r,p,s))
                   for p in m.PERMS for s in (-1,1)}
            expected={(x,y) for x,y in itertools.product(m.STATES,repeat=2)
                      if m.category(x,y)==m.category(q,r)}
            self.assertEqual(orbit,expected)

    def test_each_kernel_symmetric_and_normalized(self):
        for w in [(F(1),F(0),F(0),F(0)),(F(0),F(1),F(0),F(0)),
                  (F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),
                  (F(1,5),F(2,5),F(3,10),F(1,10))]:
            for q in m.STATES:
                self.assertEqual(sum(m.kernel(q,r,w) for r in m.STATES),1)
                for r in m.STATES:
                    self.assertEqual(m.kernel(q,r,w),m.kernel(r,q,w))

    def test_invariant_distribution_unique(self):
        # Transitivity forces every invariant mass to match the reference.
        ref=m.STATES[0]
        self.assertEqual({m.symmetry(ref,p,s) for p in m.PERMS for s in (-1,1)},set(m.STATES))
        self.assertEqual(sum(F(1,6) for _ in m.STATES),1)

    def test_record_reversible_and_symmetry_invariant(self):
        for q,r,b in itertools.product(m.STATES,m.STATES,(0,1)):
            self.assertEqual(m.copy_event(*m.copy_event(q,r,b)),(q,r,b))
            if b==0:self.assertEqual(m.copy_event(q,r,b)[2],int(r==m.negative(q)))
            for p,s in itertools.product(m.PERMS,(-1,1)):
                self.assertEqual(m.copy_event(m.symmetry(q,p,s),m.symmetry(r,p,s),b)[2],
                                 m.copy_event(q,r,b)[2])

    def test_bad_input(self):
        q=m.STATES[0]
        with self.assertRaises(ValueError):m.kernel(q,q,(1,0,0,1))
        with self.assertRaises(ValueError):m.kernel(q,q,(F(-1),F(2),F(0),F(0)))
        with self.assertRaises(ValueError):m.copy_event(q,q,2)
        with self.assertRaises(ValueError):m.category(q,(0,0,0))

if __name__=='__main__':unittest.main()
