#!/usr/bin/env python3
"""Synthetic controls; not a validation of any real alignment."""
from copy import deepcopy
from roy_s09_mri_multi_scan_summary import summarize


def item(scan, payloads, triggers):
    n = len(payloads)
    inv = {'volumes': [{'frame': i+1, 'image_sha256': x} for i, x in enumerate(payloads)],
           'volumes_read': n, 'pair_files_read': n*2, 'other_files_ignored': 0, 'series_number': scan}
    gate = {'mri_volumes': n, 'mri_series': scan, 'eeg_embedded_series': scan,
            'eeg_trigger_count': triggers, 'trigger_spacing_s': 2.2, 'eeg_sha256': 'example',
            'candidate_first_fmri_frames': list(range(1, n-triggers+2))}
    sens = {'volumes': n, 'eeg_sha256': 'example', 'candidate_count': n-triggers+1,
            'pearson_r_range': [-0.2, 0.3]}
    return scan, inv, gate, sens


def main():
    one, two = item(1, ['a', 'b', 'c'], 2), item(2, ['d', 'a'], 1)
    result = summarize([one, two])
    assert result['scans'][0]['conditional_first_frame_candidates'] == [1, 2]
    assert result['pairwise_payload_hash_overlap'][0]['shared_image_payload_hashes'] == 1
    bad = deepcopy(one)
    bad[2]['mri_series'] = 9
    for inputs in ([bad], [one, one]):
        try:
            summarize(inputs)
        except ValueError:
            pass
        else:
            raise AssertionError('inconsistent input must stop')
    print('PASS: synthetic summary, overlap, incompatible series and duplicate stop')


if __name__ == '__main__':
    main()
