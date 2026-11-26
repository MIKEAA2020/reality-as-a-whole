"""Exact accounting and coherence controls for echo-incidence balance."""
from fractions import Fraction as F
from itertools import product
import unittest
import sympy as sp
from verification.zero_joint_quality_incidence_root import quality,swap,weight
from verification.zero_echo_incidence_balance_root import (
    EVENTS,magnitude,typed_weights,physical_marginal,total_now_weight,signed_total,
    reduced_formula,type_exchange_invariant,counterpart_invariant,constant_alpha,
)


class EchoIncidenceBalanceRootTests(unittest.TestCase):
    def test_physical_table_and_pair_swap_preserve_both_quality_and_magnitude(self):
        self.assertEqual([magnitude(i) for i in range(4)],[F(3,16),F(3,16),F(5,16),F(21,16)])
        for i,s in EVENTS:
            j,t=swap(i,s)
            self.assertEqual(quality(j,t),tuple(reversed(quality(i,s))))
            self.assertEqual(magnitude(i),magnitude(j))
            self.assertEqual(weight(i,s),weight(j,t))

    def test_constant_type_weights_never_affect_sign_balance(self):
        for a in (F(0),F(1,10),F(1,2),F(3,4),F(1)):
            alpha=constant_alpha(a)
            self.assertEqual(total_now_weight(alpha),a)
            self.assertEqual(signed_total(alpha),0)
            self.assertTrue(counterpart_invariant(alpha))
            self.assertEqual(type_exchange_invariant(alpha),a==F(1,2))
            self.assertTrue(all(w==F(1,8) for w in physical_marginal(alpha).values()))

    def test_equal_type_weights_and_type_symmetry_still_allow_imbalance(self):
        a=constant_alpha(F(1,2))
        a[0,1]=a[1,-1]=F(3,4)
        a[0,-1]=a[1,1]=F(1,4)
        self.assertTrue(all(0<x<1 for x in a.values()))
        self.assertEqual(total_now_weight(a),F(1,2))
        self.assertTrue(type_exchange_invariant(a))
        self.assertFalse(counterpart_invariant(a))
        self.assertEqual(signed_total(a),F(3,64))
        self.assertTrue(all(w==F(1,8) for w in physical_marginal(a).values()))
        weights=typed_weights(a)
        for sign, expected_count, expected_magnitude in ((1,F(5,8),F(35,128)),(-1,F(3,8),F(29,128))):
            cells=[(i,s,p) for i,s in EVENTS for k,p in enumerate(('now','echo')) if quality(i,s)[k]==sign]
            self.assertEqual(sum((weights[c] for c in cells),F(0)),expected_count)
            self.assertEqual(sum((weights[c]*magnitude(c[0]) for c in cells),F(0)),expected_magnitude)

    def test_sign_counterpart_suffices_but_is_not_necessary(self):
        a={(i,s):F(i+1,5) for i,s in EVENTS}
        self.assertTrue(counterpart_invariant(a))
        self.assertFalse(type_exchange_invariant(a))
        self.assertEqual(signed_total(a),0)
        b=constant_alpha(F(1,2))
        b[0,1]=b[1,1]=F(3,4)
        self.assertFalse(counterpart_invariant(b))
        self.assertEqual(signed_total(b),0)

    def test_exact_balance_equation_and_sharp_bounds_at_every_binary_vertex(self):
        totals=[]
        for vals in product((0,1),repeat=8):
            a=dict(zip(EVENTS,vals))
            self.assertEqual(signed_total(a),reduced_formula(a))
            totals.append(signed_total(a))
        self.assertEqual((min(totals),max(totals)),(F(-3,32),F(3,32)))
        # Every fractional assignment is a convex combination of the binary
        # vertices; the expression is affine, so these bounds are global.
        a=constant_alpha(F(1,2));a[0,1]=a[1,-1]=1;a[0,-1]=a[1,1]=0
        self.assertTrue(type_exchange_invariant(a))
        self.assertEqual(total_now_weight(a),F(1,2))
        self.assertEqual(signed_total(a),F(3,32))

    def test_diagonal_data_do_not_reproduce_pure_quantum_marginal(self):
        # A logical 8-event comparator has the same diagonal table as the
        # echo, not a claim that it is the full original Hilbert space.
        rho=sp.ones(8,8)/8
        a=[1]+[0]*7
        now=sp.diag(*[sp.Rational(x,8) for x in a])
        echo=sp.eye(8)/8-now
        self.assertEqual(now+echo,sp.eye(8)/8)
        self.assertEqual(list((now+echo).diagonal()),list(rho.diagonal()))
        self.assertNotEqual(now+echo,rho)
        # Trying to restore the pure marginal while keeping this 'now' block
        # makes the required other block nonpositive (negative 2x2 minor).
        remainder=rho-now
        self.assertEqual(remainder[:2,:2].det(),-sp.Rational(1,64))
        self.assertLess(float(min(remainder.eigenvals().keys())),0)
        # For any 0<=A<=|psi><psi|, A annihilates every vector orthogonal
        # to psi and positivity forces A=a|psi><psi|. Hence the conditional
        # type weight is constant on every nonzero diagonal event.
        for a in (sp.Rational(0),sp.Rational(1,3),sp.Rational(1)):
            self.assertEqual(a*rho+(1-a)*rho,rho)

    def test_reject_invalid_type_probabilities(self):
        a=constant_alpha(F(1,2));a[0,1]=F(3,2)
        with self.assertRaises(ValueError):typed_weights(a)
        del a[0,1]
        with self.assertRaises(ValueError):typed_weights(a)

if __name__=='__main__':unittest.main()
