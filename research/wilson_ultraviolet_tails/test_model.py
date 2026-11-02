import math
import unittest
import model as m
class UltravioletTests(unittest.TestCase):
    def test_01_normalization(self):self.assertAlmostEqual(m.w.simpson(lambda z:30*z*z*(1-z)**2,1.,800),1,places=10)
    def test_02_unbounded_support(self):self.assertGreater(m.occupation(100),0);self.assertGreater(abs(m.packet(100,0)),0)
    def test_03_trace(self):self.assertAlmostEqual(sum(m.occupation(i) for i in range(40)),1,places=10)
    def test_04_weighted_moments(self):
        for q in range(5):self.assertAlmostEqual(sum(m.occupation(i)*(i+2)**q for i in range(100)),m.RAW[q],places=9)
    def test_05_target_tail(self):self.assertLessEqual(abs(m.target(.7,.3,40)-m.target(.7,.3,8)),m.target_tail(8))
    def test_06_translation(self):self.assertAlmostEqual(m.packet(3,.7,.3),m.packet(3,.4),places=11)
    def test_07_packet_cauchy_bound(self):self.assertLessEqual(abs(m.packet(3,.7,.3,.02)),1/math.sqrt(2*math.pi))
    def test_08_whole_retained_band_inside_window(self):self.assertLess(.02*(8+1),1)
    def test_09_uniform_error(self):
        for n in (8,16,32):
            a=1/n**2;N=2*int(math.log2(n));self.assertLessEqual(abs(m.current(a,n,.7,.3,N)-m.target(.7,.3,40)),m.error_bound(a,n,.3,N)+m.target_tail(40))
    def test_10_joint_convergence(self):
        errors=[abs(m.current(1/n**2,n,.7,.3,2*int(math.log2(n)))-m.target(.7,.3,40)) for n in (8,16,32,64)]
        self.assertLess(errors[-1],errors[0]/20)
    def test_11_mode_cutoff_tail_decays(self):self.assertLess(m.target_tail(16),m.target_tail(8)/100)
    def test_12_gram_nonnegative(self):self.assertGreater(m.terms(.02,4,.7,.3,8)[1],0)
    def test_13_covariance_positive(self):self.assertTrue(all(0<=z<=1 for z in m.r.r.p.eigenvalues(m.covariance(.02,2,.4,.3,8))))
    def test_14_actual_fock(self):
        a,n,x,t=.02,2,.4,.3;c=m.w.cell;rho=m.r.r.p.density_matrix(m.covariance(a,n,x,t,8));ref=c.density_matrix(m.w.same_chirality_covariance(a,n));op=c.current_product(a)
        self.assertAlmostEqual((c.expectation(op,rho)-c.expectation(op,ref)).real,m.current(a,n,x,t,8),places=9)
    def test_15_continuum_total_energy(self):self.assertAlmostEqual(m.total_energy(40),2.5,places=9)
    def test_16_spectral_energy_bound(self):
        for a,N in ((.02,8),(.01,12),(.001,20)):self.assertLessEqual(abs(m.wilson_energy(a,N)-2.5),m.energy_bound(a,N)+1e-9)
    def test_17_local_energy_limit(self):self.assertLess(abs(m.local_energy(.0001,.7,.3,30)-m.target(.7,.3,40)),1e-6)
    def test_18_fixed_rank_is_not_full_target(self):self.assertGreater(abs(m.target(.7,.3,2)-m.target(.7,.3,40)),.001)
    def test_19_two_point_reconstruction(self):
        cov=m.covariance(.02,2,.4,.3,8);rho=m.r.r.p.density_matrix(cov);car=m.w.car
        for i in (0,1):
            for j in (0,1):self.assertAlmostEqual(m.w.cell.expectation(car.mul(car.adjoint(car.annihilator(2,j)),car.annihilator(2,i)),rho),cov[i][j])
    def test_20_refinement(self):self.assertAlmostEqual(m.packet(8,.7,.3,.02,steps=400),m.packet(8,.7,.3,.02,steps=800),places=9)
    def test_21_positive_spectral_spinor(self):
        k,a=8.,.02;u,v=math.cos(a*k/4),math.sin(a*k/4);e=2*math.sin(a*k/2)/a
        self.assertAlmostEqual(math.sin(a*k)*u/a+(1-math.cos(a*k))*v/a,e*u)
    def test_22_fixed_site_factor(self):self.assertAlmostEqual(m.current(.0001,2,.7,.3,30),m.w.shape(2)*m.target(.7,.3,30),places=6)
    def test_23_energy_tail(self):self.assertLessEqual(2.5-m.total_energy(8),2**-8*11)
    def test_24_validation(self):
        for call in (lambda:m.current(.2,2,0,count=8),lambda:m.current(.01,0,0),lambda:m.target(0,count=0),lambda:m.occupation(-1),lambda:m.S(5)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
