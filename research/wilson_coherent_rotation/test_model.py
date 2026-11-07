import math
import unittest
import model as m
class CoherenceTests(unittest.TestCase):
    def test_01_rotated_covariance_projection(self):
        M=m.matrix();C=((M[0][0],M[0][1]),(M[1][0],1+M[1][1]));C2=m.w.car.dense_mul(C,C)
        for i in (0,1):
            for j in (0,1):self.assertAlmostEqual(C2[i][j],C[i][j])
    def test_02_covariance_trace_one(self):self.assertAlmostEqual(sum((m.matrix()[i][i]+(i==1)) for i in (0,1)),1)
    def test_03_relative_kernel_not_diagonal(self):self.assertGreater(abs(m.matrix()[0][1]),0)
    def test_04_signed_determinant(self):
        M=m.matrix(.4,.7);self.assertAlmostEqual((M[0][0]*M[1][1]-M[0][1]*M[1][0]).real,-math.sin(.4)**2)
    def test_05_hole_band_energy(self):self.assertLess(m.packet(1,0,energy_action=True).real,0)
    def test_06_compressed_positive(self):self.assertTrue(all(0<=z<=1 for z in m.p.eigenvalues(m.covariance(.02,2,.4,.3))))
    def test_07_fock_expectation(self):
        a,n,x,t=.02,2,.4,.3;c=m.w.cell;rho=m.p.density_matrix(m.covariance(a,n,x,t));ref=c.density_matrix(m.w.same_chirality_covariance(a,n));op=c.current_product(a)
        self.assertAlmostEqual((c.expectation(op,rho)-c.expectation(op,ref)).real,m.current(a,n,x,t),places=9)
    def test_08_kernel_hermitian(self):self.assertAlmostEqual(m.kernel(.4,.7,.3,.02),m.kernel(.7,.4,.3,.02).conjugate())
    def test_09_gram_identity(self):
        a,n,x,t=.02,4,.4,.3;u,v=x+a*n/2,x-a*n/2
        det=m.kernel(u,u,t,a)*m.kernel(v,v,t,a)-abs(m.kernel(u,v,t,a))**2
        self.assertAlmostEqual(math.pi*det.real,m.terms(a,n,x,t)[1],places=11)
    def test_10_phase_matters_locally(self):self.assertGreater(abs(m.target(.7,.3,phase=0)-m.target(.7,.3,phase=math.pi)),.01)
    def test_11_dephasing_changes_stress(self):
        diag=math.sin(math.pi/4)**2*((m.packet(0,.7,.3).conjugate()*m.packet(0,.7,.3,j=1)).imag-(m.packet(1,.7,.3).conjugate()*m.packet(1,.7,.3,j=1)).imag)
        self.assertGreater(abs(m.target(.7,.3)-diag),.001)
    def test_12_bound(self):
        for n in (8,16,32):
            a=1/n**2;self.assertLessEqual(abs(m.current(a,n,.7,.3)-m.target(.7,.3)),m.error_bound(a,n,.3))
    def test_13_mesoscopic_limit(self):self.assertLess(abs(m.current(1/128**2,128,.7,.3)-m.target(.7,.3)),.001)
    def test_14_fixed_site_factor(self):self.assertAlmostEqual(m.current(.0001,2,.7,.3),m.w.shape(2)*m.target(.7,.3),places=6)
    def test_15_local_hamiltonian_agrees(self):self.assertAlmostEqual(m.local_energy(.0001,.7,.3),m.target(.7,.3),places=6)
    def test_16_total_energy(self):self.assertAlmostEqual(m.total_energy(),2.5,places=9)
    def test_17_total_spectral_limit(self):self.assertAlmostEqual(m.total_energy(.0001),m.total_energy(),places=6)
    def test_18_vacuum_angle(self):self.assertEqual(m.current(.02,4,.4,.3,theta=0),0)
    def test_19_full_swap_has_no_coherence(self):self.assertLess(abs(m.matrix(math.pi/2)[0][1]),1e-15)
    def test_20_translation(self):self.assertAlmostEqual(m.target(.7,.3),m.target(.4,0),places=10)
    def test_21_phase_periodic(self):self.assertAlmostEqual(m.target(.7,.3,phase=.3),m.target(.7,.3,phase=.3+2*math.pi))
    def test_22_two_point_reconstruction(self):
        cov=m.covariance(.02,2,.4,.3);rho=m.p.density_matrix(cov);car=m.w.car
        for i in (0,1):
            for j in (0,1):self.assertAlmostEqual(m.w.cell.expectation(car.mul(car.adjoint(car.annihilator(2,j)),car.annihilator(2,i)),rho),cov[i][j])
    def test_23_refinement(self):self.assertAlmostEqual(m.packet(1,.7,.3,.02,steps=600),m.packet(1,.7,.3,.02,steps=1200),places=10)
    def test_24_validation(self):
        for call in (lambda:m.current(.8,2,0),lambda:m.current(.1,0,0),lambda:m.matrix(-1),lambda:m.matrix(phase=float('nan')),lambda:m.packet(2,0)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
