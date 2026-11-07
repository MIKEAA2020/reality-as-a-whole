import math
import unittest
import model as m

c,w=m.car,m.w


class VacuumTests(unittest.TestCase):
    def setUp(self):
        self.k,self.mass=1.2,.7
        self.p=m.dirac_covariance(self.k,self.mass)
        self.state=m.slater_state(self.p)
        self.f=(1+.3j,-.2j)
        self.g=(.4j,.6-.1j)

    def close(self,a,b):
        self.assertLess(w.distance(a,b),1e-11)

    def opclose(self,a,b):
        self.assertLess(c.error(a,b),1e-10)

    def test_01_dirac_projection(self):
        self.close(w.mul(self.p,self.p),self.p)

    def test_02_dirac_selfadjoint(self):
        self.close(w.adjoint(self.p),self.p)
        self.assertAlmostEqual(sum(self.p[i][i].real for i in range(2)),1)

    def test_03_dirac_negative_energy(self):
        self.close(w.mul(w.hamiltonian(self.k,self.mass),self.p),w.scale(-math.hypot(self.k,self.mass),self.p))

    def test_04_dirac_stationarity(self):
        u=w.dirac(self.k,self.mass,.8)
        self.close(w.mul(w.mul(u,self.p),w.adjoint(u)),self.p)

    def test_05_walk_projection(self):
        for k in (-10,0,1,12):
            p=m.walk_covariance(k,self.mass,.2)
            self.close(w.mul(p,p),p)
            self.close(w.adjoint(p),p)

    def test_06_bloch_symbol(self):
        for k in (-3,0,2):
            a=.2
            actual=w.add(w.scale(math.cos(k*a)*math.cos(self.mass*a),w.I),w.scale(-1j,m.pauli_vector(m.walk_vector(k,self.mass,a))))
            self.close(actual,w.walk(k,self.mass,a))

    def test_07_walk_stationarity(self):
        p=m.walk_covariance(self.k,self.mass,.2)
        u=w.walk(self.k,self.mass,.2)
        self.close(w.mul(w.mul(u,p),w.adjoint(u)),p)

    def test_08_branch_hamiltonian(self):
        a=.2
        h=m.effective_hamiltonian(self.k,self.mass,a)
        energy=w.quasienergy(self.k,self.mass,a)
        actual=w.add(w.scale(math.cos(a*energy),w.I),w.scale(-1j*math.sin(a*energy)/energy,h))
        self.close(actual,w.walk(self.k,self.mass,a))

    def test_09_walk_negative_branch(self):
        p=m.walk_covariance(self.k,self.mass,.2)
        h=m.effective_hamiltonian(self.k,self.mass,.2)
        self.close(w.mul(h,p),w.scale(-w.quasienergy(self.k,self.mass,.2),p))

    def test_10_projector_bound(self):
        for a in (.2,.1,.05):
            for k in (-2,-.5,0,1,2):
                self.assertLessEqual(w.distance(m.walk_covariance(k,self.mass,a),m.dirac_covariance(k,self.mass)),m.projector_bound(2,self.mass,a)+1e-12)

    def test_11_fixed_momentum_convergence(self):
        errors=[w.distance(m.walk_covariance(self.k,self.mass,1/n),self.p) for n in (10,20,40,80)]
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],.01)

    def test_12_zone_edge_nonuniformity(self):
        # The negative projector flips its low-energy X direction at k=pi/a.
        errors=[w.distance(m.common_covariance(math.pi*n-1/n,self.mass,1/n),m.dirac_covariance(math.pi*n-1/n,self.mass)) for n in (20,40,80)]
        self.assertGreater(min(errors),.67)
        self.assertAlmostEqual(errors[-1],1/math.sqrt(2),delta=.01)

    def test_13_common_tail_empty(self):
        self.close(m.common_covariance(100,self.mass,.2),w.scale(0,w.I))
        self.close(m.common_covariance(self.k,self.mass,.2),m.walk_covariance(self.k,self.mass,.2))

    def test_14_sampled_cutoff_tail_bound(self):
        for a in (.2,.1):
            err2,low2,tail2=0,0,0
            for k,f in ((-30,(.01j,0)),(-1,self.f),(1,self.g),(20,(0,.03))):
                d=w.add(m.common_covariance(k,self.mass,a),w.scale(-1,m.dirac_covariance(k,self.mass)))
                err2+=sum(abs(x)**2 for x in w.apply(d,f))
                if abs(k)<=2:
                    low2+=sum(abs(x)**2 for x in f)
                else:
                    tail2+=sum(abs(x)**2 for x in f)
            self.assertLessEqual(math.sqrt(err2),m.projector_bound(2,self.mass,a)*math.sqrt(low2)+math.sqrt(tail2)+1e-12)

    def test_15_slater_normalized(self):
        self.assertAlmostEqual(sum(abs(x)**2 for x in self.state),1)

    def test_16_slater_covariance_convention(self):
        op=c.mul(c.adjoint(c.field(self.f)),c.field(self.g))
        self.assertAlmostEqual(abs(m.expectation(op,self.state)-m.pairing(self.p,self.f,self.g)),0)

    def test_17_complement_pairing(self):
        op=c.mul(c.field(self.f),c.adjoint(c.field(self.g)))
        actual=m.inner(self.f,w.apply(w.add(w.I,w.scale(-1,self.p)),self.g))
        self.assertAlmostEqual(abs(m.expectation(op,self.state)-actual),0)

    def test_18_anomalous_pairing_zero(self):
        self.assertAlmostEqual(abs(m.expectation(c.mul(c.field(self.f),c.field(self.g)),self.state)),0)

    def test_19_wick_four_point(self):
        # Two filled modes: C=I has a nonzero two-particle determinant.
        state=(0,0,0,1)
        fs=(self.f,self.g)
        gs=((.2,1j),(.7j,.1))
        op=c.identity(4)
        for f in fs:
            op=c.mul(op,c.adjoint(c.field(f)))
        for g in reversed(gs):
            op=c.mul(op,c.field(g))
        self.assertAlmostEqual(abs(m.expectation(op,state)-m.normal_expectation(w.I,fs,gs)),0)

    def test_20_rank_one_wick(self):
        self.assertAlmostEqual(abs(m.normal_expectation(self.p,(self.f,self.g),(self.f,self.g))),0)

    def test_21_density_pair_wick(self):
        op=c.mul(c.one_mode_density(self.f),c.one_mode_density(self.g))
        self.assertAlmostEqual(abs(m.expectation(op,self.state)-m.density_pair(self.p,self.f,self.g)),0)

    def test_22_state_stationary_fock(self):
        gamma=c.fock_lift(w.dirac(self.k,self.mass,.8))
        op=c.mul(c.adjoint(c.field(self.f)),c.field(self.g))
        self.assertAlmostEqual(abs(m.expectation(c.pullback(gamma,op),self.state)-m.expectation(op,self.state)),0)

    def test_23_finite_ground_energy(self):
        h=m.second_quantized(w.hamiltonian(self.k,self.mass))
        self.assertAlmostEqual(m.expectation(h,self.state).real,-math.hypot(self.k,self.mass))

    def test_24_subtracted_ground_zero(self):
        h=m.renormalized_generator(self.k,self.mass)
        out=[sum(value*self.state[j] for (r,j),value in h.items() if r==i) for i in range(4)]
        self.assertLess(c.norm_vector(out),1e-12)

    def test_25_positive_particle_hole_formula(self):
        vminus=m.occupied_spinor(self.p)
        vplus=m.occupied_spinor(w.add(w.I,w.scale(-1,self.p)))
        energy=math.hypot(self.k,self.mass)
        expected=c.scale(energy,c.add(c.add(c.identity(4),c.scale(-1,c.one_mode_density(vminus))),c.one_mode_density(vplus)))
        self.opclose(m.renormalized_generator(self.k,self.mass),expected)

    def test_26_particle_energy(self):
        pplus=w.add(w.I,w.scale(-1,self.p))
        op=c.adjoint(c.field(m.occupied_spinor(pplus)))
        vec=tuple(sum(value*self.state[j] for (r,j),value in op.items() if r==i) for i in range(4))
        self.assertAlmostEqual(m.expectation(m.renormalized_generator(self.k,self.mass),vec).real,math.hypot(self.k,self.mass))

    def test_27_hole_energy(self):
        op=c.field(m.occupied_spinor(self.p))
        vec=tuple(sum(value*self.state[j] for (r,j),value in op.items() if r==i) for i in range(4))
        self.assertAlmostEqual(m.expectation(m.renormalized_generator(self.k,self.mass),vec).real,math.hypot(self.k,self.mass))

    def test_28_covariance_two_point_convergence(self):
        errors=[abs(m.pairing(m.walk_covariance(self.k,self.mass,1/n),self.f,self.g)-m.pairing(self.p,self.f,self.g)) for n in (10,20,40,80)]
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))

    def test_29_density_correlation_convergence(self):
        errors=[abs(m.density_pair(m.walk_covariance(self.k,self.mass,1/n),self.f,self.g)-m.density_pair(self.p,self.f,self.g)) for n in (10,20,40,80)]
        self.assertLess(errors[-1],errors[0]/4)

    def test_30_absolute_energy_divergence(self):
        for cutoff in (10,100,1000):
            ratio=m.cutoff_energy_density(cutoff,self.mass)/(-cutoff**2/(2*math.pi))
            self.assertAlmostEqual(ratio,1,delta=.03)

    def test_31_charge_selection(self):
        self.assertEqual(m.normal_expectation(self.p,(self.f,),()),0)
        self.assertEqual(m.normal_expectation(self.p,(),()),1)

    def test_32_validation(self):
        for mass in (0,-1,float('inf')):
            with self.assertRaises(ValueError):
                m.dirac_covariance(1,mass)
        with self.assertRaises(ValueError):
            m.walk_covariance(0,1,math.pi)
        with self.assertRaises(ValueError):
            m.projector_bound(40,1,.1)
        with self.assertRaises(ValueError):
            m.cutoff_energy_density(-1,1)


if __name__=='__main__':
    unittest.main()
