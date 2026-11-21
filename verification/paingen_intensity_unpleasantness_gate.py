#!/usr/bin/env python3
"""Fixed retrospective condition-mean comparison; aggregate output only.

See PAINGEN_INTENSITY_UNPLEASANTNESS_HELDOUT_PLAN.md. No mismatch is measured;
contemporaneous intensity is not an independent physical or phenomenal assay.
"""
import argparse
import csv
import io
import json
import math
from pathlib import Path

import numpy as np

from paingen_unpleasantness_baselines import (
    CONDITIONS, COMMIT, EXPECTED, SIZE, URL, fold_for, get_data, number,
)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / 'verification/paingen_intensity_unpleasantness_gate.json'
FEATURES = ('intensity', 'nps', 'siips')
MODELS = {
    'condition': (),
    'condition_nps_siips': ('nps', 'siips'),
    'condition_intensity': ('intensity',),
    'condition_intensity_nps_siips': ('intensity', 'nps', 'siips'),
}
N_BOOT = 5000
SEED = 1907


def load_rows(raw):
    reader = csv.DictReader(io.StringIO(raw.decode('utf-8-sig'), newline=''))
    fields = {'participant_ID', 'family_ID', 'heat', 'stimLvl', 'prodicaine',
              'Yint', 'Yunp', 'nps', 'siips'}
    if not fields.issubset(reader.fieldnames or []):
        raise ValueError('source schema mismatch')
    rows, seen, family_by_person = [], set(), {}
    missing = {name: 0 for name in ('Yint', 'Yunp', 'nps', 'siips')}
    source_people, source_families = set(), set()
    total, excluded = 0, 0
    for record in reader:
        total += 1
        person, family = record['participant_ID'].strip(), record['family_ID'].strip()
        if not person or not family:
            raise ValueError('missing grouping ID')
        if person in family_by_person and family_by_person[person] != family:
            raise ValueError('participant belongs to multiple families')
        family_by_person[person] = family
        source_people.add(person); source_families.add(family)
        condition = tuple(number(record[x]) for x in ('heat', 'stimLvl', 'prodicaine'))
        if condition not in CONDITIONS:
            raise ValueError('unexpected condition')
        key = (person, condition)
        if key in seen:
            raise ValueError('duplicate participant/condition')
        seen.add(key)
        values = {field: number(record[field]) for field in missing}
        for field, value in values.items():
            missing[field] += value is None
        if any(v is None for v in values.values()):
            excluded += 1
            continue
        rows.append({'person': person, 'family': family, 'condition': condition,
                     'fold': fold_for(family), 'y': values['Yunp'],
                     'intensity': values['Yint'], 'nps': values['nps'],
                     'siips': values['siips']})
    if not rows:
        raise ValueError('no complete rows')
    sample = {'source_rows': total, 'source_people': len(source_people),
              'source_families': len(source_families), 'excluded_rows_any_required': excluded,
              'missing_or_nonfinite_by_field': missing, 'complete_rows': len(rows),
              'complete_people': len({r['person'] for r in rows}),
              'complete_families': len({r['family'] for r in rows})}
    return rows, sample


def oof_predictions(rows):
    n = len(rows)
    onehot = np.array([[float(r['condition'] == c) for c in CONDITIONS] for r in rows])
    y = np.array([r['y'] for r in rows])
    fold = np.array([r['fold'] for r in rows])
    family = np.array([r['family'] for r in rows])
    features = {f: np.array([r[f] for r in rows]) for f in FEATURES}
    result = {m: np.full(n, np.nan) for m in MODELS}
    fold_stats = []
    for k in range(5):
        test, train = fold == k, fold != k
        if not test.any() or not train.any():
            raise ValueError('empty fold')
        if set(family[test]) & set(family[train]):
            raise ValueError('family leakage')
        scaled = {}
        for f in FEATURES:
            mean, sd = features[f][train].mean(), features[f][train].std()
            if not np.isfinite(sd) or sd <= 0:
                raise ValueError('constant or invalid training feature: ' + f)
            scaled[f] = (features[f] - mean) / sd
        for name, fs in MODELS.items():
            x = np.column_stack([onehot] + [scaled[f] for f in fs])
            beta, _, rank, _ = np.linalg.lstsq(x[train], y[train], rcond=None)
            if rank != x.shape[1]:
                raise ValueError('rank-deficient training design: ' + name)
            result[name][test] = x[test] @ beta
        fold_stats.append({'fold': k, 'test_rows': int(test.sum()),
                           'test_families': len(set(family[test]))})
    if not all(np.isfinite(p).all() for p in result.values()):
        raise ValueError('nonfinite predictions')
    return result, fold_stats


