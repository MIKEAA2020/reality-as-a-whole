#!/usr/bin/env python3
"""Audit Banik et al. ramp sampling and cross-check decoded MATLAB fields.

Usage: python verification/hubble_ramp_coverage.py /path/to/hubFrct_2021
Requires mat-io==1.0.2, NumPy and SciPy (see EXPANDING_BEC_RAMP_COVERAGE.md).
This is not a fit and does not estimate a temporal phase or phase residual.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from matio import load_from_mat

# Absolute tolerance in seconds used only to match nominally equal timestamps
# and to avoid roundoff misclassifying a ramp endpoint as a ramp interior.
TOL = 1e-9


def vector(x):
    return np.asarray(x).ravel()


def scalar(x):
    a = vector(x)
    if len(a) != 1:
        raise ValueError('Expected scalar')
    return float(a[0])


def inspect(path, root):
    data = load_from_mat(path)
    obj = data['A']
    if obj.classname != 'PhononData':
        raise ValueError(f'{path}: unexpected class {obj.classname}')
    p = obj.properties
    typ = str(vector(p['dataRingType'])[0])
    t, r, dr = (vector(p[k]) for k in ('EvTime', 'MeanRad_avg', 'MeanRad_dev'))
    if not (len(t) == len(r) == len(dr)):
        raise ValueError(f'{path}: decoded time/radius lengths differ')
    n1d = np.asarray(data['n1Ds'])
    runs, time, atom = (vector(data[k]) for k in ('Runs', 'time', 'AN'))
    if n1d.shape[1] != len(runs) or len(time) != len(runs) or len(atom) != len(runs):
        raise ValueError(f'{path}: raw per-column lengths differ')
    if not np.all(np.isfinite(t)) or not np.all(np.isfinite(r)):
        raise ValueError(f'{path}: nonfinite decoded radius or time')
    phonon = np.isin(runs, vector(p['RunNos_phnEv']))
    groups = [phonon & (np.abs(time - ti) <= TOL) for ti in t]
    counts = np.array([g.sum() for g in groups])
    if np.any(counts == 0) or int(counts.sum()) != int(phonon.sum()):
        raise ValueError(f'{path}: phonon samples do not partition into time slices')
    mean_atom = np.array([np.mean(atom[g]) for g in groups])
    err_atom = float(np.max(np.abs(mean_atom - vector(p['AN_phnEv_avg']))))
    # Independently reconstruct the author's scaled-reference subtraction
    # from raw 1D profiles and the decoded reference profiles. This tests
    # mapping and grouping, but is not an independent MATLAB verification.
    start, duration = scalar(p['t_phn1']), scalar(p['t_exp'])
    target = np.asarray(p['n1D_phnEv_avg'])
    exp_times = vector(p['n1D_ringExpTimes'])
    maxerr = 0.0
    checked = excluded = 0
    for j, ti in enumerate(t):
        # Endpoint treatment in the author's float comparisons is subtle;
        # skip near-boundary slices rather than assign a possibly wrong ref.
        if abs(ti - start) <= TOL or abs(ti - start - duration) <= TOL:
            excluded += 1
            continue
        raw_mean = np.mean(n1d[:, groups[j]], axis=1)
        if ti < start:
            ref = vector(p['n1D_ringI_avg'])
        elif ti > start + duration:
            ref = vector(p['n1D_ringF_avg'])
        else:
            match = np.flatnonzero(np.abs(exp_times - ti) <= TOL)
            if len(match) != 1:
                raise ValueError(f'{path}: expected one ramp reference at {ti}')
            ref = np.asarray(p['n1D_ringExp_avg'])[:, match[0]]
        predicted = raw_mean - ref * (raw_mean.sum() / ref.sum())
        maxerr = max(maxerr, float(np.max(np.abs(predicted - target[:, j]))))
        checked += 1
    if err_atom > 1e-8 or maxerr > 1e-7:
        raise ValueError(f'{path}: independent numeric reconstruction failed')
    interior = (t > start + TOL) & (t < start + duration - TOL)
    # The paper quotes 3.6 ms as the 10-90% rise time for this 10 ms
    # error-function protocol, whose center is start + duration/2.
    core = np.abs(t - (start + duration / 2)) < 0.0018 - TOL
    ramp_rows = [
        {'offset_ms': float((t[i] - start) * 1000),
         'radius_um': float(r[i]), 'radius_dev_um': float(dr[i]),
         'phonon_preparations': int(counts[i]), 'in_3_6ms_center_window': bool(core[i])}
        for i in np.flatnonzero(interior)
    ]
    fi = vector(p['fi'])
    return {
        'path': str(path.relative_to(root)),
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'ring_type': typ,
        'start_ms': start * 1000,
        'programmed_duration_ms': duration * 1000,
        'time_slices': len(t),
        'phonon_preparations_per_slice': sorted(set(int(c) for c in counts)),
        'max_atom_number_mean_error': err_atom,
        'max_normalized_profile_error': maxerr,
        'profile_slices_checked': checked,
        'profile_endpoint_slices_excluded': excluded,
        'static_mean_radius_um': float(np.mean(r)) if typ == 'Initial' else None,
        'static_fitted_frequency_hz': float(fi[0]) if typ == 'Initial' and len(fi) == 1 else None,
        'interior_ramp_samples': ramp_rows if typ == 'All' else [],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_root', type=Path)
    args = parser.parse_args()
    root = args.source_root.resolve()
    files = [p for branch in ('expansions', 'contractions')
             for p in sorted((root / 'data' / branch).glob('PhnRuns_*.mat'))]
    if not files:
        raise SystemExit('No source MAT files found')
    records = [inspect(p, root) for p in files]
    summary = {}
    for branch in ('expansions', 'contractions'):
        sub = [x for x in records if x['path'].startswith(f'data/{branch}/')]
        dynamic = [x for x in sub if x['ring_type'] == 'All']
        statics = [x for x in sub if x['ring_type'] == 'Initial']
        if not dynamic or not statics:
            raise ValueError(f'{branch}: missing expected static or dynamic records')
        samples = [s for d in dynamic for s in d['interior_ramp_samples']]
        core = [s for s in samples if s['in_3_6ms_center_window']]
        summary[branch] = {
            'dynamic_protocols': len(dynamic),
            'static_files_in_directory': len(statics),
            'interior_samples_per_protocol': sorted(set(len(d['interior_ramp_samples']) for d in dynamic)),
            'core_samples_per_protocol': sorted(set(sum(s['in_3_6ms_center_window'] for s in d['interior_ramp_samples']) for d in dynamic)),
            'interior_samples_with_mean_radius_20_to_30_um_inclusive': sum(20 <= s['radius_um'] <= 30 for s in samples),
            'core_radius_um_min': min(s['radius_um'] for s in core),
            'core_radius_um_max': max(s['radius_um'] for s in core),
            'nearest_mean_radius_below_25_um': max(s['radius_um'] for s in samples if s['radius_um'] < 25),
            'nearest_mean_radius_above_25_um': min(s['radius_um'] for s in samples if s['radius_um'] > 25),
        }
    print(json.dumps({
        'source': 'https://github.com/JQIamo/hubFrct_2021',
        'expected_source_commit': '88c8a87aed5961f589db66a7e7e4e97f161ad51c',
        'note': 'Source commit is not verified here. Verify per-file hashes against the pinned inventory. Mean-radius gaps do not include systematic uncertainties.',
        'timestamp_tolerance_seconds': TOL,
        'max_atom_number_mean_error': max(r['max_atom_number_mean_error'] for r in records),
        'max_normalized_profile_error': max(r['max_normalized_profile_error'] for r in records),
        'profile_slices_checked': sum(r['profile_slices_checked'] for r in records),
        'profile_endpoint_slices_excluded': sum(r['profile_endpoint_slices_excluded'] for r in records),
        'summary': summary,
        'records': records,
    }, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
