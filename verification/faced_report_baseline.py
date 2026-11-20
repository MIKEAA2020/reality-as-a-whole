#!/usr/bin/env python3
"""FACED converted metadata audit; no BDF or stimulus data accessed."""
import collections, csv, hashlib, io, json, math, pathlib, platform, statistics, tarfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
REF='2577b0bbc089b49e828cd98d80445133634b6d34'
BASE=ROOT/'.arena/faced'
# Chen et al. supplementary table S4, valence column, two-decimal published means.
PUBLISHED_VIDEO_MEANS=[2.00,1.51,1.60,1.64,1.71,1.57,1.65,1.48,1.57,1.57,1.96,2.05,3.05,3.24,3.33,3.09,4.04,4.22,4.42,5.23,4.93,4.21,4.39,4.43,4.30,4.42,4.25,4.62]

def blob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def get_verified(tar, tree, path):
    info=tar.getmember('nm000112-'+REF+'/'+path)
    if not info.isfile() or info.size > 200_000: raise ValueError('unexpected input type or size '+path)
    b=tar.extractfile(info).read()
    if blob(b)!=tree[path]: raise ValueError('git blob mismatch '+path)
    return b

def validate(rows, duration):
    videos=[]
    for row in rows:
        if row['video_index'] in ('n/a',''): continue
        try:
            idx=int(row['video_index']); onset=float(row['onset']); d=float(row['duration']); rating=float(row['Valence'])
        except ValueError as e: raise ValueError('invalid event field') from e
        if not 1<=idx<=28 or not all(math.isfinite(v) for v in (onset,d,rating)) or d<=0 or onset<0 or onset+d>duration+0.001 or not 0<=rating<=7:
            raise ValueError('invalid event bounds')
        if row['binary_label'] not in ('positive','negative','neutral') or not row['emotion_label'] or row['emotion_label']=='n/a': raise ValueError('invalid category')
        videos.append((idx,onset,d,rating,row['emotion_label'],row['binary_label'],row['sample']))
    if len(set(v[0] for v in videos))!=len(videos): raise ValueError('duplicate video')
    spans=sorted(videos,key=lambda v:v[1])
    if any(a[1]+a[2]>b[1]+1e-6 for a,b in zip(spans,spans[1:])): raise ValueError('overlapping video spans')
    return videos

def mean(v): return sum(v)/len(v)
def scores(actual,pred):
    errors=[a-b for a,b in zip(actual,pred)]
    return {'n':len(errors),'mae':mean([abs(x) for x in errors]),'rmse':math.sqrt(mean([x*x for x in errors]))}
def predict(train,test,kind):
    overall=mean([r['y'] for r in train]); grouped=collections.defaultdict(list)
    if kind!='grand':
        key='cat' if kind=='category' else 'video'
        for r in train: grouped[r[key]].append(r['y'])
    preds=[]; fallbacks=0
    for r in test:
        if kind=='grand': preds.append(overall); continue
        vals=grouped.get(r[key]); fallbacks+=int(not vals)
        preds.append(mean(vals) if vals else overall)
    return preds,fallbacks

def splits(rows, crossed):
    cats=collections.defaultdict(set)
    for r in rows: cats[r['cat']].add(r['video'])
    vfold={v:i%3 for c in cats for i,v in enumerate(sorted(cats[c]))}
    for pf in range(5):
        for vf in (range(3) if crossed else [None]):
            test=[r for r in rows if r['subject']%5==pf and (not crossed or vfold[r['video']]==vf)]
            train=[r for r in rows if r['subject']%5!=pf and (not crossed or vfold[r['video']]!=vf)]
            yield train,test

