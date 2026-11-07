#!/usr/bin/env python3
"""Icosahedral CHSH controls, with arbitrary-state and singlet scopes separated.

The singlet enumeration and operator witness are numerical checks; the report
contains the analytic argument and cites the standard CHSH square identity.
No physical claim about OPH's full measurement family follows.
"""
from collections import Counter
from itertools import product
from math import sqrt, isclose
from pathlib import Path
import json


def add(A,B):
    return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]


def scale(c,A):
    return [[c*x for x in row] for row in A]


def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def kron(A,B):
    return [[A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])]
             for j in range(len(A[0])*len(B[0]))]
            for i in range(len(A)*len(B))]


def pauli(n):
    x,y,z=n
    return [[z,x-1j*y],[x+1j*y,-z]]


def main():
    phi=(1+sqrt(5))/2
    raw=[(0,s,t*phi) for s in (-1,1) for t in (-1,1)]
    raw += [(s,t*phi,0) for s in (-1,1) for t in (-1,1)]
    raw += [(s*phi,0,t) for s in (-1,1) for t in (-1,1)]
    norm=sqrt(1+phi*phi)
    v=[tuple(x/norm for x in row) for row in raw]
    dots=[[sum(x*y for x,y in zip(a,b)) for b in v] for a in v]
    classes=Counter()
    for row in dots:
        for d in row:
            if isclose(abs(d),1,abs_tol=1e-12):
                classes['same_or_opposite']+=1
            else:
                assert isclose(abs(d),1/sqrt(5),abs_tol=1e-12)
                classes['distinct_axes']+=1
    # Singlet: E(a,b)=-a·b. Absolute value makes global sign immaterial.
    hist=Counter()
    for a0,a1,b0,b1 in product(range(12), repeat=4):
        s=dots[a0][b0]+dots[a0][b1]+dots[a1][b0]-dots[a1][b1]
        hist[round(abs(s),10)]+=1
    singlet_bound=1+3/sqrt(5)
    singlet_max=max(hist)
    assert isclose(singlet_max,singlet_bound,abs_tol=1e-9)
    assert hist[singlet_max]==960 and sum(hist.values())==20736

    # Four actual 4x4 qubit matrices with distinct local axes. Both sides may
    # use the same labels: the state need not be a singlet.
    A0,A1=pauli(v[0]),pauli(v[1])
    B0,B1=pauli(v[0]),pauli(v[1])
    C=add(add(kron(A0,B0),kron(A0,B1)),add(kron(A1,B0),scale(-1,kron(A1,B1))))
    C2=mul(C,C)
    I=[[complex(i==j) for j in range(4)] for i in range(4)]
    high,low=36/5,4/5
    # P projects onto the top eigenspace of C², and (I+C/sqrt(high))/2
    # selects its positive-C part. Pick a nonzero column of that product.
    P=scale(1/(high-low), add(C2,scale(-low,I)))
    pos=scale(.5,add(I,scale(1/sqrt(high),C)))
    select=mul(pos,P)
    w=None
    for col in range(4):
        cand=[select[i][col] for i in range(4)]
        length=sqrt(sum(abs(x)**2 for x in cand))
        if length>1e-8:
            w=[x/length for x in cand]
            break
    assert w is not None
    Cw=[sum(C[i][j]*w[j] for j in range(4)) for i in range(4)]
    expect=sum(w[i].conjugate()*Cw[i] for i in range(4))
    universal_bound=6/sqrt(5)
    assert abs(expect.imag)<1e-12
    assert isclose(expect.real,universal_bound,abs_tol=1e-12)
    assert universal_bound < 14/5 < 2*sqrt(2)
    threshold=universal_bound/(14/5)
    out={'status':'passed','enumerated_setting_quadruples':sum(hist.values()),
         'pair_dot_classes':dict(classes),
         'singlet_max':singlet_bound,'singlet_maximizers':hist[singlet_max],
         'all_score_magnitudes':{str(k):hist[k] for k in sorted(hist,reverse=True)},
         'any_two_qubit_state_max':universal_bound,
         'witness_expected_value':expect.real,
         'friend_gate_comparator':14/5,'friend_gate_gap':14/5-universal_bound,
         'visibility_threshold_for_friend_gate_family':threshold,
         'scope':'Ideal dichotomic qubit Pauli observables chosen from 12 vertices on each side, arbitrary bipartite quantum state for the general bound; singlet bound additionally assumes aligned frames and singlet correlations. Not an OPH-wide prediction or an experimental data comparison.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
