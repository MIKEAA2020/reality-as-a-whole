#!/usr/bin/env python3
"""Post hoc subset consistency diagnostic; no participant-level outputs.

Input hashes, event blobs, parser and provisional join follow the earlier
provenance audit. Subset matches are arithmetic witnesses, not verified trial
selection. See PAINGEN_CONDITION_MEAN_SUBSET_DIAGNOSTIC_PLAN.md.
"""
import argparse
import collections
import io
import json
from pathlib import Path
import tarfile

from paingen_source_crosscheck import bkey, obtain
from paingen_trial_provenance_audit import (
    ARCHIVE_SHA256, ARCHIVE_SIZE, COMMIT, PATH, TREE_SHA256,
    compare_rating, digest, finite, git_blob, parse_run, rating, source_rating,
)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / 'verification/paingen_condition_subset_diagnostic.json'
TOLERANCE = 1e-10
MAX_TRIALS = 10


def classify(trials, target):
    """Find all shared-pair subset witnesses; a trial is (I, U, run)."""
    n = len(trials)
    if not 1 <= n <= MAX_TRIALS:
        raise ValueError('trial count exceeds declared exhaustive-search bound')
    if len(target) != 2 or any(v is None for v in target):
        raise ValueError('finite paired target required')
    matches, intensity_matches, unpleasantness_matches = [], [], []
    for mask in range(1, 1 << n):
        selected = [trials[j] for j in range(n) if mask & (1 << j)]
        means = [sum(t[k] for t in selected) / len(selected) for k in (0, 1)]
        ok_i = abs(means[0]-target[0]) <= TOLERANCE
        ok_u = abs(means[1]-target[1]) <= TOLERANCE
        if ok_i: intensity_matches.append(mask)
        if ok_u: unpleasantness_matches.append(mask)
        if ok_i and ok_u: matches.append(mask)
    full = (1 << n)-1
    if full in matches:
        category = 'full_set_matches'
    elif matches:
        category = 'proper_subset_only'
    else:
        category = 'no_common_subset'
    run_names = {t[2] for t in trials}
    single_run_masks = set()
    if len(run_names) == 2:
        for run in run_names:
            single_run_masks.add(sum(1 << j for j, t in enumerate(trials) if t[2] == run))
    run_matches = [m for m in matches if m in single_run_masks]
    return {'category': category, 'n_trials': n, 'two_runs': len(run_names) == 2,
            'matching_subsets': len(matches), 'whole_single_run_witness': bool(run_matches),
            'unique_witness_whole_single_run': len(matches) == 1 and bool(run_matches),
            'unique_excluded_count': n-matches[0].bit_count() if len(matches) == 1 else None,
            'intensity_only_exists': bool(intensity_matches),
            'unpleasantness_only_exists': bool(unpleasantness_matches)}


def bucket(counter, result):
    counter['eligible_cells'] += 1
    counter[result['category']] += 1
    counter['cells_with_two_recorded_runs'] += result['two_runs']
    if result['category'] == 'proper_subset_only':
        counter['proper_unique_witness' if result['matching_subsets'] == 1 else 'proper_multiple_witnesses'] += 1
        counter['proper_has_whole_single_run_witness'] += result['whole_single_run_witness']
        counter['proper_unique_and_whole_single_run'] += result['unique_witness_whole_single_run']
        if result['unique_excluded_count'] is not None:
            counter['proper_unique_excludes_' + str(result['unique_excluded_count'])] += 1
    if result['category'] == 'no_common_subset':
        counter['no_common_intensity_only_exists'] += result['intensity_only_exists']
        counter['no_common_unpleasantness_only_exists'] += result['unpleasantness_only_exists']
        counter['no_common_both_individually_exist'] += result['intensity_only_exists'] and result['unpleasantness_only_exists']