def score(y, p, groups):
    y, p, groups = np.asarray(y), np.asarray(p), np.asarray(groups)
    if len(y) == 0 or len(y) != len(p) or len(y) != len(groups):
        raise ValueError('empty or inconsistent scoring inputs')
    err = y - p
    group_mse = [np.mean(err[groups == g]**2) for g in sorted(set(groups))]
    group_mae = [np.mean(np.abs(err[groups == g])) for g in sorted(set(groups))]
    return {'count': len(y), 'families': len(group_mse),
            'row_rmse': float(np.sqrt(np.mean(err**2))),
            'row_mae': float(np.mean(np.abs(err))),
            'family_rmse': float(np.sqrt(np.mean(group_mse))),
            'family_mae': float(np.mean(group_mae)),
            'prediction_min': float(np.min(p)), 'prediction_max': float(np.max(p)),
            'predictions_below_zero': int(np.sum(p < 0)),
            'predictions_above_one': int(np.sum(p > 1))}


def bootstrap_ratio(values, groups, n_boot=N_BOOT, seed=SEED):
    """Cluster bootstrap mean, retaining repeated family draws and all its rows."""
    values, groups = np.asarray(values, dtype=float), np.asarray(groups)
    if not len(values) or len(values) != len(groups) or not np.isfinite(values).all():
        raise ValueError('invalid bootstrap input')
    keys = sorted(set(groups))
    sums = np.array([values[groups == g].sum() for g in keys])
    counts = np.array([np.sum(groups == g) for g in keys])
    rng = np.random.default_rng(seed)
    draws = rng.integers(0, len(keys), (n_boot, len(keys)))
    denominators = counts[draws].sum(axis=1)
    if np.any(denominators == 0):
        raise ValueError('empty bootstrap denominator')
    samples = sums[draws].sum(axis=1) / denominators
    return [float(x) for x in np.quantile(samples, [0.025, 0.975])]


def bootstrap_rmse_delta(y, base, plus, groups, n_boot=N_BOOT, seed=SEED):
    """Family bootstrap of row-weighted RMSE differences, fixed OOF predictions."""
    y, base, plus, groups = map(np.asarray, (y, base, plus, groups))
    if not len(y) or not (len(y) == len(base) == len(plus) == len(groups)):
        raise ValueError('invalid bootstrap input')
    keys = sorted(set(groups))
    counts = np.array([np.sum(groups == g) for g in keys])
    a = np.array([np.sum((y[groups == g]-base[groups == g])**2) for g in keys])
    b = np.array([np.sum((y[groups == g]-plus[groups == g])**2) for g in keys])
    rng = np.random.default_rng(seed)
    draws = rng.integers(0, len(keys), (n_boot, len(keys)))
    denom = counts[draws].sum(axis=1)
    if np.any(denom == 0):
        raise ValueError('empty bootstrap denominator')
    delta = np.sqrt(b[draws].sum(axis=1)/denom)-np.sqrt(a[draws].sum(axis=1)/denom)
    return [float(x) for x in np.quantile(delta, [0.025, 0.975])]


