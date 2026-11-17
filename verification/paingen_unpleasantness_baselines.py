#!/usr/bin/env python3
"""Exploratory out-of-family unpleasantness prediction; aggregate output only.

See PAINGEN_UNPLEASANTNESS_PREDICTOR_PROTOCOL.md. Takes a pinned public table
on demand or via --data, hashes it, never writes participant rows or IDs.
Requires NumPy (see verification/requirements-framework-battery.txt).
"""
import argparse
import csv
import hashlib
import io
import itertools
import json
import math
from pathlib import Path
import urllib.request
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
COMMIT = 'da46f2f9739ad2e9eeb9658711582be6357c1026'
EXPECTED = '0eda58e9f8f83ec5294e92c907babfc771c0172ef22706e0be52c7182dbe8f56'
SIZE = 3728915
URL = ('https://api.github.com/repos/rotemb9/paingen-placebo-fmri-paper/'
       'contents/pain_evoked_brain_measures.csv?ref=' + COMMIT)
MODELS = {'condition_only':(), 'condition_plus_nps':('nps',),
          'condition_plus_siips':('siips',), 'condition_plus_both':('nps','siips')}
CONDITIONS = list(itertools.product((-0.5, 0.5), (-0.5, 0.0, 0.5), (-0.5, 0.5)))
SALT='paingen-family-split-v1:'


def get_data(path):
    if path:
        raw=Path(path).read_bytes()
    else:
        req=urllib.request.Request(URL,headers={'User-Agent':'SEEP-audit/1.0',
            'Accept':'application/vnd.github.raw+json'})
        with urllib.request.urlopen(req,timeout=60) as response:
            length=response.headers.get('Content-Length')
            if length is not None and int(length)>SIZE:
                raise ValueError('source exceeds fixed byte budget')
            raw=response.read(SIZE+1)
    if len(raw)!=SIZE or hashlib.sha256(raw).hexdigest()!=EXPECTED:
        raise ValueError('source length/hash mismatch')
    return raw


def number(value):
    try:
        v=float(value)
    except (ValueError,TypeError):
        return None
    return v if math.isfinite(v) else None


def fold_for(family):
    return int(hashlib.sha256((SALT+family).encode()).hexdigest(),16)%5


