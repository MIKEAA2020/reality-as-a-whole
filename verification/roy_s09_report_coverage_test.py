#!/usr/bin/env python3
"""Synthetic regression for report reconstruction; no participant data."""
from pathlib import Path
import tempfile

import numpy as np
from scipy.io import savemat
from roy_s09_report_coverage import analyze


def main():
    fs = 250
    starts0 = np.array([i * 50 * fs for i in range(5)])
    mask = np.zeros(starts0[-1] + 50 * fs, dtype=bool)
    for start in starts0:
        mask[start + 5*fs:start + 6*fs] = True  # pure, adds to union
        mask[start + 15*fs:start + 16*fs] = True  # mixed, already unresolved
    fixture = {'sampling_freq': fs, 'latency_trial': starts0 + 1,
        'latency_s1': starts0 + 2*fs + 1, 'latency_s3': starts0 + 12*fs + 1,
        'latency_s2': starts0 + 22*fs + 1, 'bad_epoch': mask}
    with tempfile.TemporaryDirectory() as temp:
        p = Path(temp) / 'synthetic.mat'
        savemat(p, fixture)
        s = analyze(p)
        seconds = s['all_trial_samples']['seconds_by_label']
        assert seconds == {'unknown_before_first_event': 10.0, 'code_1': 50.0,
                           'code_2': 100.0, 'code_3_mixed': 50.0}
        assert s['all_trial_samples']['samples'] == 5*42*fs
        assert abs(s['all_trial_samples']['unknown_or_mixed_fraction'] - 12/42) < 1e-12
        assert abs(s['fraction_bad_epoch_or_unresolved_report'] - 13/42) < 1e-12
        assert s['adjacent_pure_mixed_pure_event_patterns']['1_to_2'] == 5
        fixture['latency_s2'] = fixture['latency_s3']  # ambiguous event ordering
        savemat(p, fixture)
        try:
            analyze(p)
        except ValueError as e:
            assert 'share a sample' in str(e)
        else:
            raise AssertionError('Duplicate report events must stop analysis')
    print('PASS: synthetic interval reconstruction, union bound, and duplicate-event stop')


if __name__ == '__main__':
    main()
