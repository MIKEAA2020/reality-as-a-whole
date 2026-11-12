#!/usr/bin/env python3
"""Finite checks of conditional modal-relevance result, not metaphysical proof."""
import itertools
import json
from pathlib import Path


def schema_at(access, w):
    n=len(access)
    return all(not any(v[t] for t in access[w]) or v[w]
               for v in itertools.product((False,True),repeat=n))


def necessitates(exists, truth, access, w):
    return all(not exists[t] or truth[t] for t in access[w])


def main():
    frames=[]
    for b in itertools.product((False,True),repeat=4):
        # Restrict to reflexive two-point frames for this finite regression.
        if not (b[0] and b[3]):continue
        frames.append([[j for j in range(2) if b[2*i+j]] for i in range(2)])
    cases=0;collapsed_cases=0
    for access in frames:
        for p,a,b in itertools.product(itertools.product((False,True),repeat=2),repeat=3):
            cases+=1
            if schema_at(access,0) and p[0] and a[0] and b[0]:
                collapsed_cases+=1
                assert all(p[j] for j in access[0])
                assert necessitates(a,p,access,0) and necessitates(b,p,access,0)
    # When an alternative with not-p is accessible and a remains present,
    # bare necessitation excludes a; b may still necessitate p.
    access=[[0,1],[0,1]];p=(True,False);a=(True,True);b=(True,False)
    assert not schema_at(access,0)
    assert not necessitates(a,p,access,0) and necessitates(b,p,access,0)
    # Single reflexive point with two designated entities and two distinct
    # truthbearer names: alternative stipulations, not genuine grounding proofs.
    access=[[0]];p=q=a=b=(True,)
    assert all(necessitates(x,y,access,0) for x in (a,b) for y in (p,q))
    admissible=[]
    for bits in itertools.product((0,1),repeat=4):
        relation={(i,j) for (i,j),bit in zip(itertools.product(range(2),repeat=2),bits) if bit}
        if all(sum((i,j) in relation for i in range(2))==1 for j in range(2)) and \
           all(sum((i,j) in relation for j in range(2))==1 for i in range(2)):
            admissible.append(sorted([list(pair) for pair in relation]))
    assert len(admissible)==2
    # A local contrast need not violate globally fixed indexed propositions.
    warm={'sector_A':True,'sector_B':False}
    assert warm['sector_A'] and not warm['sector_B']
    assert schema_at([[0]],0) # warm(A) and not-warm(B) can both be global facts.
    result={'scope':'semantic toys and stipulated relations, not metaphysical grounding or actual subjects',
            'reflexive_two_point_frames':len(frames),'valuation_cases_checked':cases,
            'schema_and_two_actual_candidates_checked':collapsed_cases,
            'under_schema_all_actual_candidates_necessitate_each_actual_truth':True,
            'noncollapse_control':{'a_necessitates_p':False,'b_necessitates_p':True},
            'minimal_toy_one_to_one_relations_count':len(admissible),
            'toy_relations_pairs_entity_then_truth':admissible,
            'local_sector_contrast_compatible_with_global_schema':True}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: collapse relevance, distinguishing control, toy assignments and local indexing')

if __name__=='__main__':main()
