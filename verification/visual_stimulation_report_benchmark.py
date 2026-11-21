#!/usr/bin/env python3
"""Pinned clinical event metadata only: no iEEG, privacy-identifying text or phenomenal assay."""
import argparse,csv,hashlib,io,json,math,re,tarfile
from collections import Counter,defaultdict
from fractions import Fraction as F
from pathlib import Path

COMMIT='ff529027bef934f384e7385f1b83d7190ef307d0'
TREE='d8e1eb561d4352dd37662677372f5572099c2082'
EVENT=re.compile(r'^(sub-\d+)/(ses-\d+)/ieeg/\1_\2_task-dcs_events\.tsv$')
TARGETS=('sym_static','sym_dynamic','sym_continuous_hallucination','sym_intermittent_hallucination')

def git_blob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def parse_events(data, strict=True):
    r=csv.DictReader(io.StringIO(data.decode('utf-8-sig')),delimiter='\t')
    if not r.fieldnames or not {'label','onset','duration','stim_contacts','stim_intensity',*TARGETS}.issubset(r.fieldnames):raise ValueError('required schema')
    rows=list(r);on=[x for x in rows if x['label'] not in ('prestim','poststim')]
    if strict and (len(rows)!=3 or len(on)!=1 or sum(x['label']=='prestim' for x in rows)!=1 or sum(x['label']=='poststim' for x in rows)!=1):raise ValueError('event structure')
    candidates=[x for x in rows if x.get('stim_intensity') not in ('','n/a',None)]
    if len(candidates)!=1:raise ValueError('non-unique current row')
    x=candidates[0]
    current=F(x['stim_intensity']); onset=F(x['onset']); duration=F(x['duration'])
    if current<=0 or onset<0 or duration<0:raise ValueError('invalid stimulation metadata')
    flags={k:v for k,v in x.items() if k.startswith('sym_')}
    if not flags or any(v not in ('0','1') for v in flags.values()):raise ValueError('missing/nonbinary annotation')
    pre=next((y for y in rows if y['label']=='prestim'),None);post=next((y for y in rows if y['label']=='poststim'),None)
    pre_before=bool(pre and F(pre['onset'])+F(pre['duration'])<=onset)
    post_after=bool(post and F(post['onset'])>=onset)
    return {'current':current,'onset':onset,'duration':duration,'flags':{k:int(v) for k,v in flags.items()},
            'pre_before_marker':pre_before,'post_after_marker':post_after,'row_count':len(rows),'post_present':bool(post),
            'description_present':bool(x['label'].strip()),'contacts_present':x['stim_contacts'] not in ('','n/a'),
            'explicit_sham_label':'sham' in x['label'].casefold(),
            'explicit_lower_intensity_label':bool(re.search(r'lower[- ]intensity|half[- ]intensity|half (?:the )?intensity',x['label'].casefold()))}

def score(rows):
    """In-sample descriptive oracle; no fitted or held-out prediction."""
    result={}
    for target in TARGETS:
        grouped=defaultdict(list)
        for r in rows:grouped[(r['person'],r['current'])].append(r['flags'][target])
        repeated=[v for v in grouped.values() if len(v)>1]
        oracle=sum(min(sum(v),len(v)-sum(v)) for v in grouped.values())
        result[target]={'ones':sum(r['flags'][target] for r in rows),'patients_with_one':len({r['person'] for r in rows if r['flags'][target]}),
                       'same_patient_current_repeated_groups':len(repeated),
                       'same_patient_current_mixed_groups':sum(bool(sum(v)) and sum(v)<len(v) for v in repeated),
                       'oracle_in_sample_mistakes':oracle,'oracle_in_sample_mistake_fraction':float(F(oracle,len(rows)))}
    return result

