"""Constitutive candidate on the existing echo, with exact alternatives.

Everything modeled is conditional on explicit occurrence, quality, metric,
owner and sampling hypotheses. Passing checks cannot establish experience.
Run: python -m unittest verification.zero_sr_echo_constitution_test -v
"""
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_joint_quality_incidence_root import (
    quality, weight, swap, counterpart, echo_checkpoints, R)
from verification.zero_echo_constitutive_modes import modes
from verification.zero_echo_joint_identity_balance import EVENTS, magnitude, physical_ledger
from verification.zero_echo_mode_clock_transport import (
    BASIS, PREFIXES, logical_circuit, past_labels, mode_values)


def candidate_quality(i, sign, transverse_gain=1):
    """Coordinates under the hypothetical quality interpretation, not proof."""
    s, t = modes(i, sign)
    g = magnitude(i)
    return g*s, g*F(transverse_gain)*t


def candidate_owner(i, sign, time, persistent=True):
    if time not in range(4):
        raise ValueError('invalid checkpoint')
    ledger = physical_ledger(i, sign)
    return ledger if persistent else (ledger, time)


def symmetry_rule(a, b, n, k):
    """Every specified finite-spectrum equivariant vector has this form."""
    return F(a)*F(n+k, 2), F(b)*F(n-k, 2)


def classes(fn):
    groups = {}
    for event in EVENTS:
        groups.setdefault(fn(*event), []).append(event)
    return groups


def guess_probability(groups):
    return sum(max(weight(*event) for event in group)
               for group in groups.values())


