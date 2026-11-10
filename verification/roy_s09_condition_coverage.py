#!/usr/bin/env python3
"""Post-hoc S09 report coverage grouped by documented scan condition.

Uses existing 250 Hz coverage summaries and the audited scan labels. No decoder,
patient-level inference, causal conclusion or experience calibration is supplied.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def summarize(coverage_files, condition_audit, inspections):
    labels={x['scan']:x['documented_condition'] for x in condition_audit['scans']}
    if set(labels) != set(range(1, 10)):
        raise ValueError('Need exactly nine documented scan labels')
    scans={}
    for doc in coverage_files:
        for scan in doc['scans']:
            match=re.fullmatch(r'S09_scan(\d+)_filtered_gac_cbc\.mat',scan['file'])
            if not match:
                raise ValueError('Unexpected coverage file name')
            i=int(match.group(1))
            if i in scans or i not in labels or scan['sha256'] != inspections[i]['sha256']:
                raise ValueError('Duplicate, unknown or incompatible scan')
            seconds=scan['all_trial_samples']['samples']/scan['sampling_hz']
            items=scan['all_trial_samples']['seconds_by_label']
            if abs(sum(items.values()) - seconds)>1e-7:
                raise ValueError('Coverage does not add to denominator')
            scans[i]={'condition':labels[i], 'seconds':seconds,
                      'unknown_seconds':items['unknown_before_first_event'],
                      'mixed_seconds':items['code_3_mixed']}
    if set(scans)!=set(labels):
        raise ValueError('Coverage incomplete')
    groups={}
    for i, item in sorted(scans.items()):
        g=groups.setdefault(item['condition'],{'scans':[], 'trial_seconds':0.0,'unknown_seconds':0.0,'mixed_seconds':0.0})
        g['scans'].append(i)
        for k in ('unknown_seconds','mixed_seconds'):
            g[k]+=item[k]
        g['trial_seconds']+=item['seconds']
    for g in groups.values():
        g['unresolved_fraction']=(g['unknown_seconds']+g['mixed_seconds'])/g['trial_seconds']
    return {'kind':'post-hoc single-participant report coverage by documented scan labels, not condition inference',
            'groups':groups,
            'assumptions':['Each trial lasts 42 seconds from EEG trial marker; report code carried forward until next event.',
                           'Before first response is unknown; code 3 counts as unresolved for a binary coverage score.',
                           'Scan labels follow original README and the reanalysis script; actual stimuli and replay lineage were not independently checked.'],
            'limitations':['Reported mixing is not incorrect perception or decoder error.',
                           'Single subject and post-hoc grouping; run order, stimuli, reporting and other confounds are not controlled.',
                           'No fMRI-to-EEG alignment, population inference or direct experience error is established.']}


def main():
    def read(name): return json.loads((ROOT/name).read_text())
    files=[read(n) for n in ('roy_s09_scans1_to3_report_coverage.json',
        'roy_s09_scans4_to6_report_coverage.json','roy_s09_report_coverage.json')]
    audit=read('roy_s09_public_support_audit.json')
    inspections={i:read(f'roy_s09_scan{i}_inspection.json') for i in range(1,10)}
    print(json.dumps(summarize(files,audit,inspections),indent=2,allow_nan=False))


if __name__=='__main__':
    main()
