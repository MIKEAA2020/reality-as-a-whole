#!/usr/bin/env python3
"""Retrospective first-versus-tenth recorded RGB exposure, aggregate output only."""
import argparse
import collections
import hashlib
import json
import math
import statistics
import zipfile
from pathlib import Path

from scipy.stats import t
from shelat_2026_archive_descriptives import EXPECTED, LEARNING, SART, rows
from shelat_2026_warning_cue_audit import STRUCTURE, classify


def collect(path, experiment):
    if hashlib.sha256(path.read_bytes()).hexdigest() != EXPECTED[experiment]:
        raise ValueError('archive hash mismatch')
    with zipfile.ZipFile(path) as z:
        maps = collections.defaultdict(set)
        structures = {}
        for name in z.namelist():
            m = LEARNING.search(name)
            if m:
                for row in rows(z, name):
                    maps[m[1]].add((row['counterbalance_condition'], row['condition_nonrew']))
            m = STRUCTURE.search(name)
            if m:
                for row in rows(z, name):
                    key = (m[1], int(row['block_num']), int(row['trial_num']))
                    if key in structures:
                        raise ValueError('duplicate structure')
                    structures[key] = row['counterbalance_condition']
        records = collections.defaultdict(list)
        seen = set()
        subjects = set()
        for name in z.namelist():
            m = SART.search(name)
            if not m:
                continue
            sid = m[1]
            subjects.add(sid)
            if len(maps[sid]) != 1:
                raise ValueError('inconsistent training mapping')
            reward, selected = next(iter(maps[sid]))
            for row in rows(z, name):
                block, trial = int(row['block_num']), int(row['trial_num'])
                key = (sid, block, trial)
                if key in seen or key not in structures:
                    raise ValueError('duplicate data or missing structure')
                seen.add(key)
                # Validate every actual display, not just administratively labeled triggers.
                trigger, category = classify(row, reward, selected, structures[key])
                if category == 'neutral':
                    continue
                if trigger not in ('fast', 'slow', 'fixed'):
                    raise ValueError('RGB on nontrigger display')
                acc = row['accuracy']
                accuracy = int(acc) if acc in ('0', '1') else None
                if acc not in ('0', '1', ''):
                    raise ValueError('unexpected accuracy code')
                if bool(acc) != bool(row['response']) or bool(acc) != bool(row['rt']):
                    raise ValueError('response, RT and accuracy presence differ')
                rt = float(row['rt']) if row['rt'] else None
                if rt is not None and not math.isfinite(rt):
                    raise ValueError('nonfinite RT')
                records[(experiment, sid)].append({'block': block, 'trial': trial,
                    'trigger': trigger, 'category': category, 'accuracy': accuracy, 'rt': rt})
        for sid in subjects:
            records[(experiment, sid)].sort(key=lambda item: (item['block'], item['trial']))
        return dict(records)


def exact_mcnemar(b, c):
    """Double the smaller binomial tail, capped at 1; null discordance symmetry."""
    n = b + c
    return 1.0 if not n else min(1.0, 2 * sum(math.comb(n, k) for k in range(min(b, c)+1)) / 2**n)


def summarize(records):
    summaries = {}
    for number in (1, 10):
        selected = [v[number-1] for v in records.values() if len(v) >= number]
        acc = collections.Counter('missing' if r['accuracy'] is None else ('correct' if r['accuracy'] == 1 else 'incorrect') for r in selected)
        observed = acc['correct'] + acc['incorrect']
        summaries[str(number)] = {'available_occurrences': len(selected),
            'outcomes': {k: acc[k] for k in ('correct', 'incorrect', 'missing')},
            'correct_fraction_among_usable': acc['correct']/observed if observed else None,
            'rt_below_200_ms': sum(r['rt'] is not None and r['rt'] < 200 for r in selected),
            'trigger': dict(sorted(collections.Counter(r['trigger'] for r in selected).items())),
            'color_category': dict(sorted(collections.Counter(r['category'] for r in selected).items())),
            'block': dict(sorted(collections.Counter(str(r['block']) for r in selected).items()))}
    pair = collections.Counter()
    for v in records.values():
        if len(v) < 10 or v[0]['accuracy'] is None or v[9]['accuracy'] is None:
            continue
        pair[(v[0]['accuracy'], v[9]['accuracy'])] += 1
    n = sum(pair.values())
    diff = (pair[(0, 1)] - pair[(1, 0)])/n if n else None
    changes = [float(b-a) for (a, b), count in pair.items() for _ in range(count)]
    if n >= 2:
        se = statistics.stdev(changes)/math.sqrt(n)
        half = float(t.ppf(.975, n-1))*se
        interval = [diff-half, diff+half]
    else:
        interval = None
    return {'participants': len(records), 'occurrences': summaries,
            'paired_usable_n': n,
            'paired_table_first_then_tenth': {'incorrect_incorrect': pair[(0, 0)], 'incorrect_correct': pair[(0, 1)],
                                               'correct_incorrect': pair[(1, 0)], 'correct_correct': pair[(1, 1)]},
            'accuracy_change_tenth_minus_first': diff, 'paired_t_95_ci': interval,
            'exact_two_sided_mcnemar_p_unadjusted': exact_mcnemar(pair[(0, 1)], pair[(1, 0)]) if n else None}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('exp1', type=Path)
    p.add_argument('exp2', type=Path)
    args = p.parse_args()
    one, two = collect(args.exp1, 1), collect(args.exp2, 2)
    groups = {'exp1': one, 'exp2': two, 'pooled': {**one, **two}}
    within_trigger = {}
    for trigger in ('fast', 'slow', 'fixed'):
        within_trigger[trigger] = {
            name: summarize({subject: [row for row in events if row['trigger'] == trigger]
                             for subject, events in group.items()})
            for name, group in groups.items()
        }
    result = {'scope': 'Retrospective all recorded RGB displays, including fixed triggers and no RT exclusions; aggregate only.',
              'results': {name: summarize(group) for name, group in groups.items()},
              'post_result_within_trigger': within_trigger}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