def metrics(y,p,groups=None):
    y=np.asarray(y,dtype=float); p=np.asarray(p,dtype=float)
    if len(y)==0: raise ValueError('empty metric subset')
    mse=float(np.mean((y-p)**2))
    r=None if len(y)<2 or np.std(y)==0 or np.std(p)==0 else float(np.corrcoef(y,p)[0,1])
    out={'count':len(y),'rmse':math.sqrt(mse),'mae':float(np.mean(np.abs(y-p))),
         'pearson_r':r,'mean_observed':float(np.mean(y)),'mean_predicted':float(np.mean(p))}
    if groups is not None:
        sums={}; counts={}
        for g,e in zip(groups,(y-p)**2):
            sums[g]=sums.get(g,0.0)+float(e); counts[g]=counts.get(g,0)+1
        out['family_averaged_rmse']=math.sqrt(sum(sums[g]/counts[g] for g in sums)/len(sums))
        out['families']=len(sums)
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',help='local exact pinned CSV; otherwise fetch only that file from GitHub')
    args=ap.parse_args()
    raw=get_data(args.data)
    reader=csv.DictReader(io.StringIO(raw.decode('utf-8-sig'),newline=''))
    required={'participant_ID','family_ID','Yunp','nps','siips','heat','stimLvl','prodicaine'}
    if not required.issubset(reader.fieldnames or []): raise ValueError('schema mismatch')
    rows=[]; total=0; invalid=0; family_by_person={}; seen=set(); source_families=set(); source_people=set()
    for record in reader:
        total+=1
        person=record['participant_ID'].strip(); family=record['family_ID'].strip()
        if not person or not family: raise ValueError('missing grouping ID')
        if person in family_by_person and family_by_person[person]!=family:
            raise ValueError('participant has inconsistent family')
        family_by_person[person]=family
        source_families.add(family); source_people.add(person)
        h,level,placebo=(number(record[x]) for x in ('heat','stimLvl','prodicaine'))
        cond=(h,level,placebo)
        if cond not in CONDITIONS: raise ValueError('unexpected centered condition codes')
        key=(person,cond)
        if key in seen: raise ValueError('duplicate participant/condition')
        seen.add(key)
        y,nps,siips=(number(record[x]) for x in ('Yunp','nps','siips'))
        if y is None or nps is None or siips is None:
            invalid+=1
            continue
        rows.append({'person':person,'family':family,'condition':cond,
                     'y':y,'nps':nps,'siips':siips,'fold':fold_for(family)})
    n=len(rows)
    y=np.array([r['y'] for r in rows]); families=[r['family'] for r in rows]
    folds=np.array([r['fold'] for r in rows])
    onehot=np.array([[float(r['condition']==c) for c in CONDITIONS] for r in rows])
    features={name:np.array([r[name] for r in rows]) for name in ('nps','siips')}
    predictions={name:np.full(n,np.nan) for name in MODELS}
    fold_summary=[]
    for fold in range(5):
        test=folds==fold; train=~test
        if not test.any() or not train.any():raise ValueError('empty fold')
        if set(families[i] for i in np.flatnonzero(test)) & set(families[i] for i in np.flatnonzero(train)):
            raise AssertionError('family leakage')
        matrices={}
        for feat in ('nps','siips'):
            mean=features[feat][train].mean(); sd=features[feat][train].std()
            if sd<=0: raise ValueError('constant signature in training')
            matrices[feat]=(features[feat]-mean)/sd
        for name,extra in MODELS.items():
            design=np.column_stack([onehot]+[matrices[f] for f in extra])
            coef,_,rank,_=np.linalg.lstsq(design[train],y[train],rcond=None)
            if rank!=design.shape[1]:raise ValueError('rank deficient fold/design')
            predictions[name][test]=design[test]@coef
        fold_summary.append({'fold':fold,'complete_rows':int(test.sum()),
                             'families':len(set(families[i] for i in np.flatnonzero(test)))})
    assert all(np.isfinite(p).all() for p in predictions.values())
    scores={name:metrics(y,p,families) for name,p in predictions.items()}
    for name in scores:
        scores[name]['rmse_difference_vs_condition_only']=scores[name]['rmse']-scores['condition_only']['rmse']

    # Pair placebo/control only on participant, modality and stimulus level.
    pairidx={}
    for i,row in enumerate(rows):
        h,level,treat=row['condition']; key=(row['person'],h,level)
        pairidx.setdefault(key,{})[treat]=i
    pairs=[(idx[-0.5],idx[0.5],k[1]) for k,idx in pairidx.items()
           if -0.5 in idx and 0.5 in idx]
    paired={}
    for label,modality in [('all',None),('thermal',0.5),('mechanical',-0.5)]:
        subset=[(a,b) for a,b,h in pairs if modality is None or h==modality]
        ya=np.array([y[a]-y[b] for a,b in subset]); gs=[families[a] for a,b in subset]
        assert all(families[a]==families[b] and folds[a]==folds[b] for a,b in subset)
        res={'zero_effect':metrics(ya,np.zeros(len(ya)),gs)}
        for name,p in predictions.items():
            pp=np.array([p[a]-p[b] for a,b in subset])
            res[name]=metrics(ya,pp,gs)
        paired[label]=res
    summary={'status':'completed',
             'scope':'exploratory published condition means; out-of-family not out-of-study; no measured mismatch, causality of ground, subjective identity or clinical diagnosis',
             'source':{'url':URL,'commit':COMMIT,'sha256':EXPECTED,'bytes':SIZE},
             'selection':{'source_rows':total,'source_people':len(source_people),'source_families':len(source_families),
                 'incomplete_outcome_or_predictor_rows':invalid,'complete_rows':n,
                 'complete_people':len(set(r['person'] for r in rows)),
                 'complete_families':len(set(families))},
             'folds':fold_summary,'condition_level_oof':scores,'paired_control_minus_placebo_oof':paired,
             'unit_note':'Yunp source-file scale as supplied, not independently calibrated or a pain measurement unit',
             'protocol':'PAINGEN_UNPLEASANTNESS_PREDICTOR_PROTOCOL.md',
             'privacy':'No participant identifiers, demographics, or participant-level results are stored here.'}
    out=ROOT/'verification/paingen_unpleasantness_baselines.json'
    out.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    main()
