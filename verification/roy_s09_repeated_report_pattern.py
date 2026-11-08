#!/usr/bin/env python3
"""Post-hoc comparison of one report-timing pattern in two S09 scans.

This reads only report-event arrays and trial markers, not raw EEG or DICOM.
It is NOT an out-of-sample decoder test: the run, trial and label swap were
noticed from these same data. Only aggregate event/coverage statistics are
written to stdout. Uses numpy==2.2.6 and scipy==1.15.3.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def trial(path, index):
    keys = ['sampling_freq', 'latency_trial', 'latency_s1', 'latency_s2', 'latency_s3']
    d = loadmat(path, squeeze_me=True, struct_as_record=False, variable_names=keys)
    fs = int(d['sampling_freq'])
    if fs != 250:
        raise ValueError('Unexpected sampling rate')
    starts = np.atleast_1d(d['latency_trial']).astype(int)
    if index < 1 or index > len(starts):
        raise ValueError('Invalid 1-based trial index')
    start = int(starts[index-1])
    stop = start + 42 * fs
    events = sorted((int(t)-start, k) for k in (1, 2, 3)
        for t in np.atleast_1d(d['latency_s'+str(k)]) if start <= int(t) < stop)
    if len({t for t, _ in events}) != len(events):
        raise ValueError('Duplicate report-event times')
    labels = np.zeros(42*fs, dtype=np.uint8)
    for i, (offset, code) in enumerate(events):
        end = events[i+1][0] if i+1 < len(events) else 42*fs
        labels[offset:end] = code
    return events, labels


def compare(path_a, path_b, trial_index):
    ea, a = trial(path_a, trial_index)
    eb, b = trial(path_b, trial_index)
    if len(ea) != len(eb) or not ea:
        raise ValueError('Event counts differ; ordinal pairing is not defined')
    ac = np.array([e[1] for e in ea], dtype=int)
    bc = np.array([e[1] for e in eb], dtype=int)
    swapped_codes = np.where(ac == 1, 2, np.where(ac == 2, 1, ac))
    offsets_s = np.array([x[0] - y[0] for x, y in zip(ea, eb)])/250.0
    swapped = np.where(a == 1, 2, np.where(a == 2, 1, a))
    both_pure = (a >= 1) & (a <= 2) & (b >= 1) & (b <= 2)
    n_pure = int(both_pure.sum())
    if n_pure == 0:
        raise ValueError('No shared pure-report time')
    match_swapped = int(np.sum((swapped == b) & both_pure))
    match_same = int(np.sum((a == b) & both_pure))
    return {'kind': 'post-hoc same-participant trial comparison, not decoder validation',
        'scan_a': path_a.name, 'sha256_a': sha256(path_a),
        'scan_b': path_b.name, 'sha256_b': sha256(path_b),
        'trial_index_1_based': trial_index, 'sampling_hz': 250,
        'assumed_trial_duration_s': 42, 'ordinal_event_pairs': len(ea),
        'identical_codes': int(np.sum(ac == bc)),
        'matching_after_1_2_swap': int(np.sum(swapped_codes == bc)),
        'offset_a_minus_b_s': {'median': float(np.median(offsets_s)),
            'min': float(np.min(offsets_s)), 'max': float(np.max(offsets_s)),
            'rms': float(np.sqrt(np.mean(offsets_s**2)))},
        'both_pure_seconds': n_pure/250.0,
        'match_on_both_pure_same_codes': match_same/n_pure,
        'match_on_both_pure_after_swap': match_swapped/n_pure,
        'agreement_after_swap_full_trial_counting_any_nonpure_as_disagreement': match_swapped/len(a),
        'nonpure_either_fraction': float(np.sum(~both_pure)/len(a)),
        'limitations': ['Pair and mapping selected after inspecting the data; no confirmatory score or p value.',
            'Report time series are compared, not EEG; condition and cause of similarity are unverified.',
            'Sampled 42-second trial windows and event carry-forward are assumptions.',
            'Both-pure agreement excludes unknown and mixed intervals; it is not all-time performance.']}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('scan_a', type=Path)
    p.add_argument('scan_b', type=Path)
    p.add_argument('--trial', type=int, default=4)
    args = p.parse_args()
    print(json.dumps(compare(args.scan_a, args.scan_b, args.trial), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
