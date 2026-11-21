#!/usr/bin/env python3
"""Audit released PAINgen BIDS event provenance; aggregate output only.

Inputs are local pinned GitHub tree and archive. Does not extract the archive,
read MRI/participant metadata, or write participant identifiers or events.
See PAINGEN_TRIAL_PROVENANCE_ORDER_FIXED_PLAN.md for interpretation.
"""
import argparse
import collections
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import re
import tarfile

from paingen_source_crosscheck import obtain, bkey

ROOT = Path(__file__).resolve().parent.parent
COMMIT = '8a38ee30b870373547676bf0d0638e16160472a1'
TREE_SHA256 = '4a68281dc147b8436167466550ec5dedb4abb9fc86c27291a5a21fe60769799f'
ARCHIVE_SHA256 = 'b8a04bcc0130edcd65067ccdc98e6f480b403f6165417898f8292f48148a8be7'
ARCHIVE_SIZE = 2954589
PATH = re.compile(r'^sub-(?P<person>[^/]+)/ses-(?P<session>[^/]+)/func/sub-(?P=person)_ses-(?P=session)_task-paingen_dir-pa_run-(?P<run>0[1-4])_events\.tsv$')
COLUMNS = {'onset', 'duration', 'trial_type', 'int_rating', 'unp_rating', 'level'}
OUT = ROOT / 'verification/paingen_trial_provenance_audit.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def rating(value):
    if value is None or value.strip().lower() in ('n/a', 'na', ''):
        return ('missing', None)
    try:
        x = float(value)
    except ValueError:
        return ('invalid', None)
    if not math.isfinite(x) or not 0 <= x <= 1:
        return ('invalid', None)
    return ('valid', x)


def finite(value):
    try:
        x = float(value)
    except (ValueError, TypeError):
        return None
    return x if math.isfinite(x) else None


def percentile(values, q):
    values = sorted(values)
    pos = q * (len(values) - 1); lo = int(pos); hi = min(lo+1, len(values)-1)
    return values[lo] + (values[hi]-values[lo])*(pos-lo)


def summarize(values, invalid):
    if not values:
        return {'finite_positive': 0, 'invalid_or_nonpositive': invalid}
    return {'finite_positive': len(values), 'invalid_or_nonpositive': invalid,
            'min': min(values), 'p25': percentile(values, .25),
            'median': percentile(values, .5), 'p75': percentile(values, .75), 'max': max(values)}


def parse_run(data):
    reader = csv.DictReader(io.StringIO(data.decode('utf-8-sig'), newline=''), delimiter='\t')
    if not COLUMNS.issubset(reader.fieldnames or []):
        return None, 'schema'
    rows = list(reader)
    if not rows:
        return None, 'header_only'
    times = [finite(r['onset']) for r in rows]
    if any(t is None for t in times):
        return None, 'invalid_onset'
    # Post-inspection amendment: chronological onset, not source row order.
    # Sorting is only allowed when every onset is distinct.
    if len(set(times)) != len(times):
        return None, 'tied_onsets'
    rows = [r for _, r in sorted(zip(times, rows), key=lambda x: x[0])]
    if len(rows) != 32:
        return None, 'row_count_not_32'
    episodes = []
    for k in range(0, len(rows), 4):
        cue, stim, first, second = rows[k:k+4]
        if (cue['trial_type'] != 'warning_cue' or stim['trial_type'] not in ('heat', 'press') or
                {first['trial_type'], second['trial_type']} != {'int_rating', 'unp_rating'}):
            return None, 'episode_grammar'
        episodes.append((cue, stim, first, second))
    return episodes, None


def compare_rating(a, b):
    sa, va = rating(a); sb, vb = rating(b)
    if 'invalid' in (sa, sb):
        return 'invalid_at_least_one'
    if sa == sb == 'missing':
        return 'both_missing'
    if 'missing' in (sa, sb):
        return 'one_missing'
    return 'both_equal' if abs(va-vb) <= 1e-10 else 'both_unequal'


def source_rating(value):
    if value is None or value.strip().lower() in ('', 'n/a', 'na', 'nan'):
        return None
    status, val = rating(value)
    if status != 'valid':
        raise ValueError('invalid or out-of-range source rating')
    return val


def mean_comparison(reconstructed, source):
    """Compare identical condition keys, retaining missing-field categories."""
    overlap = reconstructed.keys() & source.keys()
    counts = collections.Counter()
    max_abs = None
    for key in overlap:
        for f in ('Yint', 'Yunp'):
            vals = reconstructed[key][f]
            a = sum(vals)/len(vals) if vals else None
            b = source_rating(source[key][f])
            if a is None and b is None:
                label = 'both_missing'
            elif a is None:
                label = 'reconstruction_missing_only'
            elif b is None:
                label = 'export_missing_only'
            else:
                diff = abs(a-b)
                max_abs = diff if max_abs is None else max(max_abs, diff)
                label = 'both_equal' if diff <= 1e-10 else 'both_unequal'
            counts[f + '_' + label] += 1
    return {'reconstructed_keys': len(reconstructed), 'export_keys': len(source),
            'overlap_keys': len(overlap), 'reconstructed_only_keys': len(reconstructed.keys()-source.keys()),
            'export_only_keys': len(source.keys()-reconstructed.keys()),
            'outcomes': dict(sorted(counts.items())), 'maximum_finite_absolute_difference': max_abs}


