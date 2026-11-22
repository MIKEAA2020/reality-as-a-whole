#!/usr/bin/env python3
"""Exploratory S01/S09 report-center development, not a held-out validation.

Outputs aggregate metrics and frozen training parameters only, never raw EEG,
individual event sequences, or timestamps. See companion protocol for caveats.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat
from roy_s09_eeg_report_transfer import feature, sha
from roy_s01_frozen_three_state_transfer import RIVALRY, verify_sources
from roy_s01_mixed_coverage_diagnostic import load_trials

FS = 250
WIDTH = 2 * FS
STEP = FS // 5  # 0.2 s exactly
CLASSES = (1, 2, 3)
SCANS = {'S01': RIVALRY, 'S09': (1, 2, 3, 5, 7)}


def trial_rows(signal, mask, state, trial_id, fs=FS):
    if fs != FS or len(signal) != 42*fs or len(mask) != len(signal) or len(state) != len(signal):
        raise ValueError('Unexpected trial dimensions or rate')
    if not np.all(np.isin(state, (0,1,2,3))) or not np.all(np.isin(mask,(0,1))):
        raise ValueError('Unexpected state or artifact mask')
    # Adjacent reports of the same code form one uninterrupted state segment.
    segments = np.cumsum(np.r_[True, state[1:] != state[:-1]])
    rows = []
    for center in range(fs, len(state)-fs+1, STEP):
        start=center-fs; end=center+fs
        bad=bool(np.any(mask[start:end]))
        z=None if bad else feature(signal[start:end], fs, 6.6666666667, 8.5714285714)
        rows.append({'label':int(state[center]), 'bad':bad, 'feature':z,
                     'slot':center//fs, 'segment':(trial_id,int(segments[center]))})
    return rows


def read_scan(path, expected_sha, scan):
    if sha(path)!=expected_sha: raise ValueError('Input SHA-256 mismatch')
    states, masks, fs, _ = load_trials(path)
    d = loadmat(path, squeeze_me=True,struct_as_record=False,
                variable_names=['EEG','sampling_freq','freqtag1','freqtag2','chanlabels','latency_trial'])
    from roy_s09_scan1_alignment_gate import sample_indices
    names=[str(x) for x in np.atleast_1d(d['chanlabels'])]
    eeg=d['EEG']; signal=np.asarray(eeg.data)
    tags=sorted([float(d['freqtag1']),float(d['freqtag2'])])
    if fs!=FS or float(eeg.srate)!=fs or names.count('POz')!=1 or signal.ndim!=2 or signal.shape[0]!=len(names):
        raise ValueError('Invalid EEG schema')
    if abs(tags[0]-6.6666666667)>1e-6 or abs(tags[1]-8.5714285714)>1e-6:
        raise ValueError('Invalid tagging frequencies')
    starts=sample_indices(d['latency_trial'])-1
    out=[]
    for trial,(start,state,mask) in enumerate(zip(starts,states,masks)):
        x=signal[names.index('POz'),start:start+42*fs]
        out.extend(trial_rows(x,mask,state,(scan,trial)))
    return out


def majority(counts, default=1):
    a=np.asarray(counts,dtype=float)
    if a.shape!=(3,) or not np.isfinite(a).all() or (a<0).any(): raise ValueError('Invalid counts')
    return default if a.sum()==0 else int(np.argmax(a))+1


def fit(participants):
    """Equal participant weight within each class, including slot baselines."""
    if not participants: raise ValueError('No training participants')
    means=[]
    for k in CLASSES:
        per=[]
        for rows in participants.values():
            values=[r['feature'] for r in rows if not r['bad'] and r['label']==k]
            if not values or any(v is None or not np.isfinite(v) for v in values):
                raise ValueError('Missing or invalid participant training class')
            per.append(float(np.mean(values)))
        means.append(float(np.mean(per)))
    proportions=[]; slots=[]
    for rows in participants.values():
        clean=[r for r in rows if not r['bad'] and r['label'] in CLASSES]
        if not clean: raise ValueError('Missing training labels')
        proportions.append([sum(r['label']==k for r in clean)/len(clean) for k in CLASSES])
    global_majority=majority(np.mean(proportions,axis=0))
    for slot in range(42):
        # Equal participant weight at each observed slot; missing slots are ignored.
        groups=[]
        for rows in participants.values():
            local=[r for r in rows if not r['bad'] and r['label'] in CLASSES and r['slot']==slot]
            if local: groups.append([sum(r['label']==k for r in local)/len(local) for k in CLASSES])
        slots.append(majority(np.mean(groups,axis=0),global_majority) if groups else global_majority)
    return {'class_mean_features':means,'majority':global_majority,'slot_rules':slots,
            'training_participants':sorted(participants)}


def predict(row,model):
    if row['bad']: return None
    z=row['feature']
    if z is None or not np.isfinite(z) or not 0<=row['slot']<42: raise ValueError('Invalid feature or slot')
    return {'eeg':min(CLASSES,key=lambda k:(abs(z-model['class_mean_features'][k-1]),k)),
            'majority':model['majority'], 'time_only':model['slot_rules'][row['slot']]}


def assess(rows,model):
    cms={m:np.zeros((3,3),dtype=int) for m in ('eeg','majority','time_only')}
    groups={m:{} for m in cms}
    for r in rows:
        pred=predict(r,model)
        if pred is None or r['label'] not in CLASSES: continue
        for m,k in pred.items():
            cms[m][r['label']-1,k-1]+=1
            if r['label']==3: groups[m].setdefault(r['segment'],[]).append(k==3)
    models={}
    for m,mat in cms.items():
        counts=mat.sum(axis=1); predicted=mat.sum(axis=0); total=int(mat.sum())
        recalls=[float(mat[i,i]/counts[i]) if counts[i] else None for i in range(3)]
        precision=float(mat[2,2]/predicted[2]) if predicted[2] else None
        segments=groups[m]
        models[m]={'confusion_true_rows_pred_columns':mat.tolist(), 'recalls':recalls,
                   'macro_recall':float(sum(recalls)/3) if all(x is not None for x in recalls) else None,
                   'accuracy':float(np.trace(mat)/total) if total else None,
                   'mixed_precision':precision,
                   'mixed_eligible_segments':len(segments),
                   'mixed_segment_equal_weight_recall':float(np.mean([np.mean(v) for v in segments.values()])) if segments else None,
                   'mixed_segments_with_any_hit':sum(any(v) for v in segments.values())}
    unresolved=sum(r['label']==0 for r in rows); bad=sum(r['bad'] for r in rows)
    overlap=sum(r['bad'] and r['label']==0 for r in rows)
    return {'total_centers':len(rows),'unknown_centers':unresolved,'artifact_centers':bad,
            'unknown_artifact_overlap':overlap,'labeled_clean_centers':len(rows)-unresolved-bad+overlap,
            'models':models}


def main():
    p=argparse.ArgumentParser();p.add_argument('s01',type=Path);p.add_argument('s09',type=Path);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args(); root=Path(__file__).resolve().parent
    s01hash=verify_sources(args.s01); all_rows={}
    for subject in SCANS:
        rows=[]
        for s in SCANS[subject]:
            directory=args.s01 if subject=='S01' else args.s09
            path=directory/f'{subject}_scan{s}_filtered_gac_cbc.mat'
            expected=s01hash[s] if subject=='S01' else json.loads((root/f'roy_s09_scan{s}_inspection.json').read_text())['sha256']
            rows.extend(read_scan(path,expected,s))
        all_rows[subject]=rows
    out={'scope':'Exploratory development on previously inspected S01 and S09; leave-one-participant comparisons are not independent validation.',
         'scans':{s:list(v) for s,v in SCANS.items()},'center_step_seconds':0.2,'eeg_window_seconds':2,
         'leave_one_development_participant_out':{s:assess(all_rows[s],fit({other:all_rows[other]})) for s,other in (('S01','S09'),('S09','S01'))},
         'pooled_development_model':fit(all_rows),
         'limitations':['EEG windows overlap and contain context before and after the target report center.',
                        'Center code is report-derived, not an independently verified percept; marker timing remains provisional.',
                        'Mixed segment aggregates are descriptive and conditional on a clean in-trial center.']}
    text=json.dumps(out,indent=2,allow_nan=False)+'\n';args.output.write_text(text);print(text,end='')


if __name__=='__main__': main()
