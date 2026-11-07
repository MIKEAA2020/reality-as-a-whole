#!/usr/bin/env python3
"""Exact illustrative timing distributions; not a patient-data analysis.

Race-model inequality and context-invariance issues are established prior art;
see Gondan & Minakata (2016), doi:10.3758/s13414-015-1018-y. These toy
parameters and the joint-content illustration are project-specific.
"""
from fractions import Fraction as F
from pathlib import Path
import json

FAST, SLOW = 1, 2
SINGLE = {FAST:F(1,4), SLOW:F(3,4)}
# Joint latent finishing times on redundant-target trials.
CONTEXT_INVARIANT_DEPENDENT = {(FAST,SLOW):F(1,4), (SLOW,FAST):F(1,4), (SLOW,SLOW):F(1,2)}
CONTEXT_VARIANT = {(FAST,SLOW):F(2,5), (SLOW,FAST):F(2,5), (SLOW,SLOW):F(1,5)}


def marginal(pair_dist, i):
    return {t:sum(p for pair,p in pair_dist.items() if pair[i]==t) for t in (FAST,SLOW)}


def minimum(pair_dist):
    return {t:sum(p for pair,p in pair_dist.items() if min(pair)==t) for t in (FAST,SLOW)}


def mean(dist):
    return sum(F(t)*p for t,p in dist.items())


def transcript(mode, outcome_dist):
    # Random, independent X/Y attributes do not affect timing in either model.
    # R is the same detection response; no correctness claim about recognition.
    return {(mode,x,y,'press',t):F(1,4)*p
            for x in (0,1) for y in (0,1) for t,p in outcome_dist.items()}


def main():
    assert sum(SINGLE.values())==1
    for dist in (CONTEXT_INVARIANT_DEPENDENT,CONTEXT_VARIANT):
        assert sum(dist.values())==1
    a = minimum(CONTEXT_INVARIANT_DEPENDENT)
    assert marginal(CONTEXT_INVARIANT_DEPENDENT,0)==SINGLE
    assert marginal(CONTEXT_INVARIANT_DEPENDENT,1)==SINGLE
    assert a[FAST] == F(1,2)
    independent_race_fast = 1-(1-F(1,4))**2
    assert independent_race_fast==F(7,16) and a[FAST] > independent_race_fast
    assert a[FAST] <= 2*SINGLE[FAST]  # dependence does not violate Miller's bound
    assert mean(SINGLE)-mean(a)==F(1,4)

    b = minimum(CONTEXT_VARIANT)
    assert marginal(CONTEXT_VARIANT,0)[FAST] == F(2,5)
    assert marginal(CONTEXT_VARIANT,1)[FAST] == F(2,5)
    assert b[FAST]==F(4,5)
    bound = min(F(1),2*SINGLE[FAST])
    assert b[FAST] - bound == F(3,10)
    # Distinct toy pooled mechanism: on bilateral trials both binary channel
    # activations are (1,1) with probability 4/5, otherwise (0,0). A sum
    # threshold of 2 produces fast RT. On single trials the response law is
    # SINGLE. This is not a physiologically validated mechanism.
    pooled_activations = {(1,1):F(4,5), (0,0):F(1,5)}
    pooled_response_law = {t:sum(p for pair,p in pooled_activations.items()
                                 if (FAST if sum(pair)>=2 else SLOW)==t)
                           for t in (FAST,SLOW)}
    assert sum(pooled_activations.values()) == 1
    assert b == pooled_response_law
    for mode, law in [('left',SINGLE),('right',SINGLE),('bilateral',b)]:
        pooled_law = pooled_response_law if mode=='bilateral' else SINGLE
        assert transcript(mode,law)==transcript(mode,pooled_law)
        # Full observed transcript here contains mode, press and time, but not X/Y.
        for t in (FAST,SLOW):
            even=sum(p for (m,x,y,r,t0),p in transcript(mode,law).items() if t0==t and x^y==0)
            odd=sum(p for (m,x,y,r,t0),p in transcript(mode,law).items() if t0==t and x^y==1)
            assert even==odd
    out = {
        'status':'passed',
        'timing_units':'arbitrary',
        'single_fast_probability':str(SINGLE[FAST]),
        'context_invariant_dependent_race_fast_probability':str(a[FAST]),
        'independent_race_fast_probability':str(independent_race_fast),
        'context_invariant_dependent_race_mean_gain':str(mean(SINGLE)-mean(a)),
        'context_variant_channel_fast_marginal':str(marginal(CONTEXT_VARIANT,0)[FAST]),
        'context_variant_redundant_fast_probability':str(b[FAST]),
        'miller_upper_bound_at_fast':str(bound),
        'context_variant_violation_at_fast':str(b[FAST]-bound),
        'context_variant_race_and_pooled_observable_laws_identical':True,
        'toy_attribute_parity_best_accuracy_from_observed_mode_press_time':'1/2',
        'scope':'Fictional discrete-time examples; actual patients, trial data, physiological mechanism, information capacity and phenomenal unity were not tested.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
