#!/usr/bin/env python3
"""Synthetic regression for timing screen including uint16 trial starts."""
from pathlib import Path
import tempfile

import numpy as np
from scipy.io import savemat
from roy_s09_event_similarity_screen import screen


def main():
    starts=np.array([3000, 16500, 30000, 43500, 57000],dtype=np.uint16)
    seconds=starts.astype(np.int64)
    data={'sampling_freq':250, 'latency_trial':starts,
          'latency_s1':seconds+250, 'latency_s2':seconds+750,
          'latency_s3':seconds+500}
    with tempfile.TemporaryDirectory() as td:
        a,b=Path(td)/'a.mat',Path(td)/'b.mat'
        savemat(a,data)
        savemat(b,{**data,'latency_s1':data['latency_s2'],'latency_s2':data['latency_s1']})
        result=screen([a,b])
        assert result['between_scan_trial_pairs']==25
        assert result['equal_nonzero_count_pairs']==25
        assert result['equal_count_pairs_all_times_within_200ms']==25
        assert all(x['event_count']==3 and x['swap_code_pairs']==3 for x in result['equal_count_pair_summaries'])
    print('PASS: trial-boundary arithmetic, pair counts, timing and label swap')


if __name__=='__main__':
    main()
