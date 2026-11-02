import math
import unittest
import model as m

w,c,v=m.w,m.car,m.vac


class WilsonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h,cls.e,cls.o,cls.p=m.spectral_data(7)

    def test_01_free_dispersion_identity(self):
        for a in (.1,.5,1):
            for k in (0,1,math.pi/a):
                expected=.7**2+4*(1+.7*a)*math.sin(k*a/2)**2/a**2
                self.assertAlmostEqual(m.energy(k,.7,a)**2,expected)

    def test_02_wilson_mass_positive(self):
        for k in (-10,-1,0,1,10):self.assertGreaterEqual(m.wilson_mass(k,.2),0)

    def test_03_unique_free_minimum(self):
        a=.1
        self.assertAlmostEqual(m.energy(0,.7,a),.7)
        self.assertTrue(all(m.energy(k,.7,a)>.7 for k in (-10,-1,1,10)))

    def test_04_edge_lifted(self):
        for a in (.1,.05,.025):
            self.assertAlmostEqual(m.energy(math.pi/a,.7,a),.7+2/a)

    def test_05_central_control_retains_doubler(self):
        a=.1
        self.assertAlmostEqual(m.energy(0,.7,a,r=0),m.energy(math.pi/a,.7,a,r=0))

    def test_06_finite_energy_window_exact(self):
        a=.1; cutoff=1.5; kmax=m.finite_energy_cutoff(cutoff,.7,a)
        self.assertAlmostEqual(m.energy(kmax,.7,a),cutoff)
        self.assertGreater(m.energy(kmax+.01,.7,a),cutoff)

    def test_07_window_converges_to_continuum(self):
        target=math.sqrt(1.5**2-.7**2)
        errors=[abs(m.finite_energy_cutoff(1.5,.7,a)-target) for a in (.1,.05,.025)]
        self.assertLess(errors[-1],errors[0]/3)

    def test_08_free_gap_uniform(self):
        self.assertTrue(all(m.energy(k,.7,a)>=.7-1e-12 for a in (.1,.5) for k in (-10,0,10)))

    def test_09_curved_gap_uniform_examples(self):
        for n in (5,7,13):
            self.assertGreaterEqual(min(abs(x) for x in m.spectral_data(n)[1]),.7*.8-1e-11)

    def test_10_eigensystem_residual(self):
        actual=c.dense_mul(self.h,self.o)
        expected=tuple(tuple(self.o[i][j]*self.e[j] for j in range(14)) for i in range(14))
        self.assertLess(m.curved.frobenius_distance(actual,expected),1e-10)

    def test_11_negative_projection(self):
        self.assertLess(m.curved.frobenius_distance(c.dense_mul(self.p,self.p),self.p),1e-11)
        self.assertAlmostEqual(sum(self.p[i][i] for i in range(14)),7)

    def test_12_projector_stationarity(self):
        self.assertLess(m.curved.frobenius_distance(c.dense_mul(self.h,self.p),c.dense_mul(self.p,self.h)),1e-10)

    def test_13_spectral_pairing_still_holds(self):
        for a,b in zip(self.e,reversed(self.e)):self.assertAlmostEqual(a,-b)

    def test_14_low_momentum_wilson_term_vanishes(self):
        for a in (.1,.05,.025):
            self.assertLessEqual(m.wilson_mass(1.2,a),a*1.2**2/2+1e-12)

    def test_15_free_symbol_convergence_first_order(self):
        errors=[w.distance(m.symbol(1.2,.7,a),w.hamiltonian(1.2,.7)) for a in (.1,.05,.025)]
        self.assertAlmostEqual(errors[0]/errors[-1],4,delta=.1)

    def test_16_real_space_nearest_neighbours(self):
        result=m.lattice_hamiltonian({0:(1,.3j)},.7,.1)
        self.assertEqual(set(result),{-1,0,1})

    def test_17_r0_recovers_central_hamiltonian(self):
        f={0:(1,.3j),3:(.2,1j)}
        self.assertEqual(m.lattice_hamiltonian(f,.7,.1,r=0),m.central.lattice_hamiltonian(f,.7,.1))

    def test_18_wilson_core_difference_shrinks(self):
        errors=[]
        for a in (.1,.05,.025):
            f=m.local.cell_average_blob(a,.5,(1,.3j))
            wh=m.lattice_hamiltonian(f,.7,a); ch=m.central.lattice_hamiltonian(f,.7,a)
            errors.append(math.sqrt(sum(abs(x-y)**2 for j in wh.keys()|ch.keys() for x,y in zip(wh.get(j,(0,0)),ch.get(j,(0,0))))))
        self.assertLess(errors[-1],errors[0]/3)

    def test_19_fixed_smear_projection_limit_diagnostic(self):
        errors=[m.circle_errors(n)[0] for n in (7,13,21)]
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],errors[0]*.6)

    def test_20_two_point_limit_diagnostic(self):
        self.assertLess(m.circle_errors(21)[1],m.circle_errors(7)[1]*.6)

    def test_21_wick_limit_diagnostic(self):
        self.assertLess(m.circle_errors(21)[2],m.circle_errors(7)[2]*.6)

    def test_22_cross_regulator_agreement(self):
        self.assertLess(m.cross_regulator_pairing_error(21),m.cross_regulator_pairing_error(7)*.6)

    def test_23_high_zone_low_energy_bound(self):
        for n in (9,15,21):
            a=2*math.pi/n
            actual=m.low_energy_high_zone_norm(n)
            self.assertLessEqual(actual,m.high_zone_bound(a,1.5,math.pi/2)+1e-11)

    def test_24_bound_vanishes_with_spacing(self):
        bounds=[m.high_zone_bound(a,1.5,math.pi/2) for a in (.1,.05,.025)]
        self.assertLess(bounds[-1],bounds[0]/3)

    def test_25_no_uniform_projector_convergence(self):
        for n in (20,40,80):
            a=1/n; k=math.pi/a-a
            self.assertGreater(w.distance(m.negative_fibre(k,.7,a),v.dirac_covariance(k,.7)),.65)

    def test_26_massless_axial_symmetry_broken_at_finite_spacing(self):
        h=m.symbol(1.2,0,.1); h0=m.symbol(1.2,0,.1,r=0)
        self.assertGreater(w.distance(w.mul(h,w.Z),w.mul(w.Z,h)),.1)
        self.assertLess(w.distance(w.mul(h0,w.Z),w.mul(w.Z,h0)),1e-12)

    def test_27_low_momentum_axial_breaking_vanishes(self):
        values=[w.distance(w.mul(m.symbol(1.2,0,a),w.Z),w.mul(w.Z,m.symbol(1.2,0,a))) for a in (.1,.05,.025)]
        self.assertAlmostEqual(values[0]/values[-1],4,delta=.1)

    def test_28_continuous_time_tail_persists(self):
        self.assertGreater(c.norm_vector(m.free_site_amplitude(2,.1)),1e-6)

    def test_29_hamiltonian_not_floquet_walk(self):
        a=.2; k=1.2
        p=math.sin(k*a)/a; mass=.7+m.wilson_mass(k,a)
        self.assertGreater(w.distance(w.dirac(p,mass,a),w.walk(k,.7,a)),.01)

    def test_30_flat_regulator_positive_excitation_energies(self):
        _,e,_,_=m.spectral_data(3)
        e0=sum(x for x in e if x<0)
        energies=[sum(x for j,x in enumerate(e) if mask&(1<<j))-e0 for mask in range(64)]
        self.assertGreaterEqual(min(energies),-1e-12)
        self.assertGreaterEqual(min(x for x in energies if x>1e-8),.56-1e-11)

    def test_31_free_circle_low_energy_count_stabilizes(self):
        cutoff=1.5; expected=2*len([k for k in range(-10,11) if math.hypot(k,.7)<=cutoff])
        for n in (21,25):
            a=2*math.pi/n
            count=2*sum(m.energy(k,.7,a)<=cutoff for k in range(-(n//2),n//2+1))
            self.assertEqual(count,expected)

    def test_32_validation(self):
        for call in (lambda:m.wilson_mass(1,.1,-1),lambda:m.wilson_mass(1,0),lambda:m.negative_fibre(0,0,.1),lambda:m.finite_energy_cutoff(.1,.7,.1),lambda:m.high_zone_bound(.1,1,0),lambda:m.free_site_amplitude(2,.1,sites=1)):
            with self.assertRaises(ValueError):call()


if __name__=='__main__':
    unittest.main()
