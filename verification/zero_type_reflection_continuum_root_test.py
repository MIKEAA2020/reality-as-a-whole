"""Continuum obstruction, all-resolution shortcut and graph repair checks."""
from fractions import Fraction as F
import unittest
import numpy as np
import sympy as sp

from verification.zero_type_reflection_continuum_root import (
    reflected_angle,sym_loop_weight,midpoint_angles,shortcut_rate,
    quadratic_energy,graph_f,graph_derivative,existing_rates,
)


class TypeReflectionContinuumRootTests(unittest.TestCase):
    def test_original_reflection_jumps_on_a_smooth_relational_observable(self):
        for epsilon in (F(1,10),F(1,100),F(1,1000)):
            left=F(-1)+epsilon;right=epsilon
            self.assertEqual(reflected_angle(-epsilon),left)
            self.assertEqual(reflected_angle(epsilon),right)
            self.assertEqual(right-left,1)
            # The reflected observable u jumps by 1 at the band junction;
            # endpoint values at exactly zero cannot repair its L² class.

    def test_all_resolutions_obstruct_nearest_neighbour_crossing(self):
        for n in (4,8,12,16,32):
            q,r,s=existing_rates(n);m=n//2
            self.assertEqual(q[0,m],0.)
            self.assertGreater(q[m-1,m],0.)
            self.assertAlmostEqual(s[0,m],float(shortcut_rate(n)),places=10)
            self.assertAlmostEqual(s[m-1,m],float(shortcut_rate(n)),places=10)
            np.testing.assert_allclose(s@r,r@s,atol=1e-11)
            np.testing.assert_allclose(s@np.ones(n),0,atol=1e-10)
        # For any nearest-neighbor Q commuting with R, Q[m-1,m] =
        # Q[0,m] = 0, disconnecting the two halves. This is algebraic,
        # independent of the numerical rates in the original operator.

    def test_continuum_shortcut_cost_diverges_for_f_of_u_equals_u(self):
        for n in (4,8,16,32,64,128):
            q,_,s=existing_rates(n);u=midpoint_angles(n);m=n//2
            self.assertAlmostEqual(u[m]-u[0],1.,places=14)
            energy=quadratic_energy(s,u)
            self.assertGreaterEqual(energy+1e-12,n/8)
            self.assertAlmostEqual(quadratic_energy(q,u),F(2,3)*(1-F(1,n*n)),places=10)
        # A single long edge contributes exactly N/8 to the normalized form.
        # The finite N symmetry repair therefore has no bounded free-interval
        # energy on the smooth fixed function f(u)=u as N grows.

    def test_formal_graph_loop_has_matching_reflection_symmetric_weight(self):
        for u in (F(-1),F(-7,8),F(-1,2),F(-1,8),F(0)):
            self.assertEqual(sym_loop_weight(u),sym_loop_weight(-1-u))
            self.assertGreaterEqual(sym_loop_weight(u),F(1,2))
        self.assertEqual(sym_loop_weight(-1),F(1,2))
        self.assertEqual(sym_loop_weight(0),F(1,2))
        with self.assertRaises(ValueError):sym_loop_weight(F(1,2))
        with self.assertRaises(ValueError):shortcut_rate(6)

    def test_nonconstant_smooth_graph_mode_respects_glued_vertex_and_reflection(self):
        eps=1e-8
        self.assertAlmostEqual(graph_f(-1+eps),graph_f(-eps),places=6)
        self.assertAlmostEqual(graph_f(-eps),graph_f(eps),places=6)
        for u in (-.8,-.63,-.4,-.1,.1,.4,.9):
            self.assertAlmostEqual(graph_f(reflected_angle(u)),-graph_f(u),places=12)
        # Kirchhoff: outgoing loop fluxes at -1 and 0 cancel; tail flux is 0.
        left=F(1,2)*graph_derivative(-1)
        right=-F(1,2)*graph_derivative(-eps)
        tail=graph_derivative(eps)
        self.assertAlmostEqual(left+right+tail,0,places=10)
        u=sp.symbols('u',real=True);p=sp.Rational(1,2)-u-u*u
        energy=sp.integrate(p*(2*sp.pi*sp.cos(2*sp.pi*u))**2/2,(u,-1,0))
        self.assertEqual(sp.simplify(energy),-sp.Rational(1,8)+2*sp.pi**2/3)
        target=float(energy)
        errors=[]
        for n in (16,32,64,128,256):
            _,_,q=existing_rates(n)
            f=[graph_f(x) for x in midpoint_angles(n)]
            errors.append(abs(quadratic_energy(q,f)-target))
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],.05)  # finite-grid, first-order vertex error

    def test_only_constant_common_zero_of_positive_graph_form(self):
        # Graph connectedness plus positive edge weights gives the proof;
        # finite matrices check a representative discretization.
        for n in (4,8,16,32):
            _,_,q=existing_rates(n)
            eigen=np.linalg.eigvalsh(-q)
            self.assertAlmostEqual(eigen[0],0,places=10)
            self.assertGreater(eigen[1],0)
        # A zero form forces zero derivative on loop and tail. Vertex
        # continuity then makes their constants equal.

if __name__=='__main__':unittest.main()
