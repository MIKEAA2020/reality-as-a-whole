#!/usr/bin/env python3
"""Synthetic tests: these do not establish real S08 condition or event coding."""
import copy
import json
from pathlib import Path
from unittest.mock import patch
import roy_s08_fixed_transfer as task


def manifest():
    return {'participant':'S08','event_code_mapping':'same_as_S09',
            'event_mapping_evidence':'fixture evidence', 'condition_evidence':'fixture evidence',
            'files':{str(i):{'path':f'/private/S08_scan{i}_filtered_gac_cbc.mat',
                             'sha256':str(i)*64} for i in task.SCANS}}


def fails(m):
    try:task.validate_manifest(m)
    except ValueError:return
    raise AssertionError('Invalid manifest accepted')


def main():
    recorded=json.loads((Path(__file__).parent/'roy_s09_eeg_report_transfer.json').read_text())
    assert task.MODEL==recorded['training_model']
    m=manifest(); task.validate_manifest(m)
    for edit in ('subject','mapping','missing','duplicate','wrong_name','evidence','hash'):
        bad=copy.deepcopy(m)
        if edit=='subject':bad['participant']='S09'
        if edit=='mapping':bad['event_code_mapping']='unknown'
        if edit=='missing':del bad['files']['5']
        if edit=='duplicate':bad['files']['5']['sha256']=bad['files']['1']['sha256']
        if edit=='wrong_name':bad['files']['1']['path']='/private/S08_scan3_filtered_gac_cbc.mat'
        if edit=='evidence':bad['event_mapping_evidence']=' '
        if edit=='hash':bad['files']['1']['sha256']='garbage'
        fails(bad)
    # 105 windows per run, with pure, mixed and artifact cases; no fit call exists.
    rows=[{'slot':0,'label':1,'bad':False,'feature':0.0},
          {'slot':1,'label':2,'bad':False,'feature':0.3},
          {'slot':2,'label':2,'bad':True,'feature':None}]
    rows += [{'slot':i%21,'label':0,'bad':False,'feature':None} for i in range(102)]
    with patch.object(task,'read_windows',return_value=rows) as reader:
        result=task.run(m)
    assert [c.args[0].name for c in reader.call_args_list]==[f'S08_scan{i}_filtered_gac_cbc.mat' for i in task.SCANS]
    assert [c.args[1] for c in reader.call_args_list]==[str(i)*64 for i in task.SCANS]
    assert result['results']['1']['models']['eeg']['confusion_true_rows_pred_columns']==[[1,0],[0,1]]
    assert result['results']['1']['models']['eeg']['pure_clean_windows']==2
    assert result['results']['1']['models']['time_only']['pure_clean_accuracy']==0.5
    assert result['pooled_descriptive']['total_windows']==315
    assert result['pooled_descriptive']['unresolved_report_windows']==306
    assert result['pooled_descriptive']['pure_report_but_bad_epoch_windows']==3
    assert result['pooled_descriptive']['models']['eeg']['full_grid_correct_fraction']==6/315
    assert 'private' not in json.dumps(result) and 'fixture evidence' not in json.dumps(result)
    assert task.MODEL==recorded['training_model']
    with patch.object(task,'read_windows',return_value=rows[:-1]):
        try:task.run(m)
        except ValueError:pass
        else:raise AssertionError('Missing windows must stop')
    print('PASS: fixed model, scan isolation, manifest gates, baseline and denominators')

if __name__=='__main__':main()
