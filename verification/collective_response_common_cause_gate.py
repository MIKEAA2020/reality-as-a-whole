#!/usr/bin/env python3
"""Shared-seed factorization of previous parity channel and mechanistic audit.

Rational finite checks; no assertion about actual consciousness or Bell tests.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import ceil, log, exp
from pathlib import Path
import json

BITS=tuple(product((0,1),repeat=3))
def parity(x): return x[0]^x[1]^x[2]
def central(x,l):
    u,v,n=l
    return (u,v,u^v^parity(x)^n)
def local(x,l):
    u,v,n=l
    return (x[0]^u,x[1]^v,x[2]^u^v^n)
def weight(k,l): return (1+k*(-1)**l[2])/8
def target(k,x,y): return (1+k*(-1)**(parity(x)^parity(y)))/8
def channel(impl,k,x):
    result={y:F(0) for y in BITS}
    for l in BITS: result[impl(x,l)]+=weight(k,l)
    return result

tests=[F(i,5) for i in range(-5,6)]
for k in tests:
    assert sum(weight(k,l) for l in BITS)==1
    assert all(weight(k,l)>=0 for l in BITS)
    for x in BITS:
        C=channel(central,k,x); D=channel(local,k,x)
        assert C==D
        assert all(C[y]==target(k,x,y) for y in BITS)
        # Conditional local outputs respond only to their own setting for any seed.
        for l in BITS:
            for i in range(3):
                for other in BITS:
                    if other[i]==x[i]: assert local(x,l)[i]==local(other,l)[i]

# One explicit fixed-seed contrast. Controls fix the SAME declared seed bits
# for both architectures, and all three input bits, no postselection.
l=(0,0,0); x=(1,0,0)
c=central(x,l); d=local(x,l)
assert c==(0,0,1) and d==(1,0,0)
# Every seed can be set under the candidate ideal source-control mechanism;
# count where architectures disagree, for each fixed input.
disagree={''.join(map(str,x)):sum(central(x,l)!=local(x,l) for l in BITS) for x in BITS}
assert disagree['000']==0
assert disagree['100']==8

# Apply existing toy connected-component rule C to a declared graph whose
# nodes pair input and output locations. Edge i--j means toggling input i can
# change output j at a fixed seed, i != j. Shared seed is explicitly outside
# this three-site graph. This is a stipulation, not actual subject inference.
def influence_graph(impl):
    edges=set()
    for l,x in product(BITS,repeat=2):
        for i in range(3):
            x2=list(x); x2[i]^=1
            for j in range(3):
                if i!=j and impl(x,l)[j]!=impl(tuple(x2),l)[j]:
                    edges.add(tuple(sorted((i,j))))
    return edges

def components(edges):
    remaining=set(range(3)); result=[]
    while remaining:
        comp={remaining.pop()}
        while True:
            extend={v for edge in edges if comp.intersection(edge) for v in edge}-comp
            if not extend: break
            comp.update(extend); remaining.difference_update(extend)
        result.append(tuple(sorted(comp)))
    return sorted(result)

edges_c=influence_graph(central); edges_d=influence_graph(local)
assert edges_c=={(0,2),(1,2)} and edges_d==set()
assert components(edges_c)==[(0,1,2)]
assert components(edges_d)==[(0,),(1,),(2,)]

# Passive site permutations and independent within-site bit-label swaps.
# Inputs, outputs and interventions are transported through the same site map.
from itertools import permutations
transformations=0
for perm,fi,fo in product(permutations(range(3)),BITS,BITS):
    def transported(impl,xx,ll):
        original=[0,0,0]
        for i in range(3): original[perm[i]]=xx[i]^fi[i]
        yy=impl(tuple(original),ll)
        return tuple(yy[perm[i]]^fo[i] for i in range(3))
    for impl,edges in ((central,edges_c),(local,edges_d)):
        expected={tuple(sorted((perm.index(a),perm.index(b)))) for a,b in edges}
        assert influence_graph(lambda xx,ll: transported(impl,xx,ll))==expected
    transformations+=1
assert transformations==384

# Uncontrolled model: no amount of x/y-only adaptivity can distinguish
# independent fresh-seed channels. Check one nontrivial 3-round deterministic
# adaptive policy over all transcripts and separately use the general proof.
k=F(1,5)
def policy(previous):
    if not previous: return (1,0,0)
    prev=previous[-1]
    return (prev[1],prev[2],prev[0]^1)
def transcript_probability(impl, transcript):
    previous=[]; p=F(1)
    for y in transcript:
        x=policy(previous)
        p*=channel(impl,k,x)[y]
        previous.append(y)
    return p
sumC=sumD=F(0)
for transcript in product(BITS,repeat=3):
    a=transcript_probability(central,transcript)
    b=transcript_probability(local,transcript)
    assert a==b
    sumC+=a; sumD+=b
assert sumC==sumD==1

# Hypothetical source-clamp and readout validity bounds, not measurements.
eta=F(1,20); r=F(3,100)
low=1-eta-r; high=eta+r
assert low==F(23,25) and high==F(2,25)
delta=float(low-high)
n=ceil(2*log(40)/(delta*delta))
assert n==11 and exp(-n*delta*delta/2)<.025

out={'status':'passed','tested_kappas':[str(k) for k in tests],
     'full_kernel_equality_for_every_input_and_output':True,
     'local_model_measurement_independent_seed_and_factorized_response':True,
     'site_inputs_accessed_locally_only':True,
     'seed_controlled_central_graph_edges':sorted(edges_c),
     'seed_controlled_distributed_graph_edges':sorted(edges_d),
     'stipulated_connected_component_subject_counts':{'central':1,'distributed':3},
     'site_permutation_and_local_label_swap_checks':transformations,
     'fresh_seed_three_round_adaptive_transcripts_checked':512,
     'fixed_seed_000_input_100':{'central':list(c),'local':list(d)},
     'assumed_validity_failure_bound':str(eta),'assumed_readout_error_bound':str(r),
     'hypothetical_response_ranges':{'central_at_least':str(low),'local_at_most':str(high)},
     'independent_trials_hoeffding_n_for_each_error_le_0_025':n,
     'scope':'finite classical mechanisms, idealized controls; not actual devices or a phenomenal assay'}
text=json.dumps(out,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(text)
print(text)
