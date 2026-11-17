#!/usr/bin/env python3
"""Exploratory grouped pain-report prediction; aggregate results only.
See CARDIAC_FEEDBACK_PAIN_PREDICTION_PROTOCOL.md; no EEG or mismatch is inferred.
"""
import argparse
import collections
import hashlib
import io
import json
import math
from pathlib import Path
import urllib.request

import numpy as np
import openpyxl

ROOT=Path(__file__).resolve().parent.parent
COMMIT='c1c8721f0e3d00fefc602ed32b84e24c218c56d3'
SHA='c186908c35e4819d2ea094fa339b4a9fc691556b13dc62585d12d09c6041bb02'
SIZE=537743
URL=('https://api.github.com/repos/EP171993/painperception/contents/'
     'Data_v3%20-%202504.xlsx?ref='+COMMIT)
SALT='cardiac-pain-participant-split-v1:'
GROUPS=('Intero','Extero'); LEVELS=(2,3,4); FEEDBACK=('Congruent','Slower','Faster')
MODELS={'baseline':(), 'unsigned_label':('unsigned',),
        'signed_label':('signed',), 'both_labels':('unsigned','signed')}


def load(path):
    if path: raw=Path(path).read_bytes()
    else:
        request=urllib.request.Request(URL,headers={'Accept':'application/vnd.github.raw+json',
                                                     'User-Agent':'reality-whole-research/1.0'})
        with urllib.request.urlopen(request,timeout=60) as response:
            length=response.headers.get('Content-Length')
            if length and int(length)>SIZE: raise ValueError('download exceeds fixed budget')
            raw=response.read(SIZE+1)
    if len(raw)!=SIZE or hashlib.sha256(raw).hexdigest()!=SHA:
        raise ValueError('pinned workbook length or digest mismatch')
    wb=openpyxl.load_workbook(io.BytesIO(raw),read_only=True,data_only=True)
    if 'Data' not in wb.sheetnames: raise ValueError('missing Data sheet')
    iterator=wb['Data'].iter_rows(values_only=True)
    fields=next(iterator)
    if len(fields)!=len(set(fields)): raise ValueError('duplicate columns')
    if not {'Exp','SSID','Session','Trial','Feedback','StimInt','LIK'}.issubset(fields):
        raise ValueError('schema mismatch')
    records=[dict(zip(fields,row)) for row in iterator if any(x is not None for x in row)]
    wb.close()
    return records


def finite(v):
    return isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v)


