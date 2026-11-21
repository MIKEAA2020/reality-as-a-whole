#!/usr/bin/env python3
"""Pinned, aggregate-only metadata screen; no signals or behavioral scores."""
import csv
import hashlib
import io
import json
import math
import sys
import tarfile
from collections import Counter, defaultdict
from pathlib import Path

COMMIT = 'c4fb7e96fb314b1c222ab9a826ce2a6e565ff6e6'
ARCHIVE_SHA = 'e74bcc9da6c8dc0f1c323705995456e08d6190a2605115c1fac458a651085ef4'
TREE_SHA = '343cc64aaaad93d44fb2a7ed0052d729a621b1f1881ef47d2e9c5ccc19590e55'
TARGET_COUNT = 93
OUT = Path(__file__).with_suffix('.json')


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def numeric_class(value):
    if value is None or value.strip() in ('', 'n/a'):
        return 'missing'
    try:
        n = float(value)
    except ValueError:
        return 'invalid'
    return 'valid' if math.isfinite(n) and n >= 0 else 'invalid'


def timing_class(task, levels, event_values, sidecar):
    """Recognize documented whole-record rows, not their synthetic numeric onset."""
    label = 'recording_' + task
    desc = levels.get(label, '').lower()
    if (set(event_values) == {label} and 'whole' in desc and
            'not annotated' in desc and sidecar.get('TaskName') == task):
        return 'not_annotated_recording_span_only'
    return 'ambiguous'


def target(path):
    return (path.endswith('_events.tsv') or path.endswith('_ieeg.json') or
            path in ('task-stim_events.json', 'task-sps_events.json', 'dataset_description.json'))


def inspect(archive_bytes, tree_bytes):
    if sha256(archive_bytes) != ARCHIVE_SHA or sha256(tree_bytes) != TREE_SHA:
        raise ValueError('pinned archive or tree digest differs')
    tree = json.loads(tree_bytes)
    if tree.get('truncated') is not False or tree.get('sha') != COMMIT:
        raise ValueError('unexpected or truncated tree')
    expected = {x['path']: x for x in tree['tree'] if x['type'] == 'blob' and target(x['path'])}
    if len(expected) != TARGET_COUNT:
        raise ValueError('unexpected target count')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode='r:gz') as tar:
        for member in tar:
            if not member.isfile():
                continue
            prefix, sep, path = member.name.partition('/')
            if not sep or not target(path):
                continue
            if path in files or path not in expected:
                raise ValueError('duplicate or unexpected target')
            content = tar.extractfile(member).read()
            entry = expected[path]
            if len(content) != entry['size'] or blob_sha(content) != entry['sha'] or content.startswith(b'version https://git-lfs.github.com/spec/'):
                raise ValueError('target blob verification failed')
            files[path] = content
    if set(files) != set(expected):
        raise ValueError('target set differs')
    dictionaries = {task: json.loads(files['task-' + task + '_events.json'])['trial_type']['Levels']
                    for task in ('stim', 'sps')}
    if any(set(dictionaries[t]) != {'recording_' + t} for t in dictionaries):
        raise ValueError('unexpected documented event levels')
    people = defaultdict(set)
    keys = set()
    output = {t: {'files': 0, 'rows': 0, 'schema_patterns': Counter(),
                  'onset': Counter(), 'duration': Counter(), 'labels': Counter(),
                  'runs_with_documented_stimulus_or_report_event': 0,
                  'timing_documentation': Counter()} for t in ('stim', 'sps')}
    for path, data in files.items():
        if not path.endswith('_events.tsv'):
            continue
        parts = path.split('/')
        if len(parts) != 3 or not parts[0].startswith('sub-') or parts[1] != 'ieeg' or not parts[2].startswith(parts[0] + '_'):
            raise ValueError('unexpected event path structure')
        tasks = [t for t in ('stim', 'sps') if '_task-' + t + '_' in parts[2]]
        if len(tasks) != 1:
            raise ValueError('ambiguous task')
        task = tasks[0]
        key = path[:-len('_events.tsv')]
        if key in keys:
            raise ValueError('duplicate run key')
        keys.add(key)
        sidepath = key + '_ieeg.json'
        if sidepath not in files:
            raise ValueError('missing matching sidecar')
        sidecar = json.loads(files[sidepath])
        reader = csv.DictReader(io.StringIO(data.decode('utf-8-sig')), delimiter='\t')
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames) or not {'onset', 'duration', 'trial_type'} <= set(reader.fieldnames):
            raise ValueError('invalid event schema')
        rows = list(reader)
        if not rows or any(None in row or None in row.values() for row in rows):
            raise ValueError('empty or malformed event table')
        entry = output[task]
        entry['files'] += 1
        entry['rows'] += len(rows)
        entry['schema_patterns'][', '.join(sorted(reader.fieldnames))] += 1
        for row in rows:
            entry['onset'][numeric_class(row['onset'])] += 1
            entry['duration'][numeric_class(row['duration'])] += 1
            # Only documented values are printed; unexpected labels trigger stop.
            if row['trial_type'] not in dictionaries[task]:
                raise ValueError('undocumented event label; interpretation stopped')
            entry['labels'][row['trial_type']] += 1
        entry['timing_documentation'][timing_class(task, dictionaries[task],
                                                       [r['trial_type'] for r in rows], sidecar)] += 1
        # The only documented labels are whole-recording spans, not stimulus or report events.
        people[task].add(parts[0])
    if {p[:-len('_ieeg.json')] for p in files if p.endswith('_ieeg.json')} != keys:
        raise ValueError('unpaired sidecars')
    for task in output:
        output[task]['people'] = len(people[task])
    return {'commit': COMMIT, 'archive_sha256': ARCHIVE_SHA, 'tree_sha256': TREE_SHA,
            'verified_target_blobs': len(files), 'tasks': output,
            'people_with_both_tasks': len(people['stim'] & people['sps']),
            'limitations': ['person overlap is not contact, block, or trial pairing',
                            'recording-span onset is not stimulation or report onset',
                            'no outcome, behavioral table, or neural signal inspected']}


def main():
    if len(sys.argv) != 3:
        raise SystemExit('usage: python rao_stim_metadata_readiness.py ARCHIVE TREE_JSON')
    result = inspect(Path(sys.argv[1]).read_bytes(), Path(sys.argv[2]).read_bytes())
    rendered = json.dumps(result, indent=2, sort_keys=True) + '\n'
    OUT.write_text(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
