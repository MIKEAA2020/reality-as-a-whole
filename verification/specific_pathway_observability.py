"""Finite controls for a fixed-decoder preservation bound; synthetic data only."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def tv(p,q):
    return sum(abs(x-y) for x,y in zip(p,q))/2


def accuracy(p0,p1,decoder):
    # Uniform class priors; p0/p1 are output distributions.
    return sum((p0[i] if not decoder[i] else p1[i]) for i in range(len(p0)))/2


def main():
    probabilities=[(F(i,4),1-F(i,4)) for i in range(5)]
    decoders=list(product((0,1),repeat=2))
    checks=0
    for p00,p01,p10,p11 in product(probabilities, repeat=4):
        d0,d1=tv(p00,p10),tv(p01,p11)
        for dec in decoders:
            a0=accuracy(p00,p01,dec);a1=accuracy(p10,p11,dec)
            assert abs(a1-a0)<=(d0+d1)/2
            assert abs(2*a0-1)<=tv(p00,p01)
            assert abs(2*a1-1)<=tv(p10,p11)
            checks+=1
    # Same feature distributions, different classifiers: x plus an independent
    # uniform 100-valued nuisance. Deterministic decoders choose a different
    # number of nuisance values on which to flip x. This is not the real study.
    a0=F(63,100);a1=F(59,100)
    for x in (0,1):
        assert sum((x if r<63 else 1-x)==x for r in range(100))==63
        assert sum((x if r<59 else 1-x)==x for r in range(100))==59
    # Same fixed decoder/accuracy but condition is encoded in unobserved
    # feature: distributions disjoint despite both accuracies being one.
    # Feature pairs (x,z) ordered as 00,01,10,11.
    dec=(0,0,1,1)
    p00=(F(1),F(0),F(0),F(0)); p01=(F(0),F(0),F(1),F(0))
    p10=(F(0),F(1),F(0),F(0)); p11=(F(0),F(0),F(0),F(1))
    assert accuracy(p00,p01,dec)==accuracy(p10,p11,dec)==1
    assert tv(p00,p10)==tv(p01,p11)==1
    # Decoder witness: at accuracy 3/5 and balanced labels, d>=1/5.
    a=F(3,5); bound=2*a-1
    assert bound==F(1,5)
    result={'status':'passed','exact_finite_cases':checks,
            'same_feature_different_decoders':{'first_accuracy':str(a0),'second_accuracy':str(a1),'true_conditional_tv':'0'},
            'same_fixed_decoder_accuracy_different_features':{'both_accuracies':'1','each_conditional_tv':'1'},
            'synthetic_decoder_witness':{'accuracy':str(a),'consumer_statistical_tv_lower_bound':str(bound)},
            'scope':'ideal balanced binary-label probability distributions; no real-data reanalysis or causal-channel identification'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
