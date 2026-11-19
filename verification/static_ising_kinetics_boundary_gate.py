#!/usr/bin/env python3
"""Static Ising data do not determine a stipulated finite-time intervention graph."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

from causal_influence_subject_gate import adjacency, causal_influence, p_plus
from competing_subject_constitution_rules import overlapping_local_maxima, lists
from coupled_subject_boundary_gate import STATES, stationary, flip_probability

ROOT=Path(__file__).resolve().parent.parent
T=F(1,4)
G=adjacency(T)
D={(j,i):causal_influence(i,j,G) for i in range(4) for j in range(4) if i!=j}
PI=stationary(T, (None,)*4)


def kernel(s,rates):
    row={tuple(-x if j==i else x for j,x in enumerate(s)):rates[i]*flip_probability(s,i,T)
         for i in range(4)}
    row[s]=1-sum(row.values())
    assert sum(row.values())==1 and all(x>=0 for x in row.values())
    return row


def fixed_bin_direction(i,j,rates):
    # j is clamped, and target i initially -1. Other neighbours are
    # independently randomized, matching the previous conditional context.
    others=sorted(set(G[i])-{j})
    out=[]
    for sign in (1,-1):
        total=F(0)
        for vals in product((-1,1),repeat=len(others)):
            c=dict(zip(others,vals)) | {j:sign}
            # The target can become + only if the clock chooses site i.
            total+=rates[i]*p_plus(i,c,G)
        out.append(total/F(2**len(others)))
    return out[0]-out[1]


def analyze(rates):
    assert sum(rates)==1 and all(r>0 for r in rates)
    for s in STATES:
        row=kernel(s,rates)
        for u,p in row.items():
            assert PI[s]*p==PI[u]*kernel(u,rates).get(s,F(0))
    for u in STATES:
        assert sum(PI[s]*kernel(s,rates).get(u,F(0)) for s in STATES)==PI[u]
    wd={}
    for i in range(4):
        for j in range(4):
            if i!=j:
                observed=fixed_bin_direction(i,j,rates) if j in G[i] else F(0)
                assert observed==rates[i]*D[(j,i)]
                wd[(j,i)]=observed
    pair={(i,j):min(wd[(i,j)],wd[(j,i)]) for i in range(4) for j in range(i+1,4)}
    winners,ties=overlapping_local_maxima(range(4),pair)
    return {'rates':[str(x) for x in rates],
            'fixed_bin_edges':{f'{i}-{j}':str(w) for (i,j),w in pair.items() if w},
            'L_winners':lists(winners),'unresolved':lists(ties)}

uniform=analyze((F(1,4),)*4)
biased=analyze((F(1,100), F(49,100), F(49,100), F(1,100)))
assert uniform['fixed_bin_edges']=={'0-1':'5/42','1-2':'1/21','2-3':'5/42'}
assert uniform['L_winners']==[[0,1],[2,3]] and not uniform['unresolved']
assert biased['fixed_bin_edges']=={'0-1':'1/200','1-2':'7/75','2-3':'1/200'}
assert biased['L_winners']==[[1,2]] and not biased['unresolved']
assert sum(PI.values())==1

out={'status':'passed','scope':'Two classical finite spin update models sharing exactly the same stationary law. Time-bin selection rule is a new stated convention, not the old target-selected influence or evidence for consciousness.',
     'static_stationary_distribution':'identical full 16-state distribution, including every equal-time marginal and correlation',
     'stationary_distribution_states':len(PI),
     'old_target_selected_influences':'identical in both models because their local conditional update laws are identical',
     'uniform_updates':uniform,'central_updates':biased,
     'fixed_bin_protocol':'clamp j, initialize target i=-1, randomize other i-neighbors uniformly, make one random-site update (clamped site idles), measure target',
     'limitations':'No actual data; different rates are in principle distinguishable using time-resolved observations or interventions; site choice and initial preparation are stipulated; no evidence for any subject-selection law.'}
(ROOT/'verification/static_ising_kinetics_boundary_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
