#!/usr/bin/env python3
"""Finite checks of a randomized report audit and conservative bridge bound.

All populations are synthetic. E is a stipulated experience label, not
measured data; the assumed report-to-experience error is not estimated here.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def probability(rows, predicate):
    return sum((p for p, g, e, r, y in rows if predicate(g, e, r, y)), F(0))


def rates(rows):
    assert sum(row[0] for row in rows) == 1
    return {
        'gate_failure': probability(rows, lambda g,e,r,y: not g),
        'report_experience_disagreement': probability(rows, lambda g,e,r,y: r != e),
        'proxy_report_disagreement': probability(rows, lambda g,e,r,y: y != r),
        'proxy_experience_disagreement': probability(rows, lambda g,e,r,y: y != e),
        'proxy_positive': probability(rows, lambda g,e,r,y: y == 1),
    }


def random_audit_disagreement(rows, audit_probability):
    # Audit A is randomized independently after all target-window values
    # have been determined. R is the potential report that an audit elicits.
    audited_weight = F(0)
    audited_disagreement = F(0)
    for p, g, e, r, y in rows:
        for audit in (0, 1):
            p_joint = p * (audit_probability if audit else 1-audit_probability)
            if audit:
                audited_weight += p_joint
                if r != y:
                    audited_disagreement += p_joint
    return audited_disagreement / audited_weight


def main():
    # Disjoint failures saturate the union bounds for either scoped hypothesis.
    # Each row is (probability, gate G, experience E, potential report R, proxy Y).
    m = [(F(1,10),0,0,0,0), (F(1,20),1,1,0,0),
         (F(2,25),1,1,1,0), (F(77,100),1,1,1,1)]
    n = [(F(1,10),0,1,1,1), (F(1,20),1,0,1,1),
         (F(2,25),1,0,0,1), (F(77,100),1,0,0,0)]
    rm, rn = rates(m), rates(n)
    assert all(e == 1 for p,g,e,r,y in m if g)
    assert all(e == 0 for p,g,e,r,y in n if g)
    for row in (rm,rn):
        assert row['gate_failure'] == F(1,10)
        assert row['proxy_report_disagreement'] == F(2,25)
        assert row['report_experience_disagreement'] == F(1,20)
        assert row['proxy_experience_disagreement'] == F(13,100)
    assert rm['proxy_positive'] == F(77,100)
    assert rn['proxy_positive'] == F(23,100)
    for a in (F(1,10),F(1,4),F(1,2),F(1)):
        assert random_audit_disagreement(m,a) == F(2,25)
        assert random_audit_disagreement(n,a) == F(2,25)

    # Physically observed (R,Y,G) has same law but E can equal R or 1-R.
    truth = [(p,g,r,r,y) for p,g,e,r,y in m]
    inverted = [(p,g,1-r,r,y) for p,g,e,r,y in m]
    def observed(rows):
        out = {}
        for p,g,e,r,y in rows:
            out[(g,r,y)] = out.get((g,r,y),F(0)) + p
        return out
    assert observed(truth) == observed(inverted)
    assert rates(truth)['report_experience_disagreement'] == 0
    assert rates(inverted)['report_experience_disagreement'] == 1

    # Exhaustively check single-state implications and triangle inequality,
    # including an unresolved symbol -1 that counts as an error for both.
    checked = 0
    for g,e,r,y in product((0,1), (0,1,-1), (0,1,-1), (0,1,-1)):
        # Treat unresolved target or readout conservatively as mismatch.
        d = int(r == -1 or y == -1 or r != y)
        z = int(e == -1 or r == -1 or e != r)
        ey = int(e == -1 or y == -1 or e != y)
        assert ey <= d+z
        # For M, admissible valid gate requires E=1; for D, E=0.
        if not g or e == 1:
            assert int(y != 1) <= int(not g)+d+z
        if not g or e == 0:
            assert int(y == 1) <= int(not g)+d+z
        checked += 1
    output = {
        'status': 'passed', 'single_state_cases_checked': checked,
        'synthetic_rival_M': {k:str(v) for k,v in rm.items()},
        'synthetic_rival_D': {k:str(v) for k,v in rn.items()},
        'unconditional_proxy_positive_separation': str(rm['proxy_positive']-rn['proxy_positive']),
        'random_audit_probabilities_checked': ['1/10','1/4','1/2','1'],
        'random_audit_conditional_disagreement': '2/25',
        'same_observed_GR_Y_can_have_report_error': ['0','1'],
        'scope': 'Illustrative exact probability distributions and algebra, not a study or validated assay. Audit selection is independent after the target window and potential report consistency is assumed. Actual experience, physical gate validity and report-to-experience error are not measured or derived.'}
    text = json.dumps(output,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
