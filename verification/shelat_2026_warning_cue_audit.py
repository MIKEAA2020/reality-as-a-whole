#!/usr/bin/env python3
"""Aggregate physical-color/target contingency in public Shelat archives.

Observational, retrospective, all SART data rows, no response/RT exclusions.
Trial structures are joined in memory; participant-level data are never output.
"""
import argparse
import ast
import collections
import hashlib
import json
import re
import zipfile
from pathlib import Path

from shelat_2026_archive_descriptives import EXPECTED, LEARNING, SART, label, rows

STRUCTURE = re.compile(r'/behavior/([^/]+)/sart/trialstruc_.*_block(\d+)_sart\.csv$')
RGB = {'red', 'green', 'blue'}
TRIGGERS = {'fast', 'slow', 'fixed'}
CATEGORIES = ('neutral', 'novel', 'reward', 'selection')


def classify(row, reward, selected, counterbalance):
    """Validate the actual arrays and tag; return physical category, trigger, angle."""
    trigger = row['infreq_trigger'] or 'nontrigger'
    if trigger not in TRIGGERS | {'nontrigger'}:
        raise ValueError('unexpected trigger')
    colors = ast.literal_eval(row['actual_shape_colors'])
    bars = ast.literal_eval(row['actual_bar_orientations'])
    if not isinstance(colors, list) or len(colors) != 6 or not all(isinstance(x, str) for x in colors):
        raise ValueError('malformed color array')
    if not isinstance(bars, list) or len(bars) != 6:
        raise ValueError('malformed orientation array')
    found = [color.lower() for color in colors if color.lower() in RGB]
    if len(found) > 1:
        raise ValueError('multiple RGB items')
    category = label(found[0] if found else 'neutral', reward, selected)
    tag = row['triggered_colors']
    if trigger == 'nontrigger':
        if tag or found:
            raise ValueError('unexpected tag or RGB on nontrigger trial')
    elif label(tag.lower(), reward, selected) != category:
        raise ValueError('triggered color and actual array disagree')
    target_angles = [x for x in bars if x in (0, 90)]
    if len(target_angles) != 1 or counterbalance not in ('h', 'v'):
        raise ValueError('invalid target orientation or counterbalance')
    angle = target_angles[0]
    expected = (90 if counterbalance == 'v' else 0) if trigger != 'nontrigger' else (0 if counterbalance == 'v' else 90)
    if angle != expected:
        raise ValueError('trigger and counterbalanced orientation disagree')
    return trigger, category


def audit(path, experiment):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != EXPECTED[experiment]:
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
                        raise ValueError('duplicate structure key')
                    structures[key] = row['counterbalance_condition']
        counts = collections.Counter()
        seen = set()
        subjects = set()
        for name in z.namelist():
            m = SART.search(name)
            if not m:
                continue
            sid = m[1]
            subjects.add(sid)
            if len(maps[sid]) != 1:
                raise ValueError('inconsistent learning mapping')
            reward, selected = next(iter(maps[sid]))
            for row in rows(z, name):
                key = (sid, int(row['block_num']), int(row['trial_num']))
                if key in seen or key not in structures:
                    raise ValueError('duplicate or missing joined structure')
                seen.add(key)
                trigger, category = classify(row, reward, selected, structures[key])
                counts[(trigger, category)] += 1
        table = {t: {c: counts[(t, c)] for c in CATEGORIES} for t in ('nontrigger', 'fixed', 'fast', 'slow')}
        rare = sum(sum(table[t].values()) for t in ('fixed', 'fast', 'slow'))
        rgb_rare = sum(sum(table[t][c] for c in ('novel', 'reward', 'selection')) for t in ('fixed', 'fast', 'slow'))
        rgb_nontrigger = sum(table['nontrigger'][c] for c in ('novel', 'reward', 'selection'))
        neutral_rare = rare - rgb_rare
        nontrigger = sum(table['nontrigger'].values())
        return {'experiment': experiment, 'archive_sha256': digest, 'subjects': len(subjects),
                'data_rows': len(seen), 'matched_structure_rows': len(seen), 'structure_rows': len(structures),
                'counts_by_trigger_and_actual_color_category': table,
                'rare_given_rgb': {'numerator': rgb_rare, 'denominator': rgb_rare + rgb_nontrigger},
                'rare_given_no_rgb': {'numerator': neutral_rare, 'denominator': neutral_rare + nontrigger - rgb_nontrigger},
                'rgb_given_rare': {'numerator': rgb_rare, 'denominator': rare}}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('exp1', type=Path)
    p.add_argument('exp2', type=Path)
    args = p.parse_args()
    print(json.dumps({'scope': 'All SART rows including fixed triggers and rows excluded from response models; physical array RGB presence, not awareness or perceived salience.',
                      'experiments': [audit(args.exp1, 1), audit(args.exp2, 2)]}, indent=2))


if __name__ == '__main__':
    main()
