#!/usr/bin/env python3
"""Three linked neutral configurations: holonomy and relative event controls.

Finite group example; no gravitational geometry, physical time, actual
experience, fundamental measure or no-residue solution is derived.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

try:
    from . import zero_total_internal_connection as c
    from . import zero_total_relational_record as m
except ImportError:
    import zero_total_internal_connection as c
    import zero_total_relational_record as m

E=c.IDENTITY
SIGN=((0,1,2),-1)


def events(cfg):
    q0,q1,q2,h01,h12,h02=cfg
    return tuple(int(c.act(h,r)==m.negative(q)) for q,r,h in
                 ((q0,q1,h01),(q1,q2,h12),(q0,q2,h02)))


def holonomy(cfg):
    _,_,_,h01,h12,h02=cfg
    return c.compose(c.compose(h01,h12),c.inv(h02))


def gauge(cfg,g0,g1,g2):
    q0,q1,q2,h01,h12,h02=cfg
    return (c.act(g0,q0),c.act(g1,q1),c.act(g2,q2),
            c.compose(g0,c.compose(h01,c.inv(g1))),
            c.compose(g1,c.compose(h12,c.inv(g2))),
            c.compose(g0,c.compose(h02,c.inv(g2))))


def gauge_fix(cfg):
    _,_,_,h01,h12,_=cfg
    return gauge(cfg,E,h01,c.compose(h01,h12))


def flat_distribution():
    counts=Counter()
    # In tree gauge with flat loop, the three aligned snapshots are uniform.
    for q0,q1,q2 in product(m.STATES,repeat=3):
        counts[events((q0,q1,q2,E,E,E))]+=1
    return {bits:F(counts[bits],216) for bits in product((0,1),repeat=3)}


def haar_distribution():
    counts=Counter(); q=m.STATES[0]
    # For any fixed endpoints, a uniform link maps its target uniformly
    # over S. Three independent links yield the same bit law for all endpoints.
    for h01,h12,h02 in product(c.GROUP,repeat=3):
        counts[events((q,q,q,h01,h12,h02))]+=1
    return {bits:F(counts[bits],1728) for bits in product((0,1),repeat=3)}


def link_pair_counts():
    pairs=[Counter(),Counter(),Counter()]
    for h01,h12 in product(c.GROUP,repeat=2):
        h02=c.compose(h01,h12)
        for ctr,pair in zip(pairs,((h01,h12),(h01,h02),(h12,h02))):ctr[pair]+=1
    return pairs


def run():
    assert len(c.GROUP)==12
    for ctr in link_pair_counts():
        assert len(ctr)==144 and set(ctr.values())=={1}
    q=m.STATES[0]; minus=m.negative(q)
    s=next(g for g in c.GROUP if g!=E and c.act(g,q)==q)
    assert c.compose(s,s)==E
    flat=(q,q,q,E,E,E); invisible_loop=(q,q,q,E,E,s)
    assert events(flat)==events(invisible_loop)==(0,0,0)
    assert holonomy(flat)==E and holonomy(invisible_loop)!=E
    flipflat=(q,minus,q,E,E,E); flipcurved=(q,minus,q,E,E,SIGN)
    assert events(flipflat)==(1,1,0) and events(flipcurved)==(1,1,1)
    assert holonomy(flipcurved)==SIGN
    for cfg in (flat,invisible_loop,flipflat,flipcurved,
                (m.STATES[1],m.STATES[2],m.STATES[3],c.GROUP[2],c.GROUP[5],c.GROUP[8])):
        fixed=gauge_fix(cfg)
        assert fixed[3]==fixed[4]==E
        assert fixed[5]==c.inv(holonomy(cfg))
        assert events(fixed)==events(cfg)
        for g0,g1,g2 in product(c.GROUP,repeat=3):
            changed=gauge(cfg,g0,g1,g2)
            assert events(changed)==events(cfg)
            assert holonomy(changed)==c.compose(g0,c.compose(holonomy(cfg),c.inv(g0)))
    pf,ph=flat_distribution(),haar_distribution()
    assert sum(pf.values())==sum(ph.values())==1
    assert pf[(1,1,1)]==0 and ph[(1,1,1)]==F(1,216)
    for i in range(3):
        assert sum(p for bits,p in pf.items() if bits[i])==F(1,6)
        assert sum(p for bits,p in ph.items() if bits[i])==F(1,6)
        for j in range(i):
            assert sum(p for bits,p in pf.items() if bits[i] and bits[j])==F(1,36)
            assert sum(p for bits,p in ph.items() if bits[i] and bits[j])==F(1,36)
    tv=sum(abs(pf[x]-ph[x]) for x in pf)/2
    assert tv==F(1,54)
    half={bits:(pf[bits]+ph[bits])/2 for bits in pf}
    assert half[(1,1,1)]==F(1,432)
    assert sum(abs(half[x]-ph[x]) for x in pf)/2==F(1,108)
    assert F(1,2)*F(1,12)+F(1,2)==F(13,24)
    return {'status':'passed','arithmetic':'exact integer and rational',
        'flat_flip_pattern_probability':{''.join(map(str,k)):str(v) for k,v in pf.items()},
        'haar_flip_pattern_probability':{''.join(map(str,k)):str(v) for k,v in ph.items()},
        'one_link_flip_probability_both':'1/6','two_link_flip_probability_both':'1/36',
        'three_flip_probability_flat':'0','three_flip_probability_haar':'1/216',
        'full_support_half_flat_mixture_three_flip':'1/432',
        'half_flat_mixture_flat_probability':'13/24',
        'total_variation_three_bit_distributions':str(tv),
        'total_variation_haar_vs_half_flat':'1/108',
        'two_link_marginals_equal':True,'flat_event_blind_to_nontrivial_stabilizer_holonomy':True,
        'scope':'Finite formal connection and stipulated measures; not emergent gravity, actual clocks, consciousness, or proof of zero-residue.'}


if __name__=='__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
