#!/usr/bin/env python3
"""Independent exact check of restricted OPH number-mixture arithmetic.

The theorem and controls originate in FloatingPragma's pinned source, not here.
No physical, phenomenal or full OPH model claim is tested.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def hypergeom(V,m,v,q):
    if not (0 <= q <= m and 0 <= v-q <= V-m):
        return F(0)
    return F(comb(m,q)*comb(V-m,v-q),comb(V,v))


def main():
    # Pinned source's full local-state comparison with the matching
    # sharp-number conditional state, assuming its diagonal sector model.
    intervals=[(240,937004677738,937004677739),
               (960,968471222490,968471222491),
               (3840,984231719274,984231719275)]
    rows=[]
    for v,lo,hi in intervals:
        V,m,q=4*v,4*v//3,v//3
        d=1-hypergeom(V,m,v,q)
        assert F(lo,10**12)<d<F(hi,10**12)
        rows.append({'V':V,'m':m,'v':v,'q':q,
                     'half_trace_distance_float':float(d),
                     'exact_rational_inside_source_interval':True})
    # For fixed v compare the complete retained diagonal state with the
    # Bernoulli(p) product, using equal within-sector configuration weights.
    # TV on sector weights equals the full diagonal-state trace distance.
    fixed=[]
    v=8
    for V in (24,96,960):
        m=V//3
        p=F(m,V)
        h=[hypergeom(V,m,v,q) for q in range(v+1)]
        b=[F(comb(v,q))*p**q*(1-p)**(v-q) for q in range(v+1)]
        assert sum(h)==sum(b)==1
        d=sum(abs(x-y) for x,y in zip(h,b))/2
        bound=min(F(1),F(v*(v-1),2*V))
        assert d<=bound
        fixed.append({'V':V,'v':v,'half_trace_distance':str(d),
                      'distance_float':float(d),'bound':str(bound)})
    out={'status':'passed',
         'source_commit':'98391cb29e965cc7338acf5852f6b95b15c27f3c',
         'sharp_sector_comparisons':rows,'fixed_window_product_comparisons':fixed,
         'scope':'Independent arithmetic only for stated diagonal hypergeometric states. Not a replay of the native source program or Lean, not validation of OPH physical premises, continuous QFT, subject incidence, phenomenal identity, a physical cosmological capacity, or an observer measure.'}
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
