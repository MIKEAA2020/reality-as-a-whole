#!/usr/bin/env python3
"""Synthetic, bounded test of a difference between two published code listings.

Pass the original Python file at the pinned commit (or matching Zenodo bytes).
No patient data, original MATLAB execution, or clinical accuracy is tested.
Requires numpy, scipy and matplotlib; see requirements-spectral-translation.txt.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

EXPECTED_SHA256 = '45baa3452b2d2830723126e83453e8552370e023f8089ea930d36dfa055438e7'
MATCH = '    idxs_peaks = idxs_peaks[YRes0[idxs_peaks] > threResPks ]'
REPLACEMENT = '    threResPks = max(threResPks, .1)\n' + MATCH


def load_function(source, name):
    ns = {'__name__': name}
    exec(compile(source, name, 'exec'), ns)
    return ns['compute_SpectralExponent']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='original pinned compute_spectral_exponent.py')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    args = parser.parse_args()
    data = args.source.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f'Unexpected source SHA-256: {digest}')
    text = data.decode('utf-8').replace('\r\n', '\n')
    if text.count(MATCH) != 1:
        raise ValueError('Expected exactly one peak-selection line')
    published = load_function(text, 'pinned_python')
    floor_variant = load_function(text.replace(MATCH, REPLACEMENT), 'python_floor_variant')

    frequency = np.arange(1, 20.01, 1 / 3)
    # An exact synthetic PSD, not an EEG time series or patient data.
    # log10(PSD) = -1.5 log10(f) plus a small Gaussian peak.
    baseline = frequency ** -1.5
    bump = 0.12 * np.exp(-0.5 * ((frequency - 10) / 0.7) ** 2)
    spectrum = baseline * 10 ** bump
    original = published(frequency, spectrum, do_plot=False)
    altered = floor_variant(frequency, spectrum, do_plot=False)
    base_original = published(frequency, baseline, do_plot=False)
    base_altered = floor_variant(frequency, baseline, do_plot=False)
    assert abs(original[0] - (-1.4993671426851343)) < 1e-10
    assert abs(altered[0] - (-1.48287934479103)) < 1e-10
    assert int(original[3]['reject'].sum()) == 24
    assert int(altered[3]['reject'].sum()) == 0
    assert abs(base_original[0] - base_altered[0]) < 1e-10
    assert abs(base_original[0] + 1.5) < 1e-10
    result = {
        'status': 'PASS',
        'scope': 'Synthetic PSD; original pinned Python vs same Python with peak-threshold floor added. Not MATLAB execution, patient analysis or clinical validation.',
        'source_sha256': digest,
        'source_commit': '4bd4929d3a052d1c7eb0a5fb73ff860c4e4ac421',
        'synthetic_definition': 'f = 1, 1+1/3, ..., 20 Hz; PSD = f^-1.5 * 10^(0.12*exp(-0.5*((f-10)/0.7)^2))',
        'python': {'slope': float(original[0]), 'threshold': float(original[2]['threResPks']), 'rejected_resampled_points': int(original[3]['reject'].sum())},
        'floor_variant': {'slope': float(altered[0]), 'threshold': float(altered[2]['threResPks']), 'rejected_resampled_points': int(altered[3]['reject'].sum())},
        'difference_floor_minus_python': float(altered[0] - original[0]),
        'no_peak_baseline_slope': float(base_original[0]),
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
