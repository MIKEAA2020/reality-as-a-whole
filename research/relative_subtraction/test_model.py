from decimal import Decimal as D
import math
import unittest
import model as m

p=m.previous


class RelativeSubtractionTests(unittest.TestCase):
    def test_01_exact_remainder_matches_split(self):
        f=p.cubic('.2')
        for h in (.1,.01,.001):
            self.assertAlmostEqual(m.remainder(.2,.4,h),float(p.split_finite_kernel(f,.4,str(h))),places=13)

    def test_02_coincident_remainder(self):
        target=float(p.schwarzian(p.cubic('.2')(D('.4'))))/6
        self.assertAlmostEqual(m.remainder(.2,.4,0),target)

    def test_03_even_remainder(self):
        self.assertEqual(m.remainder(.2,.4,.3),m.remainder(.2,.4,-.3))

    def test_04_real_quadratic_bound(self):
        bound=m.quadratic_bound(.2,.4)
        for z in (-.7,-.1,.1,.7):
            self.assertLessEqual(abs(m.remainder(.2,.4,z)-m.remainder(.2,.4,0)),bound*z*z+1e-15)

    def test_05_complex_quadratic_bound(self):
        bound=m.quadratic_bound(.2,.4)
        for z in (.2-.1j,.01-.3j,.3j):
            self.assertLessEqual(abs(m.remainder(.2,.4,z)-m.remainder(.2,.4,0)),bound*abs(z)**2+1e-15)

    def test_06_unsafe_affine_cutoff_invents_stress(self):
        artifact=m.naive_affine_real(2,'0.00001','0.0000000001')
        self.assertAlmostEqual(float(artifact),2.25,places=7)
        self.assertEqual(p.state_stress(p.affine(2),.4),0)

    def test_07_epsilon_over_h_zero_not_sufficient(self):
        h=D('.00001'); epsilon=h*h
        self.assertLess(epsilon/h,D('.0001'))
        self.assertGreater(abs(m.naive_affine_real(2,h,epsilon)),2)

    def test_08_affine_artifact_coefficient(self):
        h=D('.00001'); scale=D(3); rate=D('.7')
        actual=m.naive_affine_real(scale,h,rate*h*h)
        expected=3*rate*rate*(1-1/(scale*scale))
        self.assertAlmostEqual(float(actual),float(expected),places=7)

    def test_09_unmatched_slow_regulator_diverges(self):
        first=abs(m.naive_affine_real(2,'.01','.001'))
        second=abs(m.naive_affine_real(2,'.0001','.000001'))
        self.assertGreater(second,first*50)

    def test_10_sufficient_fast_unmatched_path(self):
        h=D('.0001')
        self.assertLess(abs(m.naive_affine_real(2,h,h**3)),D('1e-6'))

    def test_11_cutoff_first_limit(self):
        h=D('.01')
        a=abs(m.naive_affine_real(2,h,'0.00001'))
        b=abs(m.naive_affine_real(2,h,'0.00000001'))
        self.assertLess(b,a/100000)

    def test_12_coincidence_first_is_wrong_for_unmatched_cutoff(self):
        self.assertEqual(m.naive_affine_real(2,0,'.01'),D(-30000))

    def test_13_correct_affine_cutoff_transport(self):
        for h,e in (('.1','.01'),('0','.01'),('.00001','.0001')):
            self.assertLess(abs(m.matched_affine_real(2,h,e)),D('1e-60'))

    def test_14_matched_analytic_equal_scale_path(self):
        target=m.remainder(.2,.4,0)
        errors=[abs(m.analytic_regulator(.2,.4,h,h)-target) for h in (.1,.05,.025)]
        self.assertLess(errors[-1],errors[0]/10)

    def test_15_analytic_regulator_may_dominate_separation(self):
        target=m.remainder(.2,.4,0)
        h=1e-8; epsilon=1e-4
        self.assertLess(abs(m.analytic_regulator(.2,.4,h,epsilon)-target),1e-8)

    def test_16_analytic_coincidence_first(self):
        target=m.remainder(.2,.4,0)
        self.assertLess(abs(m.analytic_regulator(.2,.4,0,1e-4)-target),1e-8)

    def test_17_unregulated_split_recovered(self):
        self.assertEqual(m.analytic_regulator(.2,.4,.1,0),m.remainder(.2,.4,.1))

    def test_18_mollifier_normalized_even(self):
        for variant in (0,1):
            samples=m.mollifier_samples(400,variant)
            self.assertAlmostEqual(sum(w for _,w in samples),1)
            self.assertAlmostEqual(sum(s*w for s,w in samples),0)
            self.assertTrue(all(w>0 for _,w in samples))

    def test_19_common_mollifier_joint_limit(self):
        target=m.remainder(.2,.4,0)
        errors=[abs(m.mollify(.2,.4,h,h)-target) for h in (.1,.05,.025)]
        self.assertLess(errors[-1],errors[0]/10)

    def test_20_mollifier_coincidence_first(self):
        self.assertLess(abs(m.mollify(.2,.4,0,1e-4)-m.remainder(.2,.4,0)),1e-8)

    def test_21_mollifier_uniform_error_bound(self):
        bound=m.quadratic_bound(.2,.4)
        for h,e in ((.1,.2),(0,.2),(.2,0),(.01,.01)):
            self.assertLessEqual(abs(m.mollify(.2,.4,h,e)-m.remainder(.2,.4,0)),bound*(h*h+e*e)+1e-14)

    def test_22_same_linear_regulator_commutes_with_subtraction(self):
        direct=m.mollify_separately_off_diagonal(.2,.4,.1,.02,100)
        subtracted=m.mollify(.2,.4,.1,.02,100)
        self.assertAlmostEqual(direct,subtracted,places=14)

    def test_23_relative_stress_normalization(self):
        target=p.state_stress(p.cubic('.2'),.4)
        self.assertAlmostEqual(m.relative_stress(.2,.4),target)
        self.assertAlmostEqual(m.relative_stress(.2,.4,epsilon=1e-4),target,places=9)

    def test_24_curved_relative_trace_zero(self):
        jet=p.static_jet(.4); t=m.relative_stress(.2,.3)
        ref=p.stress(jet); state=p.stress(jet,tu=t)
        self.assertEqual(p.trace(jet,ref),p.trace(jet,state))
        self.assertNotEqual(ref,state)

    def test_25_relative_chiral_term_conserved(self):
        # The addition depends on u only; its crossed derivative is zero.
        self.assertTrue(all(abs(x)<1e-15 for x in p.ward_residuals(p.static_jet(.4),tu_v=0,tv_u=0)))

    def test_26_relative_tensor_covariance(self):
        fj=p.cubic('.3')(D('.4')); first=float(fj[1]); s=float(p.schwarzian(fj))/(24*math.pi)
        ta,tb=.2,-.1
        transformed_a=(ta+s)/first**2; transformed_b=(tb+s)/first**2
        self.assertAlmostEqual(ta-tb,first**2*(transformed_a-transformed_b))

    def test_27_cosmological_ambiguity_cancels_relatively(self):
        jet=p.static_jet(.4); t=m.relative_stress(.2,.3)
        def difference(shift):
            return tuple(a-b for a,b in zip(p.stress(jet,tu=t,cosmological=shift),p.stress(jet,cosmological=shift)))
        for a,b in zip(difference(0),difference(.7)):self.assertAlmostEqual(a,b)

    def test_28_full_curved_stress_limit_in_declared_scheme(self):
        jet=p.affine_density_jet(.2,.3)
        expected=p.stress(jet,p.state_stress(p.cubic('.2'),.3),p.state_stress(p.cubic('.3'),.2))
        actual=p.stress(jet,m.relative_stress(.2,.3,.0001,.0002),m.relative_stress(.3,.2,.0001,.0002))
        self.assertTrue(all(abs(a-b)<1e-9 for a,b in zip(actual,expected)))

    def test_29_two_common_smoothing_kernels_same_limit(self):
        target=m.remainder(.2,.4,0)
        for variant in (0,1):
            self.assertLess(abs(m.mollify(.2,.4,.0001,.0001,variant=variant)-target),1e-8)

    def test_30_real_and_analytic_regulators_same_limit(self):
        real=m.mollify(.2,.4,.0001,.0001)
        analytic=m.analytic_regulator(.2,.4,.0001,.0001)
        self.assertLess(abs(real-analytic),1e-8)

    def test_31_stable_tiny_separation(self):
        self.assertAlmostEqual(m.remainder(.2,.4,1e-12),m.remainder(.2,.4,0),places=15)

    def test_32_validation(self):
        for call in (lambda:m.remainder(-1,0,0),lambda:m.quadratic_bound(.2,.4,0),lambda:m.analytic_regulator(.2,.4,.1,-1),lambda:m.mollifier_samples(1),lambda:m.mollify(.2,.4,0,-1),lambda:m.mollify_separately_off_diagonal(.2,.4,.01,.1),lambda:m.naive_affine_real(0,.1,.1)):
            with self.assertRaises(ValueError):call()


if __name__=='__main__':
    unittest.main()
