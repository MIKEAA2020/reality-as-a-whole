#!/usr/bin/env python3
"""Exact finite checks of a conditional occurrence-weighting interface.
No physical or phenomenal claims are experimentally tested by this program.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import random

ROOT=Path(__file__).resolve().parent.parent


def occurrence_probability(p,r):
    # p is sector-1 weight, r = eligible-occurrence density(1)/density(0)
    return p*r/(1-p+p*r)


def ratio_from_probability(p,y):
    return y*(1-p)/(p*(1-y))


def main():
    # Sector zero has one eligible center, sector one has three.
    p=F(1,4); r=F(3)
    raw0=(1-p)*1;raw1=p*3
    occurrence=raw1/(raw0+raw1)
    within_sector=p
    assert occurrence==F(1,2) and within_sector==F(1,4)
    # A three-outcome diagonal POVM on two sectors; postselect 0 or 1.
    e0=(F(1,3),F(0));e1=(F(0),F(1));efail=(F(2,3),F(0))
    assert all(e0[i]+e1[i]+efail[i]==1 for i in (0,1))
    assert all(0<=v<=1 for op in (e0,e1,efail) for v in op)
    expect=lambda effect: (1-p)*effect[0]+p*effect[1]
    assert expect(e1)/(expect(e0)+expect(e1))==occurrence
    assert expect(efail)==F(1,2)
    # The conditional rule is non-affine, so no fixed POVM outcome can
    # represent it for every mixed state without conditioning.
    assert occurrence_probability(F(0),r)==0
    assert occurrence_probability(F(1),r)==1
    assert occurrence_probability(F(1,4),r)==F(1,2)!=F(1,4)

    # Refinement preserving total mass: split each cell, not duplicate it.
    original=[F(2,9),F(7,9)]
    split0=[original[0]*F(1,5),original[0]*F(4,5)]
    assert sum(split0)==original[0]
    refined=sum(split0)/(sum(split0)+original[1]);assert refined==original[0]
    duplicated=2*original[0]/(2*original[0]+original[1]);assert duplicated!=refined

    # Fully rational synthetic calibration example (outcome 0 has p0=3/4).
    # If P0 in [37/50,19/25], invert decreasing function wrt r.
    p0=F(3,4); yl=F(37,50); yu=F(19,25)
    ratio_bounds=(p0*(1-yu)/(yu*(1-p0)),p0*(1-yl)/(yl*(1-p0)))
    assert ratio_bounds==(F(18,19),F(39,37))
    assert p0/(p0+(1-p0)*ratio_bounds[0])==yu
    assert p0/(p0+(1-p0)*ratio_bounds[1])==yl

    rng=random.Random(8062026);count=10000
    for _ in range(count):
        base=F(rng.randrange(1,100),100)
        a=F(rng.randrange(1,101),rng.randrange(1,101))
        b=F(rng.randrange(1,101),rng.randrange(1,101))
        lo,hi=sorted((a,b))
        v=lo+(hi-lo)*F(rng.randrange(101),100)
        low=occurrence_probability(base,lo); high=occurrence_probability(base,hi)
        actual=occurrence_probability(base,v)
        assert low<=actual<=high
        assert ratio_from_probability(base,actual)==v
        assert (actual==base)==(v==1)
    # For k outcomes the identity result is equivalent to constant strictly
    # positive densities when all baseline weights are positive.
    choices=(F(1,4),F(1,2),F(1),F(2),F(4)); mult_cases=0
    for a in choices:
        for b in choices:
            for c in choices:
                w=(F(1,5),F(3,10),F(1,2));d=(a,b,c)
                z=sum(x*y for x,y in zip(w,d))
                result=tuple(x*y/z for x,y in zip(w,d))
                assert (result==w)==(a==b==c)
                mult_cases+=1
    output={'status':'completed',
       'scope':'conditional finite occurrence-weight model only; no physical evidence for duplicate observers, weighting, or phenomenal constitution',
       'sector1_base_weight':str(p),'sector1_occurrence_density_ratio':str(r),
       'occurrence_normalized_sector1_weight':str(occurrence),
       'sector_normalized_sector1_weight':str(within_sector),
       'postselected_povm_failure_weight':str(expect(efail)),
       'non_affinity_witness':{'input_p':'1/4','postselected_p':'1/2','endpoint_values':['0','1']},
       'refinement_preserving_mass':str(refined),'naive_duplicate_weight':str(duplicated),
       'hypothetical_calibration':{'sector0_base':'3/4','sector0_observed_interval':['37/50','19/25'],
                                   'sector1_to_sector0_density_interval':[str(x) for x in ratio_bounds]},
       'random_rational_bound_and_inversion_checks':count,'multi_outcome_density_checks':mult_cases,
       'seed':8062026}
    (ROOT/'verification/subject_measure_selection_gate.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
