import unittest
from model import *


class ContinuumScalingTests(unittest.TestCase):
    def assertMatrixClose(self,a,b,tol=2e-12):
        self.assertLessEqual(distance(a,b),tol)

    def test_01_coin_is_unitary(self):
        for m in (-1,0,.7):
            for a in (.01,.1,1):
                u=coin(m,a)
                self.assertMatrixClose(mul(adjoint(u),u),I)

    def test_02_shift_is_unitary(self):
        for k in (-3,0,1.2):
            self.assertMatrixClose(mul(adjoint(shift(k,.1)),shift(k,.1)),I)

    def test_03_walk_is_unitary(self):
        for k in (-3,0,1.2):
            self.assertMatrixClose(mul(adjoint(walk(k,.7,.1)),walk(k,.7,.1)),I)

    def test_04_operator_norm_formula(self):
        self.assertAlmostEqual(norm(((1+0j,0j),(0j,2+0j))),2)
        self.assertAlmostEqual(norm(scale(1j,X)),1)
        self.assertEqual(norm(scale(0,I)),0)

    def test_05_zero_parameters(self):
        self.assertMatrixClose(walk(0,0,.1),I)
        self.assertMatrixClose(dirac(0,0,1),I)

    def test_06_massless_evolution_is_exact_in_momentum_representation(self):
        for k in (-3,.3,2):
            for n in (1,7,32):
                self.assertMatrixClose(power(walk(k,0,.1),n),dirac(k,0,n*.1))

    def test_07_zero_momentum_mass_evolution_is_exact(self):
        for m in (-1,.7):
            self.assertMatrixClose(power(walk(0,m,.1),13),dirac(0,m,1.3))

    def test_08_commutator_norm(self):
        for k,m in ((1,.7),(-2,.3),(0,1)):
            a,b=scale(k,Z),scale(m,X)
            commutator=add(mul(a,b),scale(-1,mul(b,a)))
            self.assertAlmostEqual(norm(commutator),2*abs(k*m))

    def test_09_one_step_error_bound(self):
        for k in (-2,-.7,0,.3,2):
            for m in (-1,0,.8):
                for a in (.2,.05,.01):
                    self.assertLessEqual(distance(walk(k,m,a),dirac(k,m,a)),one_step_bound(k,m,a)+2e-13)

    def test_10_fixed_time_error_bound(self):
        for n in (8,16,32):
            a=1/n
            for k in (-1,.4,2):
                error=distance(power(walk(k,.7,a),n),dirac(k,.7,1))
                self.assertLessEqual(error,n_step_bound(k,.7,a,n)+2e-12)

    def test_11_uniform_fixed_band_bound(self):
        cutoff,m,n=2,.7,40
        a=1/n
        for j in range(41):
            k=-cutoff+2*cutoff*j/40
            self.assertLessEqual(distance(power(walk(k,m,a),n),dirac(k,m,1)),a*cutoff*abs(m)+2e-12)

    def test_12_observed_first_order_fixed_time_convergence(self):
        errors=[distance(power(walk(1.2,.7,1/n),n),dirac(1.2,.7,1)) for n in (32,64,128)]
        self.assertGreater(errors[0],errors[1])
        self.assertGreater(errors[1],errors[2])
        for ratio in (errors[0]/errors[1],errors[1]/errors[2]):
            self.assertGreater(ratio,1.8)
            self.assertLess(ratio,2.2)

    def test_13_discrete_composition_and_inverse(self):
        u=walk(.8,.7,.05)
        self.assertMatrixClose(power(u,13),mul(power(u,5),power(u,8)))
        self.assertMatrixClose(mul(adjoint(power(u,13)),power(u,13)),I)

    def test_14_zone_edge_does_not_share_the_uniform_low_band_limit(self):
        target=2*abs(math.sin(.5))
        for n in (20,40,80):
            a=1/n
            error=distance(power(walk(math.pi/a,1,a),n),dirac(math.pi/a,1,1))
            self.assertGreater(error,.8)
            self.assertLess(abs(error-target),.06)
            interior=math.pi/a-.1
            self.assertGreater(distance(power(walk(interior,1,a),n),dirac(interior,1,1)),.8)

    def test_15_zone_edge_failure_changes_an_observable_not_just_global_phase(self):
        n=40
        a=1/n
        k=math.pi/a
        psi_walk=apply(power(walk(k,1,a),n),(1+0j,0j))
        psi_dirac=apply(dirac(k,1,1),(1+0j,0j))
        self.assertAlmostEqual(spin_expectation(psi_walk,Z),math.cos(2),places=11)
        self.assertGreater(spin_expectation(psi_dirac,Z),.99)

    def test_16_exact_dispersion_trace_identity(self):
        for k,m,a in ((.8,.7,.1),(2,1,.2),(-3,.4,.05)):
            u=walk(k,m,a)
            self.assertAlmostEqual((u[0][0]+u[1][1]).real/2,math.cos(k*a)*math.cos(m*a))
            self.assertAlmostEqual((u[0][0]+u[1][1]).imag,0)

    def test_17_low_band_quasienergy_converges(self):
        k,m=.8,.7
        energy=math.hypot(k,m)
        errors=[abs(quasienergy(k,m,1/n)-energy) for n in (16,32,64)]
        self.assertGreater(errors[0],errors[1])
        self.assertGreater(errors[1],errors[2])
        self.assertGreater(errors[0]/errors[1],3.8)
        self.assertLess(errors[0]/errors[1],4.2)

    def test_18_zone_edge_dispersion_is_not_globally_relativistic(self):
        a=.01
        k=math.pi/a
        self.assertGreater(abs(quasienergy(k,1,a)-math.hypot(k,1)),.9)

    def test_19_lattice_support_is_finite_and_has_correct_parity(self):
        initial={0:(1+0j,0j)}
        for n in (1,3,8):
            output=real_evolve(initial,.7,.1,n)
            self.assertTrue(all(abs(j)<=n and (j-n)%2==0 for j in output))

    def test_20_physical_lattice_cone_speed_is_one_in_declared_units(self):
        a,n=.05,12
        output=real_evolve({0:(1+0j,0j)},.7,a,n)
        self.assertTrue(all(abs(j*a)<=n*a+1e-14 for j in output))

    def test_21_real_space_norm_is_preserved(self):
        initial={0:(1/math.sqrt(2),0j),2:(0j,1/math.sqrt(2))}
        for n in (1,5,20):
            self.assertAlmostEqual(norm_squared(real_evolve(initial,.7,.1,n)),norm_squared(initial),places=12)

    def test_22_real_space_and_fourier_symbol_agree(self):
        initial={-1:(.5+0j,.5j),2:(.5j,.5+0j)}
        for k in (-2,.3,1.1):
            left=fourier_sample(real_step(initial,.7,.1),k,.1)
            right=apply(walk(k,.7,.1),fourier_sample(initial,k,.1))
            self.assertLess(sum(abs(a-b) for a,b in zip(left,right)),1e-13)

    def test_23_parseval_on_sufficient_finite_fourier_grid(self):
        a,n_grid=.1,31
        output=real_evolve({0:(1+0j,0j)},.7,a,5)
        total=0
        for ell in range(-15,16):
            k=2*math.pi*ell/(n_grid*a)
            f=fourier_sample(output,k,a)
            total+=sum(abs(x)**2 for x in f)*2*math.pi/(n_grid*a)
        self.assertAlmostEqual(total,norm_squared(output),places=12)

    def test_24_ordering_matters_at_finite_step(self):
        self.assertGreater(distance(mul(shift(1,.1),coin(.7,.1)),mul(coin(.7,.1),shift(1,.1))),.001)

    def test_25_opposite_order_has_same_restricted_limit_bound(self):
        k,m,a=1,.7,.1
        alternative=mul(coin(m,a),shift(k,a))
        self.assertLessEqual(distance(alternative,dirac(k,m,a)),one_step_bound(k,m,a)+2e-13)

    def test_26_clifford_relations(self):
        self.assertMatrixClose(mul(GAMMA0,GAMMA0),I)
        self.assertMatrixClose(mul(GAMMA1,GAMMA1),scale(-1,I))
        self.assertMatrixClose(add(mul(GAMMA0,GAMMA1),mul(GAMMA1,GAMMA0)),scale(0,I))

    def test_27_spinor_boost_covariance_of_gamma_matrices(self):
        for eta in (-1,.3,.8):
            s,inv=boost_spin(eta),boost_spin(-eta)
            c,h=math.cosh(eta),math.sinh(eta)
            self.assertMatrixClose(mul(mul(inv,GAMMA0),s),add(scale(c,GAMMA0),scale(-h,GAMMA1)))
            self.assertMatrixClose(mul(mul(inv,GAMMA1),s),add(scale(-h,GAMMA0),scale(c,GAMMA1)))

    def test_28_mass_shell_is_lorentz_invariant(self):
        for k in (-2,0,.7):
            for m in (0,.8):
                for eta in (-1,.4):
                    energy,momentum=boost_momentum(k,m,eta)
                    self.assertAlmostEqual(energy**2-momentum**2,m*m,places=11)

    def test_29_dirac_hamiltonian_squares_to_mass_shell(self):
        for k,m in ((1,.7),(0,1),(-2,.8)):
            h=hamiltonian(k,m)
            self.assertMatrixClose(mul(h,h),scale(k*k+m*m,I))

    def test_30_continuum_current_bound(self):
        for psi in ((1,0),(0,1),(1,1j),(.3+.2j,.5-.4j)):
            density=sum(abs(z)**2 for z in psi)
            self.assertLessEqual(abs(spin_expectation(psi,Z)),density+1e-14)

    def test_31_scaled_coin_approaches_identity(self):
        m=.7
        for a in (.1,.05,.01):
            self.assertLessEqual(distance(coin(m,a),I),abs(m)*a+1e-14)
        fixed=coin(1,.7)
        self.assertGreater(distance(fixed,I),.6)

    def test_32_invalid_parameters_rejected(self):
        for a in (0,-.1):
            with self.assertRaises(ValueError):
                walk(1,.7,a)
        with self.assertRaises(ValueError):
            walk(math.inf,.7,.1)
        with self.assertRaises(ValueError):
            power(I,-1)
        with self.assertRaises(ValueError):
            real_evolve({0:(1,0)},.7,.1,.5)

if __name__=='__main__':
    unittest.main(verbosity=2)
