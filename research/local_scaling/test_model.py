import math
import unittest
import model as m

w,c=m.w,m.car


class LocalScalingTests(unittest.TestCase):
    def setUp(self):
        self.spin=(.3+1j,.7-.2j)
        self.mass=.7

    def test_01_normalized_cell_embedding(self):
        a={-1:(1,.2j),2:(.3j,.4)}
        self.assertAlmostEqual(m.piecewise_inner(a,.2,a,.2).real,w.norm_squared(a))

    def test_02_disjoint_cells_orthogonal(self):
        self.assertEqual(m.piecewise_inner({0:(1,0)},.2,{1:(1,0)},.2),0)

    def test_03_cell_overlap_between_grids(self):
        self.assertAlmostEqual(m.piecewise_inner({0:(1,0)},.2,{0:(1,0)},.1).real,1/math.sqrt(2))

    def test_04_averaging_norm_contraction(self):
        f=m.cell_average_blob(.17,.7,self.spin)
        self.assertLessEqual(w.norm_squared(f),m.blob_norm_squared(.7)*sum(abs(x)**2 for x in self.spin))

    def test_05_projection_poincare_bound(self):
        for a in (.2,.1,.05,.025):
            self.assertLessEqual(m.projection_error(a,.7,self.spin),a*math.sqrt(m.blob_derivative_norm_squared(.7))*c.norm_vector(self.spin)+1e-12)

    def test_06_projection_refinement(self):
        errors=[m.projection_error(a,.7,self.spin) for a in (.2,.1,.05)]
        self.assertLess(errors[-1],errors[0]/3)

    def test_07_exact_finite_support(self):
        for a in (.2,.13):
            f=m.cell_average_blob(a,.7,self.spin,.3)
            self.assertTrue(all(.3-.7-a/2<j*a<.3+.7+a/2 for j in f))

    def test_08_physical_support_buffer(self):
        a=.13; f=m.cell_average_blob(a,.7,self.spin,.3)
        self.assertTrue(all(m.cell(j,a)[0]>.3-.7-a and m.cell(j,a)[1]<.3+.7+a for j in f))

    def test_09_inside_open_interval_for_small_cells(self):
        for a in (.1,.05):
            f=m.cell_average_blob(a,.7,self.spin)
            self.assertEqual(f,m.localize_to_interval(f,a,-1,1))

    def test_10_boundary_crossing_cells_are_excluded(self):
        cells=m.full_cells(.2,-.93,.93)
        self.assertNotIn(5,cells); self.assertNotIn(-5,cells)
        self.assertTrue(all(-.93<m.cell(j,.2)[0]<m.cell(j,.2)[1]<.93 for j in cells))

    def test_11_piecewise_coin_intertwining(self):
        f=m.cell_average_blob(.2,.7,self.spin)
        coin=w.coin(self.mass,.2)
        g={j:w.apply(coin,x) for j,x in f.items()}
        self.assertAlmostEqual(w.norm_squared(g),w.norm_squared(f))

    def test_12_conditional_shift_cell_translation(self):
        f={0:(1,2j)}
        self.assertEqual(w.real_step(f,0,.2),{1:(1+0j,0j),-1:(0j,2j)})

    def test_13_signed_evolution_inverse(self):
        f=m.cell_average_blob(.1,.4,self.spin)
        g=m.evolve(m.evolve(f,self.mass,.1,4),self.mass,.1,-4)
        self.assertLess(m.piecewise_distance(f,.1,g,.1),1e-7)

    def test_14_evolution_norm_preservation(self):
        f=m.cell_average_blob(.1,.4,self.spin)
        self.assertAlmostEqual(w.norm_squared(m.evolve(f,self.mass,.1,-4)),w.norm_squared(f))

    def test_15_massless_positive_time_reference(self):
        a=.1; f=m.cell_average_blob(a,.7,self.spin)
        error=m.massless_reference_error(m.evolve(f,0,a,4),a,.4,.7,self.spin)
        self.assertAlmostEqual(error,m.projection_error(a,.7,self.spin))

    def test_16_massless_negative_time_reference(self):
        a=.1; f=m.cell_average_blob(a,.7,self.spin)
        error=m.massless_reference_error(m.evolve(f,0,a,-4),a,-.4,.7,self.spin)
        self.assertAlmostEqual(error,m.projection_error(a,.7,self.spin))

    def test_17_massive_cauchy_bound(self):
        a,b=.05,1/320; t=.2
        f=m.cell_average_blob(a,.7,self.spin); g=m.cell_average_blob(b,.7,self.spin)
        error=m.piecewise_distance(m.evolve(f,self.mass,a,4),a,m.evolve(g,self.mass,b,64),b)
        bound=(a+b)*(1+t*self.mass)*math.sqrt(m.blob_derivative_norm_squared(.7))*c.norm_vector(self.spin)
        self.assertLessEqual(error,bound+1e-10)

    def test_18_massive_refinement(self):
        b=1/640; t=.2
        reference=m.evolve(m.cell_average_blob(b,.7,self.spin),self.mass,b,128)
        errors=[m.piecewise_distance(m.evolve(m.cell_average_blob(a,.7,self.spin),self.mass,a,round(t/a)),a,reference,b) for a in (.1,.05,.025)]
        self.assertLess(errors[-1],errors[0]/3)

    def test_19_diamond_pullback_stays_in_base(self):
        a=.1; radius=1
        for n in (-3,0,3):
            for j in range(-8,9):
                if m.cell_in_diamond(n,j,a,radius):
                    support=m.evolve({j:self.spin},self.mass,a,-n)
                    self.assertTrue(all(m.cell_in_diamond(0,k,a,radius) for k in support))

    def test_20_diamond_base_generators_present(self):
        for j in m.full_cells(.1,-1,1):
            self.assertTrue(m.cell_in_diamond(0,j,.1,1))

    def test_21_compact_spacetime_source_cells(self):
        _,labels=m.local_spacetime_blob(.05,self.mass,.2,.3,self.spin)
        self.assertTrue(labels)
        self.assertTrue(all(m.cell_in_diamond(n,j,.05,1) for n,j in labels))

    def test_22_spacetime_pullback_support(self):
        f,_=m.local_spacetime_blob(.05,self.mass,.2,.3,self.spin)
        self.assertTrue(all(m.cell_in_diamond(0,j,.05,1) for j in f))

    def test_23_spacetime_refinement(self):
        b=1/320
        reference,_=m.local_spacetime_blob(b,self.mass,.2,.3,self.spin)
        errors=[]
        for a in (.05,.025):
            f,_=m.local_spacetime_blob(a,self.mass,.2,.3,self.spin)
            errors.append(m.piecewise_distance(f,a,reference,b))
        self.assertLess(errors[-1],errors[0]*.7)

    def test_24_exact_lattice_spacelike_pairing(self):
        # Spacelike separation 8 sites versus 3 time steps.
        a=m.evolve({0:(1,0)},self.mass,.1,-4)
        b=m.evolve({8:(.3,1j)},self.mass,.1,-1)
        self.assertLess(abs(m.net.lattice_inner(a,b)),1e-12)

    def test_25_zero_average_invisible_direction(self):
        # Odd smooth-shaped direction x*b(x) has zero average on its cell.
        a=.2
        integral=sum((j+.5)*a/1000*m.blob(2*(j+.5)/1000)*a/1000 for j in range(-500,500))
        self.assertLess(abs(integral),1e-15)
        self.assertGreater(m.blob(.25),0)

    def test_26_even_unit_ball_obstruction(self):
        # Independent complement occupation has distance 1/2 from scalar midpoint.
        n=c.number(2,1); mid=c.scale(.5,c.identity(4))
        diff=c.add(n,c.scale(-1,mid))
        self.assertEqual(set(abs(value) for value in diff.values()),{.5})
        self.assertEqual(c.mul(diff,diff),c.scale(.25,c.identity(4)))

    def test_27_periodic_vacuum_projector(self):
        a=.1
        for k in (-100,1,100):
            p=m.vac.walk_covariance(k,self.mass,a)
            self.assertLess(w.distance(w.mul(p,p),p),1e-11)
            self.assertLess(w.distance(p,m.vac.walk_covariance(k+2*math.pi/a,self.mass,a)),1e-11)

    def test_28_periodic_vacuum_low_band_limit(self):
        for a in (.1,.05):
            for k in (-2,0,2):
                self.assertLessEqual(w.distance(m.vac.walk_covariance(k,self.mass,a),m.vac.dirac_covariance(k,self.mass)),m.vac.projector_bound(2,self.mass,a)+1e-12)

    def test_29_covariance_intertwines_cell_embedding(self):
        f=((1,.2j),(.4j,.3),(0,.7j))
        coarse=m.periodic_covariance_apply(f,self.mass,.2,.2)
        a=m.periodic_embed(coarse,3)
        b=m.periodic_covariance_apply(m.periodic_embed(f,3),self.mass,.2/3,.2)
        self.assertLess(sum(abs(x-y)**2 for fa,fb in zip(a,b) for x,y in zip(fa,fb)),1e-24)

    def test_30_cell_projector_commutes_with_periodic_covariance(self):
        f=tuple((.1*j+1j,.2-.3j*j) for j in range(9))
        c_then_r=m.periodic_embed(m.periodic_compress(m.periodic_covariance_apply(f,self.mass,.2/3,.2),3),3)
        r_then_c=m.periodic_covariance_apply(m.periodic_embed(m.periodic_compress(f,3),3),self.mass,.2/3,.2)
        self.assertLess(sum(abs(x-y)**2 for fa,fb in zip(c_then_r,r_then_c) for x,y in zip(fa,fb)),1e-24)

    def test_31_averaging_is_not_exact_inverse_homomorphism(self):
        a=.1; norm2=m.blob_norm_squared(.7)*c.norm_vector(self.spin)**2
        projected=w.norm_squared(m.cell_average_blob(a,.7,self.spin))
        self.assertGreater(norm2-projected,0)
        self.assertLess(norm2-projected,.02)

    def test_32_validation(self):
        for a in (0,-1,float('inf')):
            with self.assertRaises(ValueError):
                m.cell(0,a)
        with self.assertRaises(ValueError):
            m.blob(0,0)
        with self.assertRaises(ValueError):
            m.evolve({},1,.1,.5)
        with self.assertRaises(ValueError):
            m.full_cells(.1,1,-1)


if __name__=='__main__':
    unittest.main()
