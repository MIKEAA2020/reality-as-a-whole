#!/usr/bin/env python3
"""Bounded, metadata-only cross-modal readiness audit; no EEG or subject identities."""
import argparse,csv,hashlib,io,json,math,re,tarfile
from collections import Counter,defaultdict
from decimal import Decimal
from pathlib import Path

COMMIT='3252827891885aa1890e6b1531a2d3aeefeaa5fd'
ROOT_TREE='5243c0dec6dd0d47f06a4e218255c0a0a6121220'
EXPECTED=['t01/p50','t02/p150','t03/p100','t04/p50','t05/p150','t06/p100','t07/p150','t08/p50','t09/p100','t10/end']
TASKS=('audioactive','thermalactive')
EVENT=re.compile(r'^(sub-\d+)/eeg/\1_task-(audioactive|thermalactive)_events\.tsv$')
EEGJSON=re.compile(r'^(sub-\d+)/eeg/\1_task-(audioactive|thermalactive)_eeg\.json$')

def blob_id(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def finite(v):
 try:
  x=float(v)
  if math.isfinite(x):return x
 except (ValueError,TypeError):pass
 return None

def inspect_event(b):
 reader=csv.DictReader(io.StringIO(b.decode('utf-8-sig')),delimiter='\t')
 required={'onset','duration','sample','trial_type','value'}
 if not reader.fieldnames or not required.issubset(reader.fieldnames):return {'schema_ok':False}
 rows=list(reader)
 if len(rows)>50:return {'schema_ok':False}
 onsets=[finite(r['onset']) for r in rows];samples=[finite(r['sample']) for r in rows]
 valid=all(x is not None and x>=0 for x in onsets) and all(x is not None and x>=0 and x.is_integer() for x in samples)
 increasing=valid and all(a<b for a,b in zip(onsets,onsets[1:]))
 sample_differences=[abs(s-1000*o) for s,o in zip(samples,onsets)] if valid else []
 return {'schema_ok':True,'row_count':len(rows),'sequence_ok':[r['trial_type'] for r in rows]==EXPECTED,
         'time_valid':bool(increasing),'max_sample_onset_difference':max(sample_differences,default=None)}

def mean_floor():
 a=list(map(Decimal,['28.11','64.76','111.00']));b=list(map(Decimal,['30.62','86.08','157.99']))
 dif=[y-x for x,y in zip(a,b)]
 return {'thermal_mean':[str(x) for x in a],'auditory_mean':[str(x) for x in b],
         'auditory_minus_thermal':[str(x) for x in dif],
         'equal_output_oracle_rmse_over_six_published_means':float((sum(x*x for x in dif)/Decimal(12)).sqrt()),
         'scope':'published rounded group means, not individual pairs, statistics or empirical physical mismatch'}

def run(treepath,archivepath):
 tree=json.loads(Path(treepath).read_text());
 if tree.get('truncated') is not False or tree.get('sha')!=ROOT_TREE:raise ValueError('wrong or truncated tree')
 items={x['path']:x for x in tree['tree']};member_by_path={};need={p for p in items if EVENT.fullmatch(p) or EEGJSON.fullmatch(p)}
 raw=Path(archivepath).read_bytes()
 if len(raw)>15_000_000:raise ValueError('archive cap')
 prefix='ds008349-'+COMMIT+'/'
 with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tar:
  for m in tar:
   if m.name == prefix[:-1] and m.isdir():continue
   if not m.name.startswith(prefix):raise ValueError('unexpected archive prefix')
   p=m.name[len(prefix):]
   if p not in need:continue
   if not m.isfile() or m.size>20_000:raise ValueError('unexpected type/size')
   if p in member_by_path:raise ValueError('duplicate')
   b=tar.extractfile(m).read()
   if blob_id(b)!=items[p]['sha']:raise ValueError('git blob mismatch')
   member_by_path[p]=b
 if set(member_by_path)!=need:raise ValueError('archive missing checked inputs')
 groups={task:Counter() for task in TASKS};subjects={task:set() for task in TASKS};sidecar_subjects={task:set() for task in TASKS};max_diff={t:0. for t in TASKS};sidecars={t:Counter() for t in TASKS}
 for path,b in member_by_path.items():
  m=EVENT.fullmatch(path)
  if m:
   sub,task=m.groups();subjects[task].add(sub);r=inspect_event(b);c=groups[task];c['files']+=1
   if not r['schema_ok']:c['schema_fail']+=1;continue
   for key in ('sequence_ok','time_valid'):c[key]+=int(r[key])
   c['total_rows']+=r['row_count']
   if r['max_sample_onset_difference'] is not None:max_diff[task]=max(max_diff[task],r['max_sample_onset_difference'])
  else:
   m=EEGJSON.fullmatch(path);sub,task=m.groups();v=json.loads(b)
   sidecars[task]['files']+=1
   sidecars[task]['sampling_1000']+=int(v.get('SamplingFrequency')==1000)
   sidecar_subjects[task].add(sub)
 counts={}
 for task in TASKS:
  rating_re=re.compile(r'^(sub-\d+)/eeg/\1_task-'+task+r'_stim\.tsv\.gz$')
  eeg_re=re.compile(r'^(sub-\d+)/eeg/\1_task-'+task+r'_eeg\.eeg$')
  counts[task]={'event_checks':dict(groups[task]),'event_subjects':len(subjects[task]),
    'eeg_sidecars':dict(sidecars[task]),'event_subjects_with_matching_eeg_sidecar':len(subjects[task]&sidecar_subjects[task]),
    'maximum_sample_onset_difference_samples_at_1khz':max_diff[task],
    'rating_paths':sum(bool(rating_re.fullmatch(p)) for p in items),
    'rating_paths_symlink':sum(bool(rating_re.fullmatch(p)) and x.get('mode')=='120000' for p,x in items.items()),
    'eeg_paths':sum(bool(eeg_re.fullmatch(p)) for p in items),
    'eeg_paths_symlink':sum(bool(eeg_re.fullmatch(p)) and x.get('mode')=='120000' for p,x in items.items())}
 return {'dataset_commit':COMMIT,'source_archive_sha256':hashlib.sha256(raw).hexdigest(),
         'tree_entries':len(items),'archive_bytes':len(raw),'checked_git_blobs':len(need),
         'tasks':counts,'subjects_with_both_event_files':len(subjects[TASKS[0]] & subjects[TASKS[1]]),
         'published_mean_comparison':mean_floor(),
         'scope':'metadata-only, no EEG, continuous rating data, physical mismatch or experiential bridge'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--tree',default='.arena/ds008349/tree.json');p.add_argument('--archive',default='.arena/ds008349/archive.tar.gz');a=p.parse_args()
 text=json.dumps(run(a.tree,a.archive),indent=2,allow_nan=False)+'\n';Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
