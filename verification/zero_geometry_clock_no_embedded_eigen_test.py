"""Controls for the continuum no-embedded-eigenvalue estimate.

The inequality and cyclicity theorem are analytic in the companion note;
finite sampling and Nyström eigenvalues do not establish continuum spectral
claims. Uses existing standard-library routines only.
"""
import cmath
import math
import unittest

from verification.zero_sphere_interacting_clock_spectral_test import build
from verification.zero_sphere_finite_resolution_clock_instrument_test import dot,apply,window_kernel
from verification.zero_interacting_clock_mourre_spectrum_test import kernel_prime
from verification.zero_interacting_geometry_slice_clock_test import factors,initial_state,p_to_s

COUPLING=.8
M=14/(3*math.pi*math.sqrt(3))
Q=COUPLING*M/2


class GeometryClockNoEmbeddedEigenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p,cls.f,cls.E,cls.systems=build(80)

    def test_exact_kernel_constant_and_contraction(self):
        self.assertAlmostEqual(Q,28/(15*math.pi*math.sqrt(3)))
        self.assertLess(Q,.344)
        self.assertGreater(Q,.342)
        self.assertLess(COUPLING,3*math.pi*math.sqrt(3)/7)
        for d in (0,.1,.25,.5,.75,1):
            self.assertLessEqual(abs(kernel_prime(d)),14*d/(3*math.pi)+1e-12)
            self.assertLessEqual(abs(kernel_prime(-d)),14*d/(3*math.pi)+1e-12)

    def test_uniform_kernel_derivative_l2_bound(self):
        n=len(self.p);dp=1/n
        for p0 in (-7.,-6.975,-6.8,-6.5,-6.2,-6.025,-6.):
            integral=sum(dp*kernel_prime(p0-q)**2 for q in self.p)
            self.assertLessEqual(integral,M*M+1e-12)
        # Analytical comparison ∫_0^1 |x-y|²dy <= 1/3.
        for i in range(101):
            x=i/100
            self.assertLessEqual((x**3+(1-x)**3)/3,1/3+1e-15)

    def test_l2_divergence_if_numerator_does_not_vanish_on_shell(self):
        # ∫_ε^δ du/u² = 1/ε−1/δ -> infinity, at interior or edge.
        delta=.1
        vals=[1/e-1/delta for e in (.01,.001,.0001)]
        self.assertLess(vals[0],vals[1]);self.assertLess(vals[1],vals[2])
        self.assertGreater(vals[-1],9000)

    def test_pinned_smooth_kernel_contraction_on_complex_samples(self):
        # Forcing (Ef)(p0)=0 mimics the necessary on-shell condition.
        # This is a discrete control, not the continuum proof.
        p=self.p;n=len(p);dp=1/n
        for p0 in (-6.997,-6.853,-6.503,-6.173,-6.003):
            k=[window_kernel(p0-x) for x in p]
            k2=sum(x*x for x in k)
            for mode in (1,3,9):
                v=[complex(math.sin(mode*x),math.cos((mode+1)*x)) for x in p]
                coeff=sum(k[i]*v[i] for i in range(n))/k2
                v=[v[i]-coeff*k[i] for i in range(n)]
                self.assertLess(abs(sum(k[i]*v[i]*dp for i in range(n))),1e-13)
                ev=apply(self.E,v)
                quot=[COUPLING*ev[i]/((p[i]**2-p0**2)/6) for i in range(n)]
                self.assertLessEqual(math.sqrt(dot(quot,quot).real/dot(v,v).real),Q+1e-10)

    def test_finite_grid_interior_points_are_not_bound_state_count(self):
        for d in (1,-1):
            ev=self.systems[d][1]
            self.assertEqual(sum(6<x<49/6 for x in ev),len(ev)-1)
            self.assertEqual(sum(x<6 or x>49/6 for x in ev),1)
        # The N−1 interior eigenvalues discretize the continuous band and
        # are not evidence for or against continuum embedded eigenstates.

    def test_continuum_slice_change_spectral_measures_atomic_control(self):
        # ν_(β,α)=<aβ,P(ds)aα>, rho=dν/dμα=Aβ/Aα; μβ=|rho|² μα.
        # gβ=gα/conj(rho) with norm ∑2ω|g|² μ invariant.
        r0=factors(self.p,self.systems,0)
        r2=factors(self.p,self.systems,2)
        coeff=p_to_s(initial_state(self.f),self.systems)
        norm0=norm2=0.
        for h,d in coeff:
            for j,e in enumerate(self.systems[d][1]):
                w=math.sqrt(e-2*h);A0=r0[h,d][j]*math.sqrt(2*w);A2=r2[h,d][j]*math.sqrt(2*w)
                mu0=abs(A0)**2;mu2=abs(A2)**2;rho=A2/A0
                nu0=r0[h,d][j]*coeff[h,d][j];nu2=r2[h,d][j]*coeff[h,d][j]
                g0=nu0/mu0;g2=nu2/mu2
                self.assertAlmostEqual(mu2,abs(rho)**2*mu0,places=13)
                self.assertAlmostEqual(abs(g2-g0/rho.conjugate()),0,places=12)
                norm0+=2*w*abs(g0)**2*mu0;norm2+=2*w*abs(g2)**2*mu2
        self.assertAlmostEqual(norm0,1,places=11);self.assertAlmostEqual(norm2,1,places=11)

    def test_invisible_degeneracy_counterexample_not_applicable_by_assumption(self):
        # A multiplicity-two spectral fiber allows an antisymmetric invisible
        # state for a symmetric slice vector; proven multiplicity-one a.c. and
        # one simple point eigenstate exclude this in the actual continuum model.
        for phi in (0,3,7):
            plus=cmath.exp(1j*phi)/math.sqrt(2)
            minus=-cmath.exp(1j*phi)/math.sqrt(2)
            self.assertAlmostEqual(abs(plus+minus),0)

if __name__=='__main__':unittest.main()
