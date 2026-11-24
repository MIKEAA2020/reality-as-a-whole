"""Finite-window instrument in the interacting FLRW physical sector.

Numerical edge eigenvectors use Nyström discretization; the continuum existence
and non-invariance arguments are in the accompanying note. No autonomous
local readout, exact instantaneous geometry-clock switch, or full GR claimed.
"""
import cmath
import math
import unittest
from verification.zero_sphere_interacting_clock_spectral_test import build,transform,untransform
from verification.zero_sphere_finite_resolution_clock_instrument_test import apply,dot,no_filter


def vecsub(x,y): return [a-b for a,b in zip(x,y)]
def norm2(x): return dot(x,x).real
def cmul(c,x): return [c*a for a in x]


def evolve(V,values,v,t,h=0):
    a=transform(V,v)
    return untransform(V,[z*cmath.exp(1j*math.sqrt(e-2*h)*t) for z,e in zip(a,values)])


class InteractingClockBoundTransitionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results={n:build(n) for n in (40,80,160)}
        cls.p,cls.f,cls.E,systems=cls.results[80]
        cls.T,cls.values,cls.V=systems[1]
        cls.b=[row[0] for row in cls.V]
        cls.eb=apply(cls.E,cls.b)

    def test_bound_mode_and_contraction(self):
        self.assertLess(self.values[0],6)
        self.assertAlmostEqual(norm2(self.b),1,places=11)
        self.assertLess(norm2(vecsub(apply(self.T,self.b),cmul(self.values[0],self.b))),1e-22)
        # E is a compressed multiplication by 0<=g<=1 in the continuum.
        self.assertGreater(norm2(self.eb),0)
        self.assertLess(norm2(self.eb),1)

    def test_yes_instrument_completeness_on_complex_vectors(self):
        v=[self.f[i]*(1+1j*(i/len(self.f))) for i in range(len(self.f))]
        yes=apply(self.E,v); no=no_filter(self.E,v)
        self.assertAlmostEqual(norm2(yes)+norm2(no),norm2(v),places=10)
        yes=apply(self.E,self.b);no=no_filter(self.E,self.b)
        self.assertAlmostEqual(norm2(yes)+norm2(no),1,places=10)

    def test_bound_outcome_is_not_bound_preserving(self):
        proj=dot(self.b,self.eb)
        outside=vecsub(self.eb,cmul(proj,self.b))
        self.assertAlmostEqual(norm2(self.eb),.05710999243144555,places=10)
        self.assertAlmostEqual(abs(proj)**2,.015945035267930265,places=10)
        self.assertAlmostEqual(norm2(outside),.04116495716351529,places=10)
        self.assertAlmostEqual(norm2(outside)/norm2(self.eb),.7208013065827215,places=10)
        self.assertAlmostEqual(norm2(self.eb),abs(proj)**2+norm2(outside),places=11)

    def test_reverse_transition_from_complement(self):
        outside=vecsub(self.eb,cmul(dot(self.b,self.eb),self.b))
        psi=cmul(1/math.sqrt(norm2(outside)),outside)
        self.assertAlmostEqual(abs(dot(self.b,psi)),0,places=11)
        amplitude=dot(self.b,apply(self.E,psi))
        self.assertAlmostEqual(abs(amplitude)**2,norm2(outside),places=11)

    def test_forward_and_reverse_transition_are_spectral_matrix_elements(self):
        column=transform(self.V,self.eb)
        self.assertAlmostEqual(sum(abs(x)**2 for x in column[1:]),
                               norm2(self.eb)-abs(column[0])**2,places=11)
        for j in (1,5,40,79):
            v=[row[j] for row in self.V]
            self.assertAlmostEqual(abs(dot(v,self.eb)-dot(self.b,apply(self.E,v)).conjugate()),0,places=11)

    def test_bound_reading_probability_stationary_but_readout_disturbs(self):
        initial=norm2(apply(self.E,self.b))
        for t in (0,40,100):
            b_t=evolve(self.V,self.values,self.b,t)
            self.assertAlmostEqual(norm2(apply(self.E,b_t)),initial,places=11)
        # After a yes outcome, the unnormalised state E|b> contains non-bound
        # components; it is not an eigenstate of the interacting root.
        a=transform(self.V,self.eb)
        gaps=[math.sqrt(x)-math.sqrt(self.values[0]) for x in self.values]
        gap_second_moment=sum(abs(a[i])**2*gaps[i]**2 for i in range(len(a)))/norm2(self.eb)
        self.assertGreater(gap_second_moment,1e-5)

    def test_joint_repeated_yes_is_basis_independent(self):
        # P(yes at scalar φ=0, yes at scalar φ=t), on an initial bound state.
        for t in (0,40,100):
            direct=norm2(apply(self.E,evolve(self.V,self.values,self.eb,t)))
            a=transform(self.V,self.eb)
            evolving=[a[i]*cmath.exp(1j*math.sqrt(self.values[i])*t) for i in range(len(a))]
            emat=[[dot([row[i] for row in self.V],apply(self.E,[row[j] for row in self.V]))
                   for j in range(len(a))] for i in range(len(a))]
            spectral=norm2(apply(emat,evolving))
            self.assertAlmostEqual(direct,spectral,places=11)
            self.assertGreaterEqual(direct,0)
            self.assertLessEqual(direct,norm2(self.eb)+1e-12)

    def test_numerical_resolution_not_continuum_proof(self):
        records=[]
        for n in (40,80,160):
            p,f,E,systems=self.results[n];values,V=systems[1][1:]
            b=[row[0] for row in V];eb=apply(E,b)
            records.append((norm2(eb),norm2(eb)-abs(dot(b,eb))**2))
        self.assertAlmostEqual(records[-1][0],.05559684575802826,places=10)
        self.assertAlmostEqual(records[-1][1],.040471793692935826,places=10)
        self.assertLess(abs(records[2][0]-records[1][0]),abs(records[1][0]-records[0][0]))
        self.assertGreater(records[-1][1],.04)

if __name__=='__main__':unittest.main()
