#!/usr/bin/env python3
"""Exploratory dyad-to-chord transfer on public Bowling aggregate ratings.

Stimulus-side symbolic baselines; NOT neural frustration, pain, a preregistration,
or an independently sampled test cohort. Input and original source are pinned.
"""
import csv
import hashlib
import itertools
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'sources/external/dcmlab-consonance/bowling2018_consonance.tsv'
EXPECTED = 'd2d47991ca051c05ac556d55a35969af0a9de21219a60104a6093f5e4caceacc'
raw = DATA.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED
with DATA.open(newline='', encoding='utf-8') as f:
    rows = [{'pitches': tuple(sorted(map(int, row['pitches'].split(',')))),
             'rating': float(row['rating'])} for row in csv.DictReader(f, delimiter='\t')]
assert len(rows) == 298
by_size = {s: [r for r in rows if len(r['pitches']) == s] for s in (2,3,4)}
assert {s:len(v) for s,v in by_size.items()} == {2:12,3:66,4:220}

# Cross-check every symbolic chord/rating against the inconData transcription
# of the original supplement; the projects share provenance and are not independent studies.
source_files = {
    2: ('dyads.csv', 'f617e04b92feeb6a73a64a696163a9554d2cee578b81a40a190dd135708a5855'),
    3: ('triads.csv', 'd9210a546e06b83aae7109552a601304c647f6612ea2fba95b0219dae7462a20'),
    4: ('tetrads.csv', '4e3826af63c366c69d84947bd68bf1d38598a33ed3f2357230e858092f04f103'),
}
original = {}
for size, (name, checksum) in source_files.items():
    path = ROOT/'sources/external/incondata-bowling2018'/name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == checksum
    with path.open(newline='', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            key=tuple(int(row[f'pc_{i}']) for i in range(1,size+1))
            assert key not in original
            original[key]=row
for row in rows:
    p=row['pitches']; key=tuple(v-p[0] for v in p)
    assert key in original and abs(row['rating']-float(original[key]['rating_mean']))<1e-8
assert len(original)==len(rows)

def original_details(p):
    row=original[tuple(v-p[0] for v in p)]
    freq=[float(row[f'f_{i}']) for i in range(1,len(p)+1)]
    return {'reported_frequencies_hz': freq,
            'frequency_ratios_sorted': sorted(b/a for a,b in itertools.combinations(freq,2)),
            'published_harmonic_similarity': float(row['bowling_harm_sim'])}

# One observed dyad per semitone interval; no numerical calibration on triads
# or tetrads. Values are means of human ratings, not physical forces.
dyad = {p['pitches'][1]-p['pitches'][0]:p['rating'] for p in by_size[2]}
assert sorted(dyad) == list(range(1,13))

def intervals(p):
    return tuple(sorted(b-a for a,b in itertools.combinations(p,2)))

def predictions(p):
    values = [dyad[d] for d in intervals(p)]
    return statistics.mean(values), min(values)

def metric(y, z):
    assert len(y) == len(z) and len(y)>1
    diff = [a-b for a,b in zip(y,z)]
    sse = sum(v*v for v in diff)
    sst = sum((a-statistics.mean(y))**2 for a in y)
    return {'rmse': math.sqrt(sse/len(y)), 'mae': statistics.mean(map(abs,diff)),
            'pearson_r': statistics.correlation(y,z), 'r2_against_target_mean': 1-sse/sst,
            'mean_prediction': statistics.mean(z), 'mean_observed': statistics.mean(y)}

def group_heldout(y,x,keys):
    # Leave all chords sharing the held-out interval multiset out of the fit.
    pred=[]
    for k in keys:
        train=[j for j in range(len(y)) if keys[j] != k]
        xm=statistics.mean(x[j] for j in train); ym=statistics.mean(y[j] for j in train)
        v=sum((x[j]-xm)**2 for j in train)
        assert v>0
        slope=sum((x[j]-xm)*(y[j]-ym) for j in train)/v
        # same x and prediction for all chords having k
        i=keys.index(k)
        pred.append(ym+slope*(x[i]-xm))
    return metric(y,pred)

out = {'status':'completed',
       'status_detail':'exploratory, not preregistered or an independent participant cohort',
       'source_commit':'a13bcb0a52ac41cff9647e8b6406aed32a8250c6',
       'source_sha256':EXPECTED,
       'participants_reported_in_original':30,
       'upstream_transcription_commit':'b95b4db27356a04241ed1a2e38ffc8f5e1f68bbe',
       'cross_checked_chord_types_and_ratings':len(rows),
       'notes':'main predictors use symbolic interval distances, not measured acoustics, coupling, neural dynamics, or subjective pain',
       'dyad_counts':len(dyad),'data':{}}
for size in (3,4):
    data=by_size[size]; y=[r['rating'] for r in data]
    keys=[intervals(r['pitches']) for r in data]
    xmean=[predictions(r['pitches'])[0] for r in data]
    xmin=[predictions(r['pitches'])[1] for r in data]
    groups=defaultdict(list)
    for r,key in zip(data,keys): groups[key].append(r)
    sse_oracle=sum(sum((r['rating']-statistics.mean(t['rating'] for t in group))**2 for r in group)
                   for group in groups.values())
    sst=sum((z-statistics.mean(y))**2 for z in y)
    ties=[(max(r['rating'] for r in group)-min(r['rating'] for r in group), key, group)
          for key,group in groups.items() if len(group)>1]
    ties.sort(key=lambda v:(-v[0], v[1]))
    gap,key,group=ties[0]
    out['data'][str(size)]={
        'chord_count':len(data),
        'pairwise_mean_direct':metric(y,xmean),
        'pairwise_min_direct':metric(y,xmin),
        'pairwise_mean_group_heldout_affine_calibration':group_heldout(y,xmean,keys),
        'pairwise_min_group_heldout_affine_calibration':group_heldout(y,xmin,keys),
        'multiset_classes':len(groups),
        'classes_with_multiple_chords':len(ties),
        'oracle_multiset_only_rmse':math.sqrt(sse_oracle/len(y)),
        'oracle_multiset_only_sse_fraction':sse_oracle/sst,
        'oracle_caveat':'in-sample mathematical lower bound based on these observed means; not predictive or a noise-corrected estimate',
        'largest_within_multiset_gap':{'interval_multiset':key,'gap':gap,
            'chords':[{'pitches':r['pitches'],'rating':r['rating'],
                       **original_details(r['pitches'])} for r in group]},
    }
# The selected example must really collide under *both* symbolic rules while
# the target averages differ; no claim of physical or statistical matching.
triad_a = next(r for r in by_size[3] if r['pitches'] == (56,58,64))
triad_b = next(r for r in by_size[3] if r['pitches'] == (55,61,63))
assert intervals(triad_a['pitches']) == intervals(triad_b['pitches']) == (2,6,8)
assert predictions(triad_a['pitches']) == predictions(triad_b['pitches'])
assert abs(triad_a['rating']-triad_b['rating']) > 0.86
# On the dyads, the two candidate rules equal the source rating by construction.
for row in by_size[2]:
    a,b=predictions(row['pitches'])
    assert a == b == row['rating']
outfile=ROOT/'verification/bowling_pairwise_transfer_audit.json'
outfile.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
