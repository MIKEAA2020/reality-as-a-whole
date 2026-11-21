#!/usr/bin/env python3
"""Conditional scale-complete E-L extension, not an experiential assay."""
import json, math
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
from coupled_subject_boundary_gate import STATES, stationary
from integrated_subject_horizon_audit import kernel, advance, V
from competing_subject_constitution_rules import overlapping_local_maxima

T=F(1,4)
PAIRS={frozenset((0,1)),frozenset((2,3))}
WHOLE={frozenset((0,1,2,3))}
# The undirected edge dictionary transports together with preferred sign and coupling.
EDGES={(0,1):(F(1,2),1),(1,2):(F(1,4),1),(2,3):(F(1,2),1)}

def indicator(s,i,j,tau):return (1-tau*s[i]*s[j])//2

def signature(s, subset, edges):
    """Return exact tuple of coupling, mismatch for internal model edges."""
    return tuple((c,indicator(s,i,j,tau)) for (i,j),(c,tau) in sorted(edges.items()) if i in subset and j in subset)

def quality(sig,mode='graded'):
    if not sig: raise ValueError('no internal physical edges')
    if mode=='binary':return float(any(q for _,q in sig))
    if mode!='graded':raise ValueError('bad mode')
    weights=[math.log((1+float(c))/(1-float(c))) for c,_ in sig]
    return sum(w*q for w,(_,q) in zip(weights,sig))/sum(weights)

def horizon_winners(n):
    k=kernel(T)
    d={(j,a):{s:F(1,8) for s in STATES if s[j]==a} for j in V for a in (-1,1)}
    for _ in range(n):d={key:advance(z,k) for key,z in d.items()}
    def effect(j,i):return sum(p for s,p in d[j,1].items() if s[i]==1)-sum(p for s,p in d[j,-1].items() if s[i]==1)
    weights={(i,j):min(effect(i,j),effect(j,i)) for i in V for j in V if i<j}
    return overlapping_local_maxima(frozenset(V),weights)

def transform(s,edges,subset,perm,sign):
    st=[0]*4
    for i in V:st[perm[i]]=s[i]*sign[i]
    et={}
    for (i,j),(c,tau) in edges.items():
        edge=tuple(sorted((perm[i],perm[j])))
        et[edge]=(c,tau*sign[i]*sign[j])
    return tuple(st),et,frozenset(perm[i] for i in subset)

def run():
    one,one_ties=horizon_winners(1); nine,nine_ties=horizon_winners(9)
    assert one==PAIRS and nine==WHOLE and not one_ties and not nine_ties
    dist=stationary(T,(None,)*4); assert sum(dist.values())==1
    grouped=defaultdict(F); disagreement=F(0); diff_expect=0.; checks=0
    for s in STATES:
        left=indicator(s,0,1,1); mid=indicator(s,1,2,1); right=indicator(s,2,3,1)
        k=left+right;grouped[k,mid]+=dist[s]
        full=signature(s,frozenset(V),EDGES); a=quality(full);b=quality(full,'binary')
        if a!=b: disagreement+=dist[s];diff_expect+=float(dist[s])*(b-a)
        for pair in PAIRS:
            z=signature(s,pair,EDGES)
            assert quality(z)==quality(z,'binary')
        for perm in permutations(V):
            for sign in product((-1,1),repeat=4):
                for sub in one|nine:
                    s2,e2,sub2=transform(s,EDGES,sub,perm,sign)
                    x=signature(s,sub,EDGES);y=signature(s2,sub2,e2)
                    assert sorted(x)==sorted(y)
                    assert abs(quality(x)-quality(y))<1e-12 and quality(x,'binary')==quality(y,'binary')
                    checks+=1
    expected={(0,0):F(45,128),(0,1):F(27,128),(1,0):F(30,128),(1,1):F(18,128),(2,0):F(5,128),(2,1):F(3,128)}
    assert dict(grouped)==expected
    a=math.log(3);b=math.log(F(5,3));total=2*a+b
    contrast=a/total
    return {'scope':'fixed t=1/4 spin sector, two postulated subjective laws; not an empirical or battery pass',
      'horizon_1_L_sets':[sorted(x) for x in sorted(one,key=lambda x:tuple(sorted(x)))],
      'horizon_9_L_sets':[sorted(x) for x in nine],
      'weights':{'outer':'ln(3)','middle':'ln(5/3)','total':'2 ln(3)+ln(5/3)'},
      'quality_distribution':[{'outer_mismatch_count':k,'middle_mismatch':m,'probability':str(grouped[k,m]),'graded':(k*a+m*b)/total,'binary':int(k+m>0)} for k,m in sorted(grouped)],
      'pair_quality_equal_for_all_states':True,'relabeling_and_sign_transport_checks':checks,
      'model_probability_of_law_disagreement':str(disagreement),'mean_binary_minus_graded':diff_expect,
      'conditional_contrast':{'event':'one outer mismatch, middle matched','probability':str(grouped[1,0]),'graded':contrast,'binary':1.,'minimum_gap':1-contrast,'strict_assay_error_threshold':(1-contrast)/2},
      'interpretation':'distribution is a physical equilibrium model; phenomenality and calibrated readout are extra postulates'}

def main():
    r=run();text=json.dumps(r,indent=2,allow_nan=False)+'\n';Path(__file__).with_suffix('.json').write_text(text); print(text)
if __name__=='__main__':main()
