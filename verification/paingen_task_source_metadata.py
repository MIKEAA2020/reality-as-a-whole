#!/usr/bin/env python3
"""Verify pinned public task *source*, not subject records or trial outcomes."""
import argparse
import hashlib
import json
from pathlib import Path

COMMIT = '89ec44cc82d09a6cddced6e7fcf2dd73c8a87281'
PREFIX = '2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms/'
BLOBS = {
    'generate_ts_pain_test.m': ('8df967543bb5e4d72fdd3ce975cee9b97b64a9cc', 4000),
    'main.m': ('79704eb0e40b7a541de71410bdc43617bf80493b', 45376),
    'get_overallratings.m': ('9a1b691418ca1515f844d3790fce10d5bb497cd8', 3487),
    'parse_trial_sequence.m': ('685763cc8ee907e2a2de6165e0662008cf531e1b', 2202),
    'RUN_cond_and_test.m': ('cc3c0b719ad384e69c7f090dfaed2e4355ff7968', 1407),
    'generate_ts_pain_only_test.m': ('4d6a7bc547174355b0773152b5a63820d27ddedf', 2933),
}
FRAGMENTS = {
    'generate_ts_pain_test.m': ("n_stim = 8;", "prompt_order = prompt_order(randperm(size(prompt_order,1)),:);", "'overall_int', 'overall_unpleasant'"),
    'main.m': ("data.version = 'PAINGEN_v1_09-16-2018_BogdanPetre';", "get_overallratings(overall_types, data, rating_types, run_i, tr_i)"),
    'get_overallratings.m': ("if cur_t-start_t >= 5", "'_RT = end_t-start_t;'") ,
    'parse_trial_sequence.m': ("'How INTENSE was the pain?'", "'How UNPLEASANT was the pain?'"),
    'RUN_cond_and_test.m': ('generate_ts_pain_only_test',),
    'generate_ts_pain_only_test.m': ("S1{2} = repmat({'overall_expect'; 'overall_int'}, 8, 1);",),
}


def verify(tree, files):
    if tree.get('sha') != COMMIT or tree.get('truncated') is not False or not isinstance(tree.get('tree'), list):
        raise ValueError('wrong commit, truncated or malformed tree')
    entries = {}
    for entry in tree['tree']:
        path = entry['path']
        if path in entries:
            raise ValueError('duplicate tree path')
        entries[path] = entry
    verified = {}
    for name, (expected, size) in BLOBS.items():
        row = entries.get(PREFIX + name, {})
        if row.get('type') != 'blob' or row.get('sha') != expected or row.get('size') != size:
            raise ValueError('source tree entry mismatch: ' + name)
        blob = files[name]
        actual = hashlib.sha1(b'blob ' + str(len(blob)).encode() + b'\0' + blob).hexdigest()
        if len(blob) != size or actual != expected:
            raise ValueError('source blob mismatch: ' + name)
        text = blob.decode('utf-8')
        if not all(fragment in text for fragment in FRAGMENTS[name]):
            raise ValueError('source content structure mismatch: ' + name)
        verified[name] = {'git_blob_sha1': actual, 'sha256': hashlib.sha256(blob).hexdigest(), 'size': size}
    return {'source_commit': COMMIT, 'tree_entries': len(entries), 'truncated': False,
            'verified_source_files': verified,
            'scope': 'source-code identity checks only; no raw logs, event rows or outcomes'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--tree', required=True, type=Path)
    p.add_argument('--source-dir', required=True, type=Path)
    args = p.parse_args()
    tree = json.loads(args.tree.read_text())
    files = {name: (args.source_dir/name).read_bytes() for name in BLOBS}
    result = verify(tree, files)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