def evaluate(rows,crossed):
    methods=['grand','category'] if crossed else ['grand','category','video']
    all_actual=[]; all_preds={m:[] for m in methods}; falls={m:0 for m in methods}; count=0
    for train,test in splits(rows,crossed):
        if not train or not test: raise ValueError('empty fold')
        count+=1; all_actual.extend(r['y'] for r in test)
        for m in methods:
            preds,fb=predict(train,test,m);all_preds[m].extend(preds);falls[m]+=fb
    if len(all_actual)!=len(rows): raise ValueError('testing not once')
    return {'folds':count,'scores':{m:{**scores(all_actual,all_preds[m]),'fallbacks':falls[m]} for m in methods}}

def main():
    tree={x['path']:x['sha'] for x in json.loads((BASE/'tree.json').read_text())['tree'] if x['type']=='blob'}
    records=[]; hashes={}; counts=[]; manufacturers=collections.Counter(); sample_mismatch=0; sample_checked=0; max_sample_difference=0.; metadata={}
    with tarfile.open(BASE/'metadata.tar.gz','r:gz') as tar:
        for s in range(123):
            prefix=f'sub-{s:03d}/eeg/sub-{s:03d}_task-watchingVideoClips'
            path=prefix+'_events.tsv'; b=get_verified(tar,tree,path); hashes[path]=hashlib.sha256(b).hexdigest()
            rows=list(csv.DictReader(io.StringIO(b.decode('utf-8-sig')),delimiter='\t'))
            path=prefix+'_eeg.json'; b=get_verified(tar,tree,path);hashes[path]=hashlib.sha256(b).hexdigest()
            sidecar=json.loads(b); fs=sidecar['SamplingFrequency']; duration=sidecar['RecordingDuration']
            manufacturers[sidecar.get('Manufacturer','missing')]+=1
            vids=validate(rows,duration);counts.append(len(vids))
            for i,on,d,y,emotion,cat,sample in vids:
                data=(emotion,cat)
                if i in metadata and metadata[i]!=data: raise ValueError(f'inconsistent metadata for video {i}')
                metadata[i]=data
                if sample not in ('n/a',''):
                    sample_checked+=1
                    delta=abs(int(sample)-on*fs); max_sample_difference=max(max_sample_difference,delta)
                    sample_mismatch += delta>0.501
                records.append({'subject':s,'video':i,'y':y,'cat':cat})
        for path in ['code/faced.py','dataset_description.json','README.md']:
            b=get_verified(tar,tree,path); hashes[path]=hashlib.sha256(b).hexdigest()
    if len(metadata)!=28: raise ValueError('incomplete video metadata')
    groups=collections.defaultdict(list)
    for r in records: groups[r['video']].append(r['y'])
    output={'python_version':platform.python_version(),'source_commit':REF,'archive_sha256':hashlib.sha256((BASE/'metadata.tar.gz').read_bytes()).hexdigest(),
      'input_sha256':hashes,'subject_count':123,'video_count':len(groups),'eligible_rows':len(records),
      'per_subject_video_counts':dict(sorted(collections.Counter(counts).items())), 'manufacturers':dict(manufacturers),
      'sample_fields_checked':sample_checked,'sample_onset_inconsistencies_over_half_sample':sample_mismatch,'max_sample_onset_difference_samples':max_sample_difference,
      'published_s4_valence_mean_max_abs_difference':max(abs(mean(groups[i])-PUBLISHED_VIDEO_MEANS[i-1]) for i in range(1,29)),
      'published_s4_valence_means_within_rounding_0_005':sum(abs(mean(groups[i])-PUBLISHED_VIDEO_MEANS[i-1]) <= 0.005 for i in range(1,29)),
      'mean_video_valence':mean([mean(g) for g in groups.values()]),
      'mean_within_video_population_sd':mean([statistics.pstdev(g) for g in groups.values()]),
      'population_sd_video_means':statistics.pstdev([mean(g) for g in groups.values()]),
      'known_video_heldout_subject':evaluate(records,False),'heldout_subject_and_video':evaluate(records,True)}
    (ROOT/'verification/faced_report_baseline.json').write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='input_sha256'},indent=2))
if __name__=='__main__': main()
