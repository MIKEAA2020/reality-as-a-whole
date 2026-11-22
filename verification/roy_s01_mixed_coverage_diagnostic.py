#!/usr/bin/env python3
"""Post-test aggregate S01 report-code coverage diagnostic; no model tuning."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat
from roy_s09_scan1_alignment_gate import sample_indices
from roy_s01_frozen_three_state_transfer import RIVALRY, verify_sources


def summarize(states, bad, fs):
    """states and bad contain full 42-second trials; no raw series returned."""
    if len(states) != len(bad) or fs <= 0 or any(len(s) != 42*fs for s in states):
        raise ValueError('Invalid trial inputs')
    if any(len(m) != len(s) for s,m in zip(states,bad)):
        raise ValueError('Invalid mask length')
    samples = np.concatenate(states)
    windows = [s[i:i+2*fs] for s in states for i in range(0, len(s), 2*fs)]
    counts = np.array([np.count_nonzero(w == 3) for w in windows])
    return {'total_trial_samples': int(len(samples)),
            'time_by_report_code_seconds': {str(k): float(np.count_nonzero(samples==k)/fs) for k in (0,1,2,3)},
            'windows': len(windows), 'windows_with_any_mixed': int(np.count_nonzero(counts>0)),
            'windows_mixed_at_least_50pct': int(np.count_nonzero(2*counts>=2*fs)),
            'windows_mixed_at_least_75pct': int(np.count_nonzero(4*counts>=3*2*fs)),
            'max_mixed_fraction_of_any_window': float(max(counts, default=0)/(2*fs))}


def load_trials(path):
    d = loadmat(path,squeeze_me=True,struct_as_record=False,
                variable_names=['sampling_freq','latency_trial','latency_s1','latency_s2','latency_s3','bad_epoch'])
    fs = int(d['sampling_freq'])
    if fs != 250: raise ValueError('Unexpected sampling rate')
    starts = sample_indices(d['latency_trial']) - 1
    if len(starts) != 5 or np.any(np.diff(starts)<42*fs): raise ValueError('Invalid trial markers')
    mask = np.atleast_1d(d['bad_epoch'])
    if not np.all(np.isin(mask,(0,1))): raise ValueError('Invalid artifact code')
    events = sorted((int(t)-1,k) for k in (1,2,3) for t in sample_indices(d['latency_s'+str(k)]))
    if len({t for t,k in events}) != len(events): raise ValueError('Simultaneous events')
    states=[]; masks=[]; event_counts={str(k):0 for k in (1,2,3)}
    for start in starts:
        end=int(start)+42*fs
        if start<0 or end>len(mask): raise ValueError('Trial out of bounds')
        state=np.zeros(42*fs,dtype=np.uint8)
        local=[(t,k) for t,k in events if start<=t<end]
        for i,(t,k) in enumerate(local):
            right=local[i+1][0] if i+1<len(local) else end
            state[t-start:right-start]=k
            event_counts[str(k)] += 1
        states.append(state); masks.append(mask[start:end])
    return states,masks,fs,event_counts


def main():
    p=argparse.ArgumentParser(); p.add_argument('directory',type=Path); p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    verify_sources(args.directory)
    scans={}; all_states=[]; all_masks=[]
    for s in RIVALRY:
        states,masks,fs,events=load_trials(args.directory/f'S01_scan{s}_filtered_gac_cbc.mat')
        scans[str(s)]={'event_counts_within_trial':events, **summarize(states,masks,fs)}
        all_states.extend(states); all_masks.extend(masks)
    result={'scope':'Post-test descriptive report-code coverage, same provisional carry-forward reconstruction; no accuracy, experience, or tuning.',
            'per_scan':scans, 'pooled':summarize(all_states,all_masks,250)}
    text=json.dumps(result,indent=2,allow_nan=False)+'\n'; args.output.write_text(text); print(text,end='')


if __name__ == '__main__':main()
