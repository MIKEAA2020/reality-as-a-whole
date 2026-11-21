#!/usr/bin/env python3
"""Support graphs and strong lumpability in the prior E-L four-spin kernel."""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
from coupled_subject_boundary_gate import STATES
from integrated_subject_horizon_audit import kernel
from integrated_subject_context_dynamics import maximal_discrepancy


def qs(s):return tuple((1-s[i]*s[i+1])//2 for i in range(3))
def outer(s):q=qs(s);return (q[0],q[2])
def any_q(s):return (int(any(qs(s))),)

PROJECTIONS={'fine_spins':lambda s:s, 'all_edges':qs,'outer_edges':outer,'any_mismatch':any_q}


def graph(k,project):
    verts={project(s) for s in STATES};edges=set()
    for s,row in k.items():
        for u,p in row.items():
            if p>0 and project(s)!=project(u):edges.add(frozenset((project(s),project(u))))
    degree=Counter({v:0 for v in verts})
    for edge in edges:
        for v in edge:degree[v]+=1
    return verts,edges,degree


def max_discrepancy(k,project):
    fibers=defaultdict(list)
    for s in STATES:fibers[project(s)].append(s)
    rows={}
    for s in STATES:
        row=defaultdict(F)
        for u,p in k[s].items():row[project(u)]+=p
        rows[s]=row
    best=F(0)
    for group in fibers.values():
        for s,u in combinations(group,2):
            keys=set(rows[s])|set(rows[u])
            d=sum((abs(rows[s][a]-rows[u][a]) for a in keys),F(0))/2
            best=max(best,d)
    return best


def run():
    k=kernel(F(1,4));result={}
    for name,project in PROJECTIONS.items():
        verts,edges,degrees=graph(k,project)
        d=max_discrepancy(k,project)
        result[name]={'vertices':len(verts),'edges':len(edges),'sorted_degrees':sorted(degrees.values()),'max_projected_transition_tv':str(d)}
    assert (result['fine_spins']['vertices'],result['fine_spins']['edges'])==(16,32)
    assert result['fine_spins']['sorted_degrees']==[4]*16
    assert all(sum(a!=b for a,b in zip(*tuple(e)))==1 for e in graph(k,PROJECTIONS['fine_spins'])[1])
    vs,es,degrees=graph(k,qs)
    assert len(vs)==8 and len(es)==16 and all(v==4 for v in degrees.values())
    # The four/four partition by qL XOR qR has every possible cross edge.
    parts=({v for v in vs if v[0]==v[2]},{v for v in vs if v[0]!=v[2]})
    assert len(parts[0])==len(parts[1])==4 and all(frozenset((a,b)) in es for a in parts[0] for b in parts[1])
    assert result['outer_edges']['vertices']==4 and result['outer_edges']['edges']==4
    assert result['outer_edges']['sorted_degrees']==[2]*4
    assert result['any_mismatch']['vertices']==2 and result['any_mismatch']['edges']==1
    assert max_discrepancy(k,qs)==0
    assert max_discrepancy(k,outer)==maximal_discrepancy(k,'left_right_q')[0]==F(2,21)
    for s in STATES:
        r=tuple(reversed(s));a=qs(s);b=qs(r)
        assert b==tuple(reversed(a))
        assert outer(r)==tuple(reversed(outer(s)))
        assert any_q(r)==any_q(s)
    return {'model':'same four-spin t=1/4 one-update heat-bath kernel','graphs':result,
            'strong_lumpability':'zero max TV iff all fine rows in each projected fiber agree on projected next-block probabilities',
            'relabelling_states_checked':len(STATES),
            'scope':'physical support graph only: no phenomenal identification, subject boundary, autonomous dynamics for non-lumpable projections, or physical substrate claim'}


def main():
    text=json.dumps(run(),indent=2)+'\n';Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
