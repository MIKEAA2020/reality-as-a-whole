#!/usr/bin/env python3
"""Compare two previously computed hypothetical offset sensitivities.

All numeric contrasts are differences of descriptive Pearson correlations,
not effect sizes, statistical tests or evidence of different task conditions.
The 18x18 grid assumes each scan's offset can vary independently.
"""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare(path1,path2):
    a=json.loads(path1.read_text()); b=json.loads(path2.read_text())
    def values(x):
        rows=x['all_candidates']
        starts=[int(y['first_trigger_frame']) for y in rows]
        if len(starts)!=len(set(starts)):
            raise ValueError('Duplicate candidate offset')
        return {int(y['first_trigger_frame']):float(y['pearson_r']) for y in rows}
    a,b=values(a),values(b)
    if not a or not b:
        raise ValueError('Empty candidate set')
    grid=[v-u for u in a.values() for v in b.values()]
    same=[b[k]-a[k] for k in sorted(a.keys() & b.keys())]
    def stats(v):
        if not v: return None
        return {'count':len(v),'min':min(v),'max':max(v),
                'negative':sum(x<0 for x in v),'zero':sum(x==0 for x in v),
                'positive':sum(x>0 for x in v)}
    return {'kind':'exploratory offset-dependent difference of correlations; not a condition effect',
        'input_1_sha256':digest(path1),'input_2_sha256':digest(path2),
        'independent_offset_grid':stats(grid), 'same_offset_sensitivity_only':stats(same),
        'limitations':['No true offset is established. Same-offset comparison is an extra unverified assumption.',
            'These are differences of crude whole-field correlations, not contrasts from a fitted fMRI GLM.',
            'Offsets are not selected using the resulting correlation or contrast.']}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('scan1_sensitivity',type=Path);p.add_argument('scan2_sensitivity',type=Path)
    a=p.parse_args()
    print(json.dumps(compare(a.scan1_sensitivity,a.scan2_sensitivity),indent=2,allow_nan=False))


if __name__=='__main__': main()
