#!/usr/bin/env python3
"""Synthetic control for the exploratory timing comparison; no human data."""
from pathlib import Path
import tempfile

import numpy as np
from scipy.io import savemat
from roy_s09_repeated_report_pattern import compare


def main():
    fs = 250
    with tempfile.TemporaryDirectory() as temp:
        a, b = Path(temp)/'a.mat', Path(temp)/'b.mat'
        d = {'sampling_freq': fs, 'latency_trial': np.array([1]),
             'latency_s1': np.array([251]), 'latency_s2': np.array([751]),
             'latency_s3': np.array([501])}
        savemat(a, d)
        savemat(b, {**d, 'latency_s1': d['latency_s2'], 'latency_s2': d['latency_s1']})
        x = compare(a, b, 1)
        assert x['ordinal_event_pairs'] == 3 and x['matching_after_1_2_swap'] == 3
        assert x['both_pure_seconds'] == 40 and x['match_on_both_pure_after_swap'] == 1
        assert x['match_on_both_pure_same_codes'] == 0
        assert abs(x['agreement_after_swap_full_trial_counting_any_nonpure_as_disagreement']-40/42)<1e-12
        savemat(b, {**d, 'latency_s3': np.array([], dtype=int)})
        try:
            compare(a, b, 1)
        except ValueError as e:
            assert 'Event counts differ' in str(e)
        else:
            raise AssertionError('Unequal event counts must stop ordinal pairing')
    print('PASS: label swap, full denominator, and unequal-event stop')


if __name__ == '__main__':
    main()
