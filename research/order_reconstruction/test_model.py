from fractions import Fraction as F
from itertools import product
import random
import unittest
import model as m


def source_from_coords(coords):
    nodes=tuple(range(len(coords)))
    return nodes,frozenset((i,j) for i in nodes for j in nodes if all(a<=b for a,b in zip(coords[i],coords[j])))


class ReconstructionTests(unittest.TestCase):
    def grid(self,r=3,s=4):
        nodes,rel,_=m.grid_fixture(r,s)
        return m.reconstruct(nodes,rel)

    def weights(self,g,weights):
        # Test fixture values may be transposed into the returned axis convention.
        return weights if len(weights)==g.shape[0]-1 else tuple(zip(*weights))

    def test_01_smallest_grid(self):
        g=self.grid(2,2)
        self.assertEqual(g.shape,(2,2))
        self.assertEqual(len(g.coordinates),4)

    def test_02_rectangular_shape(self):
        self.assertEqual(sorted(self.grid().shape),[3,4])

    def test_03_all_small_shapes(self):
        for r,s in product(range(2,5),repeat=2):
            g=self.grid(r,s)
            self.assertEqual(sorted(g.shape),sorted((r,s)))

    def test_04_order_reflected(self):
        g=self.grid()
        for x,y in product(g.nodes,repeat=2):
            self.assertEqual((x,y) in g.relation,all(a<=b for a,b in zip(g.coordinates[x],g.coordinates[y])))

    def test_05_meet_join_coordinates(self):
        g=self.grid()
        for x,y in product(g.nodes,repeat=2):
            self.assertEqual(g.coordinates[g.meet[x,y]],tuple(min(a,b) for a,b in zip(g.coordinates[x],g.coordinates[y])))
            self.assertEqual(g.coordinates[g.join[x,y]],tuple(max(a,b) for a,b in zip(g.coordinates[x],g.coordinates[y])))

    def test_06_opaque_relabelling(self):
        rng=random.Random(123); labels=[f'opaque-{i*37+11}' for i in range(12)]; rng.shuffle(labels)
        nodes,rel,truth=m.grid_fixture(3,4,labels)
        shuffled=list(nodes); rng.shuffle(shuffled)
        g=m.reconstruct(shuffled,rel)
        self.assertTrue(g.coordinates==truth or g.coordinates=={x:(b,a) for x,(a,b) in truth.items()})

    def test_07_input_enumeration_only_swaps_axes(self):
        nodes,rel,truth=m.grid_fixture(3,4)
        g=m.reconstruct(tuple(reversed(nodes)),rel)
        self.assertTrue(g.coordinates==truth or g.coordinates=={x:(b,a) for x,(a,b) in truth.items()})

    def test_08_axis_exchange(self):
        g=self.grid(4,3)
        nodes,rel,truth=m.grid_fixture(3,4)
        transpose={x:(b,a) for x,(a,b) in truth.items()}
        self.assertEqual(sorted(g.shape),[3,4])
        self.assertTrue(all(((x,y) in rel)==all(a<=b for a,b in zip(transpose[x],transpose[y])) for x in nodes for y in nodes))
        self.assertEqual(len(rel),len(g.relation))

    def test_09_nonreflexive_rejected(self):
        nodes,rel,_=m.grid_fixture(2,2)
        with self.assertRaises(ValueError):
            m.reconstruct(nodes,rel-{(nodes[0],nodes[0])})

    def test_10_nontransitive_rejected(self):
        nodes,rel,_=m.grid_fixture(2,2)
        with self.assertRaises(ValueError):
            m.reconstruct(nodes,rel-{(nodes[0],nodes[-1])})

    def test_11_antisymmetry_required(self):
        with self.assertRaises(ValueError):
            m.reconstruct(('a','b'),product(('a','b'),repeat=2))

    def test_12_antichain_not_lattice(self):
        with self.assertRaises(ValueError):
            m.reconstruct(('a','b'),(('a','a'),('b','b')))

    def test_13_M3_nondistributive_rejected(self):
        nodes=tuple(range(5)); rel={(x,x) for x in nodes}|{(0,x) for x in nodes}|{(x,4) for x in nodes}
        with self.assertRaisesRegex(ValueError,'distributive'):
            m.reconstruct(nodes,rel)

    def test_14_three_axis_boolean_lattice_rejected(self):
        nodes,rel=source_from_coords(tuple(product(range(2),repeat=3)))
        with self.assertRaisesRegex(ValueError,'two nonempty'):
            m.reconstruct(nodes,rel)

    def test_15_chain_not_two_dimensional_grid(self):
        with self.assertRaisesRegex(ValueError,'two nonempty'):
            m.reconstruct(tuple(range(4)),((i,j) for i in range(4) for j in range(i,4)))

    def test_16_missing_point_does_not_get_filled_silently(self):
        nodes,rel,_=m.grid_fixture(3,3)
        missing=nodes[4]
        with self.assertRaises(ValueError):
            m.reconstruct(tuple(x for x in nodes if x!=missing),((x,y) for x,y in rel if missing not in (x,y)))

    def test_17_positive_valuation_recovery(self):
        g=self.grid(); weights=self.weights(g,((F(1,2),F(1),F(3,2)),(F(2),F(5,2),F(3))))
        self.assertEqual(m.recover_weights(g,m.interval_values(g,weights)),weights)

    def test_18_additivity_violation_rejected(self):
        g=self.grid(); values=m.interval_values(g,self.weights(g,((1,2,3),(4,5,6))))
        inverse={coord:node for node,coord in g.coordinates.items()}
        values[inverse[0,0],inverse[g.shape[0]-1,g.shape[1]-1]]+=1
        with self.assertRaisesRegex(ValueError,'additive'):
            m.recover_weights(g,values)

    def test_19_null_valuation_violation_rejected(self):
        g=self.grid(); values=m.interval_values(g,self.weights(g,((1,2,3),(4,5,6))))
        inverse={coord:node for node,coord in g.coordinates.items()}
        values[inverse[0,0],inverse[0,1]]=1
        with self.assertRaises(ValueError):
            m.recover_weights(g,values)

    def test_20_zero_atom_rejected(self):
        g=self.grid()
        with self.assertRaises(ValueError):
            m.recover_weights(g,m.interval_values(g,self.weights(g,((0,2,3),(4,5,6)))))

    def test_21_flat_factorization_exact(self):
        weights=((F(1,2),1,F(3,2)),(1,2,3))
        du,dv=m.flat_widths(weights)
        self.assertEqual(du,(1,2)); self.assertEqual(dv,(1,2,3))
        self.assertTrue(all(F(1,2)*du[i]*dv[j]==weights[i][j] for i in range(2) for j in range(3)))

    def test_22_boost_factor_gauge(self):
        weights=((1,2),(3,6)); du,dv=m.flat_widths(weights)
        scale=F(7,3)
        self.assertTrue(all(du[i]*scale*dv[j]/scale/2==weights[i][j] for i in range(2) for j in range(2)))

    def test_23_nonrankone_excludes_flat_null_grid(self):
        with self.assertRaises(ValueError):
            m.flat_widths(((1,2),(3,7)))

    def test_24_proper_interval_from_flat_valuation(self):
        weights=((F(1,2),1,F(3,2)),(1,2,3)); du,dv=m.flat_widths(weights)
        volume=sum(sum(row) for row in weights)
        self.assertEqual(sum(du)*sum(dv),2*volume)

    def test_25_uncalibrated_volume_scale(self):
        weights=((1,2),(3,6)); scale=F(5,2)
        du,dv=m.flat_widths(weights)
        self.assertTrue(all((du[i]*scale)*(dv[j]*scale)/2==weights[i][j]*scale**2 for i in range(2) for j in range(2)))

    def test_26_refine_coarsen_exact(self):
        weights=((F(1,3),F(2,7)),(F(3,5),F(4,9)))
        self.assertEqual(m.coarsen(m.refine(weights,2,3),2,3),weights)

    def test_27_rankone_refinement(self):
        du,dv=m.flat_widths(m.refine(((1,2),(3,6))))
        self.assertEqual(len(du),4); self.assertEqual(len(dv),4)

    def test_28_nonflat_refinement_hidden_by_coarse_values(self):
        flat=((1,1),(1,1)); other=((F(3,2),F(1,2)),(F(1,2),F(3,2)))
        self.assertEqual(m.coarsen(flat),m.coarsen(other))
        m.flat_widths(flat)
        with self.assertRaises(ValueError):
            m.flat_widths(other)

    def test_29_covers_not_intrinsically_null(self):
        # Cartesian (t,x) data: bottom, two middles, top. Both realize C2 x C2.
        def rel(points):
            return {(i,j) for i,p in enumerate(points) for j,q in enumerate(points) if q[0]-p[0]>=abs(q[1]-p[1])}
        null=((0,0),(1,-1),(1,1),(2,0))
        timelike=((0,0),(1,-.4),(1,.4),(2,0))
        self.assertEqual(rel(null),rel(timelike))
        self.assertEqual(m.reconstruct(range(4),rel(timelike)).shape,(2,2))
        self.assertEqual((null[1][0]-null[0][0])**2-(null[1][1]-null[0][1])**2,0)
        self.assertGreater((timelike[1][0]-timelike[0][0])**2-(timelike[1][1]-timelike[0][1])**2,0)

    def test_30_refinement_embedding_preserves_order(self):
        coarse=self.grid(3,4); fine=self.grid(5,7)
        fine_inverse={coord:node for node,coord in fine.coordinates.items()}
        embedding={node:fine_inverse[2*i,2*j] for node,(i,j) in coarse.coordinates.items()}
        for x,y in product(coarse.nodes,repeat=2):
            self.assertEqual((x,y) in coarse.relation,(embedding[x],embedding[y]) in fine.relation)

    def test_31_noise_can_destroy_exact_rankone(self):
        m.flat_widths(((1,2),(3,6)))
        with self.assertRaises(ValueError):
            m.flat_widths(((1,2),(3,F(6000001,1000000))))

    def test_32_validation(self):
        for call in (lambda:m.reconstruct((),()),lambda:m.reconstruct(('a',),(('a','b'),)),lambda:m.reconstruct(('a','a'),()),lambda:m.flat_widths(((0,),)),lambda:m.refine(((1,),),0,2),lambda:m.coarsen(((1,),),2,2)):
            with self.assertRaises(ValueError):
                call()


if __name__=='__main__':
    unittest.main()
