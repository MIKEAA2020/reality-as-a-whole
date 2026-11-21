#!/usr/bin/env python3
"""Finite-mode checks of a regulator gap; see the accompanying analytic note.

The FFT evaluates A_0(t) on an individual-mode cube. Gauss-Legendre quadrature
performs the Laplace integral. Finite-N values do not prove the continuum limit.
Requires numpy.
"""
import json
import math
from pathlib import Path
import numpy as np


def a0_fft(n, t, mass=1.0):
    if n < 0 or t <= 0 or mass <= 0:
        raise ValueError('n>=0, t>0 and mass>0 required')
    # Triple sums lie in [-3N,3N], so M>3N prevents aliasing into zero.
    size = max(1, 3*n+1)
    coords = np.arange(-n, n+1)
    sq = coords.astype(float)**2
    omega = np.sqrt(mass*mass+sq[:, None, None]+sq[None, :, None]+sq[None, None, :])
    weights = np.exp(-t*omega)/omega
    arr = np.zeros((size, size, size))
    index = coords % size
    arr[np.ix_(index, index, index)] = weights
    transform = np.fft.fftn(arr)
    return float(np.fft.ifftn(transform**3)[0, 0, 0].real)


def gap_fft(n, epsilon, mass=1.0, points=32):
    if epsilon <= 0 or points < 2:
        raise ValueError('epsilon>0 and points>=2 required')
    nodes, weights = np.polynomial.legendre.leggauss(points)
    zs = (nodes+1)/2
    total = 0.0
    for z, weight in zip(zs, weights/2):
        t = epsilon/z
        total += weight*(1-z/2)*t**3*a0_fft(n, t, mass)
    return float(total)


def run():
    samples = []
    for eps, ns in ((0.5, (8, 12, 20)), (0.25, (12, 20, 32)),
                    (0.125, (20, 32, 48))):
        for n in ns:
            samples.append({'epsilon': eps, 'N': n, 'gap_k_squared_1': gap_fft(n, eps)})
    kernel_samples = [{'t': t, 'N': n, 't_cubed_A0': t**3*a0_fft(n, t)}
                      for t, n in ((0.5, 20), (0.25, 36), (0.125, 64))]
    return {'scope': 'finite mode cubes and Gauss quadrature, h=m=1, |k|^2=1',
            'exact_universal_normalized_coefficient': '3/(128*pi^4)',
            'exact_raw_short_time_coefficient': 2*math.pi**2,
            'exact_gap_for_L_2pi_k2_1': 1.5*math.pi**2,
            'samples': samples, 'kernel_samples': kernel_samples}


if __name__ == '__main__':
    report = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