def metrics(y,p,ids):
    y=np.asarray(y); p=np.asarray(p)
    if len(y)==0: raise ValueError('empty subset')
    errs=(y-p)**2; by=collections.defaultdict(list)
    for group,e in zip(ids,errs): by[group].append(float(e))
    corr=None if np.std(y)==0 or np.std(p)==0 else float(np.corrcoef(y,p)[0,1])
    return {'rows':len(y),'participants':len(by),'rmse':float(np.sqrt(np.mean(errs))),
            'participant_averaged_rmse':math.sqrt(np.mean([np.mean(v) for v in by.values()])),
            'mae':float(np.mean(np.abs(y-p))),'pearson_r':corr,
            'predictions_outside_1_to_5':int(((p<1)|(p>5)).sum())}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data',help='local exact pinned workbook (otherwise bounded GitHub download)')
    args=parser.parse_args(); original=load(args.data)
    rows=[]; persons={}; seen=set(); excluded_other_session=0; excluded_missing=0
    for r in original:
        exp=r['Exp']; id_=r['SSID']; session=r['Session']; fb=r['Feedback']; stim=r['StimInt']
        if exp not in GROUPS or not finite(id_) or int(id_)!=id_:
            raise ValueError('unexpected experiment or ID encoding')
        person=str(int(id_))
        if person in persons and persons[person]!=exp:raise ValueError('participant in both experiments')
        persons[person]=exp
        if session not in (1,2):raise ValueError('unexpected session')
        if session==1:
            if fb!='No Feedback':raise ValueError('unexpected session 1 feedback')
            excluded_other_session+=1;continue
        if fb not in FEEDBACK or stim not in LEVELS: raise ValueError('unexpected session 2 condition')
        if not all(finite(r[k]) for k in ('Trial','LIK')):
            excluded_missing+=1;continue
        trial=float(r['Trial']); y=float(r['LIK'])
        if y not in (1,2,3,4,5):raise ValueError('unexpected ordinal outcome')
        key=(person,trial)
        if key in seen:raise ValueError('duplicate participant/session 2 trial')
        seen.add(key)
        fold=int(hashlib.sha256((SALT+person).encode()).hexdigest(),16)%5
        rows.append({'person':person,'exp':exp,'fb':fb,'stim':stim,'trial':trial,'y':y,'fold':fold})
    n=len(rows); y=np.array([r['y'] for r in rows]); folds=np.array([r['fold'] for r in rows])
    groups=[r['person'] for r in rows]
    basis=np.array([[float(r['exp']==e and r['stim']==level) for e in GROUPS for level in LEVELS]
                    +[r['trial']*float(r['exp']==e) for e in GROUPS] for r in rows])
    features={}
    for name in ('unsigned','signed'):
        values=[]
        for r in rows:
            v= (int(r['fb']!='Congruent') if name=='unsigned'
                else {'Faster':1,'Slower':-1,'Congruent':0}[r['fb']])
            values.append([float(v)*float(r['exp']==e) for e in GROUPS])
        features[name]=np.array(values)
    pred={name:np.full(n,np.nan) for name in MODELS}; folds_summary=[]
    for k in range(5):
        test=folds==k; train=~test
        if not test.any() or not train.any():raise ValueError('empty fold')
        assert not (set(groups[i] for i in np.flatnonzero(test)) & set(groups[i] for i in np.flatnonzero(train)))
        for name,extra in MODELS.items():
            X=np.column_stack([basis]+[features[v] for v in extra])
            coef,_,rank,_=np.linalg.lstsq(X[train],y[train],rcond=None)
            if rank!=X.shape[1]:raise ValueError('training design rank deficient')
            pred[name][test]=X[test]@coef
        folds_summary.append({'fold':k,'rows':int(test.sum()),
             'participants':len(set(groups[i] for i in np.flatnonzero(test))),
             'participants_by_experiment':{e:len(set(rows[i]['person'] for i in np.flatnonzero(test) if rows[i]['exp']==e)) for e in GROUPS}})
    if not all(np.isfinite(p).all() for p in pred.values()):raise ValueError('nonfinite predictions')
    predictions={}
    for label in ('all',)+GROUPS:
        mask=np.array([label=='all' or r['exp']==label for r in rows])
        ids=[groups[i] for i in np.flatnonzero(mask)]
        predictions[label]={name:metrics(y[mask],p[mask],ids) for name,p in pred.items()}
        base=predictions[label]['baseline']['rmse']
        for data in predictions[label].values():data['rmse_difference_from_baseline']=data['rmse']-base
    # Fixed balanced summaries, no participant-level output.
    bycell=collections.defaultdict(list)
    for r in rows:bycell[(r['person'],r['stim'],r['fb'])].append(r['y'])
    summaries={}
    for exp in GROUPS:
        people=sorted(p for p,e in persons.items() if e==exp)
        complete=[]
        for p in people:
            if all(bycell[(p,level,fb)] for level in LEVELS for fb in FEEDBACK):
                means={fb:float(np.mean([np.mean(bycell[(p,level,fb)]) for level in LEVELS])) for fb in FEEDBACK}
                complete.append(means)
        if not complete: raise ValueError('no complete matched participants')
        summaries[exp]={'participants_source':len(people),'complete_participants':len(complete),
          'excluded_incomplete_participants':len(people)-len(complete),
          'complete_cells':len(complete)*len(LEVELS)*len(FEEDBACK),
          'mean_by_feedback':{fb:float(np.mean([r[fb] for r in complete])) for fb in FEEDBACK},
          'mean_faster_minus_slower':float(np.mean([r['Faster']-r['Slower'] for r in complete])),
          'mean_unsigned_minus_congruent':float(np.mean([(r['Faster']+r['Slower'])/2-r['Congruent'] for r in complete]))}
    receipt={'status':'completed',
      'scope':'exploratory participant-held-out reported unpleasantness prediction within published study; assigned labels not measured neural/channel mismatch',
      'source':{'url':URL,'commit':COMMIT,'sha256':SHA,'bytes':SIZE,'sheet':'Data'},
      'selection':{'source_rows':len(original),'excluded_session_one':excluded_other_session,
                   'excluded_missing_outcome_or_trial':excluded_missing,'feedback_rows':n,
                   'participants':len(set(groups)),'participants_by_experiment':{e:len({r['person'] for r in rows if r['exp']==e}) for e in GROUPS}},
      'folds':folds_summary,'out_of_fold':predictions,'descriptive_balanced_contrasts':summaries,
      'privacy':'Only aggregate results saved; individual identifiers and records are not output.',
      'protocol':'CARDIAC_FEEDBACK_PAIN_PREDICTION_PROTOCOL.md'}
    (ROOT/'verification/cardiac_feedback_pain_predictions.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
