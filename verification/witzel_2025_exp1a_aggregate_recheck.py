#!/usr/bin/env python3
"""Recheck published Exp 1a opposite-hue t tests from author-aggregated MAT.

This is retrospective and not an independent replication or raw-trial analysis.
External input (not checked in): GitHub blob 1a10e123ee6a6aad33f18029918d9038b67d6904.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import scipy
from scipy.io import loadmat
from scipy.stats import ttest_1samp

SHA256 = '9d380d2f0e7795f9755fa54e8660d084dde3672dfe583979aab284920202cd45'
GIT_BLOB = '1a10e123ee6a6aad33f18029918d9038b67d6904'
LABELS = ('red', 'orange', 'yellow', 'green', 'turquoise', 'blue', 'purple', 'magenta')
ARTICLE_T = (5.35, 10.00, 1.98, -7.15, 0.63, -8.52, 4.69, 4.00)
ALPHA = 0.05 / 8


def signed_angular_difference(values, center):
    """Match the author's tie convention: +180 for antipodal values."""
    d = np.mod(np.asarray(values, dtype=float) - center, 360.0)
    return np.where(d <= 180, d, d - 360)


def condition_stats(labels, comp, individual):
    comp = np.asarray(comp, dtype=float)
    individual = np.asarray(individual, dtype=float)
    if tuple(str(x) for x in labels) != LABELS:
        raise ValueError('unexpected condition labels/order')
    if comp.shape != (8, 9, 3) or individual.shape != (31, 8):
        raise ValueError('unexpected data shape')
    rows = []
    for i, label in enumerate(LABELS):
        center = comp[i, 4, 1] % 360
        offsets = signed_angular_difference(comp[i, :, 1], center)
        if not np.allclose(offsets, np.arange(-40, 41, 10), atol=1e-7, rtol=0):
            raise ValueError('comparison grid differs from expected +/- 40 degree range')
        d = signed_angular_difference(individual[:, i], center)
        d = d[np.isfinite(d)]
        if len(d) < 2 or np.any(np.abs(d) > 40 + 1e-7):
            raise ValueError('insufficient or unexpected median responses')
        test = ttest_1samp(d, 0)
        ci = test.confidence_interval(confidence_level=0.95)
        sd = np.std(d, ddof=1)
        rows.append({'inducer_label': label, 'n': int(len(d)),
                     'opposite_hue_degrees': float(center),
                     'mean_signed_deviation_degrees': float(np.mean(d)),
                     't': float(test.statistic), 'df': int(len(d)-1),
                     'p_two_sided': float(test.pvalue),
                     'ci_95_unadjusted_degrees': [float(ci.low), float(ci.high)],
                     'cohen_d': float(np.mean(d)/sd),
                     'significant_bonferroni_0_05_over_8': bool(test.pvalue < ALPHA),
                     'participant_medians_at_grid_edge': int(np.sum(np.isclose(np.abs(d), 40, rtol=0, atol=1e-7))),
                     'published_t_rounded_2dp': ARTICLE_T[i],
                     'abs_difference_from_published_t': float(abs(test.statistic - ARTICLE_T[i]))})
    return rows


def analyze(path):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if digest != SHA256 or blob != GIT_BLOB:
        raise ValueError('input hash does not match the pinned released aggregate file')
    mat = loadmat(path, struct_as_record=False, squeeze_me=True)
    a = mat['AGG1a']
    rows = condition_stats(a.stimuli.lbl, a.stimuli.comp, a.afteri.indi)
    return {'scope': 'Retrospective recheck of author-aggregated participant medians, not raw-trial reanalysis, new participants, or independent replication.',
            'provenance': {'source': 'https://github.com/christophWit/The-Non-Opponent-Nature-of-Colour-Afterimages',
                           'commit': '8901e132b6536a5b1333e7f8ba02bf14925e3a94',
                           'file': 'aggdata.mat', 'bytes': len(raw), 'sha256': digest, 'git_blob_sha1': blob,
                           'zenodo_v1_reported_md5': '76e7398d76b828d6215b6c107510306d',
                           'computed_md5': hashlib.md5(raw).hexdigest()},
            'method': 'Author-supplied participant medians minus central comparison hue on shortest signed arc; one-sample two-sided t tests, eight Bonferroni tests; confidence intervals unadjusted.',
            'alpha_per_test': ALPHA,
            'versions': {'python': '.'.join(map(str, sys.version_info[:3])), 'numpy': np.__version__, 'scipy': scipy.__version__},
            'conditions': rows,
            'n_significant': sum(row['significant_bonferroni_0_05_over_8'] for row in rows),
            'all_t_match_article_to_2_decimals': all(abs(row['t'] - row['published_t_rounded_2dp']) < 0.0051 for row in rows)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', default='.arena/witzel/aggdata.mat')
    args = parser.parse_args()
    print(json.dumps(analyze(args.path), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
