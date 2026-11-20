#!/usr/bin/env python3
"""Retrospective held-out test of third-party purported DREAMER feature table.

See EEG_BASELINE_DEVIATION_VALENCE_ANALYSIS_PLAN.md. No raw inputs or
participant-level predictions are written. Requires Python standard library.
"""
import csv
import hashlib
import json
import math
import random
import statistics
from pathlib import Path

SOURCE=Path('.arena/dreamer/dreamer_features.csv')
HASH='7d232f1cf469ef9fb85a0d0e83777d100016bd437617a639ffb7e5127615b239'
OUT=Path('verification/eeg_baseline_deviation_valence_gate.json')

def mean(xs): return statistics.mean(xs)

def load():
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest()!=HASH: raise ValueError('source hash mismatch')
    with SOURCE.open(newline='') as f: source=list(csv.DictReader(f))
    rows=[]; keys=set()
    for row in source:
        subject=int(row['subject']); clip=int(row['clip']); y=float(row['valence'])
        alpha=[float(row[f'ch{i}_alpha']) for i in range(14)]
        if not 1<=y<=5 or y!=int(y) or not all(math.isfinite(x) for x in alpha):
            raise ValueError('invalid label or alpha feature')
        if (subject,clip) in keys: raise ValueError('duplicate subject/clip')
        keys.add((subject,clip))
        rows.append({'s':subject,'c':clip,'y':y,
                     'deviation':math.sqrt(mean([v*v for v in alpha])), 'signed':mean(alpha)})
    subjects=sorted({r['s'] for r in rows}); clips=sorted({r['c'] for r in rows})
    if len(subjects)!=23 or len(clips)!=18 or len(keys)!=len(subjects)*len(clips):
        raise ValueError('unexpected or incomplete subject/clip grid')
    return rows,subjects,clips

def fit(train,feature=None,film=False):
    """Training-only OLS, optionally with categorical film intercepts."""
    if film:
        categories=sorted({r['c'] for r in train})
        ybar={c:mean([r['y'] for r in train if r['c']==c]) for c in categories}
        xbar={c:mean([r[feature] for r in train if r['c']==c]) for c in categories} if feature else {}
        pairs=[(r[feature]-xbar[r['c']],r['y']-ybar[r['c']]) for r in train] if feature else []
        xx=sum(x*x for x,y in pairs); slope=sum(x*y for x,y in pairs)/xx if xx else 0.0
        return lambda r:ybar[r['c']]+(slope*(r[feature]-xbar[r['c']]) if feature else 0.0)
    ybar=mean([r['y'] for r in train])
    if not feature: return lambda r:ybar
    xbar=mean([r[feature] for r in train]); xx=sum((r[feature]-xbar)**2 for r in train)
    slope=sum((r[feature]-xbar)*(r['y']-ybar) for r in train)/xx if xx else 0.0
    return lambda r:ybar+slope*(r[feature]-xbar)

def qtile(a,p):
    a=sorted(a); z=(len(a)-1)*p; i=int(z); return a[i]+(z-i)*(a[min(i+1,len(a)-1)]-a[i])

def summary(rows,preds,comparisons,subjects):
    metrics={}
    for model,p in preds.items():
        if len(p)!=len(rows) or any(not math.isfinite(v) for v in p): raise ValueError('incomplete prediction')
        errs=[v-r['y'] for v,r in zip(p,rows)]
        metrics[model]={'rmse':math.sqrt(mean([e*e for e in errs])), 'mae':mean([abs(e) for e in errs])}
    # Same bootstrap indices for each model comparison, preserving pairing.
    rng=random.Random(1823); by_subject={s:[i for i,r in enumerate(rows) if r['s']==s] for s in subjects}
    differences={name:[] for name in comparisons}
    sample_deltas={name:[(preds[a][i]-r['y'])**2-(preds[b][i]-r['y'])**2
                         for i,r in enumerate(rows)] for name,(a,b) in comparisons.items()}
    for _ in range(10000):
        draw=[subjects[rng.randrange(len(subjects))] for _ in subjects]
        for name,deltas in sample_deltas.items():
            differences[name].append(mean([mean([deltas[i] for i in by_subject[s]]) for s in draw]))
    return {'metrics':metrics,'mse_difference_candidate_minus_comparator':{
        n:{'mean':mean(ds),'fixed_prediction_participant_bootstrap_95':[qtile(differences[n],.025),qtile(differences[n],.975)]}
        for n,ds in sample_deltas.items()}}

def main():
    rows,subjects,clips=load(); n=len(rows)
    loso_names={'global':(None,False),'global_plus_deviation':('deviation',False),
                'global_plus_signed':('signed',False),'film_mean':(None,True),
                'film_plus_deviation':('deviation',True),'film_plus_signed':('signed',True)}
    double_names={k:v for k,v in loso_names.items() if not v[1]}
    loso={k:[float('nan')]*n for k in loso_names}
    double={k:[float('nan')]*n for k in double_names}
    assigned1=[0]*n; assigned2=[0]*n
    for subject in subjects:
        train=[r for r in rows if r['s']!=subject]
        for name,(feature,film) in loso_names.items():
            fn=fit(train,feature,film)
            for i,r in enumerate(rows):
                if r['s']==subject: loso[name][i]=fn(r)
        for i,r in enumerate(rows): assigned1[i]+=int(r['s']==subject)
    sg={s:i%5 for i,s in enumerate(subjects)}; cg={c:i%3 for i,c in enumerate(clips)}
    for sgroup in range(5):
        for cgroup in range(3):
            train=[r for r in rows if sg[r['s']]!=sgroup and cg[r['c']]!=cgroup]
            test=[i for i,r in enumerate(rows) if sg[r['s']]==sgroup and cg[r['c']]==cgroup]
            assert not ({r['s'] for r in train} & {rows[i]['s'] for i in test})
            assert not ({r['c'] for r in train} & {rows[i]['c'] for i in test})
            for name,(feature,film) in double_names.items():
                fn=fit(train,feature,film)
                for i in test: double[name][i]=fn(rows[i])
            for i in test: assigned2[i]+=1
    assert all(v==1 for v in assigned1+assigned2)
    results={'source_csv_sha256':HASH,'source_commit':'4f7da1a235e9f144928d648a4d7a6c541de6bf2b',
             'source_provenance':'Third-party table claims DREAMER origin; raw source not verified.',
             'n_people':len(subjects),'n_films':len(clips),'n_observations':n,
             'person_held_out':summary(rows,loso,{'deviation_vs_film_mean':('film_plus_deviation','film_mean'),
                                                'deviation_vs_signed':('film_plus_deviation','film_plus_signed')},subjects),
             'person_and_film_group_held_out':summary(rows,double,{'deviation_vs_global':('global_plus_deviation','global'),
                                                                   'deviation_vs_signed':('global_plus_deviation','global_plus_signed')},subjects),
             'bootstrap':{'seed':1823,'replicates':10000,'conditional_on_predictions':True},
             'scope':'Exploratory scalp alpha power deviation, not phase frustration, pain, mechanism or experiential identity.'}
    OUT.write_text(json.dumps(results,indent=2)+'\n'); print(json.dumps(results,indent=2))
if __name__=='__main__': main()
