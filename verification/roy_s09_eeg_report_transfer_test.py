#!/usr/bin/env python3
"""Synthetic-only tests; do not validate participant labels or experience."""
import numpy as np
from roy_s09_eeg_report_transfer import feature, train, assess


def row(slot,label,bad=False,z=None):return {'slot':slot,'label':label,'bad':bad,'feature':z}


def main():
    fs=250;t=np.arange(2*fs)/fs;low,high=6.6666666667,8.5714285714
    assert feature(np.sin(2*np.pi*low*t),fs,low,high)>0
    assert feature(np.sin(2*np.pi*high*t),fs,low,high)<0
    try:feature(np.zeros(2*fs),fs,low,high)
    except ValueError:pass
    else:raise AssertionError('Undefined spectral ratio must stop')
    training=[row(0,1,z=3),row(0,1,z=1),row(1,2,z=-2),row(1,2,z=-4)]
    model=train(training)
    assert model['mean_code1']==2 and model['mean_code2']==-3 and model['majority']==1
    assert model['slot_rules'][0]==1 and model['slot_rules'][1]==2 and model['slot_rules'][2]==1
    test=[row(0,1,z=1),row(1,2,z=-1),row(2,1,z=-3),row(3,0),row(4,2,bad=True)]
    got=assess(test,model)
    assert got['unresolved_report_windows']==1 and got['pure_report_but_bad_epoch_windows']==1
    assert got['models']['eeg']['confusion_true_rows_pred_columns']==[[1,1],[0,1]]
    assert got['models']['eeg']['pure_clean_accuracy']==2/3
    assert got['models']['eeg']['full_grid_correct_fraction']==2/5
    assert got['models']['majority']['pure_clean_accuracy']==2/3
    assert got['models']['time_only']['pure_clean_accuracy']==1.0
    tie=assess([row(0,1,z=-0.5)],model)
    assert tie['models']['eeg']['confusion_true_rows_pred_columns']==[[1,0],[0,0]]
    for invalid in ([row(0,1,z=1)], [row(0,1,z=np.nan),row(1,2,z=1)]):
        try:train(invalid)
        except ValueError:pass
        else:raise AssertionError('Missing class or nonfinite feature must stop')
    assert model==train(training), 'Test evaluation may not alter fitted model'
    print('PASS: spectral ordering, fit isolation, ties, baseline, confusion and abstention')


if __name__=='__main__':main()
