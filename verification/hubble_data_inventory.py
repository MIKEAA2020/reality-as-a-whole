#!/usr/bin/env python3
"""Inventory public Banik et al. MAT files without interpreting opaque MCOS data.

Usage: python verification/hubble_data_inventory.py /path/to/hubFrct_2021 > inventory.json
Requires numpy and scipy. Source commit and retrieval are documented in
EXPANDING_BEC_DATA_FEASIBILITY.md. No inference or experimental fitting is done.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat


def inspect(path, root):
    data = loadmat(path)
    for name in ('Runs', 'time', 'AN', 'n1Ds'):
        if name not in data:
            raise ValueError(f'{path}: missing {name}')
    runs = data['Runs'].ravel()
    time = data['time'].ravel()
    atom = data['AN'].ravel()
    n1d = data['n1Ds']
    if n1d.ndim != 2 or not (len(runs) == len(time) == len(atom) == n1d.shape[1]):
        raise ValueError(f'{path}: per-column arrays do not align')
    opaque = data.get('None')
    classes = [] if opaque is None else [
        str(item['s2'].decode('utf-8', errors='replace')) for item in opaque.ravel()
    ]
    return {
        'path': str(path.relative_to(root)),
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'columns': len(time),
        'angular_bins': n1d.shape[0],
        # 1 ns rounding only prevents floating-point representations from
        # splitting nominally identical timestamps; includes control runs.
        'unique_time_values_rounded_1ns': len(np.unique(np.round(time, 9))),
        'time_min_s': float(np.min(time)),
        'time_max_s': float(np.max(time)),
        'nonfinite_time': int(np.count_nonzero(~np.isfinite(time))),
        'nonfinite_n1d': int(np.count_nonzero(~np.isfinite(n1d))),
        'opaque_classes': classes,
        'top_level_variables': sorted(k for k in data if not k.startswith('__')),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_root', type=Path)
    args = parser.parse_args()
    root = args.source_root.resolve()
    records = []
    for subset in ('expansions', 'contractions'):
        paths = sorted((root / 'data' / subset).glob('PhnRuns_*.mat'))
        if not paths:
            raise SystemExit(f'No MAT files found in data/{subset}')
        records.extend(inspect(path, root) for path in paths)
    grouped = {}
    for record in records:
        grouped.setdefault(record['sha256'], []).append(record['path'])
    duplicates = sorted((v for v in grouped.values() if len(v) > 1), key=lambda x: x[0])
    # Compare identically named files across the two directories by their
    # accessible numeric arrays. Different MAT headers/objects give different
    # file hashes even when these arrays are identical.
    exp = root / 'data' / 'expansions'
    con = root / 'data' / 'contractions'
    shared_names = sorted({p.name for p in exp.glob('PhnRuns_*.mat')} &
                          {p.name for p in con.glob('PhnRuns_*.mat')})
    common_arrays = []
    for name in shared_names:
        a = loadmat(exp / name, variable_names=['Runs', 'time', 'AN', 'n1Ds'])
        b = loadmat(con / name, variable_names=['Runs', 'time', 'AN', 'n1Ds'])
        common_arrays.append({'filename': name, 'arrays_equal': {
            k: bool(np.array_equal(a[k], b[k])) for k in ('Runs', 'time', 'AN', 'n1Ds')
        }})
    result = {
        'source': 'https://github.com/JQIamo/hubFrct_2021',
        'expected_commit': '88c8a87aed5961f589db66a7e7e4e97f161ad51c',
        'note': 'Expected commit is not verified by this script. Columns include phonon and normalization runs and must not be treated as independent time series.',
        'files': len(records),
        'files_by_directory': {subset: sum(r['path'].startswith(f'data/{subset}/') for r in records) for subset in ('expansions', 'contractions')},
        'distinct_file_hashes': len(grouped),
        'duplicate_file_groups': duplicates,
        'same_filename_numeric_comparisons': common_arrays,
        'all_shapes_aligned': True,
        'all_contain_phonondata_opaque_object': all('PhononData' in r['opaque_classes'] for r in records),
        'records': records,
    }
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
