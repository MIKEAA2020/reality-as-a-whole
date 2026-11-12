#!/usr/bin/env python3
"""QC three supplied S08 scan ZIPs; no images, paths or DICOM metadata emitted."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import numpy as np
from scipy.io import loadmat
from roy_mri_pair_inventory import inventory
from roy_s09_scan1_alignment_gate import sample_indices, candidate_starts

SCANS=(1,3,5)
ZIP_DROPBOX_HASH={1:'6baf689b69184d6eb87b5b0f0d0aa9a6555f959b0ad8811e3804cacb3fce7006',
                  3:'01b93ce25b9adc09d2eededbc4a812e5bdf7129042965fa5c00add775a7a3e1c',
                  5:'0a564de4053ff9f0970da79660ee14c4e4fbf15520c04efeb91f59a0103075d0'}
EEG_SHA={1:'0ea46d49eeb8b4fce5bf7ff0f0726ebf1a75e0b1fa16496cb309c07b3544493f',
         3:'05e7195b2c5df9357b0e079a3ef021edaae65666f5285618453cbaccd29c2916',
         5:'9dda27e8dfa198986f1697c8d41837c00eccff544c80ccc5cbd809f289c96939'}


def hashes(p):
    h=hashlib.sha256(); blocks=[]
    with p.open('rb') as f:
        while b:=f.read(4*1024*1024):
            h.update(b); blocks.append(hashlib.sha256(b).digest())
    return h.hexdigest(),hashlib.sha256(b''.join(blocks)).hexdigest()


def run(eeg_dir,zip_dir):
    out={}
    for scan in SCANS:
        p=zip_dir/f'scan{scan}.zip'; eeg=eeg_dir/f'S08_scan{scan}_filtered_gac_cbc.mat'
        sha,db=hashes(p)
        if db!=ZIP_DROPBOX_HASH[scan] or hashes(eeg)[0]!=EEG_SHA[scan]:
            raise ValueError('Input hash mismatch')
        with zipfile.ZipFile(p) as z:
            others=[i for i in z.infolist() if not i.is_dir() and Path(i.filename).suffix.lower() not in ('.hdr','.img')]
            extra_bytes=0
            for item in others:
                with z.open(item) as f:
                    while b:=f.read(1024*1024):extra_bytes+=len(b)
        q=inventory(p) # Reads and validates all pair files, including ZIP CRC.
        e=loadmat(eeg,squeeze_me=True,struct_as_record=False,
                  variable_names=['dcminfo','sampling_freq','latency_tr'])
        if int(e['dcminfo'].SeriesNumber)!=q['series_number']:
            raise ValueError('EEG and MRI series differ')
        tr=sample_indices(e['latency_tr']);diff=np.unique(np.diff(tr)).tolist()
        candidates=(candidate_starts(q['volumes_read'],len(tr))
                    if q['frame_min']==1 and not q['missing_frame_indices_inside_observed_range']
                    and len(tr)>1 and len(tr)<=q['volumes_read']
                    and float(e['sampling_freq'])==250.0 and diff==[550] else None)
        out[str(scan)]={'zip_sha256':sha,'dropbox_hash_matches':True,
           'volumes_read':q['volumes_read'],'pair_files_read':q['pair_files_read'],
           'other_files_read':len(others),'other_bytes_read':extra_bytes,
           'frame_min':q['frame_min'],'frame_max':q['frame_max'],
           'missing_frames':q['missing_frame_indices_inside_observed_range'],
           'geometry':q['geometry'],'all_voxels_finite':True,'eeg_and_mri_series_match':True,
           'eeg_triggers':len(tr),'trigger_spacing_samples_unique':diff,
           'assumed_consecutive_first_frame_candidates':candidates}
    return {'kind':'three scan archive QC, not temporal alignment or fMRI GLM','scans':out,
            'limitations':['Archive content checks do not verify trial stimuli, original archive provenance, registration or anatomical privacy.',
              'Trigger candidates assume consecutive ordering, no missing triggers and unknown anchor.']}


def main():
    p=argparse.ArgumentParser();p.add_argument('eeg_dir',type=Path);p.add_argument('zip_dir',type=Path)
    args=p.parse_args();print(json.dumps(run(args.eeg_dir,args.zip_dir),indent=2,allow_nan=False))

if __name__=='__main__':main()
