import math
import unittest
import model as m
class PacketTests(unittest.TestCase):
    def test_01_normalization(self):self.assertAlmostEqual(m.integral(lambda k:m.amplitude(k)**2),1,places=10)
    def test_02_positive_energy_support(self):self.assertEqual(m.amplitude(0),0);self.assertEqual(m.amplitude(4),0)
    def test_03_spinor_normalized(self):
        for k in (1,2,3):self.assertAlmostEqual(math.cos(.1*k/4)**2+math.sin(.1*k/4)**2,1)
    def test_04_eigenvector(self):
        a=.1
        for k in (1,2,3):
            z=math.sin(a*k)/a;b=(1-math.cos(a*k))/a;e=2*math.sin(a*k/2)/a;u,v=math.cos(a*k/4),math.sin(a*k/4)
            self.assertAlmostEqual(z*u+b*v,e*u);self.assertAlmostEqual(b*u-z*v,e*v)
    def test_05_continuum_translation(self):self.assertAlmostEqual(abs(m.packet(.7,.3)-m.packet(.4)),0,places=12)
    def test_06_nonconstant_density(self):self.assertNotAlmostEqual(abs(m.packet(0))**2,abs(m.packet(2))**2)
    def test_07_time_variation(self):self.assertNotAlmostEqual(abs(m.packet(0,0,.1))**2,abs(m.packet(0,1,.1))**2)
    def test_08_spinor_limit(self):self.assertLess(abs(m.packet(.4,.3,.001)-m.packet(.4,.3)),1e-6)
    def test_09_wrong_chirality_vanishes(self):self.assertLess(abs(m.packet(.4,.3,.001,component=1)),.001)
    def test_10_derivative_bound(self):
        for j in (0,1):self.assertLessEqual(abs(m.packet(.4,.3,.02,j)-m.packet(.4,.3,derivative=j)),.02**2*m.D(j,.3)+1e-12)
    def test_11_current_bound(self):
        for x,t in ((0,0),(.7,.3),(2,1)):
            for n in (4,8,16):
                a=1/n**2;self.assertLessEqual(abs(m.current(a,n,x,t)-m.target(x,t)),m.error_bound(a,n,t)+1e-11)
    def test_12_current_convergence(self):self.assertLess(abs(m.current(1/64**2,64,.7,.3)-m.target(.7,.3)),1e-4)
    def test_13_fixed_count_artifact(self):self.assertAlmostEqual(m.current(.0001,2,.7,.3),m.w.shape(2)*m.target(.7,.3),places=7)
    def test_14_covariance_positive(self):self.assertTrue(all(0<=x<=1 for x in m.eigenvalues(m.covariance(.02,2,.4,.3))))
    def test_15_actual_fock_expectation(self):
        a,n,x,t=.02,2,.4,.3;c=m.w.cell
        rho=m.density_matrix(m.covariance(a,n,x,t));ref=c.density_matrix(m.w.same_chirality_covariance(a,n));op=c.current_product(a)
        actual=c.expectation(op,rho)-c.expectation(op,ref)
        self.assertAlmostEqual(actual.real,m.current(a,n,x,t),places=9)
    def test_16_linear_weight(self):self.assertAlmostEqual(m.current(.02,4,.4,.3,.3),.3*m.current(.02,4,.4,.3))
    def test_17_local_energy_limit(self):self.assertAlmostEqual(m.local_energy(.0001,.4,.3),m.target(.4,.3),places=7)
    def test_18_integrated_energy(self):self.assertAlmostEqual(m.total_energy(),2,places=10)
    def test_19_total_energy_limit(self):self.assertAlmostEqual(m.total_energy(.0001),m.total_energy(),places=7)
    def test_20_zero_excitation(self):self.assertEqual(m.current(.02,4,0,weight=0),0)
    def test_21_refinement(self):self.assertAlmostEqual(m.packet(.4,.3,.02),m.packet(.4,.3,.02,steps=1600),places=10)
    def test_22_packet_not_eigenstate(self):self.assertGreater(m.integral(lambda k:(k-2)**2*m.amplitude(k)**2),0)
    def test_23_no_opposite_continuum_component(self):self.assertEqual(m.packet(1,component=1),0)
    def test_24_validation(self):
        for call in (lambda:m.current(2,1,0),lambda:m.current(.1,0,0),lambda:m.current(.1,1,0,weight=2),lambda:m.packet(0,derivative=-1)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
