import math
import unittest
import model as m
class InfiniteRankTests(unittest.TestCase):
    def test_01_occupation_sum(self):self.assertAlmostEqual(sum(m.occupation(i) for i in range(20)),m.particle_number(20))
    def test_02_disjoint_bands(self):
        for i in range(10):
            lo,d=m.band(i+1);self.assertAlmostEqual(lo+d,m.band(i)[0])
    def test_03_normalized_rescaled_amplitude(self):self.assertAlmostEqual(m.w.simpson(lambda z:30*z*z*(1-z)**2,1,800),1,places=10)
    def test_04_compact_common_band(self):
        for i in range(20):
            lo,d=m.band(i);self.assertTrue(1<=lo<lo+d<=2)
    def test_05_B0(self):self.assertAlmostEqual(m.B(0,0),math.sqrt(15/(2*math.pi))/6)
    def test_06_packet_bound(self):self.assertLessEqual(abs(m.packet(3,.4,.3,.02)),m.B(3,0))
    def test_07_translation(self):self.assertAlmostEqual(m.packet(2,.7,.3),m.packet(2,.4),places=12)
    def test_08_derivative(self):
        eps=1e-5;fd=(m.packet(2,.4+eps)-m.packet(2,.4-eps))/(2*eps)
        self.assertAlmostEqual(fd,m.packet(2,.4,j=1),places=9)
    def test_09_trace_tail(self):self.assertAlmostEqual(sum(m.occupation(i) for i in range(6,30)),2**-6,places=8)
    def test_10_target_tail(self):self.assertLessEqual(abs(m.target(.7,.3,20)-m.target(.7,.3,6)),m.target_tail(6))
    def test_11_current_tail(self):self.assertLessEqual(abs(m.current(.02,4,.7,.3,16)-m.current(.02,4,.7,.3,6)),m.tail_bound(.02,4,6))
    def test_12_gram_nonnegative(self):self.assertGreaterEqual(m.terms(.02,4,.7,.3,6)[1],0)
    def test_13_total_bound(self):
        for n in (8,16,32):
            a=1/n**2;self.assertLessEqual(abs(m.current(a,n,.7,.3,12)-m.target(.7,.3,12)),m.error_bound(a,n,.3)+m.tail_bound(a,n,12)+m.target_tail(12))
    def test_14_mesoscopic(self):self.assertLess(abs(m.current(1/64**2,64,.7,.3,12)-m.target(.7,.3,12)),1e-5)
    def test_15_fixed_site_factor(self):self.assertAlmostEqual(m.current(.0001,2,.7,.3,12),m.w.shape(2)*m.target(.7,.3,12),places=7)
    def test_16_covariance_positive(self):self.assertTrue(all(0<=z<=1 for z in m.r.p.eigenvalues(m.covariance(.02,2,.4,.3,8))))
    def test_17_actual_fock(self):
        a,n,x,t=.02,2,.4,.3;c=m.w.cell;rho=m.r.p.density_matrix(m.covariance(a,n,x,t,8));ref=c.density_matrix(m.w.same_chirality_covariance(a,n));op=c.current_product(a)
        self.assertAlmostEqual((c.expectation(op,rho)-c.expectation(op,ref)).real,m.current(a,n,x,t,8),places=9)
    def test_18_total_energy_limit(self):self.assertAlmostEqual(m.total_energy(30),1.5,places=8)
    def test_19_energy_tail(self):
        self.assertLessEqual(1.5-m.total_energy(8),2*2**-8)
        for a in (.1,.05,.01):self.assertLessEqual(abs(m.wilson_energy(a,16)-m.total_energy(16)),a*a/3+1e-9)
    def test_20_tail_quartic_decay(self):self.assertAlmostEqual(m.target_tail(5)/m.target_tail(6),4)
    def test_21_quadrature_refinement(self):self.assertAlmostEqual(m.packet(2,.4,.3,.02,steps=200),m.packet(2,.4,.3,.02,steps=400),places=10)
    def test_22_joint_rank_spacing(self):
        errors=[]
        for n in (8,16,32):errors.append(abs(m.current(1/n**2,n,.7,.3,int(math.log2(n)))-m.target(.7,.3,16)))
        self.assertLess(errors[-1],errors[0]/8)
    def test_23_infinite_rank_not_infinite_number(self):self.assertTrue(all(m.occupation(i)>0 for i in range(30)));self.assertLess(m.particle_number(30),1)
    def test_24_validation(self):
        for call in (lambda:m.current(2,2,0),lambda:m.current(.1,0,0),lambda:m.current(.1,2,0,count=0),lambda:m.band(-1),lambda:m.tail_moment(-1,0)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
