#!/usr/bin/env python3
"""Summarize previously audited MRI inventories and conditional EEG gates.

No raw data, condition labels or real alignment are inferred. Image-hash overlap
checks byte-for-byte identity only, not scientific independence.
"""
import argparse
import json
from itertools import combinations
from pathlib import Path


def summarize(items):
    """items: list of (scan number, inventory, conditional gate, sensitivity)."""
    rows, hashes = [], {}
    for scan, inv, gate, sens in items:
        if scan in hashes:
            raise ValueError('Duplicate scan number')
        volumes = inv['volumes']
        frames = [v['frame'] for v in volumes]
        if frames != list(range(1, len(volumes) + 1)):
            raise ValueError('Expected consecutive frames starting at 1')
        if (len(volumes) != inv['volumes_read'] or len(volumes) != gate['mri_volumes']
                or inv['pair_files_read'] != 2 * len(volumes)
                or gate['mri_series'] != inv['series_number']
                or gate['eeg_embedded_series'] != inv['series_number']
                or sens['volumes'] != len(volumes)
                or sens['eeg_sha256'] != gate['eeg_sha256']):
            raise ValueError('Inventory, gate and sensitivity are inconsistent')
        candidates = gate['candidate_first_fmri_frames']
        if not 1 <= gate['eeg_trigger_count'] <= len(volumes):
            raise ValueError('Invalid trigger count for consecutive mapping')
        if candidates != list(range(1, len(volumes) - gate['eeg_trigger_count'] + 2)):
            raise ValueError('Unexpected candidate enumeration')
        if sens['candidate_count'] != len(candidates):
            raise ValueError('Sensitivity candidate count inconsistent')
        payloads = [v['image_sha256'] for v in volumes]
        hashes[scan] = set(payloads)
        rows.append({'scan': scan, 'mri_pairs': len(volumes),
                     'pair_files_read': inv['pair_files_read'],
                     'other_files_ignored': inv['other_files_ignored'],
                     'mri_series': inv['series_number'],
                     'unique_payload_hashes': len(hashes[scan]),
                     'eeg_tr_markers': gate['eeg_trigger_count'],
                     'trigger_spacing_s': gate['trigger_spacing_s'],
                     'conditional_first_frame_candidates': candidates,
                     'descriptive_correlation_range': sens['pearson_r_range']})
    overlap = [{'scans': [a, b], 'shared_image_payload_hashes': len(hashes[a] & hashes[b])}
               for a, b in combinations(sorted(hashes), 2)]
    return {'kind': 'file inventory and conditional alignment summary, not an fMRI contrast',
            'assumptions': ['EEG marker subset maps consecutively and one-to-one to chronologically ordered MRI frames at recorded TR; not independently verified.',
                            'Candidate enumeration is not a count of proven physically feasible alignments.'],
            'limitations': ['Matching series numbers and distinct image hashes do not prove temporal alignment or experimental independence.',
                            'Correlations are exploratory global-mean QC, not nuisance-corrected GLM estimates or consciousness measurements.',
                            'Source ZIPs are not checked against the original release subject archive manifest.'],
            'scans': sorted(rows, key=lambda row: row['scan']),
            'pairwise_payload_hash_overlap': overlap}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('scans', type=int, nargs='+')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    items = []
    for scan in args.scans:
        def read(suffix):
            return json.loads((root / f'roy_s09_scan{scan}_{suffix}.json').read_text())
        items.append((scan, read('full_fmri_inventory'), read('alignment_gate'), read('offset_sensitivity')))
    print(json.dumps(summarize(items), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
