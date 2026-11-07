#!/usr/bin/env python3
"""Synthetic counterexample at actual Banik sampling times, NOT a data fit.

Usage: python verification/hubble_phase_identifiability.py /path/to/hubFrct_2021
Requires mat-io==1.0.2 and NumPy. See EXPANDING_BEC_RAMP_COVERAGE.md.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from matio import load_from_mat


def example(path, root):
    p = load_from_mat(path)['A'].properties
    times = np.asarray(p['EvTime']).ravel()
    start = float(np.asarray(p['t_phn1']).item())
    duration = float(np.asarray(p['t_exp']).item())
    center = start + duration / 2
    left = float(times[times < center].max())
    right = float(times[times > center].min())
    if np.any((times > left + 1e-9) & (times < right - 1e-9)):
        raise ValueError('selected interval contains another sample')
    width = right - left
    freq = 50.0  # illustrative hertz, not fitted to this trace
    omega = 2 * np.pi * freq
    epsilon = 0.1  # radians
    if omega <= epsilon * np.pi / width:
        raise ValueError('phase need not be monotone under this construction')

    def phase(t, sign):
        t = np.asarray(t)
        z = (t - left) / width
        bump = np.where((z > 0) & (z < 1), np.sin(np.pi * z) ** 2, 0.0)
        return omega * (t - start) + sign * epsilon * bump

    plus, minus = phase(times, 1), phase(times, -1)
    qdiff = float(np.max(np.abs(np.sin(plus) - np.sin(minus))))
    mid = (left + right) / 2
    phase_diff = float(phase(mid, 1) - phase(mid, -1))
    assert qdiff < 1e-11
    assert abs(phase_diff - 2 * epsilon) < 1e-11
    # At each measured time the continuously differentiable bump and its derivative vanish,
    # so synthetic q and q' agree; only the unobserved interior differs.
    sample_slope_diff = float(np.max(np.abs(omega * np.cos(plus) - omega * np.cos(minus))))
    assert sample_slope_diff < 1e-8
    return {'source_file': str(path.relative_to(root)),
            'sample_time_slices': len(times),
            'unsampled_interval_ms_relative_to_ramp_start': [(left-start)*1000, (right-start)*1000],
            'max_sample_signal_difference': qdiff,
            'max_sample_signal_derivative_difference_per_s': sample_slope_diff,
            'synthetic_midpoint_phase_difference_rad': phase_diff,
            'analytic_phase_rate_lower_bound_rad_per_s': omega - epsilon*np.pi/width}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_root', type=Path)
    root = ap.parse_args().source_root.resolve()
    files = [
        root/'data/expansions/PhnRuns_2021-02-24_0827-0946.mat',
        root/'data/contractions/PhnRuns_2021-02-20_0115-0234.mat',
    ]
    print(json.dumps({'warning': 'Synthetic signals, illustrative 50 Hz; not an experimental fit or uncertainty interval.',
                      'examples': [example(p, root) for p in files]}, indent=2))


if __name__ == '__main__':
    main()
