from fractions import Fraction as F
from itertools import product
import unittest
import model as m


class CompletionTests(unittest.TestCase):
    def test_01_vertex_embeddings(self):
        for n in range(5):
            for i in range((1<<n)+1):
                self.assertEqual(m.vertex(n,i),m.vertex(n+1,2*i))

    def test_02_product_order_refinement(self):
        points=tuple(product(range(5),repeat=2))
        for p,q in product(points,repeat=2):
            self.assertEqual(all(x<=y for x,y in zip(p,q)),all(2*x<=2*y for x,y in zip(p,q)))

    def test_03_direct_limit_identification(self):
        self.assertEqual(m.vertex(1,1),m.vertex(5,16))
        self.assertEqual(m.vertex(0,0),m.vertex(5,0))

    def test_04_rank_midpoint_not_metric_midpoint(self):
        self.assertEqual(m.vertex(1,1),F(1,2))
        self.assertEqual(m.quantile(1,1,F(2,3)),F(1,3))

    def test_05_cut_brackets_shrink(self):
        x=F(5,13); previous=(F(0),F(1))
        for n in range(7):
            left,right=m.bracket(n,x)
            self.assertTrue(previous[0]<=left<=x<=right<=previous[1])
            self.assertEqual(right-left,F(1,1<<n)); previous=(left,right)

    def test_06_binary_endpoint_identification(self):
        for n in (2,4,8):
            high=m.binary_prefix((1,)+(0,)*(n-1))
            low=m.binary_prefix((0,)+(1,)*(n-1))
            self.assertEqual(high-low,F(1,1<<n))

    def test_07_same_point_distinct_address_limits(self):
        self.assertEqual(m.binary_prefix((1,0,0,0)),F(1,2))
        self.assertEqual(m.binary_prefix((0,1,1,1)),F(7,16))
        self.assertEqual(m.binary_prefix((0,)+(1,)*7)+F(1,256),F(1,2))

    def test_08_prefix_cylinders_are_disjoint(self):
        a={bits for bits in product((0,1),repeat=4) if bits[0]==0}
        b={bits for bits in product((0,1),repeat=4) if bits[0]==1}
        self.assertFalse(a&b); self.assertEqual(len(a|b),16)

    def test_09_uniform_consistency(self):
        self.assertTrue(all(m.consistency(m.uniform,n) for n in range(5)))

    def test_10_affine_consistency(self):
        self.assertTrue(all(m.consistency(m.affine,n) for n in range(5)))

    def test_11_biased_consistency(self):
        self.assertTrue(all(m.consistency(m.biased,n) for n in range(5)))

    def test_12_late_bias_matches_every_observed_prefix(self):
        self.assertTrue(all(m.weights(m.late_bias,n)==m.weights(m.uniform,n) for n in range(4)))

    def test_13_unobserved_tail_can_differ(self):
        self.assertNotEqual(m.weights(m.late_bias,4),m.weights(m.uniform,4))
        self.assertTrue(m.consistency(m.late_bias,3))

    def test_14_inconsistent_values_detected(self):
        bad=lambda n,i,j:m.uniform(n,i,j)+(F(1,100) if n==2 and i==0 and j==0 else 0)
        self.assertFalse(m.consistency(bad,1))

    def test_15_boundary_address_positivity_consistency(self):
        self.assertTrue(all(m.consistency(m.boundary_path,n) for n in range(5)))
        self.assertGreater(min(x for row in m.weights(m.boundary_path,4) for x in row),0)

    def test_16_cell_decay_not_sufficient_for_strip_decay(self):
        matrix=m.weights(m.boundary_path,6)
        self.assertLess(max(x for row in matrix for x in row),F(1,100))
        row_max,column_max=m.strip_maxima(matrix)
        self.assertGreaterEqual(row_max,F(1,4)); self.assertEqual(column_max,F(1,64))

    def test_17_nested_halfopen_strips_empty_with_positive_mass(self):
        lefts=[]
        for n in range(1,7):
            path=(1<<(n-1))-1
            lefts.append(m.vertex(n,path))
            self.assertEqual(m.vertex(n,path+1),F(1,2))
            self.assertGreaterEqual(sum(m.weights(m.boundary_path,n)[path]),F(1,4))
        self.assertTrue(all(a<b for a,b in zip(lefts,lefts[1:])))
        self.assertEqual(F(1,2)-lefts[-1],F(1,64))

    def test_18_uniform_strip_decay(self):
        for n in range(6):
            self.assertEqual(m.strip_maxima(m.weights(m.uniform,n)),(F(1,1<<n),)*2)

    def test_19_biased_strip_decay(self):
        for n in range(6):
            self.assertEqual(m.strip_maxima(m.weights(m.biased,n)),(F(2,3)**n,)*2)

    def test_20_affine_density_bounds(self):
        for n in range(5):
            rho=m.densities(m.weights(m.affine,n))
            self.assertTrue(all(1<=x<=F(11,6) for row in rho for x in row))

    def test_21_affine_neighbour_modulus(self):
        for n in range(1,6):
            self.assertLessEqual(m.neighbour_jump(m.weights(m.affine,n)),F(1,2)*F(1,1<<n))

    def test_22_affine_uniform_error_bound(self):
        for n in range(5):
            matrix=m.weights(m.affine,n)
            for u,v in product((F(0),F(1,7),F(1,2),F(1)),repeat=2):
                expected=1+u/3+v/2
                self.assertLessEqual(abs(m.density_at(matrix,u,v)-expected),F(1,1<<n))

    def test_23_affine_completion_is_curved(self):
        self.assertEqual(m.affine_curvature(0,0),F(1,3))
        self.assertGreater(m.affine_curvature(1,1),0)

    def test_24_jump_density_is_bounded_and_consistent(self):
        for n in range(5):
            self.assertTrue(m.consistency(m.jump,n))
            self.assertTrue(all(1<=x<=2 for row in m.densities(m.weights(m.jump,n)) for x in row))

    def test_25_uniform_cauchy_does_not_imply_continuity(self):
        for n in range(1,5):
            self.assertEqual(m.neighbour_jump(m.weights(m.jump,n)),1)
            for u in (F(1,3),F(2,3)):
                self.assertEqual(m.density_at(m.weights(m.jump,n),u,0),m.density_at(m.weights(m.jump,n+1),u,0))

    def test_26_biased_density_bounds_fail(self):
        for n in range(1,6):
            rho=m.densities(m.weights(m.biased,n))
            self.assertEqual(max(x for row in rho for x in row),F(16,9)**n)
            self.assertEqual(min(x for row in rho for x in row),F(4,9)**n)

    def test_27_quantile_refinement_coherence(self):
        for n in range(5):
            for k in range((1<<n)+1):
                self.assertEqual(m.quantile(n,k,F(2,3)),m.quantile(n+1,2*k,F(2,3)))

    def test_28_product_quantile_rectangle_measure(self):
        n=4; p,q=F(2,3),F(1,3); matrix=m.weights(m.biased,n)
        i0,i1,j0,j1=2,11,3,14
        actual=sum((matrix[i][j] for i in range(i0,i1) for j in range(j0,j1)),F(0))
        expected=(m.quantile(n,i1,p)-m.quantile(n,i0,p))*(m.quantile(n,j1,q)-m.quantile(n,j0,q))
        self.assertEqual(actual,expected)

    def test_29_quantiles_strictly_increasing(self):
        vals=[m.quantile(5,k,F(2,3)) for k in range(33)]
        self.assertEqual((vals[0],vals[-1]),(0,1))
        self.assertTrue(all(a<b for a,b in zip(vals,vals[1:])))

    def test_30_affine_coarse_weights_not_rankone(self):
        a=m.weights(m.affine,1)
        self.assertNotEqual(a[0][0]*a[1][1],a[0][1]*a[1][0])

    def test_31_total_mass_preserved(self):
        for rule in (m.uniform,m.affine,m.biased,m.late_bias,m.jump,m.boundary_path):
            self.assertTrue(all(m.total(m.weights(rule,n))==m.total(m.weights(rule,0)) for n in range(5)))

    def test_32_validation(self):
        for call in (lambda:m.level(-1),lambda:m.level(9),lambda:m.vertex(1,3),lambda:m.bracket(1,2),lambda:m.binary_prefix((0,2)),lambda:m.digit_probability(1,0,1),lambda:m.weights(lambda n,i,j:0,1)):
            with self.assertRaises(ValueError):
                call()


if __name__=='__main__':
    unittest.main()
