import itertools
import unittest
from fractions import Fraction as F
from verification.zero_sphere_relative_orientation import (null_ray,delta,relative_product,mixed_gram_product,z_boost,spatial_reflection)
from verification.zero_sphere_intrinsic_orientation_test import chirality


class RelativeOrientationTests(unittest.TestCase):
    def setUp(self):
        self.ref=[null_ray(0,0),null_ray(1,0),null_ray(2,0)]
        self.plus=self.ref+[null_ray(0,1),null_ray(0,2)]
        self.minus=self.ref+[null_ray(0,1),null_ray(0,-1)]

    def test_exact_physical_null_ray_examples(self):
        self.assertEqual(delta(self.plus[:4]),-16)
        self.assertEqual(delta(self.plus[:3]+self.plus[4:]),-32)
        self.assertEqual(relative_product(self.plus),512)
        self.assertEqual(relative_product(self.minus),-256)
        self.assertEqual(relative_product(self.plus),mixed_gram_product(self.plus))
        self.assertEqual(relative_product(self.minus),mixed_gram_product(self.minus))

    def test_proper_boost_and_parity(self):
        for rays in (self.plus,self.minus):
            P=relative_product(rays)
            self.assertEqual(relative_product([z_boost(v) for v in rays]),P)
            reflected=[spatial_reflection(v) for v in rays]
            self.assertEqual(delta(reflected[:4]),-delta(rays[:4]))
            self.assertEqual(relative_product(reflected),P)

    def test_positive_rescaling_preserves_sign_but_not_magnitude(self):
        scales=[F(2),F(3,2),F(4),F(5),F(7)]
        scaled=[tuple(c*x for x in v) for c,v in zip(scales,self.minus)]
        factor=(scales[0]*scales[1]*scales[2])**2*scales[3]*scales[4]
        self.assertEqual(relative_product(scaled),factor*relative_product(self.minus))
        self.assertLess(relative_product(scaled),0)

    def test_internal_reference_order_and_probe_swap_are_irrelevant(self):
        for order in itertools.permutations(self.ref):
            points=list(order)+self.minus[3:]
            self.assertEqual(relative_product(points),relative_product(self.minus))
        self.assertEqual(relative_product(self.minus[:3]+[self.minus[4],self.minus[3]]),relative_product(self.minus))

    def test_full_five_ray_relabelling_not_a_symmetry_of_partition(self):
        changed=[self.minus[i] for i in (0,1,3,2,4)]
        self.assertEqual(relative_product(changed),256)
        self.assertEqual(relative_product(self.minus),-256)

    def test_crossing_reference_circle_gives_zero(self):
        line=self.ref+[null_ray(0,1),null_ray(3,0)]
        self.assertEqual(relative_product(line),0)
        self.assertEqual(mixed_gram_product(line),0)

    def test_smooth_projective_quantity_and_relative_orientation(self):
        base=[(0,1),(1,1),(2,1)]
        phi=chirality(base+[(1j,1)])
        same=chirality(base+[(2j,1)])
        opposite=chirality(base+[(-1j,1)])
        self.assertAlmostEqual(phi,1/7)
        self.assertAlmostEqual(same,1/8)
        self.assertAlmostEqual(opposite,-1/7)
        self.assertAlmostEqual(phi*same,1/56)
        self.assertAlmostEqual(phi*opposite,-1/49)
        for permutation in itertools.permutations(base):
            self.assertAlmostEqual(chirality(list(permutation)+[(1j,1)])*chirality(list(permutation)+[(-1j,1)]),-1/49)

    def test_reject_invalid_or_past_null_vector(self):
        with self.assertRaises(ValueError): relative_product(self.minus[:4])
        bad=[tuple(-x for x in self.minus[0])]+self.minus[1:]
        with self.assertRaises(ValueError): relative_product(bad)


if __name__=='__main__': unittest.main()