def obtain_events(treepath, archivepath):
    raw = Path(treepath).read_bytes()
    if digest(raw) != TREE_SHA256:
        raise ValueError('tree digest mismatch')
    tree = json.loads(raw)
    if tree.get('truncated'):
        raise ValueError('tree truncated')
    entries = [z for z in tree['tree'] if z['path'].endswith('_events.tsv')]
    nodes = {z['path']: z for z in entries}
    if len(entries) != 1574 or len(nodes) != 1574:
        raise ValueError('unexpected event count or duplicate path')
    raw = Path(archivepath).read_bytes()
    if len(raw) != ARCHIVE_SIZE or digest(raw) != ARCHIVE_SHA256:
        raise ValueError('archive digest or size mismatch')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:gz') as tf:
        for m in tf:
            if not m.name.endswith('_events.tsv'):
                continue
            parts = m.name.split('/', 1)
            if len(parts) != 2 or parts[0] != 'ds004746-' + COMMIT:
                raise ValueError('archive root mismatch')
            path = parts[1]
            if path in files or path not in nodes or not m.isfile():
                raise ValueError('unexpected or duplicate archive member')
            node = nodes[path]
            if node['mode'] != '100644' or node['type'] != 'blob' or m.size != node['size'] or m.size > 100000:
                raise ValueError('unexpected event blob metadata')
            with tf.extractfile(m) as f:
                data = f.read(100001)
            if len(data) != m.size or git_blob(data) != node['sha']:
                raise ValueError('event blob digest mismatch')
            files[path] = data
    if set(files) != set(nodes):
        raise ValueError('archive/tree event set mismatch')
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--tree', required=True)
    ap.add_argument('--archive', required=True)
    ap.add_argument('--behavior')
    args = ap.parse_args()
    files = obtain_events(args.tree, args.archive)
    source = {}
    for row in obtain('behavior', args.behavior):
        key = bkey(row)
        if key in source:
            raise ValueError('duplicate export key')
        source[key] = row
    cells, seen_person_run = collections.defaultdict(list), set()
    accepted, rejected, episodes = 0, collections.Counter(), 0
    for path, data in sorted(files.items()):
        match = PATH.fullmatch(path)
        if not match:
            raise ValueError('unexpected event path')
        person, run = match['person'], match['run']
        if (person, run) in seen_person_run:
            raise ValueError('duplicate person/run')
        seen_person_run.add((person, run))
        event_rows, failure = parse_run(data)
        if failure:
            rejected[failure] += 1
            continue
        accepted += 1
        for _, stim, first, second in event_rows:
            episodes += 1
            events = {first['trial_type']: first, second['trial_type']: second}
            for field in ('int_rating', 'unp_rating'):
                if compare_rating(stim[field], events[field][field]) != 'both_equal':
                    raise ValueError('unexpected missing or inconsistent event rating')
            i, u = rating(stim['int_rating'])[1], rating(stim['unp_rating'])[1]
            level = finite(stim['level'])
            mapping = {46.5: 3, 47.: 4, 47.5: 5} if stim['trial_type'] == 'heat' else {3.: 3, 4.: 4, 5.: 5}
            if level not in mapping:
                raise ValueError('unsupported stimulus level')
            key = (person, int(stim['trial_type'] == 'heat'), mapping[level], int(run in ('02','03')))
            cells[key].append((i, u, run))
    if accepted != 1566 or episodes != 12528 or len(cells) != 4707:
        raise ValueError('event screening count mismatch')
    overlap = cells.keys() & source.keys()
    if len(overlap) != 4707 or len(source) != 4709:
        raise ValueError('condition-key join count mismatch')
    groups = collections.defaultdict(collections.Counter)
    trial_counts = collections.Counter()
    missing = 0
    for key in overlap:
        row = source[key]
        target = (source_rating(row['Yint']), source_rating(row['Yunp']))
        if any(x is None for x in target):
            missing += 1
            continue
        ans = classify(cells[key], target)
        trial_counts[ans['n_trials']] += 1
        modality = 'thermal' if key[1] else 'mechanical'
        treatment = 'placebo' if key[3] else 'control'
        for label in ('all', 'modality:' + modality, 'treatment:' + treatment):
            bucket(groups[label], ans)
    overall = groups['all']
    if missing != 307 or overall['eligible_cells'] != 4400 or overall['full_set_matches'] != 3780:
        raise ValueError('prior aggregate comparison not reproduced')
    receipt = {
        'status': 'completed',
        'scope': 'Post hoc exact arithmetic on paired BIDS trial values and same-study condition means; subset witnesses do not identify actual source selection.',
        'dataset_commit': COMMIT, 'dataset_tree_sha256': TREE_SHA256,
        'dataset_archive_sha256': ARCHIVE_SHA256,
        'behavior_commit': 'da46f2f9739ad2e9eeb9658711582be6357c1026',
        'behavior_sha256': 'b40b4a1b1e001f2317fea07a49c6ee6de062f181a20affe149fe50a81b58545b',
        'event_files_verified': len(files), 'accepted_runs': accepted,
        'rejected_runs': dict(sorted(rejected.items())), 'episodes': episodes,
        'reconstructed_cells': len(cells), 'source_cells': len(source),
        'overlap': len(overlap), 'export_only': len(source.keys()-cells.keys()),
        'missing_either_export_mean_in_overlap': missing,
        'eligible_trial_count_distribution': {str(k): v for k, v in sorted(trial_counts.items())},
        'groups': {k: dict(sorted(v.items())) for k, v in sorted(groups.items())},
        'tolerance': TOLERANCE, 'max_trials_per_cell': MAX_TRIALS,
        'plan': 'PAINGEN_CONDITION_MEAN_SUBSET_DIAGNOSTIC_PLAN.md',
        'privacy': 'No IDs, trial values, per-person outcomes, or subset masks are written.'}
    OUTPUT.write_text(json.dumps(receipt, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(json.dumps(receipt, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
