"""Exact rational locality/constraint checks for central-difference linearized ADM.

The model is a declared periodic finite lattice, not full Regge calculus or
nonlinear quantum GR. The verifier checks coefficient identities, not the
existence of a continuum limit or a physical matter detector.
"""
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path


def add(out,key,value):
    out[key]=out.get(key,F(0))+value
    if not out[key]: del out[key]


def shifted(s,axis,amount,n):
    v=list(s); v[axis]=(v[axis]+amount)%n
    return tuple(v)


def derivative(base, axes, n):
    sites={base:F(1)}
    for axis in axes:
        result={}
        for site,c in sites.items():
            add(result,shifted(site,axis,1,n),c/2)
            add(result,shifted(site,axis,-1,n),-c/2)
        sites=result
    return sites


def put(out,component,base,axes,weight,n):
    for site,c in derivative(base,axes,n).items():
        add(out,(tuple(sorted(component)),site),weight*c)


def scalar(base,n):
    out={}
    # Σij ∂i∂j h_ij - Σi,j ∂j² h_ii.
    for i in range(3):
        for j in range(3):
            put(out,(i,j),base,(i,j),F(1),n)
            put(out,(i,i),base,(j,j),F(-1),n)
    return out


def momentum(base,i,n):
    out={}
    # Canonical p_(ii)=π^ii, p_(ij)=2π^ij for i<j.
    for j in range(3):
        put(out,(i,j),base,(j,),F(-2 if i==j else -1),n)
    return out


def curvature(base,n):
    # R_xzyz = 1/2 (∂y∂z h_xz + ∂z∂x h_yz
    #                    -∂y∂x h_zz -∂z² h_xy).
    out={}
    for comp,axes,sign in [((0,2),(1,2),1),((1,2),(2,0),1),
                           ((2,2),(1,0),-1),((0,1),(2,2),-1)]:
        put(out,comp,base,axes,F(sign,2),n)
    return out


def dot(a,b):
    return sum((x*b.get(k,F(0)) for k,x in a.items()),F(0))


def eval_q(op,values):
    return sum(float(c)*values(comp,site) for (comp,site),c in op.items())


def run_lattice(n):
    assert n>=7 and n%2==1
    origin=(0,0,0)
    hs=scalar(origin,n)
    r=curvature(origin,n)
    tested=0
    # Translation invariance extends these pointwise checks from origin to all sites.
    for pt in product(range(n),repeat=3):
        for i in range(3):
            d=momentum(pt,i,n)
            assert dot(hs,d)==0
            assert dot(r,d)==0
            tested+=1
    # Bare h_xy is not a Dirac observable: find a concrete momentum constraint
    # at x-neighbour whose p_xy coefficient is nonzero.
    bare={((0,1),origin):F(1)}
    bare_witness=dot(bare,momentum((1,0,0),1,n))
    assert bare_witness!=0
    # TT classical initial data: h_xy=cos(kz), all other components/momenta=0.
    k=2*math.pi/n
    def field(comp,s):
        return math.cos(k*s[2]) if comp==(0,1) else 0.0
    max_constraint=max(abs(eval_q(scalar(s,n),field)) for s in product(range(n),repeat=3))
    rval=eval_q(r,field)
    expected=math.sin(k)**2/2
    assert max_constraint < 1e-14 and abs(rval-expected)<1e-14 and rval>0
    # Rank count: each nonzero discrete momentum has 3 independent D and 1 H.
    # Odd n ensures sin(2πm/n) vanishes only at m=0 in each direction.
    sites=n**3
    constraints=4*(sites-1)
    return {'n':n,'sites':sites,'origin_constraint_checks':tested,
            'independent_constraints_by_mode_count':constraints,
            'reduced_canonical_pairs_by_mode_count':6*sites-constraints,
            'bare_metric_witness':str(bare_witness),
            'curvature_coefficient_terms':len(r),
            'tt_max_hamiltonian_constraint_residual':max_constraint,
            'tt_curvature_at_origin':rval, 'tt_expected':expected}


def main():
    data={'status':'passed','lattices':[run_lattice(7),run_lattice(9)],
          'scope':'Linearized canonical lattice gravity; no nonlinear or continuum refoliation proof.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':main()
