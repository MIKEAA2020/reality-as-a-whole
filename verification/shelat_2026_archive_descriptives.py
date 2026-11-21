#!/usr/bin/env python3
"""Bounded independent audit of two public ZIPs; not the authors' analysis.

Reads input ZIPs without extracting or printing survey or participant-level data.
Uses folder participant IDs solely to calculate group-level descriptives. The
published scripts and Experiment 2 registration were unavailable at writing.
Thus category coding and sequential filtering here are explicit reconstructions,
not claims that these are the authors' own preprocessing or statistical fits.
"""
import argparse
import collections
import csv
import hashlib
import io
import json
import math
import re
import statistics
import zipfile
from pathlib import Path

EXPECTED = {
    1: '3b7f349012efd0a6b6acdc89f902de429860b22b324f81a986bfce9787b875de',
    2: '1b036ddcd105799e7a288e2a7479396398dc621a94c44a8249339d3815db0ea0',
}
SART = re.compile(r'/behavior/([^/]+)/sart/data_[^/]*_block(\d+)_sart\.csv$')
LEARNING = re.compile(r'/behavior/([^/]+)/learning/trialstruc_[^/]*_block(\d+)_learn\.csv$')
COLORS = {'r': 'red', 'g': 'green', 'b': 'blue'}
CONDITIONS = ('neutral', 'novel', 'reward', 'selection')
TRIGGERS = ('fast', 'slow')


def rows(zf, name):
    with zf.open(name) as stream, io.TextIOWrapper(stream, encoding='utf-8-sig', newline='') as text:
        yield from csv.DictReader(text)


def label(color, rewarded, selected):
    if rewarded not in COLORS or selected not in COLORS or rewarded == selected:
        raise ValueError('invalid or non-distinct training color mapping')
    if color == 'neutral':
        return 'neutral'
    if color == COLORS[rewarded]:
        return 'reward'
    if color == COLORS[selected]:
        return 'selection'
    if color in set(COLORS.values()):
        return 'novel'
    raise ValueError('unexpected triggered color')


def describe(path, experiment):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != EXPECTED[experiment]:
        raise ValueError(f'experiment {experiment} archive hash mismatch: {digest}')
    with zipfile.ZipFile(path) as zf:
        maps = collections.defaultdict(set)
        subjects = set()
        main_blocks = 0
        total_rows = 0
        raw = collections.Counter()
        kept = collections.Counter()
        correct = collections.Counter()
        participant_counts = collections.Counter()
        participant_accuracy = collections.Counter()
        discarded_noresponse = 0
        discarded_short = 0
        for name in zf.namelist():
            match = LEARNING.search(name)
            if match:
                for row in rows(zf, name):
                    maps[match[1]].add((row['counterbalance_condition'], row['condition_nonrew']))
        for name in zf.namelist():
            match = SART.search(name)
            if not match:
                continue
            sid = match[1]
            subjects.add(sid)
            main_blocks += 1
            if len(maps[sid]) != 1:
                raise ValueError('missing or inconsistent subject training color mapping')
            reward, selected = next(iter(maps[sid]))
            for row in rows(zf, name):
                total_rows += 1
                trigger = row['infreq_trigger']
                if trigger not in TRIGGERS:
                    continue
                color = label(row['triggered_colors'], reward, selected)
                raw[(trigger, color)] += 1
                if not row['response'] or not row['rt']:
                    discarded_noresponse += 1
                    continue
                rt = float(row['rt'])
                if not math.isfinite(rt):
                    raise ValueError('nonfinite RT')
                if rt < 200:
                    discarded_short += 1
                    continue
                accuracy = int(row['accuracy'])
                if accuracy not in (0, 1):
                    raise ValueError('nonbinary accuracy')
                key = (trigger, color)
                kept[key] += 1
                correct[key] += accuracy
                participant_counts[(sid, *key)] += 1
                participant_accuracy[(sid, trigger)] += accuracy
        total_triggered = sum(raw.values())
        after_response = total_triggered - discarded_noresponse
        table = {}
        for trigger in TRIGGERS:
            for condition in CONDITIONS:
                key = (trigger, condition)
                values = [participant_counts[(sid, *key)] for sid in subjects]
                table[f'{trigger}_{condition}'] = {
                    'raw_n': raw[key], 'retained_n': kept[key],
                    'correct_n': correct[key],
                    'pooled_accuracy': correct[key] / kept[key] if kept[key] else None,
                    'participant_count_mean': statistics.mean(values),
                    'participant_count_sample_sd': statistics.stdev(values),
                }
        trigger_summary = {}
        for trigger in TRIGGERS:
            n = sum(kept[(trigger, c)] for c in CONDITIONS)
            acc = sum(correct[(trigger, c)] for c in CONDITIONS)
            valid = []
            for sid in subjects:
                count = sum(participant_counts[(sid, trigger, c)] for c in CONDITIONS)
                if count:
                    valid.append(participant_accuracy[(sid, trigger)] / count)
            trigger_summary[trigger] = {
                'retained_n': n, 'correct_n': acc, 'pooled_accuracy': acc/n,
                'participant_mean_accuracy': statistics.mean(valid),
                'participants_with_trigger': len(valid),
            }
        return {
            'experiment': experiment, 'archive_sha256': digest,
            'sart_subject_folders': len(subjects), 'numeric_sart_data_blocks': main_blocks,
            'sart_data_rows': total_rows, 'raw_fast_slow_trials': total_triggered,
            'excluded_no_response_or_missing_rt': discarded_noresponse,
            'excluded_no_response_or_missing_rt_pct_of_raw': 100*discarded_noresponse/total_triggered,
            'excluded_lt200_after_no_response': discarded_short,
            'excluded_lt200_pct_after_no_response': 100*discarded_short/after_response,
            'trigger_accuracy': trigger_summary,
            'trigger_condition_counts': table,
        }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('exp1', type=Path)
    p.add_argument('exp2', type=Path)
    args = p.parse_args()
    report = {'scope': 'Descriptive reconstruction only; no author scripts or mixed-model reproduction.',
              'exclusions': 'Fast/slow triggered trials, then no response/missing RT, then RT < 200 ms.',
              'color_mapping': 'Training trial structure counterbalance_condition = rewarded, condition_nonrew = selected; remaining RGB = novel.',
              'experiments': [describe(args.exp1, 1), describe(args.exp2, 2)]}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
