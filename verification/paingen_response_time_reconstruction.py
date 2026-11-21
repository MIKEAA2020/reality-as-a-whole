#!/usr/bin/env python3
"""Reconstruct candidate published RT screening; aggregates only, no MRI.

This is not the verified original pipeline. See the fixed retrospective plan.
"""
import argparse
import collections
import json
from pathlib import Path

from paingen_condition_subset_diagnostic import obtain_events, classify
from paingen_source_crosscheck import bkey, obtain
from paingen_trial_provenance_audit import (
    ARCHIVE_SHA256, COMMIT, PATH, TREE_SHA256, compare_rating, finite,
    parse_run, rating, source_rating,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'verification/paingen_response_time_reconstruction.json'
TOL = 1e-10


def rt_status(value):
    x = finite(value)
    if x is None:
        return 'unavailable'
    if x < 0.02:
        return 'below'
    if x > 5.01:
        return 'above'
    return 'in_range'


def compare_cell(trials, target):
    """Trial tuples (intensity, unpleasantness, run, RT). No RT is imputed."""
    if not trials or len(target) != 2 or any(v is None for v in target):
        raise ValueError('expected nonempty trials and finite pair of target means')
    raw = tuple(sum(row[k] for row in trials)/len(trials) for k in (0,1))
    old = tuple(abs(raw[k]-target[k]) <= TOL for k in (0,1))
    counts = collections.Counter(rt_status(t[3]) for t in trials)
    if counts['unavailable']:
        return {'old': old, 'new': None, 'reason': 'unavailable_rt', 'removed': None, 'retained': None}
    keep = [t for t in trials if rt_status(t[3]) == 'in_range']
    if not keep:
        return {'old': old, 'new': None, 'reason': 'no_retained_trials', 'removed': len(trials), 'retained': 0}
    filtered = tuple(sum(t[k] for t in keep)/len(keep) for k in (0,1))
    new = tuple(abs(filtered[k]-target[k]) <= TOL for k in (0,1))
    return {'old': old, 'new': new, 'reason': None, 'removed': len(trials)-len(keep), 'retained': len(keep)}


def missing_cell(counter, trials, target):
    """Post-result diagnostic of missing exported ratings; no imputation."""
    counter['keys'] += 1
    counter['both_ratings_missing' if all(x is None for x in target) else 'one_rating_missing'] += 1
    counts = collections.Counter(rt_status(t[3]) for t in trials)
    counter['recorded_trial_pairs'] += len(trials)
    for status in ('below', 'in_range', 'above', 'unavailable'):
        counter['rt_' + status] += counts[status]
    if counts['unavailable']:
        counter['any_unavailable_rt'] += 1
    elif counts['in_range']:
        counter['at_least_one_rt_in_range'] += 1
    else:
        counter['all_recorded_rt_outside_range'] += 1


def transition(old, new):
    return ('match' if old else 'mismatch') + '_to_' + ('match' if new else 'mismatch')


def count_cell(counter, result):
    counter['eligible'] += 1
    old = all(result['old'])
    counter['prior_pair_match' if old else 'prior_pair_mismatch'] += 1
    for i, label in enumerate(('intensity', 'unpleasantness')):
        counter['prior_' + label + ('_match' if result['old'][i] else '_mismatch')] += 1
    if result['reason']:
        counter['unresolved_' + result['reason']] += 1
        counter['unresolved_prior_' + ('match' if old else 'mismatch')] += 1
        return
    counter['resolved'] += 1
    counter['pair_' + transition(old, all(result['new']))] += 1
    for i, label in enumerate(('intensity', 'unpleasantness')):
        counter[label + '_' + transition(result['old'][i], result['new'][i])] += 1
    counter['cells_changed_membership'] += result['removed'] > 0
    counter['removed_trial_pairs_in_resolved_cells'] += result['removed']
    counter['retained_trial_pairs_in_resolved_cells'] += result['retained']


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
    cells, seen = collections.defaultdict(list), set()
    accepted, rejected, episodes = 0, collections.Counter(), 0
    rt_counts = collections.Counter()
    for path, data in sorted(files.items()):
        match = PATH.fullmatch(path)
        if not match:
            raise ValueError('unexpected BIDS path')
        person, run = match['person'], match['run']
        if (person, run) in seen:
            raise ValueError('duplicate person/run')
        seen.add((person, run))
        parsed, reason = parse_run(data)
        if reason:
            rejected[reason] += 1
            continue
        accepted += 1
        for _, stim, first, second in parsed:
            episodes += 1
            events = {first['trial_type']: first, second['trial_type']: second}
            for f in ('int_rating', 'unp_rating'):
                if compare_rating(stim[f], events[f][f]) != 'both_equal':
                    raise ValueError('rating mismatch in event fields')
            if 'response_time' not in events['int_rating']:
                raise ValueError('missing response_time column')
            rt = finite(events['int_rating']['response_time'])
            rt_counts[rt_status(rt)] += 1
            if rt == 0.02: rt_counts['exact_lower_boundary'] += 1
            if rt == 5.01: rt_counts['exact_upper_boundary'] += 1
            level = finite(stim['level'])
            mapping = {46.5: 3, 47.: 4, 47.5: 5} if stim['trial_type'] == 'heat' else {3.: 3, 4.: 4, 5.: 5}
            if level not in mapping:
                raise ValueError('unsupported level')
            key = (person, int(stim['trial_type'] == 'heat'), mapping[level], int(run in ('02','03')))
            cells[key].append((rating(stim['int_rating'])[1], rating(stim['unp_rating'])[1], run, rt))
    if accepted != 1566 or episodes != 12528 or len(cells) != 4707:
        raise ValueError('prior event count changed')
    overlap = cells.keys() & source.keys()
    if len(overlap) != 4707 or len(source) != 4709:
        raise ValueError('prior export join count changed')
    groups = collections.defaultdict(collections.Counter)
    missing = 0
    eligible_trial_pairs = 0
    missing_diagnostic = collections.Counter()
    prior_subset = collections.Counter()
    rt_screen_fixes_no_subset = 0
    for key in overlap:
        target = (source_rating(source[key]['Yint']), source_rating(source[key]['Yunp']))
        if any(x is None for x in target):
            missing += 1
            missing_cell(missing_diagnostic, cells[key], target)
            continue
        trials = cells[key]
        eligible_trial_pairs += len(trials)
        result = compare_cell(trials, target)
        modality = 'thermal' if key[1] else 'mechanical'
        treatment = 'placebo' if key[3] else 'control'
        for group in ('all', 'modality:' + modality, 'treatment:' + treatment):
            count_cell(groups[group], result)
        if not all(result['old']):
            prior = classify([(i,u,run) for i,u,run,_ in trials], target)['category']
            prior_subset[prior] += 1
            if prior == 'no_common_subset' and result['new'] is not None and all(result['new']):
                rt_screen_fixes_no_subset += 1
    if missing != 307 or groups['all']['eligible'] != 4400 or groups['all']['prior_pair_match'] != 3780:
        raise ValueError('prior comparison counts changed')
    if prior_subset['proper_subset_only'] != 585 or prior_subset['no_common_subset'] != 35:
        raise ValueError('prior subset counts changed')
    if rt_screen_fixes_no_subset:
        raise ValueError('filtered subset match contradicts exhaustive no-subset result')
    overall = groups['all']
    if (overall['prior_intensity_match'] != 3790 or
            overall['prior_unpleasantness_match'] != 3792):
        raise ValueError('prior outcome-specific comparisons changed')
    if sum(rt_counts[s] for s in ('below', 'in_range', 'above', 'unavailable')) != episodes:
        raise ValueError('RT counts do not sum to episodes')
    if (sum(overall[k] for k in ('resolved', 'unresolved_unavailable_rt', 'unresolved_no_retained_trials')) != 4400 or
            missing_diagnostic['recorded_trial_pairs'] + eligible_trial_pairs != episodes):
        raise ValueError('cell or trial accounting mismatch')
    # Emit zero counts explicitly, including transition regressions and boundaries.
    for group in groups.values():
        for name in ('pair', 'intensity', 'unpleasantness'):
            for status in ('match_to_match', 'mismatch_to_match', 'match_to_mismatch', 'mismatch_to_mismatch'):
                group[name + '_' + status] += 0
        for status in ('unresolved_unavailable_rt', 'unresolved_no_retained_trials'):
            group[status] += 0
    for status in ('below', 'in_range', 'above', 'unavailable', 'exact_lower_boundary', 'exact_upper_boundary'):
        rt_counts[status] += 0
    result = {'status':'completed',
              'scope':'Retrospective candidate reconstruction of published intensity response-time filter; not the verified author pipeline, independent experiment, or a q assay.',
              'dataset_commit':COMMIT,'dataset_tree_sha256':TREE_SHA256,
              'dataset_archive_sha256':ARCHIVE_SHA256,
              'behavior_commit':'da46f2f9739ad2e9eeb9658711582be6357c1026',
              'behavior_sha256':'b40b4a1b1e001f2317fea07a49c6ee6de062f181a20affe149fe50a81b58545b',
              'event_files_verified':len(files),'accepted_runs':accepted,'rejected_runs':dict(sorted(rejected.items())),
              'episodes':episodes,'response_time_status_all_accepted_episodes':dict(sorted(rt_counts.items())),
              'event_cells':len(cells),'export_cells':len(source),'overlapping_cells':len(overlap),
              'export_only_cells':len(source.keys()-cells.keys()),'overlap_missing_export_mean':missing,
              'posthoc_missing_export_rt_diagnostic':dict(sorted(missing_diagnostic.items())),
              'groups':{k:dict(sorted(v.items())) for k,v in sorted(groups.items())},
              'prior_mismatch_subset_categories':dict(sorted(prior_subset.items())),
              'plan':'PAINGEN_RESPONSE_TIME_RECONSTRUCTION_PLAN.md',
              'privacy':'No participant identifiers, trial rows or person-level results are written.'}
    OUT.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
