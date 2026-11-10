#!/usr/bin/env python3
"""Synthetic checks only; not independent validation of the source labels."""
import tempfile
from pathlib import Path

import fitz
import numpy as np
from scipy.io import savemat
from roy_s09_public_support_audit import labels, code_labels, pdf_labels, motion_qc


def must_fail(f):
    try:
        f()
    except ValueError:
        return
    raise AssertionError('Invalid synthetic data accepted')


def main():
    sample = ['rivalry', 'rivalry', 'rivalry', 'replay_smooth', 'rivalry',
              'replay_smooth', 'rivalry', 'replay_inst', 'replay_inst']
    body = ','.join(f"'{x}'" for x in sample)
    assert labels(body) == sample
    assert code_labels('s9 = {'+body+'};') == sample
    must_fail(lambda: labels(body + ",'unknown'"))
    must_fail(lambda: code_labels('s19 = {'+body+'};'))
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        doc=fitz.open(); doc.new_page(); page=doc.new_page()
        first = ','.join(f"'{x}'" for x in sample[:5])
        second = ','.join(f"'{x}'" for x in sample[5:])
        page.insert_text((40, 50), '- S09\nScan Types: {'+first+',\n'+second+'}\n- S10', fontsize=8)
        pdf=d/'test.pdf'; doc.save(pdf);doc.close()
        assert pdf_labels(pdf) == sample
        txt=d/'motion.txt'; mask=d/'mask.mat'
        np.savetxt(txt, np.arange(18).reshape(3,6));savemat(mask, {'mask': np.ones(3)})
        result=motion_qc(txt,mask,3)
        assert result['motion_rows']==3 and result['motion_columns']==6 and result['mask_all_ones']
        must_fail(lambda: motion_qc(txt,mask,4))
        v=np.arange(18,dtype=float).reshape(3,6);v[0,0]=np.nan;np.savetxt(txt,v)
        must_fail(lambda: motion_qc(txt,mask,3))
    print('PASS: synthetic labels, PDF layout, motion shape and invalid-input stops')


if __name__ == '__main__':
    main()
