#!/usr/bin/env python3
"""Matched-stimulus report stress test; pinned source, aggregate output only.

See PAINGEN_STIMULUS_ONLY_VALENCE_STRESS_TEST_PLAN.md. Matched stimulus is not
measured internal mismatch; differences in report are not phenomenal identity.
"""
import argparse
import csv
import io
import json
import math
import random
from pathlib import Path

from paingen_unpleasantness_baselines import get_data, number, CONDITIONS, COMMIT, EXPECTED, SIZE, URL

ROOT = Path(__file__).resolve().parent.parent
BOOTSTRAPS = 5000
SEED = 202


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data', help='local exact pinned CSV; otherwise fetch bounded pinned source')
    args = ap.parse_args()
    reader = csv.DictReader(io.StringIO(get_data(args.data).decode('utf-8-sig'), newline=''))
    required = {'participant_ID', 'family_ID', 'heat', 'stimLvl', 'prodicaine', 'Yunp'}
    if not required.issubset(reader.fieldnames or []):
        raise ValueError('source schema mismatch')
    records = {}
    families_by_person = {}
    people, families = set(), set()
    total = missing = 0
    for rec in reader:
        total += 1
        person, family = rec['participant_ID'].strip(), rec['family_ID'].strip()
        if not person or not family:
            raise ValueError('missing grouping ID')
        if person in families_by_person and families_by_person[person] != family:
            raise ValueError('participant belongs to multiple families')
        families_by_person[person] = family
        people.add(person); families.add(family)
        h, level, treatment = (number(rec[x]) for x in ('heat', 'stimLvl', 'prodicaine'))
        if (h, level, treatment) not in CONDITIONS:
            raise ValueError('unexpected condition')
        key = (person, h, level)
        if treatment in records.setdefault(key, {}):
            raise ValueError('duplicate person/condition')
        y = number(rec['Yunp'])
        missing += y is None
        records[key][treatment] = y
    pairs = []
    incomplete = 0
    for (person, modality, level), values in records.items():
        if values.get(-0.5) is None or values.get(0.5) is None:
            incomplete += 1
            continue
        d = values[-0.5] - values[0.5]
        # For a shared prediction p, the squared pair error is minimized at
        # p=(control+placebo)/2 and the mean per row is d²/4.
        midpoint = (values[-0.5] + values[0.5]) / 2
        assert math.isclose(((values[-0.5] - midpoint)**2 + (values[0.5] - midpoint)**2)/2,
                            d*d/4, rel_tol=1e-12, abs_tol=1e-15)
        pairs.append((person, families_by_person[person], modality, level, d))
    if not pairs:
        raise ValueError('no matched complete cases')
    # Families, not rows, are sampled. Stable sorting ensures repeatability.
    grouped = {}
    for person, family, modality, level, d in pairs:
        grouped.setdefault(family, []).append((modality, d))
    family_keys = sorted(grouped)
    categories = [('all', None), ('thermal', 0.5), ('mechanical', -0.5)]
    results = {}
    for label, mod in categories:
        subset = [r for r in pairs if mod is None or r[2] == mod]
        if not subset: raise ValueError('empty modality')
        ds = [r[4] for r in subset]
        n = len(ds)
        sums_counts = []
        for family in family_keys:
            vals = [d for m, d in grouped[family] if mod is None or m == mod]
            sums_counts.append((sum(vals), len(vals)))
        rng = random.Random(SEED)
        boots = []
        for _ in range(BOOTSTRAPS):
            draw = [rng.randrange(len(family_keys)) for _ in family_keys]
            denom = sum(sums_counts[i][1] for i in draw)
            if not denom: raise ValueError('empty bootstrap resample')
            boots.append(sum(sums_counts[i][0] for i in draw) / denom)
        boots.sort()
        # Standard linear interpolation of empirical percentile distribution.
        def percentile(p):
            x = p * (len(boots)-1); lo = int(x); hi = min(lo+1, len(boots)-1)
            return boots[lo] + (x-lo)*(boots[hi]-boots[lo])
        pos, neg = sum(x > 0 for x in ds), sum(x < 0 for x in ds)
        eq = n-pos-neg
        results[label] = {
            'matched_cells': n,
            'unique_people': len({r[0] for r in subset}),
            'unique_families': len({r[1] for r in subset}),
            'mean_control_minus_placebo': sum(ds)/n,
            'mean_absolute_difference': sum(abs(x) for x in ds)/n,
            'root_mean_square_difference': math.sqrt(sum(x*x for x in ds)/n),
            'equal_output_oracle_row_rmse_floor': math.sqrt(sum(x*x for x in ds)/n)/2,
            'positive': pos, 'negative': neg, 'exact_ties': eq,
            'positive_fraction': pos/n, 'negative_fraction': neg/n, 'tie_fraction': eq/n,
            'family_bootstrap_mean_difference_95_percentile_interval': [percentile(0.025), percentile(0.975)],
        }
    output = {
        'status': 'completed',
        'scope': 'Published study matched condition means; observed reports, not direct q, new data, ground, or phenomenal identity.',
        'source': {'url': URL, 'commit': COMMIT, 'sha256': EXPECTED, 'bytes': SIZE},
        'sample': {'source_rows': total, 'source_people': len(people), 'source_families': len(families),
                   'source_rows_missing_unpleasantness': missing,
                   'candidate_person_modality_level_cells': len(records),
                   'complete_matched_cells': len(pairs), 'incomplete_or_missing_matched_cells': incomplete},
        'bootstrap': {'resamples': BOOTSTRAPS, 'seed': SEED, 'cluster': 'family',
                      'estimand': 'pair-weighted mean difference in selected matched cells',
                      'note': 'Exploratory percentile intervals, conditional on cluster sampling and complete-case selection.'},
        'results': results,
        'plan': 'PAINGEN_STIMULUS_ONLY_VALENCE_STRESS_TEST_PLAN.md',
        'privacy': 'No individual data, IDs or participant-level outcomes written.',
    }
    text = json.dumps(output, indent=2) + '\n'
    (ROOT / 'verification/paingen_stimulus_only_valence_test.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
