#!/usr/bin/env python3
"""Toy conditional influence certificate; NOT a brain or experience assay."""
from fractions import Fraction as F
from math import atanh, ceil, exp, log, tanh
from itertools import product
from pathlib import Path
import json

from causal_influence_subject_gate import influence_graph

ROOT = Path(__file__).resolve().parent.parent

def logit(x):
    assert 0 < x < 1
    return log(x / (1-x))

def response(x, j):
    return 1/(1+exp(-2*(x+j)))

# Pointwise slope bound, including mixed sign local contexts; the analytical
# identity establishes it for all x, not this grid alone.
checks = 0
for x in [-8, -2, -.5, 0, .5, 2, 8]:
    for j in [0, .01, .1, .5, 1, 2]:
        diff = response(x,j)-response(x,-j)
        assert diff <= tanh(j)+1e-12 and diff >= 0
        checks += 1

# Existing four-spin chain, fully specified contexts (target pair {0,1}).
directed, weights = influence_graph(F(1,4))
assert directed[(1,0)] == F(1,2) and directed[(0,1)] == F(10,21)
assert weights[(0,1)] == F(10,21) and weights[(1,2)] == F(4,21)
# target 0 external all+/all- unchanged with spin 1 held +;
# target 1 external spin 2 +/- with spin 0 held +.
external = [(F(3,4), F(3,4)), (F(5,6), F(9,14))]
core = [(F(3,4), F(1,4)), (F(31,42), F(11,42))]
assert core[0][0]-core[0][1] == F(1,2)
assert core[1][0]-core[1][1] == F(10,21)
B = sum(logit(float(pplus))-logit(float(pminus)) for pplus,pminus in external)/4
assert abs(B-atanh(.25)) < 1e-12
assert F(4,21) < B < float(F(10,21))

# Hypothetical displayed sample means, 1% simultaneous cell precision.
e = F(1,100)
Bu = sum(logit(float(pp+e))-logit(float(pm-e)) for pp,pm in external)/4
w_lower = min(pp-pm-2*e for pp,pm in core)
assert w_lower == F(479,1050) and Bu < float(w_lower)
cells=8
alpha=.05
n=ceil(log(2*cells/alpha)/(2*float(e)**2))
failure=2*cells*exp(-2*n*float(e)**2)
assert failure <= alpha and 2*cells*exp(-2*(n-1)*float(e)**2) > alpha

# Hidden collective effect: no deviation for baseline or single flips,
# yet different target law for the all-flipped context.
for m in (2,3,4,8):
    tested=[(1,)*m]+[tuple(-1 if j==i else 1 for j in range(m)) for i in range(m)]
    f0=lambda state:0
    f1=lambda state:int(all(s==-1 for s in state))
    assert all(f0(s)==f1(s) for s in tested)
    assert f0((-1,)*m)==0 and f1((-1,)*m)==1

out={
 'status':'passed',
 'scope':'Finite classical heat-bath model and hypothetical intervention data only; no human data, QFT, consciousness assay, or claim of accessible unknown interventions.',
 'heat_bath_pointwise_grid_checks':checks,
 'reference_chain':{'pair_weight':str(weights[(0,1)]), 'external_graph_weight':str(weights[(1,2)]),
                    'model_aggregate_upper_bound':B, 'exact_bound_expression':'atanh(1/4)',
                    'external_cell_means':[[str(a),str(b)] for a,b in external],
                    'internal_cell_means':[[str(a),str(b)] for a,b in core]},
 'illustrative_confidence_calculation':{
     'cell_count':cells,'assumed_observed_mean_tolerance':str(e),
     'simultaneous_failure_probability_bound':failure,'iid_trials_per_cell':n,
     'total_iid_trials':n*cells,'external_bound_upper':Bu,
     'internal_weight_lower':str(w_lower),'gap':float(w_lower)-Bu,
     'assumptions':'Finite pairwise additive ferromagnetic heat-bath law; all outside inputs controllable; stable correctly clamped core and backgrounds; independent within-cell Bernoulli observations; no systematic bias; hypothetical displayed sample means.'},
 'hidden_collective_counterexample':{'outside_counts_checked':[2,3,4,8],
     'observable_tested_contexts':'baseline and individual flips only',
     'counterexample':'two mechanisms agree on all tested contexts, disagree on all flipped context'},
}
(ROOT/'verification/collective_context_leakage_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
