#!/usr/bin/env python3
"""Observed S09 scan-1 counts + conditional volume/trigger alignment witness.

Uses a completed non-identifying MRI inventory and the authorized EEG .mat.
Only selected variables and safe numeric DICOM fields are loaded/output.
This does not infer a true mapping; candidate mappings depend on stated
assumptions and can be ruled out by information not inspected here.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def sample_indices(values):
    """Accept numerical roundoff near sample indices, never silently truncate."""
    values = np.atleast_1d(np.asarray(values, dtype=float))
    if not np.isfinite(values).all() or np.any(np.abs(values - np.rint(values)) > 1e-7):
        raise ValueError('Latencies are not integer sample indices within numerical tolerance')
    return np.rint(values).astype(np.int64)


def candidate_starts(n_volumes, n_triggers):
    if n_volumes < 1 or n_triggers < 1 or n_triggers > n_volumes:
        raise ValueError('Invalid lengths for consecutive one-to-one mapping')
    return list(range(1, n_volumes - n_triggers + 2))


def analyze(inventory_path, eeg_path):
    inventory = json.loads(inventory_path.read_text())
    nvol = int(inventory['volumes_read'])
    indices = [int(v['frame']) for v in inventory['volumes']]
    if indices != list(range(1, nvol+1)):
        raise ValueError('This witness requires exactly frames 1..N in order')
    d = loadmat(eeg_path, squeeze_me=True, struct_as_record=False,
        variable_names=['EEG', 'sampling_freq', 'dcminfo', 'latency_tr', 'latency_trial'])
    fs = float(d['sampling_freq'])
    eeg = d['EEG']
    if fs != float(eeg.srate) or fs <= 0:
        raise ValueError('Inconsistent sampling rates')
    tr = sample_indices(d['latency_tr'])
    trials = sample_indices(d['latency_trial'])
    if len(tr) < 2 or len(trials) < 1 or np.any(np.diff(tr) <= 0):
        raise ValueError('Missing or non-monotonic triggers')
    observed_diffs = np.diff(tr)/fs
    if not np.allclose(observed_diffs, observed_diffs[0], atol=1e-12, rtol=0):
        raise ValueError('Irregular EEG trigger spacing; this witness does not apply')
    tr_seconds = float(observed_diffs[0])
    meta_tr = float(d['dcminfo'].RepetitionTime)/1000
    if abs(meta_tr-tr_seconds) > 1e-9:
        raise ValueError('EEG trigger spacing and embedded TR disagree')
    starts = candidate_starts(nvol, len(tr))
    delay_first_trial = float((trials[0]-tr[0])/fs)
    trial_time_options = [(k-1)*tr_seconds+delay_first_trial for k in starts]
    series_eeg = int(d['dcminfo'].SeriesNumber)
    if series_eeg != int(inventory['series_number']):
        raise ValueError('MRI series numbers differ')
    return {'kind': 'conditional alignment nonuniqueness witness, not an fMRI GLM',
        'eeg_sha256': sha256(eeg_path), 'mri_volumes': nvol,
        'mri_first_last_frames': [indices[0], indices[-1]], 'mri_series': int(inventory['series_number']),
        'eeg_embedded_series': series_eeg, 'sampling_hz': fs, 'eeg_samples': int(eeg.pnts),
        'eeg_sample_span_s': float((eeg.pnts-1)/fs), 'eeg_trigger_count': len(tr),
        'eeg_first_trigger_s':float((tr[0]-1)/fs), 'eeg_last_trigger_s':float((tr[-1]-1)/fs),
        'trigger_spacing_s':tr_seconds, 'first_trial_after_first_eeg_trigger_s':delay_first_trial,
        'candidate_first_fmri_frames': starts,
        'candidate_corresponding_first_trial_seconds_from_fmri_frame_1':trial_time_options,
        'assumptions': ['Frames 1..N are temporally ordered and equally spaced at the recorded TR.',
            'EEG trigger array represents a consecutive one-to-one subset of the fMRI frames.',
            'No independent absolute start-time or volume-to-trigger anchor is supplied.',
            'These assumptions and candidate offsets have not been verified against original acquisition or GLM records.'],
        'limitations': ['Series agreement is necessary consistency, not proof of correspondence.',
            'Unknown preprocessing drops and trial timing conventions may change the mapping.',
            'A fit selected from these offsets using the same outcomes would not be independent confirmation.']}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('inventory',type=Path)
    p.add_argument('eeg',type=Path)
    args=p.parse_args()
    print(json.dumps(analyze(args.inventory,args.eeg),indent=2,allow_nan=False))


if __name__=='__main__':
    main()
