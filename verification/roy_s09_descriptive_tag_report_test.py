#!/usr/bin/env python3
"""Synthetic signal and artifact-exclusion tests; no human data."""
import tempfile
from pathlib import Path

import numpy as np
from scipy.io import savemat
from roy_s09_descriptive_tag_report import analyze


def main():
    fs = 250
    starts = np.array([i*50*fs for i in range(5)])
    size = int(starts[-1] + 50*fs)
    t = np.arange(size)/fs
    eeg = np.sin(2*np.pi*(60/9)*t) + np.sin(2*np.pi*(60/7)*t)
    for start in starts:
        a = np.arange(start, start+20*fs)
        b = np.arange(start+20*fs, start+42*fs)
        eeg[a] = 4*np.sin(2*np.pi*(60/9)*t[a]) + np.sin(2*np.pi*(60/7)*t[a])
        eeg[b] = np.sin(2*np.pi*(60/9)*t[b]) + 4*np.sin(2*np.pi*(60/7)*t[b])
    mask = np.zeros(size, dtype=bool)
    mask[1] = True  # reject only first grid window
    data = {'EEG': {'srate': fs, 'data': np.array([eeg, eeg])}, 'chanlabels': np.array(['POz', 'Oz'], dtype=object),
            'sampling_freq': fs, 'freqtag1': 60/7, 'freqtag2': 60/9,
            'latency_trial': starts+1, 'latency_s1': starts+1,
            'latency_s2': starts+20*fs+1, 'latency_s3': np.array([], dtype=int), 'bad_epoch': mask}
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)/'synthetic.mat'
        savemat(p, data)
        result = analyze(p)
        assert result['code_1_windows_total'] == 49
        assert result['code_2_windows_total'] == 55
        assert result['paired_trials'] == 5
        assert result['mean_of_trial_median_differences'] > 2
        assert result['per_trial'][0]['rejected_windows'] == 1
    print('PASS: frequency ordering, synthetic power contrast and artifact-window rejection')


if __name__ == '__main__':
    main()
