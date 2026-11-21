#!/usr/bin/env python3
"""Audit the pinned author supplement's label readiness; do not score predictions.

Input is not redistributed. This reports metadata and field consistency, not a
verification of trial identity, raw data, experience or any neural measurement.
"""
import csv
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import sys

SHA256='12b5d1384ffc64a5f02c22a72ebcc9a29074f2bafac0da8f96f5a37a08861f2b'
GIT_BLOB='8b995c541e7084bc616501c626f90505b35a89cf'


def audit(path,verify=True):
    b=Path(path).read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if verify and (hashlib.sha256(b).hexdigest()!=SHA256 or blob!=GIT_BLOB):
        raise ValueError('Input does not match pinned supplement blob')
    reader=csv.DictReader(io.StringIO(b.decode('utf-8-sig'),newline=''))
    if reader.fieldnames!=['ID','Trial_Num','laser_power','Painrating']:
        raise ValueError('Unexpected schema')
    byperson=defaultdict(list); seen=set(); energy=Counter(); flags=Counter(); fractional_persons=set(); missing_persons=set()
    for row in reader:
        person=int(row['ID']); trial=int(row['Trial_Num'])
        if person<=0 or trial<=0 or (person,trial) in seen:raise ValueError('invalid or duplicate identity/trial')
        seen.add((person,trial))
        try:e=Decimal(row['laser_power']);rating=Decimal(row['Painrating'])
        except InvalidOperation:raise ValueError('nonnumeric field')
        if not e.is_finite() or e<0:raise ValueError('invalid energy')
        missing=not rating.is_finite()
        if not missing and not 0<=rating<=10:raise ValueError('rating outside stated range')
        if missing:flags['nonfinite_rating']+=1; missing_persons.add(person)
        if e==0:
            flags['zero_energy']+=1
            if missing or rating!=0:flags['zero_energy_not_zero_rating']+=1
        if not missing and rating%1:
            flags['fractional_rating']+=1;fractional_persons.add(person)
        if e>0 and not missing:flags['positive_energy_finite_rating']+=1
        energy[str(e)]+=1; byperson[person].append((trial,e,rating))
    zero_persons=[v for v in byperson.values() if any(e==0 for _,e,_ in v)]
    suffix=0
    for rows in zero_persons:
        rows.sort(key=lambda x:x[0])
        first=next(i for i,(_,e,_) in enumerate(rows) if e==0)
        suffix+=int(all(e==0 for _,e,_ in rows[first:]))
    return {'git_blob':blob,'sha256':hashlib.sha256(b).hexdigest(), 'rows':len(seen),
            'distinct_ids':len(byperson),'rows_per_id_distribution':dict(sorted(Counter(map(len,byperson.values())).items())),
            'field_flags':dict(flags),'ids_with_nonfinite_rating':len(missing_persons),
            'ids_with_fractional_rating':len(fractional_persons),
            'ids_with_zero_energy':len(zero_persons),'zero_energy_ids_with_suffix_only':suffix,
            'energy_counts':dict(sorted(energy.items(),key=lambda x:Decimal(x[0]))),
            'score_status':'suppressed: trial-level label construction, scale and excluded records not independently validated',
            'scope':'author supplementary table only; no raw EEG, observed pain, unpleasantness, physical mismatch or subject inference'}


def main():
    if len(sys.argv)!=2:raise SystemExit('Usage: python verification/laser_pain_trial_baseline.py /path/to/pinned.csv')
    result=audit(sys.argv[1]);text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
