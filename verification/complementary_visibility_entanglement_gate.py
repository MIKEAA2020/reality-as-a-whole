#!/usr/bin/env python3
"""Exact two-qubit identification checks; known witnesses, not experimental data."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

zero=F(0)
one=F(1)
I=[[one,zero],[zero,one]]
X=[[zero,one],[one,zero]]
Z=[[one,zero],[zero,-one]]
# Y⊗Y is real: avoid complex or inexact arithmetic.
YY=[[zero,zero,zero,-one], [zero,zero,one,zero],
    [zero,one,zero,zero], [-one,zero,zero,zero]]
bell={'phi_plus':(1,0,0,1), 'phi_minus':(1,0,0,-1),
      'psi_plus':(0,1,1,0), 'psi_minus':(0,1,-1,0)}


def kron(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]


def exp(rho, op):
    return sum(rho[i][j]*op[j][i] for i in range(4) for j in range(4))


def state(weights):
    return [[sum(weights[k]*F(v[i]*v[j],2) for k,v in bell.items())
             for j in range(4)] for i in range(4)]


def pt(rho):
    return [[rho[(i//2)*2+j%2][(j//2)*2+i%2] for j in range(4)] for i in range(4)]


def pt_eigenvalues(rho):
    # A Bell-diagonal partial transpose has two independent 2x2 blocks,
    # each with equal diagonals; eigenvalues are diagonal +/- offdiagonal.
    a=pt(rho)
    for i,j in product(range(4), repeat=2):
        if (i,j) not in {(0,0),(3,3),(0,3),(3,0),(1,1),(2,2),(1,2),(2,1)}:
            assert a[i][j] == 0
    assert a[0][0] == a[3][3] and a[0][3] == a[3][0]
    assert a[1][1] == a[2][2] and a[1][2] == a[2][1]
    return [a[0][0]+a[0][3],a[0][0]-a[0][3],
            a[1][1]+a[1][2],a[1][1]-a[1][2]]


w=F(16,25)
cases={
    'minimum_negativity': {'phi_plus':w, 'phi_minus':F(9,50), 'psi_plus':F(9,50), 'psi_minus':zero},
    'white_noise': {'phi_plus':F(73,100), 'phi_minus':F(9,100), 'psi_plus':F(9,100), 'psi_minus':F(9,100)},
    'bell_violation': {'phi_plus':F(41,50), 'phi_minus':zero, 'psi_plus':zero, 'psi_minus':F(9,50)},
}
ops={'XX':kron(X,X),'ZZ':kron(Z,Z),'XZ':kron(X,Z),'ZX':kron(Z,X),
     'XI':kron(X,I),'IX':kron(I,X),'ZI':kron(Z,I),'IZ':kron(I,Z),'YY':YY}
rows={}
for name, weights in cases.items():
    assert sum(weights.values())==one and all(v>=0 for v in weights.values())
    rho=state(weights)
    values={k:exp(rho,v) for k,v in ops.items()}
    assert values['XX']==values['ZZ']==w
    assert all(values[k]==0 for k in ['XZ','ZX','XI','IX','ZI','IZ'])
    eigenvalues=pt_eigenvalues(rho)
    negativity=sum(-v for v in eigenvalues if v<0)
    assert negativity == max(zero,max(weights.values())-F(1,2))
    assert negativity >= (2*w-1)/2
    # Horodecki criterion: S_max² = 4 times sum of two largest squared
    # singular values of T. Bell-diagonal T=(XX,YY,ZZ).
    ss=sorted((values[k]**2 for k in ['XX','YY','ZZ']),reverse=True)
    smax_squared=4*sum(ss[:2])
    rows[name]={'bell_weights':{k:str(v) for k,v in weights.items()},
                'XX':str(w),'ZZ':str(w),'YY':str(values['YY']),
                'partial_transpose_eigenvalues':[str(v) for v in eigenvalues],
                'negativity':str(negativity),'chsh_max_squared':str(smax_squared),
                'chsh_violation':smax_squared>4}
assert rows['minimum_negativity']['negativity']=='7/50'
assert rows['white_noise']['negativity']=='23/100'
assert rows['bell_violation']['negativity']=='8/25'
assert [rows[n]['chsh_violation'] for n in cases] == [False,False,True]
# Additional rational examples from the analytically parameterized family.
# This does not, by itself, prove the full interval stated in the report.
for v in (F(3,5), F(16,25), F(7,10)):
    low={'phi_plus':v, 'phi_minus':(1-v)/2, 'psi_plus':(1-v)/2, 'psi_minus':zero}
    high={'phi_plus':(1+v)/2, 'phi_minus':zero, 'psi_plus':zero, 'psi_minus':(1-v)/2}
    for weights in (low, high):
        r=state(weights)
        assert exp(r,ops['XX']) == exp(r,ops['ZZ']) == v
        assert exp(r,ops['XZ']) == exp(r,ops['ZX']) == 0
    assert sum(-e for e in pt_eigenvalues(state(low)) if e<0) == v-F(1,2)
    assert 2*v*v <= 1 and 1+v*v > 1
# For EVERY pair of unit directions in the XZ plane, the joint distribution
# is [1 + ab*w*(nx*mx+nz*mz)]/4. Test rational Pythagorean directions and
# all outcomes explicitly, checking the full distribution, not just S.
angles=[(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-4,5),F(3,5))]
for ax,az in angles:
    for bx,bz in angles:
        for a,b in product((-1,1), repeat=2):
            probs=[]
            for name in cases:
                rho=state(cases[name])
                A=[[ax*X[i][j]+az*Z[i][j] for j in range(2)] for i in range(2)]
                B=[[bx*X[i][j]+bz*Z[i][j] for j in range(2)] for i in range(2)]
                PA=[[(I[i][j]+a*A[i][j])/2 for j in range(2)] for i in range(2)]
                PB=[[(I[i][j]+b*B[i][j])/2 for j in range(2)] for i in range(2)]
                probs.append(exp(rho,kron(PA,PB)))
            assert len(set(probs))==1
            assert probs[0]==(1+a*b*w*(ax*bx+az*bz))/4
out={'scope':'Trusted ideal qubit models; no experimental-data or subject-identity inference.',
     'plane_correlation':str(w),'fidelity_lower_bound':str(w),
     'sharp_negativity_lower_bound':str((2*w-1)/2),
     'fixed_witness_value':str(1-2*w),'tested_joint_probabilities':len(angles)**2*4,
     'states':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
