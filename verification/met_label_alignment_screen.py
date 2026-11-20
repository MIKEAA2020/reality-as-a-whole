#!/usr/bin/env python3
"""Pinned MET label/alignment screen; no EEG or experiential identity analysis."""
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / '.arena' / 'met'
OUT = ROOT / 'verification' / 'met_label_alignment_screen.json'
RATING_HASH = '830c854fa33aff943a6a9c36b343f7d81cf6b01da6b4ed67ff1057831c27cc59'
TREE_SHA = 'e2613bff898998734e67a9abe4b431154f1c3ec2'
CATEGORIES = {'LVLA', 'LVHA', 'HVLA', 'HVHA', 'N'}
COLS = {'participant_id','song_id','Song Catergory','Valence','Arousal',
        'Likeability','Familiarity','Remark'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_rating(value, high):
    value = value.strip()
    if value in ('', '0', 'n/a'):
        return None
    if not re.fullmatch(r'\d+', value) or not 1 <= int(value) <= high:
        raise ValueError('invalid nonmissing numeric rating')
    return int(value)


def predict_mean(train, predicate):
    selected = [row['val'] for row in train if predicate(row)]
    fallback = not selected
    if fallback:
        selected = [row['val'] for row in train]
    if not selected:
        raise ValueError('empty training set')
    return sum(selected) / len(selected), fallback


def training_sets(rows, test):
    known = [r for r in rows if r['person'] != test['person']]
    new = [r for r in known if r['song'] != test['song']]
    return known, new


def scores(pairs):
    errors = [p-y for p,y in pairs]
    return {'n': len(errors), 'mae': sum(abs(e) for e in errors)/len(errors),
            'rmse': math.sqrt(sum(e*e for e in errors)/len(errors))}


def main():
    ratings = DATA / 'ratings.tsv'
    if sha(ratings) != RATING_HASH:
        raise ValueError('unexpected ratings file hash')
    tree = json.loads((DATA / 'tree.json').read_text())
    if tree.get('sha') != TREE_SHA or tree.get('truncated'):
        raise ValueError('tree SHA mismatch or incomplete tree')
    eeg = {}
    pattern = re.compile(r'^sub-(\d{2})/ses-(t\d{2})/eeg/sub-\1_ses-\2_task-music_eeg\.(set|eeg)$')
    for obj in tree['tree']:
        m = pattern.fullmatch(obj['path'])
        if m:
            key = ('sub-'+m[1], m[2])
            eeg.setdefault(key, []).append(obj['mode'])
    with ratings.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        if set(reader.fieldnames or []) != COLS:
            raise ValueError('unexpected columns')
        raw = list(reader)
    seen, rows = set(), []
    missing = Counter()
    remarks = Counter()
    all_categories = defaultdict(set)
    matched, modes = 0, Counter()
    for r in raw:
        person, song = r['participant_id'].strip(), r['song_id'].strip()
        if not re.fullmatch(r'sub-\d{2}', person) or not re.fullmatch(r't\d{2}', song):
            raise ValueError('malformed key')
        key = (person, song)
        if key in seen:
            raise ValueError('duplicate participant-song key')
        seen.add(key)
        category = r['Song Catergory'].strip()
        if category not in CATEGORIES:
            raise ValueError('unexpected category')
        all_categories[song].add(category)
        parsed = {}
        for name, high in [('Valence',9), ('Arousal',9), ('Likeability',5), ('Familiarity',5)]:
            parsed[name] = parse_rating(r[name], high)
            if parsed[name] is None:
                missing[name] += 1
        remark = r['Remark'].strip()
        remarks[remark or '(blank)'] += 1
        if key in eeg:
            matched += 1
            modes.update(eeg[key])
        if parsed['Valence'] is not None:
            rows.append({'person':person, 'song':song, 'category':category,
                         'val':parsed['Valence']})
    if any(len(v) != 1 for v in all_categories.values()):
        raise ValueError('song category inconsistent across participants')
    if not rows:
        raise ValueError('no valid targets')
    results = {'known_songs':defaultdict(list), 'new_songs':defaultdict(list)}
    fallbacks = Counter()
    for test in rows:
        known, new = training_sets(rows, test)
        assert all(r['person'] != test['person'] for r in known)
        assert all(r['person'] != test['person'] and r['song'] != test['song'] for r in new)
        for setting, train, variants in [
            ('known_songs', known, ('grand','song','category')),
            ('new_songs', new, ('grand','category')),
        ]:
            for variant in variants:
                pred, fallback = predict_mean(train, {
                    'grand': lambda r: True,
                    'song': lambda r: r['song'] == test['song'],
                    'category': lambda r: r['category'] == test['category'],
                }[variant])
                fallbacks[f'{setting}_{variant}'] += int(fallback)
                results[setting][variant].append((pred,test['val']))
    summary = {
        'scope':'retrospective label-only, not neural analysis or independent preregistration',
        'source_commit':TREE_SHA, 'ratings_sha256':sha(ratings),
        'rows':len(raw), 'valid_valence_rows':len(rows),
        'participants':len({r['person'] for r in rows}),
        'songs':len({r['song'] for r in rows}),
        'rating_missing_counts':dict(missing), 'remark_counts':dict(remarks),
        'matched_eeg_path_keys':matched, 'matched_eeg_path_modes':dict(modes),
        'categories_per_song_consistent':True,
        'participant_trial_count_distribution':dict(sorted(Counter(Counter(r['person'] for r in rows).values()).items())),
        'song_rating_count_distribution':dict(sorted(Counter(Counter(r['song'] for r in rows).values()).items())),
        'category_fallbacks':dict(fallbacks),
        'errors':{s:{v:scores(p) for v,p in variants.items()} for s,variants in results.items()},
        'caveat':'path presence does not establish accessible or usable EEG; all valid labels, not EEG-eligible subset',
    }
    OUT.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