class SREchoConstitutionTests(unittest.TestCase):
    def test_all_equivariant_finite_value_maps_on_bounded_grid(self):
        # Check all maps from four sign pairs to a 3x3 output grid; no
        # linearity is assumed. Algebra proves the same for arbitrary reals.
        pairs = tuple(product((1, -1), repeat=2))
        outputs = tuple(product((-1, 0, 1), repeat=2))
        matching = []
        for values in product(outputs, repeat=4):
            mapping = dict(zip(pairs, values))
            def neg(v): return (-v[0], -v[1])
            def reflect(v): return (v[0], -v[1])
            if all(mapping[k, n] == reflect(mapping[n, k]) and
                   mapping[-n, -k] == neg(mapping[n, k]) for n, k in pairs):
                matching.append(mapping)
                a = mapping[1, 1][0]
                b = mapping[1, -1][1]
                for n, k in pairs:
                    self.assertEqual(mapping[n, k], symmetry_rule(a, b, n, k))
        self.assertEqual(len(matching), 9)
        self.assertEqual(sum(m[1, 1] == (1, 0) for m in matching), 3)

    def test_candidate_transforms_as_declared_on_actual_echo(self):
        for gain in (F(0), F(1), F(2), F(-1)):
            for i, sign in EVENTS:
                q = candidate_quality(i, sign, gain)
                self.assertEqual(candidate_quality(*swap(i, sign), gain), (q[0], -q[1]))
                self.assertEqual(candidate_quality(*counterpart(i, sign), gain), (-q[0], -q[1]))
                self.assertEqual(sum(x*x for x in q),
                                 magnitude(i)**2 * (1 if R[i] == 1 else gain**2))

    def test_anchored_normalized_isometry_still_needs_orientation(self):
        # Full four-sign formal spectrum at a fixed positive magnitude.
        for gain in (F(-2), F(-1), F(0), F(1, 2), F(1), F(2)):
            pairs = tuple(product((1, -1), repeat=2))
            norm_preserved = all(sum(x*x for x in symmetry_rule(1, gain, n, k)) ==
                                 F(n*n+k*k, 2) for n, k in pairs)
            self.assertEqual(norm_preserved, gain in (-1, 1))
        self.assertEqual(symmetry_rule(1, 1, 1, -1), (0, 1))
        self.assertEqual(symmetry_rule(1, -1, 1, -1), (0, -1))

    def test_actual_positive_sector_cannot_select_gain(self):
        for i, sign in EVENTS:
            q1 = candidate_quality(i, sign, 1)
            q2 = candidate_quality(i, sign, 2)
            if R[i] == 1:
                self.assertEqual(q1, q2)
            else:
                self.assertNotEqual(q1, q2)
                self.assertEqual(q1[0], 0)
                self.assertEqual(q2[1], 2*q1[1])
        self.assertEqual(sum(weight(i, s) for i, s in EVENTS if R[i] == -1), F(1, 2))
        self.assertEqual({magnitude(i) for i in range(4) if R[i] == -1}, {F(3, 16)})
        self.assertEqual({magnitude(i) for i in range(4) if R[i] == 1},
                         {F(5, 16), F(21, 16)})

    def test_content_equality_is_not_owner_equality(self):
        for gain in (F(1), F(2), F(-1)):
            qclasses = classes(lambda i, s: candidate_quality(i, s, gain))
            self.assertEqual(len(qclasses), 6)
            self.assertEqual(guess_probability(qclasses), F(3, 4))
        self.assertEqual(len(classes(lambda i, s: candidate_quality(i, s, 0))), 5)
        self.assertEqual(guess_probability(classes(lambda i, s: candidate_quality(i, s, 0))), F(5, 8))
        self.assertEqual(candidate_quality(0, 1), candidate_quality(1, -1))
        self.assertNotEqual(candidate_owner(0, 1, 3), candidate_owner(1, -1, 3))
        self.assertEqual(len(classes(physical_ledger)), 8)

    def test_ledger_ownership_and_incidence_are_distinct_hypotheses(self):
        slots = [(i, sign, t) for i, sign in EVENTS for t in range(4)]
        self.assertEqual(len(slots), 32)
        self.assertEqual(len({candidate_owner(i, s, t, True) for i, s, t in slots}), 8)
        self.assertEqual(len({candidate_owner(i, s, t, False) for i, s, t in slots}), 32)
        self.assertEqual(sum(weight(i, s)*F(1, 4) for i, s, t in slots), 1)
        for i, sign in EVENTS:
            self.assertEqual(len({candidate_owner(i, sign, t, True) for t in range(4)}), 1)
            self.assertEqual(len({candidate_owner(i, sign, t, False) for t in range(4)}), 4)
            self.assertEqual(sum(weight(i, sign)*F(1, 4) for t in range(4)), F(1, 8))
            # Both labelings have the same physical checkpoint records.
            self.assertEqual(len(echo_checkpoints(i, sign)), 4)

    def test_transport_full_mode_vector_not_naive_instantaneous_vector(self):
        for initial, sign in product(BASIS, (1, -1)):
            anchor = logical_circuit(initial, ('T', 'Q', 'T'))
            anchored = mode_values(anchor[1], anchor[2], sign)
            for checkpoint, prefix in enumerate(PREFIXES):
                b, j, r = logical_circuit(initial, prefix)
                ja, ra = past_labels(checkpoint, b, j, r)
                self.assertEqual(mode_values(ja, ra, sign), anchored)
                for gain in (F(0), F(1), F(2)):
                    self.assertEqual((anchored[0], gain*anchored[1]),
                                     (mode_values(ja, ra, sign)[0],
                                      gain*mode_values(ja, ra, sign)[1]))
        initial = (-1, 1, 1)
        anchor = logical_circuit(initial, ('T', 'Q', 'T'))
        self.assertNotEqual(mode_values(initial[1], initial[2], 1),
                            mode_values(anchor[1], anchor[2], 1))

    def test_counterpart_pairs_sum_zero_not_vanishing_individuals(self):
        for i in range(4):
            q = candidate_quality(i, 1)
            other = candidate_quality(i, -1)
            self.assertEqual(tuple(x+y for x, y in zip(q, other)), (0, 0))
            self.assertNotEqual(q, (0, 0))
            self.assertNotEqual(other, (0, 0))


if __name__ == '__main__':
    unittest.main()
