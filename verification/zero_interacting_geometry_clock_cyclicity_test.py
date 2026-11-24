"""Checks supporting the continuum geometry-slice cyclicity theorem.

Analytic theorem (multiplicity-one a.c. sector + analyticity + Fubini) is in
accompanying note. Finite grids do not prove continuum cyclicity or absence
of singular-continuous spectrum. Standard-library verification only.
"""
import cmath
import math
import unittest

from verification.zero_sphere_interacting_clock_spectral_test import build
from verification.zero_sphere_finite_resolution_clock_instrument_test import window_kernel,dot


def oriented_eigenvector(V,j):
    b=[row[j] for row in V]
    return b if sum(b)>0 else [-x for x in b]


def slice_amplitude(p,b,alpha):
    return sum(cmath.exp(1j*x*alpha)*y for x,y in zip(p,b))/math.sqrt(2*math.pi*len(p))


class GeometrySliceCyclicityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.data={n:build(n) for n in (40,80,160)}

    def test_window_kernel_is_strictly_positive_over_entire_band(self):
        # On |d|<=1, sin(2d)/(pi*d)>0 and Gaussian is positive.
        vals=[window_kernel(j/1000) for j in range(1001)]
        self.assertGreater(min(vals),.17)
        self.assertAlmostEqual(window_kernel(1),math.exp(-.5)*math.sin(2)/math.pi)

    def test_edge_eigenvalues_outside_the_free_band(self):
        for p,f,E,S in self.data.values():
            self.assertLess(S[1][1][0],6)
            self.assertGreater(S[-1][1][-1],49/6)
            for h in (0,1):
                self.assertGreater(min(S[1][1])-2*h,0)

    def test_extremal_eigenvectors_strictly_positive_after_phase_choice(self):
        # This finite-matrix check illustrates, rather than proves, the
        # continuum variational/positivity-improving argument.
        for p,f,E,S in self.data.values():
            for d,j in ((1,0),(-1,-1)):
                b=oriented_eigenvector(S[d][2],j)
                self.assertGreater(min(b),0)
                self.assertAlmostEqual(dot(b,b).real,1,places=11)
                theta=S[d][1][j];mat=S[d][0]
                residual=[sum(mat[i][k]*b[k] for k in range(len(p)))-theta*b[i]
                          for i in range(len(p))]
                self.assertLess(dot(residual,residual).real,1e-22)

    def test_strict_visibility_bound_in_central_geometry_interval(self):
        # Factoring e^(-6.5 i alpha) leaves cos[(p+6.5)alpha]>0
        # for |alpha|<pi and positive b. Thus the amplitude cannot vanish.
        for p,f,E,S in self.data.values():
            for d,j in ((1,0),(-1,-1)):
                b=oriented_eigenvector(S[d][2],j)
                amp0=abs(slice_amplitude(p,b,0))
                for a in (-3.,-2.,-1.,0.,1.,2.,3.):
                    amp=abs(slice_amplitude(p,b,a))
                    self.assertGreaterEqual(amp+1e-13,math.cos(abs(a)/2)*amp0)
                    self.assertGreater(amp,0)
        self.assertAlmostEqual(abs(slice_amplitude(self.data[80][0],
                               oriented_eigenvector(self.data[80][3][1][2],0),0)),
                               .18684262711641278,places=10)

    def test_geometry_evaluation_family_spans_finite_band_regulator(self):
        # alpha_k=2pi*k yields a discrete Fourier basis on the equally spaced
        # momenta, so no nonzero vector is invisible to every geometry slice.
        n=40;p=self.data[n][0]
        basis=[[cmath.exp(-2j*math.pi*k*x)/math.sqrt(n) for x in p] for k in range(n)]
        for k in range(n):
            for j in range(n):
                self.assertAlmostEqual(abs(dot(basis[k],basis[j])-(1 if k==j else 0)),0,places=11)

    def test_free_continuum_has_no_missing_spectral_modes(self):
        # lambda=0, s=omega_h(p) monotone. The geometry evaluation vector
        # and the Jacobian are nonzero at every interior p. Its spectral
        # amplitude is sqrt(|dp/ds|) exp(-ip alpha)/sqrt(2pi).
        for h in (0,1):
            for p in (-6.999,-6.8,-6.5,-6.2,-6.001):
                s=math.sqrt(p*p/6-2*h);jac=6*s/abs(p)
                for a in (-3.,0.,2.,100.):
                    A=math.sqrt(jac)*cmath.exp(-1j*p*a)/math.sqrt(2*math.pi)
                    self.assertAlmostEqual(abs(A)**2,jac/(2*math.pi),places=13)
                    self.assertGreater(abs(A),0)

    def test_twofold_spectral_multiplicity_breaks_one_slice_cyclicity(self):
        # Multiplicity-two counterexample: Ω acts identically on both
        # sectors; a=(u,u)/sqrt(2) misses an antisymmetric state.
        p,f,E,S=self.data[40];scale=math.sqrt(2)
        first=[z/scale for z in f];second=[-z/scale for z in f]
        state_norm=dot(first,first).real+dot(second,second).real
        for t in (-30,0,5,100):
            amplitude=sum((first[i]+second[i])*cmath.exp(1j*(x*x/6)*t)/scale
                          for i,x in enumerate(p))
            self.assertAlmostEqual(abs(amplitude),0)
        self.assertAlmostEqual(state_norm,1,places=12)

if __name__=='__main__':unittest.main()
