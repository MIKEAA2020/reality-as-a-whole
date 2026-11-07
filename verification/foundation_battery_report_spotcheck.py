#!/usr/bin/env python3
"""Independent scoped checks prompted by the supplied external battery report.

This is not the report's preregistered code, does not reproduce its full
battery, and does not validate any metaphysical or physical premise.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parent.parent
COMMIT='42927f7debe04cf61c6da1fa6fd30501b5f4a0fb'
SOURCE='CURRENT_FRAMEWORK_BATTERY_DOSSIER.md'
REPORTED_SHA='be6443432fee63f7c9a54efb96da8d9f5f8aee36aabf522a35ac9988d3330aa2'


def main():
    frozen=subprocess.run(['git','show',f'{COMMIT}:{SOURCE}'],cwd=ROOT,
                          capture_output=True,check=True).stdout
    digest=hashlib.sha256(frozen).hexdigest()
    assert digest==REPORTED_SHA
    assert hashlib.sha256((ROOT/SOURCE).read_bytes()).hexdigest()==REPORTED_SHA

    # At one point, d=◇p and e=◇¬p are independent Boolean slots. Strong
    # schema instances for p and ¬p plus T for p suffice for p↔□p.
    rows=[]
    for p,d,e in product((False,True),repeat=3):
        schema_p=(not d) or p
        schema_not_p=(not e) or (not p)
        box_p=not e
        T_p=(not box_p) or p
        T_not_p=d or (not p)  # □¬p = ¬◇p; T applied to ¬p
        if schema_p and schema_not_p and T_p:
            assert p==box_p
            rows.append({'p':p,'diamond_p':d,'diamond_not_p':e,
                         'box_p':box_p,'T_for_negation':T_not_p})
    assert len(rows)==3
    full_T=[r for r in rows if r['T_for_negation']]
    assert len(full_T)==2
    assert all(r['p']==r['diamond_p'] for r in full_T)

    # Independent illustration: same classical interacting transition and
    # readout under two different stipulated plural-subject partitions.
    partition_1=((0,1),(2,3))
    partition_2=((0,),(1,),(2,),(3,))
    assert len(partition_1)==2 and len(partition_2)==4
    checks=0
    for x in product((0,1),repeat=4):
        for u in product((0,1),repeat=4):
            def outcome(partition):
                assert partition in (partition_1,partition_2)
                nxt=tuple(x[(i-1)%4]^x[(i+1)%4]^u[i] for i in range(4))
                return nxt, tuple(nxt[i]^u[i] for i in range(4))
            assert outcome(partition_1)==outcome(partition_2)
            checks+=1
    assert checks==256

    # Same three labelled centers and question, different normalized positive
    # measures. This is an independent example, not a replay of their file.
    m1=(F(1,3),F(1,3),F(1,3))
    m2=(F(1,2),F(1,4),F(1,4))
    assert sum(m1)==sum(m2)==1 and all(x>0 for x in m1+m2)
    assert m1[0]==F(1,3) and m2[0]==F(1,2)

    satisfying=[]
    for perfect,best in product((False,True),repeat=2):
        if ((not perfect) or best) and (not best):
            assert not perfect
            satisfying.append([perfect,best])
    assert satisfying==[[False,False]]

    result={'status':'passed', 'frozen_commit':COMMIT, 'source_path':SOURCE,
            'source_sha256':digest,
            'modal_valid_rows_with_T_for_p_only':rows,
            'modal_row_count_with_full_T_for_p_and_negation':len(full_T),
            'independent_subject_partition_counts':[2,4],
            'independent_intervention_cases_checked':checks,
            'illustrative_self_location_probabilities':['1/3','1/2'],
            'nonoptimality_satisfying_perfect_best_assignments':satisfying,
            'scope':'Independent elementary spot checks only. The reported source hash is confirmed. External preregistration, source program, JSON and freeze file were not provided, so their execution, exact encodings and formal admission criteria are not independently verified. Toy partitions do not establish real subjects, genuinely possible worlds or physical predictions.'}
    text=json.dumps(result,indent=2)+'\n'
    (ROOT/'verification/foundation_battery_report_spotcheck.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
