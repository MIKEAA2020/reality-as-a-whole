#!/usr/bin/env python3
"""Bounded sequential NIfTI-pair QC for a local directory or ZIP.

Does not print original paths or DICOM metadata. Does not extract user-supplied
paths to disk. Every .hdr/.img byte in every paired volume is read. This is
format/QC inspection, NOT a time-series GLM or a check of task conditions.
Requires numpy==2.2.6 and nibabel==5.3.2.
"""
import argparse
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

import nibabel as nib
import numpy as np

# Matches the trailing scan-series and two matching volume indices, without
# retaining or printing any identifying prefix in the original filename.
TAIL = re.compile(r'-(\d{4})-(\d{5})-(\d{6})-(\d{2})$', re.I)
MAX_MEMBER_BYTES = 5 * 1024 * 1024
MAX_PAIR_BYTES = 100 * 1024 * 1024


def inventory(source):
    source = Path(source)
    archive = None
    if source.is_dir():
        entries = [(p.relative_to(source).as_posix(), p.stat().st_size, p)
                   for p in source.rglob('*') if p.is_file()]
        def read(item): return item.read_bytes()
    elif zipfile.is_zipfile(source):
        archive = zipfile.ZipFile(source)
        entries = [(i.filename, i.file_size, i) for i in archive.infolist() if not i.is_dir()]
        def read(item): return archive.read(item)
    else:
        raise ValueError('Input must be a local directory or ZIP')
    try:
        groups = {}
        other_count = 0
        total_bytes = 0
        for name, size, ref in entries:
            p = PurePosixPath(name)
            ext = p.suffix.lower()
            if ext not in ('.hdr', '.img'):
                other_count += 1
                continue
            if size < 0 or size > MAX_MEMBER_BYTES:
                raise ValueError('A pair member exceeds the 5 MiB safety cap')
            total_bytes += size
            if total_bytes > MAX_PAIR_BYTES:
                raise ValueError('Pair data exceed the 100 MiB safety cap')
            match = TAIL.search(p.stem)
            if not match:
                raise ValueError('A pair filename does not match expected series/frame pattern')
            series, a, b, image = match.groups()
            if int(a) != int(b):
                raise ValueError('Frame number fields differ')
            key = (str(p.parent), p.stem)
            group = groups.setdefault(key, {'series': int(series), 'frame': int(a)})
            if ext in group:
                raise ValueError('Duplicate pair member')
            group[ext] = (ref, size)
        if not groups:
            raise ValueError('No .hdr/.img pairs found')
        if any('.hdr' not in g or '.img' not in g for g in groups.values()):
            raise ValueError('Unpaired header or image; stop')
        if len({g['series'] for g in groups.values()}) != 1:
            raise ValueError('Multiple series; split them before inspection')
        if len({g['frame'] for g in groups.values()}) != len(groups):
            raise ValueError('Duplicate frame numbers')
        baseline = None
        results = []
        with tempfile.TemporaryDirectory() as temp:
            local = Path(temp)/'volume.hdr'
            for g in sorted(groups.values(), key=lambda x: x['frame']):
                hdr = read(g['.hdr'][0])
                img_bytes = read(g['.img'][0])
                if len(hdr) != g['.hdr'][1] or len(img_bytes) != g['.img'][1]:
                    raise ValueError('Member byte count mismatch')
                local.write_bytes(hdr)
                local.with_suffix('.img').write_bytes(img_bytes)
                image = nib.load(str(local))
                if len(image.shape) != 3:
                    raise ValueError('Expected one 3D volume per image pair')
                values = np.asanyarray(image.dataobj)
                geometry = {'shape': list(image.shape), 'dtype': str(image.get_data_dtype()),
                            'zooms_mm': [float(z) for z in image.header.get_zooms()],
                            'affine': image.affine.tolist()}
                if not np.isfinite(image.affine).all() or not np.isfinite(values).all():
                    raise ValueError('Nonfinite affine or voxel values')
                if baseline is None:
                    baseline = geometry
                elif geometry != baseline:
                    raise ValueError('Volume geometry changes; stop')
                results.append({'frame': g['frame'], 'header_bytes': len(hdr),
                    'image_bytes': len(img_bytes),
                    'header_sha256': hashlib.sha256(hdr).hexdigest(),
                    'image_sha256': hashlib.sha256(img_bytes).hexdigest(),
                    'nonzero_voxels': int(np.count_nonzero(values)),
                    'min_scaled': float(values.min()), 'max_scaled': float(values.max()),
                    'mean_scaled': float(values.mean())})
        frames = [r['frame'] for r in results]
        missing = sorted(set(range(min(frames), max(frames)+1))-set(frames))
        return {'kind': 'sequential local pair inventory; no task or GLM inference',
            'volumes_read': len(results), 'pair_files_read': 2*len(results),
            'other_files_ignored': other_count, 'pair_bytes_read': total_bytes,
            'series_number': next(iter(groups.values()))['series'],
            'frame_min': min(frames), 'frame_max': max(frames),
            'missing_frame_indices_inside_observed_range': missing,
            'geometry': baseline, 'volumes': results,
            'limitations': ['Checks observed files, not whether the acquired series is complete.',
                'Series-number agreement does not establish scan condition or event/volume alignment.',
                'Voxel aggregates are QC only, not an fMRI statistical analysis.']}
    finally:
        if archive is not None:
            archive.close()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('input_path', type=Path)
    p.add_argument('--expect-volumes', type=int)
    args = p.parse_args()
    output = inventory(args.input_path)
    if args.expect_volumes is not None and output['volumes_read'] != args.expect_volumes:
        raise ValueError('Observed volume count differs from requested count')
    print(json.dumps(output, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
