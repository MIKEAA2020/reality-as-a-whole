#!/usr/bin/env python3
"""Exhaustive finite-set check of a conditional witness-count bound.

No real people, clinical classification or phenomenal calibration is tested.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def bounds(m, a, b, j=0):
    assert 0 <= a <= m and 0 <= b <= m and 0 <= j <= min(a, b)
    return max(0, m - a - b + j), m - j


def exhaustive(m, a, b, j):
    observed = set()
    mask = (1 << m) - 1
    for f in range(1 << m):
        if f.bit_count() > a:
            continue
        for g in range(1 << m):
            if g.bit_count() <= b and (f & g).bit_count() >= j:
                observed.add((mask & ~(f | g)).bit_count())
    return observed


def main():
    cases = 0
    for m in range(7):
        for a in range(m + 1):
            for b in range(m + 1):
                for j in range(min(a, b) + 1):
                    lo, hi = bounds(m, a, b, j)
                    assert exhaustive(m, a, b, j) == set(range(lo, hi + 1))
                    cases += 1
    assert bounds(4, 1, 2) == (1, 4)
    assert bounds(4, 1, 3) == (0, 4)
    assert bounds(4, 1, 3, 1) == (1, 3)
    report = {
        'scope': 'Finite set arithmetic only; no clinical observations, error bounds, experience or causal structure are established.',
        'parameter_combinations_checked_exhaustively': cases,
        'maximum_synthetic_selected_cases': 6,
        'illustrations': {
            'm4_a1_b2_overlap0': list(bounds(4, 1, 2)),
            'm4_a1_b3_overlap0': list(bounds(4, 1, 3)),
            'm4_a1_b3_overlap1': list(bounds(4, 1, 3, 1))
        }
    }
    (ROOT / 'verification/experiential_anatomical_witness_gate.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
