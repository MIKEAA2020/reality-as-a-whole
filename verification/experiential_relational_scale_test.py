#!/usr/bin/env python3
"""Finite ratio-network controls; not evidence of a phenomenal scale."""
from collections import deque
from fractions import Fraction as F
from itertools import product
import unittest


def infer(nodes, edges):
    """Return normalized components or reject nonpositive/inconsistent ratios.

    Each edge (i,j,r) means m_j = r*m_i. Each connected component's
    first encountered node has magnitude one, a choice of unit only.
    """
    adj = {n: [] for n in nodes}
    for i, j, ratio in edges:
        r = F(ratio)
        if r <= 0:
            raise ValueError('ratio must be positive')
        adj[i].append((j, r))
        adj[j].append((i, 1/r))
    magnitudes = {}
    components = []
    for root in nodes:
        if root in magnitudes:
            continue
        magnitudes[root] = F(1)
        component = []
        pending = deque([root])
        while pending:
            i = pending.popleft()
            component.append(i)
            for j, ratio in adj[i]:
                expected = magnitudes[i]*ratio
                if j in magnitudes:
                    if magnitudes[j] != expected:
                        raise ValueError('inconsistent cycle')
                else:
                    magnitudes[j] = expected
                    pending.append(j)
        components.append(component)
    return magnitudes, components


def total(magnitudes, signs, weights):
    return sum(weights[n]*signs[n]*m for n, m in magnitudes.items())


class RelationalScaleTests(unittest.TestCase):
    def test_connected_calibration_and_asymmetric_zero(self):
        nodes = ['a', 'b', 'c']
        m, components = infer(nodes, [('a', 'b', F(1, 2)), ('b', 'c', 1), ('a', 'c', F(1, 2))])
        signs = {'a': 1, 'b': -1, 'c': -1}
        weights = dict.fromkeys(nodes, 1)
        self.assertEqual(len(components), 1)
        self.assertEqual(total(m, signs, weights), 0)
        self.assertEqual(sorted(signs[n]*m[n] for n in nodes), [F(-1, 2), F(-1, 2), F(1)])
        self.assertFalse(any(signs[n]*m[n] == -m['a'] for n in nodes))
        self.assertEqual(total({n: 7*v for n, v in m.items()}, signs, weights), 0)

    def test_consistent_and_inconsistent_cycle(self):
        nodes = [0, 1, 2]
        m, _ = infer(nodes, [(0, 1, 2), (1, 2, 3), (0, 2, 6)])
        self.assertEqual([m[n] for n in nodes], [1, 2, 6])
        with self.assertRaises(ValueError):
            infer(nodes, [(0, 1, 2), (1, 2, 3), (0, 2, 5)])
        with self.assertRaises(ValueError):
            infer(nodes, [(0, 1, 0)])

    def test_connected_calibration_does_not_force_zero(self):
        m, _ = infer([0, 1, 2], [(0, 1, F(1, 2)), (1, 2, 2)])
        signs, weights = {0: 1, 1: -1, 2: -1}, dict.fromkeys([0, 1, 2], 1)
        self.assertEqual(total(m, signs, weights), F(-1, 2))
        self.assertEqual(total({n: 4*v for n, v in m.items()}, signs, weights), -2)

    def test_disconnected_rescaling_can_fit_or_change_zero(self):
        m, components = infer(['p', 'n'], [])
        self.assertEqual(len(components), 2)
        signs, weights = {'p': 1, 'n': -1}, {'p': 2, 'n': 1}
        self.assertEqual(total(m, signs, weights), 1)
        self.assertEqual(total({'p': F(1), 'n': F(2)}, signs, weights), 0)
        self.assertNotEqual(total({'p': F(2), 'n': F(2)}, signs, weights), 0)

    def test_componentwise_balance_is_robust_without_connection(self):
        m, components = infer([0, 1, 2, 3], [(0, 1, 1), (2, 3, 2)])
        self.assertEqual(len(components), 2)
        signs = {0: 1, 1: -1, 2: 1, 3: -1}
        weights = {0: 1, 1: 1, 2: 2, 3: 1}
        for c1, c2 in product(map(F, (1, 2, 5)), repeat=2):
            scaled = {n: m[n]*(c1 if n < 2 else c2) for n in m}
            self.assertEqual(total(scaled, signs, weights), 0)

    def test_same_order_different_cardinal_ratios(self):
        x, y = [F(1), F(2), F(3)], [F(1), F(4), F(9)]
        self.assertTrue(x[0] < x[1] < x[2] and y[0] < y[1] < y[2])
        self.assertNotEqual(x[1]/x[0], y[1]/y[0])


if __name__ == '__main__':
    unittest.main()
