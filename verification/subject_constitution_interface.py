#!/usr/bin/env python3
"""Frozen finite spin/episode/report interface; no empirical subject claims."""
from fractions import Fraction as F
from itertools import permutations
from math import comb
from pathlib import Path
import json

from causal_influence_subject_gate import influence_graph
from competing_subject_constitution_rules import (
    connected_components, overlapping_local_maxima, relabel, lists,
)
from coupled_subject_boundary_gate import stationary

ROOT = Path(__file__).resolve().parent.parent
V = frozenset(range(4))
ENDPOINTS = frozenset((0, 3))


def selected(rule, active, pair):
    if rule == 'C':
        return connected_components(active, pair), frozenset()
    if rule == 'L':
        return overlapping_local_maxima(active, pair)
    raise ValueError(rule)


def contrast(sets, ties, endpoints):
    if ties:
        return None
    return int(any(endpoints <= subset for subset in sets))


def minority_error(n, flip):
    """Odd n, independent symmetric flip probability, strict majority wrong."""
    return sum(F(comb(n, k))*flip**k*(1-flip)**(n-k)
               for k in range(n//2+1,n+1))


def joint_with_assay(dist, z, flip):
    """Return a full (spin, Z, report) table; no claimed physical assay."""
    return {(state,z,r): prob * ((1-flip) if r==z else flip)
            for state,prob in dist.items() for r in (0,1)}


def main():
    flip=F(1,10); n=21
    assert n%2==1
    report=[]; checks=0
    for t in (F(0),F(1,4),F(1,2)):
        _,pair=influence_graph(t)
        dist=stationary(t,(None,)*4)
        q_equal=sum(prob for state,prob in dist.items() if state[0]==state[3])
        rows={}
        for rule in ('C','L'):
            sets,ties=selected(rule,V,pair)
            z=contrast(sets,ties,ENDPOINTS)
            for perm in permutations(range(4)):
                rel_pair={tuple(sorted((perm[i],perm[j]))):weight
                          for (i,j),weight in pair.items()}
                moved_sets,moved_ties=selected(rule,V,rel_pair)
                assert moved_sets==relabel(sets,perm)
                assert moved_ties==relabel(ties,perm)
                assert contrast(moved_sets,moved_ties,frozenset(perm[i] for i in ENDPOINTS))==z
                checks+=1
            error=None if z is None else (q_equal if z==0 else 1-q_equal)
            q_assay=None if z is None else (1-flip if z==1 else flip)
            rows[rule]={'subjects':lists(sets),'unresolved_ties':lists(ties),
                        'endpoint_joint_label':z,
                        'physical_comparator_error':str(error) if error is not None else None,
                        'hypothetical_assay_yes_probability':str(q_assay) if q_assay is not None else None}
            if z is not None and rule=='L':
                # XL and NL use identical prepared spin and phenomenal labels
                # and the same measurement channel, differing only in their
                # stipulated grounding interpretation.
                joint_xl=joint_with_assay(dist,z,flip)
                joint_nl=joint_with_assay(dist,z,flip)
                assert joint_xl==joint_nl and sum(joint_xl.values())==1
        report.append({'coupling':str(t),'physical_endpoint_agreement':str(q_equal),'rules':rows})
    lookup={x['coupling']:x for x in report}
    source=lookup['0']; target=lookup['1/4']; tie=lookup['1/2']
    assert source['rules']['C']['endpoint_joint_label']==source['rules']['L']['endpoint_joint_label']==0
    assert target['rules']['C']['endpoint_joint_label']==1
    assert target['rules']['L']['endpoint_joint_label']==0
    assert target['physical_endpoint_agreement']=='17/32'
    assert target['rules']['C']['physical_comparator_error']=='15/32'
    assert target['rules']['L']['physical_comparator_error']=='17/32'
    assert target['rules']['C']['hypothetical_assay_yes_probability']=='9/10'
    assert target['rules']['L']['hypothetical_assay_yes_probability']=='1/10'
    assert tie['rules']['L']['endpoint_joint_label'] is None
    err=minority_error(n,flip)
    out={'scope':'Fixed hypothetical finite model only; no subjects, observations, calibrated assay or physical recovery established.',
         'settings':report,'permutation_rule_checks':checks,
         'physical_comparator':{'target_yes_probability':'17/32',
              'target_error_C':'15/32','target_error_L':'17/32',
              'a_10_percent_error_bridge_fails_both':True},
         'assay':{'symmetric_error_rate':str(flip),'target_trials':n,'majority_threshold_yes':n//2+1,
                  'probability_wrong_each_if_independent':str(err),
                  'probability_wrong_each_decimal':float(err),
                  'full_XL_NL_joint_distributions_equal_by_construction':True},
         'negative_control':'L unresolved at t=1/2; no subject count or assay yes-probability inferred.'}
    text=json.dumps(out,indent=2)+'\n'
    (ROOT/'verification/subject_constitution_interface.json').write_text(text)
    print(text)


if __name__=='__main__': main()
