#!/usr/bin/env python3
"""Finite integrated candidate and neutral rival; no actual subject is claimed."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json

from coupled_subject_boundary_gate import STATES, stationary
from causal_influence_subject_gate import influence_graph
from competing_subject_constitution_rules import overlapping_local_maxima, connected_components, relabel

ROOT=Path(__file__).resolve().parent.parent
ACTIVE=frozenset(range(4))
PAIR_L=frozenset((0,1)); PAIR_R=frozenset((2,3))
PAIRS=(PAIR_L,PAIR_R)

def mismatch(s,i,j,tau=1):
    # tau is the independently specified preferred alignment, not a rating.
    return (1-tau*s[i]*s[j])//2

def joint_mismatch(dist):
    out=defaultdict(F)
    for s,p in dist.items():
        out[(mismatch(s,0,1),mismatch(s,2,3))]+=p
    return dict(out)

def text_dist(dist):
    return {f'{a}{b}':str(dist.get((a,b),F(0))) for a,b in product((0,1),repeat=2)}

base={}; perm_checks=0; gauge_checks=0; joint_checks=0
for t in (F(0),F(1,4),F(1,2)):
    _,edges=influence_graph(t)
    selected,ties=overlapping_local_maxima(ACTIVE,edges)
    c=connected_components(ACTIVE,edges)
    d=stationary(t,(None,)*4)
    joint=joint_mismatch(d)
    assert joint=={(0,0):F(9,16),(0,1):F(3,16),
                   (1,0):F(3,16),(1,1):F(1,16)}
    endpoint=sum(p for s,p in d.items() if s[0]==s[3])
    assert endpoint==(1+t/4)/2
    if t in (F(0),F(1,4)):
        assert selected==frozenset(PAIRS) and not ties
    else:
        assert not selected and len(ties)==6
    if t==0: assert c==frozenset(PAIRS)
    if t==F(1,4): assert c==frozenset((ACTIVE,))
    # Correctly transport the actual spin states, edges, boundary selection,
    # and comparison pairs together through relabelings.
    for perm in permutations(range(4)):
        edges2={tuple(sorted((perm[i],perm[j]))):w for (i,j),w in edges.items()}
        selected2,ties2=overlapping_local_maxima(ACTIVE,edges2)
        assert selected2==relabel(selected,perm) and ties2==relabel(ties,perm)
        assert connected_components(ACTIVE,edges2)==relabel(c,perm)
        for s in STATES:
            s2=[None]*4
            for i in range(4): s2[perm[i]]=s[i]
            assert mismatch(s2,perm[0],perm[1])==mismatch(s,0,1)
            assert mismatch(s2,perm[2],perm[3])==mismatch(s,2,3)
            perm_checks+=1
    # Local spin sign re-encodings are not relabeling a preference as positive:
    # preferred edge signs must transform with the spin representation.
    for g in product((-1,1),repeat=4):
        for s in STATES:
            new=tuple(g[i]*s[i] for i in range(4))
            for i,j in ((0,1),(2,3)):
                assert mismatch(new,i,j,g[i]*g[j])==mismatch(s,i,j)
                gauge_checks+=1
    base[str(t)]={'local_maximum_subject_sets':[sorted(x) for x in sorted(selected,key=lambda v:tuple(sorted(v)))],
                  'local_unresolved_candidates':[sorted(x) for x in sorted(ties,key=lambda v:(len(v),tuple(sorted(v))))],
                  'connected_rule_subject_sets':[sorted(x) for x in sorted(c,key=lambda v:tuple(sorted(v)))],
                  'joint_physical_mismatch_distribution':text_dist(joint),
                  'endpoint_agreement_probability':str(endpoint)}
    # Clamp cases compare two copied kernels, not a newly measured assay.
    # The boundary rule is NOT defined post-clamp; these are physical
    # mismatch observables on the original named pair edges only.
    for clamp in product((None,-1,1),repeat=4):
        d=stationary(t,clamp)
        table_e={(s,mismatch(s,0,1),mismatch(s,2,3)):p for s,p in d.items()}
        table_n={(s,mismatch(s,0,1),mismatch(s,2,3)):p for s,p in d.items()}
        assert table_e==table_n and sum(table_e.values())==1
        joint_checks+=1

# A state mismatch is not the minimum frustration of even the pair's
# isolated cost: either preferred assignment gives zero for each pair.
for s in product((-1,1),repeat=2):
    cost=mismatch(s,0,1)
    mincost=min(mismatch(z,0,1) for z in product((-1,1),repeat=2))
    assert mincost==0 and cost in (0,1)
assert base['0']['joint_physical_mismatch_distribution']==base['1/4']['joint_physical_mismatch_distribution']
assert base['0']['endpoint_agreement_probability']=='1/2'
assert base['1/4']['endpoint_agreement_probability']=='17/32'

out={'status':'completed',
     'scope':'specified finite spin and stipulated experiential labels; no observed subject, validated assay, ontology, physics recovery or ground necessity',
     'formal_settings':base,
     'state_relabeling_checks':perm_checks,'local_sign_encoding_checks':gauge_checks,
     'identical_stipulated_grounding_copies_clamp_kernels':joint_checks,
     'note_on_ties':'when L has unresolved ties, pair mismatch variables remain physical observables, not identified subjects',
     'note_on_clamps':'conditioned equilibrium spin distributions; L after clamping is not defined',
     'pair_isolated_minimum_frustration':0,
     'physical_observable_vs_experience':'same numeric mismatch distribution is not an independent phenomenal assay',
     'grounding_underdetermination':'experiential and neutral versions are given identical physical and stipulated phenomenal kernel by construction; no general impossibility claim'}
path=ROOT/'verification/integrated_experiential_misalignment_candidate.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
