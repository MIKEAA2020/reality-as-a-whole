#!/usr/bin/env python3
"""Exact bounded likelihood/prefix-code controls, not an ontology inference."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def probability(model, policy, observations):
    """Two-stage binary readout: first action, then action conditional on y1."""
    first, if_zero, if_one = policy
    y1, y2 = observations
    a2 = if_one if y1 else if_zero
    def p(y, a):
        q = model[a]
        return q if y else 1 - q
    return p(y1, first) * p(y2, a2)


def posterior(prior, likelihood_a, likelihood_b):
    z = prior*likelihood_a + (1-prior)*likelihood_b
    return prior*likelihood_a/z


def main():
    experiential = (F(1,4), F(3,4))
    neutral = (F(1,4), F(3,4))  # identical operational models by construction
    predictive_rival = (F(1,3), F(2,3))
    policies = list(product(range(2), repeat=3))
    obs = list(product(range(2), repeat=2))
    pairs = 0
    for policy in policies:
        pa = [probability(experiential, policy, y) for y in obs]
        pb = [probability(neutral, policy, y) for y in obs]
        assert sum(pa) == sum(pb) == 1
        for x, y in zip(pa, pb):
            assert x == y and x > 0
            assert posterior(F(2,3), x, y) == F(2,3)
            assert posterior(F(1,3), x, y) == F(1,3)
            pairs += 1
    policy=(0,0,1)
    aa=[probability(experiential,policy,y) for y in obs]
    cc=[probability(predictive_rival,policy,y) for y in obs]
    tv=sum(abs(a-b) for a,b in zip(aa,cc))/2
    assert tv == F(17,144)
    # Prefix-free two-model codebooks; empty code is not used.  Normalizing
    # 2^-length to the two-model class is a chosen subjective prior only.
    def is_prefix_free(codes):
        return all(not b.startswith(a) for i,a in enumerate(codes)
                   for j,b in enumerate(codes) if i != j)
    code1={'A':'0','B':'10'}; code2={'A':'10','B':'0'}
    assert is_prefix_free(list(code1.values())) and is_prefix_free(list(code2.values()))
    def prior_a(codes):
        w=[F(1,2**len(codes[k])) for k in ('A','B')]
        return w[0]/sum(w)
    assert prior_a(code1)==F(2,3) and prior_a(code2)==F(1,3)
    out={'scope':'Constructed operationally identical rivals and toy codebooks; not empirical confirmation, demonstrated metaphysical possibility or a universal complexity result.',
         'policy_count':len(policies),'two_observation_histories_per_policy':len(obs),
         'equal_likelihood_checks':pairs,'posterior_equals_prior_examples':['2/3','1/3'],
         'operationally_different_control':{'policy':list(policy),
              'experiential_distribution':[str(x) for x in aa],
              'different_model_distribution':[str(x) for x in cc],
              'total_variation':str(tv)},
         'prefix_codes':{'favor_A':code1,'favor_B':code2,
                         'normalized_weight_A_in_each':['2/3','1/3']}}
    text=json.dumps(out,indent=2)+'\n'
    (ROOT/'verification/experiential_grounding_rival_gate.json').write_text(text)
    print(text)


if __name__=='__main__': main()
