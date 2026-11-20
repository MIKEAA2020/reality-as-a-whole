#!/usr/bin/env python3
"""Metadata-only audit; never writes individual records. See fixed audit plan."""
import csv, glob, hashlib, json, math, os, re
from collections import Counter, defaultdict
from pathlib import Path

BASE=Path('.arena/daly/ds002721-c0b784f902bb3dc6bd674e27feba5693b0fb9506')
OUT=Path('verification/daly_affective_music_event_alignment.json')
MANIFEST_SHA='c026a6bee732bf4eea5e8b60ba2a03d526e05a49b2b2b72ec87df1fbc44c22e7'
CODEBOOK_SHA='ec04e7cf03d312583740918fb65e05c00f26b50a9a4eed5502667c4a6d6fd01e'
PATTERN=re.compile(r'^sub-(\d+)_task-run([2-5])_events\.tsv$')

def audit_events(events):
    """Return aggregate structural statistics, preserving duplicate-event counts."""
    counts=Counter({'strict_questionnaire_intervals':0})
    events=sorted(events)
    starts=[t for t,c in events if c==788]
    fixation=[t for t,c in events if c==786]
    counts['music_start_rows']=len(starts); counts['fixation_rows']=len(fixation)
    counts['starts_without_fixation_in_previous_4s']=sum(not any(0 < t-f <=4 for f in fixation) for t in starts)
    counts['duplicate_identical_events']=len(events)-len(set(events))
    for t in starts:
        codes={c for a,c in events if a==t and 301<=c<=360}
        near={c for a,c in events if abs(a-t)<=.100000001 and 301<=c<=360}
        counts[f'starts_exact_documented_music_identity_{len(codes)}']+=1
        counts[f'starts_near_documented_music_identity_{len(near)}']+=1
        counts['starts_exact_361_399']+=int(any(a==t and 361<=c<=399 for a,c in events))
        counts['starts_near_361_399']+=int(any(abs(a-t)<=.100000001 and 361<=c<=399 for a,c in events))
        counts['starts_exact_401_499']+=int(any(a==t and 401<=c<=499 for a,c in events))
        counts['starts_near_401_499']+=int(any(abs(a-t)<=.100000001 and 401<=c<=499 for a,c in events))
    for idx,t in enumerate(starts):
        end=starts[idx+1] if idx+1<len(starts) else math.inf
        groups=defaultdict(set)
        for a,c in set(events):
            if t<=a<end and (800<=c<=807 or 901<=c<=909): groups[a].add(c)
        by_q=Counter(); bad_q_group=False; answer_without_q=False; at_start=False
        for a,codes in groups.items():
            qs=[c for c in codes if 800<=c<=807]; ans=[c for c in codes if 901<=c<=909]
            for q in qs: by_q[q]+=1
            if qs and (len(qs)!=1 or len(ans)!=1): bad_q_group=True
            if ans and not qs: answer_without_q=True
            if a==t: at_start=True
        missing=any(by_q[q]==0 for q in range(800,808))
        repeated=any(by_q[q]>1 for q in range(800,808))
        counts['intervals']+=1
        counts['intervals_missing_question_code']+=int(missing)
        counts['intervals_repeated_question_timestamp']+=int(repeated)
        counts['intervals_question_group_without_exact_single_answer']+=int(bad_q_group)
        counts['intervals_answer_without_question_same_time']+=int(answer_without_q)
        counts['intervals_question_or_answer_at_start']+=int(at_start)
        if not (missing or repeated or bad_q_group or answer_without_q or at_start): counts['strict_questionnaire_intervals']+=1
    return counts

def main():
    paths=sorted(p for p in BASE.glob('sub-*/eeg/*_events.tsv') if PATTERN.match(p.name))
    if not paths: raise FileNotFoundError('Download pinned archive as documented in the audit report.')
    totals=Counter(); start_counts=Counter(); durations=Counter(); subjects=set(); run_codes=Counter(); hashes={}; keys=set()
    for path in paths:
        m=PATTERN.match(path.name); subject,run=m.groups(); key=(subject,run)
        if key in keys: raise ValueError('duplicate participant/run')
        keys.add(key); subjects.add(subject); run_codes[run]+=1
        hashes[str(path.relative_to(BASE))]=hashlib.sha256(path.read_bytes()).hexdigest()
        events=[]
        with path.open(newline='') as f:
            for r in csv.DictReader(f,delimiter='\t'):
                t=float(r['onset']); code=int(r['trial_type']); dur=float(r['duration'])
                if not math.isfinite(t) or not math.isfinite(dur): raise ValueError('nonfinite input')
                durations[str(dur)]+=1; events.append((t,code))
        stats=audit_events(events); totals.update(stats); start_counts[str(stats['music_start_rows'])]+=1
    codebooks=list(BASE.glob('sub-*/eeg/*_events.json'))
    book_hashes=Counter(hashlib.sha256(p.read_bytes()).hexdigest() for p in codebooks)
    manifest_sha=hashlib.sha256(json.dumps(hashes,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if manifest_sha!=MANIFEST_SHA or set(book_hashes)!={CODEBOOK_SHA}:
        raise ValueError('Input manifest or codebook differs from pinned source')
    receipt={'source_commit':'c0b784f902bb3dc6bd674e27feba5693b0fb9506','n_participants_with_matching_run_file':len(subjects),
             'n_run_files':len(paths),'run_files_by_number':dict(sorted(run_codes.items())),
             'music_starts_per_run_histogram':dict(sorted(start_counts.items())),
             'duration_row_value_histogram_seconds':dict(sorted(durations.items())),
             'counts':dict(sorted(totals.items())), 'event_json_file_count':len(codebooks),
             'distinct_event_json_sha256_count':len(book_hashes),
             'sha256_of_manifest_of_analyzed_event_files':manifest_sha,
             'scope':'Metadata structure only; no raw EEG, stimuli, inferred ratings, timing validation, subjecthood, or phenomenal bridge.'}
    OUT.write_text(json.dumps(receipt,indent=2)+'\n'); print(json.dumps(receipt,indent=2))
if __name__=='__main__': main()
