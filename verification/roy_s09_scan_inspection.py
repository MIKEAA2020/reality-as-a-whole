#!/usr/bin/env python3
"""Inspect one released Roy EEG scan, without exporting embedded DICOM metadata.

Usage: PYTHONPATH=/path/to/deps python verification/roy_s09_scan_inspection.py /path/to/S09_scan8_filtered_gac_cbc.mat
Requires numpy==2.2.6 and scipy==1.15.3. JSON to stdout; no raw data are saved.
This is an exploratory scan QC, not a decoder, preregistered test or replication.
"""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np
from scipy import signal
from scipy.io import loadmat


def hashes(path):
    sha = hashlib.sha256()
    block_digests = []
    with path.open('rb') as stream:
        while block := stream.read(4 * 1024 * 1024):
            sha.update(block)
            block_digests.append(hashlib.sha256(block).digest())
    return sha.hexdigest(), hashlib.sha256(b''.join(block_digests)).hexdigest()


def inspect(path):
    sha, dbhash = hashes(path)
    keys = ['EEG', 'chanlabels', 'sampling_freq', 'freqtag1', 'freqtag2',
            'bad_epoch', 'bad_sample', 'ev_types', 'latency_s1', 'latency_s2',
            'latency_s3', 'latency_trial', 'latency_tr', 'trialResponse']
    d = loadmat(path, squeeze_me=True, struct_as_record=False, variable_names=keys)
    eeg = d['EEG']
    fs = int(d['sampling_freq'])
    data = eeg.data
    if data.shape != (int(eeg.nbchan), int(eeg.pnts)) or fs != int(eeg.srate):
        raise ValueError('EEG shape or sampling rates are inconsistent; stop')
    mask = np.asarray(d['bad_epoch'], dtype=bool)
    mask2 = np.asarray(d['bad_sample'], dtype=bool)
    if mask.shape != (data.shape[1],) or mask2.shape != mask.shape:
        raise ValueError('Bad-sample mask lengths are inconsistent; stop')
    onset = np.atleast_1d(d['latency_trial']).astype(int)
    # Round numerical noise only; truncation can manufacture a 551-sample gap.
    from roy_s09_scan1_alignment_gate import sample_indices
    trs = sample_indices(d['latency_tr'])
    responses = np.atleast_1d(d['trialResponse'])
    if len(onset) != len(responses):
        raise ValueError('Trial starts and trialResponse counts differ; stop')
    labels = [str(x) for x in np.atleast_1d(d['chanlabels'])]
    tags = [float(d['freqtag1']), float(d['freqtag2'])]

    # Compare each trial-relative response with the nearest event of the same
    # recorded code. The onset and event latencies share MATLAB's 1-based
    # convention; it cancels in their difference. Detect non-unique matches.
    deltas = [[] for _ in onset]
    matched = {str(k): [] for k in (1, 2, 3)}
    code_counts = Counter()
    for i, response in enumerate(responses):
        matrix = np.asarray(response.domResponse)
        if matrix.ndim != 2 or matrix.shape[1] != 2:
            raise ValueError('Unexpected response array layout; stop')
        for code, seconds in matrix:
            k = int(code)
            if k not in (1, 2, 3) or code != k:
                raise ValueError('Unexpected response code; stop')
            code_counts[str(k)] += 1
            events = np.atleast_1d(d['latency_s' + str(k)]).astype(float)
            target = onset[i] + float(seconds) * fs
            idx = int(np.argmin(np.abs(events - target)))
            deltas[i].append(float((events[idx] - target) / fs))
            matched[str(k)].append(idx)
    timing = []
    for delta in deltas:
        timing.append({'n': len(delta), 'median_s': float(np.median(delta)),
                       'min_s': float(np.min(delta)), 'max_s': float(np.max(delta))})
    match_info = {}
    for code in ('1', '2', '3'):
        event_count = len(np.atleast_1d(d['latency_s' + code]))
        unique_count = len(set(matched[code]))
        match_info[code] = {'responses': code_counts[code], 'event_latencies': event_count,
                            'unique_nearest_events': unique_count}

    # Preset diagnostic: 4-second Hann-window periodograms, starting at
    # 2, 6, ..., 38 seconds after each reported trial trigger (42 s duration).
    # Exclude entire windows containing bad_epoch samples. This is descriptive
    # and does not reproduce the published spatial optimization or RLS method.
    # Ratios compare nearest Fourier bin with a median of bins 0.5--1 Hz away.
    spectral = {}
    for label in ('Oz', 'POz'):
        if label not in labels:
            raise ValueError('Declared electrode missing: ' + label)
        psds = []
        for start in onset:
            for offset in range(2, 39, 4):
                lo = int(start) - 1 + fs * offset
                hi = lo + 4 * fs
                if lo < 0 or hi > data.shape[1] or np.any(mask[lo:hi]):
                    continue
                frequencies, power = signal.periodogram(data[labels.index(label), lo:hi],
                    fs=fs, window='hann', detrend='constant', nfft=4*fs)
                psds.append(power)
        if not psds:
            raise ValueError('No valid windows for ' + label)
        avg = np.mean(psds, axis=0)
        ratios = []
        for tag in tags:
            index = int(np.argmin(np.abs(frequencies - tag)))
            side = (np.abs(frequencies-tag) >= 0.5) & (np.abs(frequencies-tag) <= 1.0)
            baseline = float(np.median(avg[side]))
            if baseline <= 0:
                raise ValueError('Nonpositive sideband power; stop')
            ratios.append({'nominal_tag_hz': tag, 'nearest_bin_hz': float(frequencies[index]),
                           'power_to_sideband_median': float(avg[index]/baseline)})
        spectral[label] = {'clean_four_second_windows': len(psds), 'tag_ratios': ratios}

    return {
        'kind': 'exploratory single-scan inspection, not experience calibration',
        'file_name': path.name, 'size_bytes': path.stat().st_size,
        'sha256': sha, 'dropbox_content_hash': dbhash,
        'eeg': {'channels': int(eeg.nbchan), 'samples': int(eeg.pnts), 'sampling_hz': fs,
                'all_values_finite': bool(np.all(np.isfinite(data))),
                'sample_span_seconds': (int(eeg.pnts)-1)/fs,
                'tag_variables_hz': {'freqtag1': tags[0], 'freqtag2': tags[1]}},
        'events': {'types': dict(sorted(Counter(str(x) for x in np.atleast_1d(d['ev_types'])).items())),
                   'tr_count': len(trs), 'tr_spacing_samples_unique': np.unique(np.diff(trs)).tolist(),
                   'trial_count': len(onset), 'trial_start_samples_matlab_1_based': onset.tolist(),
                   'response_alignment_by_trial': timing, 'response_code_event_matches': match_info},
        'artifact_masks': {'bad_epoch_samples': int(np.sum(mask)), 'bad_sample_samples': int(np.sum(mask2)),
                           'either_samples': int(np.sum(mask|mask2))},
        'descriptive_spectrum': spectral,
        'limitations': ['Condition not independently verified; no color mapping inferred from freqtag1/2 order.',
            'Nearest-event offsets may reflect timing conventions or different clocks; not automatically corrected.',
            'Spectral ratios are exploratory, sensitive to window, artifacts and sidebands, not calibrated thresholds.',
            'Original file may include sensitive DICOM metadata; none reproduced in this summary.']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mat_file', type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.mat_file), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
