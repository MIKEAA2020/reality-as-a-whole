import math
import unittest
import model as m

w,c,v=m.w,m.car,m.vac


class HamiltonianStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h,cls.e,cls.o,cls.p=m.spectral_data(5)

    def test_01_free_gap(self):
        for a in (.1,.5,1):
            for k in (0,1,math.pi/a):
                h=m.free_symbol(k,.7,a)
                self.assertLess(w.distance(w.mul(h,h),w.scale((math.sin(k*a)/a)**2+.7**2,w.I)),1e-11)

    def test_02_perturbation_norm(self):
        h=m.ring_hamiltonian(5,epsilon=.2); h0=m.ring_hamiltonian(5,epsilon=0)
        difference=tuple(tuple(x-y for x,y in zip(a,b)) for a,b in zip(h,h0))
        eig,_=m.curved.symmetric_eigensystem(difference)
        self.assertLessEqual(max(abs(x) for x in eig),.7*.2+1e-12)

    def test_03_uniform_gap_examples(self):
        for n in (3,5,7):
            _,e,_,_=m.spectral_data(n)
            self.assertGreaterEqual(min(abs(x) for x in e),.7*.8-1e-11)

    def test_04_sign_symmetry(self):
        for a,b in zip(self.e,reversed(self.e)):
            self.assertAlmostEqual(a,-b)

    def test_05_eigensystem_residual(self):
        actual=c.dense_mul(self.h,self.o)
        expected=tuple(tuple(self.o[i][j]*self.e[j] for j in range(10)) for i in range(10))
        self.assertLess(m.curved.frobenius_distance(actual,expected),1e-11)

    def test_06_projection(self):
        self.assertLess(m.curved.frobenius_distance(c.dense_mul(self.p,self.p),self.p),1e-11)
        self.assertAlmostEqual(sum(self.p[i][i] for i in range(10)),5)

    def test_07_stationarity(self):
        self.assertLess(m.curved.frobenius_distance(c.dense_mul(self.h,self.p),c.dense_mul(self.p,self.h)),1e-11)

    def test_08_common_complement_choice(self):
        # Full gapped-extension projector and empty-tail projector agree on range R.
        p=v.dirac_covariance(1,.7); px=v.dirac_covariance(0,.7)
        full=tuple(tuple(p[i][j] if i<2 and j<2 else px[i-2][j-2] if i>=2 and j>=2 else 0j for j in range(4)) for i in range(4))
        empty=tuple(tuple(p[i][j] if i<2 and j<2 else 0j for j in range(4)) for i in range(4))
        f=(1,.3j,0,0)
        self.assertEqual(c.apply(full,f),c.apply(empty,f))
        self.assertGreater(m.curved.frobenius_distance(full,empty),.5)

    def test_09_centered_derivative_consistency_bound(self):
        for a in (.2,.1,.05):
            self.assertLessEqual(abs(math.sin(1.2*a)/a-1.2),a*a*1.2**3/6+1e-14)

    def test_10_cell_projection_converges(self):
        self.assertLess(m.local.projection_error(.025,.5),m.local.projection_error(.1,.5)/3)

    def test_11_derivative_core_consistency(self):
        errors=[m.derivative_consistency(a) for a in (.1,.05,.025)]
        self.assertLess(errors[-1],errors[0]/5)

    def test_12_sampled_mass_bound(self):
        a=.1
        for x in (-.049,.01,.049):
            self.assertLessEqual(.7*abs(m.curved.omega(x)-m.curved.omega(0)),a*.7*.2/2+1e-12)

    def test_13_resolvent_bound(self):
        z=.2+.5j
        self.assertLessEqual(max(abs(1/(x-z)) for x in self.e),1/abs(z.imag))

    def test_14_negative_sign_integral(self):
        for value in self.e:
            self.assertAlmostEqual(m.sign_integral_scalar(value),float(value<0),places=11)

    def test_15_integral_projection_reconstruction(self):
        d=len(self.e)
        actual=tuple(tuple(sum(self.o[i][k]*m.sign_integral_scalar(self.e[k])*self.o[j][k] for k in range(d)) for j in range(d)) for i in range(d))
        self.assertLess(m.curved.frobenius_distance(actual,self.p),1e-11)

    def test_16_fixed_smear_circle_convergence(self):
        errors=[m.circle_errors(n)[0] for n in (7,11,15)]
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],errors[0]/2)

    def test_17_two_point_circle_convergence(self):
        self.assertLess(m.circle_errors(15)[1],m.circle_errors(7)[1]/2)

    def test_18_wick_circle_convergence(self):
        self.assertLess(m.circle_errors(15)[2],m.circle_errors(7)[2]/2)

    def test_19_flat_projection_not_stationary(self):
        n=5; a=2*math.pi/n; p=[[0j]*(2*n) for _ in range(2*n)]
        for i,k in enumerate(range(-2,3)):
            block=v.dirac_covariance(math.sin(2*math.pi*k/n)/a,.7)
            for r in (0,1):
                for s in (0,1):p[2*i+r][2*i+s]=block[r][s]
        self.assertGreater(m.curved.frobenius_distance(c.dense_mul(self.h,p),c.dense_mul(p,self.h)),.01)

    def test_20_time_correlation_circle_convergence(self):
        def value(n,reference=False):
            _,e,o,p=m.spectral_data(n,reference)
            u=m.curved.spectral_propagator(e,o,-.4)
            f,g=m.fixed_smear(n),m.fixed_smear(n,True)
            return v.pairing(p,c.apply(u,f),g)
        target=value(19,True)
        self.assertLess(abs(value(15)-target),abs(value(7)-target)/2)

    def test_21_no_strict_continuous_time_lattice_cone(self):
        # Massless chiral propagator at two sites after t=.1a is J_2(.1), nonzero.
        self.assertGreater(abs(m.bessel_j(2,.1)),.001)

    def test_22_nearest_neighbour_generator(self):
        support=m.lattice_hamiltonian({0:(1,.3j)},.7,.1)
        self.assertEqual(set(support),{-1,0,1})

    def test_23_not_floquet_logarithm(self):
        a=.2; k=1.2
        central=w.dirac(math.sin(k*a)/a,.7,a)
        self.assertGreater(w.distance(central,w.walk(k,.7,a)),.01)

    def test_24_nonuniform_projector_limit(self):
        errors=[]
        for n in (20,40,80):
            a=1/n; k=math.pi/a-a
            errors.append(w.distance(v.dirac_covariance(math.sin(k*a)/a,.7),v.dirac_covariance(k,.7)))
        self.assertGreater(min(errors),.65)

    def test_25_uv_changes_with_spacing(self):
        a,b=.1,.05
        self.assertNotEqual(math.pi/a-a,math.pi/b-b)
        self.assertGreater(abs(math.sin((math.pi/a-a)*a)/a-(math.pi/a-a)),20)

    def test_26_free_doubling(self):
        a=.1
        self.assertAlmostEqual(math.hypot(math.sin(0)/a,.7),math.hypot(math.sin(math.pi)/a,.7))

    def test_27_tail_choice_vanishes_on_fixed_smear(self):
        errors=[m.local.projection_error(a,.5) for a in (.1,.05,.025)]
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))

    def test_28_positive_finite_excitation_energies(self):
        _,e,_,_=m.spectral_data(3)
        e0=sum(x for x in e if x<0)
        energies=[sum(x for j,x in enumerate(e) if state&(1<<j))-e0 for state in range(64)]
        self.assertGreaterEqual(min(energies),-1e-12)
        self.assertGreaterEqual(min(x for x in energies if x>1e-8),.7*.8-1e-11)

    def test_29_ring_mass_wrap_not_galerkin(self):
        h=m.ring_hamiltonian(5); g=m.circle_galerkin(2)
        self.assertEqual(h[0][9],.7*.2/2)
        self.assertEqual(g[0][9],0)

    def test_30_uv_norm_grows_but_gap_stays_open(self):
        _,e7,_,_=m.spectral_data(7); _,e15,_,_=m.spectral_data(15)
        self.assertGreater(max(abs(x) for x in e15),max(abs(x) for x in e7))
        self.assertGreaterEqual(min(abs(x) for x in e15),.56-1e-11)

    def test_31_low_momentum_second_order_symbol_error(self):
        errors=[w.distance(m.free_symbol(1.2,.7,a),w.hamiltonian(1.2,.7)) for a in (.1,.05,.025)]
        self.assertAlmostEqual(errors[0]/errors[-1],16,delta=.1)

    def test_32_validation(self):
        for call in (lambda:m.ring_hamiltonian(4),lambda:m.ring_hamiltonian(5,mass=0),lambda:m.circle_galerkin(0),lambda:m.free_symbol(1,1,0),lambda:m.bessel_j(-1,.1),lambda:m.sign_integral_scalar(0)):
            with self.assertRaises(ValueError):call()


if __name__=='__main__':
    unittest.main()
