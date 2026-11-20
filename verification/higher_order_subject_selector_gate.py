#!/usr/bin/env python3
"""Check an output-synergy blind spot in a pairwise subject selector.

Exact finite conditional probabilities; no physical or phenomenological claim.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb, log2
import json
from pathlib import Path

BITS=list(product((0,1),repeat=3))
K=F(1,5)
def parity(v): return sum(v)%2
def kernel(k,x,y): return (1+k*(-1)**(parity(x)^parity(y)))/8

def fixed_marginal(k,x,indices,values):
    return sum((kernel(k,x,y) for y in BITS if tuple(y[i] for i in indices)==values),F(0))

# Every individual and paired output distribution agrees for each fully
# fixed input, hence also for any mixture and any partial input clamp.
for x in BITS:
    for r in (1,2):
        for indices in combinations(range(3),r):
            for values in product((0,1),repeat=r):
                assert fixed_marginal(K,x,indices,values)==fixed_marginal(F(0),x,indices,values)==F(1,2**r)
    assert sum(kernel(K,x,y) for y in BITS)==1
    assert all(kernel(K,x,y)>0 for y in BITS)
    tv=sum(abs(kernel(K,x,y)-kernel(F(0),x,y)) for y in BITS)/2
    assert tv==K/2

# Explicit implementation: two fair seed bits U,V and parity-noise N,
# with P(N=0)=(1+k)/2. The same circuit can be placed inside or
# outside the chosen boundary if it receives x and supplies all outputs.
for x,y in product(BITS,repeat=2):
    p=F(0)
    for u,v,nbit in product((0,1),repeat=3):
        output=(u,v,u^v^parity(x)^nbit)
        noise=(1+K)/2 if nbit==0 else (1-K)/2
        if output==y: p+=noise/4
    assert p==kernel(K,x,y)

# Check 27 partial interventions; un-fixed inputs uniformly randomized. Output
# correlations of any pair remain identical even under simultaneous clamps.
for spec in product((None,0,1),repeat=3):
    inputs=[x for x in BITS if all(a is None or x[i]==a for i,a in enumerate(spec))]
    for r in (1,2):
        for inds in combinations(range(3),r):
            for vals in product((0,1),repeat=r):
                for k in (F(0),K):
                    p=sum((fixed_marginal(k,x,inds,vals) for x in inputs),F(0))/len(inputs)
                    assert p==F(1,2**r)

# Whole-output parity shifts under flipping any one specified input. In each
# case the entire source state is fixed; pair outputs remain uninformative.
for i in range(3):
    for x in BITS:
        flipped=list(x); flipped[i]^=1; flipped=tuple(flipped)
        p=lambda xx:sum((kernel(K,xx,y) for y in BITS if parity(y)==0),F(0))
        assert abs(p(x)-p(flipped))==K

# Relabel both source and target by the bijection (bit0,bit1,parity).
def encode(v): return (v[0],v[1],parity(v))
def decode(z): return (z[0],z[1],z[0]^z[1]^z[2])
assert all(decode(encode(x))==x for x in BITS)
for perm in permutations(range(3)):
    for x,y in product(BITS,repeat=2):
        xp=tuple(x[i] for i in perm); yp=tuple(y[i] for i in perm)
        assert kernel(K,xp,yp)==kernel(K,x,y)
for z,w in product(BITS,repeat=2):
    assert kernel(K,decode(z),decode(w))==(1+K*(-1)**(z[2]^w[2]))/8
# Naively comparing source coordinate to target coordinate in this new
# description yields 1/5 for parity->parity, versus 0 for all raw coordinates.
def effect_in_rep(use_encoding,i,j):
    dist=[]
    for val in (0,1):
        xs=[v for v in BITS if v[i]==val]
        q=F(0)
        for v in xs:
            x=decode(v) if use_encoding else v
            for y in BITS:
                out=encode(y) if use_encoding else y
                if out[j]==1: q+=kernel(K,x,y)/len(xs)
        dist.append(q)
    return abs(dist[1]-dist[0])
assert all(effect_in_rep(False,i,j)==0 for i,j in product(range(3),repeat=2))
assert effect_in_rep(True,2,2)==K
assert all(effect_in_rep(True,i,j)==(K if i==j==2 else 0) for i,j in product(range(3),repeat=2))

# Distinguish specified H0 vs H1 with n independent full-output parity reads.
# Binomial likelihood-ratio test, equal prior, exact Bayes error.
n=100
p0=F(1,2); p1=(1+K)/2
law0=[F(comb(n,j))*p0**j*(1-p0)**(n-j) for j in range(n+1)]
law1=[F(comb(n,j))*p1**j*(1-p1)**(n-j) for j in range(n+1)]
err=sum(min(a,b) for a,b in zip(law0,law1))/2
assert sum(law0)==sum(law1)==1
assert F(0)<err<F(1,2)
# Hoeffding n bound for midpoint κ/2 for R=±1; errors each ≤ .025.
from math import ceil, log, exp
n_bound=ceil(8*log(40)/float(K*K))
assert exp(-n_bound*float(K*K)/8)<=0.025
p=float((1+K)/2); binary_entropy=-p*log2(p)-(1-p)*log2(1-p)
result={'status':'passed','kappa':str(K),'all_pair_marginals_under_27_partial_clamps_identical':True,
        'all_fixed_inputs_have_full_joint_TV':'1/10',
        'any_fixed_input_flip_changes_even_output_probability':'1/5',
        'transition_mutual_information_under_uniform_full_intervention_bits':1-binary_entropy,
        'pairwise_single_output_influence_original_axes':0,
        'parity_coordinate_to_parity_coordinate_influence':'1/5',
        'equal_prior_optimal_full_parity_test_n_100_error':float(err),
        'hoeffding_n_for_each_error_at_most_0_025':n_bound,
        'scope':'two stipulated kernels and allowed interventions; no empirical data, subject-count inference, general IIT calculation, or proof of experiential constitution'}
out=json.dumps(result,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(out)
print(out)
