#!/usr/bin/env python3
"""Read a bounded structural ZIP containing exactly one NIfTI header/image pair.

Report only numeric geometry, intensity QC and hashes; never emit archive member
names, header descriptions or images. This does not validate defacing, anatomy,
registration, participant identity or clinical status. Requires numpy/nibabel.
"""
import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

import nibabel as nib
import numpy as np

MAX_MEMBER_BYTES = 150 * 1024 * 1024
MAX_PAIR_BYTES = 150 * 1024 * 1024


def inventory(source):
    with zipfile.ZipFile(source) as archive:
        entries = [entry for entry in archive.infolist() if not entry.is_dir()]
        if len(entries) != 2:
            raise ValueError('Expected exactly two structural pair files')
        pair = {}
        for entry in entries:
            name = PurePosixPath(entry.filename)
            ext = name.suffix.lower()
            if ext not in ('.hdr', '.img') or ext in pair:
                raise ValueError('Expected exactly one header and one image')
            if entry.file_size > MAX_MEMBER_BYTES:
                raise ValueError('Structural member exceeds safety cap')
            pair[ext] = entry
        if set(pair) != {'.hdr', '.img'}:
            raise ValueError('Incomplete structural pair')
        if PurePosixPath(pair['.hdr'].filename).with_suffix('') != PurePosixPath(pair['.img'].filename).with_suffix(''):
            raise ValueError('Structural pair stems differ')
        if sum(x.file_size for x in entries) > MAX_PAIR_BYTES:
            raise ValueError('Structural pair exceeds safety cap')
        with tempfile.TemporaryDirectory() as tmp:
            local = Path(tmp) / 'structural.hdr'
            checksums, sizes = {}, {}
            for ext in ('.hdr', '.img'):
                # ZipFile.read validates member CRC. No archive path is extracted.
                content = archive.read(pair[ext])
                if len(content) != pair[ext].file_size:
                    raise ValueError('Structural member size mismatch')
                checksums[ext] = hashlib.sha256(content).hexdigest()
                sizes[ext] = len(content)
                local.with_suffix(ext).write_bytes(content)
                del content
            image = nib.load(str(local))
            if not isinstance(image, nib.Nifti1Pair) or len(image.shape) != 3:
                raise ValueError('Expected a three-dimensional NIfTI-1 pair')
            values = np.asanyarray(image.dataobj)
            if not np.isfinite(values).all() or not np.isfinite(image.affine).all():
                raise ValueError('Non-finite structural data or affine')
            return {'kind': 'structural pair file and voxel QC, not anatomy or registration validation',
                    'pair_files_read': 2, 'header_bytes': sizes['.hdr'], 'image_bytes': sizes['.img'],
                    'header_sha256': checksums['.hdr'], 'image_sha256': checksums['.img'],
                    'geometry': {'shape': list(image.shape), 'dtype': str(image.get_data_dtype()),
                                 'zooms_mm': [float(x) for x in image.header.get_zooms()],
                                 'affine': image.affine.tolist(),
                                 'qform_code': int(image.header['qform_code']),
                                 'sform_code': int(image.header['sform_code'])},
                    'voxel_qc': {'all_finite': True, 'nonzero_voxels': int(np.count_nonzero(values)),
                                 'min_scaled': float(values.min()), 'max_scaled': float(values.max()),
                                 'mean_scaled': float(values.mean())},
                    'limitations': ['No visual or automated anatomical assessment or defacing validation.',
                                    'Header coordinate information does not establish structural-to-functional registration.',
                                    'No clinical assessment, segmentations, event timing or evidence of subjective experience.']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('zip_path', type=Path)
    args = parser.parse_args()
    print(json.dumps(inventory(args.zip_path), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
