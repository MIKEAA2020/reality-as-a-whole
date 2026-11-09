#!/usr/bin/env python3
"""Synthetic directory/ZIP and failure-path checks; no patient images."""
from pathlib import Path
import tempfile
import zipfile

import nibabel as nib
import numpy as np
from roy_mri_pair_inventory import inventory


def main():
    with tempfile.TemporaryDirectory() as temp:
        base=Path(temp)/'source'
        base.mkdir()
        for n in (1, 3):
            name=base/f'example-0007-{n:05d}-{n:06d}-01.hdr'
            image=nib.Nifti1Pair(np.full((2,3,4), n, dtype=np.uint16), np.diag([3.,3.,3.,1.]))
            nib.save(image, str(name))
        direct=inventory(base)
        assert direct['volumes_read']==2 and direct['pair_files_read']==4
        assert direct['missing_frame_indices_inside_observed_range']==[2]
        assert [v['mean_scaled'] for v in direct['volumes']]==[1.,3.]
        packed=Path(temp)/'scans.zip'
        with zipfile.ZipFile(packed,'w',compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(base.iterdir()):
                z.write(p,arcname='nested/'+p.name)
        assert inventory(packed)==direct
        (base/'example-0007-00003-000003-01.img').unlink()
        try:
            inventory(base)
        except ValueError as e:
            assert 'Unpaired' in str(e)
        else:
            raise AssertionError('Unpaired volume must stop the inspection')
    print('PASS: sequential directory/ZIP equivalence, missing index and unpaired-file stop')


if __name__=='__main__':
    main()
