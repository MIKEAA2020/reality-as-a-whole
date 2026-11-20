#!/usr/bin/env python3
"""Run the frozen retrospective report/choice comparison in AFFECT_EXPECTATION_OUTCOME_HELDOUT_PLAN.md.

Download pinned inputs (not redistributed) with --download, or place them in the
input directory; SHA-256 is always verified. Output contains aggregates only.
"""
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.request import urlopen

import numpy as np
from scipy.optimize import minimize
from scipy.special import expit

COMMIT = '3031323d4140067b102d6db4fc5e7312038fa745'
FILES = {
    'study1_ug.csv': ('data/study1_ug/study1_ug.csv', '5aebf979021a6bf0d071e5ea86ec159b684425ba0225cdc474caa21f736af04a'),
    'study1_ec.csv': ('data/study1_ug/study1_ec.csv', 'cb31cf7c87905624f74583b804a0a154276e95fd6293ff7552c6c73dacb16a05'),
    'study2_ug_reward_emotion.csv': ('data/study2_rep/study2_ug_reward_emotion.csv', '52a66e9e091a43e82f181841f37822e293f57b2e6ebde3a7f2ecc11150079ed8'),
    'study2_ec.csv': ('data/study2_rep/study2_ec.csv', 'c02b92cfe6343626278a138af5b0cc17cd00bf646defa0f5d60cbcadd7b0823f'),
}
MODELS = {'reward': (0,), 'difference': (0, 3), 'valence': (0, 2), 'both': (0, 1, 2)}


def inputs(folder, download):
    folder.mkdir(parents=True, exist_ok=True)
    for name, (remote, expected) in FILES.items():
        p = folder / name
        if not p.exists() and download:
            url = f'https://raw.githubusercontent.com/jpheffne/epe/{COMMIT}/{remote}'
            with urlopen(url, timeout=60) as response:
                p.write_bytes(response.read())
        if not p.exists():
            raise FileNotFoundError(f'{p} missing; use --download or place pinned source file there')
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if digest != expected:
            raise ValueError(f'digest mismatch for {p}: {digest}')


def read_csv(p):
    with p.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def numeric(row, name):
    try:
        x = float(row[name])
        return x if np.isfinite(x) else None
    except (ValueError, TypeError):
        return None


def dataset(folder, study):
    ec = read_csv(folder / f'study{study}_ec.csv')
    neutral = [r for r in ec if r['emotion'] == 'neutral']
    counts = Counter(r['sub'] for r in neutral)
    if not neutral or max(counts.values()) != 1:
        raise ValueError(f'study {study}: missing or duplicate neutral records')
    a, b = ('X1', 'Y1') if study == 1 else ('valence', 'arousal')
    eligible = set()
    for row in neutral:
        x, y = numeric(row, a), numeric(row, b)
        if x is not None and y is not None and -50 <= x <= 50 and -50 <= y <= 50:
            eligible.add(row['sub'])
    source = 'study1_ug.csv' if study == 1 else 'study2_ug_reward_emotion.csv'
    raw = read_csv(folder / source)
    people, rows, outcomes = [], [], []
    audit = Counter(total_rows=len(raw), neutral_records=len(neutral), eligible_subjects=len(eligible))
    for row in raw:
        if row['sub'] not in eligible:
            audit['excluded_or_no_neutral_rows'] += 1
            continue
        fields = ['choice', 'EP_X1', 'feedback_X1'] + (['RPE'] if study == 1 else ['offer', 'RP'])
        vals = {field: numeric(row, field) for field in fields}
        if any(x is None for x in vals.values()):
            audit['missing_rows'] += 1
            continue
        y = vals['choice']
        if y not in (0, 1):
            raise ValueError('choice is not binary')
        p, v = vals['EP_X1'], vals['feedback_X1']
        rpe = vals['RPE'] if study == 1 else (100 - vals['offer']) / 100 - vals['RP']
        if study == 1:
            source_d = numeric(row, 'EPE_X1')
            if source_d is None or abs(source_d - (v - p)) > 1e-7:
                raise ValueError('source EPE is not feedback minus expectation')
        if abs(p) > 250 or abs(v) > 250:
            audit['valence_outside_plus_minus_250'] += 1
        people.append(row['sub']); outcomes.append(y); rows.append([rpe, p, v, v-p])
    return np.array(people), np.array(rows, float), np.array(outcomes, float), dict(audit)


def fit(x, y):
    mu, sd = x.mean(axis=0), x.std(axis=0)
    if np.any(sd < 1e-12):
        raise ValueError('zero variance training feature')
    z = np.column_stack([np.ones(len(x)), (x-mu)/sd])
    def loss(beta):
        score = z @ beta
        val = np.mean(np.logaddexp(0, score) - y*score) + .005 * np.dot(beta[1:], beta[1:])
        grad = z.T @ (expit(score)-y)/len(y)
        grad[1:] += .01*beta[1:]
        return val, grad
    result = minimize(loss, np.zeros(z.shape[1]), jac=True, method='BFGS', options={'gtol': 1e-8, 'maxiter': 1000})
    if not result.success and np.linalg.norm(result.jac, ord=np.inf) > 1e-7:
        raise RuntimeError(f'optimization failure: {result.message}; grad {result.jac}')
    return mu, sd, result.x


def run(study, folder):
    person, x, y, audit = dataset(folder, study)
    ids = sorted(set(person), key=lambda s: hashlib.sha256(f'{study}:{s}'.encode()).hexdigest())
    folds = {s: i % 5 for i, s in enumerate(ids)}
    fold = np.array([folds[s] for s in person])
    results = {}
    per_person = {}
    for label, columns in MODELS.items():
        z = x[:, columns]
        prediction = np.zeros(len(y))
        for k in range(5):
            train, test = fold != k, fold == k
            mu, sd, beta = fit(z[train], y[train])
            prediction[test] = expit(beta[0] + ((z[test]-mu)/sd) @ beta[1:])
        pr = np.clip(prediction, 1e-12, 1-1e-12)
        loss = -y*np.log(pr) - (1-y)*np.log1p(-pr)
        brier = (prediction-y)**2
        pp = np.array([loss[person == s].mean() for s in ids])
        per_person[label] = pp
        results[label] = {'person_weighted_log_loss': float(pp.mean()),
                          'person_weighted_brier': float(np.mean([brier[person == s].mean() for s in ids])),
                          'trial_weighted_log_loss': float(loss.mean())}
    delta = per_person['difference'] - per_person['valence']
    rng = np.random.default_rng(1729)
    boot = np.mean(delta[rng.integers(0, len(ids), size=(2000, len(ids)))], axis=1)
    return {'study': study, 'audit': audit, 'people': len(ids), 'rows': len(y),
            'choice_event_rate': float(y.mean()), 'models': results,
            'difference_minus_valence_person_log_loss': float(delta.mean()),
            'fixed_oof_prediction_person_bootstrap_95_percentile': np.quantile(boot, [.025, .975]).tolist()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=Path, default=Path('.arena/epe'))
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--output', type=Path, default=Path('verification/affect_choice_heldout.json'))
    args = parser.parse_args()
    inputs(args.input_dir, args.download)
    output = {'source_commit': COMMIT, 'input_sha256': {k: v[1] for k,v in FILES.items()},
              'method': 'subject-disjoint 5-fold logistic comparison; see frozen plan',
              'studies': [run(s, args.input_dir) for s in (1, 2)]}
    args.output.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))

if __name__ == '__main__':
    main()