def make_pairs(rows):
    cells = {}
    for i, row in enumerate(rows):
        modality, level, treat = row['condition']
        cell = cells.setdefault((row['person'], modality, level), {})
        if treat in cell:
            raise ValueError('duplicate matched cell treatment')
        cell[treat] = i
    pairs = [(v[-0.5], v[0.5], key[1]) for key, v in cells.items()
             if -0.5 in v and 0.5 in v]
    if not pairs:
        raise ValueError('no matched pairs')
    for a, b, _ in pairs:
        if rows[a]['family'] != rows[b]['family'] or rows[a]['fold'] != rows[b]['fold']:
            raise ValueError('pair family/fold mismatch')
    return pairs, len(cells)


def pair_summary(rows, predictions, pairs, modality=None):
    selected = [(a, b) for a, b, m in pairs if modality is None or m == modality]
    if not selected:
        raise ValueError('empty pair category')
    a, b = np.array(selected).T
    u = np.array([r['y'] for r in rows]); i = np.array([r['intensity'] for r in rows])
    family = np.array([r['family'] for r in rows])[a]
    du, di = u[a]-u[b], i[a]-i[b]
    corr = None if len(du) < 2 or np.std(du) == 0 or np.std(di) == 0 else float(np.corrcoef(du, di)[0, 1])
    scores = {}
    for name, pred in predictions.items():
        # Bounds [0,1] do not apply to signed contrast predictions.
        s = score(du, pred[a]-pred[b], family)
        for field in ('predictions_below_zero', 'predictions_above_one'):
            del s[field]
        scores[name] = s
    return {'pairs': len(selected), 'people': len({rows[x]['person'] for x in a}),
            'families': len(set(family)), 'mean_dU': float(du.mean()),
            'mean_dI': float(di.mean()), 'mean_dU_minus_dI': float((du-di).mean()),
            'mean_dU_minus_dI_family_bootstrap_95': bootstrap_ratio(du-di, family),
            'rms_dU': float(np.sqrt(np.mean(du**2))),
            'rms_dI': float(np.sqrt(np.mean(di**2))), 'correlation_dU_dI': corr,
            'contrast_oof_scores': scores}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', help='local exact pinned CSV, otherwise fetch bounded pinned file')
    args = parser.parse_args()
    rows, sample = load_rows(get_data(args.data))
    predictions, folds = oof_predictions(rows)
    y = np.array([r['y'] for r in rows]); groups = np.array([r['family'] for r in rows])
    scores = {name: score(y, pred, groups) for name, pred in predictions.items()}
    a, b = scores['condition_intensity'], scores['condition_intensity_nps_siips']
    diff = {key: b[key]-a[key] for key in ('row_rmse', 'row_mae', 'family_rmse', 'family_mae')}
    diff['row_rmse_family_bootstrap_95_fixed_predictions'] = bootstrap_rmse_delta(
        y, predictions['condition_intensity'], predictions['condition_intensity_nps_siips'], groups)
    pairs, cells = make_pairs(rows)
    sample['complete_row_person_modality_level_cells'] = cells
    sample['complete_matched_cells'] = len(pairs)
    sample['one_condition_only_complete_cells'] = cells-len(pairs)
    result = {
        'status': 'completed',
        'scope': 'Retrospective condition means and out-of-family report predictions within one study; not same-trial validation, q, causal mediation, or phenomenal identity.',
        'source': {'url': URL, 'commit': COMMIT, 'bytes': SIZE, 'sha256': EXPECTED},
        'sample': sample, 'folds': folds, 'row_scores': scores,
        'full_minus_intensity_model_scores': diff,
        'pairs': {name: pair_summary(rows, predictions, pairs, mod) for name, mod in
                  [('all', None), ('thermal', 0.5), ('mechanical', -0.5)]},
        'bootstrap': {'resamples': N_BOOT, 'seed': SEED, 'cluster': 'family',
                      'note': 'Percentile intervals; fixed OOF predictions for RMSE, no model refitting; not full CV uncertainty.'},
        'plan': 'PAINGEN_INTENSITY_UNPLEASANTNESS_HELDOUT_PLAN.md',
        'privacy': 'No participant IDs or individual observations are written.'}
    OUTPUT.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
