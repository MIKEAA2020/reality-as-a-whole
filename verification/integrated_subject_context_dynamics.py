#!/usr/bin/env python3
"""Exact finite projected dynamics of E-L; no phenomenal inference."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
from coupled_subject_boundary_gate import STATES, stationary
from integrated_subject_horizon_audit import kernel, mismatch
from integrated_cross_scale_quality import horizon_winners, PAIRS


def q(s, i): return (1-s[i]*s[i+1])//2

def project(s, name):
    if name=='pair_state': return tuple(s[:2])
    if name=='left_q': return (q(s,0),)
    if name=='left_middle_q': return (q(s,0),q(s,1))
    if name=='left_right_q': return (q(s,0),q(s,2))
    if name=='edge_qs': return tuple(q(s,i) for i in range(3))
    raise ValueError(name)

def projected_row(k,s,name):
    r=defaultdict(F)
    for u,p in k[s].items():r[project(u,name)]+=p
    return dict(r)

def tv(a,b):return sum(abs(a.get(x,F(0))-b.get(x,F(0))) for x in set(a)|set(b))/2

def maximal_discrepancy(k,name):
    groups=defaultdict(list)
    for s in STATES:groups[project(s,name)].append(s)
    best=F(-1);witness=None;case_count=0
    for label,states in sorted(groups.items()):
        for a,b in combinations(states,2):
            d=tv(projected_row(k,a,name),projected_row(k,b,name));case_count+=1
            if d>best:best=d;witness=(label,a,b)
    return best,witness,case_count

def ranges(k):
    out={}
    for a in (0,1):
        rows=[]
        for s in STATES:
            if q(s,0)==a:
                p=sum(w for u,w in k[s].items() if q(u,0)!=a)
                rows.append((p,s))
        lo=min(rows);hi=max(rows)
        out[str(a)]={'min':str(lo[0]),'min_state':lo[1],'max':str(hi[0]),'max_state':hi[1],
                     'minimax_absolute_probability_error':str((hi[0]-lo[0])/2)}
    return out

def stationary_stats(t):
    k=kernel(t);d=stationary(t,(None,)*4)
    double=defaultdict(F);triple=defaultdict(F)
    for x,px in d.items():
        for y,p in k[x].items():
            double[q(x,0),q(y,0)]+=px*p
            for z,r in k[y].items():triple[q(x,0),q(y,0),q(z,0)]+=px*p*r
    assert sum(double.values())==sum(triple.values())==1
    for a in (0,1):
        for b in (0,1):assert sum(triple[a,b,c] for c in (0,1))==double[a,b]
    one={str(a):str(double[a,1]/sum(double[a,c] for c in (0,1))) for a in (0,1)}
    history={f'previous={a},current={b}':str(triple[a,b,1]/sum(triple[a,b,c] for c in (0,1))) for a in (0,1) for b in (0,1)}
    return one,history

def run():
    winners,ties=horizon_winners(1);assert winners==PAIRS and not ties
    cases={}
    for t in (F(0),F(1,4)):
        k=kernel(t);rows={}
        for name in ('pair_state','left_q','left_middle_q','left_right_q','edge_qs'):
            d,w,n=maximal_discrepancy(k,name)
            rows[name]={'maximum_tv':str(d),'witness_projection':w[0], 'fine_states':[w[1],w[2]],'fine_state_pairs_checked':n}
        one,hist=stationary_stats(t)
        cases[str(t)]={'projection_tests':rows,'mismatch_switch_probability_ranges':ranges(k),
                       'stationary_next_q1_given_current':one,'stationary_next_q1_given_previous_and_current':hist}
    return {'model':'same four-spin random-site heat-bath dynamics; one-step L selects the pair',
            'cases':cases,'scope':'projected physical model, not a subject or quality test'}

def main():
    text=json.dumps(run(),indent=2)+'\n';Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
