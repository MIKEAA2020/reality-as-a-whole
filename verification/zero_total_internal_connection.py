#!/usr/bin/env python3
"""Finite linked neutral configurations and independent frame transformations.

No connection dynamics, actual ontology, self-subsistence, physical gravity,
fundamental energy or experience is inferred from this model.
"""
from fractions import Fraction as F
from itertools import product
from math import log
from pathlib import Path
import json

try:
    from . import zero_total_relational_record as m
    from . import zero_total_symmetry_measure as z
except ImportError:
    import zero_total_relational_record as m
    import zero_total_symmetry_measure as z

GROUP=tuple((p,s) for p in m.PERMS for s in (-1,1))
IDENTITY=((0,1,2),1)
TRIPLES=tuple(product(m.STATES,m.STATES,GROUP))


def act(g,q):
    return m.symmetry(q,g[0],g[1])


def compose(g,h):
    """g after h: act(compose(g,h),q) = act(g,act(h,q))."""
    p,s=g; t,u=h
    return (tuple(t[p[i]] for i in range(3)),s*u)


def inv(g):
    p,s=g
    return (tuple(p.index(i) for i in range(3)),s)


def transform(triple,g,k):
    q,r,h=triple
    return (act(g,q),act(k,r),compose(g,compose(h,inv(k))))


def event_class(triple):
    q,r,h=triple
    return m.category(q,act(h,r))


def record(triple,bit):
    if bit not in (0,1): raise ValueError('bit must be 0 or 1')
    return (triple,bit ^ int(event_class(triple)=='flip'))


def weight(triple,w):
    q,r,h=triple
    return F(1,72)*m.kernel(q,act(h,r),w)


def marginals(w):
    probs={t:weight(t,w) for t in TRIPLES}
    assert sum(probs.values())==1
    classes={x:F(0) for x in z.CATS}
    qr={(q,r):F(0) for q,r in product(m.STATES,repeat=2)}
    qh={(q,h):F(0) for q,h in product(m.STATES,GROUP)}
    rh={(r,h):F(0) for r,h in product(m.STATES,GROUP)}
    for (q,r,h),p in probs.items():
        classes[event_class((q,r,h))]+=p
        qr[q,r]+=p; qh[q,h]+=p; rh[r,h]+=p
    assert all(p==F(1,36) for p in qr.values())
    assert all(p==F(1,72) for p in qh.values())
    assert all(p==F(1,72) for p in rh.values())
    return probs,classes


def run():
    for g,h in product(GROUP,repeat=2):
        assert compose(g,h) in GROUP
        for q in m.STATES:
            assert act(compose(g,h),q)==act(g,act(h,q))
        assert compose(g,inv(g))==IDENTITY==compose(inv(g),g)
    unseen=set(TRIPLES); orbits=[]
    while unseen:
        rep=next(iter(unseen))
        orbit={transform(rep,g,k) for g,k in product(GROUP,repeat=2)}
        assert orbit <= unseen
        unseen-=orbit
        assert len({event_class(t) for t in orbit})==1
        orbits.append((event_class(rep),len(orbit),144//len(orbit)))
    orbits.sort()
    assert sorted(n for _,n,_ in orbits)==[72,72,144,144]
    for t in TRIPLES:
        for g,k in product(GROUP,repeat=2):
            assert event_class(transform(t,g,k))==event_class(t)
        for bit in (0,1):
            assert record(*record(t,bit))==(t,bit)
        assert sum(t[0])==sum(t[1])==0
    fine,cf=marginals(z.FINE); orbit,co=marginals(z.ORBIT)
    assert all(p==F(1,432) for p in fine.values())
    assert cf['flip']==F(1,6) and co['flip']==F(1,4)
    for t in TRIPLES:
        size=next(n for c,n,_ in orbits if c==event_class(t))
        assert orbit[t]==F(1,4*size)
    # Orbit-stabilizer weights: 1/|Aut| normalize to the pushforward
    # of the uniform labelled-triple distribution in this finite model.
    groupoid={c:F(1,stab) for c,_,stab in orbits}
    norm=sum(groupoid.values())
    assert all(groupoid[c]/norm==cf[c] for c in z.CATS)
    conditional_information=log(6)-z.entropy(z.conditional_distribution(z.ORBIT))
    assert conditional_information>0
    return {'status':'passed','arithmetic':'exact rational except entropy in nats',
        'group_order':len(GROUP),'independent_frame_group_order':len(GROUP)**2,
        'linked_triples':len(TRIPLES),
        'gauge_orbits':{c:{'size':n,'stabilizer_order':s} for c,n,s in orbits},
        'fine_class_probabilities':{c:str(cf[c]) for c in z.CATS},
        'orbit_uniform_class_probabilities':{c:str(co[c]) for c in z.CATS},
        'identical_pairwise_marginals':{'q_r':'1/36','q_h':'1/72','r_h':'1/72'},
        'flip_event_fine':'1/6','flip_event_orbit_uniform':'1/4',
        'orbit_measure_three_way_total_correlation_nats':conditional_information,
        'gauge_invariant_record_is_reversible':True,
        'scope':'Finite stipulated connection and distributions, not a gravitational link, emergent spacetime, physical clock, or experience.'}


if __name__=='__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
