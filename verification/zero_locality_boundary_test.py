#!/usr/bin/env python3
"""Locality and boundary controls; not evidence for actual valence or signalling."""
from fractions import Fraction as F
from itertools import product
import unittest

from verification.relational_actual_history_zero_test import (
    functional, gradient_density, variance, ystar,
)


def chain_y(x):
    """(I+L)^-1 x for the unweighted three-site chain."""
    matrix = ((5, 2, 1), (2, 4, 2), (1, 2, 5))
    return tuple(sum(F(c)*v for c, v in zip(row, x))/8 for row in matrix)


def chain_gradient(x, y):
    edges = ((0, 1), (1, 2))
    grad = [y[i]-x[i] for i in range(3)]
    for i, j in edges:
        grad[i] += y[i]-y[j]
        grad[j] += y[j]-y[i]
    return tuple(grad)


def ptrace_b(rho):
    return tuple(tuple(sum(rho[2*a+b][2*ap+b] for b in (0, 1))
                       for ap in (0, 1)) for a in (0, 1))


def apply_b_x(rho):
    def flip(i):
        return 2*(i//2)+(1-i%2)
    return tuple(tuple(rho[flip(i)][flip(j)] for j in range(4)) for i in range(4))


def project_b(rho, outcome):
    return tuple(tuple(rho[i][j] if i%2 == outcome and j%2 == outcome else F(0)
                       for j in range(4)) for i in range(4))


class LocalityBoundaryTests(unittest.TestCase):
    def test_two_global_mean_minima_change_local_response(self):
        weights = (F(1),)*3
        k, a, m, lam = F(1), F(1), F(7, 2), F(1)
        examples = [((F(2), F(-1), F(-1)), (F(1), F(-1, 2), F(-1, 2))),
                    ((F(2), F(-1), F(2)), (F(1, 2), F(-1), F(1, 2)))]
        for x, expected_q in examples:
            y = ystar(x, weights, k)
            self.assertEqual(tuple(v-w for v, w in zip(x, y)), expected_q)
            self.assertEqual(variance(x, weights), 2)
            self.assertEqual(functional(x, y, weights, k, a, m, lam), -1)
            self.assertEqual(gradient_density(x, y, weights, k, a, m, lam), ((0, 0, 0), (0, 0, 0)))
            self.assertEqual(sum(expected_q), 0)
        self.assertEqual(examples[0][0][:2], examples[1][0][:2])
        self.assertNotEqual(examples[0][1][0], examples[1][1][0])

    def test_nearest_neighbor_solution_and_zero(self):
        x = (F(2), F(-1), F(-1))
        y = chain_y(x)
        q = tuple(v-w for v, w in zip(x, y))
        self.assertEqual(y, (F(7, 8), F(-1, 4), F(-5, 8)))
        self.assertEqual(q, (F(9, 8), F(-3, 4), F(-3, 8)))
        self.assertEqual(chain_gradient(x, y), (0, 0, 0))
        self.assertEqual(sum(q), 0)
        for x in product(map(F, range(-2, 3)), repeat=3):
            y = chain_y(x)
            self.assertEqual(chain_gradient(x, y), (0, 0, 0))
            self.assertEqual(sum(v-w for v, w in zip(x, y)), 0)

    def test_stationary_chain_end_to_end_dependence(self):
        x = (F(2), F(-1), F(-1))
        y = chain_y(x)
        delta = F(3)
        x2 = (x[0], x[1], x[2]+delta)
        y2 = chain_y(x2)
        self.assertEqual(y2[0]-y[0], delta/8)
        self.assertEqual((x2[0]-y2[0])-(x[0]-y[0]), -delta/8)

    def test_one_clock_boundary_integral(self):
        def y_prime(t):
            return 2*t-6*t*t+4*t*t*t
        def q(t):
            return 2-12*t+12*t*t
        self.assertEqual((y_prime(F(0)), y_prime(F(1))), (0, 0))
        self.assertEqual(y_prime(F(1))-y_prime(F(0)), 0)
        self.assertEqual((q(F(0)), q(F(1, 2)), q(F(1))), (2, -1, 2))
        self.assertEqual(F(2)-F(12, 2)+F(12, 3), 0)
        # y=tau^2 gives y''=2 and endpoint flux 2 instead.
        self.assertEqual(F(2)*(F(1)-F(0)), 2)

    def test_bell_state_unconditional_no_signalling_and_conditioning(self):
        rho = tuple(tuple(F(1, 2) if i in (0, 3) and j in (0, 3) else F(0)
                          for j in range(4)) for i in range(4))
        marginal = ((F(1, 2), F(0)), (F(0), F(1, 2)))
        self.assertEqual(ptrace_b(rho), marginal)
        self.assertEqual(ptrace_b(apply_b_x(rho)), marginal)
        branch0, branch1 = project_b(rho, 0), project_b(rho, 1)
        dephased = tuple(tuple(branch0[i][j]+branch1[i][j] for j in range(4)) for i in range(4))
        self.assertEqual(ptrace_b(dephased), marginal)
        self.assertEqual(ptrace_b(branch0), ((F(1, 2), F(0)), (F(0), F(0))))
        self.assertEqual(ptrace_b(branch1), ((F(0), F(0)), (F(0), F(1, 2))))
        # Branches are unnormalized; conditional records require selection information.

    def test_local_source_changes_global_constraint(self):
        x = (F(2), F(-1), F(-1))
        source = (F(1), F(0), F(0))
        # Stationarity of F_y - sum_i J_i*y_i is (I+L)y=x+J.
        y = chain_y(tuple(v+j for v, j in zip(x, source)))
        self.assertEqual(chain_gradient(x, y), source)
        self.assertEqual(sum(v-w for v, w in zip(x, y)), -sum(source))


if __name__ == '__main__':
    unittest.main()
