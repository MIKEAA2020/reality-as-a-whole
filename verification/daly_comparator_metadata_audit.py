#!/usr/bin/env python3
"""Read pinned public event metadata and exercise a pinned external parser, not EEG."""
import ast
import csv
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd

BASE = Path('.arena/daly103/ds002721-3972f19d2846be4f283fe21c7fe39a1a11efda99')
UPSTREAM = Path('.arena/music-pipeline/run_ds002721_v2_0.py')
OUT = Path('verification/daly_comparator_metadata_audit.json')
UPSTREAM_SHA = 'a3f7c1d70a4494faa5689589acae061e8d461d505c400d00fb4e1381544850e2'
EVENT_MANIFEST_SHA = 'c026a6bee732bf4eea5e8b60ba2a03d526e05a49b2b2b72ec87df1fbc44c22e7'
PATTERN = re.compile(r'^sub-(\d+)_task-run([2-5])_events\.tsv$')


def make_parser():
    source = UPSTREAM.read_bytes()
    if hashlib.sha256(source).hexdigest() != UPSTREAM_SHA:
        raise ValueError('Unexpected upstream parser file hash')
    parsed = ast.parse(source)
    wanted = [n for n in parsed.body if isinstance(n,(ast.ClassDef,ast.FunctionDef))
              and n.name in ('TrialSpec','parse_events')]
    if len(wanted) != 2:
        raise ValueError('Unexpected parser schema')
    env = {'dataclass': dataclass, 'Path': Path, 'math': math, 'np': np,
           'QUESTION_CODES': {'pleasantness': 800,'energy':801,'tension':802},
           'ALL_QUESTION_CODES': set(range(800,808))}
    exec(compile(ast.Module(body=wanted, type_ignores=[]),str(UPSTREAM),'exec'),env)
    return env


def audit_rows(events):
    # Event rows are (timestamp, code, duration); no same-time order presumed here.
    events = sorted(events)
    starts = [(t,d) for t,c,d in events if c == 788]
    counts = Counter()
    offsets = {'first_question_after_start': [], 'first_response_after_start': []}
    for idx,(t,d) in enumerate(starts):
        end = starts[idx+1][0] if idx+1 < len(starts) else math.inf
        counts['music_starts'] += 1
        counts['start_duration_20'] += int(d == 20)
        counts['next_music_start_within_20'] += int(end < t+20)
        interval = [(x,c) for x,c,_ in events if t <= x < end]
        is_q = lambda c: 800 <= c <= 807
        is_r = lambda c: 901 <= c <= 909 or 833 <= c <= 841
        for width in (12,20):
            for name,pred in (('question',is_q),('answer_or_response',is_r)):
                counts[f'{name}_within_{width}s_including_start'] += int(any(t <= x < t+width and pred(c) for x,c in interval))
                counts[f'{name}_within_{width}s_strictly_after_start'] += int(any(t < x < t+width and pred(c) for x,c in interval))
        for name,pred in (('first_question_after_start',is_q),('first_response_after_start',is_r)):
            candidates = [x-t for x,c in interval if t < x and pred(c)]
            if candidates: offsets[name].append(min(candidates))
        groups = defaultdict(set)
        for x,c in interval:
            if t < x < end: groups[x].add(c)
        disagree=False
        for values in groups.values():
            q=[c for c in values if is_q(c)]
            a=[c for c in values if 901<=c<=909]
            b=[c for c in values if 833<=c<=841]
            if len(q)==len(a)==len(b)==1:
                same=(a[0]-900)==(b[0]-832)
                counts['one_q_one_answer_one_response_timestamps']+=1
                counts['triples_equal' if same else 'triples_unequal']+=1
                disagree |= not same
        counts['intervals_with_unequal_triple']+=int(disagree)
    return counts, offsets


def same(a,b):
    return (isinstance(a,float) and isinstance(b,float) and math.isnan(a) and math.isnan(b)) or a == b


