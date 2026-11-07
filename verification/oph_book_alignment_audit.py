#!/usr/bin/env python3
"""Finite controls for a declared vector analogy to OPH book ch. 41.

The identity is elementary, and the example is not OPH's native process or
an empirical model of pain. See OPH_BOOK_EXPERIENCE_ALIGNMENT_AUDIT.md.
"""
from itertools import product
from math import hypot, isclose
from pathlib import Path
import json

V = ((1,0), (-1,0), (0,1), (0,-1))


def quantities(x, inputs):
    hx = sum(v[0] for v in inputs)
    hy = sum(v[1] for v in inputs)
    hnorm = hypot(hx,hy)
    dot = x[0]*hx+x[1]*hy
    local_load = hnorm-dot
    seam_sum = len(inputs)-dot
    irreducible_conflict = len(inputs)-hnorm
    assert isclose(seam_sum, irreducible_conflict+local_load, abs_tol=1e-12)
    assert local_load >= -1e-12 and irreducible_conflict >= -1e-12
    return {'x':list(x),'inputs':[list(v) for v in inputs], 'field':[hx,hy],
            'alignment_remainder':local_load,'seam_sum':seam_sum,
            'best_achievable_seam_sum':irreducible_conflict}


def main():
    cases=0
    hidden_conflicts=0
    nonzero_field_hidden=0
    for n in range(1,7):
        for xs in product(V, repeat=n):
            for x in V:
                q=quantities(x,xs)
                cases+=1
                if abs(q['alignment_remainder']) < 1e-12 and q['seam_sum'] > 0:
                    hidden_conflicts+=1
                    if q['field'] != [0,0]:
                        nonzero_field_hidden+=1
    same_x_same_field_no_conflict=quantities((1,0),((1,0),))
    same_x_same_field_conflict=quantities((1,0),((1,0),(1,0),(-1,0)))
    assert same_x_same_field_no_conflict['field']==same_x_same_field_conflict['field']==[1,0]
    assert same_x_same_field_no_conflict['alignment_remainder']==0
    assert same_x_same_field_conflict['alignment_remainder']==0
    assert same_x_same_field_no_conflict['seam_sum']==0
    assert same_x_same_field_conflict['seam_sum']==2
    assert same_x_same_field_conflict['best_achievable_seam_sum']==2
    assert nonzero_field_hidden>0
    out={'status':'passed','cases':cases,'zero_local_remainder_positive_seam_sum':hidden_conflicts,
         'of_which_nonzero_aggregate_field':nonzero_field_hidden,
         'matching_aggregate_no_conflict':same_x_same_field_no_conflict,
         'matching_aggregate_conflict':same_x_same_field_conflict,
         'scope':'Toy vector seam score with freely chosen unit x and fixed unit target vectors; not a simulation of OPH native dynamics, consciousness, or clinical experience. Enumeration is a control, not proof of the general identity.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
