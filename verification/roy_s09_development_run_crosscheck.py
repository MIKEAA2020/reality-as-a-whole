#!/usr/bin/env python3
"""Post-hoc leave-one-run-out check only on already-inspected S09 scans 1–3.

Uses the unchanged EEG/report rule and baselines; held-out from fitting only,
not blind, not preregistered, not population or experience inference.
"""
import argparse
import json
from pathlib import Path

from roy_s09_eeg_report_transfer import read_windows, train, assess

SCANS=(1,2,3)


def crosscheck(windows):
    if set(windows)!=set(SCANS):
        raise ValueError('Requires exactly development scans 1, 2 and 3')
    folds=[]
    for held_out in SCANS:
        fit_scans=[scan for scan in SCANS if scan!=held_out]
        model=train([row for scan in fit_scans for row in windows[scan]])
        folds.append({'held_out_scan':held_out,'fit_scans':fit_scans,
                      'training_model':model,'result':assess(windows[held_out],model)})
    return {'kind':'post-hoc within-development leave-one-run-out diagnostic',
            'folds':folds,
            'limitations':['All three runs and model were previously inspected; not blind or preregistered.',
                           'Folds share training runs and one participant; windows are dependent.',
                           'Do not use these results to retune and then present prior test runs as untouched.',
                           'Selected pure-report windows do not establish accuracy about experience.']}


def main():
    p=argparse.ArgumentParser();p.add_argument('files',nargs=3,type=Path);a=p.parse_args()
    scans={}
    for n,path in zip(SCANS,a.files):
        if path.name != f'S09_scan{n}_filtered_gac_cbc.mat':
            raise ValueError('Expected scan 1, 2, 3 in order')
        info=json.loads((Path(__file__).resolve().parent/f'roy_s09_scan{n}_inspection.json').read_text())
        scans[n]=read_windows(path,info['sha256'])
    print(json.dumps(crosscheck(scans),indent=2,allow_nan=False))


if __name__=='__main__':main()
