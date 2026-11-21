#!/usr/bin/env python3
"""Conservatively recover intact cue-bounded episodes in rejected event files.

This is a retrospective candidate reconstruction, not the source processing code.
"""
import argparse
import collections
import csv
import io
import json
from pathlib import Path

from paingen_condition_subset_diagnostic import obtain_events
from paingen_remaining_mismatch_runs import run_category
from paingen_response_time_reconstruction import compare_cell, rt_status, transition
from paingen_source_crosscheck import bkey, obtain
from paingen_trial_provenance_audit import (ARCHIVE_SHA256, COMMIT, PATH, TREE_SHA256,
                                             compare_rating, finite, parse_run, rating, source_rating)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'verification/paingen_partial_run_salvage.json'
REQUIRED = {'onset', 'duration', 'trial_type', 'int_rating', 'unp_rating', 'level', 'response_time'}


def level_code(stim):
    level = finite(stim['level'])
    mapping = {46.5: 3, 47.: 4, 47.5: 5} if stim['trial_type'] == 'heat' else {3.: 3, 4.: 4, 5.: 5}
    return mapping.get(level)


def recover(data):
    reader = csv.DictReader(io.StringIO(data.decode('utf-8-sig'), newline=''), delimiter='\t')
    if not REQUIRED.issubset(reader.fieldnames or []):
        return [], collections.Counter({'file_schema': 1})
    rows = list(reader)
    if not rows:
        return [], collections.Counter({'file_empty': 1})
    times = [finite(r['onset']) for r in rows]
    if any(t is None for t in times):
        return [], collections.Counter({'file_invalid_onset': 1})
    if len(set(times)) != len(times):
        return [], collections.Counter({'file_tied_onsets': 1})
    rows = [r for _, r in sorted(zip(times, rows), key=lambda x: x[0])]
    counts = collections.Counter()
    groups = []
    for row in rows:
        if row['trial_type'] == 'warning_cue':
            groups.append([row])
        elif groups:
            groups[-1].append(row)
        else:
            counts['orphan_rows'] += 1
    result = []
    for group in groups:
        if (len(group) != 4 or group[1]['trial_type'] not in ('heat', 'press') or
                {group[2]['trial_type'], group[3]['trial_type']} != {'int_rating', 'unp_rating'}):
            counts['group_grammar'] += 1
            continue
        cue, stim, first, second = group
        events = {first['trial_type']: first, second['trial_type']: second}
        if any(compare_rating(stim[f], events[f][f]) != 'both_equal' for f in ('int_rating', 'unp_rating')):
            counts['group_ratings'] += 1
        elif level_code(stim) is None:
            counts['group_level'] += 1
        elif rt_status(events['int_rating']['response_time']) == 'unavailable':
            counts['group_rt'] += 1
        else:
            result.append((cue, stim, first, second))
            counts['valid_episodes'] += 1
    return result, counts


