#!/usr/bin/env python3
"""Aggregate S08 latency/response correspondence; not independent semantic proof."""
import argparse
import json
from pathlib import Path
from roy_s08_mri_qc import EEG_SHA, SCANS
from roy_s09_scan_inspection import inspect


def run(directory):
    out={}
    for scan in SCANS:
        p=directory/f'S08_scan{scan}_filtered_gac_cbc.mat'
        q=inspect(p)
        if q['sha256'] != EEG_SHA[scan]:raise ValueError('Unexpected EEG file hash')
        matches=q['events']['response_code_event_matches']
        if any(v['responses'] != v['event_latencies'] or v['responses'] != v['unique_nearest_events'] for v in matches.values()):
            raise ValueError('Response and latency code correspondence fails')
        offsets=q['events']['response_alignment_by_trial']
        out[str(scan)]={'sha256':q['sha256'],'dropbox_content_hash':q['dropbox_content_hash'],
            'eeg':q['eeg'],'trial_count':q['events']['trial_count'],
            'response_code_event_matches':matches,
            'offset_min_s':min(x['min_s'] for x in offsets),
            'offset_max_s':max(x['max_s'] for x in offsets)}
    return {'kind':'within-file report-code correspondence; not independent validation of event meanings',
        'scans':out,'limitations':['Nearest same-code correspondence does not prove experimental report semantics, tag assignment or subjective accuracy.',
        'Time offsets are descriptive; no correction was made.']}


def main():
    p=argparse.ArgumentParser();p.add_argument('eeg_dir',type=Path);args=p.parse_args()
    print(json.dumps(run(args.eeg_dir),indent=2,allow_nan=False))

if __name__=='__main__':main()
