#!/usr/bin/env python3
"""Offline fake-GitHub tests: bounded selection and blob verification."""
import base64
import hashlib
import tempfile
from pathlib import Path
from unittest.mock import patch
import roy_s09_fetch_public_support as fetcher


def main():
    tree=[]; responses={}
    def add(remote, payload):
        h=hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest()
        tree.append({'type':'blob','path':remote,'sha':h,'size':len(payload)})
        responses[h]={'content':base64.b64encode(payload).decode()}
    for i,p in enumerate(('info_scans_conditions.m','data/rival_ind.mat','data/replay_smooth_ind.mat')):
        add(p,bytes([i+1]))
    for n in range(1,10):
        for ext in ('txt','mat'):
            add(f'{fetcher.PREFIX}scan{n}/synthetic.{ext}',f'{n}{ext}'.encode())
    def fake_api(url):
        return {'sha':fetcher.COMMIT,'truncated':False,'tree':tree} if '/git/trees/' in url else responses[url.rsplit('/',1)[-1]]
    with tempfile.TemporaryDirectory() as tmp, patch.object(fetcher,'api',side_effect=fake_api):
        out=Path(tmp)/'private';fetcher.fetch(out)
        assert (out/'motion/scan9.txt').read_bytes()==b'9txt'
        assert len(list((out/'motion').iterdir()))==18
        tree.append(tree[-1])
        try: fetcher.fetch(out)
        except ValueError: pass
        else: raise AssertionError('Duplicate motion file must stop')
    print('PASS: synthetic pinned tree, verified blobs and duplicate stop')


if __name__=='__main__': main()
