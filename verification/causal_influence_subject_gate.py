#!/usr/bin/env python3
"""Exact intervention and cut-score diagnostic; neither rule is IIT 4.0."""
from fractions import Fraction as F
from itertools import product, combinations, permutations
from math import ceil, log, exp
from pathlib import Path
import json

V = tuple(range(4))
BASE_EDGES = ((0,1),(1,2),(2,3))


def adjacency(t):
    a = {i:{} for i in V}
    for (i,j),k in zip(BASE_EDGES, (F(1,2),t,F(1,2))):
        if k:
            a[i][j]=k
            a[j][i]=k
    return a


def p_plus(i, neighbor_values, graph):
    plus = minus = F(1)
    for j,k in graph[i].items():
        plus *= 1 + k*neighbor_values[j]
        minus *= 1 - k*neighbor_values[j]
    return plus/(plus+minus)


def causal_influence(i,j,graph):
    if j not in graph[i]:
        return F(0)
    others = sorted(set(graph[i])-{j})
    result=F(0)
    for bs in product((-1,1),repeat=len(others)):
        ctx=dict(zip(others,bs))
        # All neighboring inputs besides j are independently randomized.
        result += p_plus(i,ctx | {j:1},graph) - p_plus(i,ctx | {j:-1},graph)
    return result / (2**len(others))


def influence_graph(t):
    graph=adjacency(t)
    directed={(j,i):causal_influence(i,j,graph) for i in V for j in V if i != j}
    pair={(i,j):min(directed[i,j],directed[j,i]) for i,j in combinations(V,2)}
    return directed,pair


def score(subset, pair):
    # Minimum unnormalized symmetric influence across nontrivial cuts.
    subset=frozenset(subset)
    values=[]
    anchor=min(subset)
    rem=sorted(subset-{anchor})
    for bits in product((0,1),repeat=len(rem)):
        side={anchor} | {v for v,b in zip(rem,bits) if b}
        if len(side)==len(subset):
            continue
        values.append(sum((pair[tuple(sorted((i,j)))] for i in side
                           for j in subset-side),F(0)))
    return min(values)


def maximizers(pair):
    sets=[frozenset(s) for n in range(2,5) for s in combinations(V,n)]
    vals={s:score(s,pair) for s in sets}
    mx=max(vals.values())
    return mx, {s for s,v in vals.items() if v==mx and mx>0}


def main():
    cases=[]
    for t in (F(0),F(1,4),F(1,2),F(3,4)):
        d,pair=influence_graph(t)
        mx,sets=maximizers(pair)
        if t==F(1,4):
            assert d[0,1]==d[3,2]==F(10,21)
            assert d[1,0]==d[2,3]==F(1,2)
            assert d[1,2]==d[2,1]==F(4,21)
            assert sets=={frozenset((0,1)),frozenset((2,3))}
        if t==F(3,4):
            assert pair[0,1]==pair[2,3]==F(14,55)
            assert pair[1,2]==F(36,55)
            assert sets=={frozenset((1,2))}
        if t==F(1,2):
            assert len(sets)==6  # all contiguous intervals, length >=2
        # Permutation equivariance for every labeling, including ties.
        for perm in permutations(V):
            perm_pair={tuple(sorted((perm[i],perm[j]))):v for (i,j),v in pair.items()}
            mx2,sets2=maximizers(perm_pair)
            expected={frozenset(perm[i] for i in s) for s in sets}
            assert mx2==mx and sets2==expected
        cases.append({'cross_tanh':str(t),
                      'directed_influences':{f'{j}->{i}':str(d[j,i]) for j,i in d if d[j,i]},
                      'symmetric_edge_weights':{f'{i}-{j}':str(pair[i,j]) for i,j in BASE_EDGES},
                      'maximum_cut_score':str(mx),
                      'maximizing_subsets':[sorted(x) for x in sorted(sets,key=lambda z:(len(z),sorted(z)))]})
    # 12 cells = two randomized input conditions per six directions.
    # Each mean error <= 1/28 => each difference error <= 1/14.
    m=ceil(392*log(480))
    failure_bound=24*exp(-2*m/(28**2))
    assert m==2421 and failure_bound<.05
    # Hypothetical (not observed) paired report/experience error bounds.
    a,b,r_one,r_two=F(4,5),F(1,5),F(1,10),F(1,10)
    report_lower,report_upper=a-r_one,b+r_two
    assert report_lower==F(7,10) and report_upper==F(3,10)
    assert report_lower>report_upper
    n=ceil(log(40)/(2*.2**2))
    assert n==47 and exp(-2*n*.2**2)<.025
    result={'status':'passed', 'cases':cases,
            'relabelings_checked_per_case':24,
            'weak_regime_internal_minus_cross_influence':str(F(2,7)),
            'calibration_bound':{'independent_trials_per_direction_input_cell':m,
                                 'number_of_cells':12,
                                 'simultaneous_error_bound':failure_bound,
                                 'mean_tolerance':'1/28',
                                 'influence_tolerance':'1/14'},
            'hypothetical_phenomenal_bridge': {
                'one_subject_experience_minimum': str(a),
                'two_subject_experience_maximum': str(b),
                'report_error_bounds': [str(r_one),str(r_two)],
                'operational_probability_lower_and_upper': [str(report_lower),str(report_upper)],
                'independent_trials': n,
                'each_hoeffding_error_bound': exp(-2*n*.2**2)},
            'scope':'Toy one-update interventional probabilities and an invented unnormalized cut score. No brain, real subject, conscious quality, measure, metaphysical necessity or IIT 4.0 value is derived. Causal sufficiency and fully controllable spin-neighbor clamps are assumed.'}
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
