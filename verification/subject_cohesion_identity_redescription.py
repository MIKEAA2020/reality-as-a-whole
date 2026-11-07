#!/usr/bin/env python3
"""Identity, tie and encoded-intervention gates. No subjects are derived."""
from fractions import Fraction as F
from itertools import combinations, product
from math import log, sqrt
from pathlib import Path
import json

from causal_influence_subject_gate import causal_influence, influence_graph, maximizers, score
from coupled_subject_boundary_gate import stationary, STATES


def max_cardinality_maximizers(t):
    _,pair=influence_graph(t)
    mx,sets=maximizers(pair)
    largest=max(map(len,sets))
    return mx, {s for s in sets if len(s)==largest}


def main():
    eps=F(1,1024)
    cases=[]
    for t in (F(1,2)-eps,F(1,2),F(1,2)+eps):
        mx,selected=max_cardinality_maximizers(t)
        cases.append({'t':str(t), 'score':str(mx),
                      'selected':[sorted(s) for s in sorted(selected,key=lambda x:(len(x),sorted(x)))]})
    assert cases[0]['selected']==[[0,1],[2,3]]
    assert cases[1]['selected']==[[0,1,2,3]]
    assert cases[2]['selected']==[[1,2]]
    d0=stationary(F(1,2)-eps,(None,)*4)
    d1=stationary(F(1,2)+eps,(None,)*4)
    tv=sum(abs(d0[s]-d1[s]) for s in STATES)/2
    assert tv==eps
    # Bernoulli distribution for the middle edge product has parameter (1+t)/2.
    tm,tp=float(F(1,2)-eps),float(F(1,2)+eps)
    p,q=(1+tm)/2,(1+tp)/2
    kl=p*log(p/q)+(1-p)*log((1-p)/(1-q))
    n=100
    error_bound=max(0,(1-sqrt(n*kl/2))/2)
    assert error_bound>.49

    # A three-vertex path with equal 2/5 weights and size-normalized
    # minimum-cut scores has exactly two overlapping symmetry-related maxima.
    pairs={(0,1):F(2,5),(1,2):F(2,5),(0,2):F(0)}
    three={0:{1:F(1,2)}, 1:{0:F(1,2),2:F(1,2)}, 2:{1:F(1,2)}}
    for i,j in ((0,1),(1,2)):
        assert min(causal_influence(i,j,three),causal_influence(j,i,three))==pairs[i,j]
    ss=[frozenset(x) for n0 in (2,3) for x in combinations(range(3),n0)]
    vals={s:score(s,pairs)/len(s) for s in ss}
    best=max(vals.values())
    tops={s for s in ss if vals[s]==best}
    assert tops=={frozenset((0,1)),frozenset((1,2))}
    subsets=[frozenset(x) for n0 in range(3) for x in combinations(sorted(tops,key=lambda z:sorted(z)),n0)]
    reflect=lambda s:frozenset(2-i for i in s)
    def invariant(choice):
        return {reflect(s) for s in choice}==set(choice)
    def disjoint(choice):
        return all(a.isdisjoint(b) for a,b in combinations(choice,2))
    viable=[choice for choice in subsets if choice and invariant(choice) and disjoint(choice)]
    assert viable==[]
    full=frozenset((0,1,2))
    assert vals[full]==F(2,15) and best==F(1,5)

    # Two prior subjects A,B and one subsequent U: exact persistence as a
    # partial one-to-one relation. Left-right symmetry swaps A and B.
    links=[frozenset(),frozenset(('A',)),frozenset(('B',))]
    swap=lambda rel:frozenset({'A':'B','B':'A'}[x] for x in rel)
    symmetric=[x for x in links if swap(x)==x]
    assert symmetric==[frozenset()]

    # Duplicated-coordinate representation. Ordinary and simultaneous clamp
    # actions stay on diagonal. Independent coordinate clamp exits it.
    diagonal={(0,0),(1,1)}
    def model(state,off):
        return state if state in diagonal else (off,off)
    for s in diagonal:
        assert model(s,0)==model(s,1)==s
    for x in (0,1):
        s=(x,x) # admissible simultaneous encoding of do(X=x)
        assert model(s,0)==model(s,1)==s
    independently_clamped=(1,0) # x=(0,0), set coordinate 0 alone to 1
    assert independently_clamped not in diagonal
    assert model(independently_clamped,0)==(0,0)
    assert model(independently_clamped,1)==(1,1)

    result={'status':'passed','four_spin_max_cardinality_rule':cases,
            'endpoint_snapshot_tv':str(tv),
            'iid_full_snapshot_count':n,'one_sample_kl_nats':kl,
            'equal_prior_pinsker_error_lower_bound':error_bound,
            'three_spin_normalized_cut_maxima':[sorted(s) for s in sorted(tops,key=lambda s:sorted(s))],
            'three_spin_max_score':str(best),'unique_lower_full_score':str(vals[full]),
            'nonempty_reflection_invariant_disjoint_top_selections':len(viable),
            'one_to_one_persistence_matchings':['empty','A-to-U','B-to-U'],
            'reflection_invariant_matchings':['empty'],
            'encoded_valid_states':[list(x) for x in sorted(diagonal)],
            'independent_clamp_state':list(independently_clamped),
            'off_diagonal_outputs':[list(model(independently_clamped,k)) for k in (0,1)],
            'scope':'Finite diagnostic only. Maximal cohesion is not IIT and no real subject, consciousness, physically valid independent clamp, universal uniqueness, full dynamics or metaphysical actuality is established. Identity no-go assumes distinct prior subjects, a single successor, one-to-one strict identity, and exact reflection symmetry.'}
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
