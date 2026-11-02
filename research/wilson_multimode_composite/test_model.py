import math
import unittest
import model as m
class MultimodeTests(unittest.TestCase):
    def test_01_first_mode_normalization(self):self.assertAlmostEqual(m.p.integral(lambda k:m.amplitude(k,0)**2),1,places=10)
    def test_02_second_mode_normalization(self):self.assertAlmostEqual(m.p.integral(lambda k:m.amplitude(k,1)**2),1,places=9)
    def test_03_orthogonality(self):self.assertAlmostEqual(m.p.integral(lambda k:m.amplitude(k,0)*m.amplitude(k,1)),0,places=12)
    def test_04_packet_formula(self):
        import cmath
        direct=m.p.integral(lambda k:m.amplitude(k,1)*cmath.exp(1j*k*.4))/math.sqrt(2*math.pi)
        self.assertAlmostEqual(m.packet(1,.4),direct,places=11)
    def test_05_continuum_translation(self):self.assertAlmostEqual(m.packet(1,.7,.3),m.packet(1,.4),places=11)
    def test_06_partial_occupations_positive(self):
        for v in ((1,1),(.3,.8),(0,1)):
            self.assertTrue(all(0<=z<=1 for z in m.p.eigenvalues(m.covariance(.02,2,.4,.3,v))))
    def test_07_density_normalized(self):self.assertAlmostEqual(m.w.car.trace(m.p.density_matrix(m.covariance(.02,2,.4,.3))).real,1)
    def test_08_actual_fock_expectation(self):
        a,n,x,t=.02,2,.4,.3;c=m.w.cell;rho=m.p.density_matrix(m.covariance(a,n,x,t));ref=c.density_matrix(m.w.same_chirality_covariance(a,n));op=c.current_product(a)
        self.assertAlmostEqual((c.expectation(op,rho)-c.expectation(op,ref)).real,m.current(a,n,x,t),places=9)
    def test_09_gram_determinant(self):
        a,n,x,t=.02,4,.4,.3;h=a*n;u,v=x+h/2,x-h/2
        det=(m.kernel(u,u,t,a)*m.kernel(v,v,t,a)-abs(m.kernel(u,v,t,a))**2).real
        self.assertAlmostEqual(math.pi*det,m.terms(a,n,x,t)[1],places=12)
    def test_10_exchange_nonzero(self):self.assertGreater(m.terms(.02,4,.4,.3)[1],1e-6)
    def test_11_exchange_bound(self):
        for n in (4,8,16):self.assertLessEqual(m.terms(1/n**2,n,.7,.3)[1],m.exchange_bound(1/n**2,n))
    def test_12_exchange_quadratic_decay(self):
        values=[m.terms(1/n**2,n,.7,.3)[1] for n in (8,16,32)]
        self.assertLess(values[-1],values[0]/12)
    def test_13_total_error_bound(self):
        for n in (8,16,32):
            a=1/n**2;self.assertLessEqual(abs(m.current(a,n,.7,.3)-m.target(.7,.3)),m.error_bound(a,n,.3))
    def test_14_mesoscopic_limit(self):self.assertLess(abs(m.current(1/64**2,64,.7,.3)-m.target(.7,.3)),.001)
    def test_15_fixed_count_factor(self):self.assertAlmostEqual(m.current(.0001,2,.7,.3),m.w.shape(2)*m.target(.7,.3),places=6)
    def test_16_local_energy_limit(self):self.assertAlmostEqual(m.local_energy(.0001,.7,.3),m.target(.7,.3),places=6)
    def test_17_total_energy_four(self):self.assertAlmostEqual(sum(m.p.integral(lambda k:k*m.amplitude(k,i)**2) for i in (0,1)),4,places=9)
    def test_18_single_mode_reduction(self):self.assertAlmostEqual(m.current(.02,4,.4,.3,(1,0)),m.p.current(.02,4,.4,.3))
    def test_19_vacuum_reduction(self):self.assertEqual(m.current(.02,4,.4,.3,(0,0)),0)
    def test_20_not_linear_in_both_occupations(self):
        full=m.current(.02,4,.4,.3);linear=m.current(.02,4,.4,.3,(1,0))+m.current(.02,4,.4,.3,(0,1))
        self.assertGreater(full-linear,1e-6)
    def test_21_exchange_weight_product(self):self.assertAlmostEqual(m.terms(.02,4,.4,.3,(.3,.8))[1],.24*m.terms(.02,4,.4,.3)[1])
    def test_22_derivative_bound_second_mode(self):self.assertLessEqual(abs(m.packet(1,.4,.3,.02,1)-m.packet(1,.4,.3,derivative=1)),.02**2*m.D(1,1,.3)+1e-12)
    def test_23_two_point_reconstruction(self):
        cov=m.covariance(.02,2,.4,.3);rho=m.p.density_matrix(cov);car=m.w.car
        for i in (0,1):
            for j in (0,1):self.assertAlmostEqual(m.w.cell.expectation(car.mul(car.adjoint(car.annihilator(2,j)),car.annihilator(2,i)),rho),cov[i][j])
    def test_24_validation(self):
        for call in (lambda:m.current(.1,2,0,occupations=(1,2)),lambda:m.current(.1,2,0,occupations=(1,)),lambda:m.packet(2,0),lambda:m.current(2,2,0)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
