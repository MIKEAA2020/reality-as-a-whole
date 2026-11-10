#!/usr/bin/env python3
"""Synthetic pair/ZIP controls, not medical or real-data validation."""
import tempfile
import zipfile
from pathlib import Path

import nibabel as nib
import numpy as np
from roy_structural_pair_inventory import inventory


def must_fail(path):
    try:
        inventory(path)
    except ValueError:
        return
    raise AssertionError('Invalid archive accepted')


def main():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        path = root / 'test.hdr'
        data = np.arange(24, dtype=np.float32).reshape(2, 3, 4)
        nib.save(nib.Nifti1Pair(data, np.eye(4)), str(path))
        hdr, img = path.read_bytes(), path.with_suffix('.img').read_bytes()
        good = root / 'good.zip'
        with zipfile.ZipFile(good, 'w') as z:
            z.writestr('one/test.hdr', hdr)
            z.writestr('one/test.img', img)
        got = inventory(good)
        assert got['pair_files_read'] == 2
        assert got['geometry']['shape'] == [2, 3, 4]
        assert got['voxel_qc']['nonzero_voxels'] == 23
        assert got['voxel_qc']['mean_scaled'] == 11.5
        for name, members in [('unpaired', [('test.hdr', hdr)]),
                              ('mismatched', [('a.hdr', hdr), ('b.img', img)]),
                              ('extra', [('a.hdr', hdr), ('a.img', img), ('extra.txt', b'x')])]:
            p = root / f'{name}.zip'
            with zipfile.ZipFile(p, 'w') as z:
                for member, content in members:
                    z.writestr(member, content)
            must_fail(p)
        bad = root / 'bad.zip'
        bad_data = data.copy(); bad_data[0, 0, 0] = np.nan
        nib.save(nib.Nifti1Pair(bad_data, np.eye(4)), str(path))
        with zipfile.ZipFile(bad, 'w') as z:
            z.writestr('test.hdr', path.read_bytes())
            z.writestr('test.img', path.with_suffix('.img').read_bytes())
        must_fail(bad)
    print('PASS: synthetic structural ZIP, missing, mismatched, extra, and non-finite controls')


if __name__ == '__main__':
    main()
