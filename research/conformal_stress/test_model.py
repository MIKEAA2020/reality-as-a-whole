from decimal import Decimal as D, localcontext
import math
import unittest
import model as m


class StressTests(unittest.TestCase):
    def test_01_identity_subtraction(self):
        self.assertEqual(m.split_finite_kernel(m.affine(),.3,'0.0001'),0)

    def test_02_affine_subtraction(self):
        self.assertLess(abs(m.split_finite_kernel(m.affine(3,2),.3,'0.0001')),D('1e-60'))

    def test_03_mobius_subtraction(self):
        f=m.mobius()
        self.assertLess(abs(m.schwarzian(f(D('.3')))),D('1e-25'))
        self.assertLess(abs(m.split_finite_kernel(f,.3,'0.0001')),D('1e-60'))

    def test_04_cubic_schwarzian(self):
        x=.4; a=.2
        expected=6*a/(1+3*a*x*x)-1.5*(6*a*x/(1+3*a*x*x))**2
        self.assertAlmostEqual(float(m.schwarzian(m.cubic(a)(D(str(x))))),expected)

    def test_05_point_split_limit(self):
        f=m.cubic(.2); x=.4
        target=float(m.schwarzian(f(D(str(x)))))/6
        self.assertAlmostEqual(float(m.split_finite_kernel(f,x,'0.0001')),target,places=8)

    def test_06_symmetric_split_second_order(self):
        f=m.cubic(.2); x=.4; target=float(m.schwarzian(f(D(str(x)))))/6
        errors=[abs(float(m.split_finite_kernel(f,x,h))-target) for h in ('.04','.02','.01')]
        self.assertAlmostEqual(errors[0]/errors[-1],16,delta=.1)

    def test_07_schwarzian_chain_rule(self):
        f,g=m.cubic('.2'),m.cubic('.3'); x=D('.4')
        actual=m.schwarzian(m.compose_jets(f,g,x))
        y,g1,_,_=g(x)
        expected=g1*g1*m.schwarzian(f(y))+m.schwarzian(g(x))
        self.assertLess(abs(actual-expected),D('1e-24'))

    def test_08_kernel_composition(self):
        f,g=m.cubic('.2'),m.cubic('.3'); x=D('.4'); h=D('.0001')
        composed=lambda u:m.compose_jets(f,g,u)
        expected=float(m.schwarzian(composed(x)))/6
        self.assertAlmostEqual(float(m.split_finite_kernel(composed,x,h)),expected,places=7)

    def test_09_exponential_schwarzian(self):
        self.assertAlmostEqual(float(m.schwarzian(m.exponential('.7')(D('.4')))),-.7**2/2)

    def test_10_exponential_stress(self):
        k=.7; f=m.exponential(k)
        expected=k*k/(48*math.pi)
        self.assertAlmostEqual(m.state_stress(f,.4),expected)
        self.assertAlmostEqual(m.split_stress(f,.4,'0.0001'),expected,places=10)

    def test_11_thermal_two_chiralities(self):
        k=.7; temperature=k/(2*math.pi); t=m.state_stress(m.exponential(k),.4)
        tensor=m.stress(m.flat_jet(),t,t)
        self.assertAlmostEqual(tensor[0]+2*tensor[1]+tensor[2],math.pi*temperature**2/6)
        jet=m.static_jet(.4); hot=m.stress(jet,t,t); cold=m.stress(jet)
        delta_energy=math.exp(-2*jet['sigma'])*sum(a-b for a,b in zip((hot[0],2*hot[1],hot[2]),(cold[0],2*cold[1],cold[2])))
        self.assertAlmostEqual(delta_energy,math.pi*(temperature/math.exp(jet['sigma']))**2/6)

    def test_12_fermion_current_kernel_relation(self):
        with localcontext() as ctx:
            ctx.prec=80
            f=m.cubic('.2'); l,dl,_,_=f(D('.3')); r,dr,_,_=f(D('.4'))
            fermion=(dl*dr).sqrt()/(l-r)
            self.assertLess(abs(fermion**2-dl*dr/(l-r)**2),D('1e-70'))

    def test_13_flat_normalized_vacuum_stress_zero(self):
        self.assertEqual(m.stress(m.flat_jet()),(0.,0.,0.))

    def test_14_trace_anomaly(self):
        for x in (-1,0,.4,1):
            jet=m.static_jet(x)
            self.assertAlmostEqual(m.trace(jet,m.stress(jet)),m.curvature(jet)/(24*math.pi))

    def test_15_conservation_u(self):
        for x in (-1,0,.4,1):self.assertAlmostEqual(m.ward_residuals(m.static_jet(x))[0],0)

    def test_16_conservation_v(self):
        for x in (-1,0,.4,1):self.assertAlmostEqual(m.ward_residuals(m.static_jet(x))[1],0)

    def test_17_static_energy_component(self):
        jet=m.static_jet(.4); tu,tuv,tv=m.stress(jet)
        sx=2*jet['u']; sxx=4*jet['uu']; a=1/(12*math.pi)
        self.assertAlmostEqual(tu+2*tuv+tv,a*(sxx-.5*sx*sx))

    def test_18_static_pressure_component(self):
        jet=m.static_jet(.4); tu,tuv,tv=m.stress(jet)
        self.assertAlmostEqual(tu-2*tuv+tv,-(2*jet['u'])**2/(24*math.pi))

    def test_19_finite_cosmological_shift(self):
        jet=m.static_jet(.4)
        before=m.trace(jet,m.stress(jet)); after=m.trace(jet,m.stress(jet,cosmological=.3))
        self.assertAlmostEqual(after-before,.6)

    def test_20_cosmological_shift_conserved(self):
        for r in m.ward_residuals(m.static_jet(.4),cosmological=.3):self.assertAlmostEqual(r,0)

    def test_21_flat_normalization_fixes_shift(self):
        t=m.stress(m.flat_jet(),cosmological=.3)
        self.assertAlmostEqual(t[0]+2*t[1]+t[2],.3)

    def test_22_state_dependence_leaves_anomaly(self):
        jet=m.static_jet(.4)
        self.assertEqual(m.trace(jet,m.stress(jet,tu=.2,tv=.3)),m.trace(jet,m.stress(jet)))
        self.assertNotEqual(m.stress(jet,tu=.2,tv=.3),m.stress(jet))

    def test_23_nonchiral_integration_functions_fail_conservation(self):
        self.assertAlmostEqual(m.ward_residuals(m.flat_jet(),tu_v=.2)[0],.2)

    def transformed(self,jet):
        f=m.cubic('.2')(D('.3')); g=m.cubic('.3')(D('.4'))
        f1,g1=float(f[1]),float(g[1]); a=1/(24*math.pi)
        tu,tv=.2,.3
        tup=(tu+a*float(m.schwarzian(f)))/f1**2
        tvp=(tv+a*float(m.schwarzian(g)))/g1**2
        return m.stress(jet,tu,tv),m.stress(m.reparametrize_jet(jet,f,g),tup,tvp),f1,g1

    def test_24_tensor_covariance_uu(self):
        old,new,f1,g1=self.transformed(m.static_jet(.4))
        self.assertAlmostEqual(old[0],f1*f1*new[0])

    def test_25_tensor_covariance_vv(self):
        old,new,f1,g1=self.transformed(m.static_jet(.4))
        self.assertAlmostEqual(old[2],g1*g1*new[2])

    def test_26_tensor_covariance_uv_and_scalar_curvature(self):
        jet=m.static_jet(.4); old,new,f1,g1=self.transformed(jet)
        self.assertAlmostEqual(old[1],f1*g1*new[1])
        f=m.cubic('.2')(D('.3')); g=m.cubic('.3')(D('.4'))
        self.assertAlmostEqual(m.curvature(jet),m.curvature(m.reparametrize_jet(jet,f,g)))

    def test_27_state_function_not_a_tensor_alone(self):
        f=m.cubic('.2'); self.assertGreater(abs(m.state_stress(f,.3)),.001)

    def test_28_same_flat_vacuum_coordinate_cancellation(self):
        jet=m.flat_jet(); f=m.cubic('.2')(D('.3')); g=m.cubic('.3')(D('.4'))
        new=m.reparametrize_jet(jet,f,g)
        tu=float(m.schwarzian(f))/(24*math.pi*float(f[1])**2)
        tv=float(m.schwarzian(g))/(24*math.pi*float(g[1])**2)
        self.assertTrue(all(abs(x)<1e-15 for x in m.stress(new,tu,tv)))

    def test_29_affine_density_curvature_and_conservation(self):
        jet=m.affine_density_jet(.2,.3); rho=1+.2/3+.3/2
        self.assertAlmostEqual(m.curvature(jet),(1/3)/rho**3)
        self.assertTrue(all(abs(x)<1e-15 for x in m.ward_residuals(jet)))
        self.assertAlmostEqual(m.trace(jet,m.stress(jet)),m.curvature(jet)/(24*math.pi))

    def test_30_central_charge_linearity(self):
        jet=m.static_jet(.4)
        self.assertTrue(all(abs(b-2*a)<1e-15 for a,b in zip(m.stress(jet),m.stress(jet,central_charge=2))))

    def test_31_polyakov_weyl_variation_density(self):
        jet=m.affine_density_jet(.2,.3)
        trace_density=math.exp(2*jet['sigma'])*m.trace(jet,m.stress(jet))
        box_sigma=4*jet['uv']
        self.assertAlmostEqual(trace_density,-box_sigma/(12*math.pi))

    def test_32_validation(self):
        for call in (lambda:m.affine(0),lambda:m.cubic(-1),lambda:m.exponential(0),lambda:m.mobius(1,0,0,-1),lambda:m.split_finite_kernel(m.affine(),0,0),lambda:m.static_jet(0,epsilon=1),lambda:m.affine_density_jet(0,0,a=0)):
            with self.assertRaises(ValueError):call()


if __name__=='__main__':
    unittest.main()