def record(cells, person, run, episode):
    _, stim, first, second = episode
    events = {first['trial_type']: first, second['trial_type']: second}
    if level_code(stim) is None:
        raise ValueError('unsupported stimulus level')
    key = (person, int(stim['trial_type'] == 'heat'), level_code(stim), int(run in ('02', '03')))
    cells[key].append((rating(stim['int_rating'])[1], rating(stim['unp_rating'])[1],
                       run, finite(events['int_rating']['response_time'])))


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
    base, extra = collections.defaultdict(list), collections.defaultdict(list)
    statuses = {}
    accepted = episodes = 0
    rejected, recovery_counts, additional_rt, files_with_valid = collections.Counter(), collections.Counter(), collections.Counter(), 0
    for path, data in sorted(files.items()):
        m = PATH.fullmatch(path)
        if not m:
            raise ValueError('unexpected event path')
        person, run = m['person'], m['run']
        if (person, run) in statuses:
            raise ValueError('duplicate person/run')
        prior, reason = parse_run(data)
        statuses[(person, run)] = 'rejected' if reason else 'accepted'
        recovered, counts = recover(data)
        if reason is None:
            if counts != {'valid_episodes': 8} or recovered != prior:
                raise ValueError('recovery parser does not reproduce an accepted run')
            accepted += 1
            episodes += len(prior)
            for episode in prior:
                record(base, person, run, episode)
        else:
            rejected[reason] += 1
            recovery_counts.update(counts)
            files_with_valid += bool(recovered)
            for episode in recovered:
                record(extra, person, run, episode)
                _, _, first, second = episode
                events = {first['trial_type']: first, second['trial_type']: second}
                additional_rt[rt_status(events['int_rating']['response_time'])] += 1
    if accepted != 1566 or episodes != 12528 or len(base) != 4707:
        raise ValueError('prior event counts changed')
    overlap = base.keys() & source.keys()
    if len(overlap) != 4707 or len(source) != 4709:
        raise ValueError('prior source join changed')
    pairs, dim, unresolved, original_mismatch_strata = collections.Counter(), collections.Counter(), collections.Counter(), collections.defaultdict(collections.Counter)
    prior_mismatch = prior_match = missing = changed = 0
    for key in overlap:
        target = (source_rating(source[key]['Yint']), source_rating(source[key]['Yunp']))
        if any(v is None for v in target):
            missing += 1
            continue
        old = compare_cell(base[key], target)
        if old['new'] is None:
            raise ValueError('original screened cell unresolved')
        prior_flag = all(old['new'])
        prior_match += prior_flag
        prior_mismatch += not prior_flag
        augmented = base[key] + extra.get(key, [])
        new = compare_cell(augmented, target)
        if new['new'] is None:
            unresolved[new['reason']] += 1
            continue
        changed += new['retained'] != old['retained']
        pairs[transition(prior_flag, all(new['new']))] += 1
        for idx, label in enumerate(('intensity', 'unpleasantness')):
            dim[label + '_' + transition(old['new'][idx], new['new'][idx])] += 1
        if not prior_flag:
            runs = ('02', '03') if key[3] else ('01', '04')
            category = run_category([statuses.get((key[0], r), 'absent') for r in runs])
            if category == 'two_accepted' and len(augmented) != len(base[key]):
                raise ValueError('candidate episode attached to two-accepted cell')
            original_mismatch_strata[category][('now_match' if all(new['new']) else 'still_mismatch')] += 1
    if missing != 307 or prior_match != 4365 or prior_mismatch != 35:
        raise ValueError('prior baseline not reproduced')
    source_only = source.keys() - base.keys()
    source_only_covered = [key for key in source_only if any(rt_status(t[3]) == 'in_range' for t in extra.get(key, []))]
    covered_finite = 0
    export_only_agreement = collections.Counter()
    for key in source_only_covered:
        target = tuple(source_rating(source[key][f]) for f in ('Yint', 'Yunp'))
        if any(v is None for v in target):
            export_only_agreement['missing_export'] += 1
            continue
        covered_finite += 1
        answer = compare_cell(extra[key], target)
        if answer['new'] is None:
            export_only_agreement['unresolved'] += 1
            continue
        export_only_agreement['pair_match' if all(answer['new']) else 'pair_mismatch'] += 1
        for i, label in enumerate(('intensity', 'unpleasantness')):
            export_only_agreement[label + ('_match' if answer['new'][i] else '_mismatch')] += 1
    for label in ('pair', 'intensity', 'unpleasantness'):
        for status in ('match', 'mismatch'):
            export_only_agreement[label + '_' + status] += 0
    for status in ('match_to_match', 'match_to_mismatch', 'mismatch_to_match', 'mismatch_to_mismatch'):
        pairs[status] += 0
        for label in ('intensity', 'unpleasantness'):
            dim[label + '_' + status] += 0
    for status in ('in_range', 'below', 'above', 'unavailable'):
        additional_rt[status] += 0
    receipt = {'status': 'completed', 'scope': 'Post-result candidate episode recovery from rejected runs; not verified original processing.',
               'dataset_commit': COMMIT, 'tree_sha256': TREE_SHA256, 'archive_sha256': ARCHIVE_SHA256,
               'behavior_commit': 'da46f2f9739ad2e9eeb9658711582be6357c1026',
               'behavior_sha256': 'b40b4a1b1e001f2317fea07a49c6ee6de062f181a20affe149fe50a81b58545b',
               'files_verified': len(files), 'accepted_files_replayed': accepted, 'accepted_episodes_replayed': episodes,
               'prior_rejected_runs': dict(sorted(rejected.items())), 'rejected_files_with_recovered_episodes': files_with_valid,
               'rejected_files_recovery_counts': dict(sorted(recovery_counts.items())),
               'recovered_episode_rt_counts': dict(sorted(additional_rt.items())),
               'original_eligible_cells': prior_match + prior_mismatch, 'original_export_missing': missing,
               'eligible_cells_with_added_in_range_episode': changed,
               'paired_transitions': dict(sorted(pairs.items())), 'dimension_transitions': dict(sorted(dim.items())),
               'unresolved_augmented': dict(sorted(unresolved.items())),
               'original_mismatch_by_run_category': {k: dict(sorted(v.items())) for k, v in sorted(original_mismatch_strata.items())},
               'export_only_keys': len(source_only), 'export_only_keys_now_covered_by_in_range_episode': len(source_only_covered),
               'export_only_keys_covered_with_both_finite_means': covered_finite,
               'posthoc_export_only_mean_agreement': dict(sorted(export_only_agreement.items())),
               'plan': 'PAINGEN_PARTIAL_RUN_EPISODE_SALVAGE_PLAN.md',
               'privacy': 'No participant identifiers, episode rows or individual outcomes written.'}
    OUT.write_text(json.dumps(receipt, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(json.dumps(receipt, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
