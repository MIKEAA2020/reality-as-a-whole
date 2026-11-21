#!/usr/bin/env python3
"""Independent Gaussian random-intercept REML model on retained SART RTs.

Input ZIPs must match the published SHA-256 hashes. All subject-level cell
summaries exist only in memory; printed JSON contains only pooled model results.
This does not execute the authors' R/lme4 workflow or estimate lmerTest degrees
of freedom. Inference uses normal Wald intervals and unadjusted normal p values.
"""
import argparse
import collections
import hashlib
import json
import math
import zipfile
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import minimize_scalar
from scipy.special import ndtr

from shelat_2026_archive_descriptives import EXPECTED, LEARNING, SART, label, rows

CONDITIONS = ('novel', 'reward', 'selection')


def load(path, experiment):
    if hashlib.sha256(path.read_bytes()).hexdigest() != EXPECTED[experiment]:
        raise ValueError('archive hash mismatch')
    mapping = collections.defaultdict(set)
    # count, sum(rt), sum(rt²), count correct; only used transiently in memory.
    cells = collections.defaultdict(lambda: [0, 0., 0., 0])
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            m = LEARNING.search(name)
            if m:
                for row in rows(z, name):
                    mapping[m[1]].add((row['counterbalance_condition'], row['condition_nonrew']))
        for name in z.namelist():
            m = SART.search(name)
            if not m:
                continue
            sid = m[1]
            if len(mapping[sid]) != 1:
                raise ValueError('inconsistent subject colors')
            rewarded, selected = next(iter(mapping[sid]))
            for row in rows(z, name):
                if row['infreq_trigger'] not in ('fast', 'slow') or not row['rt'] or not row['response']:
                    continue
                rt = float(row['rt'])
                if not math.isfinite(rt):
                    raise ValueError('nonfinite RT')
                if rt < 200:
                    continue
                accuracy = int(row['accuracy'])
                if accuracy not in (0, 1):
                    raise ValueError('invalid accuracy')
                condition = label(row['triggered_colors'], rewarded, selected)
                cell = cells[(f'{experiment}:{sid}', condition, row['infreq_trigger'])]
                cell[0] += 1
                cell[1] += rt
                cell[2] += rt*rt
                cell[3] += accuracy
    return cells


def design(condition, trigger):
    ds = [float(condition == c) for c in CONDITIONS]
    slow = float(trigger == 'slow')
    return np.array([1, *ds, slow, *(d*slow for d in ds)])


def fit(cells):
    keys = sorted(cells)
    subjects = sorted({k[0] for k in keys})
    group = np.array([subjects.index(k[0]) for k in keys], dtype=int)
    X = np.array([design(k[1], k[2]) for k in keys])
    count = np.array([cells[k][0] for k in keys], dtype=float)
    ysum = np.array([cells[k][1] for k in keys], dtype=float)
    y2sum = np.array([cells[k][2] for k in keys], dtype=float)
    n, p = int(count.sum()), X.shape[1]
    grouped_n = np.bincount(group, weights=count, minlength=len(subjects))
    grouped_y = np.bincount(group, weights=ysum, minlength=len(subjects))
    grouped_x = np.column_stack([np.bincount(group, weights=count*X[:, j], minlength=len(subjects)) for j in range(p)])
    naive_xx = X.T @ (count[:, None]*X)
    naive_xy = X.T @ ysum
    naive_yy = y2sum.sum()

    def profile(logratio, details=False):
        # V = residual_variance * (I + ratio Z Z'); profile out residual variance.
        ratio = np.exp(logratio)
        weight = ratio/(1 + ratio*grouped_n)
        xx = naive_xx - grouped_x.T @ (weight[:, None]*grouped_x)
        xy = naive_xy - grouped_x.T @ (weight*grouped_y)
        yy = naive_yy - np.sum(weight*grouped_y**2)
        beta = np.linalg.solve(xx, xy)
        residual = yy - beta @ xy
        sign, logdet_xx = np.linalg.slogdet(xx)
        if sign <= 0 or residual <= 0 or n <= p:
            raise ValueError('invalid REML system')
        sigma2 = residual/(n-p)
        value = (n-p)*np.log(sigma2) + np.log1p(ratio*grouped_n).sum() + logdet_xx
        if details:
            return value, beta, sigma2*np.linalg.inv(xx), sigma2, ratio
        return value

    opt = minimize_scalar(profile, bounds=(-12., 8.), method='bounded', options={'xatol': 1e-10})
    value, beta, cov, variance, ratio = profile(opt.x, True)
    eps = 1e-4
    derivative = float((profile(opt.x+eps)-profile(opt.x-eps))/(2*eps))
    curvature = float((profile(opt.x+eps)-2*value+profile(opt.x-eps))/eps**2)
    terms = {}
    termnames = ['Intercept', 'distractor_novel', 'distractor_reward', 'distractor_selection', 'trigger_slow'] + [f'distractor_{c}:trigger_slow' for c in CONDITIONS]

    def contrast(v):
        b = float(v @ beta)
        se = float(np.sqrt(v @ cov @ v))
        return {'estimate_ms': b, 'se_ms': se,
                'wald_95_ci_ms': [b - 1.959963984540054*se, b + 1.959963984540054*se],
                'z': b/se, 'p_unadjusted_normal': float(2*ndtr(-abs(b/se)))}

    for i, name in enumerate(termnames):
        terms[name] = contrast(np.eye(p)[i])
    contrasts = {}
    for ref in ('neutral', 'selection'):
        fast = design('reward', 'fast')-design(ref, 'fast')
        slow = design('reward', 'slow')-design(ref, 'slow')
        contrasts[f'fast:reward_vs_{ref}'] = contrast(fast)
        contrasts[f'slow:reward_vs_{ref}'] = contrast(slow)
        contrasts[f'slow_minus_fast:reward_vs_{ref}'] = contrast(slow-fast)
    return {'participants': len(subjects), 'retained_trials': n,
            'correct_trials': int(sum(cell[3] for cell in cells.values())),
            'optimizer_success': bool(opt.success), 'optimizer_message': str(opt.message),
            'log_variance_ratio': float(opt.x), 'profile_derivative': derivative,
            'profile_curvature': curvature, 'residual_sd_ms': float(np.sqrt(variance)),
            'random_intercept_sd_ms': float(np.sqrt(variance*ratio)),
            'terms': terms, 'exploratory_contrasts': contrasts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('exp1', type=Path)
    parser.add_argument('exp2', type=Path)
    args = parser.parse_args()
    one, two = load(args.exp1, 1), load(args.exp2, 2)
    report = {'scope': 'Gaussian REML random intercept, all retained correct and incorrect fast/slow trials; independent implementation, no lmerTest df, no participant output.',
              'numpy_version': np.__version__, 'scipy_version': scipy.__version__,
              'results': {'exp1': fit(one), 'exp2': fit(two), 'pooled': fit({**one, **two})}}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
