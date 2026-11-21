#!/usr/bin/env python3
"""Independent geometrical controls, not a QPV security or data replay."""
import json
import math
import random
import unittest
from pathlib import Path

from kavuri_qpv_asymmetric_geometry import CENTRAL, evaluate, from_timings, interval_union
from qpv_symmetric_geometry import geometry

ROOT = Path(__file__).resolve().parents[1]


def direct_rho_limit(x, L, ra, rb, ma, mb, quantum):
    """Bisection using distances to foci, not squared-polynomial envelopes."""
    def inside(rho):
        da = math.hypot(x+L/2, rho)
        db = math.hypot(x-L/2, rho)
        sa, sb = da <= ra, db <= rb
        ea, eb = da+db <= ma, da+db <= mb
        return (sa and sb and ea and eb) if quantum else ((sa and ea) or (sb and eb))
    if not inside(0):
        return 0.
    lo, hi = 0., max(ra, rb, ma, mb)
    for _ in range(45):
        mid = (lo+hi)/2
        if inside(mid):
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


class AsymmetricChecks(unittest.TestCase):
    def test_symmetric_against_exact_earlier_formulas(self):
        ref = geometry(100, 110)
        got = evaluate(200, 110, 110, 220, 220)
        self.assertAlmostEqual(got['ratios']['length_same_latency'], 11, places=10)
        self.assertAlmostEqual(got['ratios']['volume_same_latency'], float(ref['volume_ratio']), places=9)
        self.assertAlmostEqual(got['ratios']['area_same_latency'], ref['area_ratio'], places=9)
        self.assertAlmostEqual(got['quantum_volume_m3'], float(ref['quantum_volume_over_pi'])*math.pi, places=6)

    def test_interval_union_and_1d_hand_calculation(self):
        self.assertEqual(interval_union([(0, 3), (2, 5), (8, 9)]), [(0, 5), (8, 9)])
        self.assertEqual(interval_union([None, (3, 3)]), [])
        L, ra, rb, ma, mb = from_timings(CENTRAL)
        got = evaluate(L, ra, rb, ma, mb)
        parts = got['classical_component_axis_intervals_m']
        left = min(p[0] for p in parts)
        right = max(p[1] for p in parts)
        overlap = min(p[1] for p in parts)-max(p[0] for p in parts)
        self.assertGreater(overlap, 0)
        self.assertAlmostEqual(overlap, got['quantum_length_m'], places=9)
        self.assertAlmostEqual(right-left, got['classical_length_m'], places=9)
        self.assertAlmostEqual(got['ratios']['length_naive_component_sum_diagnostic'], got['ratios']['length_same_latency']+1, places=10)
        self.assertLess(got['ratios']['length_same_latency'], max(ma, mb)/got['quantum_length_m'])
        self.assertLess(got['ratios']['length_ellipsoid_upper_bound'], 3.5)

    def test_direct_distance_bisection_midpoint_integrals(self):
        L, ra, rb, ma, mb = from_timings(CENTRAL)
        got = evaluate(L, ra, rb, ma, mb)
        # Midpoint quadrature with independent direct distance tests; no polynomial
        # coefficients or active-profile switching from the production code.
        lo, hi = -max(ma, mb)/2, max(ma, mb)/2
        n = 12000
        dx = (hi-lo)/n
        area = [0., 0.]
        volume = [0., 0.]
        for j in range(n):
            x = lo+(j+.5)*dx
            for k in (0, 1):
                rho = direct_rho_limit(x, L, ra, rb, ma, mb, quantum=(k == 0))
                area[k] += 2*rho*dx
                volume[k] += math.pi*rho*rho*dx
        for computed, key in zip(area, ('quantum_area_m2', 'classical_area_m2')):
            self.assertAlmostEqual(computed, got[key], delta=got[key]*1e-4)
        for computed, key in zip(volume, ('quantum_volume_m3', 'classical_volume_m3')):
            self.assertAlmostEqual(computed, got[key], delta=got[key]*1e-4)

    def test_saved_receipt_and_rounding_bound(self):
        receipt = json.loads((ROOT/'verification/kavuri_qpv_asymmetric_geometry.json').read_text())
        got = evaluate(*from_timings(CENTRAL))
        for key, value in got['ratios'].items():
            self.assertAlmostEqual(value, receipt['central']['ratios'][key], places=10)
        bound = receipt['rounding_corner_stress_test']['conservative_all_inputs_1d_ratio_upper_bound']
        self.assertLess(bound, 3.5)
        rng = random.Random(411)
        for _ in range(50):
            varied = {key: value+rng.uniform(-.05, .05) for key, value in CENTRAL.items()}
            self.assertLessEqual(evaluate(*from_timings(varied))['ratios']['length_same_latency'], bound)
        self.assertAlmostEqual(receipt['cross_check_from_separately_rounded_preprint_table3']['ratios']['length_same_latency'], 3.47211660329531, places=10)
        with self.assertRaises(ValueError):
            evaluate(200, 110, 110, 199, 220)


if __name__ == '__main__':
    unittest.main()
