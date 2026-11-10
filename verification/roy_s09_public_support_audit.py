#!/usr/bin/env python3
"""Audit S09 source labels and publicly shared motion data, without filenames.

Inputs: user-provided README PDF, a pinned reanalysis Git tree JSON and its
locally fetched info_scans_conditions.m, two condition-index MAT files, and
nine sanitized scanN.txt / scanN.mat motion pairs. Outputs aggregates and
hashes, never source member paths, medical images, patient metadata or data.
Requires PyMuPDF, SciPy and NumPy. Agreement may reflect shared provenance;
none of these checks establishes EEG-to-fMRI timing or motion-row alignment.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import fitz
import numpy as np
from scipy.io import loadmat

COMMIT = 'b8ca204024a4f7151645c6c2e908eb564203ac66'
PREFIX = 'data/rivalry_fMRI_head_motion_files/S09/'
TAIL = re.compile(r'-(\d{4})-(\d{5})-(\d{6})-(\d{2})')
ALLOWED = {'rivalry', 'replay_smooth', 'replay_inst'}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git_blob_sha(path):
    b = Path(path).read_bytes()
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()


def labels(body):
    found = re.findall(r"'([^']+)'", body)
    if len(found) != 9 or any(x not in ALLOWED for x in found):
        raise ValueError('Expected exactly nine recognized scan labels')
    return found


def pdf_labels(pdf):
    with fitz.open(pdf) as doc:
        if len(doc) < 2:
            raise ValueError('README needs page 2')
        text = doc[1].get_text('text', sort=True)
    match = re.search(r'(?ms)^\s*-\s*S09\s*$\s*(.*?)(?=^\s*-\s*S10\s*$)', text)
    if not match or 'Scan Types:' not in match.group(1):
        raise ValueError('S09 scan block missing or ambiguous')
    return labels(match.group(1).split('Scan Types:', 1)[1])


def code_labels(text):
    match = re.search(r'(?m)^\s*s9\s*=\s*\{([^}]*)\}', text)
    if not match:
        raise ValueError('Missing S09 code label list')
    return labels(match.group(1))


def mat_indices(path, field):
    d = loadmat(path, squeeze_me=True, variable_names=[field])
    a = np.atleast_1d(d[field])
    if len(a) != 20:
        raise ValueError('Expected 20 subject lists')
    idx = np.atleast_1d(a[8]).astype(int).tolist()
    return idx


def motion_qc(text_path, mask_path, expected_rows):
    x = np.loadtxt(text_path, ndmin=2)
    d = loadmat(mask_path, squeeze_me=True, variable_names=['mask'])
    mask = np.atleast_1d(d['mask'])
    if x.shape != (expected_rows, 6) or mask.shape != (expected_rows,):
        raise ValueError('Motion/mask dimensions differ from MRI inventory')
    if not np.isfinite(x).all() or not np.isfinite(mask).all():
        raise ValueError('Nonfinite motion/mask values')
    return {'motion_rows': int(x.shape[0]), 'motion_columns': 6,
            'motion_all_finite': True, 'mask_rows': int(mask.size),
            'mask_all_ones': bool(np.all(mask == 1)),
            'motion_sha256': sha256(text_path), 'mask_sha256': sha256(mask_path)}


def run(pdf, source, summary, tree, motion_dir):
    p = pdf_labels(pdf)
    c = code_labels((source / 'info_scans_conditions.m').read_text())
    if p != c:
        raise ValueError('README and reanalysis S09 lists do not agree')
    r = mat_indices(source / 'rival_ind.mat', 'rival_ind')
    s = mat_indices(source / 'replay_smooth_ind.mat', 'replay_smooth_ind')
    if r != [i+1 for i, x in enumerate(p) if x == 'rivalry'] or s != [i+1 for i, x in enumerate(p) if x == 'replay_smooth']:
        raise ValueError('Condition index MAT arrays do not match scan list')
    inv = json.loads(summary.read_text())
    entries = json.loads(tree.read_text())
    if entries.get('truncated') or entries.get('sha') != COMMIT:
        raise ValueError('GitHub tree is truncated or does not name the pinned revision')
    for repo_path, local_name in [('info_scans_conditions.m', 'info_scans_conditions.m'),
                                  ('data/rival_ind.mat', 'rival_ind.mat'),
                                  ('data/replay_smooth_ind.mat', 'replay_smooth_ind.mat')]:
        candidates = [x for x in entries['tree'] if x['type'] == 'blob' and x['path'] == repo_path]
        if len(candidates) != 1 or git_blob_sha(source / local_name) != candidates[0]['sha']:
            raise ValueError('Condition source blob differs from pinned tree')
    if sorted(rec['scan'] for rec in inv['scans']) != list(range(1, 10)):
        raise ValueError('Expected scans 1 through 9 exactly once')
    rows = []
    for rec in inv['scans']:
        scan = rec['scan']
        matching = [x for x in entries['tree'] if x['type']=='blob' and
                    x['path'].startswith(PREFIX) and f'/scan{scan}/' in x['path']]
        by_ext = {}
        for x in matching:
            ext = x['path'].rsplit('.', 1)[-1]
            if ext not in ('txt', 'mat') or ext in by_ext:
                raise ValueError('Unexpected S09 motion tree entries')
            by_ext[ext] = x
        if set(by_ext) != {'txt', 'mat'}:
            raise ValueError('Missing motion-related Git blobs')
        for ext in ('txt', 'mat'):
            if git_blob_sha(motion_dir / f'scan{scan}.{ext}') != by_ext[ext]['sha']:
                raise ValueError('Local blob hash differs from pinned Git tree')
        m = TAIL.search(by_ext['txt']['path'])
        if not m or int(m.group(1)) != rec['mri_series'] or any(int(m.group(i)) != 1 for i in (2, 3, 4)):
            raise ValueError('Motion filename does not identify expected series and first frame')
        qc = motion_qc(motion_dir / f'scan{scan}.txt', motion_dir / f'scan{scan}.mat', rec['mri_pairs'])
        rows.append({'scan': scan, 'documented_condition': p[scan-1],
                     'mri_series': rec['mri_series'], 'mri_volumes': rec['mri_pairs'],
                     'eeg_triggers': rec['eeg_tr_markers'], **qc})
    return {'kind':'documented scan labels and public motion file QC, not trial or timing validation',
            'pinned_reanalysis_commit':COMMIT, 'readme_pdf_sha256':sha256(pdf),
            'condition_script_sha256':sha256(source/'info_scans_conditions.m'),
            'readme_and_reanalysis_lists_agree':True,
            'rivalry_indices':r, 'smooth_replay_indices':s,
            'instantaneous_replay_indices':[i+1 for i,x in enumerate(p) if x=='replay_inst'],
            'scans':rows,
            'limitations':['README and reanalysis lists may share provenance; agreement is not independent confirmation of acquisition.',
                           'Motion filename series and row counts match MRI inventories; row-by-frame identity and timing are not proven.',
                           'Mask all-ones is descriptive, not an asserted censor convention or quality certificate.',
                           'No original SPM design, per-trial eye/replay mapping or EEG-to-MRI start anchor is established.']}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('pdf', type=Path);p.add_argument('source_dir',type=Path)
    p.add_argument('summary',type=Path);p.add_argument('tree',type=Path);p.add_argument('motion_dir',type=Path)
    a=p.parse_args()
    print(json.dumps(run(a.pdf,a.source_dir,a.summary,a.tree,a.motion_dir),indent=2,allow_nan=False))


if __name__=='__main__':
    main()
