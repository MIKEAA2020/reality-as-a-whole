#!/usr/bin/env python3
"""Exploratory report-state coverage; no EEG decoder or condition inference.

Run with numpy==2.2.6 and scipy==1.15.3:
  python verification/roy_s09_report_coverage.py /path/S09_scan7_filtered_gac_cbc.mat ...
The raw files may contain sensitive DICOM data. Only selected variables are
loaded; stdout contains aggregate, scan-level counts and file SHA-256 hashes.
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


def analyze(path):
    keys = ['sampling_freq', 'latency_s1', 'latency_s2', 'latency_s3',
            'latency_trial', 'bad_epoch']
    d = loadmat(path, squeeze_me=True, struct_as_record=False, variable_names=keys)
    fs = int(d['sampling_freq'])
    if fs != 250:
        raise ValueError('Unexpected sampling rate; stop rather than infer')
    mask = np.atleast_1d(d['bad_epoch']).astype(bool)
    starts = np.atleast_1d(d['latency_trial']).astype(int) - 1  # MATLAB -> Python
    if len(starts) != 5 or np.any(np.diff(starts) < 42 * fs):
        raise ValueError('Expected five nonoverlapping 42 s windows; stop')
    events = []
    for k in (1, 2, 3):
        raw = np.atleast_1d(d['latency_s' + str(k)]).astype(int)
        events.extend((int(i)-1, k) for i in raw)
    events.sort()
    if len({t for t, _ in events}) != len(events):
        raise ValueError('Two report events share a sample; ordering ambiguous')

    all_counts = np.zeros(4, dtype=int)
    clean_counts = np.zeros(4, dtype=int)
    transition_counts = {'1_to_1': 0, '1_to_2': 0, '2_to_1': 0, '2_to_2': 0}
    for start in starts:
        stop = int(start) + 42 * fs
        if start < 0 or stop > len(mask):
            raise ValueError('Trial extends beyond the mask; stop')
        local = [(t, k) for t, k in events if start <= t < stop]
        state = np.zeros(stop-start, dtype=np.uint8)
        for idx, (t, k) in enumerate(local):
            end = local[idx+1][0] if idx+1 < len(local) else stop
            state[t-start:end-start] = k
        for k in range(4):
            all_counts[k] += int(np.sum(state == k))
            clean_counts[k] += int(np.sum((state == k) & ~mask[start:stop]))
        for idx in range(1, len(local)-1):
            prev, cur, nxt = local[idx-1][1], local[idx][1], local[idx+1][1]
            if cur == 3 and prev in (1, 2) and nxt in (1, 2):
                transition_counts[f'{prev}_to_{nxt}'] += 1

    def summary(counts):
        total = int(np.sum(counts))
        if total == 0:
            raise ValueError('No eligible samples')
        return {'samples': total,
                'seconds_by_label': {key: float(counts[i]/fs) for i, key in
                    enumerate(('unknown_before_first_event', 'code_1', 'code_2', 'code_3_mixed'))},
                'unknown_or_mixed_fraction': float((counts[0]+counts[3])/total),
                'pure_fraction': float((counts[1]+counts[2])/total)}
    total = int(np.sum(all_counts))
    # If Y is unresolved on every bad_epoch sample, the union of unresolved
    # R and bad_epoch is all samples except clean code-1/code-2 samples.
    conditional_bound = 1.0 - float(clean_counts[1] + clean_counts[2]) / total
    return {'file': path.name, 'sha256': sha256(path), 'sampling_hz': fs,
            'assumed_trial_duration_seconds': 42, 'trial_count': len(starts),
            'all_trial_samples': summary(all_counts), 'outside_bad_epoch': summary(clean_counts),
            'fraction_bad_epoch_or_unresolved_report': conditional_bound,
            'adjacent_pure_mixed_pure_event_patterns': transition_counts}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mat_files', nargs='+', type=Path)
    args = parser.parse_args()
    output = {'kind': 'exploratory one-person coverage; not decoder accuracy',
        'definitions': ['Sampled at 250 Hz; each trial begins at latency_trial and lasts 42 seconds.',
            'Before first event is unknown; each subsequent code is carried to the next event or trial end.',
            'Code 3 is mixed according to the release documentation; no experiential truth is inferred.',
            'Fraction unknown-or-mixed is a lower bound on binary full-coverage disagreement when unresolved reports are counted as disagreements.',
            'Bad-epoch-excluded coverage has a different denominator and is a sensitivity analysis.',
            'The bad-epoch-or-unresolved union bounds disagreement only if the decoder abstains on every bad_epoch sample.',
            'Trial condition, exact stimulus timing and the report-state reconstruction have not been independently validated.'],
        'scans': [analyze(path) for path in args.mat_files]}
    print(json.dumps(output, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
