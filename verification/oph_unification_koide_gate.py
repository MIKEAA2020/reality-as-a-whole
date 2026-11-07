#!/usr/bin/env python3
"""Exact controls for what positive C3-circulant symmetry does and does not imply.

The Koide identity and balance condition are established in the OPH source;
this verifier illustrates them and does not audit the full source-to-mass join.
"""
from fractions import Fraction as F
from pathlib import Path
from math import sqrt
import json


def rational_case(a,b):
    a,b=F(a),F(b)
    # Real symmetric circulant: λ = a+2b, a-b, a-b.
    roots=(a+2*b,a-b,a-b)
    assert all(x>0 for x in roots)
    Q=sum(x*x for x in roots)/sum(roots)**2
    general=F(1,3)+F(2,3)*(b/a)**2
    assert Q==general
    return roots,Q


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def main():
    equal,qe=rational_case(2,0)
    simple,qs=rational_case(2,1)
    assert equal==(F(2),F(2),F(2)) and qe==F(1,3)
    assert simple==(F(4),F(1),F(1)) and qs==F(1,2)

    # Nondegenerate Hermitian circulant: eigs 5, 2±√3, all positive.
    m=[[3,1+1j,1-1j],[1-1j,3,1+1j],[1+1j,1-1j,3]]
    assert all(m[i][j]==m[j][i].conjugate() for i in range(3) for j in range(3))
    assert m[0][0]==3 and (m[0][0]*m[1][1]-m[0][1]*m[1][0])==7
    assert det3(m)==5  # positive leading principal minors => positive definite
    tr=sum(m[i][i] for i in range(3))
    tr2=sum(m[i][j]*m[j][i] for i in range(3) for j in range(3))
    assert tr==9 and tr2==39
    assert 2-sqrt(3)>0 and 5>2+sqrt(3)>2-sqrt(3)
    qdistinct=F(39,81)
    assert qdistinct==F(13,27) and qdistinct != F(2,3)

    count=0
    for a in range(1,31):
        for b in range(-a,a+1):
            if a+2*b>0 and a-b>0:
                _,Q=rational_case(a,b)
                assert Q != F(2,3)  # irrational |b|/a is needed
                count+=1
    # Standard Einstein-vacuum control: Ricci=Λg, null contractions vanish,
    # but its scalar curvature is 4Λ. Signature (-,+,+,+).
    g=(-1,1,1,1)
    nulls=((F(1),F(1),F(0),F(0)),
           (F(1),F(3,5),F(4,5),F(0)),
           (F(1),F(0),F(0),F(-1)))
    for Lambda in (F(0),F(1,3),F(-2,5),F(4)):
        scalar=sum(g[i]*Lambda*g[i] for i in range(4))
        assert scalar==4*Lambda
        for k in nulls:
            assert sum(g[i]*k[i]*k[i] for i in range(4))==0
            assert sum(Lambda*g[i]*k[i]*k[i] for i in range(4))==0

    out={'status':'passed','positive_integer_real_circulants_checked':count,
         'equal_positive_roots_Q':str(qe),
         'positive_example_eigenvalues':[str(x) for x in simple],
         'positive_example_Q':str(qs),
         'distinct_positive_spectrum':{'eigenvalues':['5','2-sqrt(3)','2+sqrt(3)'],
                                       'Q':str(qdistinct),'leading_principal_minors':[3,7,5]},
         'source_formula':'Q = 1/3 + (2/3)(|b|/a)^2; Q=2/3 iff |b|/a=1/sqrt(2)',
         'einstein_vacuum_null_controls':{'lambda_values':4,'null_vectors':3,
                                          'null_contraction':'0','ricci_scalar':'4*Lambda'},
         'scope':'Positive Hermitian cyclic response matrices under the additional hypothesized root-mass reading, plus algebraic null-contraction controls. The equal-event-block source packet, physical lepton attachment, physical masses and OPH as a whole are not tested. Symmetry and positivity alone do not impose balance; the GR control assumes its Einstein-vacuum premise.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
