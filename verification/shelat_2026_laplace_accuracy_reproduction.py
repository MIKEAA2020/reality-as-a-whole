#!/usr/bin/env python3
"""Independent random-intercept logistic Laplace fits to the Shelat ZIPs.

Requires numpy/scipy and the exact published archive hashes. Writes no input
records or subject-level outputs. This is NOT the authors' R/lme4 code; see
SHELAT_2026_ANALYSIS_CODE_AND_MODEL_REPRODUCTION.md for comparison and scope.
"""
import argparse
import collections
import csv
import hashlib
import io
import json
import math
import zipfile
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import minimize
from scipy.special import expit, ndtr
from scipy.optimize._numdiff import approx_derivative

from shelat_2026_archive_descriptives import EXPECTED, LEARNING, SART, label, rows

CONDITIONS = ('novel', 'reward', 'selection')


def load(path, experiment):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != EXPECTED[experiment]:
        raise ValueError('archive hash mismatch')
    mapping = collections.defaultdict(set)
    result = collections.defaultdict(lambda: [0, 0])
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
                a = int(row['accuracy'])
                if a not in (0, 1):
                    raise ValueError('invalid accuracy')
                condition = label(row['triggered_colors'], rewarded, selected)
                key = (f'{experiment}:{sid}', int(row['block_num']), condition, row['infreq_trigger'])
                result[key][0] += 1
                result[key][1] += a
    return result


def design(block, condition, trigger, mode):
    s = float(trigger == 'slow')
    if mode == 'trigger':
        return [1, s]
    ds = [float(condition == c) for c in CONDITIONS]
    if mode == 'block_distractor':
        return [1, block, *ds, *(block*d for d in ds)]
    if mode != 'full':
        raise ValueError('invalid design')
    return [1, block, *ds, s, *(block*d for d in ds), block*s,
            *(s*d for d in ds), *(block*s*d for d in ds)]


def names(mode):
    if mode == 'trigger':
        return ['Intercept', 'trigger_slow']
    core = ['Intercept', 'block'] + [f'distractor_{c}' for c in CONDITIONS]
    if mode == 'block_distractor':
        return core + [f'block:distractor_{c}' for c in CONDITIONS]
    return core + ['trigger_slow'] + [f'block:distractor_{c}' for c in CONDITIONS] + ['block:trigger_slow'] + [f'distractor_{c}:trigger_slow' for c in CONDITIONS] + [f'block:distractor_{c}:trigger_slow' for c in CONDITIONS]


