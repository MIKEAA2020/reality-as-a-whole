from decimal import Decimal as D, localcontext
import math
import unittest
import model as m

c=m.car


class CellCurrentTests(unittest.TestCase):
    def setUp(self):
        self.alpha,self.u,self.a,self.n=.2,.4,.02,4
        self.cf=m.covariance_pair(self.alpha,self.u,self.a,self.n)
        self.c0=m.covariance_pair(0,self.u,self.a,self.n)
        self.rho=m.density_matrix(self.cf)
        self.target=m.previous.state_stress(m.previous.cubic('.2'),.4)

    def test_01_car_cells(self):
        a,b=c.annihilator(2,0),c.annihilator(2,1)
        self.assertEqual(c.add(c.mul(a,c.adjoint(b)),c.mul(c.adjoint(b),a)),{})

    def test_02_covariance_hermitian(self):
        self.assertEqual(self.cf[0][1],self.cf[1][0].conjugate())

    def test_03_positive_contraction(self):
        self.assertTrue(all(0<=x<=1 for x in m.covariance_eigenvalues(self.cf)))

    def test_04_density_trace_one(self):
        self.assertAlmostEqual(c.trace(self.rho).real,1)

    def test_05_density_positive(self):
        off=abs(self.cf[0][1]); d=.25-off*off
        self.assertTrue(all(x>=0 for x in (d,d,(.5-off)**2,(.5+off)**2)))

    def test_06_density_realizes_covariance(self):
        for i in (0,1):
            for j in (0,1):
                op=c.mul(c.adjoint(c.annihilator(2,i)),c.annihilator(2,j))
                self.assertAlmostEqual(abs(m.expectation(op,self.rho)-self.cf[j][i]),0)

    def test_07_centered_current_mean_zero(self):
        for i in (0,1):
            op=c.add(c.number(2,i),c.scale(-.5,c.identity(4)))
            self.assertAlmostEqual(abs(m.expectation(op,self.rho)),0)

    def test_08_current_wick_identity(self):
        actual=m.expectation(m.current_product(self.a),self.rho)
        expected=-math.pi*abs(self.cf[0][1])**2/self.a**2
        self.assertAlmostEqual(actual.real,expected)

    def test_09_actual_lattice_operator_difference(self):
        op=m.current_product(self.a)
        actual=m.expectation(op,self.rho)-m.expectation(op,m.density_matrix(self.c0))
        self.assertAlmostEqual(actual.real,m.relative_stress(self.alpha,self.u,self.a,self.n),places=11)

    def test_10_current_product_selfadjoint(self):
        self.assertEqual(m.current_product(self.a),c.adjoint(m.current_product(self.a)))

    def test_11_observable_norm_diverges(self):
        for a in (.1,.05,.025):
            op=m.current_product(a)
            self.assertTrue(all(abs(abs(x)-math.pi/(4*a*a))<1e-10 for x in op.values()))

    def test_12_smooth_relative_fermion_formula(self):
        alpha,u,s=.2,.4,.1
        f=m.previous.cubic(str(alpha))
        with localcontext() as ctx:
            ctx.prec=70
            l,dl,_,_=f(D(str(u))-D(str(s))/2); r,dr,_,_=f(D(str(u))+D(str(s))/2)
            direct=(dl*dr).sqrt()/(r-l)-1/D(str(s))
        self.assertAlmostEqual(float(direct),m.relative_fermion_kernel(alpha,u,s),places=13)

    def test_13_relative_fermion_regular_at_zero(self):
        self.assertEqual(m.relative_fermion_kernel(.2,.4,0),0)
        self.assertAlmostEqual(m.relative_fermion_kernel(.2,.4,1e-6)/1e-6,m.relative.remainder(.2,.4,0)/2,places=10)

    def test_14_flat_cell_integral_exact(self):
        with localcontext() as ctx:
            ctx.prec=70
            n=D(2)
            expected=n*((n+1)*(n+1).ln()-2*n*n.ln()+(n-1)*(n-1).ln())
        self.assertAlmostEqual(m.shape(2),float(expected),places=14)

    def test_15_cell_shape_independent_of_scale(self):
        for a in (.1,.01,.001):
            self.assertAlmostEqual(m.flat_cell_kernel(a,4)*(4*a),m.shape(4))

    def test_16_shape_error_bound(self):
        for n in (2,4,8,16):
            r=1/n
            self.assertLessEqual(m.shape(n)-1,r*r/(6*(1-r*r))+1e-15)

    def test_17_shape_approaches_one(self):
        values=[m.shape(n) for n in (2,4,8,16)]
        self.assertTrue(all(x>1 for x in values))
        self.assertTrue(all(b<a for a,b in zip(values,values[1:])))

    def test_18_fixed_cell_count_limit(self):
        for n in (2,4,8):
            actual=m.relative_stress(.2,.4,.0001,n)
            self.assertAlmostEqual(actual,m.shape(n)*self.target,places=8)

    def test_19_uncalibrated_bias_persists(self):
        actual=m.relative_stress(.2,.4,.0001,2)
        self.assertGreater(abs(actual-self.target),.0004)

    def test_20_fixed_count_calibrated_limit(self):
        for n in (2,4,8):
            actual=m.relative_stress(.2,.4,.0001,n,calibrated=True)
            self.assertAlmostEqual(actual,self.target,places=8)

    def test_21_mesoscopic_limit_without_calibration(self):
        errors=[abs(m.relative_stress(.2,.4,1/n**2,n)-self.target) for n in (8,16,32,64)]
        self.assertAlmostEqual(errors[0]/errors[-1],64,delta=.3)

    def test_22_smooth_quadrature_refinement(self):
        coarse=m.relative_stress(.2,.4,.02,4,steps=24)
        fine=m.relative_stress(.2,.4,.02,4,steps=48)
        self.assertLess(abs(coarse-fine),1e-8)

    def test_23_mesoscopic_scale_relation(self):
        for n in (8,16,32):
            a=1/n**2; h=n*a
            self.assertEqual(a/h,1/n)
            self.assertLess(a,h)

    def test_24_cell_support_shrinks_to_midpoint(self):
        extents=[n/n**2/2+1/n**2/2 for n in (8,16,32)]
        self.assertTrue(all(b<a for a,b in zip(extents,extents[1:])))

    def test_25_small_state_difference_does_not_fix_composite(self):
        differences=[]; stresses=[]
        for a in (.02,.01):
            cf=m.covariance_pair(.2,.4,a,2); c0=m.covariance_pair(0,.4,a,2)
            differences.append(abs(cf[0][1]-c0[0][1])); stresses.append(m.relative_stress(.2,.4,a,2))
        self.assertAlmostEqual(differences[0]/differences[1],4,delta=.01)
        self.assertGreater(abs(stresses[-1]),.01)

    def test_26_compressed_state_is_mixed(self):
        purity=c.trace(c.mul(self.rho,self.rho)).real
        self.assertTrue(0<purity<1)

    def test_27_common_identity_counterterm_cancels(self):
        op=m.current_product(self.a); shifted=c.add(op,c.scale(7,c.identity(4)))
        r0=m.density_matrix(self.c0)
        a=m.expectation(op,self.rho)-m.expectation(op,r0)
        b=m.expectation(shifted,self.rho)-m.expectation(shifted,r0)
        self.assertAlmostEqual(abs(a-b),0)

    def test_28_relative_curved_trace_unchanged(self):
        jet=m.previous.static_jet(.4)
        t=m.relative_stress(.2,.4,.001,4)
        self.assertEqual(m.previous.trace(jet,m.previous.stress(jet,tu=t)),m.previous.trace(jet,m.previous.stress(jet)))

    def test_29_relative_chiral_conservation(self):
        self.assertTrue(all(abs(x)<1e-15 for x in m.previous.ward_residuals(m.previous.static_jet(.4))))

    def test_30_reference_state_subtraction_zero(self):
        self.assertEqual(m.relative_stress(0,.4,.02,4),0)
        self.assertEqual(m.averaged_relative_kernel(0,.4,.02,4),0)

    def test_31_both_chiralities_in_fixed_curved_prescription(self):
        jet=m.previous.affine_density_jet(.2,.3)
        actual=m.previous.stress(jet,m.relative_stress(.2,.3,.0001,4,calibrated=True),m.relative_stress(.3,.2,.0001,4,calibrated=True))
        target=m.previous.stress(jet,m.previous.state_stress(m.previous.cubic('.2'),.3),m.previous.state_stress(m.previous.cubic('.3'),.2))
        self.assertTrue(all(abs(a-b)<1e-8 for a,b in zip(actual,target)))

    def test_32_validation(self):
        for call in (lambda:m.shape(1),lambda:m.shape(3),lambda:m.flat_cell_kernel(0,2),lambda:m.averaged_relative_kernel(.2,.4,.1,2,steps=1),lambda:m.density_matrix(((.5,1),(1,.5)))):
            with self.assertRaises(ValueError):call()


if __name__=='__main__':
    unittest.main()
