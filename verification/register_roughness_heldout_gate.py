#!/usr/bin/env python3
"""Reproduce the fixed retrospective high-vs-middle register comparison.

Obtain the two source CSVs from the pinned GitHub contents API into
.arena/register. Only aggregate results are printed/written; source includes
recruitment identifiers and must not be committed. See the companion plan.
"""
import csv
import hashlib
import json
import math
import random
import statistics
from collections import Counter
from pathlib import Path

ROOT=Path('.arena/register')
FILES={'data.csv':'05f078b5b6680f040af56a669d064e5218651fb754f1811dde36b6363951764a',
       'roughness_and_sharpness.csv':'d5b2014241ca5279ed6ed433ae473ceb39ccb32ad3e4d9d75667e43efd90e367'}

def read(name):
    path=ROOT/name
    if hashlib.sha256(path.read_bytes()).hexdigest()!=FILES[name]:
        raise ValueError(f'source hash mismatch: {name}')
    with path.open(newline='',encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def num(x):
    try:
        a=float(x)
        return a if math.isfinite(a) else None
    except (ValueError,TypeError): return None

def quantile(v,p):
    v=sorted(v); k=(len(v)-1)*p; lo=int(k); hi=min(lo+1,len(v)-1)
    return v[lo]+(k-lo)*(v[hi]-v[lo])

def main():
    physical=read('roughness_and_sharpness.csv'); raw=read('data.csv')
    pred={}
    for row in physical:
        k=(int(row['Stimuli']),int(row['Register']))
        if k in pred: raise ValueError('duplicate stimulus-feature key')
        pred[k]={'roughness':num(row['Roughness']),'sharpness':num(row['Sharpness'])}
    if len(pred)!=28 or any(k not in pred for k in ((c,r) for c in range(1,5) for r in range(1,8))):
        raise ValueError('incomplete feature grid')
    for chord in range(1,5):
        assert all(pred[chord,high]['roughness'] < pred[chord,mid]['roughness']
                   for high in (6,7) for mid in (4,5))
        assert all(pred[chord,high]['sharpness'] > pred[chord,mid]['sharpness']
                   for high in (6,7) for mid in (4,5))
    excludes=Counter(); data=[]; ids=set()
    for row in raw:
        if not row['participant'] or row['participant'] in ids:
            raise ValueError('missing or duplicate participant key')
        ids.add(row['participant'])
        headphone=num(row['check:1'])
        if headphone is None or headphone<4:
            excludes['headphone_missing_or_below_4']+=1; continue
        repeat=[num(row[f'repeated_items{i}:1']) for i in (1,2,3)]
        if any(v is None for v in repeat) or statistics.mean(abs(v) for v in repeat)>=4:
            excludes['repeat_missing_or_mean_absolute_ge_4']+=1; continue
        by_chord=[]
        for c in range(1,5):
            vals=[num(row[f'Chord{c}{r}:1']) for r in ('R0','Ru1','Ru2','Ru3')]
            by_chord.append(vals)
        if any(v is None or not 0<=v<=10 for vals in by_chord for v in vals):
            excludes['target_missing_or_out_of_range']+=1; continue
        data.append(by_chord)
    if len(data)<2: raise ValueError('insufficient eligible people')
    mid=lambda vals:(vals[0]+vals[1])/2
    high=lambda vals:(vals[2]+vals[3])/2
    per=[statistics.mean(high(v)-mid(v) for v in person) for person in data]
    diff=statistics.mean(per)
    mean_middle=statistics.mean(mid(v) for person in data for v in person)
    mean_high=statistics.mean(high(v) for person in data for v in person)
    assert abs(diff-(mean_high-mean_middle))<1e-12
    rng=random.Random(7163)
    boot=[statistics.mean(per[rng.randrange(len(per))] for _ in per) for _ in range(10000)]
    vals=[]
    for c in range(4):
        m=statistics.mean(mid(p[c]) for p in data); h=statistics.mean(high(p[c]) for p in data)
        vals.append({'chord':c+1,'middle_mean':m,'high_mean':h,'difference_high_minus_middle':h-m,
                     'roughness_middle':[pred[c+1,r]['roughness'] for r in (4,5)],
                     'roughness_high':[pred[c+1,r]['roughness'] for r in (6,7)],
                     'sharpness_middle':[pred[c+1,r]['sharpness'] for r in (4,5)],
                     'sharpness_high':[pred[c+1,r]['sharpness'] for r in (6,7)]})
    out={'scope':'Retrospective human-rating subset, not a neural or phenomenal identity test.',
         'source_commit':'cdc4fc748e1535d9c0dd197f4c429bee80ff9514', 'input_sha256':FILES,
         'total_source_rows':len(raw),'exclusion_counts_in_order':dict(excludes),'eligible_people':len(data),
         'middle_mean':mean_middle,'high_mean':mean_high,'high_minus_middle':diff,
         'bootstrap_95_percentile': [quantile(boot,.025),quantile(boot,.975)],
         'descriptive_people_negative_zero_positive':[sum(x<0 for x in per),sum(x==0 for x in per),sum(x>0 for x in per)],
         'minimum_rmse_for_two_observed_cell_means_under_monotone_rule':max(0,-diff)/2,
         'chord_specific':vals,'not_original_55_person_QC_sample':True}
    Path('verification/register_roughness_heldout_gate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
