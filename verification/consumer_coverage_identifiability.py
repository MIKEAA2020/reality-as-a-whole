"""Exact finite synthetic counterexample for partial consumer coverage.

No neural, subjective-experience, or real-world data are represented here.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def tv(p, q):
    return sum(abs(p.get(k, F(0)) - q.get(k, F(0))) for k in p.keys() | q.keys()) / 2


def observational(p):
    # Independent fair X,Z,K,W; N has Pr(N=1)=1/4. In treated arm,
    # H selects transmitted source with probability p, otherwise W.
    out = defaultdict(F)
    for x, z, n, k, w, h in product(range(2), repeat=6):
        weight = F(1, 2) ** 4 * (F(1, 4) if n else F(3, 4)) * (p if h else 1-p)
        c = x ^ n
        s = c if z == 0 or h else w
        r = s ^ k
        out[(x, z, c, r)] += weight
    assert sum(out.values()) == 1
    return dict(out)


def interventional(p, c, z=1):
    out = defaultdict(F)
    for k, w, h in product(range(2), repeat=3):
        weight = F(1, 4) * (p if h else 1-p)
        s = c if z == 0 or h else w
        out[(s ^ k, k)] += weight
    assert sum(out.values()) == 1
    return dict(out)


def marginal(p, axis):
    out = defaultdict(F)
    for (r, k), v in p.items():
        out[(r, k)[axis]] += v
    return dict(out)


def conditional(p, r):
    mass = sum(v for (rr, _), v in p.items() if rr == r)
    assert mass > 0
    return {k: p.get((r, k), F(0)) / mass for k in range(2)}


def main():
    rows=[]
    reference=observational(F(0))
    for p in (F(0), F(1,4), F(1,2), F(3,4), F(1)):
        assert observational(p)==reference
        d0,d1=interventional(p, 0),interventional(p, 1)
        observed=tv(marginal(d0,0),marginal(d1,0))
        hidden_cond=sum(marginal(d0,0)[r]*tv(conditional(d0,r),conditional(d1,r)) for r in range(2))
        joint=tv(d0,d1)
        assert observed==0 and joint==p and hidden_cond==p
        assert joint<=observed+hidden_cond
        for c in (0,1):
            assert marginal(interventional(p,c,z=0),0)=={0:F(1,2),1:F(1,2)}
        assert tv(interventional(p,0,z=0),interventional(p,1,z=0))==1
        rows.append({'retained_fraction_p':str(p), 'measured_R_tv':str(observed),
                     'full_joint_causal_tv':str(joint), 'conditional_hidden_tv':str(hidden_cond)})
    # Check the generic finite conditional-TV bound independently on all
    # 4-point distributions with masses in quarter increments.
    distributions=[]
    for counts in product(range(5), repeat=4):
        if sum(counts)==4:
            distributions.append({key:F(v,4) for key,v in zip(product(range(2),repeat=2),counts)})
    count=0
    for p0,p1 in product(distributions,repeat=2):
        y0,y1=marginal(p0,0),marginal(p1,0)
        # Conditional p1 on a zero-mass row is arbitrary; choose p0's
        # conditional there, which preserves the valid bound.
        hidden=F(0)
        for r in range(2):
            if y0.get(r,F(0)):
                k0=conditional(p0,r)
                k1=conditional(p1,r) if y1.get(r,F(0)) else k0
                hidden+=y0[r]*tv(k0,k1)
        assert tv(p0,p1)<=tv(y0,y1)+hidden
        count+=1
    result={'status':'passed','models':rows,'observed_joint_law_identical_for_all_p':True,
            'generic_bound_exhaustive_pairs':count,
            'scope':'synthetic binary causal models; conditional coverage term is not observed or bounded by the example'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
