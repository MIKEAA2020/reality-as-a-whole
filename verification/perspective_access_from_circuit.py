"""Causal access in one toy process; no claim about phenomenal subjecthood.

A and B are physical record locations, not stipulated experiencing subjects.
Exact rational arithmetic, except a displayed binary entropy in bits.
"""
from fractions import Fraction
from itertools import product
from math import log2
from pathlib import Path
import json


def dist(q, fix_x=None, fix_y=None):
    result={}
    for x,y,n in product((0,1),repeat=3):
        if fix_x is not None and x!=fix_x: continue
        if fix_y is not None and y!=fix_y: continue
        px=Fraction(1,2) if fix_x is None else Fraction(1)
        py=Fraction(1,2) if fix_y is None else Fraction(1)
        pn=q if n else 1-q
        if pn:
            result[(x,y,n)]=px*py*pn
    assert sum(result.values())==1
    return result


def view(h, scope):
    x,y,n=h
    if scope=='A': return (x,)
    if scope=='B': return (y,x^n)
    if scope=='G': return (x,y,n)
    if scope=='AB': return (x,y,x^n)
    raise ValueError(scope)


def support_class(states, h, scope):
    return [j for j in states if view(j,scope)==view(h,scope)]


def knows(states, h, scope, p):
    return all(p(j) for j in support_class(states,h,scope))


def marginal(d, f):
    out={}
    for h,p in d.items():out[f(h)]=out.get(f(h),Fraction(0))+p
    return out


def tv(p,r):
    return sum(abs(p.get(k,0)-r.get(k,0)) for k in p.keys()|r.keys())/2


def audit(q):
    states=dist(q)
    h=(1,0,0)
    assert h in states
    x_is_one=lambda a:a[0]==1
    y_is_zero=lambda a:a[1]==0
    assert knows(states,h,'G',x_is_one) and knows(states,h,'G',y_is_zero)
    assert knows(states,h,'A',x_is_one) and not knows(states,h,'A',y_is_zero)
    assert knows(states,h,'B',y_is_zero)
    assert knows(states,h,'B',x_is_one)==(q==0)
    assert support_class(states,h,'AB')==support_class(states,h,'G')
    b1=marginal(dist(q,fix_x=1),lambda z:view(z,'B'))
    b0=marginal(dist(q,fix_x=0),lambda z:view(z,'B'))
    a1=marginal(dist(q,fix_y=1),lambda z:view(z,'A'))
    a0=marginal(dist(q,fix_y=0),lambda z:view(z,'A'))
    assert tv(b1,b0)==1-2*q
    assert tv(a1,a0)==0
    correct=sum(p for z,p in states.items() if (z[0]^z[2])==z[0])
    assert correct==1-q
    if q in (0,1): h2=0.
    else:
        t=float(q);h2=-t*log2(t)-(1-t)*log2(1-t)
    return {'noise_q':str(q),'global_support_size':len(states),
            'A_class_size':len(support_class(states,h,'A')),
            'B_class_size':len(support_class(states,h,'B')),
            'joint_record_class_size':len(support_class(states,h,'AB')),
            'B_knows_x_in_this_model':knows(states,h,'B',x_is_one),
            'B_guess_x_from_message_success':str(correct),
            'tv_B_under_do_x':str(tv(b1,b0)), 'tv_A_under_do_y':str(tv(a1,a0)),
            'I_x_message_given_y_bits':1-h2}


def main():
    result={'status':'passed','declared_actual_history':[1,0,0],
            'cases':[audit(Fraction(0)),audit(Fraction(1,10)),audit(Fraction(1,2))],
            'scope':'finite classical stochastic causal model and local-record indistinguishability',
            'limitations':'No phenomenal acquaintance, identity of subject, neuroscience, spacetime emergence, or physical intervention demonstrated.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
