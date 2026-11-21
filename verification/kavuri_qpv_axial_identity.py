#!/usr/bin/env python3
"""Exact finite checks of an axial identity; no experimental or security validation."""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def intersect(*intervals):
    lo = max(i[0] for i in intervals)
    hi = min(i[1] for i in intervals)
    return (lo, hi) if hi > lo else None


def union(intervals):
    valid = sorted(i for i in intervals if i is not None)
    merged = []
    for lo, hi in valid:
        if merged and lo <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(hi, merged[-1][1]))
        else:
            merged.append((lo, hi))
    return merged


def axial_geometry(L, sA, sB, rA, rB, c=1):
    L, sA, sB, rA, rB, c = map(F, (L, sA, sB, rA, rB, c))
    ra = c*(rA-sA)/2
    rb = c*(rB-sB)/2
    m3 = c*(rA-sB)
    m4 = c*(rB-sA)
    if L <= 0 or c <= 0 or min(ra, rb) <= 0 or min(m3, m4) <= L:
        return None
    a = L/2
    sa, sb = (-a-ra, -a+ra), (a-rb, a+rb)
    e3, e4 = (-m3/2, m3/2), (-m4/2, m4/2)
    q = intersect(sa, sb, e3, e4)
    if q is None:
        return None
    cparts = (intersect(sa, e3), intersect(sb, e4))
    ci = union(cparts)
    qlen = q[1]-q[0]
    clen = sum((right-left for left, right in ci), F(0))
    return {'q': q, 'classical': ci, 'qlen': qlen, 'clen': clen,
            'ra': ra, 'rb': rb, 'm3': m3, 'm4': m4,
            'condition_release': c*abs(sA-sB) <= L,
            'condition_response': c*abs(rA-rB) <= L}


def main():
    eligible = good = outside = failures = 0
    examples = {}
    category_counts = {}
    # Units c=1. Overall time translation is immaterial, so set sA=0.
    # This deliberately explores both inside and outside the sufficient conditions.
    for L, sb, ra_time, rb_time in product(range(1, 7), range(-8, 9), range(1, 19), range(-7, 20)):
        case = axial_geometry(L, 0, sb, ra_time, rb_time)
        if case is None:
            continue
        identity = case['clen'] == L + case['qlen']
        category = f"release_{case['condition_release']}_response_{case['condition_response']}_identity_{identity}"
        category_counts[category] = category_counts.get(category, 0) + 1
        if case['condition_release'] and case['condition_response']:
            eligible += 1
            assert identity
            assert case['qlen'] == case['ra']+case['rb']-L
            assert case['clen'] == case['ra']+case['rb']
            assert case['classical'] == [(-case['m3']/2, case['m4']/2)]
            good += 1
        else:
            outside += 1
            if not identity:
                failures += 1
                kind = ('both_conditions_fail' if not case['condition_release'] else 'only_response_condition_fails')
                examples.setdefault(kind, {'L': L, 'sA': 0, 'sB': sb, 'rA': ra_time, 'rB': rb_time,
                    'quantum_length': str(case['qlen']), 'classical_length': str(case['clen']),
                    'release_condition': case['condition_release'], 'response_condition': case['condition_response']})
            elif not case['condition_release'] and case['condition_response']:
                examples.setdefault('release_condition_fails_identity_holds', {'L': L, 'sA': 0, 'sB': sb, 'rA': ra_time, 'rB': rb_time,
                    'quantum_length': str(case['qlen']), 'classical_length': str(case['clen']),
                    'release_condition': case['condition_release'], 'response_condition': case['condition_response']})
    assert eligible > 0 and failures > 0 and set(examples) == {'both_conditions_fail', 'only_response_condition_fails', 'release_condition_fails_identity_holds'}
    # Article central values, with c in m/ns, represented exactly as decimals.
    p = axial_geometry('195.1', '1291.0', '1429.1', '2340.3', '2207.7', '0.299792458')
    assert p is not None and p['condition_release'] and p['condition_response']
    assert p['clen'] == F('195.1')+p['qlen']
    out = {'scope': 'Exact rational tests of a conditional axial set identity, not security, source records or human identity.',
           'enumeration': {'qualifying_cases': eligible, 'identity_holds_qualifying_cases': good,
                           'outside_sufficient_conditions': outside, 'outside_cases_where_identity_fails': failures,
                           'counts_by_condition_and_identity': category_counts,
                           'outside_examples': examples},
           'preprint_central_inputs': {'release_separation_m': str(F('0.299792458')*F('138.1')),
               'response_separation_m': str(F('0.299792458')*F('132.6')),
               'verifier_separation_m': '195.1', 'quantum_length_m': str(p['qlen']),
               'comparable_classical_length_m': str(p['clen']),
               'ideal_classical_ratio': float(F('195.1')/p['qlen']),
               'comparable_classical_ratio': float(p['clen']/p['qlen'])}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
