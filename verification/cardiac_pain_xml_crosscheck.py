#!/usr/bin/env python3
"""Independent XLSX-XML read of aggregate descriptive cardiac feedback results."""
import argparse
import collections
import hashlib
import io
import json
import math
import posixpath
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
SHA='c186908c35e4819d2ea094fa339b4a9fc691556b13dc62585d12d09c6041bb02'
SIZE=537743
URL=('https://api.github.com/repos/EP171993/painperception/contents/'
     'Data_v3%20-%202504.xlsx?ref=c1c8721f0e3d00fefc602ed32b84e24c218c56d3')
N={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
   'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
   'p':'http://schemas.openxmlformats.org/package/2006/relationships'}


def raw_file(path):
    if path:raw=Path(path).read_bytes()
    else:
        request=urllib.request.Request(URL,headers={'Accept':'application/vnd.github.raw+json','User-Agent':'pain-xml-source-crosscheck/1'})
        with urllib.request.urlopen(request,timeout=60) as f:
            length=f.headers.get('Content-Length')
            if length and int(length)>SIZE:raise ValueError('source exceeds budget')
            raw=f.read(SIZE+1)
    if len(raw)!=SIZE or hashlib.sha256(raw).hexdigest()!=SHA:raise ValueError('source size or digest mismatch')
    return raw


def column_number(ref):
    n=0
    for c in ref:
        if not c.isalpha():break
        n=n*26+ord(c.upper())-ord('A')+1
    return n-1


def parse_xlsx(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        workbook=ET.fromstring(z.read('xl/workbook.xml'))
        sheet=next(s for s in workbook.findall('m:sheets/m:sheet',N) if s.attrib['name']=='Data')
        relation=sheet.attrib['{'+N['r']+'}id']
        rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        target=next(r.attrib['Target'] for r in rels.findall('p:Relationship',N) if r.attrib['Id']==relation)
        target=target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/'+target)
        shared_root=ET.fromstring(z.read('xl/sharedStrings.xml'))
        shared=[''.join(node.itertext()) for node in shared_root.findall('m:si',N)]
        xml=ET.fromstring(z.read(target))
        for row in xml.findall('m:sheetData/m:row',N):
            result={}
            for cell in row.findall('m:c',N):
                i=column_number(cell.attrib['r']); val=cell.find('m:v',N)
                if val is None:continue
                v=val.text
                result[i]=shared[int(v)] if cell.attrib.get('t')=='s' else float(v)
            if result:yield result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data');args=p.parse_args()
    rows=iter(parse_xlsx(raw_file(args.data))); header=next(rows); columns={v:k for k,v in header.items()}
    needed=('Exp','SSID','Session','Feedback','StimInt','LIK')
    if not set(needed).issubset(columns):raise ValueError('missing column')
    cells=collections.defaultdict(list); counts=collections.Counter(); nsource=0
    for row in rows:
        nsource+=1
        def get(name):return row.get(columns[name])
        if get('Session')!=2:continue
        exp,person,level,fb,y=(get(k) for k in ('Exp','SSID','StimInt','Feedback','LIK'))
        if exp not in ('Intero','Extero') or fb not in ('Congruent','Faster','Slower') or level not in (2,3,4) or y not in (1,2,3,4,5):
            raise ValueError('unexpected encoding')
        cells[(exp,person,int(level),fb)].append(y);counts[exp]+=1
    expected=json.loads((ROOT/'verification/cardiac_feedback_pain_predictions.json').read_text())
    assert nsource==expected['selection']['source_rows']
    matched=0; output={}
    for exp in ('Intero','Extero'):
        people={p for e,p,level,fb in cells if e==exp}
        assert counts[exp]==expected['out_of_fold'][exp]['baseline']['rows']
        assert all(len(cells[(exp,p,level,fb)])==2 for p in people for level in (2,3,4) for fb in ('Congruent','Faster','Slower'))
        means={fb:sum(sum(cells[(exp,p,level,fb)]) for p in people for level in (2,3,4))/(len(people)*6)
               for fb in ('Congruent','Slower','Faster')}
        previous=expected['descriptive_balanced_contrasts'][exp]
        for fb,v in means.items():
            if not math.isclose(v,previous['mean_by_feedback'][fb],abs_tol=1e-12):raise AssertionError('crosscheck differs')
            matched+=1
        contrasts={'faster_minus_slower':means['Faster']-means['Slower'],
                   'unsigned_minus_congruent':(means['Faster']+means['Slower'])/2-means['Congruent']}
        assert math.isclose(contrasts['faster_minus_slower'],previous['mean_faster_minus_slower'],abs_tol=1e-12)
        assert math.isclose(contrasts['unsigned_minus_congruent'],previous['mean_unsigned_minus_congruent'],abs_tol=1e-12)
        matched+=2
        output[exp]={'rows':counts[exp],'participants':len(people),'means_and_contrasts_matched':5}
    result={'status':'completed','source_sha256':SHA,'source_rows':nsource,'groups':output,
      'aggregate_checks_matched':matched,
      'scope':'independent XML decoding cross-check of aggregates from the same workbook; not an independent sample or a check of prediction fit',
      'privacy':'No participant identifiers or participant-level values are stored.'}
    (ROOT/'verification/cardiac_pain_xml_crosscheck.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
