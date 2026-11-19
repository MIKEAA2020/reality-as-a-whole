#!/usr/bin/env python3
"""Finite spectral-overlap control, not a psychophysical prediction.

A two-by-two construction using exact partial frequencies, plus a Gaussian
log-frequency kernel sensitivity check. No audio is produced and no human data
are analyzed. The relation between a spectral index and valence is unproven.
"""
from fractions import Fraction as F
from math import exp, log2, sqrt
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIMBRES = {'A': (2, 3), 'B': (3, 4)}
RATIOS = {'3:2': F(3, 2), '4:3': F(4, 3)}

def exact_overlap(indices, r):
    # Each partial carries half the power, and the statistic is the total
    # sum of products of matching weights, hence one common partial = 1/4.
    return sum((F(1, 4) for a, b in product(indices, repeat=2)
                if F(a) == r * b), F(0))

def cents(a, b):
    return 1200 * log2(float(a / b))

def smooth_overlap(indices, r, sigma):
    return sum(exp(-(cents(F(a), r * b) ** 2) / (2 * sigma ** 2)) / 4
               for a, b in product(indices, repeat=2))

exact = {t: {r: exact_overlap(p, q) for r, q in RATIOS.items()}
         for t, p in TIMBRES.items()}
assert exact == {'A': {'3:2': F(1, 4), '4:3': F(0)},
                 'B': {'3:2': F(0), '4:3': F(1, 4)}}
D = ((exact['A']['3:2'] - exact['A']['4:3']) -
     (exact['B']['3:2'] - exact['B']['4:3']))
assert D == F(1, 2)
# For a ratio-only model, the exact best in-sample estimates are the two
# within-ratio means; the minimum unweighted RMSE is 1/8. The interaction
# contrast gives the general bound RMSE >= |D|/4.
means = {r: sum(exact[t][r] for t in TIMBRES) / 2 for r in RATIOS}
mse = sum((exact[t][r] - means[r]) ** 2 for t, r in product(TIMBRES, RATIOS)) / 4
assert mse == F(1, 64) and D / 4 == F(1, 8)
smoothed = {}
for width in (1, 10, 50):
    vals = {t: {r: smooth_overlap(p, q, width) for r, q in RATIOS.items()}
            for t, p in TIMBRES.items()}
    assert vals['A']['3:2'] > vals['A']['4:3']
    assert vals['B']['3:2'] < vals['B']['4:3']
    smoothed[str(width)] = vals
# Uniformly rescaling both tones leaves all pairwise ratios, and hence the
# synthetic score, unchanged; this is a property of this chosen kernel only.
for a, b, scale in product((2, 3, 4), (2, 3, 4), (F(2), F(3, 2))):
    assert abs(cents(F(a), F(b)) - cents(scale*a, scale*b)) < 1e-10
out = {
 'scope': 'illustrative 2x2 spectral index only; not audio, neural data, valence or identity',
 'partial_indices': TIMBRES,
 'ratios': {k: str(v) for k, v in RATIOS.items()},
 'exact_overlap': {t: {r: str(x) for r,x in d.items()} for t,d in exact.items()},
 'contrast': str(D), 'best_ratio_only_rmse': str(D/4),
 'smoothing_width_cents': smoothed,
 'sampling_note': 'all weights are stipulated equal power; no matched-perceptual-loudness assumption',
}
p = ROOT / 'verification/timbre_interval_crossover_gate.json'
p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print('PASS exact spectral 2x2 crossover, interaction contrast =', D)
print('PASS ratio-only synthetic-index RMSE floor =', D/4)
print('PASS Gaussian log-frequency smoothing widths 1, 10, 50 cents')
print('Wrote', p.relative_to(ROOT))
