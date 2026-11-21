#!/usr/bin/env python3
"""Finite-cutoff diagnostics for a time-regulated version of Öttinger (2.51).

The report is numerical evidence, not a convergence proof; the companion note
contains the separate analytic argument. Requires numpy. Momentum spacing is 1.
"""
import json
import math
from pathlib import Path
import numpy as np


def sum_cutoff(n, epsilon, k=(1, 0, 0), mass=1.0):
    """Return time and common-exponential schemes on an individual-mode cube."""
    if n < 0 or epsilon < 0 or mass <= 0:
        raise ValueError('n, epsilon must be nonnegative and mass positive')
    k = np.asarray(k, dtype=int)
    grid = np.arange(-n, n+1)
    pts = np.stack(np.meshgrid(grid, grid, grid, indexing='ij'), -1).reshape(-1, 3)
    energy = np.sqrt(mass*mass+np.sum(pts*pts, axis=1))
    width = 2*n+1
    k2 = int(k @ k)
    a0 = ak = b = correction = 0.0
    for p, wp in zip(pts, energy):
        for target in (0, 1):
            r = (k if target else np.zeros(3, dtype=int))-p-pts
            valid = np.all(np.abs(r) <= n, axis=1)
            if not valid.any():
                continue
            rv = r[valid]
            index = ((rv[:, 0]+n)*width+(rv[:, 1]+n))*width+rv[:, 2]+n
            wq = energy[valid]
            wr = energy[index]
            omega = wp+wq+wr
            base = np.exp(-epsilon*omega)/(wp*wq*wr)
            a = np.sum(base/omega)
            if target:
                ak += a
            else:
                a0 += a
                b += np.sum(base/omega**3)
                correction += np.sum(base*(epsilon/omega**2+epsilon**2/(2*omega)))
    common = a0-ak-k2*b
    return {'time_cutoff': float(common-k2*correction),
            'common_exponential': float(common),
            'gap': float(k2*correction)}


def run():
    rows = []
    for eps in (0.5, 0.75, 1.0):
        for n in (2, 4, 6, 8):
            v = sum_cutoff(n, eps)
            assert v['gap'] > 0
            assert math.isclose(v['common_exponential']-v['time_cutoff'],
                                v['gap'], abs_tol=1e-11, rel_tol=1e-11)
            rows.append({'epsilon': eps, 'N': n, **v})
    return {'scope': 'finite mode-cube samples, m=1, spacing=1, k=(1,0,0); no continuum proof',
            'momentum_normalization': 'raw sums; no factor L^-6', 'samples': rows}


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
