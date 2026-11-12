#!/usr/bin/env python3
"""Test S08 QC gating with synthetic ZIPs and mocked image inventory."""
import tempfile
import zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import numpy as np
import roy_s08_mri_qc as q


def main():
    with tempfile.TemporaryDirectory() as tmp:
        d=Path(tmp)
        for scan in q.SCANS:
            with zipfile.ZipFile(d/f'scan{scan}.zip','w') as z:z.writestr('extra.txt','ok')
        def fake_hash(path):
            scan=int(path.name[4]) if path.suffix=='.zip' else int(path.name[8])
            return ('fake',q.ZIP_DROPBOX_HASH[scan]) if path.suffix=='.zip' else (q.EEG_SHA[scan],'fake')
        volume={'series_number':7,'volumes_read':3,'pair_files_read':6,'frame_min':1,'frame_max':3,
                'missing_frame_indices_inside_observed_range':[],'geometry':{'shape':[2,2,2]}}
        data={'dcminfo':SimpleNamespace(SeriesNumber=7),'sampling_freq':250,'latency_tr':np.array([1,551])}
        with patch.object(q,'hashes',side_effect=fake_hash),patch.object(q,'inventory',return_value=volume),patch.object(q,'loadmat',return_value=data):
            out=q.run(d,d)
            assert out['scans']['1']['other_files_read']==1
            assert out['scans']['1']['assumed_consecutive_first_frame_candidates']==[1,2]
            data['latency_tr']=np.array([1,552])
            assert q.run(d,d)['scans']['1']['assumed_consecutive_first_frame_candidates'] is None
            data['dcminfo'].SeriesNumber=8
            try:q.run(d,d)
            except ValueError:pass
            else:raise AssertionError('Series mismatch must stop')
        with patch.object(q,'hashes',return_value=('wrong','wrong')):
            try:q.run(d,d)
            except ValueError:pass
            else:raise AssertionError('Hash mismatch must stop')
    print('PASS: S08 ZIP hash, series, extra-file and conditional trigger gates')

if __name__=='__main__':main()