def fit(counts, mode):
    keys = sorted(counts)
    subjects = sorted({k[0] for k in keys})
    subject_idx = {v: i for i, v in enumerate(subjects)}
    groups = np.array([subject_idx[k[0]] for k in keys], dtype=int)
    X = np.array([design(k[1], k[2], k[3], mode) for k in keys], dtype=float)
    n = np.array([counts[k][0] for k in keys], dtype=float)
    y = np.array([counts[k][1] for k in keys], dtype=float)
    group_count = len(subjects)

    def sums(a):
        return np.bincount(groups, weights=a, minlength=group_count)

    def objective(param):
        beta, logsd = param[:-1], param[-1]
        variance = np.exp(2*logsd)
        intercept = np.zeros(group_count)
        base = X @ beta
        for _ in range(500):
            prob = expit(base + intercept[groups])
            w = n * prob * (1-prob)
            h = sums(w) + 1/variance
            step = np.clip((sums(y - n*prob) - intercept/variance)/h, -1., 1.)
            intercept += step
            if np.max(np.abs(step)) < 1e-12:
                break
        else:
            raise RuntimeError('random intercept inner Newton failed')
        eta = base + intercept[groups]
        prob = expit(eta)
        w = n * prob * (1-prob)
        h = sums(w) + 1/variance
        value = np.sum(n*np.logaddexp(0, eta) - y*eta)
        value += np.sum(intercept**2/(2*variance) + .5*np.log(variance*h))
        # Differentiate the Laplace correction through the fitted random intercepts.
        wx = np.column_stack([sums(w*X[:, j]) for j in range(X.shape[1])])
        du_beta = -wx/h[:, None]
        du_logsd = 2*intercept/(variance*h)
        deriv_w = w*(1-2*prob)
        grad_beta = X.T @ (n*prob-y)
        grad_beta += .5 * np.sum((np.column_stack([sums(deriv_w*X[:, j]) for j in range(X.shape[1])]) + sums(deriv_w)[:, None]*du_beta)/h[:, None], axis=0)
        dh_logsd = sums(deriv_w)*du_logsd - 2/variance
        grad_sd = np.sum(-intercept**2/variance + 1 + .5*dh_logsd/h)
        return float(value), np.r_[grad_beta, grad_sd]

    initial = np.zeros(X.shape[1]+1)
    opt = minimize(objective, initial, method='BFGS', jac=True,
                   options={'gtol': 1e-5, 'maxiter': 1000})
    numerical_gradient = approx_derivative(lambda p: np.array([objective(p)[0]]), opt.x, method='3-point').reshape(-1)
    gradient_check = float(np.max(np.abs(numerical_gradient - opt.jac)))
    H = approx_derivative(lambda p: objective(p)[1], opt.x, method='3-point')
    H = (H+H.T)/2
    eig = np.linalg.eigvalsh(H)
    covariance = np.linalg.inv(H)
    beta = opt.x[:-1]
    se = np.sqrt(np.diag(covariance)[:-1])
    terms = {}
    for name, b, s in zip(names(mode), beta, se):
        terms[name] = {'estimate': float(b), 'se': float(s),
                       'wald_95_ci': [float(b-1.959963984540054*s), float(b+1.959963984540054*s)],
                       'z': float(b/s), 'p': float(2*ndtr(-abs(b/s)))}
    contrasts, midpoint = {}, {}

    def contrast(vector):
        estimate = float(vector @ beta)
        stderr = float(np.sqrt(vector @ covariance[:-1, :-1] @ vector))
        return {'estimate': estimate, 'se': stderr,
                'wald_95_ci': [estimate-1.959963984540054*stderr, estimate+1.959963984540054*stderr],
                'z': estimate/stderr, 'p_unadjusted': float(2*ndtr(-abs(estimate/stderr)))}

    if mode == 'full':
        def vector(block, trigger, reference):
            return (np.array(design(block, 'reward', trigger, mode)) -
                    np.array(design(block, reference, trigger, mode)))
        for block in range(1, 5):
            for trigger in ('fast', 'slow'):
                for reference in ('neutral', 'selection'):
                    contrasts[f'block{block}:{trigger}:reward_vs_{reference}'] = contrast(vector(block, trigger, reference))
        for reference in ('neutral', 'selection'):
            fast = vector(2.5, 'fast', reference)
            slow = vector(2.5, 'slow', reference)
            midpoint[f'fast:reward_vs_{reference}'] = contrast(fast)
            midpoint[f'slow:reward_vs_{reference}'] = contrast(slow)
            midpoint[f'slow_minus_fast:reward_vs_{reference}'] = contrast(slow-fast)
    return {'mode': mode, 'participants': group_count, 'retained_trials': int(n.sum()),
            'optimizer_success': bool(opt.success), 'optimizer_message': str(opt.message),
            'max_abs_gradient': float(np.max(np.abs(opt.jac))),
            'gradient_check_max_abs_difference': gradient_check,
            'hessian_min_eigenvalue': float(eig.min()),
            'random_intercept_sd': float(np.exp(opt.x[-1])), 'terms': terms,
            'exploratory_observed_block_contrasts': contrasts,
            'exploratory_block_2_5_contrasts': midpoint}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('exp1', type=Path)
    parser.add_argument('exp2', type=Path)
    args = parser.parse_args()
    one, two = load(args.exp1, 1), load(args.exp2, 2)
    both = {**one, **two}
    output = {'scope': 'Independent Laplace approximation, not lme4 nor the authors scripts; no participant data saved.',
              'numpy_version': np.__version__, 'scipy_version': scipy.__version__,
              'results': {'exp1_trigger': fit(one, 'trigger'), 'exp2_trigger': fit(two, 'trigger'),
                          'exp1_full': fit(one, 'full'), 'exp2_full': fit(two, 'full'),
                          'pooled_block_distractor': fit(both, 'block_distractor'),
                          'pooled_full': fit(both, 'full')}}
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
