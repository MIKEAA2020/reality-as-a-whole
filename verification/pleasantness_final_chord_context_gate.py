#!/usr/bin/env python3
"""Fixed retrospective matched-final-chord analysis; see companion plan.

Read pinned private-local copies of public inputs; output only aggregate stats.
Requires pyreadstat (tested 1.3.2) with output_format='dict'.
"""
import csv
import hashlib
import json
import math
import random
import statistics
from pathlib import Path
import pyreadstat

ROOT = Path('.arena/penultimate')
HASHES = {'PleDisso1.sav':'60f2a03bd08a760952d4a2223c0057b5f428d6a81acddc62407e6f3d51d7abf6',
          'stimulusTable.csv':'e7459d0b1374ab417a301e54ee3a77ef2e30a109ade29db4274ace053cba9136'}

def qtile(items,p):
    x=sorted(items); k=(len(x)-1)*p; i=int(k); j=min(i+1,len(x)-1)
    return x[i]+(k-i)*(x[j]-x[i])

def is_missing(x):
    return x is None or (isinstance(x,float) and not math.isfinite(x))

def avg(xs): return statistics.mean(xs)

def main():
    for name,digest in HASHES.items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
            raise ValueError('hash mismatch: '+name)
    with (ROOT/'stimulusTable.csv').open(newline='') as f:
        stim=list(csv.DictReader(f))
    if len(stim)!=56 or len(set(x['stimTrans'] for x in stim))!=7: raise ValueError('stimulus layout')
    for j,x in enumerate(stim):
        if x['stimTrans']!=stim[(j//8)*8]['stimTrans'] or x['stimType'] not in {'HRHF_1','HRHF_2','HRLF_1','HRLF_2','LRHF_1','LRHF_2','LRLF_1','LRLF_2'}:
            raise ValueError('unexpected stimulus table')
    D,_=pyreadstat.read_sav(str(ROOT/'PleDisso1.sav'),output_format='dict')
    fields=('id','Question','Rating','Roughness','Familiarity')
    people={}; missing_rows=0
    for i in range(len(D['id'])):
        vals=[D[f][i] for f in fields]
        if any(is_missing(v) for v in vals):
            missing_rows+=1; continue
        ident,question,rating,rough,fam=vals
        if not (question==int(question) and 1<=question<=56 and rating==int(rating) and 1<=rating<=7 and rough in (1,2) and fam in (1,2)):
            raise ValueError('invalid question/rating/factors')
        q=int(question); typ=stim[q-1]['stimType']
        expected=('H' if rough==2 else 'L')+'R'+('H' if fam==2 else 'L')+'F'
        if not typ.startswith(expected): raise ValueError('feature mapping mismatch')
        person=people.setdefault(ident,{})
        if q in person: raise ValueError('duplicate participant question')
        person[q]=float(rating)
    complete=[p for p in people.values() if len(p)==56]
    incomplete=len(people)-len(complete)
    if not complete: raise ValueError('no complete people')
    cellnames=('LRLF','LRHF','HRLF','HRHF')
    cells=[]
    for p in complete:
        c={name:avg(p[q] for q in range(1,57) if stim[q-1]['stimType'].startswith(name)) for name in cellnames}
        cells.append(c)
    def contrasts(c):
        return {'familiarity_high_minus_low':(c['LRHF']+c['HRHF']-c['LRLF']-c['HRLF'])/2,
                'roughness_high_minus_low':(c['HRLF']+c['HRHF']-c['LRLF']-c['LRHF'])/2,
                'roughness_high_minus_low_at_low_familiarity':c['HRLF']-c['LRLF'],
                'roughness_high_minus_low_at_high_familiarity':c['HRHF']-c['LRHF']}
    pp=[contrasts(c) for c in cells]; names=list(pp[0]); rng=random.Random(9381)
    boot={n:[] for n in names}
    for _ in range(10000):
        draw=[pp[rng.randrange(len(pp))] for _ in pp]
        for n in names: boot[n].append(avg(v[n] for v in draw))
    summaries={n:{'mean':avg(v[n] for v in pp),'bootstrap_95_percentile':[qtile(boot[n],.025),qtile(boot[n],.975)]} for n in names}
    grand=avg(v for p in complete for v in p.values())
    denom=sum((v-grand)**2 for p in complete for v in p.values())
    residual=0.
    for p in complete:
        for k in range(7):
            vs=[p[q] for q in range(k*8+1,k*8+9)]; m=avg(vs)
            residual+=sum((v-m)**2 for v in vs)
    stimmeans=[avg(p[q] for p in complete) for q in range(1,57)]
    mean_res=0.
    for k in range(7):
        vs=stimmeans[k*8:(k+1)*8]; m=avg(vs)
        mean_res+=sum((v-m)**2 for v in vs)
    out={'source_commit':'010777ada95da0044492d14865a162d7bc2874f8', 'input_sha256':HASHES,
         'source_rows':len(D['id']),'rows_missing_required_fields':missing_rows,'complete_people':len(complete),
         'incomplete_people_dropped':incomplete,'retained_ratings':len(complete)*56,
         'cell_means':{n:avg(c[n] for c in cells) for n in cellnames},'contrasts':summaries,
         'in_sample_person_key_oracle_rmse':math.sqrt(residual/(len(complete)*56)),
         'in_sample_person_key_oracle_fraction_of_total_squares':residual/denom,
         'across_person_means_context_within_key_rmse':math.sqrt(mean_res/56),
         'bootstrap_replicates':10000,'seed':9381,
         'scope':'Fixed selected sequences, exploratory; ratings are not internal state or identity assays.'}
    Path('verification/pleasantness_final_chord_context_gate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
