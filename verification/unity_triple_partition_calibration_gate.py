#!/usr/bin/env python3
"""Finite sanity checks of an exclusive-partition marginal bound, not an assay."""
from fractions import Fraction as F
from itertools import product
from math import exp
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def realize(p, t):
    # Five partitions: ABC, AB|C, AC|B, BC|A, A|B|C.
    return (t, *(x-t for x in p), 1-sum(p)+2*t)


def bounds(p):
    return max(F(0), (sum(p)-1)/2), min(p)


def main():
    vals = [F(i, 4) for i in range(5)]
    admissible = impossible = checked = 0
    for p in product(vals, repeat=3):
        lo, hi = bounds(p)
        if lo > hi:
            impossible += 1
            continue
        admissible += 1
        for t in (lo, hi, (lo+hi)/2):
            weights = realize(p, t)
            assert sum(weights) == 1 and all(w >= 0 for w in weights)
            assert all(weights[0] + weights[i+1] == p[i] for i in range(3))
            checked += 1
    assert admissible + impossible == 125
    p = (F(9,10),)*3
    assert bounds(p) == (F(17,20), F(9,10))
    # General family: 10% ABC, 80% all three pairs separately, 10% empty.
    # Same pair marginals as the exclusive 90% ABC / 10% empty mixture.
    overlap = {'ABC':F(1,10), 'AB_AC_BC':F(8,10), 'empty':F(1,10)}
    assert sum(overlap.values()) == 1
    assert overlap['ABC']+overlap['AB_AC_BC'] == F(9,10)
    assert overlap['ABC'] == F(1,10)
    a = b = F(1,20)
    radius = F(1,20)
    low = (F(9,10)-radius-a)/(1-a)
    triple_upper = (F(1,10)+radius)/(1-b)
    exclusive_lower = (3*low-1)/2
    assert low == F(16,19) and exclusive_lower == F(29,38)
    assert triple_upper == F(3,19) and exclusive_lower > triple_upper
    n = 1020
    failure = 8*exp(-2*n*float(radius)**2)
    assert failure < 0.05
    report = {
        'scope':'Abstract event/partition and hypothetical report-error constraints only; no human data or experiential assay.',
        'quarter_grid_marginal_triples':125,
        'feasible_triples':admissible,
        'infeasible_triples':impossible,
        'endpoint_and_midpoint_distributions_checked':checked,
        'exact_pair_marginals':['9/10']*3,
        'exclusive_triple_sharp_interval':['17/20','9/10'],
        'nonexclusive_family_triple':'1/10',
        'finite_report_example':{'per_pair_report_mean':'9/10','triple_report_mean':'1/10',
            'assumed_per_test_class_error_bounds':'1/20', 'simultaneous_sampling_radius':'1/20',
            'pair_probability_lower':'16/19','exclusive_triple_lower':'29/38',
            'triple_probability_upper':'3/19','trials_per_arm':n,'union_bound_failure':failure},
        'warning':'Calibration, no-probe-effect and comparable latent targets are assumptions, not established evidence.'}
    (ROOT/'verification/unity_triple_partition_calibration_gate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