def main():
    env=make_parser()
    parse=env['parse_events']
    paths=sorted(p for p in BASE.glob('sub-*/eeg/*_events.tsv') if PATTERN.match(p.name))
    if len(paths)!=124: raise ValueError(f'Expected 124 event files, got {len(paths)}')
    total=Counter(); offsets=defaultdict(list); diffs=Counter(); hashes={}
    nonmissing=Counter()
    for p in paths:
        m=PATTERN.match(p.name); sub,run=m.groups()
        hashes[str(p.relative_to(BASE))]=hashlib.sha256(p.read_bytes()).hexdigest()
        with p.open(newline='') as f:
            rows=list(csv.DictReader(f,delimiter='\t'))
        ev=[(float(r['onset']),int(r['trial_type']),float(r['duration'])) for r in rows]
        c,os=audit_rows(ev);total.update(c)
        for name,vals in os.items(): offsets[name].extend(vals)
        df=pd.DataFrame(rows)
        df['onset']=pd.to_numeric(df['onset'])
        original=df.copy()
        order=sorted(range(len(df)),key=lambda i:(float(df.iloc[i]['onset']),-i))
        reversed_ties=df.iloc[order].reset_index(drop=True)
        outputs=[]
        for frame in (original,reversed_ties):
            env['pd']=SimpleNamespace(read_csv=lambda *a, _frame=frame, **kw: _frame.copy(),
                                      to_numeric=pd.to_numeric,concat=pd.concat)
            outputs.append(parse(p,'sub-'+sub,'run'+run))
        if len(outputs[0]) != len(outputs[1]): raise ValueError('Music start count changed')
        for a,b in zip(*outputs):
            if a.onset != b.onset: raise ValueError('Start alignment changed')
            if a.stimulus_id.isdigit():
                code=int(a.stimulus_id)
                nonmissing['stimulus_documented_301_360'] += int(301 <= code <= 360)
                nonmissing['stimulus_other_300_699'] += int(not 301 <= code <= 360)
            else:
                nonmissing['stimulus_fallback_id'] += 1
            any_rating=False
            for attr in ('pleasantness','energy','tension'):
                v1,v2=getattr(a,attr),getattr(b,attr)
                nonmissing[attr]+=int(not math.isnan(v1))
                different=not same(v1,v2)
                diffs[attr+'_changed']+=int(different)
                if different:
                    kind = 'numeric_to_numeric' if math.isfinite(v1) and math.isfinite(v2) else 'one_missing'
                    diffs[attr+'_'+kind] += 1
                any_rating |= different
            diffs['any_target_changed']+=int(any_rating)
            diffs['stimulus_id_changed']+=int(a.stimulus_id != b.stimulus_id)
    digest=hashlib.sha256(json.dumps(hashes,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if digest != EVENT_MANIFEST_SHA: raise ValueError('Input events differ from previously audited manifest')
    summary={}
    for name,values in offsets.items():
        values.sort()
        summary[name]={'n':len(values),'min_seconds':round(values[0],3),
                       'median_seconds':round(float(np.median(values)),3),
                       'max_seconds':round(values[-1],3)}
    receipt={'scope':'event metadata and upstream parser sensitivity only; no EEG replay',
             'dataset_version':'1.0.3', 'dataset_commit':'3972f19d2846be4f283fe21c7fe39a1a11efda99',
             'upstream_commit':'634fa01848731ad2d5c88f6b3483b48dc9ba8725',
             'upstream_source_sha256':UPSTREAM_SHA,'event_manifest_sha256':digest,
             'files':len(paths),'counts':dict(sorted(total.items())),
             'first_positive_offsets':summary,'upstream_original_nonmissing':dict(sorted(nonmissing.items())),
             'upstream_tie_reverse_differences':dict(sorted(diffs.items())),
             'environment':{'python':sys.version.split()[0],'numpy':np.__version__,'pandas':pd.__version__}}
    OUT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2,sort_keys=True))

if __name__=='__main__': main()
