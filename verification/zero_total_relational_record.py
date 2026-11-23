#!/usr/bin/env python3
"""Exact neutral finite model with invariant relational event and record.

Discrete labelled mathematical example only: no physical energy, fundamental
whole, autonomous detector, probabilities in nature, or experience is derived.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json

B = ((-1,0,1),(1,-1,0),(0,1,-1))
STATES=tuple(sorted(set(permutations((1,-1,0)))))
PERMS=tuple(permutations(range(3)))


def field_charge(field):
    return tuple(sum(B[i][j]*field[j] for j in range(3)) for i in range(3))


def symmetry(q,perm,sign):
    return tuple(sign*q[i] for i in perm)


def negative(q): return tuple(-x for x in q)


def category(q,r):
    if q not in STATES or r not in STATES:
        raise ValueError('states must be in the neutral six-state sector')
    if r==q: return 'stay'
    if r==negative(q): return 'flip'
    if any(q[i]==r[i] and q[i]!=0 for i in range(3)): return 'move'
    return 'both_moved'


def kernel(q,r,weights):
    if len(weights)!=4 or any(x<0 for x in weights) or sum(weights)!=1:
        raise ValueError('weights must be four nonnegative numbers summing to one')
    a,b,c,d=weights
    return {'stay':a,'flip':b,'move':c/2,'both_moved':d/2}[category(q,r)]


def copy_event(q,r,bit):
    if bit not in (0,1): raise ValueError('one bit required')
    return (q,r,bit ^ int(category(q,r)=='flip'))


def run():
    q=STATES[0]
    group=[(p,s) for p in PERMS for s in (-1,1)]
    assert len(STATES)==6 and {symmetry(q,p,s) for p,s in group}==set(STATES)
    # The six charges are precisely +/- the three oriented edge divergences.
    edges=[]
    for j in range(3):
        for sign in (-1,1):
            field=tuple(sign*int(k==j) for k in range(3))
            edges.append(field_charge(field))
    assert set(edges)==set(STATES)
    assert all(sum(x)==0 for x in STATES)
    counts={c:sum(category(q,r)==c for r in STATES)
            for c in ('stay','flip','move','both_moved')}
    assert counts=={'stay':1,'flip':1,'move':2,'both_moved':2}
    params=(F(1,5),F(2,5),F(3,10),F(1,10))
    distributions={}
    for name,w in [('move',(F(0),F(0),F(1),F(0))),
                   ('flip',(F(0),F(1),F(0),F(0))),
                   ('mixture',params)]:
        assert all(sum(kernel(x,y,w) for y in STATES)==1 for x in STATES)
        assert all(kernel(x,y,w)==kernel(y,x,w) for x,y in product(STATES, repeat=2))
        for p,s in group:
            assert all(kernel(x,y,w)==kernel(symmetry(x,p,s),symmetry(y,p,s),w)
                       for x,y in product(STATES,repeat=2))
        for y in STATES:
            assert sum(F(1,6)*kernel(x,y,w) for x in STATES)==F(1,6)
        yes=sum(F(1,6)*kernel(x,y,w)*int(category(x,y)=='flip')
                for x,y in product(STATES, repeat=2))
        distributions[name]={'weights':[str(v) for v in w],
                             'record_one_probability':str(yes)}
    for x,y,bit in product(STATES,STATES,(0,1)):
        out=copy_event(x,y,bit)
        assert copy_event(*out)==(x,y,bit)
        assert sum(out[0])+sum(out[1])==0
        for p,s in group:
            assert category(symmetry(x,p,s),symmetry(y,p,s))==category(x,y)
    # Given only the two move successors, a stabilizing symmetry exchanges
    # them; equal probabilities plus normalization uniquely give 1/2 each.
    move_successors=[r for r in STATES if category(q,r)=='move']
    stabilizer=[(p,s) for p,s in group if symmetry(q,p,s)==q]
    assert any(symmetry(move_successors[0],p,s)==move_successors[1]
               for p,s in stabilizer)
    return {'status':'passed','arithmetic':'exact rational and integer',
        'states':[list(x) for x in STATES], 'total_charge_all_states':0,
        'symmetry_group_order':len(group), 'transition_orbit_sizes':counts,
        'uniform_distribution_each_state':'1/6',
        'invariant_kernel_family':'stay=a, flip=b, each move=c/2, each both_moved=d/2; a+b+c+d=1',
        'two_successor_move_rule_forced_probabilities':['1/2','1/2'],
        'comparison':distributions,
        'record_map_is_involution_on_72_inputs':True,
        'scope':'A finite formal classical model with stipulated sector, law and blank register; not cosmological energy, quantum gravity, experienced time, self-subsistence or subject constitution.'}


if __name__=='__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
