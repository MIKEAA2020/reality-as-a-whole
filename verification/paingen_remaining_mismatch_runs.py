#!/usr/bin/env python3
"""Retrospective run-completeness diagnostic; no individual-level output."""
import argparse
import collections
import json
from pathlib import Path

from paingen_condition_subset_diagnostic import classify, obtain_events
from paingen_response_time_reconstruction import compare_cell, rt_status
from paingen_source_crosscheck import bkey, obtain
from paingen_trial_provenance_audit import (
    ARCHIVE_SHA256, COMMIT, PATH, TREE_SHA256, compare_rating, finite,
    parse_run, rating, source_rating,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'verification/paingen_remaining_mismatch_runs.json'


def run_category(statuses):
    counts = collections.Counter(statuses)
    if len(statuses) != 2 or any(s not in ('accepted', 'rejected', 'absent') for s in statuses):
        raise ValueError('invalid relevant-run status')
    if counts['accepted'] == 2:
        return 'two_accepted'
    if counts['accepted'] == 1 and counts['rejected'] == 1:
        return 'one_accepted_one_rejected'
    if counts['accepted'] == 1 and counts['absent'] == 1:
        return 'one_accepted_one_absent'
    raise ValueError('overlapping cell must have an accepted relevant run')


def dimension(flags):
    if flags == (True, True):
        return 'both_match'
    if flags == (False, False):
        return 'both_mismatch'
    if flags == (False, True):
        return 'intensity_only_mismatch'
    if flags == (True, False):
        return 'unpleasantness_only_mismatch'
    raise ValueError('invalid comparison flags')


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
            raise ValueError('duplicate source key')
        source[key] = row
    cells = collections.defaultdict(list)
    run_status = {}
    accepted, rejected, episodes = 0, collections.Counter(), 0
    for path, data in sorted(files.items()):
        match = PATH.fullmatch(path)
        if not match:
            raise ValueError('unexpected event path')
        person, run = match['person'], match['run']
        if (person, run) in run_status:
            raise ValueError('duplicate person/run')
        parsed, reason = parse_run(data)
        run_status[(person, run)] = 'rejected' if reason else 'accepted'
        if reason:
            rejected[reason] += 1
            continue
        accepted += 1
        for _, stim, first, second in parsed:
            episodes += 1
            events = {first['trial_type']: first, second['trial_type']: second}
            for f in ('int_rating', 'unp_rating'):
                if compare_rating(stim[f], events[f][f]) != 'both_equal':
                    raise ValueError('event rating mismatch')
            if 'response_time' not in events['int_rating']:
                raise ValueError('missing RT schema')
            rt = finite(events['int_rating']['response_time'])
            if rt_status(rt) == 'unavailable':
                raise ValueError('unavailable RT')
            level = finite(stim['level'])
            mapping = {46.5: 3, 47.: 4, 47.5: 5} if stim['trial_type'] == 'heat' else {3.: 3, 4.: 4, 5.: 5}
            if level not in mapping:
                raise ValueError('unsupported level')
            key = (person, int(stim['trial_type'] == 'heat'), mapping[level], int(run in ('02', '03')))
            cells[key].append((rating(stim['int_rating'])[1], rating(stim['unp_rating'])[1], run, rt))
    if accepted != 1566 or episodes != 12528 or len(cells) != 4707:
        raise ValueError('event counts changed')
    overlap = source.keys() & cells.keys()
    if len(overlap) != 4707 or len(source) != 4709:
        raise ValueError('join counts changed')
    categories = collections.defaultdict(collections.Counter)
    people = collections.defaultdict(set)
    mismatch_dimensions, mismatch_retained = collections.Counter(), collections.Counter()
    mismatch_strata = collections.defaultdict(collections.Counter)
    missing, subset_missing = 0, 0
    for key in overlap:
        target = (source_rating(source[key]['Yint']), source_rating(source[key]['Yunp']))
        if any(v is None for v in target):
            missing += 1
            continue
        result = compare_cell(cells[key], target)
        if result['new'] is None:
            raise ValueError('unexpected unresolved RT reconstruction')
        label = 'match' if all(result['new']) else 'mismatch'
        runs = ('02', '03') if key[3] else ('01', '04')
        category = run_category([run_status.get((key[0], r), 'absent') for r in runs])
        categories[category][label] += 1
        people[(category, label)].add(key[0])
        if label == 'mismatch':
            witness = classify([(i, u, run) for i, u, run, _ in cells[key]], target)
            if witness['category'] != 'no_common_subset':
                raise ValueError('unmatched cell has a subset witness')
            subset_missing += 1
            mismatch_dimensions[dimension(result['new'])] += 1
            mismatch_retained[str(result['retained'])] += 1
            for strata, value in (('modality', 'thermal' if key[1] else 'mechanical'),
                                  ('treatment', 'placebo' if key[3] else 'control')):
                mismatch_strata[strata + ':' + value][category] += 1
    if (missing != 307 or sum(c['match'] for c in categories.values()) != 4365 or
            sum(c['mismatch'] for c in categories.values()) != 35 or subset_missing != 35):
        raise ValueError('prior results not reproduced')
    for category in ('two_accepted', 'one_accepted_one_rejected', 'one_accepted_one_absent'):
        for label in ('match', 'mismatch'):
            categories[category][label] += 0
            people[(category, label)]  # explicit empty set
    receipt = {'status': 'completed', 'scope': 'Post-result descriptive run completeness, not evidence of causal inclusion or original pipeline.',
               'dataset_commit': COMMIT, 'tree_sha256': TREE_SHA256, 'archive_sha256': ARCHIVE_SHA256,
               'behavior_commit': 'da46f2f9739ad2e9eeb9658711582be6357c1026',
               'behavior_sha256': 'b40b4a1b1e001f2317fea07a49c6ee6de062f181a20affe149fe50a81b58545b',
               'verified_event_files': len(files), 'accepted_runs': accepted, 'rejected_runs': dict(rejected),
               'episodes': episodes, 'overlap': len(overlap), 'missing_export': missing,
               'cell_counts_by_relevant_run_category': {k: dict(sorted(v.items())) for k, v in sorted(categories.items())},
               'distinct_people_by_category_and_match_status': {k: {label: len(people[(k, label)]) for label in ('match', 'mismatch')} for k in sorted(categories)},
               'mismatch_dimensions': dict(sorted(mismatch_dimensions.items())),
               'mismatch_retained_trial_count_distribution': dict(sorted(mismatch_retained.items())),
               'mismatch_run_category_by_strata': {k: dict(sorted(v.items())) for k, v in sorted(mismatch_strata.items())},
               'plan': 'PAINGEN_REMAINING_MISMATCH_RUN_COMPLETENESS_PLAN.md',
               'privacy': 'No IDs, trial rows, demographic data or individual outcomes are written.'}
    OUT.write_text(json.dumps(receipt, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(json.dumps(receipt, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
