#!/usr/bin/env python3
"""Finite semantic controls for two existing necessity routes; not metaphysical models."""
from itertools import product
import json
from pathlib import Path


def box(values, world, access):
    return all(values[v] for v in access[world])


def diamond(values, world, access):
    return any(values[v] for v in access[world])


def global_modal_schema(access):
    """Every binary valuation over this finite frame satisfies ◇p -> p at every world."""
    n=len(access)
    return all(not diamond(p,w,access) or p[w] for p in product((False,True),repeat=n) for w in range(n))


def evaluate(subject_counts, truths, access):
    n=len(access)
    if len(subject_counts)!=n or len(truths)!=n or any(v<0 for v in subject_counts):raise ValueError('Invalid model')
    e=[v>0 for v in subject_counts]
    return {'experience_actual_at_0':e[0], 'necessary_truth_at_0':box(truths,0,access),
            'experience_necessary_at_0':box(e,0,access),
            'occurrence_implies_necessity_at_0':not e[0] or box(e,0,access),
            'truth_experience_bridge_necessary_at_0':box([not t or x for t,x in zip(truths,e)],0,access),
            'all_global_propositions_modal_schema':global_modal_schema(access),
            'subject_count_at_0':subject_counts[0]}


def main():
    two=[[0,1],[0,1]]; one=[[0]]
    a=evaluate([1,0],[True,True],two)
    b=evaluate([1],[True],one)
    c=evaluate([2],[True],one)
    assert a['experience_actual_at_0'] and a['necessary_truth_at_0']
    assert not a['experience_necessary_at_0'] and not a['occurrence_implies_necessity_at_0']
    assert not a['truth_experience_bridge_necessary_at_0'] and not a['all_global_propositions_modal_schema']
    assert all(x['experience_necessary_at_0'] and x['all_global_propositions_modal_schema'] for x in (b,c))
    assert b['subject_count_at_0']==1 and c['subject_count_at_0']==2
    out={'scope':'finite formal controls, not a metaphysical possibility judgment',
         'accessible_experience_free_alternative':a,'single_world_one_subject':b,'single_world_two_subjects':c}
    path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: occurrence and truth need bridges; global collapse does not fix plurality')

if __name__=='__main__':main()
