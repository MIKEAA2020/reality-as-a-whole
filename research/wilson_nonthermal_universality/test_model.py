import math
import unittest
import model as m

class NonthermalTests(unittest.TestCase):
    def test_01_occupation_positive(self):
        for p in (0,.1,.8,1,2):self.assertTrue(0<=m.occupation(p)<=.5)
    def test_02_compact_support(self):self.assertEqual(m.occupation(2),0)
    def test_03_moment1(self):self.assertAlmostEqual(m.moment(1),1/6)
    def test_04_moment3(self):self.assertAlmostEqual(m.moment(3),1/20)
    def test_05_moment_quadrature(self):
        for k in (1,3):self.assertAlmostEqual(m.w.simpson(lambda p:2*p**k*m.occupation(p),1,1600),m.moment(k),places=12)
    def test_06_fibre_positive(self):
        for p in (0,.5,1,2):
            f=m.occupation(p); self.assertTrue(0<=1-f<=1)
    def test_07_stationarity(self):
        h=((1.,2.),(2.,-1.)); e=math.sqrt(5); f=m.occupation(e,.4,4)
        c=tuple(tuple(.5*((i==j)-(1-2*f)*h[i][j]/e) for j in range(2)) for i in range(2))
        self.assertEqual(m.w.car.dense_mul(h,c),m.w.car.dense_mul(c,h))
    def test_08_not_thermal(self):
        self.assertEqual(m.occupation(2),0);self.assertGreater(m.w.fermi_tail(2,2.5),0)
    def test_09_ratio_bound(self):
        for n in (4,8,16,32):
            a=1/n**2;r,_=m.ratios(a,n)
            self.assertLessEqual(abs(r+m.moment(1)),m.ratio_bound(a,n)+1e-12)
    def test_10_energy_bound(self):
        for a in (.1,.05,.01):self.assertLessEqual(abs(m.energy(a)-2*m.target()),m.energy_bound(a)+1e-12)
    def test_11_current_limit(self):self.assertLess(abs(m.current(1/64**2,64)-m.target()),2e-6)
    def test_12_fixed_site_factor(self):
        for n in (1,2,4):self.assertAlmostEqual(m.current(.0001,n),m.w.shape(n)*m.target(),places=8)
    def test_13_mixed_fixed_limit(self):
        for n in (1,2,4):self.assertAlmostEqual(m.mixed(.0001,n),-m.target()/(4*n*n-1),places=8)
    def test_14_mixed_vanishes(self):self.assertLess(abs(m.mixed(1/64**2,64)),2e-6)
    def test_15_energy_current_agree(self):self.assertLess(abs(2*m.current(1/64**2,64)-m.energy(1/64**2)),3e-6)
    def test_16_equal_stress_targets(self):self.assertEqual(m.target(.5,1),m.target(.125,2))
    def test_17_different_higher_moments(self):self.assertEqual(m.moment(3,.125,2),4*m.moment(3,.5,1))
    def test_18_different_states(self):self.assertNotEqual(m.occupation(.5,.5,1),m.occupation(.5,.125,2))
    def test_19_finite_spacing_discriminates(self):self.assertGreater(abs(m.energy(.1,.5,1)-m.energy(.1,.125,2)),1e-5)
    def test_20_positive_covariance(self):self.assertTrue(all(0<=x<=1 for x in m.w.cell.covariance_eigenvalues(m.covariance(.02,2))))
    def test_21_actual_operator(self):
        a,n=.02,2;c=m.w.cell;rho=c.density_matrix(m.covariance(a,n));ref=c.density_matrix(m.w.same_chirality_covariance(a,n))
        actual=c.expectation(c.current_product(a),rho)-c.expectation(c.current_product(a),ref)
        self.assertAlmostEqual(actual.real,m.current(a,n),places=10)
    def test_22_zero_excitation(self):self.assertEqual(m.current(.01,2,0),0);self.assertEqual(m.energy(.01,0),0)
    def test_23_refinement(self):self.assertAlmostEqual(m.current(.02,4,steps=800),m.current(.02,4,steps=1600),places=11)
    def test_24_validation(self):
        for call in (lambda:m.occupation(1,-1),lambda:m.occupation(1,.6),lambda:m.occupation(-1),lambda:m.moment(-1),lambda:m.current(2,1),lambda:m.current(.1,0)):
            with self.assertRaises(ValueError):call()

if __name__=='__main__':unittest.main()
