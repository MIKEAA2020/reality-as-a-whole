#!/usr/bin/env python3
"""Exploratory, previously inspected participants; no fitted model or raw output."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat
from roy_s01_frozen_three_state_transfer import SOURCE, dropbox_hash
from roy_s01_mixed_coverage_diagnostic import load_trials
from roy_s09_scan1_alignment_gate import sample_indices
from roy_s09_eeg_report_transfer import feature, sha

FS=250
STEP=50
WIDTH=500
SCANS={'S01':(1,3,5,7,10,12),'S02':(1,2,4,6,8,11),'S09':(1,2,3,5,7)}


def grid(n=42*FS):
    return np.arange(FS,n-FS+1,STEP,dtype=int)


def segments(state):
    st=np.asarray(state)
    if st.ndim!=1 or not np.isin(st,[0,1,2,3]).all():raise ValueError('Invalid state')
    boundaries=np.r_[0,np.flatnonzero(st[1:]!=st[:-1])+1,len(st)]
    return [(int(a),int(b),int(st[a])) for a,b in zip(boundaries[:-1],boundaries[1:])]


def context(state,center):
    part=np.asarray(state)[center-FS:center+FS]
    if part.shape!=(WIDTH,) or not np.isin(part,[0,1,2,3]).all():raise ValueError('Invalid context')
    weights=np.hanning(WIDTH)**2
    return {'mixed_fraction':float(np.mean(part==3)),
            'unknown_fraction':float(np.mean(part==0)),
            'code1_fraction':float(np.mean(part==1)), 'code2_fraction':float(np.mean(part==2)),
            'mixed_hann_squared_weight_fraction':float(weights[part==3].sum()/weights.sum())}


def candidates(state,mask):
    state=np.asarray(state);mask=np.asarray(mask)
    if state.shape!=(42*FS,) or mask.shape!=state.shape or not np.isin(mask,[0,1]).all():raise ValueError('Invalid trial')
    runs=segments(state); centers=grid(); mixed=[]; counts={'mixed_segments_total':0,'mixed_segments_without_valid_grid_center':0,'mixed_segments_artifact_excluded':0}
    bounds=[]
    for a,b,k in runs:
        if k!=3:continue
        counts['mixed_segments_total']+=1
        if a>0 and state[a-1] in (1,2):bounds.append(a)
        if b<len(state) and state[b] in (1,2):bounds.append(b)
        available=centers[(centers>=a)&(centers<b)]
        if not len(available):counts['mixed_segments_without_valid_grid_center']+=1;continue
        c=int(min(available,key=lambda c:(abs(2*c-(a+b)),c)))
        if mask[c-FS:c+FS].any():counts['mixed_segments_artifact_excluded']+=1;continue
        mixed.append(c)
    controls=[]
    for c in centers:
        if state[c] in (1,2) and bounds and min(abs(int(c)-b) for b in bounds)<=STEP:
            if not mask[c-FS:c+FS].any():controls.append(int(c))
    counts.update({'eligible_mixed_segments':len(mixed),'clean_control_centers':len(controls)})
    return mixed,controls,counts


def match(mixed,controls):
    if len(mixed)!=len(set(mixed)) or len(controls)!=len(set(controls)):raise ValueError('Duplicate centers')
    unused=set(controls);pairs=[]
    for m in sorted(mixed):
        choices=[c for c in unused if 2*FS<=abs(c-m)<=6*FS]
        if choices:
            c=min(choices,key=lambda c:(abs(c-m),c));unused.remove(c);pairs.append((m,c))
    return pairs


def stability(state,center):
    c=int(state[center]);return (int(state[center-STEP]==c),int(state[center+STEP]==c))


def flank_db(signal):
    x=np.asarray(signal,dtype=float)
    if x.shape!=(WIDTH,) or not np.isfinite(x).all():raise ValueError('Invalid EEG')
    x=(x-x.mean())*np.hanning(WIDTH); t=np.arange(WIDTH)/FS
    def power(f):return float(abs(x @ np.exp(-2j*np.pi*f*t))**2)
    out=[]
    for f in (6.6666666667,8.5714285714):
        p=power(f); flank=(power(f-1)+power(f+1))/2
        if p<=0 or flank<=0 or not np.isfinite(p+flank):raise ValueError('Undefined local spectral contrast')
        out.append(float(10*np.log10(p/flank)))
    return out


def stats(values):
    return {'n':len(values),'mean':float(np.mean(values)) if values else None,
            'median':float(np.median(values)) if values else None}


def summarize(subject, trials):
    context_values={k:[] for k in ('mixed_fraction','unknown_fraction','code1_fraction','code2_fraction','mixed_hann_squared_weight_fraction')}
    classes={str(k):{'total':0,'artifact':0,'clean':0} for k in (0,1,2,3)}
    countkeys=('mixed_segments_total','mixed_segments_without_valid_grid_center','mixed_segments_artifact_excluded','eligible_mixed_segments','clean_control_centers')
    counts={k:0 for k in countkeys};pairs_all=[]
    for signal,mask,state in trials:
        for c in grid():
            k=int(state[c]); bad=bool(mask[c-FS:c+FS].any())
            classes[str(k)]['total']+=1;classes[str(k)]['artifact' if bad else 'clean']+=1
            if k==3 and not bad:
                for key,value in context(state,int(c)).items():context_values[key].append(value)
        mixed,controls,n=candidates(state,mask)
        for k in countkeys:counts[k]+=n[k]
        for m,c in match(mixed,controls):
            pairs_all.append({'difference':feature(signal[m-FS:m+FS],FS,6.6666666667,8.5714285714)-feature(signal[c-FS:c+FS],FS,6.6666666667,8.5714285714),
                              'mixed_context':context(state,m),'control_context':context(state,c),
                              'distance_seconds':abs(c-m)/FS,'control_before_mixed':c<m,'control_code':int(state[c]),
                              'mixed_stability':stability(state,m),'control_stability':stability(state,c),
                              'mixed_flanks_db':flank_db(signal[m-FS:m+FS]),'control_flanks_db':flank_db(signal[c-FS:c+FS])})
    n=len(pairs_all);counts['matched_pairs']=n;counts['unmatched_eligible_mixed_segments']=counts['eligible_mixed_segments']-n
    def prop(x):return float(sum(x)/len(x)) if x else None
    differences=[p['difference'] for p in pairs_all]
    paired={'log10_ratio_mixed_minus_control':stats(differences),
            'fraction_positive':prop([v>0 for v in differences]),
            'distance_seconds':stats([p['distance_seconds'] for p in pairs_all]),
            'controls_before_mixed':sum(p['control_before_mixed'] for p in pairs_all),
            'control_code_counts':{str(k):sum(p['control_code']==k for p in pairs_all) for k in (1,2)},
            'mixed_context':{k:stats([p['mixed_context'][k] for p in pairs_all]) for k in context_values},
            'control_context':{k:stats([p['control_context'][k] for p in pairs_all]) for k in context_values},
            'mixed_unchanged_0p2s_earlier':prop([p['mixed_stability'][0] for p in pairs_all]),
            'mixed_unchanged_0p2s_later':prop([p['mixed_stability'][1] for p in pairs_all]),
            'control_unchanged_0p2s_earlier':prop([p['control_stability'][0] for p in pairs_all]),
            'control_unchanged_0p2s_later':prop([p['control_stability'][1] for p in pairs_all]),
            'local_tag_flank_db':{side:{tag:stats([p[f'{side}_flanks_db'][i] for p in pairs_all]) for i,tag in enumerate(('low','high'))} for side in ('mixed','control')}}
    return {'participant':subject,'grid_centers_by_code_and_artifact':classes,
            'clean_mixed_center_window_context':{k:stats(v) for k,v in context_values.items()},
            'matching_coverage':counts,'matched_pair_summary':paired}


def load_scan(path,expected):
    if sha(path)!=expected:raise ValueError('Input SHA-256 mismatch')
    states,masks,fs,_=load_trials(path)
    d=loadmat(path,squeeze_me=True,struct_as_record=False,variable_names=['EEG','chanlabels','latency_trial','freqtag1','freqtag2'])
    eeg=d['EEG']; names=[str(x) for x in np.atleast_1d(d['chanlabels'])];x=np.asarray(eeg.data)
    tags=sorted([float(d['freqtag1']),float(d['freqtag2'])])
    if fs!=FS or float(eeg.srate)!=FS or names.count('POz')!=1 or x.ndim!=2 or x.shape[0]!=len(names):raise ValueError('EEG schema')
    if abs(tags[0]-6.6666666667)>1e-6 or abs(tags[1]-8.5714285714)>1e-6:raise ValueError('Unexpected tags')
    starts=sample_indices(d['latency_trial'])-1;out=[]
    for start,state,mask in zip(starts,states,masks):
        sig=x[names.index('POz'),start:start+42*FS]
        if len(sig)!=42*FS:raise ValueError('Invalid EEG length')
        out.append((sig,mask,state))
    return out


def main():
    p=argparse.ArgumentParser()
    for subject in ('s01','s02','s09'):p.add_argument('--'+subject,type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    root=Path(__file__).resolve().parent; dirs={'S01':args.s01,'S02':args.s02,'S09':args.s09}
    receipt=json.loads((root/'roy_s02_dropbox_integrity_receipt.json').read_text())['files']
    expected={}
    # Validate the entire input set before computing statistics.
    for subject,scans in SCANS.items():
        for s in scans:
            path=dirs[subject]/f'{subject}_scan{s}_filtered_gac_cbc.mat'
            if subject=='S01':
                size,h=SOURCE[s]
                if path.stat().st_size!=size or dropbox_hash(path)!=h:raise ValueError('S01 Dropbox mismatch')
                digest=sha(path)
            elif subject=='S02':digest=receipt[str(s)]['sha256']
            else:digest=json.loads((root/f'roy_s09_scan{s}_inspection.json').read_text())['sha256']
            if sha(path)!=digest:raise ValueError('Source digest mismatch')
            expected[(subject,s)]=digest
    data={}
    for subject,scans in SCANS.items():
        trials=[]
        for s in scans:
            path=dirs[subject]/f'{subject}_scan{s}_filtered_gac_cbc.mat'
            trials.extend(load_scan(path,expected[(subject,s)]))
        data[subject]=summarize(subject,trials)
    result={'scope':'Retrospective exploratory diagnostics in three previously inspected participants; no held-out validation.',
            'scans':{k:list(v) for k,v in SCANS.items()},'per_participant':data,
            'limitations':['Fixed reconstructed report labels and timing are provisional.',
            'Mixed and nonmixed controls are only partly matched; pairs across events can overlap.',
            'Hann squared weight fractions are not additive decomposition of spectral power.',
            'Local flank ratios are descriptive, not validated signal-to-noise or proof of experience.']}
    text=json.dumps(result,indent=2,allow_nan=False)+'\n';args.output.write_text(text);print(text,end='')


if __name__=='__main__':main()
