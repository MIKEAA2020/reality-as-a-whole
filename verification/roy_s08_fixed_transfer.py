#!/usr/bin/env python3
"""Frozen S09-to-S08 report-agreement feasibility benchmark; no model fitting.

Inputs and mapping are externally attested, not established by this script.
Do not publish the manifest if its provenance fields contain private information.
"""
import argparse
import copy
import json
import math
import re
from pathlib import Path

from roy_s09_eeg_report_transfer import assess, read_windows

SCANS = (1, 3, 5)
# From the S09 scans 1–3 fit recorded in roy_s09_eeg_report_transfer.json.
MODEL = {
    'mean_code1': 0.01598754217666589,
    'mean_code2': 0.2368399778715139,
    'majority': 2,
    'slot_rules': [2,2,1,1,2,2,1,1,2,2,2,2,1,2,2,2,2,2,2,2,2],
    'training_pure_clean_code1': 39,
    'training_pure_clean_code2': 57,
}


def validate_manifest(manifest):
    if set(manifest) != {'participant','event_code_mapping','event_mapping_evidence',
                         'condition_evidence','files'}:
        raise ValueError('Manifest has missing or unexpected keys')
    if manifest['participant'] != 'S08' or manifest['event_code_mapping'] != 'same_as_S09':
        raise ValueError('S08 and documented same-as-S09 event coding required')
    for key in ('event_mapping_evidence', 'condition_evidence'):
        if not isinstance(manifest[key],str) or not manifest[key].strip():
            raise ValueError('External provenance evidence required')
    files=manifest['files']
    if not isinstance(files,dict) or set(files) != {str(i) for i in SCANS}:
        raise ValueError('Exactly scans 1, 3 and 5 required')
    hashes=[]
    for scan in SCANS:
        entry=files[str(scan)]
        if not isinstance(entry,dict) or set(entry)!={'path','sha256'}:
            raise ValueError('Each scan needs path and SHA-256')
        if not isinstance(entry['path'],str) or Path(entry['path']).name != f'S08_scan{scan}_filtered_gac_cbc.mat':
            raise ValueError('Incorrect filename for scan')
        if not isinstance(entry['sha256'],str) or not re.fullmatch('[0-9a-f]{64}',entry['sha256']):
            raise ValueError('Expected lowercase SHA-256')
        hashes.append(entry['sha256'])
    if len(set(hashes))!=len(SCANS):raise ValueError('Duplicate files')


def run(manifest):
    validate_manifest(manifest)
    model=copy.deepcopy(MODEL)
    results={}; all_rows=[]
    for scan in SCANS:
        entry=manifest['files'][str(scan)]
        rows=read_windows(Path(entry['path']),entry['sha256'])
        if len(rows)!=105:raise ValueError('Expected 105 windows per run')
        results[str(scan)]=assess(rows,model)
        all_rows.extend(rows)
    if model!=MODEL or not all(math.isfinite(model[k]) for k in ('mean_code1','mean_code2')):
        raise ValueError('Fixed model changed or invalid')
    return {'kind':'fixed S09-to-S08 retrospective report-agreement feasibility, not experience calibration',
            'train_participant':'S09','test_participant':'S08','test_scans':list(SCANS),
            'model':model,'results':results,'pooled_descriptive':assess(all_rows,model),
            'input_sha256':{str(i):manifest['files'][str(i)]['sha256'] for i in SCANS},
            'limitations':['Condition and event mapping are externally attested, not proved by this script.',
               'S09 model was selected post-hoc; this is not prospective preregistration or independent cohort replication.',
               'S08 windows are report-selected and dependent; full-grid failure includes unresolved windows.',
               'Agreement with reports does not establish agreement with experience.']}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('manifest',type=Path)
    args=parser.parse_args()
    print(json.dumps(run(json.loads(args.manifest.read_text())),indent=2,allow_nan=False))

if __name__=='__main__':main()