def run(treepath,archivepath):
    tree=json.loads(Path(treepath).read_text())
    if tree.get('truncated') is not False or tree.get('sha')!=TREE:raise ValueError('wrong or truncated tree')
    items={x['path']:x for x in tree['tree']};paths=sorted(p for p in items if EVENT.fullmatch(p))
    if not paths:raise ValueError('no events')
    needed=set(paths)|{p[:-3]+'json' for p in paths}
    if not needed.issubset(items):raise ValueError('missing event sidecar')
    raw=Path(archivepath).read_bytes()
    if len(raw)>10_000_000:raise ValueError('archive too large')
    prefix='ds005169-'+COMMIT+'/';data={}
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tar:
        for m in tar:
            if m.name==prefix[:-1] and m.isdir():continue
            if not m.name.startswith(prefix):raise ValueError('archive prefix')
            p=m.name[len(prefix):]
            if p not in needed:continue
            if p in data or not m.isfile() or m.size>50_000:raise ValueError('invalid event file')
            b=tar.extractfile(m).read()
            if git_blob(b)!=items[p]['sha']:raise ValueError('git blob hash mismatch')
            data[p]=b
    if set(data)!=needed:raise ValueError('missing verified file')
    rows=[];descriptions=Counter();suffixes=Counter();issues=Counter();strict_eligible=0
    for path in paths:
        person,session=EVENT.fullmatch(path).groups()
        meta=json.loads(data[path[:-3]+'json']);descriptions[(meta.get('sym_color',{}).get('Description'),meta.get('sym_non_color',{}).get('Description'))]+=1
        try:
            parse_events(data[path],strict=True);strict_eligible+=1
        except ValueError as exc:issues[str(exc)]+=1
        r=parse_events(data[path],strict=False)
        r['person']=person;r['session']=session;rows.append(r)
        base=path.removesuffix('_events.tsv')
        for ext in ('ieeg.eeg','ieeg.vhdr','ieeg.vmrk'):
            item=items.get(base+'_'+ext);suffixes[ext+'_paths']+=bool(item);suffixes[ext+'_symlinks']+=bool(item and item.get('mode')=='120000')
    flag_sets={tuple(sorted(r['flags'])) for r in rows}
    if len(flag_sets)!=1:raise ValueError('inconsistent flag schemas')
    observed=score(rows)
    exploratory=observed
    return {'commit':COMMIT,'root_tree':TREE,'archive_bytes':len(raw),'archive_sha256':hashlib.sha256(raw).hexdigest(),'git_blobs_verified':len(needed),
      'event_files':len(paths),'strict_plan_eligible':strict_eligible,'strict_plan_exclusions':dict(issues),'primary_benchmark_status':'suppressed: strict eligibility excludes most files', 'amended_events':len(rows),'amended_patients':len({r['person'] for r in rows}),'amended_event_row_count':dict(Counter(str(r['row_count']) for r in rows)),'post_marker_present':sum(r['post_present'] for r in rows),'current_at_most_1ma':sum(r['current']<=1 for r in rows),
      'all_annotations':{k:sum(r['flags'][k] for r in rows) for k in sorted(rows[0]['flags'])},
      'all_zero_flag_rows':sum(not any(r['flags'].values()) for r in rows),
      'stimulation_marker_zero_duration':sum(r['duration']==0 for r in rows),
      'pre_window_ends_before_marker':sum(r['pre_before_marker'] for r in rows),'post_window_starts_after_marker':sum(r['post_after_marker'] for r in rows),
      'text_present':sum(r['description_present'] for r in rows),'contacts_present':sum(r['contacts_present'] for r in rows),
      'explicit_sham_text':sum(r['explicit_sham_label'] for r in rows),
      'explicit_lower_intensity_text':sum(r['explicit_lower_intensity_label'] for r in rows),'signal_file_paths':dict(suffixes),
      'color_sidecar_description_pairs':[{'color':a,'non_color':b,'files':n} for (a,b),n in sorted(descriptions.items())],
      'amended_exploratory_same_patient_current':exploratory,
      'scope':'only selected annotated metadata events, not iEEG, validated experiential absence, causal effect of current, q or a framework pass'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--tree',default='.arena/visual-stimulation/tree.json');p.add_argument('--archive',default='.arena/visual-stimulation/archive.tar.gz');a=p.parse_args()
    text=json.dumps(run(a.tree,a.archive),indent=2,allow_nan=False)+'\n';Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
