"""Second-order continuum ADM constraints on a flat spatial three-torus.

All polynomial algebra is exact rational arithmetic. The only spatial
variation is z; c=cos(z), s=sin(z), with c²+s²=1. Epsilon is a formal
bookkeeping variable; a and b are the homogeneous momentum and scalar
amplitude. No numerical fitting, continuum limit, exact solution, or quantum
measurement is claimed.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from math import comb
import json

# monomial keys: powers of (epsilon, cos z, sin z, alpha, beta)
Z=(0,0,0,0,0)
def poly(v): return {} if not v else {Z:F(v)}
def variable(i):
    k=list(Z); k[i]=1
    return {tuple(k):F(1)}
def add(*xs):
    y=defaultdict(F)
    for x in xs:
        for k,v in x.items(): y[k]+=v
    return {k:v for k,v in y.items() if v}
def neg(x): return {k:-v for k,v in x.items()}
def scale(x,c): return {k:v*F(c) for k,v in x.items() if v*c}
def mul(x,y):
    out=defaultdict(F)
    for k,v in x.items():
        for l,w in y.items():
            m=tuple(a+b for a,b in zip(k,l))
            if m[0]<=2: out[m]+=v*w
    return {k:v for k,v in out.items() if v}
def dz(x):
    out={}
    for (e,c,s,a,b),v in x.items():
        if c: out=add(out,{(e,c-1,s+1,a,b):-c*v})
        if s: out=add(out,{(e,c+1,s-1,a,b):s*v})
    return out
def deriv(x,i): return dz(x) if i==2 else {}
def reduce_trig(x):
    # Repeatedly replace cos² by 1-sin².
    pending=dict(x); done={}
    while pending:
        k,v=pending.popitem(); e,c,s,a,b=k
        if c>=2:
            for kk,vv in [((e,c-2,s,a,b),v),((e,c-2,s+2,a,b),-v)]:
                pending[kk]=pending.get(kk,F(0))+vv
                if pending[kk]==0: del pending[kk]
        else: done=add(done,{k:v})
    return done
def constraint_sub(x):
    # alpha² = (1+beta²)/6, to test the energy-balance condition.
    pending=dict(x); done={}
    while pending:
        k,v=pending.popitem(); e,c,s,a,b=k
        if a>=2:
            for kk in [(e,c,s,a-2,b),(e,c,s,a-2,b+2)]:
                pending[kk]=pending.get(kk,F(0))+v/6
                if pending[kk]==0: del pending[kk]
        else: done=add(done,{k:v})
    return reduce_trig(done)
def coeff(x,power): return {k:v for k,v in x.items() if k[0]==power}
def pretty(x):
    names=('eps','cos','sin','alpha','beta')
    return ' + '.join(f'{v}*'+ '*'.join(f'{names[i]}^{p}' for i,p in enumerate(k) if p) for k,v in sorted(x.items())) or '0'

one=poly(1); zero={}; eps,c,s,a,b=[variable(i) for i in range(5)]
# g=I + eps h_TT + eps² u I, u=(7-beta²) cos(2z)/32.
cos2=add(mul(c,c),neg(mul(s,s)))
u=scale(mul(add(poly(7),neg(mul(b,b))),cos2),F(1,32))
h=[[zero for _ in range(3)] for _ in range(3)]
h[0][1]=h[1][0]=c
g=[[add(one if i==j else zero,mul(eps,h[i][j]),
         mul(mul(eps,eps),u) if i==j else zero) for j in range(3)] for i in range(3)]
# Neumann inverse of I+eps*h+eps²*u*I.
gi=[[add(one if i==j else zero,neg(mul(eps,h[i][j])),
         mul(mul(eps,eps),add(*[mul(h[i][k],h[k][j]) for k in range(3)],
             neg(u) if i==j else zero)))
     for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        assert not add(*[mul(g[i][k],gi[k][j]) for k in range(3)],neg(one if i==j else zero))

Gamma=[[[scale(add(*[mul(gi[i][l],add(deriv(g[l][k],j),deriv(g[l][j],k),neg(deriv(g[j][k],l)))) for l in range(3)]),F(1,2)) for k in range(3)] for j in range(3)] for i in range(3)]
Ric=[[add(*[add(deriv(Gamma[k][i][j],k),neg(deriv(Gamma[k][i][k],j)),
                *[add(mul(Gamma[k][k][l],Gamma[l][i][j]),neg(mul(Gamma[k][j][l],Gamma[l][i][k]))) for l in range(3)]) for k in range(3)]) for j in range(3)] for i in range(3)]
R=reduce_trig(add(*[mul(gi[i][j],Ric[i][j]) for i in range(3) for j in range(3)]))
assert not coeff(R,0) and not coeff(R,1)
# Independent geometric cross-check: write ds²=A_ab(z)dx^a dx^b+N²dz².
# Flat z=constant 2-tori and zero shift imply R=-2 N^-1 d_z K
# -K^a_b K^b_a-K², where K^a_b=A^ac d_z A_cb/(2N).
invN=add(one,scale(mul(mul(eps,eps),u),F(-1,2)))
K=[[scale(mul(invN,add(*[mul(gi[i][k],dz(g[k][j])) for k in range(2)])),F(1,2))
    for j in range(2)] for i in range(2)]
ktrace=add(K[0][0],K[1][1])
R_by_slicing=add(scale(mul(invN,dz(ktrace)),-2),
                 neg(add(*[mul(K[i][j],K[j][i]) for i in range(2) for j in range(2)])),
                 neg(mul(ktrace,ktrace)))
assert not reduce_trig(add(R,neg(R_by_slicing)))
# At order 2, sqrt(g) and its reciprocal may be replaced by 1: R starts at
# order 2, and the momenta and scalar derivatives are first order.
phi=mul(mul(eps,b),c)
scalar_energy=scale(mul(dz(phi),dz(phi)),F(1,2))
pi=[[mul(eps,a) if i==j else zero for j in range(3)] for i in range(3)]
kinetic=add(*[mul(pi[i][j],pi[i][j]) for i in range(3) for j in range(3)],
            scale(mul(add(*[pi[i][i] for i in range(3)]),add(*[pi[i][i] for i in range(3)])),F(-1,2)))
H=reduce_trig(add(neg(R),kinetic,scalar_energy))
assert not coeff(H,0) and not coeff(H,1)
assert not constraint_sub(H), pretty(constraint_sub(H))
# Momentum density: -2 ∂j(g_ik pi^kj) + pi^jk ∂i g_jk + Pφ ∂iφ;
# scalar Pφ=0. This tests all three components to second order.
D=[]
for i in range(3):
    Di=add(scale(add(*[deriv(mul(g[i][k],pi[k][j]),j) for j in range(3) for k in range(3)]),-2),
           *[mul(pi[j][k],deriv(g[j][k],i)) for j in range(3) for k in range(3)])
    D.append(reduce_trig(Di)); assert not D[-1],pretty(D[-1])
# Independent directly evaluated expected local O(eps²) Hamiltonian.
expected=mul(mul(eps,eps), add(scale(mul(s,s),F(-7,2)),poly(2),
               scale(mul(mul(b,b),mul(s,s)),F(1,2)),scale(mul(a,a),F(-3,2)),
               scale(dz(dz(u)),2)))
assert not reduce_trig(add(H,neg(expected)))
# Exact normalized torus average after c²=1-s². Odd powers vanish;
# <sin^(2m)> = binomial(2m,m)/4^m.
def average_z(x):
    out={}
    for (e,cp,sp,ap,bp),v in reduce_trig(x).items():
        if cp%2 or sp%2: continue
        assert cp==0
        m=sp//2
        out=add(out,{(e,0,0,ap,bp):v*F(comb(2*m,m),4**m)})
    return out
mean=add(poly(F(1,4)),scale(mul(b,b),F(1,4)),scale(mul(a,a),F(-3,2)))
assert not add(average_z(H),neg(mul(mul(eps,eps),mean)))
assert not constraint_sub(mean)
# Constant spatial translation acts by a z-derivative on the linearized
# R_xzyz=epsilon cos(z)/2; it is not an exact local Dirac observable.
r1=scale(mul(eps,c),F(1,2))
translation_variation=dz(r1)
assert not add(translation_variation,scale(mul(eps,s),F(1,2)))
result={'status':'passed','calculation':'Continuum ADM gravity + free massless scalar, periodic 2pi torus; through O(epsilon^2)',
        'ansatz':'h_xy=cos z; pi^ij=epsilon alpha delta^ij; phi=epsilon beta cos z; scalar momentum=0; metric second order u delta^ij with u=(7-beta^2)cos(2z)/32',
        'zero_mode_hamiltonian_obstruction':'1/4 + beta^2/4 - 3 alpha^2/2',
        'condition':'alpha^2=(1+beta^2)/6',
        'pointwise_hamiltonian_constraint_through_order_2':'zero under condition',
        'pointwise_momentum_constraints_through_order_2':'zero',
        'time_symmetric_vacuum_zero_mode': '1/4 (nonzero)',
        'translation_of_linear_curvature': '-epsilon sin(z)/2',
        'limits':'Formal truncated constraint solution; no exact spacetime, physical detector, quantum model or discrete refinement established.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
