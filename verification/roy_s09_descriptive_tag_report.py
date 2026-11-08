#!/usr/bin/env python3
"""Exploratory 2-second POz tag-power/report summaries; not a decoder.

Uses preselected two-second trial-grid windows that are entirely pure code 1
or 2, with no bad_epoch sample. Projects EEG at the exact two frequency tags;
no training or test-set mapping is performed. No task condition inferred.
Requires numpy==2.2.6 and scipy==1.15.3. Only aggregates, no EEG, DICOM fields
or event sequences, are written. Inspect the source and report limitations.
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
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def analyze(path):
    fields = ['EEG', 'sampling_freq', 'freqtag1', 'freqtag2', 'chanlabels',
              'latency_s1', 'latency_s2', 'latency_s3', 'latency_trial', 'bad_epoch']
    d = loadmat(path, squeeze_me=True, struct_as_record=False, variable_names=fields)
    fs = int(d['sampling_freq'])
    if fs != 250 or int(d['EEG'].srate) != fs:
        raise ValueError('Inconsistent sampling; stop')
    labels = [str(x) for x in np.atleast_1d(d['chanlabels'])]
    if labels.count('POz') != 1:
        raise ValueError('POz missing or ambiguous; stop')
    data = np.asarray(d['EEG'].data)
    mask = np.atleast_1d(d['bad_epoch']).astype(bool)
    if data.ndim != 2 or data.shape != (len(labels), len(mask)):
        raise ValueError('Unexpected EEG or mask shape; stop')
    signal = data[labels.index('POz')]
    starts = np.atleast_1d(d['latency_trial']).astype(int) - 1
    if len(starts) != 5 or np.any(np.diff(starts) < 42*fs):
        raise ValueError('Expected five nonoverlapping 42-second trials; stop')
    events = sorted((int(t)-1, k) for k in (1, 2, 3)
                    for t in np.atleast_1d(d['latency_s'+str(k)]))
    if len({t for t, _ in events}) != len(events):
        raise ValueError('Ambiguous duplicate event sample; stop')
    low, high = sorted((float(d['freqtag1']), float(d['freqtag2'])))
    n = 2 * fs
    times = np.arange(n)/fs
    window = np.hanning(n)
    carrier_low = np.exp(-2j*np.pi*low*times)
    carrier_high = np.exp(-2j*np.pi*high*times)
    per_trial = []
    for start in starts:
        end = int(start)+42*fs
        if start < 0 or end > len(mask):
            raise ValueError('Trial exceeds scan; stop')
        local = [(t, k) for t, k in events if start <= t < end]
        state = np.zeros(42*fs, dtype=np.uint8)
        for i, (t, k) in enumerate(local):
            right = local[i+1][0] if i+1 < len(local) else end
            state[t-start:right-start] = k
        groups = {1: [], 2: []}
        rejects = 0
        for offset in range(0, 42*fs, n):
            group = state[offset:offset+n]
            lo = int(start)+offset
            hi = lo+n
            if group[0] not in (1, 2) or np.any(group != group[0]) or np.any(mask[lo:hi]):
                rejects += 1
                continue
            x = signal[lo:hi].astype(float)
            if not np.all(np.isfinite(x)):
                raise ValueError('Nonfinite EEG; stop')
            x = (x-x.mean())*window
            p_lo = float(abs(x @ carrier_low)**2)
            p_hi = float(abs(x @ carrier_high)**2)
            if p_lo <= 0 or p_hi <= 0:
                raise ValueError('Nonpositive tag power; stop')
            groups[int(group[0])].append(float(np.log10(p_lo/p_hi)))
        med1 = float(np.median(groups[1])) if groups[1] else None
        med2 = float(np.median(groups[2])) if groups[2] else None
        per_trial.append({'code_1_windows': len(groups[1]), 'code_2_windows': len(groups[2]),
            'rejected_windows': rejects, 'code_1_median_log10_ratio': med1,
            'code_2_median_log10_ratio': med2,
            'within_trial_median_difference_1_minus_2': med1-med2 if med1 is not None and med2 is not None else None})
    paired = [t['within_trial_median_difference_1_minus_2'] for t in per_trial
              if t['within_trial_median_difference_1_minus_2'] is not None]
    return {'file': path.name, 'sha256': sha256(path), 'electrode': 'POz',
        'low_tag_hz': low, 'high_tag_hz': high, 'per_trial': per_trial,
        'paired_trials': len(paired), 'mean_of_trial_median_differences': float(np.mean(paired)) if paired else None,
        'median_of_trial_median_differences': float(np.median(paired)) if paired else None,
        'code_1_windows_total': sum(t['code_1_windows'] for t in per_trial),
        'code_2_windows_total': sum(t['code_2_windows'] for t in per_trial)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('mat_files', type=Path, nargs='+')
    a = p.parse_args()
    print(json.dumps({'kind': 'post-hoc descriptive association, not decoder accuracy or experience measurement',
        'definition': 'log10(projected power at lower tag / projected power at higher tag)',
        'window': '2 s, nonoverlap, anchored to each assumed 42 s trial trigger; mean removal and symmetric Hann',
        'eligibility': 'all samples same pure report code 1 or 2 and no bad_epoch sample',
        'warnings': ['Observed after inspecting data; task condition and exact physical timing unverified.',
            'Time windows within a trial and trials within one participant are not independent subjects.',
            'Simple POz projection is not the optimized RLS method of Roy and Jamison.',
            'No task-labeled decoder, generalization, significance test, or phenomenal error bound.'],
        'scans': [analyze(path) for path in a.mat_files]}, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
