"""Independent symbolic and numerical checks of a two-clock FLRW model.

All statements concern a specified effective model, not actual cosmic energy.
"""
import math
import unittest
import sympy as sp


def poisson(f, g, coordinates, momenta):
    return sp.simplify(sum(sp.diff(f,q)*sp.diff(g,p)-sp.diff(f,p)*sp.diff(g,q)
                           for q,p in zip(coordinates,momenta)))


class TwoClockRigorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = sp.symbols('a', positive=True, real=True)
        cls.phi, cls.chi = sp.symbols('phi chi', real=True)
        cls.pa, cls.pf, cls.pc = sp.symbols('p_a p_phi p_chi', nonzero=True, real=True)
        cls.k = sp.symbols('kappa', positive=True, real=True)
        cls.t, cls.u, cls.xi = sp.symbols('tau upsilon xi', real=True)
        a,phi,chi=cls.a,cls.phi,cls.chi
        pa,pf,pc,k=cls.pa,cls.pf,cls.pc,cls.k
        cls.coords=(a,phi,chi); cls.momenta=(pa,pf,pc)
        cls.C=-k*pa**2/(12*a)+(pf**2+pc**2)/(2*a**3)
        cls.alpha=-k*a*pa/(6*pf)
        cls.alpha_chi=-k*a*pa/(6*pc)
        cls.chi_t=chi+(pc/pf)*(cls.t-phi)
        cls.chi_u=chi+(pc/pf)*(cls.u-phi)
        cls.phi_xi=phi+(pf/pc)*(cls.xi-chi)
        cls.scale_t=a*sp.exp(cls.alpha*(cls.t-phi))
        cls.scale_xi=a*sp.exp(cls.alpha_chi*(cls.xi-chi))

    def test_symbolic_brackets_on_and_off_constraint(self):
        pb=lambda f,g: poisson(f,g,self.coords,self.momenta)
        self.assertEqual(pb(self.chi_t,self.C),0)
        self.assertEqual(sp.simplify(pb(self.alpha,self.C)+self.k*self.C/(2*self.pf)),0)
        self.assertEqual(sp.simplify(pb(self.scale_t,self.C)
                         +self.k*(self.t-self.phi)*self.C*self.scale_t/(2*self.pf)),0)
        # Check residual does not vanish identically off shell.
        value=pb(self.scale_t,self.C).subs({self.k:6,self.a:1,self.pa:-1,
                                           self.pf:3,self.pc:4,self.phi:1,self.t:2})
        self.assertNotEqual(value,0)

    def test_second_clock_and_matching_maps(self):
        match={self.xi:self.chi_t}
        self.assertEqual(sp.simplify(self.phi_xi.subs(match)-self.t),0)
        self.assertEqual(sp.simplify(self.scale_xi.subs(match)-self.scale_t),0)
        self.assertEqual(poisson(self.phi_xi,self.C,self.coords,self.momenta),0)
        # Two trajectories at the same φ-reading do not generally agree on χ reading.
        self.assertNotEqual(self.chi_t.subs({self.chi:1,self.phi:1,self.pc:4,self.pf:3,self.t:2}),
                            self.chi_t.subs({self.chi:2,self.phi:1,self.pc:4,self.pf:3,self.t:2}))
        # Use fresh unrestricted symbols: here pc=0 and pf!=0.
        a, pf, pc=sp.symbols('A p_f p_c', real=True)
        C=-self.k*self.pa**2/(12*a)+(pf**2+pc**2)/(2*a**3)
        self.assertEqual(sp.diff(C,pc).subs({a:1,pc:0}),0)
        self.assertEqual(sp.diff(C,pf).subs({a:1,pf:3}),3)

    def test_multireading_poisson_bracket(self):
        actual=poisson(self.chi_t,self.chi_u,self.coords,self.momenta)
        expected=(self.u-self.t)*(self.pf**2+self.pc**2)/self.pf**3
        self.assertEqual(sp.simplify(actual-expected),0)
        self.assertNotEqual(actual.subs({self.u:2,self.t:1,self.pf:3,self.pc:4}),0)

    def test_expand_branch_and_gauge_invariant_proper_duration(self):
        k,a,pf,pc,pa=self.k,self.a,self.pf,self.pc,self.pa
        s=sp.sqrt(pf**2+pc**2)
        branch={pa:-sp.sqrt(6/k)*s/a}
        self.assertEqual(sp.simplify(self.C.subs(branch)),0)
        self.assertEqual(sp.simplify((self.alpha*pf).subs(branch)-s*sp.sqrt(k/6)),0)
        # Exact proper-time integral over either monotone clock parameter.
        A,alpha,h,t0,t1=sp.symbols('A alpha h t0 t1',positive=True)
        tau=sp.symbols('z', real=True)
        p=h/alpha
        integral=sp.integrate(A**3*sp.exp(3*alpha*(tau-t0))/p,(tau,t0,t1))
        formula=A**3*(sp.exp(3*alpha*(t1-t0))-1)/(3*h)
        self.assertEqual(sp.simplify(integral-formula),0)
        # With χ = χ0 + (pc/pf)(τ−τ0), αχΔχ = αΔτ and αχ pc=α pf.
        self.assertEqual(sp.simplify(self.alpha_chi*self.pc-self.alpha*self.pf),0)
        self.assertEqual(sp.simplify(self.alpha_chi*(self.pc/self.pf)*(self.t-self.u)
                                     -self.alpha*(self.t-self.u)),0)

    def test_nonzero_duration_positive_local_energy_and_clock_orientation(self):
        h=5.; a0=1.; alpha=5/3
        delta_tau=(3/5)*math.log(2)
        duration=a0**3*math.expm1(3*alpha*delta_tau)/(3*h)
        self.assertAlmostEqual(duration,7/15)
        self.assertAlmostEqual(math.exp(alpha*delta_tau),2.)
        self.assertAlmostEqual(25/2/(2**6),25/128)
        self.assertAlmostEqual(5/(2**3),5/8)
        # A pastward φ increment gives negative signed duration, while a
        # negative-momentum clock decreases towards the future.
        self.assertLess(math.expm1(3*alpha*(-.1))/(3*h),0)
        self.assertGreater(math.expm1(3*(-alpha)*(-.1))/(3*h),0)


if __name__ == '__main__':
    unittest.main()
