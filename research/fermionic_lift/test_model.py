import math
import unittest
import model as m


class CARTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u=m.one_particle_walk(3,.7,.2)
        cls.g=m.fock_lift(cls.u)
        cls.cs=[m.annihilator(6,i) for i in range(6)]
        cls.eye=m.identity(64)
        cls.f=(1,2j,-.5,.3j,0,1-.2j)

    def close(self,a,b):
        self.assertLess(m.error(a,b),1e-10)

    def test_01_car_annihilation(self):
        for a in self.cs:
            for b in self.cs:
                self.close(m.add(m.mul(a,b),m.mul(b,a)),{})

    def test_02_car_mixed(self):
        for i,a in enumerate(self.cs):
            for j,b in enumerate(self.cs):
                b=m.adjoint(b)
                self.close(m.add(m.mul(a,b),m.mul(b,a)),self.eye if i==j else {})

    def test_03_nilpotence(self):
        for a in self.cs:
            self.close(m.mul(a,a),{})

    def test_04_jordan_wigner_sign(self):
        self.assertEqual(self.cs[2][3,7],1)
        self.assertEqual(self.cs[2][1,5],-1)

    def test_05_field_antilinearity(self):
        self.close(m.field(tuple(2j*x for x in self.f)),m.scale(-2j,m.field(self.f)))

    def test_06_smeared_car(self):
        a=m.field(self.f)
        self.close(m.add(m.mul(a,m.adjoint(a)),m.mul(m.adjoint(a),a)),m.scale(m.norm_vector(self.f)**2,self.eye))

    def test_07_density_projector_identity(self):
        n=m.one_mode_density(self.f)
        self.close(m.mul(n,n),m.scale(m.norm_vector(self.f)**2,n))

    def test_08_field_norm_lower_witness(self):
        # a(f) acting on a^dagger(f)|vac>/||f|| attains ||f||.
        a=m.field(self.f)
        witness=m.mul(a,m.adjoint(a))
        self.assertAlmostEqual(m.vacuum_expectation(witness).real,m.norm_vector(self.f)**2)

    def test_09_one_particle_unitarity(self):
        u=m.dense_mul(m.dense_adjoint(self.u),self.u)
        self.assertLess(sum(abs(u[i][j]-(i==j))**2 for i in range(6) for j in range(6)),1e-24)

    def test_10_lift_unitarity(self):
        self.close(m.mul(m.adjoint(self.g),self.g),self.eye)

    def test_11_vacuum_fixed(self):
        self.assertEqual({i:v for (i,j),v in self.g.items() if j==0},{0:1})

    def test_12_one_particle_sector(self):
        for i in range(6):
            for j in range(6):
                self.assertAlmostEqual(abs(self.g.get((1<<i,1<<j),0)-self.u[i][j]),0)

    def test_13_two_particle_minor(self):
        for r,s in ((0,1),(0,4),(2,5)):
            for i,j in ((0,1),(1,3),(2,5)):
                expected=self.u[r][i]*self.u[s][j]-self.u[r][j]*self.u[s][i]
                self.assertAlmostEqual(abs(self.g.get(((1<<r)|(1<<s),(1<<i)|(1<<j)),0)-expected),0)

    def test_14_exterior_antisymmetry(self):
        self.assertAlmostEqual(abs(m.minor_determinant(self.u,(0,1),(1,3))+m.minor_determinant(self.u,(0,1),(3,1))),0)

    def test_15_lift_composition(self):
        v=m.one_particle_walk(3,-.2,.3)
        self.close(m.fock_lift(m.dense_mul(self.u,v)),m.mul(self.g,m.fock_lift(v)))

    def test_16_number_preservation(self):
        n=m.number_total(6)
        self.close(m.pullback(self.g,n),n)

    def test_17_parity_preservation(self):
        self.close(m.pullback(self.g,m.parity(6)),m.parity(6))

    def test_18_generator_convention(self):
        for i,c in enumerate(self.cs):
            self.close(m.pullback(self.g,c),m.lifted_generator(self.u,i))

    def test_19_smeared_heisenberg(self):
        self.close(m.pullback(self.g,m.field(self.f)),m.field(m.apply(m.dense_adjoint(self.u),self.f)))

    def test_20_product_preservation(self):
        a,b=self.cs[0],m.adjoint(self.cs[4])
        self.close(m.pullback(self.g,m.mul(a,b)),m.mul(m.pullback(self.g,a),m.pullback(self.g,b)))

    def test_21_odd_grading(self):
        p=m.parity(6)
        self.close(m.mul(m.mul(p,self.cs[2]),p),m.scale(-1,self.cs[2]))

    def test_22_even_grading(self):
        p=m.parity(6)
        a=m.mul(m.adjoint(self.cs[0]),self.cs[1])
        self.close(m.mul(m.mul(p,a),p),a)

    def test_23_odd_disjoint_not_commuting(self):
        a,b=self.cs[0],self.cs[4]
        self.assertGreater(m.error(m.mul(a,b),m.mul(b,a)),1)

    def test_24_even_disjoint_commuting(self):
        a=m.mul(m.adjoint(self.cs[0]),self.cs[1])
        b=m.mul(m.adjoint(self.cs[4]),self.cs[5])
        self.close(m.mul(a,b),m.mul(b,a))

    def test_25_ring_one_step_cone(self):
        for i in range(6):
            target=(i//2+(-1 if i%2==0 else 1))%3
            self.assertEqual(m.mode_support(self.u,i),frozenset((2*target,2*target+1)))

    def test_26_multistep_ring_cone(self):
        u=m.one_particle_walk(7,.7,.2)
        power=tuple(tuple(complex(i==j) for j in range(14)) for i in range(14))
        for n in (1,2):
            power=m.dense_mul(power,u)
            for i in range(14):
                for j in m.mode_support(power,i):
                    distance=abs(i//2-j//2)
                    self.assertLessEqual(min(distance,7-distance),n)

    def test_27_fourier_correspondence(self):
        for ell in (-1,0,1):
            spin=(.3+1j,.7-.2j)
            f=m.fourier_mode(3,ell,spin)
            out=m.apply(self.u,f)
            expected=m.fourier_mode(3,ell,m.walk_model.apply(m.walk_model.walk(2*math.pi*ell/(3*.2),.7,.2),spin))
            self.assertLess(m.norm_vector(tuple(a-b for a,b in zip(out,expected))),1e-12)

    def test_28_vacuum_is_not_unique_invariant_state(self):
        n=m.number(6,0)
        self.assertEqual(m.vacuum_expectation(n),0)
        self.assertAlmostEqual(m.pullback(self.g,n)[63,63].real,1)
        self.assertAlmostEqual((m.trace(n)/64).real,.5)

    def test_29_fixed_band_error(self):
        for n in (10,20,40):
            error,bound=m.sampled_smear_error((-.7,1.2),((1,2j),(.3,1)),.7,1/n,n,1.2)
            self.assertLessEqual(error,bound+1e-12)

    def test_30_cutoff_tail_error(self):
        for n in (2,4,10,20):
            error,bound=m.sampled_smear_error((-7,-1,0,3,20),((.01j,0),(1,.2j),(0,.5),(.03,0),(0,.001)),.7,1/n,n,1.1)
            self.assertLessEqual(error,bound+1e-12)

    def test_31_common_extension_unitary_and_tail(self):
        self.assertEqual(m.common_space_unitary(100,.7,.2,5),m.walk_model.I)
        for k in (-2,1,100):
            u=m.common_space_unitary(k,.7,.2,5)
            self.assertLess(m.walk_model.distance(m.walk_model.mul(m.walk_model.adjoint(u),u),m.walk_model.I),1e-12)

    def test_32_validation(self):
        for args in ((0,0),(3,3),(13,1)):
            with self.assertRaises(ValueError):
                m.annihilator(*args)
        with self.assertRaises(ValueError):
            m.fock_lift(((1,2),))
        with self.assertRaises(ValueError):
            m.common_space_unitary(0,1,.1,-1)
        with self.assertRaises(ValueError):
            m.one_particle_walk(1,1,.1)


if __name__=='__main__':
    unittest.main()
