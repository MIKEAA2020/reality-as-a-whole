#!/usr/bin/env python3
"""One-sided witness arithmetic; no empirical calibration or subjects are supplied."""
from fractions import Fraction as F
import json
import math


def lower_witness_prevalence(report_rate, false_positive_bound):
    q, a = F(report_rate), F(false_positive_bound)
    if not (0 <= q <= 1 and 0 <= a < 1):
        raise ValueError('probabilities out of range')
    return max(F(0), (q-a)/(1-a))


def arbitrary_dependence_tail(n, k, alpha):
    """Sharp P(K >= k) bound with marginal positive probability <= alpha."""
    alpha = F(alpha)
    if not (isinstance(n, int) and isinstance(k, int) and 1 <= k <= n and 0 <= alpha <= 1):
        raise ValueError('invalid threshold or probability')
    return min(F(1), n*alpha/k)


def independent_tail(n, k, alpha):
    a = F(alpha)
    if not (isinstance(n, int) and isinstance(k, int) and 1 <= k <= n and 0 <= a <= 1):
        raise ValueError('invalid threshold or probability')
    return sum(F(math.comb(n, j))*a**j*(1-a)**(n-j) for j in range(k,n+1))


def encode(x):
    return {'fraction': str(x), 'decimal': float(x)}


def main():
    q, a = F(7,10), F(1,10)
    p = lower_witness_prevalence(q,a)
    n,k = 30,16
    block = arbitrary_dependence_tail(n,k,a)
    print(json.dumps({'scope':'Invented one-sided calibration and report rates; no observations or validated assay.',
      'population_example': {'positive_rate': encode(q), 'false_positive_upper_bound': encode(a),
          'sharp_lower_bound_reporter_experience': encode(p),
          'attaining_example': {'reporter_target_probability':encode(p), 'sensitivity':encode(F(1)),
                                'false_positive_rate':encode(a), 'resulting_positive_rate':encode(p+(1-p)*a)}},
      'sampling_example': {'n':n, 'threshold':k, 'per_trial_false_positive_bound':encode(a),
          'arbitrary_dependence_sharp_tail_bound':encode(block),
          'independence_or_conditional_risk_control_tail_bound':encode(independent_tail(n,k,a)),
          'dependence_attainment': 'With probability 3/16, choose 16 of 30 trials uniformly to be positive; otherwise none. Each trial is positive with probability 1/10.',
          'max_alpha_for_5_percent_arbitrary_dependence_bound':encode(F(1,20)*k/n)}}, indent=2))

if __name__=='__main__': main()
