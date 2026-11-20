#!/usr/bin/env python3
"""Finite exact checks for a history-weighting counterexample.

The convergence and mutual-singularity arguments are analytical, not
verified by finite computation. This is not an experiment or subject assay.
"""
from fractions import Fraction as F
from math import comb, ceil, exp, log
from pathlib import Path
import json

half=F(1,2)
p_high=F(3,4)
p_low=F(1,4)
def word_q(n,k):
    return half*(p_high**k*(1-p_high)**(n-k) + p_low**k*(1-p_low)**(n-k))
def base(n): return half**n
def density(n,k): return word_q(n,k)/base(n)

checks=0
for n in range(0,31):
    assert sum((comb(n,k)*word_q(n,k) for k in range(n+1)),F(0))==1
    assert sum((comb(n,k)*base(n)*density(n,k) for k in range(n+1)),F(0))==1
    for k in range(n+1):
        assert word_q(n,k)==word_q(n+1,k)+word_q(n+1,k+1)
        assert density(n,k)==half*(density(n+1,k)+density(n+1,k+1))
        assert word_q(n,k)>0
        checks+=1
    second=sum((comb(n,k)*base(n)*density(n,k)**2 for k in range(n+1)),F(0))
    assert second==half*(F(5,4)**n+F(3,4)**n)

assert word_q(1,1)==half
assert word_q(2,2)==F(5,16)
assert word_q(2,1)==F(3,16)
assert 2*word_q(2,2)==F(5,8)
assert word_q(2,2)/word_q(1,1)==F(5,8)

# A bounded global density can reproduce the first two-bit table while
# leaving every subsequent bit fair and independent of that first pair.
eta=F(1,4)
def bounded_weight(bits):
    return 1+eta*(2*bits[0]-1)*(2*bits[1]-1)
for a in (0,1):
    for b in (0,1):
        assert base(2)*bounded_weight((a,b))==word_q(2,a+b)
assert sum((base(2)*bounded_weight((a,b)) for a in (0,1) for b in (0,1)),F(0))==1
assert {bounded_weight((a,b)) for a in (0,1) for b in (0,1)}=={F(3,4),F(5,4)}
assert sum((base(4)*bounded_weight((a,b)) for a in (0,1) for b in (0,1) for c in (0,1) for d in (0,1) if c==d),F(0))==half

# Agreement indicators of disjoint two-trial blocks are iid under either
# latent component since both components give the same agreement rate.
for m in range(1,9):
    for k in range(m+1):
        a=F(5,8)**k*F(3,8)**(m-k)
        plus=(p_high**2+(1-p_high)**2)**k*(2*p_high*(1-p_high))**(m-k)
        minus=(p_low**2+(1-p_low)**2)**k*(2*p_low*(1-p_low))**(m-k)
        assert half*(plus+minus)==a

delta=F(1,8)
n=ceil(2*log(40)/float(delta)**2)
assert n==473 and exp(-n*float(delta)**2/2)<0.025

def frac(f): return str(f)
out={
  'status':'passed',
  'finite_horizons_checked_inclusive':[0,30],
  'prefix_count_checks':checks,
  'single_outcome_probability_under_each_law':'1/2',
  'q_conditional_next_one_given_one':'5/8',
  'p_vs_q_pair_agreement':['1/2','5/8'],
  'bounded_global_density_first_pair_agreement':'5/8',
  'bounded_global_density_second_pair_agreement':'1/2',
  'bounded_density_range':['3/4','5/4'],
  'likelihood_ratio_second_moment_n_10':frac(half*(F(5,4)**10+F(3,4)**10)),
  'pair_test_hoeffding_pairs':n,
  'pair_test_individual_trials':2*n,
  'scope':'finite rational prefix, consistency, martingale and block checks; infinite limits proved analytically, no empirical or experiential claims'
}
text=json.dumps(out,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(text)
print(text)
