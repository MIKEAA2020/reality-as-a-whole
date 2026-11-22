#!/usr/bin/env python3
"""Frozen S09-to-S01 report-code transfer; no fitting to S01."""
import argparse
import hashlib
import json
from pathlib import Path
from roy_s09_three_state_pilot import read_windows, assess
from roy_s09_eeg_report_transfer import sha

RIVALRY = (1, 3, 5, 7, 10, 12)
MODEL_SHA256 = '1b60b31e2aec8cb71df6380aaf531e331bc20323f9fc9985e1c6e073c3a105d7'
# Dropbox listing, obtained from the supplied folder before downloads.
SOURCE = {
 1:(35251183,'5d7f6982fc35f502b7c422afe53e81f221cb264d298a87dab1ed4c0353332987'),
 2:(35266208,'cb365012e2dd12511784b997d8f7b254ea68e17a398666378cf8a7384f73e411'),
 3:(35252730,'38ca65391d436f8c0cbac9ac2d931dcae563d3a06a9ecfe2c80d896e24635211'),
 4:(35284878,'8f0ab4885f458a272243baf577ba0a9713ea03e640f065ca68ca37e0bad2c758'),
 5:(35270978,'e74b057992fac9b107a2631e2385b2f393cf71dc54dcb7d8315273745ce1ec1f'),
 6:(35238352,'ea638a41d8106d582d0a83df7423397093f808713b5b2597341bc380e8f19352'),
 7:(35264233,'3f8526acb78b7493b8152c49722b38715d0275984d0118dd6107f220996a68ff'),
 8:(35226603,'00ef4def4a866cb200fe571595f831b3b39bb6d1e64f1eed86d7e1885d3373d2'),
 9:(35249498,'b9b4c8a5e384dd15717786d38049856ad5136d15ff3feb0b74429c09bb2e0560'),
 10:(35263488,'2b7324e3493d505699eae9110291d724405d370881e0d0619e9b055c43939219'),
 11:(35226591,'29eddb7e808022dfa613c894abafce740fcffa31cb1064596854527c65869799'),
 12:(35226650,'cab3e2680ab4db19662e7fd1d369f5890603af5e2e0b5773ba608ebae64291b8'),
 13:(35248227,'c0684ad6c00aafb8efbeb4f5075e1ffe00b7f748cf3ffb1172e222eb695a0704')}


def dropbox_hash(path):
    aggregate = hashlib.sha256()
    with path.open('rb') as f:
        while block := f.read(4*1024*1024):
            aggregate.update(hashlib.sha256(block).digest())
    return aggregate.hexdigest()


def verify_sources(directory):
    hashes = {}
    for scan, (size, expected) in SOURCE.items():
        path = directory/f'S01_scan{scan}_filtered_gac_cbc.mat'
        if path.stat().st_size != size or dropbox_hash(path) != expected:
            raise ValueError(f'Scan {scan} fails Dropbox size/content hash')
        hashes[scan] = sha(path)
    return hashes


def load_frozen_model(path):
    if sha(path) != MODEL_SHA256:
        raise ValueError('Frozen prior receipt hash mismatch')
    model = json.loads(path.read_text())['training_model']
    model['means'] = {int(k): float(v) for k,v in model['means'].items()}
    model['class_counts'] = {int(k): int(v) for k,v in model['class_counts'].items()}
    if set(model['means']) != {1,2,3} or len(model['slot_rules']) != 21:
        raise ValueError('Invalid frozen training model')
    return model


def evaluate(windows, model):
    if set(windows) != set(RIVALRY):
        raise ValueError('All six declared rivalry scans required')
    return {'per_scan': {str(s): assess(windows[s], model) for s in RIVALRY},
            'pooled': assess([r for scan in RIVALRY for r in windows[scan]], model)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    frozen = load_frozen_model(base/'roy_s09_three_state_pilot.json')
    hashes = verify_sources(args.directory)
    windows = {s: read_windows(args.directory/f'S01_scan{s}_filtered_gac_cbc.mat', hashes[s]) for s in RIVALRY}
    result = {'scope':'Frozen S09-trained procedure evaluated on one S01 participant, not experiential calibration or population inference.',
              'source': '13 local files matched supplied Dropbox size and content hashes; original public archive not independently verified',
              'frozen_receipt_sha256': MODEL_SHA256, 's01_rivalry_scans': list(RIVALRY),
              'scoring': '2-second windows, >=75% one report code, clean windows predicted; artifact abstention',
              'results': evaluate(windows, frozen)}
    text = json.dumps(result, indent=2, allow_nan=False)+'\n'
    args.output.write_text(text)
    print(text, end='')


if __name__ == '__main__': main()
