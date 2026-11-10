#!/usr/bin/env python3
"""Illustrative scan-1 global-signal sensitivity across all 18 candidate offsets.

This is not Roy's event-related GLM, a replication, a neural correlate test,
or a method for choosing the real alignment. It uses an illustrative fixed
42-second boxcar and double-gamma HRF, no drift/motion/confound adjustment and
no inference. Only series-wide aggregate means, five trial markers and safe
numeric EEG metadata are accessed. Requires numpy==2.2.6, scipy==1.15.3.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat
from scipy.special import gammainc


def block_regressor(sample_times, onsets, duration=42.0):
    def cumulative(x):
        z = np.maximum(x, 0.0)
        return gammainc(6, z) - gammainc(16, z)/6
    return sum(cumulative(sample_times-onset)-cumulative(sample_times-onset-duration)
               for onset in onsets)


def correlation(x, y):
    x = np.asarray(x, dtype=float) - np.mean(x)
    y = np.asarray(y, dtype=float) - np.mean(y)
    den = float(np.linalg.norm(x)*np.linalg.norm(y))
    if den == 0 or not np.isfinite(den):
        raise ValueError('Correlation is undefined')
    return float(np.dot(x, y)/den)


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()


def analyze(inventory_path, alignment_path, eeg_path):
    inv=json.loads(inventory_path.read_text())
    gate=json.loads(alignment_path.read_text())
    if sha(eeg_path)!=gate['eeg_sha256']:
        raise ValueError('EEG source hash differs from alignment witness')
    if len(inv['volumes'])!=gate['mri_volumes']:
        raise ValueError('MRI inventory count differs from alignment witness')
    means=np.array([x['mean_scaled'] for x in inv['volumes']],dtype=float)
    if not np.isfinite(means).all():
        raise ValueError('Nonfinite global mean')
    d=loadmat(eeg_path,squeeze_me=True,struct_as_record=False,
              variable_names=['latency_tr','latency_trial','sampling_freq'])
    first=float(np.atleast_1d(d['latency_tr'])[0])
    onsets=(np.atleast_1d(d['latency_trial']).astype(float)-first)/float(d['sampling_freq'])
    if len(onsets)!=5:
        raise ValueError('Expected five trial markers')
    tr=float(gate['trigger_spacing_s'])
    sample_times=np.arange(len(means))*tr
    rows=[]
    for k in gate['candidate_first_fmri_frames']:
        regressor=block_regressor(sample_times,onsets+(int(k)-1)*tr)
        rows.append({'first_trigger_frame':int(k), 'pearson_r':correlation(means,regressor)})
    values=[row['pearson_r'] for row in rows]
    return {'kind':'observed data + hypothetical offset sensitivity, not inferential GLM',
        'eeg_sha256':gate['eeg_sha256'], 'mri_inventory_sha256':sha(inventory_path),
        'volumes':len(means), 'candidate_count':len(rows),
        'whole_field_mean_across_volumes':float(means.mean()),
        'whole_field_mean_sample_sd':float(means.std(ddof=1)),
        'pearson_r_range':[min(values),max(values)], 'all_candidates':rows,
        'assumptions':['Frame indices 1..141 are temporally ordered with 2.2 s spacing.',
            'All 124 EEG triggers align to a consecutive one-to-one subset of frames.',
            'Each trial trigger corresponds to onset of a 42 s block.',
            'Fixed double-gamma HRF: Gamma(6,1) minus Gamma(16,1)/6.',
            'Global mean includes all voxels, including zero-valued background.'],
        'limitations':['None of the 18 candidate offsets is established by these observations.',
            'No prewhitening, drift, motion, design collinearity or multiple-comparison control.',
            'Computed correlations are descriptive and do not test a rivalry, awareness or causal claim.',
            'Do not select the most favorable alignment based on these correlations.']}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('inventory',type=Path)
    p.add_argument('alignment',type=Path)
    p.add_argument('eeg',type=Path)
    a=p.parse_args()
    print(json.dumps(analyze(a.inventory,a.alignment,a.eeg),indent=2,allow_nan=False))


if __name__=='__main__':
    main()
