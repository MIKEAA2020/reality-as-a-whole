"""Coordinate-equivalence and coarse-graining checks for the echo candidate.

A coordinate relabeling is not claimed to be a physical gauge symmetry, nor
is a modeled quality vector asserted to be a real experience.
Run with PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_sr_echo_coordinate_equivalence_test -v
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_joint_quality_incidence_root import R, weight
from verification.zero_echo_joint_identity_balance import EVENTS, magnitude
from verification.zero_echo_mode_clock_transport import (
    BASIS, PREFIXES, logical_circuit, past_labels, mode_values,
    FINE, clock_shift, anchored_history_projector)
from verification.zero_sr_echo_constitution_test import candidate_quality, candidate_owner


def change_coordinates(q, kappa):
    kappa = F(kappa)
    if kappa == 0:
        raise ValueError('zero is not an invertible coordinate change')
    return q[0], kappa*q[1]


def metric_inner(v, w, kappa):
    """Pullback of the reference Euclidean metric in kappa coordinates."""
    kappa = F(kappa)
    if kappa == 0:
        raise ValueError('zero has no invertible pullback')
    return v[0]*w[0] + v[1]*w[1]/(kappa*kappa)


def distance_sq(q, r, kappa):
    d = tuple(a-b for a, b in zip(q, r))
    return metric_inner(d, d, kappa)


def evidence_partition(kappa):
    result = defaultdict(list)
    for event in EVENTS:
        result[candidate_quality(*event, kappa)].append(event)
    return {key: tuple(value) for key, value in result.items()}


def probabilities(kappa):
    return {key: sum((weight(*event) for event in events), F(0))
            for key, events in evidence_partition(kappa).items()}


def decoded_report(q, kappa, noise):
    """Same reference-axis measurement in rescaled coordinates, with noise."""
    kappa = F(kappa)
    if kappa == 0:
        raise ValueError('cannot invert zero-gain content')
    return q[1]/kappa + F(noise)


class SREchoCoordinateEquivalenceTests(unittest.TestCase):
    def test_rescaling_intertwines_content_and_active_symmetries(self):
        for kappa in (F(-3), F(-1), F(1, 2), F(1), F(2), F(3)):
            for i, sign in EVENTS:
                q1 = candidate_quality(i, sign, 1)
                qk = candidate_quality(i, sign, kappa)
                self.assertEqual(qk, change_coordinates(q1, kappa))
                # The active type swap is (x,y)->(x,-y), and the
                # counterpart is (x,y)->(-x,-y). A_k intertwines both.
                self.assertEqual(change_coordinates((q1[0], -q1[1]), kappa),
                                 (qk[0], -qk[1]))
                self.assertEqual(change_coordinates((-q1[0], -q1[1]), kappa),
                                 (-qk[0], -qk[1]))
        with self.assertRaises(ValueError):
            change_coordinates((F(1), F(1)), 0)

    def test_inverse_metric_preserves_all_actual_pair_distances(self):
        for kappa in (F(-3), F(-1), F(1, 2), F(1), F(2), F(3)):
            for e, f in product(EVENTS, repeat=2):
                q1, r1 = candidate_quality(*e, 1), candidate_quality(*f, 1)
                qk, rk = candidate_quality(*e, kappa), candidate_quality(*f, kappa)
                self.assertEqual(distance_sq(q1, r1, 1), distance_sq(qk, rk, kappa))
                self.assertEqual(metric_inner(qk, qk, kappa), magnitude(e[0])**2)
        with self.assertRaises(ValueError):
            metric_inner((F(1), F(1)), (F(1), F(1)), 0)

    def test_norm_on_support_alone_does_not_fix_cross_metric(self):
        # In q_2 coordinates the symmetric matrix [[1,b],[b,1/4]] is
        # positive definite when |b|<1/2. All actual q lie on axes, so b
        # cannot be found by norms alone; cross-axis distances depend on b.
        k = F(2)
        b = F(1, 4)
        self.assertGreater(F(1, 4)-b*b, 0)
        for event in EVENTS:
            q = candidate_quality(*event, k)
            with_cross = q[0]**2 + 2*b*q[0]*q[1] + q[1]**2/4
            self.assertEqual(with_cross, magnitude(event[0])**2)
        qa, qb = candidate_quality(2, 1, k), candidate_quality(0, 1, k)
        d = (qa[0]-qb[0], qa[1]-qb[1])
        with_cross = d[0]**2+2*b*d[0]*d[1]+d[1]**2/4
        self.assertNotEqual(with_cross, distance_sq(qa, qb, k))
        # Imposing type swap as an isometry removes b: D^T H D=H only if b=0.
        self.assertNotEqual(b, -b)

    def test_all_nonzero_gains_preserve_classes_weights_and_owners(self):
        baseline = evidence_partition(1)
        baseline_groups = {frozenset(v) for v in baseline.values()}
        for kappa in (F(-2), F(-1), F(1, 2), F(2)):
            partition = evidence_partition(kappa)
            self.assertEqual({frozenset(v) for v in partition.values()}, baseline_groups)
            self.assertEqual(len(partition), 6)
            for q, events in baseline.items():
                mapped = change_coordinates(q, kappa)
                self.assertEqual(set(partition[mapped]), set(events))
                self.assertEqual(probabilities(kappa)[mapped], probabilities(1)[q])
            # Joint distribution of quality, owner and sampled checkpoint
            # agrees when only the quality label is transformed.
            base_joint = defaultdict(F)
            changed_joint = defaultdict(F)
            for event, time in product(EVENTS, range(4)):
                owner = candidate_owner(*event, time, True)
                base_joint[change_coordinates(candidate_quality(*event, 1), kappa), owner, time] += weight(*event)*F(1, 4)
                changed_joint[candidate_quality(*event, kappa), owner, time] += weight(*event)*F(1, 4)
            self.assertEqual(base_joint, changed_joint)
            self.assertEqual(sum(base_joint.values()), 1)

    def test_zero_gain_merges_content_but_not_physical_records(self):
        fine, coarse = probabilities(1), probabilities(0)
        self.assertEqual(sorted(fine.values()), [F(1,8)]*4+[F(1,4)]*2)
        self.assertEqual(sorted(coarse.values()), [F(1,8)]*4+[F(1,2)])
        for sign in (1, -1):
            self.assertEqual(candidate_quality(0, sign, 0), candidate_quality(1, sign, 0))
            self.assertNotEqual(candidate_quality(0, sign, 1), candidate_quality(1, sign, 1))
        self.assertEqual(R[0], -1)
        # Four physical events map to one zero content; this is a loss in
        # the proposed content map, not erasure of the physical T record.
        self.assertEqual(len(evidence_partition(0)[(0, 0)]), 4)

    def test_matching_physical_report_with_transformed_decoder(self):
        for event, kappa, noise in product(EVENTS, (F(-2), F(1,2), F(1), F(2)),
                                            (F(-1,16), F(1,16))):
            q1 = candidate_quality(*event, 1)
            qk = candidate_quality(*event, kappa)
            self.assertEqual(decoded_report(q1, 1, noise), decoded_report(qk, kappa, noise))
        q1, q2 = candidate_quality(0, 1, 1), candidate_quality(0, 1, 2)
        self.assertEqual(decoded_report(q1, 1, 0), F(3,16))
        self.assertEqual(decoded_report(q2, 2, 0), F(3,16))
        self.assertEqual(q2[1], F(3,8))  # distinct if decoder is held fixed

    def test_fine_effects_and_coarse_lueders_are_distinct(self):
        # Four-state joint N,K spectrum, G=1. A nonzero label rescaling
        # relabels the same fine projectors; zero gain groups both T signs.
        sign_pairs = tuple(product((1, -1), repeat=2))
        def labeled(k):
            groups = {}
            for idx, (n, e) in enumerate(sign_pairs):
                q = (F(n+e, 2), F(k)*F(n-e, 2))
                groups.setdefault(q, []).append(idx)
            return groups
        for k in (-2, -1, 1, 2):
            for q, indices in labeled(1).items():
                self.assertEqual(labeled(k)[change_coordinates(q, k)], indices)
        self.assertEqual(labeled(0)[(0, 0)], [1, 2])
        psi = np.array([0, 1, 1, 0], dtype=float)/np.sqrt(2)
        rho = np.outer(psi, psi)
        def lueders(groups):
            result = np.zeros((4,4))
            for indices in groups.values():
                p = np.diag([float(i in indices) for i in range(4)])
                result += p@rho@p
            return result
        self.assertAlmostEqual(float(psi@lueders(labeled(0))@psi), 1.0)
        self.assertAlmostEqual(float(psi@lueders(labeled(1))@psi), 0.5)
        self.assertTrue(np.allclose(lueders(labeled(1)), lueders(labeled(2))))

    def test_coordinate_changes_commute_with_clock_transport(self):
        for initial, sign in product(BASIS, (1, -1)):
            anchor = logical_circuit(initial, ('T','Q','T'))
            target = mode_values(anchor[1], anchor[2], sign)
            for checkpoint, prefix in enumerate(PREFIXES):
                b, j, r = logical_circuit(initial, prefix)
                ja, ra = past_labels(checkpoint, b, j, r)
                at_tick = mode_values(ja, ra, sign)
                for k in (F(-2), F(1,2), F(2)):
                    self.assertEqual(change_coordinates(at_tick, k),
                                     change_coordinates(target, k))
        w = clock_shift()
        for outcome in FINE:
            p = anchored_history_projector(1, 'fine', outcome)
            self.assertTrue(np.allclose(w@p, p@w))
            # Relabeling (S,T) to (S,kT) changes only the outcome name,
            # not this already-constructed clock-invariant effect.
            for k in (F(-2), F(1,2), F(2)):
                self.assertNotEqual(k, 0)
                self.assertEqual(change_coordinates(outcome, k)[0], outcome[0])


if __name__ == '__main__':
    unittest.main()
