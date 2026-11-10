#!/usr/bin/env python3
"""Synthetic arithmetic and stop rules, not validation of reported experience."""
from copy import deepcopy
from roy_s09_condition_coverage import summarize


def main():
    audit={'scans':[{'scan':i,'documented_condition':'A' if i<=5 else 'B'} for i in range(1,10)]}
    inspections={i:{'sha256':str(i)} for i in range(1,10)}
    scans=[]
    for i in range(1,10):
        scans.append({'file':f'S09_scan{i}_filtered_gac_cbc.mat','sha256':str(i),
                      'sampling_hz':1,'all_trial_samples':{'samples':10,
                      'seconds_by_label':{'unknown_before_first_event':1, 'code_1':4,
                      'code_2':3, 'code_3_mixed':2}}})
    result=summarize([{'scans':scans}],audit,inspections)
    assert result['groups']['A']['trial_seconds']==50
    assert result['groups']['A']['unresolved_fraction']==0.3
    broken=deepcopy(scans);broken[0]['sha256']='wrong'
    for inputs in ([{'scans':broken}], [{'scans':scans[:-1]}]):
        try: summarize(inputs,audit,inspections)
        except ValueError: pass
        else: raise AssertionError('Bad or incomplete provenance must stop')
    print('PASS: synthetic condition grouping, denominators and mismatch stops')


if __name__=='__main__': main()
