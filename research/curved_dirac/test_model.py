import math
import unittest
import model as m

w,c,v=m.w,m.car,m.vac


class CurvedDiracTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h=m.galerkin(1)
        cls.e,cls.o=m.symmetric_eigensystem(cls.h)
        cls.p=m.negative_projection(cls.e,cls.o)

    def vecclose(self,a,b):
        self.assertLess(c.norm_vector(tuple(x-y for x,y in zip(a,b))),1e-11)

    def test_01_positive_bounded_metric(self):
        self.assertTrue(all(.8-1e-15<=m.omega(x)<=1.2+1e-15 for x in (-5,-1,0,1,5)))

    def test_02_curvature_nonzero(self):
        self.assertAlmostEqual(m.curvature(0),-2*.2/(1.2**3))

    def test_03_flat_limit(self):
        self.assertEqual(m.curvature(1,epsilon=0),0)
        self.assertAlmostEqual(m.volume(0,1,0,1,epsilon=0),.5)

    def test_04_volume_refinement(self):
        coarse=m.volume(0,1,0,1)
        fine=sum(m.volume(i/2,(i+1)/2,j/2,(j+1)/2) for i in range(2) for j in range(2))
        self.assertAlmostEqual(coarse,fine)

    def test_05_volume_density_bounds(self):
        for n in (1,2,3):
            a=1/(1<<n)
            for i in range(1<<n):
                for j in range(1<<n):
                    density=m.volume(i*a,(i+1)*a,j*a,(j+1)*a)/a**2
                    self.assertTrue(.5*.8**2-1e-12<=density<=.5*1.2**2+1e-12)

    def test_06_curved_clifford_relations(self):
        om=m.omega(.4)
        g0=w.scale(1/om,w.GAMMA0); g1=w.scale(1/om,w.GAMMA1)
        self.assertLess(w.distance(w.mul(g0,g0),w.scale(1/om**2,w.I)),1e-12)
        self.assertLess(w.distance(w.mul(g1,g1),w.scale(-1/om**2,w.I)),1e-12)

    def test_07_contracted_spin_connection(self):
        sx,st=.3,.4
        connection=w.add(w.mul(w.GAMMA0,w.scale(.5*sx,w.Z)),w.mul(w.GAMMA1,w.scale(.5*st,w.Z)))
        expected=w.add(w.scale(.5*st,w.GAMMA0),w.scale(.5*sx,w.GAMMA1))
        self.assertLess(w.distance(connection,expected),1e-12)

    def rescaling_check(self,st):
        chi=(1+.2j,.3j); dx=(.2j,-.4); om=1.2; sx=.3
        psi=tuple(x/math.sqrt(om) for x in chi)
        psi_x=tuple((dx[i]-.5*sx*chi[i])/math.sqrt(om) for i in range(2))
        rhs=m.physical_rhs(psi,psi_x,.7,om,sx,st)
        transformed=tuple(math.sqrt(om)*rhs[i]+.5j*st*chi[i] for i in range(2))
        self.vecclose(transformed,m.rescaled_rhs(chi,dx,.7,om))

    def test_08_static_rescaling(self):
        self.rescaling_check(0)

    def test_09_time_dependent_rescaling(self):
        self.rescaling_check(.4)

    def test_10_cauchy_weight_not_spacetime_volume(self):
        om=1.2; chi=(1,.3j); psi=tuple(x/math.sqrt(om) for x in chi)
        self.assertAlmostEqual(om*c.norm_vector(psi)**2,c.norm_vector(chi)**2)
        self.assertNotAlmostEqual(om**2*c.norm_vector(psi)**2,c.norm_vector(chi)**2)

    def test_11_continuity_equation(self):
        chi=(1+.2j,.3j); dx=(.2j,-.4)
        rhs=m.rescaled_rhs(chi,dx,.7,1.2)
        dt=tuple(-1j*x for x in rhs)
        density_t=2*sum(complex(x).conjugate()*y for x,y in zip(chi,dt)).real
        current_x=2*sum(complex(x).conjugate()*y for x,y in zip(chi,w.apply(w.Z,dx))).real
        self.assertAlmostEqual(density_t+current_x,0)

    def test_12_variable_walk_flat_limit(self):
        f={0:(1,.3j),2:(.1j,.5)}
        a=m.variable_step(f,.7,.1,epsilon=0)
        b=w.real_step(f,.7,.1)
        self.assertEqual(a,b)

    def test_13_variable_walk_norm(self):
        f=m.local.cell_average_blob(.1,.4,(1,.3j))
        self.assertAlmostEqual(w.norm_squared(m.evolve(f,.7,.1,4)),w.norm_squared(f))

    def test_14_variable_walk_inverse(self):
        f={0:(1,.3j),2:(.1j,.5)}
        g=m.evolve(m.evolve(f,.7,.1,4),.7,.1,-4)
        self.assertLess(sum(abs(x-y)**2 for j in g.keys()|f.keys() for x,y in zip(g.get(j,(0,0)),f.get(j,(0,0)))),1e-24)

    def test_15_variable_walk_cone(self):
        for n in (-4,0,4):
            self.assertTrue(all(abs(j)<=abs(n) for j in m.evolve({0:(1,.3j)},.7,.1,n)))

    def test_16_massless_rescaled_dynamics(self):
        f={0:(1,.3j)}
        self.assertEqual(m.evolve(f,0,.1,3),w.real_evolve(f,0,.1,3))

    def test_17_compact_cell_refinement(self):
        spin=(1,.3j); fine=1/320
        reference=m.evolve(m.local.cell_average_blob(fine,.5,spin),.7,fine,64)
        errors=[]
        for a in (.1,.05,.025):
            approx=m.evolve(m.local.cell_average_blob(a,.5,spin),.7,a,round(.2/a))
            errors.append(m.local.piecewise_distance(approx,a,reference,fine))
        self.assertLess(errors[-1],errors[0]/3)

    def test_18_spacelike_lattice_pairing(self):
        a=m.evolve({0:(1,0)},.7,.1,-4)
        b=m.evolve({8:(1,0)},.7,.1,-1)
        self.assertLess(abs(m.local.net.lattice_inner(a,b)),1e-12)

    def test_19_galerkin_real_symmetric(self):
        self.assertEqual(self.h,tuple(zip(*self.h)))

    def test_20_eigen_residual(self):
        actual=c.dense_mul(self.h,self.o)
        expected=tuple(tuple(self.o[i][j]*self.e[j] for j in range(6)) for i in range(6))
        self.assertLess(m.frobenius_distance(actual,expected),1e-11)

    def test_21_eigenbasis_orthonormal(self):
        identity=tuple(tuple(float(i==j) for j in range(6)) for i in range(6))
        self.assertLess(m.frobenius_distance(c.dense_mul(c.dense_adjoint(self.o),self.o),identity),1e-11)

    def test_22_static_gap_bound(self):
        self.assertGreaterEqual(min(abs(x) for x in self.e),.7*.8-1e-12)

    def test_23_spectral_pairing(self):
        for a,b in zip(self.e,reversed(self.e)):
            self.assertAlmostEqual(a,-b)

    def test_24_negative_projection(self):
        self.assertLess(m.frobenius_distance(c.dense_mul(self.p,self.p),self.p),1e-11)
        self.assertAlmostEqual(sum(self.p[i][i] for i in range(6)),3)

    def test_25_curved_covariance_stationary(self):
        self.assertLess(m.frobenius_distance(c.dense_mul(self.h,self.p),c.dense_mul(self.p,self.h)),1e-11)

    def test_26_flat_covariance_not_stationary(self):
        p=[[0j]*6 for _ in range(6)]
        for i,k in enumerate((-1,0,1)):
            block=v.dirac_covariance(k,.7)
            for r in range(2):
                for s in range(2):p[2*i+r][2*i+s]=block[r][s]
        self.assertGreater(m.frobenius_distance(c.dense_mul(self.h,p),c.dense_mul(p,self.h)),.01)

    def test_27_finite_sea_ground(self):
        gamma=c.fock_lift(self.o)
        state=tuple(gamma.get((i,7),0j) for i in range(64))
        h=v.second_quantized(self.h); e0=sum(x for x in self.e if x<0)
        expectation=sum(complex(state[i]).conjugate()*value*state[j] for (i,j),value in h.items())
        self.assertAlmostEqual(expectation.real,e0)
        ren=c.add(h,c.scale(-e0,c.identity(64)))
        self.assertLess(c.norm_vector(tuple(sum(value*state[j] for (r,j),value in ren.items() if r==i) for i in range(64))),1e-11)

    def test_28_excitation_energy_positive(self):
        e0=sum(x for x in self.e if x<0)
        energies=[sum(x for i,x in enumerate(self.e) if state&(1<<i))-e0 for state in range(64)]
        self.assertGreaterEqual(min(energies),-1e-12)
        self.assertGreaterEqual(min(x for x in energies if x>1e-8),.7*.8)

    def test_29_spectral_propagator_unitary(self):
        u=m.spectral_propagator(self.e,self.o,.8)
        eye=tuple(tuple(complex(i==j) for j in range(6)) for i in range(6))
        self.assertLess(m.frobenius_distance(c.dense_mul(c.dense_adjoint(u),u),eye),1e-11)

    def test_30_cutoff_not_periodic_mode_wrap(self):
        self.assertEqual(self.h[0][5],0)
        self.assertNotEqual(self.h[0][3],0)

    def test_31_sampled_coin_error(self):
        a=.1
        for x in (-.049,.01,.049):
            exact=w.coin(.7*m.omega(x),a); sampled=w.coin(.7*m.omega(0),a)
            self.assertLessEqual(w.distance(exact,sampled),a*a*.7*.2/2+1e-12)

    def test_32_validation(self):
        for call in (lambda:m.omega(0,1),lambda:m.omega(0,.2,0),lambda:m.volume(1,0,0,1),lambda:m.galerkin(-1),lambda:m.evolve({},1,.1,.5),lambda:m.symmetric_eigensystem(((1,2),(0,1)))):
            with self.assertRaises(ValueError):call()


if __name__=='__main__':
    unittest.main()
