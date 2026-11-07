"""Reference/gauge audit for a candidate qualitative identity, not neural data.

The HMM and calibration numbers are illustrative exact fractions. State names
are unanchored. Independent qualitative calibration is not supplied by this file.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


PI = (F(2,5),F(3,5))
T = ((F(3,4),F(1,4)),(F(1,3),F(2,3)))
# Probability of an observed binary symbol given each hidden state.
B = ((F(4,5),F(1,5)),(F(1,5),F(4,5)))


def validate(pi,t,b):
    assert sum(pi)==1 and all(x>=0 for x in pi)
    assert all(sum(row)==1 and all(x>=0 for x in row) for row in t)
    assert all(sum(row)==1 and all(x>=0 for x in row) for row in b)


def likelihood(sequence,pi,t,b):
    if not sequence:
        return F(1)
    v=tuple(pi[i]*b[i][sequence[0]] for i in range(2))
    for symbol in sequence[1:]:
        v=tuple(sum((v[i]*t[i][j] for i in range(2)),F(0))*b[j][symbol]
                for j in range(2))
    return sum(v,F(0))


def permute(pi,t,b):
    p=(1,0)
    return tuple(pi[i] for i in p),tuple(tuple(t[i][j] for j in p) for i in p),tuple(b[i] for i in p)


def admissible_assignments(report_a, false_positive_bound, false_negative_bound):
    """Conditional on INDEPENDENT calibration of a report of anchored quality A.

Returns assignments to the original two latent states. Parameters and assignments
must both transport under a pure state renaming; the latent index is not a quale.
"""
    report_a=tuple(map(F,report_a))
    if len(report_a)!=2 or any(not 0<=q<=1 for q in report_a):
        raise ValueError("Two conditional probabilities in [0,1] required")
    a,b=map(F,(false_positive_bound,false_negative_bound))
    if not 0<=a<=1 or not 0<=b<=1:
        raise ValueError('Bounds must lie in [0,1]')
    survivors=[]
    for assignment in (('A','B'),('B','A')):
        if all((q>=1-b if quality=='A' else q<=a)
               for q,quality in zip(report_a,assignment)):
            survivors.append(assignment)
    return survivors


def run():
    validate(PI,T,B)
    swapped=permute(PI,T,B)
    validate(*swapped)
    count=0
    for length in range(1,9):
        total=F(0)
        for sequence in product((0,1),repeat=length):
            p=likelihood(sequence,PI,T,B)
            assert p==likelihood(sequence,*swapped)
            total+=p
            count+=1
        assert total==1
    assert count==510
    # These probabilities and error bounds are supplied examples, NOT measurements.
    report=(F(9,10),F(1,10))
    calibrated=admissible_assignments(report,F(1,5),F(1,5))
    unrestricted=admissible_assignments(report,1,1)
    assert calibrated==[('A','B')]
    assert len(unrestricted)==2
    swapped_survivors=admissible_assignments(tuple(reversed(report)),F(1,5),F(1,5))
    assert swapped_survivors==[('B','A')]
    return {
        'status':'passed',
        'scope':'exact illustrative likelihood and conditional reference constraints',
        'observed_sequences_checked':count,
        'maximum_sequence_length':8,
        'state_renaming_likelihood_invariance':True,
        'analytic_invariance_for_all_lengths':'bijection on hidden paths, proved in report',
        'unrestricted_assignment_count':len(unrestricted),
        'calibrated_example_assignments':calibrated,
        'renamed_calibrated_example_assignments':swapped_survivors,
        'calibration_numbers_are_observed':False,
        'phenomenal_identity_established':False,
        'subject_incidence_established':False,
        'neural_data_analyzed':False,
        'research_suite_count_changed':False,
    }


if __name__=='__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 510 illustrative sequence checks and reference-transport checks; no empirical identity.')
