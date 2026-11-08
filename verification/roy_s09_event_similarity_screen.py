#!/usr/bin/env python3
"""Post-hoc screen of equal-count report patterns across supplied scans.
No participant event sequences are output. The 200 ms threshold was chosen
because of a previously observed comparison and is not a statistical test.
Requires numpy==2.2.6 and scipy==1.15.3.
"""
import argparse
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat
from roy_s09_descriptive_tag_report import sha256


def scan(path):
    d = loadmat(path, squeeze_me=True, struct_as_record=False,
        variable_names=['sampling_freq', 'latency_trial', 'latency_s1', 'latency_s2', 'latency_s3'])
    fs = int(d['sampling_freq'])
    if fs != 250:
        raise ValueError('Unexpected sampling rate')
    starts = np.atleast_1d(d['latency_trial']).astype(int)
    if len(starts) != 5 or np.any(np.diff(starts) < 42*fs):
        raise ValueError('Expected five nonoverlapping trials')
    events = sorted((int(t), k) for k in (1, 2, 3)
                    for t in np.atleast_1d(d['latency_s'+str(k)]))
    if len({t for t, _ in events}) != len(events):
        raise ValueError('Duplicate event samples')
    trials=[]
    for start in starts:
        start=int(start)  # Prevent overflow from MATLAB uint16 storage.
        trials.append([(t-start, k) for t,k in events if start <= t < start+42*fs])
    return trials


def screen(paths):
    scans = [(p,scan(p)) for p in paths]
    pairs = 0
    candidates = []
    for (pa, ta), (pb, tb) in itertools.combinations(scans,2):
        for ia, a in enumerate(ta,1):
            for ib, b in enumerate(tb,1):
                pairs += 1
                if not a or len(a) != len(b):
                    continue
                diffs = np.array([x[0]-y[0] for x,y in zip(a,b)], dtype=float)/250
                ca = np.array([x[1] for x in a])
                cb = np.array([y[1] for y in b])
                swap = np.where(ca == 1, 2, np.where(ca == 2, 1, ca))
                max_seconds=float(np.max(np.abs(diffs)))
                candidates.append({'scan_a':pa.name, 'trial_a':ia, 'scan_b':pb.name, 'trial_b':ib,
                    'event_count':len(a), 'max_ordinal_abs_difference_s':max_seconds,
                    'same_code_pairs':int(np.sum(ca==cb)), 'swap_code_pairs':int(np.sum(swap==cb)),
                    'all_times_within_200ms':bool(np.all(np.abs(diffs)<=0.2))})
    return {'kind':'post-hoc timing screen; not a significance test',
        'files':[{'name':p.name,'sha256':sha256(p)} for p in paths],
        'between_scan_trial_pairs':pairs, 'equal_nonzero_count_pairs':len(candidates),
        'equal_count_pairs_all_times_within_200ms':sum(c['all_times_within_200ms'] for c in candidates),
        'equal_count_pair_summaries':candidates,
        'limitations':['Timing threshold was motivated by earlier data-selected match.',
            'Unequal-count sequences and non-ordinal alignments are not evaluated.',
            'No inference that conditions or replay lineage are different.']}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('mat_files', nargs='+', type=Path)
    args=p.parse_args()
    print(json.dumps(screen(args.mat_files),indent=2,allow_nan=False))


if __name__=='__main__':
    main()
