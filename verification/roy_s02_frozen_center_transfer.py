#!/usr/bin/env python3
"""Evaluate frozen S01+S09 report-center model on six S02 rivalry scans.

Source manifest is a JSON object of the six scan numbers to independently
recorded SHA-256 hashes, not hashes calculated from these files at scoring time.
Any failure stops rather than tuning; only aggregate outputs are written.
"""
import argparse
import json
from pathlib import Path
from roy_s09_eeg_report_transfer import sha
from roy_report_center_development import read_scan, assess

SCANS=(1,2,4,6,8,11)
FROZEN={
    'roy_report_center_development.json':'60ab958fad3249591ca48e82cc67101748e47677455501b6819e2c778e9bdb44',
    'roy_report_center_development.py':'760128ffb92652d2ae51c9969c6948f07dd99711a326a95a10653839d394e798',
    'roy_s01_mixed_coverage_diagnostic.py':'7f7db2cc9b9380410be56b0e211503c43c65510084b3c6ab44fe0214a9b33382',
    'roy_s09_scan1_alignment_gate.py':'1bd17993357fdd23151aed48ef288c7793de3dc23448bb13d0133828dc8fa1a5',
    'roy_s09_eeg_report_transfer.py':'20920a1da08301f116e3a7841dacd9727ab471b6f6343f5362cd52dcccde2858',
    'roy_s01_frozen_three_state_transfer.py':'1c4bf93cf37fd412f4e1aa98cc173913a6093d5515f98a7fe42f0ee45ae4ebfc',
    'roy_s09_three_state_pilot.py':'a5d582c1409725acb2cd116dcb32dd9882635ea8a08b8416d12071a3d4bea899'}


def load_frozen(root):
    for name,expected in FROZEN.items():
        if sha(root/name)!=expected: raise ValueError(f'Frozen component hash mismatch: {name}')
    m=json.loads((root/'roy_report_center_development.json').read_text())['pooled_development_model']
    if m['training_participants']!=['S01','S09'] or len(m['class_mean_features'])!=3 or len(m['slot_rules'])!=42:
        raise ValueError('Invalid frozen model')
    return m


def validate_manifest(data):
    if not isinstance(data,dict) or set(data)!=set(map(str,SCANS)):
        raise ValueError('Manifest must include exactly the six prespecified rivalry scans')
    for value in data.values():
        if not isinstance(value,str) or len(value)!=64 or any(c not in '0123456789abcdef' for c in value):
            raise ValueError('Invalid SHA-256 in manifest')
    return data


def evaluate(directory, manifest, model):
    manifest=validate_manifest(manifest)
    paths={s:directory/f'S02_scan{s}_filtered_gac_cbc.mat' for s in SCANS}
    # Check the entire declared set before reading any report/EEG values.
    for s,path in paths.items():
        if sha(path)!=manifest[str(s)]: raise ValueError(f'Scan {s} source SHA-256 mismatch')
    scans={}
    for s in SCANS:
        scans[s]=read_scan(paths[s],manifest[str(s)],s)
    return {'per_scan':{str(s):assess(scans[s],model) for s in SCANS},
            'pooled':assess([r for s in SCANS for r in scans[s]],model)}


def main():
    p=argparse.ArgumentParser();p.add_argument('directory',type=Path);p.add_argument('--source-manifest',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();root=Path(__file__).resolve().parent
    if args.output.resolve() in {(root/k).resolve() for k in FROZEN}: raise ValueError('Cannot overwrite a frozen input')
    model=load_frozen(root); manifest=json.loads(args.source_manifest.read_text())
    result={'scope':'One new participant S02; exploratory transfer to report-center labels, not population or experiential validation.',
            'scans':list(SCANS),'model_receipt_sha256':FROZEN['roy_report_center_development.json'],
            'source_sha256':validate_manifest(manifest),
            'source_caveat':'Source manifest must be independently recorded; self-computed hashes do not establish public-source authenticity.',
            'results':evaluate(args.directory,manifest,model)}
    text=json.dumps(result,indent=2,allow_nan=False)+'\n';args.output.write_text(text);print(text,end='')


if __name__=='__main__':main()
