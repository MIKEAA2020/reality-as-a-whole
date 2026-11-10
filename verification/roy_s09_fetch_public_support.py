#!/usr/bin/env python3
"""Boundedly fetch pinned, publicly shared S09 support files using gh.

Pass a private cache directory, NOT a public Git repository: the Git tree can
contain sensitive-looking original filenames and movement series are raw data.
Does not download the original 606 MB subject archive or any MRI/EEG images.
"""
import argparse
import base64
import hashlib
import json
import re
import subprocess
from pathlib import Path

REPO='Aubrey-Lyu/BR-project'
COMMIT='b8ca204024a4f7151645c6c2e908eb564203ac66'
PREFIX='data/rivalry_fMRI_head_motion_files/S09/'
MAX_TOTAL=1_000_000


def api(endpoint):
    return json.loads(subprocess.check_output(['gh','api',endpoint]))


def fetch(destination):
    tree=api(f'repos/{REPO}/git/trees/{COMMIT}?recursive=1')
    if tree.get('truncated') or tree.get('sha') != COMMIT:
        raise ValueError('Unexpected or incomplete tree')
    selected={}
    for remote, local in [('info_scans_conditions.m','info_scans_conditions.m'),
                          ('data/rival_ind.mat','rival_ind.mat'),
                          ('data/replay_smooth_ind.mat','replay_smooth_ind.mat')]:
        found=[x for x in tree['tree'] if x['type']=='blob' and x['path']==remote]
        if len(found)!=1: raise ValueError('Missing condition source')
        selected[local]=found[0]
    for x in tree['tree']:
        if x['type']!='blob' or not x['path'].startswith(PREFIX): continue
        m=re.search(r'/scan([1-9])/',x['path']); ext=x['path'].rsplit('.',1)[-1]
        if not m or ext not in ('txt','mat'): raise ValueError('Unexpected motion tree')
        local=f'motion/scan{m.group(1)}.{ext}'
        if local in selected: raise ValueError('Duplicate motion entry')
        selected[local]=x
    if len(selected)!=21 or sum(x['size'] for x in selected.values())>MAX_TOTAL:
        raise ValueError('Unexpected support count or size')
    destination.mkdir(parents=True,exist_ok=True)
    (destination/'tree.json').write_text(json.dumps(tree,indent=2)+'\n')
    for local, entry in sorted(selected.items()):
        blob=api(f"repos/{REPO}/git/blobs/{entry['sha']}")
        payload=base64.b64decode(blob['content'],validate=False)
        if len(payload)!=entry['size'] or hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest()!=entry['sha']:
            raise ValueError('Blob integrity mismatch')
        path=destination/local;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(payload)
    print(f'Fetched {len(selected)} verified support blobs, excluding MRI/EEG images')


def main():
    p=argparse.ArgumentParser();p.add_argument('private_cache',type=Path);args=p.parse_args();fetch(args.private_cache)


if __name__=='__main__': main()
