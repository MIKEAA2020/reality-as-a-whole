import cmath
import math
import unittest
import model as m

v,c,w=m.vac,m.car,m.w


class SpacetimeTests(unittest.TestCase):
    def setUp(self):
        self.k,self.mass=1.2,.7
        self.f=(.3+1j,.7-.2j)
        self.samples=((-1,.2,self.f),(.3,.7,(.1j,.5)),(.8,.3,(1,.2j)))

    def vecclose(self,a,b,tol=1e-10):
        self.assertLess(c.norm_vector(tuple(x-y for x,y in zip(a,b))),tol)

    def matclose(self,a,b):
        self.assertLess(w.distance(a,b),1e-11)

    def test_01_smear_linearity(self):
        expected=tuple(2j*x for x in m.smear(self.k,self.mass,self.samples))
        actual=m.smear(self.k,self.mass,tuple((t,a,tuple(2j*x for x in f)) for t,a,f in self.samples))
        self.vecclose(actual,expected)

    def test_02_smear_additivity(self):
        a=m.smear(self.k,self.mass,self.samples[:1]); b=m.smear(self.k,self.mass,self.samples[1:])
        self.vecclose(m.smear(self.k,self.mass,self.samples),tuple(x+y for x,y in zip(a,b)))

    def test_03_norm_bound(self):
        bound=sum(abs(a)*c.norm_vector(f) for _,a,f in self.samples)
        self.assertLessEqual(c.norm_vector(m.smear(self.k,self.mass,self.samples)),bound+1e-12)

    def test_04_time_slice_right_inverse(self):
        times=(-.1,0,.1); weights=(.2,.5,.3)
        samples=tuple((t,a,w.apply(w.dirac(self.k,self.mass,t),self.f)) for t,a in zip(times,weights))
        self.vecclose(m.smear(self.k,self.mass,samples),self.f)

    def test_05_time_slice_arbitrarily_thin(self):
        for epsilon in (.1,.001,1e-6):
            samples=tuple((t,.5,w.apply(w.dirac(self.k,self.mass,t),self.f)) for t in (-epsilon,epsilon))
            self.vecclose(m.smear(self.k,self.mass,samples),self.f)

    def test_06_equation_of_motion_quadrature(self):
        err=c.norm_vector(m.smear(self.k,self.mass,m.eom_samples(self.k,self.mass,self.f,80)))
        self.assertLess(err,1e-7)

    def test_07_equation_of_motion_refinement(self):
        a=c.norm_vector(m.smear(self.k,self.mass,m.eom_samples(self.k,self.mass,self.f,10)))
        b=c.norm_vector(m.smear(self.k,self.mass,m.eom_samples(self.k,self.mass,self.f,40)))
        self.assertLess(b,a/100)

    def test_08_time_translation(self):
        s=.6
        actual=m.smear(self.k,self.mass,tuple((t+s,a,f) for t,a,f in self.samples))
        expected=w.apply(w.dirac(self.k,self.mass,-s),m.smear(self.k,self.mass,self.samples))
        self.vecclose(actual,expected)

    def test_09_space_translation(self):
        phase=cmath.exp(-1j*self.k*.4)
        actual=m.smear(self.k,self.mass,tuple((t,a,tuple(phase*x for x in f)) for t,a,f in self.samples))
        self.vecclose(actual,tuple(phase*x for x in m.smear(self.k,self.mass,self.samples)))

    def test_10_translation_group(self):
        self.matclose(w.mul(w.dirac(self.k,self.mass,-.2),w.dirac(self.k,self.mass,-.7)),w.dirac(self.k,self.mass,-.9))

    def test_11_covariance_time_invariant(self):
        p=v.dirac_covariance(self.k,self.mass)
        q=m.smear(self.k,self.mass,self.samples)
        transformed=w.apply(w.dirac(self.k,self.mass,-.6),q)
        self.assertAlmostEqual(v.pairing(p,q,q).real,v.pairing(p,transformed,transformed).real)

    def test_12_spacetime_car(self):
        q=m.smear(self.k,self.mass,self.samples)
        a=c.field(q); b=c.field(self.f)
        actual=c.add(c.mul(a,c.adjoint(b)),c.mul(c.adjoint(b),a))
        self.assertLess(c.error(actual,c.scale(v.inner(q,self.f),c.identity(4))),1e-11)

    def test_13_diamond_shadow(self):
        for t in (-.7,0,.5):
            for x in (-.8,0,.6):
                if m.diamond_contains(t,x):
                    self.assertLess(abs(x)+abs(t),1)

    def test_14_local_time_slice_support_budget(self):
        # Initial data in [-.6,.6], |t|<.1: expanded data remain in D((-1,1)).
        for t in (-.099,0,.099):
            for x in (-.6-abs(t),.6+abs(t)):
                self.assertTrue(m.diamond_contains(t,x))

    def test_15_spacelike_box_criterion(self):
        self.assertTrue(m.spacelike_boxes((0,0,.1,.2),(.2,2,.1,.2)))
        self.assertFalse(m.spacelike_boxes((0,0,.1,.2),(2,.2,.1,.2)))

    def test_16_shadows_can_overlap_for_spacelike_boxes(self):
        a,b=(10,0,.1,.2),(10,3,.1,.2)
        self.assertTrue(m.spacelike_boxes(a,b))
        sa,sb=m.shadow(*a),m.shadow(*b)
        self.assertGreater(min(sa[1],sb[1]),max(sa[0],sb[0]))

    def test_17_inverse_walk(self):
        f={0:self.f,2:(.2j,.3)}
        recovered=m.inverse_walk(w.real_evolve(f,self.mass,.2,3),self.mass,.2,3)
        diff=sum(sum(abs(x-y)**2 for x,y in zip(recovered.get(j,(0,0)),f.get(j,(0,0)))) for j in recovered.keys()|f.keys())
        self.assertLess(diff,1e-24)

    def test_18_pullback_orthogonality_despite_overlap(self):
        a=m.inverse_walk({0:(1,0)},self.mass,.2,4)
        b=m.inverse_walk({2:(1,0)},self.mass,.2,4)
        self.assertTrue(a.keys()&b.keys())
        self.assertLess(abs(m.lattice_inner(a,b)),1e-12)

    def test_19_discrete_finite_propagation(self):
        for n in range(4):
            support=m.inverse_walk({0:self.f},self.mass,.2,n)
            self.assertTrue(all(abs(j)<=n for j in support))

    def test_20_massless_characteristics(self):
        a=m.inverse_walk({0:(1,2j)},0,.2,3)
        self.assertEqual(a,{-3:(1+0j,0j),3:(0j,2j)})

    def test_21_boost_interval(self):
        for eta in (-.8,.5):
            t,x=m.boost_point(.4,1.2,eta)
            self.assertAlmostEqual(t*t-x*x,.4**2-1.2**2)

    def test_22_boost_energy_sign_and_shell(self):
        for sign in (-1,1):
            for eta in (-1,.7):
                ep,kp,j=m.branch_boost(self.k,self.mass,sign,eta)
                self.assertGreater(sign*ep,0); self.assertGreater(j,0)
                self.assertAlmostEqual(ep*ep-kp*kp,self.mass**2)

    def test_23_boost_spinor_intertwining(self):
        for sign in (-1,1):
            p=v.dirac_covariance(self.k,self.mass)
            if sign==1:
                p=w.add(w.I,w.scale(-1,p))
            f=v.occupied_spinor(p)
            ep,kp,_=m.branch_boost(self.k,self.mass,sign,.6)
            sf=w.apply(w.boost_spin(.6),f)
            self.vecclose(w.apply(w.hamiltonian(kp,self.mass),sf),tuple(ep*x for x in sf))

    def test_24_boost_norm_jacobian(self):
        for sign in (-1,1):
            p=v.dirac_covariance(self.k,self.mass)
            if sign==1:
                p=w.add(w.I,w.scale(-1,p))
            f=v.occupied_spinor(p)
            _,_,j=m.branch_boost(self.k,self.mass,sign,.6)
            sf=w.apply(w.boost_spin(.6),f)
            self.assertAlmostEqual(c.norm_vector(sf)**2,j)

    def test_25_boost_inverse(self):
        t,x=m.boost_point(.4,1.2,.6)
        self.vecclose(m.boost_point(t,x,-.6),(.4,1.2))
        self.matclose(w.mul(w.boost_spin(.6),w.boost_spin(-.6)),w.I)

    def test_26_contragredient_source(self):
        self.matclose(w.mul(w.adjoint(w.boost_spin(.6)),m.source_boost(.6)),w.I)
        self.assertGreater(w.distance(w.mul(w.adjoint(w.boost_spin(.6)),w.boost_spin(.6)),w.I),.1)

    def test_27_lorentz_group(self):
        self.vecclose(m.boost_point(*m.boost_point(.4,1.2,.3),.5),m.boost_point(.4,1.2,.8))
        self.matclose(w.mul(w.boost_spin(.3),w.boost_spin(.5)),w.boost_spin(.8))

    def test_28_even_disjoint_locality(self):
        a,b=c.number(4,0),c.number(4,3)
        self.assertEqual(c.mul(a,b),c.mul(b,a))

    def test_29_even_union_has_extra_bilocal(self):
        a=c.mul(c.adjoint(c.annihilator(4,0)),c.annihilator(4,3))
        parity_a={(j,j):complex((-1)**(j&1)) for j in range(16)}
        p=c.parity(4)
        self.assertLess(c.error(c.mul(c.mul(p,a),p),a),1e-12)
        self.assertGreater(c.error(c.mul(parity_a,a),c.mul(a,parity_a)),1)

    def test_30_spacetime_quadrature_convergence(self):
        def samples(n):
            return tuple((j/n,1/n,tuple(m.bump(j/n)*x for x in self.f)) for j in range(-n,n+1))
        ref=m.smear(self.k,self.mass,samples(400))
        err=lambda n:c.norm_vector(tuple(x-y for x,y in zip(m.smear(self.k,self.mass,samples(n)),ref)))
        self.assertLess(err(40),err(10)/100)

    def test_31_walk_spacetime_approximation(self):
        ref=m.smear(self.k,self.mass,tuple((j/800,1/800,tuple(m.bump(j/800)*x for x in self.f)) for j in range(-800,801)))
        errors=[]
        for n in (20,40,80):
            out=[0j,0j]
            for j in range(-n,n+1):
                u=w.power(w.walk(self.k,self.mass,1/n),abs(j))
                if j>=0:
                    u=w.adjoint(u)
                q=w.apply(u,tuple(m.bump(j/n)*x for x in self.f))
                for i in range(2):
                    out[i]+=q[i]/n
            errors.append(c.norm_vector(tuple(x-y for x,y in zip(out,ref))))
        self.assertLess(errors[-1],errors[0]/3)

    def test_32_validation(self):
        with self.assertRaises(ValueError):
            m.branch_boost(1,1,0,.5)
        with self.assertRaises(ValueError):
            m.diamond_contains(0,0,radius=0)
        with self.assertRaises(ValueError):
            m.inverse_walk({},1,.1,-1)
        with self.assertRaises(ValueError):
            m.eom_samples(1,1,self.f,0)


if __name__=='__main__':
    unittest.main()