def posthoc_strata(reconstructed, source, accepted_runs):
    strata = collections.defaultdict(collections.Counter)
    overall = collections.Counter()
    for key in reconstructed.keys() & source.keys():
        flags = []
        for field in ('Yint', 'Yunp'):
            vals = reconstructed[key][field]
            a = sum(vals)/len(vals) if vals else None
            b = source_rating(source[key][field])
            flags.append(None if a is None or b is None else abs(a-b) > 1e-10)
        if any(x is None for x in flags):
            label = 'either_mean_missing'
        elif flags == [False, False]:
            label = 'both_equal'
        elif flags == [True, True]:
            label = 'both_unequal'
        elif flags == [True, False]:
            label = 'intensity_only_unequal'
        else:
            label = 'unpleasantness_only_unequal'
        modality = 'thermal' if key[1] == 1 else 'mechanical'
        treatment = 'placebo' if key[3] == 1 else 'control'
        completion = 'four_accepted_runs' if len(accepted_runs[key[0]]) == 4 else 'fewer_accepted_runs'
        for dim, value in [('modality', modality), ('treatment', treatment), ('run_completion', completion)]:
            strata[dim + ':' + value][label] += 1
        overall[label] += 1
    return {'scope': 'Post-result descriptive diagnostic; no revised mapping or exclusion.',
            'overall': dict(sorted(overall.items())),
            'strata': {k: dict(sorted(v.items())) for k, v in sorted(strata.items())}}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--tree', required=True)
    ap.add_argument('--archive', required=True)
    ap.add_argument('--behavior', help='local exact pinned author CSV; default fetches pinned source')
    args = ap.parse_args()
    treebytes = Path(args.tree).read_bytes()
    if digest(treebytes) != TREE_SHA256:
        raise ValueError('pinned GitHub tree SHA-256 mismatch')
    tree = json.loads(treebytes)
    if tree.get('truncated'):
        raise ValueError('truncated tree')
    nodes = {z['path']: z for z in tree['tree'] if z['path'].endswith('_events.tsv')}
    if len(nodes) != 1574:
        raise ValueError('event tree count mismatch')
    archive = Path(args.archive).read_bytes()
    if len(archive) != ARCHIVE_SIZE or digest(archive) != ARCHIVE_SHA256:
        raise ValueError('archive size or SHA-256 mismatch')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as tf:
        for m in tf:
            if not m.name.endswith('_events.tsv'):
                continue
            parts = m.name.split('/', 1)
            if len(parts) != 2 or parts[0] != 'ds004746-' + COMMIT:
                raise ValueError('unexpected archive member root')
            path = parts[1]
            if path in files or path not in nodes or not m.isfile():
                raise ValueError('duplicate or unexpected event archive member')
            node = nodes[path]
            if node['type'] != 'blob' or node['mode'] != '100644' or m.size != node['size'] or m.size > 100000:
                raise ValueError('unexpected event blob type or size')
            f = tf.extractfile(m)
            data = f.read(100001)
            if len(data) != m.size or git_blob(data) != node['sha']:
                raise ValueError('event blob verification failed')
            files[path] = data
    if set(files) != set(nodes):
        raise ValueError('archive event set does not equal tree')

    source = {}
    for row in obtain('behavior', args.behavior):
        key = bkey(row)
        if key in source:
            raise ValueError('duplicate source key')
        source[key] = row

    reason = collections.Counter(); order = collections.Counter()
    orders_by_person = collections.defaultdict(set)
    order_by_run = collections.defaultdict(collections.Counter)
    duration_values = collections.defaultdict(list); duration_invalid = collections.Counter()
    agreement = {field: collections.Counter() for field in ('int_rating', 'unp_rating')}
    ratings = {field: collections.Counter() for field in ('int_rating', 'unp_rating')}
    reconstructed = {}; counts_by_outcome = {'Yint': [], 'Yunp': []}
    seen_person_run = set(); level_values = collections.defaultdict(set)
    episodes_count = 0
    source_order_inversions = 0
    rating_interval = collections.Counter()
    accepted_runs = collections.defaultdict(set)
    for path in sorted(files):
        match = PATH.fullmatch(path)
        if not match:
            raise ValueError('event path does not match pinned BIDS pattern')
        person, run = match['person'], match['run']
        if (person, run) in seen_person_run:
            raise ValueError('duplicate person/run across sessions')
        seen_person_run.add((person, run))
        r = csv.DictReader(io.StringIO(files[path].decode('utf-8-sig'), newline=''), delimiter='\t')
        original_times = [finite(x.get('onset')) for x in r] if 'onset' in (r.fieldnames or []) else []
        if all(t is not None for t in original_times) and any(a > b for a, b in zip(original_times, original_times[1:])):
            source_order_inversions += 1
        episodes, failure = parse_run(files[path])
        if failure:
            reason[failure] += 1
            continue
        reason['accepted'] += 1
        accepted_runs[person].add(run)
        for cue, stim, first, second in episodes:
            episodes_count += 1
            first_type = first['trial_type']
            order[first_type] += 1; order_by_run[run][first_type] += 1
            orders_by_person[person].add(first_type)
            duration1, duration2 = finite(first['duration']), finite(second['duration'])
            if duration1 is None or duration2 is None or duration1 <= 0 or duration2 <= 0:
                rating_interval['missing_or_nonpositive_duration'] += 1
            elif float(first['onset']) + duration1 > float(second['onset']):
                rating_interval['first_end_after_second_start'] += 1
            else:
                rating_interval['first_end_at_or_before_second_start'] += 1
            for event in (cue, stim, first, second):
                category = event['trial_type']
                duration = finite(event['duration'])
                if duration is None or duration <= 0:
                    duration_invalid[category] += 1
                else:
                    duration_values[category].append(duration)
            evs = {first['trial_type']: first, second['trial_type']: second}
            for field in agreement:
                agreement[field][compare_rating(stim[field], evs[field][field])] += 1
                status, val = rating(stim[field]); ratings[field][status] += 1
            level = finite(stim['level'])
            level_values[stim['trial_type']].add(level)
            mapping = {46.5: 3, 47.: 4, 47.5: 5} if stim['trial_type'] == 'heat' else {3.: 3, 4.: 4, 5.: 5}
            if level not in mapping:
                raise ValueError('unsupported level; stop condition prevents output')
            key = (person, int(stim['trial_type'] == 'heat'), mapping[level], int(run in ('02', '03')))
            entry = reconstructed.setdefault(key, {'Yint': [], 'Yunp': []})
            for field, output in [('int_rating', 'Yint'), ('unp_rating', 'Yunp')]:
                status, val = rating(stim[field])
                if status == 'valid':
                    entry[output].append(val)

    if not episodes_count:
        raise ValueError('no accepted episodes; stop mean comparison')
    persons_order = collections.Counter('both' if len(v)==2 else next(iter(v)) for v in orders_by_person.values())
    for entry in reconstructed.values():
        for field in counts_by_outcome:
            counts_by_outcome[field].append(len(entry[field]))
    count_distributions = {f: {str(k): v for k, v in sorted(collections.Counter(x).items())}
                           for f, x in counts_by_outcome.items()}
    result = {'status': 'completed',
              'scope': 'BIDS event and same-study condition-export provenance, not validated physical timing, q, cause, subject boundaries or experiential identity.',
              'sources': {'dataset_version': '1.0.0', 'commit': COMMIT,
                          'tree_sha256': TREE_SHA256, 'archive_sha256': ARCHIVE_SHA256,
                          'archive_bytes': ARCHIVE_SIZE, 'dataset_declared_license': 'CC0',
                          'behavior_commit': 'da46f2f9739ad2e9eeb9658711582be6357c1026',
                          'behavior_sha256': 'b40b4a1b1e001f2317fea07a49c6ee6de062f181a20affe149fe50a81b58545b'},
              'event_files_verified': len(files), 'file_outcomes': dict(sorted(reason.items())),
              'files_with_inversions_in_original_row_order': source_order_inversions,
              'accepted_episode_count': episodes_count,
              'rating_order_counts': dict(sorted(order.items())),
              'rating_interval_relationship': dict(sorted(rating_interval.items())),
              'rating_order_by_run': {k: dict(sorted(v.items())) for k, v in sorted(order_by_run.items())},
              'people_by_recorded_order': dict(sorted(persons_order.items())),
              'stimulus_row_rating_status': {k: dict(sorted(v.items())) for k, v in agreement.items()},
              'stimulus_row_validity': {k: dict(sorted(v.items())) for k, v in ratings.items()},
              'event_duration_seconds': {k: summarize(duration_values[k], duration_invalid[k])
                                         for k in ('warning_cue','heat','press','int_rating','unp_rating')},
              'observed_stimulus_levels': {k: sorted(v, key=lambda x: (x is None, x)) for k, v in level_values.items()},
              'contributors_per_reconstructed_mean': count_distributions,
              'behavioral_mean_comparison': mean_comparison(reconstructed, source),
              'posthoc_mean_discrepancy_strata': posthoc_strata(reconstructed, source, accepted_runs),
              'plan': 'PAINGEN_TRIAL_PROVENANCE_ORDER_FIXED_PLAN.md',
              'amendment': 'PAINGEN_TRIAL_PROVENANCE_ORDER_PLAN_AMENDMENT.md',
              'privacy': 'No participant or family identifiers or individual observations are written.'}
    OUT.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
