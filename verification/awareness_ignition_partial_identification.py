#!/usr/bin/env python3
"""Exact toy calibration bounds; no actual neuroscience data analyzed."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def pdist_coin(p,z): return p if z else 1-p
def accum(rows,variables):
    out={}
    for row,w in rows:
        key=tuple(row[i] for i in variables)
        out[key]=out.get(key,F(0))+w
    return out

# Both uncalibrated models yield exactly the same observed Y,T table.
y=F(1,5); t=F(41,50)
def model(which):
    rows=[]
    for yy,tt,a in product((0,1),repeat=3):
        pa = F(1) if yy else (F(3,4) if which=='usually_aware' else F(0))
        e=yy
        rows.append(((a,e,yy,tt),pdist_coin(y,yy)*pdist_coin(t,tt)*pdist_coin(pa,a)))
    return rows
m1=model('usually_aware'); m2=model('aware_only_with_y')
assert accum(m1,(2,3))==accum(m2,(2,3))
def prob(rows,condition): return sum((w for row,w in rows if condition(*row)),F(0))
for m in (m1,m2): assert prob(m,lambda a,e,y,t:True)==1
pi1=prob(m1,lambda a,e,y,t:a==1)
pi2=prob(m2,lambda a,e,y,t:a==1)
q1=prob(m1,lambda a,e,y,t:a==1 and e==1)/pi1
q2=prob(m2,lambda a,e,y,t:a==1 and e==1)/pi2
assert (pi1,q1,pi2,q2)==(F(4,5),F(1,4),F(1,5),1)

# Exact model saturating the awareness-specificity and neural sensitivity bound.
c=F(19,20); r=F(9,10); pi=(t+c-1)/c
q=y/(pi*r)
rows=[]
for a,e,yy,tt in product((0,1),repeat=4):
    pa=pdist_coin(pi,a)
    pe=pdist_coin(q if a else F(0),e)
    py=pdist_coin(r if a and e else F(0),yy)
    pt=pdist_coin(F(1) if a else 1-c,tt)
    rows.append(((a,e,yy,tt),pa*pe*py*pt))
assert prob(rows,lambda a,e,y,t:True)==1
assert prob(rows,lambda a,e,y,t:y==1)==y
assert prob(rows,lambda a,e,y,t:t==1)==t
assert prob(rows,lambda a,e,y,t:a==1)==pi==F(77,95)
assert q==F(190,693)
assert prob(rows,lambda a,e,y,t:t==0 and a==0)/(1-pi)==c
assert prob(rows,lambda a,e,y,t:y==1 and e==1 and a==1)/prob(rows,lambda a,e,y,t:e==1 and a==1)==r

# Exhaustive rational examples for the claimed necessary inequality, with
# arbitrary positive-readout rates in the three non-critical latent cells.
cases=0
vals=[F(i,4) for i in range(5)]
for pi0, se, sp, q0, sens, u, v in product(vals, repeat=7):
    if pi0==0 or sp==0 or sens==0:continue
    t0=pi0*se+(1-pi0)*(1-sp)
    y0=pi0*(q0*sens+(1-q0)*u)+(1-pi0)*v
    lower=max(F(0),(t0+sp-1)/sp)
    assert pi0>=lower
    assert y0>=pi0*q0*sens
    if lower>0: assert q0<=min(F(1),y0/(lower*sens))
    cases+=1

out={'status':'passed','uncalibrated_same_joint_observed':True,
     'world_1_awareness_and_conditional_event':['4/5','1/4'],
     'world_2_awareness_and_conditional_event':['1/5','1'],
     'illustrative_proxy_positive':'41/50', 'specificity_lower':'19/20',
     'neural_sensitivity_lower':'9/10', 'readout_positive':'1/5',
     'awareness_lower':'77/95','conditional_event_upper':'190/693',
     'bound_is_sharp_for_these_margins':True,'rational_grid_cases':cases,
     'scope':'hypothetical binary model; no observed COGITATE trial rates or calibrated phenomenal assay'}
text=json.dumps(out,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(text)
print(text)
