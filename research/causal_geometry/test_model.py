import math
import unittest
import model as m

w,v,c=m.w,m.vac,m.car


class GeometryTests(unittest.TestCase):
    def close(self,a,b):
        self.assertLess(w.distance(a,b),1e-11)

    def test_01_null_roundtrip(self):
        for t,x in ((1,2),(-.3,.7),(0,0)):
            tt,xx=m.cartesian(*m.null(t,x))
            self.assertAlmostEqual(tt,t); self.assertAlmostEqual(xx,x)

    def test_02_causal_order_criterion(self):
        for t in (-2,-1,0,1,2):
            for x in (-2,-1,0,1,2):
                self.assertEqual(m.precedes((0,0),m.null(t,x)),t>=abs(x))

    def test_03_transitivity(self):
        points=[(u,v) for u in (-1,0,1) for v in (-1,0,1)]
        for p in points:
            for q in points:
                for r in points:
                    if m.precedes(p,q) and m.precedes(q,r):
                        self.assertTrue(m.precedes(p,r))

    def test_04_antisymmetry(self):
        points=[(u,v) for u in (-1,0,1) for v in (-1,0,1)]
        for p in points:
            for q in points:
                self.assertEqual(m.precedes(p,q) and m.precedes(q,p),p==q)

    def test_05_null_is_not_chronological(self):
        self.assertTrue(m.precedes((0,0),(1,0)))
        self.assertFalse(m.precedes((0,0),(1,0),strict=True))
        self.assertTrue(m.precedes((0,0),(1,1),strict=True))

    def test_06_nonlinear_order_isomorphism(self):
        points=[(u,v) for u in (-2,-1,0,1,2) for v in (-2,-1,0,1,2)]
        for p in points:
            for q in points:
                self.assertEqual(m.precedes(p,q),m.precedes(m.order_map(p),m.order_map(q)))

    def test_07_spacelike_preservation(self):
        p,q=(-1,2),(2,-1)
        self.assertLess(m.flat_interval_squared(p,q),0)
        self.assertLess(m.flat_interval_squared(m.order_map(p),m.order_map(q)),0)

    def test_08_diamond_membership_preserved(self):
        p,q=(-1,-2),(2,1)
        for r in ((0,0),(1,2),(-2,0),(1,-1)):
            old=m.precedes(p,r,True) and m.precedes(r,q,True)
            new=m.precedes(m.order_map(p),m.order_map(r),True) and m.precedes(m.order_map(r),m.order_map(q),True)
            self.assertEqual(old,new)

    def test_09_order_does_not_fix_interval(self):
        p,q=(0,0),(1,1)
        self.assertNotEqual(m.flat_interval_squared(p,q),m.flat_interval_squared(m.order_map(p),m.order_map(q)))

    def test_10_positive_conformal_factor_preserves_cones(self):
        for tangent in ((1,1),(1,-1),(0,1)):
            squared=tangent[0]*tangent[1]
            scaled=m.quadratic_density(1,2)*squared
            self.assertEqual((squared>0,squared==0),(scaled>0,scaled==0))

    def test_11_same_causality_curved_metric(self):
        self.assertNotEqual(m.quadratic_curvature(1,2),0)
        self.assertEqual(m.quadratic_curvature(1,2,b=0),0)

    def test_12_flat_volume_interval_identity(self):
        p,q=(-1,-2),(3,1)
        self.assertAlmostEqual(2*m.flat_volume(p,q),m.flat_interval_squared(p,q))

    def test_13_local_density_reconstruction(self):
        u,v=1.,2.; target=m.quadratic_density(u,v)
        errors=[]
        for h in (.2,.1,.05):
            volume=m.quadratic_volume((u-h,v-h),(u+h,v+h))
            error=m.averaged_density(volume,h,h)-target
            self.assertAlmostEqual(error,(.2+.3)*h*h/3)
            errors.append(error)
        self.assertAlmostEqual(errors[0]/errors[-1],16)

    def test_14_identifiable_three_parameter_family(self):
        params=(1.3,.4,.7); h,d=.1,.8
        means=[]
        for u,v in ((0,0),(d,0),(0,d)):
            means.append(m.averaged_density(m.quadratic_volume((u-h,v-h),(u+h,v+h),*params),h,h))
        recovered=m.reconstruct_quadratic(*means,h,d)
        for x,y in zip(params,recovered):
            self.assertAlmostEqual(x,y)

    def test_15_calibrated_volume_fixes_constant_scale(self):
        volume=m.flat_volume((0,0),(2,3),scale=4)
        self.assertAlmostEqual(math.sqrt(2*volume/(2*3)),4)

    def test_16_volume_ratios_do_not_fix_scale(self):
        for scale in (1,3,7):
            ratio=m.flat_volume((0,0),(2,3),scale)/m.flat_volume((0,0),(1,1),scale)
            self.assertAlmostEqual(ratio,6)

    def test_17_same_finite_order_different_volumes(self):
        points=[(0,0),(0,1),(1,0),(1,1)]
        order=[[m.precedes(p,q) for q in points] for p in points]
        self.assertEqual(order,[[m.precedes(m.order_map(p),m.order_map(q)) for q in points] for p in points])
        self.assertNotEqual(m.flat_volume((0,0),(1,1)),m.quadratic_volume((0,0),(1,1)))

    def test_18_integer_diamond_measure_aliasing(self):
        for u in range(-2,2):
            for v in range(-2,2):
                p,q=(u,v),(u+2,v+1)
                self.assertAlmostEqual(m.sine_volume(p,q,.3),m.flat_volume(p,q))

    def test_19_coarse_volume_does_not_fix_curvature(self):
        self.assertAlmostEqual(m.sine_curvature(0,0,.3),-16*math.pi**2*.3)
        self.assertAlmostEqual(m.sine_volume((0,0),(1,1),.3),.5)

    def test_20_fine_volume_sees_hidden_density(self):
        self.assertAlmostEqual(m.sine_density(.25,.25,.3),1.3)
        self.assertNotAlmostEqual(m.sine_volume((0,0),(.5,.5),.3),m.flat_volume((0,0),(.5,.5)))
        for u in (0,.25,.75):
            for v in (0,.25,.75):
                self.assertGreater(m.sine_density(u,v,.9),0)

    def test_21_count_mean_scaling(self):
        rho,volume,scale=7.,2.,3.
        self.assertAlmostEqual(rho*volume,(rho/scale**2)*(volume*scale**2))

    def test_22_poisson_law_scaling(self):
        for n in (0,1,10,20):
            self.assertAlmostEqual(m.poisson_probability(n,7,2),m.poisson_probability(n,7/9,18))

    def test_23_mass_dispersion_dilation(self):
        mass,k,scale=.7,1.2,3.
        self.assertAlmostEqual(math.hypot(k/scale,mass/scale),math.hypot(k,mass)/scale)

    def test_24_polarization_dilation(self):
        self.close(v.dirac_covariance(1.2/3,.7/3),v.dirac_covariance(1.2,.7))

    def test_25_dynamics_dilation(self):
        self.close(w.dirac(1.2/3,.7/3,3*.8),w.dirac(1.2,.7,.8))

    def test_26_spacetime_source_dilation(self):
        scale=3.; samples=((-1,.2,(1,.3j)),(.3,.7,(.4j,.8)))
        old=m.net.smear(1.2,.7,samples)
        new=m.net.smear(1.2/scale,.7/scale,tuple((scale*t,scale*a,tuple(x/math.sqrt(scale) for x in f)) for t,a,f in samples))
        self.assertLess(c.norm_vector(tuple(x-math.sqrt(scale)*y for x,y in zip(new,old))),1e-11)

    def test_27_dimensionless_vacuum_pairing(self):
        f,g=(1,.3j),(.4j,.8)
        self.assertAlmostEqual(abs(v.pairing(v.dirac_covariance(1.2,.7),f,g)-v.pairing(v.dirac_covariance(.4,.7/3),f,g)),0)

    def test_28_bare_car_allows_nonlocal_mode_permutation(self):
        permutation=(4,1,2,3,0,5)
        u=tuple(tuple(complex(i==permutation[j]) for j in range(6)) for i in range(6))
        gamma=c.fock_lift(u)
        self.assertLess(c.error(c.mul(c.adjoint(gamma),gamma),c.identity(64)),1e-11)
        self.assertEqual({permutation[i]//2 for i in (0,1)},{0,2})
        for i in (0,1):
            self.assertLess(c.error(c.pullback(gamma,c.annihilator(6,i)),c.lifted_generator(u,i)),1e-11)

    def test_29_covariance_without_localization(self):
        a,b=v.dirac_covariance(1.2,.7),v.dirac_covariance(1.2,2.)
        u=m.projection_intertwiner(a,b)
        self.close(w.mul(w.adjoint(u),u),w.I)
        self.close(w.mul(w.mul(u,a),w.adjoint(u)),b)

    def test_30_timelike_commutation_is_not_causal_independence(self):
        gamma=c.fock_lift(w.dirac(1.2,.7,.8)); n=c.number_total(2)
        evolved=c.pullback(gamma,n)
        self.assertLess(c.error(evolved,n),1e-11)
        self.assertLess(c.error(c.mul(evolved,n),c.mul(n,evolved)),1e-11)

    def test_31_inverse_stability_within_family(self):
        h,d=.1,.8; eta=.001
        exact=m.reconstruct_quadratic(1.,1.2,1.3,h,d)
        perturbed=m.reconstruct_quadratic(1+eta,1.2-eta,1.3+eta,h,d)
        for i in (1,2):
            self.assertLessEqual(abs(exact[i]-perturbed[i]),2*eta/d**2+1e-12)

    def test_32_validation(self):
        for call in (lambda:m.flat_volume((1,1),(0,0)),lambda:m.flat_volume((0,0),(1,1),0),lambda:m.sine_density(0,0,1),lambda:m.quadratic_density(0,0,a=-1),lambda:m.poisson_probability(-1,1,1),lambda:m.reconstruct_quadratic(1,2,3,0,1)):
            with self.assertRaises(ValueError):
                call()


if __name__=='__main__':
    unittest.main()
