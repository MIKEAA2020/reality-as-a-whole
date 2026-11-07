import math
import unittest
import model as m

c=m.car


class WilsonThermalTests(unittest.TestCase):
    def test_01_massless_wilson_dispersion(self):
        for theta in (-2,-.5,0,.5,2):
            a=.1
            self.assertAlmostEqual(m.energy(theta,a)**2,(math.sin(theta)/a)**2+((1-math.cos(theta))/a)**2)

    def test_02_unique_low_energy_zero(self):
        self.assertEqual(m.energy(0,.1),0)
        self.assertEqual(m.energy(math.pi,.1),20)

    def test_03_fermi_covariance_eigenvalues(self):
        for energy in (0,.4,2,20):
            f=m.fermi_tail(energy,2.5)/2
            self.assertTrue(0<=f<=1)
            self.assertTrue(0<=1-f<=1)

    def test_04_covariance_commutes_with_hamiltonian(self):
        # Every fibre is (I-tanh(beta E/2) h/E)/2, hence a polynomial in h.
        for theta in (.1,1,2):
            p=math.sin(theta)/.1; w=(1-math.cos(theta))/.1; e=m.energy(theta,.1)
            h=((p,w),(w,-p)); factor=math.tanh(2.5*e/2)
            cov=tuple(tuple(.5*((i==j)-factor*h[i][j]/e) for j in range(2)) for i in range(2))
            self.assertLess(sum(abs(x-y)**2 for a,b in zip(c.dense_mul(h,cov),c.dense_mul(cov,h)) for x,y in zip(a,b)),1e-25)

    def test_05_detailed_balance(self):
        for energy in (.1,1,2):
            f=m.fermi_tail(energy,2.5)/2
            self.assertAlmostEqual(f/(1-f),math.exp(-2.5*energy))

    def test_06_ground_same_chirality_kernel(self):
        for n in (1,2,4):
            integral=m.simpson(lambda t:math.sin(n*t)*math.cos(t/2),math.pi,4000)
            expected=n/(n*n-.25)
            self.assertAlmostEqual(integral,expected,places=10)

    def test_07_ground_mixed_kernel(self):
        for n in (1,2,4):
            integral=m.simpson(lambda t:math.cos(n*t)*math.sin(t/2),math.pi,4000)
            self.assertAlmostEqual(-integral/(2*math.pi),1/(4*math.pi*(n*n-.25)),places=10)

    def test_08_thermal_change_of_variable(self):
        a,n,beta=.05,4,2.5
        angle_integral=m.simpson(lambda t:math.sin(n*t)*math.cos(t/2)*m.fermi_tail(m.energy(t,a),beta),math.pi,12000)
        self.assertAlmostEqual(angle_integral,-a*(n*a)*m.thermal_ratio(a,n,beta),places=9)

    def test_09_fermi_moment1(self):
        numerical=m.simpson(lambda p:p*m.fermi_tail(p,2.5),40/2.5,1600)
        self.assertAlmostEqual(numerical,m.moment1(2.5),places=9)

    def test_10_fermi_moment3(self):
        numerical=m.simpson(lambda p:p**3*m.fermi_tail(p,2.5),40/2.5,1600)
        self.assertAlmostEqual(numerical,m.moment3(2.5),places=9)

    def test_11_ratio_error_bound(self):
        for n in (8,16,32):
            a=1/n**2
            self.assertLessEqual(abs(m.thermal_ratio(a,n)+m.moment1(2.5)),m.ratio_bound(a,n)+1e-9)

    def test_12_current_error_bound(self):
        for n in (8,16,32):
            a=1/n**2
            self.assertLessEqual(abs(m.current_stress(a,n)-m.shape(n)*m.target()),m.current_error_bound(a,n)+1e-9)

    def test_13_fixed_count_calibrated_limit(self):
        for n in (1,2,4):
            self.assertAlmostEqual(m.current_stress(.0001,n,calibrated=True),m.target(),places=7)

    def test_14_fixed_count_uncalibrated_bias(self):
        for n in (1,2,4):
            self.assertAlmostEqual(m.current_stress(.0001,n),m.shape(n)*m.target(),places=7)

    def test_15_mesoscopic_raw_limit(self):
        errors=[abs(m.current_stress(1/n**2,n)-m.target()) for n in (8,16,32,64)]
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],errors[0]/50)

    def test_16_fixed_count_mixed_artifact(self):
        for n in (1,2,4):
            expected=-m.target()/(4*n*n-1)
            self.assertAlmostEqual(m.mixed_current(.0001,n),expected,places=7)

    def test_17_mixed_mesoscopic_limit(self):
        values=[abs(m.mixed_current(1/n**2,n)) for n in (8,16,32,64)]
        self.assertLess(values[-1],values[0]/50)

    def test_18_independent_hamiltonian_energy_limit(self):
        expected=2*m.target()
        errors=[abs(m.thermal_energy_density(a)-expected) for a in (.05,.025,.0125)]
        self.assertLess(errors[-1],errors[0]/10)

    def test_19_current_energy_agreement(self):
        for n in (16,32,64):
            a=1/n**2
            self.assertLess(abs(2*m.current_stress(a,n)-m.thermal_energy_density(a)),.001/n)

    def test_20_positive_cell_covariances(self):
        for cov in (m.same_chirality_covariance(.02,2),m.same_chirality_covariance(.02,2,2.5),m.mixed_covariance(.02,2,2.5)):
            self.assertTrue(all(0<=x<=1 for x in m.cell.covariance_eigenvalues(cov)))

    def test_21_positive_density_normalized(self):
        cov=m.same_chirality_covariance(.02,2,2.5)
        rho=m.cell.density_matrix(cov)
        self.assertAlmostEqual(c.trace(rho).real,1)
        z=abs(cov[0][1]); self.assertGreaterEqual(.25-z*z,0)

    def test_22_actual_current_operator_expectation(self):
        a,n=.02,2
        rho=m.cell.density_matrix(m.same_chirality_covariance(a,n,2.5)); ref=m.cell.density_matrix(m.same_chirality_covariance(a,n))
        op=m.cell.current_product(a)
        actual=m.cell.expectation(op,rho)-m.cell.expectation(op,ref)
        self.assertAlmostEqual(actual.real,m.current_stress(a,n),places=10)

    def test_23_actual_mixed_operator_expectation(self):
        a,n=.02,2
        rho=m.cell.density_matrix(m.mixed_covariance(a,n,2.5)); ref=m.cell.density_matrix(m.mixed_covariance(a,n))
        op=m.cell.current_product(a)
        actual=m.cell.expectation(op,rho)-m.cell.expectation(op,ref)
        self.assertAlmostEqual(actual.real,m.mixed_current(a,n),places=10)

    def test_24_thermal_truncation_control(self):
        for a in (.05,.025,.0125):self.assertLess(m.omitted_ratio_tail(a),1e-14)

    def test_25_simpson_refinement(self):
        a,n=.02,4
        self.assertLess(abs(m.current_stress(a,n,steps=800)-m.current_stress(a,n,steps=1600)),1e-8)

    def test_26_observable_norm_diverges(self):
        norm=lambda a:max(abs(x) for x in m.cell.current_product(a).values())
        self.assertAlmostEqual(norm(.01)/norm(.02),4)

    def test_27_chiral_sectors_not_independent_at_finite_spacing(self):
        self.assertGreater(abs(m.mixed_covariance(.02,1)[0][1]),.1)
        self.assertNotEqual(m.mixed_current(.02,1),0)

    def test_28_relative_curved_trace(self):
        jet=m.previous.static_jet(.4); t=m.current_stress(1/32**2,32)
        self.assertEqual(m.previous.trace(jet,m.previous.stress(jet,t,t)),m.previous.trace(jet,m.previous.stress(jet)))

    def test_29_tolman_relative_energy(self):
        jet=m.previous.static_jet(.4); omega=math.exp(jet['sigma']); beta=2.5
        self.assertAlmostEqual(2*m.target(beta)/omega**2,math.pi/(6*(beta*omega)**2))

    def test_30_no_mass_gap_assumption(self):
        self.assertEqual(m.energy(0,.01),0)
        self.assertAlmostEqual(m.fermi_tail(0,2.5)/2,.5)

    def test_31_central_ground_parity_control(self):
        central_even=(1-(-1)**2)/(2*math.pi*2)
        wilson_even=m.shape(2)/(2*math.pi*2)
        self.assertEqual(central_even,0)
        self.assertGreater(wilson_even,0)

    def test_32_validation(self):
        for call in (lambda:m.shape(0),lambda:m.energy(0,0),lambda:m.thermal_ratio(.1,0),lambda:m.thermal_ratio(.1,1,beta=0),lambda:m.simpson(lambda x:x,1,3),lambda:m.moment1(0)):
            with self.assertRaises(ValueError):call()


if __name__=='__main__':
    unittest.main()
