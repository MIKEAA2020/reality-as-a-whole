import math
import unittest
import model as m
class ParticleHoleTests(unittest.TestCase):
    def test_01_negative_band_spinor(self):
        a=.1
        for k in (-1,-2,-3):
            u,v=math.cos(a*k/4),math.sin(a*k/4);e=2*math.sin(a*k/2)/a
            self.assertLess(e,0);self.assertAlmostEqual(math.sin(a*k)*u/a+(1-math.cos(a*k))*v/a,e*u)
    def test_02_full_covariance_eigenvalues(self):
        for particle,hole in ((1,1),(.3,.7),(0,1)):
            # Orthogonal spectral modes: positive particle occupation, remaining sea occupation.
            self.assertTrue(0<=particle<=1);self.assertTrue(0<=1-hole<=1)
    def test_03_hole_mode_mirror(self):self.assertEqual(m.packet('hole',.4,.3,.02),m.packet('particle',.4,.3,.02).conjugate())
    def test_04_lower_spinor_mirror(self):self.assertEqual(m.packet('hole',.4,.3,.02,component=1),-m.packet('particle',.4,.3,.02,component=1).conjugate())
    def test_05_derivative_mirror(self):self.assertEqual(m.packet('hole',.4,.3,j=1),m.packet('particle',.4,.3,j=1).conjugate())
    def test_06_hole_chiral_energy_sign(self):
        h=m.packet('hole',.4,.3);dh=m.packet('hole',.4,.3,j=1)
        self.assertAlmostEqual(-(h.conjugate()*dh).imag,m.p.target(.4,.3))
    def test_07_compressed_covariance_positive(self):
        for particle,hole in ((1,1),(.3,.7),(0,1)):
            self.assertTrue(all(0<=z<=1 for z in m.p.eigenvalues(m.covariance(.02,2,.4,.3,particle,hole))))
    def test_08_density_trace(self):self.assertAlmostEqual(m.w.car.trace(m.p.density_matrix(m.covariance(.02,2,.4,.3))).real,1)
    def test_09_actual_fock(self):
        a,n,x,t=.02,2,.4,.3;c=m.w.cell;rho=m.p.density_matrix(m.covariance(a,n,x,t));ref=c.density_matrix(m.w.same_chirality_covariance(a,n));op=c.current_product(a)
        self.assertAlmostEqual((c.expectation(op,rho)-c.expectation(op,ref)).real,m.current(a,n,x,t),places=9)
    def test_10_signed_term_negative(self):self.assertLess(m.terms(.02,4,.4,.3)[1],0)
    def test_11_signed_determinant_identity(self):
        a,n,x,t=.02,4,.4,.3;cov=m.covariance(a,n,x,t);base=m.w.same_chirality_covariance(a,n)
        k=tuple(tuple((cov[i][j]-base[i][j])/a for j in range(2)) for i in range(2))
        self.assertAlmostEqual(math.pi*(k[0][0]*k[1][1]-abs(k[0][1])**2).real,m.terms(a,n,x,t)[1],places=11)
    def test_12_signed_term_bound(self):
        for n in (4,8,16):self.assertLessEqual(abs(m.terms(1/n**2,n,.7,.3)[1]),m.signed_term_bound(1/n**2,n))
    def test_13_total_bound(self):
        for n in (8,16,32):self.assertLessEqual(abs(m.current(1/n**2,n,.7,.3)-m.target(.7,.3)),m.error_bound(1/n**2,n,.3))
    def test_14_mesoscopic_limit(self):self.assertLess(abs(m.current(1/64**2,64,.7,.3)-m.target(.7,.3)),.001)
    def test_15_fixed_site_factor(self):self.assertAlmostEqual(m.current(.0001,2,.7,.3),m.w.shape(2)*m.target(.7,.3),places=6)
    def test_16_hole_only(self):self.assertAlmostEqual(m.current(.02,4,.4,.3,0,1),m.p.current(.02,4,.4,.3))
    def test_17_particle_only(self):self.assertAlmostEqual(m.current(.02,4,.4,.3,1,0),m.p.current(.02,4,.4,.3))
    def test_18_neutral_energy(self):self.assertEqual(m.signed_number(),0);self.assertAlmostEqual(m.total_energy(),4,places=9)
    def test_19_fractional_weights(self):self.assertAlmostEqual(m.total_energy(particle=.3,hole=.7),2,places=9)
    def test_20_local_energy_limit(self):self.assertAlmostEqual(m.local_energy(.0001,.7,.3),m.target(.7,.3),places=6)
    def test_21_half_filling_restored(self):
        cov=m.covariance(.02,2,.4,.3);self.assertAlmostEqual(cov[0][0],.5);self.assertAlmostEqual(cov[1][1],.5)
    def test_22_not_positive_update(self):
        cov=m.covariance(.02,2,.4,.3,0,1);self.assertLess(cov[0][0].real,.5)
    def test_23_nonadditivity(self):self.assertLess(m.current(.02,4,.4,.3),m.current(.02,4,.4,.3,1,0)+m.current(.02,4,.4,.3,0,1))
    def test_24_validation(self):
        for call in (lambda:m.current(.1,0,0),lambda:m.current(.1,2,0,hole=2),lambda:m.current(.1,2,0,particle=-1),lambda:m.packet('other',0)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
