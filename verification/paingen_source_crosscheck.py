#!/usr/bin/env python3
"""Cross-check two shared-provenance PAINgen exports, aggregate receipt only."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parent.parent
COMMIT='da46f2f9739ad2e9eeb9658711582be6357c1026'
FILES={
 'behavior':('merged_firstlvl_stim_betas_to_share.csv',431317,'b40b4a1b1e001f2317fea07a49c6ee6de062f181a20affe149fe50a81b58545b'),
 'brain':('pain_evoked_brain_measures.csv',3728915,'0eda58e9f8f83ec5294e92c907babfc771c0172ef22706e0be52c7182dbe8f56')}

def obtain(name,path):
    filename,size,sha=FILES[name]
    if path:
        raw=Path(path).read_bytes()
    else:
        url=f'https://api.github.com/repos/rotemb9/paingen-placebo-fmri-paper/contents/{filename}?ref={COMMIT}'
        req=urllib.request.Request(url,headers={'User-Agent':'SEEP-provenance-audit/1.0','Accept':'application/vnd.github.raw+json'})
        with urllib.request.urlopen(req,timeout=60) as f:
            length=f.headers.get('Content-Length')
            if length is not None and int(length)>size:raise ValueError('source exceeds declared size')
            raw=f.read(size+1)
    if len(raw)!=size or hashlib.sha256(raw).hexdigest()!=sha:raise ValueError('source size or digest mismatch')
    return list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'),newline='')))

def numeric(v):
    try: val=float(v)
    except (ValueError,TypeError):return None
    return val if math.isfinite(val) else None

def bkey(r):
    return (r['participant_ID'],int(float(r['heat'])),int(float(r['stimLvl'])),int(float(r['prodicaine'])))

def mkey(r):
    h,level,placebo=(float(r[k]) for k in ('heat','stimLvl','prodicaine'))
    assert h in (-.5,.5) and level in (-.5,0,.5) and placebo in (-.5,.5)
    return r['participant_ID'],int(h+.5),int(2*level+4),int(placebo+.5)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--behavior',help='path to pinned behavioral CSV')
    p.add_argument('--brain',help='path to pinned brain-measures CSV')
    args=p.parse_args()
    behavior=obtain('behavior',args.behavior); brain=obtain('brain',args.brain)
    indexed={}
    for r in behavior:
        k=bkey(r)
        if k in indexed: raise ValueError('duplicate behavior participant-condition key')
        indexed[k]=r
    seen=set(); comparisons=0; identical=0
    for r in brain:
        k=mkey(r)
        if k in seen:raise ValueError('duplicate brain participant-condition key')
        seen.add(k)
        if k not in indexed:raise ValueError('brain participant-condition missing in behavioral export')
        for name in ('Yint','Yunp'):
            a,b=numeric(r[name]),numeric(indexed[k][name]); comparisons+=1
            if (a is None and b is None) or (a is not None and b is not None and abs(a-b)<=1e-12):
                identical+=1
            else: raise ValueError('rating mismatch in corresponding row')
    result={'status':'completed', 'source_commit':COMMIT,'source_hashes':{k:v[2] for k,v in FILES.items()},
            'behavior_rows':len(behavior),'brain_rows':len(brain),'brain_rows_matched_to_behavior':len(seen),
            'behavior_rows_without_brain_row':len(indexed)-len(seen),
            'rating_fields_compared_including_joint_missing':comparisons,'matching_fields':identical,
            'scope':'shared-provenance processing check; not an independent study, original scan analysis, primary raw-trial verification, or privacy certification',
            'privacy':'No participant IDs, data rows, family relations or demographic values included in this receipt.'}
    (ROOT/'verification/paingen_source_crosscheck.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
