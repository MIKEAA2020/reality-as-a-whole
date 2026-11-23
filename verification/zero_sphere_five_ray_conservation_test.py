import itertools
import unittest
from fractions import Fraction as F
from verification.zero_sphere_relative_orientation import null_ray, delta, relative_product, z_boost, spatial_reflection, lorentz_dot
from verification.zero_sphere_five_ray_conservation import cofactor_null_relation, add, scale, total_pair_momentum, center_frame_energy_numerators


class FiveRayConservationTests(unittest.TestCase):
    def setUp(self):
        self.rays=[null_ray(0,0),null_ray(1,0),null_ray(2,0),null_ray(0,1),null_ray(0,-1)]

    def test_unique_generic_partition_and_exact_momentum_conservation(self):
        result=cofactor_null_relation(self.rays)
        self.assertEqual(result['coefficients'],[48,-32,16,-16,-16])
        self.assertEqual(result['pair'],[0,2])
        self.assertEqual(result['triple'],[1,3,4])
        c=[x/16 for x in result['coefficients']]
        P=total_pair_momentum(self.rays,c,result['pair'])
        self.assertEqual(P,(8,4,0,0))
        self.assertEqual(P,add([scale(-c[i],self.rays[i]) for i in result['triple']]))
        self.assertEqual(-lorentz_dot(P,P),48)

    def test_partition_does_not_depend_on_ray_label_order(self):
        for order in itertools.permutations(range(5)):
            reordered=[self.rays[i] for i in order]
            result=cofactor_null_relation(reordered)
            self.assertEqual({order[i] for i in result['pair']},{0,2})
            self.assertEqual({order[i] for i in result['triple']},{1,3,4})

    def test_positive_projective_rescaling_and_frame_changes(self):
        scales=list(map(F,[2,3,5,7,11]))
        scaled=[scale(c,k) for c,k in zip(scales,self.rays)]
        for transformed in (scaled,[z_boost(k) for k in self.rays],[spatial_reflection(k) for k in self.rays]):
            result=cofactor_null_relation(transformed)
            self.assertEqual(result['pair'],[0,2])
            self.assertEqual(result['triple'],[1,3,4])

    def test_all_ten_role_partitions_and_canonical_sign(self):
        result=cofactor_null_relation(self.rays)
        signs=[]
        for references in itertools.combinations(range(5),3):
            probes=[i for i in range(5) if i not in references]
            rays=[self.rays[i] for i in references]+[self.rays[i] for i in probes]
            product=relative_product(rays)
            self.assertEqual(product,-result['coefficients'][probes[0]]*result['coefficients'][probes[1]])
            signs.append(1 if product>0 else -1)
        self.assertEqual(signs.count(1),6)
        self.assertEqual(signs.count(-1),4)
        canonical=[self.rays[i] for i in result['triple']+result['pair']]
        self.assertLess(relative_product(canonical),0)

    def test_intrinsic_center_frame_energy_balance(self):
        result=cofactor_null_relation(self.rays)
        c=[x/16 for x in result['coefficients']]
        nums,mass2=center_frame_energy_numerators(self.rays,c,result['pair'])
        self.assertEqual(mass2,48)
        self.assertEqual(nums,[24,16,24,16,16])
        self.assertEqual(sum(nums[i] for i in result['pair']),sum(nums[i] for i in result['triple']))
        boosted=[z_boost(k) for k in self.rays]
        nums2,mass2b=center_frame_energy_numerators(boosted,c,result['pair'])
        self.assertEqual(nums2,nums)
        self.assertEqual(mass2b,mass2)

    def test_degenerate_and_invalid_cases_not_silently_classified(self):
        degenerate=[null_ray(0,0),null_ray(1,0),null_ray(2,0),null_ray(3,0),null_ray(0,1)]
        with self.assertRaises(ValueError): cofactor_null_relation(degenerate)
        past=[scale(-1,self.rays[0])]+self.rays[1:]
        with self.assertRaises(ValueError): cofactor_null_relation(past)
        with self.assertRaises(ValueError): cofactor_null_relation(self.rays[:4])


if __name__=='__main__': unittest.main()
