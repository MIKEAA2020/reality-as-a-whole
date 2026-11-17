#!/usr/bin/env python3
"""Exact controlled coarse-graining and equilibrium/NESS toy checks.
Uses fractions, stores only aggregate model properties; no human data.
"""
import itertools
import json
import math
import random
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
G=(3,2,1)
PI=tuple(F(g,6) for g in G)
CONTROLS=[(F(1),F(1),F(1)),(F(2),F(1),F(1)),(F(1),F(1,2),F(2))]


def macro_stationary(weights):
    z=sum((F(g)*w for g,w in zip(G,weights)),F())
    return tuple(F(g)*w/z for g,w in zip(G,weights))


def micro_initial(model):
    if model=='A': return {(i,0):PI[i] for i in range(3)}
    return {(i,h):F(1,6) for i,g in enumerate(G) for h in range(g)}


def micro_transition_probability(model,dest,weights):
    i,_=dest
    if model=='A':return macro_stationary(weights)[i]
    den=sum((F(g)*w for g,w in zip(G,weights)),F())
    return weights[i]/den


def visible_path_distribution(model,policy):
    states=list(micro_initial(model))
    dist=defaultdict(F)
    for micro_path in itertools.product(states,repeat=4):
        visible=tuple(x for x,h in micro_path)
        prob=micro_initial(model)[micro_path[0]]
        for t in range(1,4):
            weights=CONTROLS[policy[visible[t-1]]]
            prob*=micro_transition_probability(model,micro_path[t],weights)
        dist[visible]+=prob
    return dict(dist)


def flow_matrix(circulating):
    c=F(1,24); j=F(1,48) if circulating else F(0)
    out=[[F(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        out[i][i]=PI[i]-2*c
        out[i][(i+1)%3]=c+j
        out[i][(i-1)%3]=c-j
    return out


def fstr(x): return str(x)


def main():
    weight_values=(F(1,2),F(1),F(2)); checked=0
    for weights in itertools.product(weight_values,repeat=3):
        macro=macro_stationary(weights)
        assert sum(macro)==1
        A={(i,0):macro[i] for i in range(3)}
        z=sum((F(g)*w for g,w in zip(G,weights)),F())
        B={(i,h):weights[i]/z for i,g in enumerate(G) for h in range(g)}
        assert tuple(sum((B[i,h] for h in range(g)),F()) for i,g in enumerate(G))==macro
        # Reset kernels are both stochastic and satisfy detailed balance
        # for every fixed control. Lumping B recovers A for every origin.
        for model,stationary in (('A',A),('B',B)):
            for origin in stationary:
                transitions={dest:micro_transition_probability(model,dest,weights) for dest in stationary}
                assert sum(transitions.values())==1
                for dest in stationary:
                    assert stationary[origin]*transitions[dest]==stationary[dest]*micro_transition_probability(model,origin,weights)
                for i,g in enumerate(G):
                    lumped=sum((p for (j,h),p in transitions.items() if j==i),F())
                    assert lumped==macro[i]
        checked+=1
    paths_checked=0
    for policy in itertools.product(range(len(CONTROLS)), repeat=3):
        a=visible_path_distribution('A',policy)
        b=visible_path_distribution('B',policy)
        assert a==b and sum(a.values())==1 and len(a)==81
        paths_checked+=len(a)
    eq=flow_matrix(False); neq=flow_matrix(True)
    for flows in (eq,neq):
        assert all(sum(row)==PI[i] for i,row in enumerate(flows))
        assert all(sum(flows[i][j] for i in range(3))==PI[j] for j in range(3))
        assert all(flows[i][j]>0 for i in range(3) for j in range(3))
    assert all(eq[i][j]==eq[j][i] for i in range(3) for j in range(3))
    assert any(neq[i][j]!=neq[j][i] for i in range(3) for j in range(3))
    ep=sum(float(neq[i][j])*math.log(float(neq[i][j]/neq[j][i]))
           for i in range(3) for j in range(3))
    assert abs(ep-math.log(3)/8)<1e-12
    D_a=[math.log(3/g) for g in G]
    D_b=[0.0,0.0,0.0]
    assert abs(D_a[2]-math.log(3))<1e-12
    def interval(lows,highs,index,tlo,thi):
        return (tlo*max(0,math.log(max(lows)/highs[index])),
                thi*math.log(max(highs)/lows[index]))
    p=[float(x) for x in PI]
    lows=[x-.01 for x in p]; highs=[x+.01 for x in p]
    example_bounds=interval(lows,highs,2,1,1)
    assert example_bounds[0] <= D_a[2] <= example_bounds[1]
    rng=random.Random(270319)
    for _ in range(15000):
        raw=[rng.uniform(.01,1) for _ in range(6)]; z=sum(raw)
        probs=[v/z for v in raw]
        lo=[v*rng.uniform(.5,.99) for v in probs]
        hi=[min(1,v*rng.uniform(1.01,1.5)) for v in probs]
        temperature=rng.uniform(.25,4)
        tlo=temperature*rng.uniform(.5,.99)
        thi=temperature*rng.uniform(1.01,1.5)
        i=rng.randrange(len(probs))
        lower,upper=interval(lo,hi,i,tlo,thi)
        actual=temperature*math.log(max(probs)/probs[i])
        assert lower-1e-12<=actual<=upper+1e-12
    result={'status':'completed',
      'scope':'exact finite stationary-and-intervention toy models; not neural data, empirical outcome, or subject/experience inference',
      'temperature_energy_units':1,'macro_probability':[fstr(p) for p in PI],
      'baseline_micro_multiplicities_model_A':[1,1,1],
      'baseline_micro_multiplicities_model_B':list(G),
      'micro_excess_by_macro_model_A':D_a,'micro_excess_by_macro_model_B':D_b,
      'coarse_effective_free_energy_excess':D_a,
      'interval_example':{'each_probability_error':0.01,'index':2,'temperature':1,
                          'lower':example_bounds[0],'upper':example_bounds[1]},
      'random_interval_containment_checks':15000,'random_seed':270319,
      'controls_tested':checked,'adaptive_policies_tested':27,
      'four_visible_state_paths_per_policy':81,'total_adaptive_paths_compared':paths_checked,
      'detailed_balance_at_each_fixed_control':True,'all_checked_paths_equal':True,
      'reversible_stationary_flow':[[fstr(x) for x in row] for row in eq],
      'nonreversible_stationary_flow':[[fstr(x) for x in row] for row in neq],
      'observable_information_entropy_production_nats_per_step':ep,
      'entropy_production_expected_ln3_over_8':math.log(3)/8,
      'limitations':'Same macro kernels are constructed, not inferred empirically; hidden-sensitive probes or independent subjective measurements can distinguish additional claims.'}
    (ROOT/'verification/equilibrium_mismatch_coarse_graining.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
