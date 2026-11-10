#!/usr/bin/env python3
"""S09 single-person, fit-held-out EEG/report feasibility; see analysis plan.

No latent experience labels, causal conclusions or raw EEG/events are output.
Requires numpy/scipy. Only selected variables are loaded from authorized MATs.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np
from scipy.io import loadmat
from roy_s09_scan1_alignment_gate import sample_indices

TRAIN=(1,2,3)
TEST=(5,7,4,6,8,9)


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def feature(signal, fs, low, high):
    x=np.asarray(signal,dtype=float)
    if x.shape!=(2*fs,) or not np.isfinite(x).all() or not 0 < low < high < fs/2:
        raise ValueError('Invalid signal or frequency')
    x=(x-x.mean())*np.hanning(len(x));t=np.arange(len(x))/fs
    pl=float(abs(x @ np.exp(-2j*np.pi*low*t))**2)
    ph=float(abs(x @ np.exp(-2j*np.pi*high*t))**2)
    if pl<=0 or ph<=0 or not np.isfinite(pl+ph):
        raise ValueError('Undefined tag ratio')
    return float(np.log10(pl/ph))


def read_windows(path, expected_sha):
    observed=sha(path)
    if observed!=expected_sha:raise ValueError('Source EEG hash mismatch')
    fields=['EEG','sampling_freq','freqtag1','freqtag2','chanlabels','latency_s1',
            'latency_s2','latency_s3','latency_trial','bad_epoch']
    d=loadmat(path,squeeze_me=True,struct_as_record=False,variable_names=fields)
    fs=int(d['sampling_freq']); eeg=d['EEG'];labels=[str(x) for x in np.atleast_1d(d['chanlabels'])]
    if fs!=250 or float(eeg.srate)!=fs or labels.count('POz')!=1:
        raise ValueError('Unexpected sample rate or channel')
    x=np.asarray(eeg.data);bad=np.atleast_1d(d['bad_epoch']).astype(bool)
    if x.ndim!=2 or x.shape!=(len(labels),len(bad)):
        raise ValueError('Unexpected EEG/mask dimensions')
    signal=x[labels.index('POz')]
    starts=sample_indices(d['latency_trial'])-1
    if len(starts)!=5 or np.any(np.diff(starts)<42*fs):raise ValueError('Invalid trial markers')
    events=sorted((int(t)-1,k) for k in (1,2,3) for t in sample_indices(d['latency_s'+str(k)]))
    if len({t for t,_ in events})!=len(events):raise ValueError('Ambiguous event ordering')
    lo,hi=sorted((float(d['freqtag1']),float(d['freqtag2'])))
    if not (abs(lo-6.6666666667)<1e-6 and abs(hi-8.5714285714)<1e-6):
        raise ValueError('Unexpected tag frequencies')
    out=[]; width=2*fs
    for start in starts:
        end=int(start)+42*fs
        if start<0 or end>len(bad):raise ValueError('Trial out of bounds')
        state=np.zeros(42*fs,dtype=np.uint8)
        local=[(t,k) for t,k in events if start<=t<end]
        for i,(t,k) in enumerate(local):
            right=local[i+1][0] if i+1<len(local) else end
            state[t-start:right-start]=k
        for slot in range(21):
            offset=slot*width;segment=state[offset:offset+width];v=int(segment[0])
            pure=v if v in (1,2) and np.all(segment==v) else 0
            rejected=bool(np.any(bad[start+offset:start+offset+width]))
            z=feature(signal[start+offset:start+offset+width],fs,lo,hi) if pure and not rejected else None
            out.append({'slot':slot,'label':pure,'bad':rejected,'feature':z})
    if len(out)!=105:raise AssertionError('Expected 105 windows')
    return out


def train(rows):
    eligible=[r for r in rows if r['label'] in (1,2) and not r['bad']]
    means={}
    for k in (1,2):
        v=[r['feature'] for r in eligible if r['label']==k]
        if not v or not np.isfinite(v).all():raise ValueError('Missing training class/feature')
        means[k]=float(np.mean(v))
    n1=sum(r['label']==1 for r in eligible); n2=len(eligible)-n1
    majority=1 if n1>=n2 else 2
    slots=[]
    for slot in range(21):
        group=[r['label'] for r in eligible if r['slot']==slot]
        c1=group.count(1);c2=group.count(2)
        slots.append(1 if c1>c2 else 2 if c2>c1 else majority)
    return {'mean_code1':means[1], 'mean_code2':means[2], 'majority':majority,
            'slot_rules':slots,'training_pure_clean_code1':n1,'training_pure_clean_code2':n2}


def assess(rows, model):
    results={name:{'confusion_true_rows_pred_columns':[[0,0],[0,0]]} for name in ('eeg','majority','time_only')}
    unresolved=sum(r['label']==0 for r in rows)
    pure_bad=sum(r['label'] in (1,2) and r['bad'] for r in rows)
    for r in rows:
        if r['label']==0 or r['bad']:continue
        z=r['feature']
        if z is None or not np.isfinite(z):raise ValueError('Invalid eligible test feature')
        pred={'eeg':1 if abs(z-model['mean_code1'])<=abs(z-model['mean_code2']) else 2,
              'majority':model['majority'],'time_only':model['slot_rules'][r['slot']]}
        for name,p in pred.items():results[name]['confusion_true_rows_pred_columns'][r['label']-1][p-1]+=1
    for r in results.values():
        cm=r['confusion_true_rows_pred_columns'];correct=cm[0][0]+cm[1][1];total=sum(sum(x) for x in cm)
        n1=sum(cm[0]);n2=sum(cm[1]);r.update({'pure_clean_windows':total,
            'pure_clean_accuracy':correct/total if total else None,
            'pure_clean_balanced_accuracy':(cm[0][0]/n1+cm[1][1]/n2)/2 if n1 and n2 else None,
            'full_grid_correct_fraction':correct/len(rows),
            'full_grid_disagreement_or_unresolved_fraction':1-correct/len(rows)})
    return {'total_windows':len(rows),'unresolved_report_windows':unresolved,
            'pure_report_but_bad_epoch_windows':pure_bad,'models':results}


def run(paths, inspection_dir):
    if set(paths)!=set(range(1,10)):raise ValueError('Exactly nine scan files required')
    windows={}
    for scan in range(1,10):
        inspection=json.loads((inspection_dir/f'roy_s09_scan{scan}_inspection.json').read_text())
        windows[scan]=read_windows(paths[scan],inspection['sha256'])
    model=train([r for scan in TRAIN for r in windows[scan]])
    tests={str(scan):assess(windows[scan],model) for scan in TEST}
    return {'kind':'post-hoc single-person fit-held-out EEG/report feasibility, not experience calibration',
            'train_scans':list(TRAIN),'test_order':list(TEST), 'training_model':model,
            'tests':tests,
            'conditions':{'1':'rivalry','2':'rivalry','3':'rivalry','4':'replay_smooth',
                          '5':'rivalry','6':'replay_smooth','7':'rivalry','8':'replay_inst','9':'replay_inst'},
            'limitations':['Participant and training EEG previously explored; this is not prospective preregistration.',
                'Test scans are held out from fitting, not independent participants or necessarily independent stimulus sequences.',
                'Strict pure-clean windows select stable reports; full-grid score counts every unresolved window as failure.',
                'Report agreement is not experience accuracy, causal evidence or an fMRI analysis.']}


def main():
    p=argparse.ArgumentParser();p.add_argument('files',nargs=9,type=Path)
    args=p.parse_args();paths={}
    for path in args.files:
        m=re.fullmatch(r'S09_scan([1-9])_filtered_gac_cbc\.mat',path.name)
        if not m or int(m.group(1)) in paths:raise ValueError('Bad scan filenames or duplicate')
        paths[int(m.group(1))]=path
    print(json.dumps(run(paths,Path(__file__).resolve().parent),indent=2,allow_nan=False))


if __name__=='__main__':main()
