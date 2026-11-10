#!/usr/bin/env python3
"""Synthetic folds check; not evidence for actual data or experience."""
from roy_s09_development_run_crosscheck import crosscheck


def row(label,feature):
    return {'slot':0,'label':label,'bad':False,'feature':feature}


def main():
    scans={1:[row(1,3),row(2,-1)],2:[row(1,5),row(2,-3)],3:[row(1,7),row(2,-5)]}
    r=crosscheck(scans)
    assert len(r['folds'])==3
    for i,fold in enumerate(r['folds'],1):
        assert fold['held_out_scan']==i and i not in fold['fit_scans']
        assert fold['result']['models']['eeg']['pure_clean_accuracy']==1
    assert r['folds'][0]['training_model']['mean_code1']==6
    assert r['folds'][1]['training_model']['mean_code1']==5
    assert r['folds'][2]['training_model']['mean_code1']==4
    try:crosscheck({1:scans[1],2:scans[2]})
    except ValueError:pass
    else:raise AssertionError('Incomplete development scans must stop')
    print('PASS: leave-one-run-out fit isolation, scoring and missing-input stop')


if __name__=='__main__':main()
