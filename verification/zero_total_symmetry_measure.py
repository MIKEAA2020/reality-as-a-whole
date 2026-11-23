#!/usr/bin/env python3
"""Gauge-orbit and maximum-entropy controls on the neutral six-state model.

These are selected finite measures on a stipulated model, not derivations of
physical probabilities, consciousness, cosmology, or an ultimate ontology.
"""
from fractions import Fraction as F
from itertools import product
from math import log
from pathlib import Path
import json

try:
    from . import zero_total_relational_record as m
except ImportError:
    import zero_total_relational_record as m

CATS=('stay','flip','move','both_moved')
FINE=(F(1,6),F(1,6),F(1,3),F(1,3))
ORBIT=(F(1,4),F(1,4),F(1,4),F(1,4))
FIXED_F_MAX=(F(1,10),F(1,2),F(1,5),F(1,5))
FIXED_F_RIVAL=(F(2,5),F(1,2),F(1,20),F(1,20))


def entropy(probabilities):
    p=list(probabilities)
    if any(x<0 for x in p) or abs(float(sum(p))-1)>1e-12:
        raise ValueError('probabilities must be nonnegative and normalized')
    return -sum(float(x)*log(float(x)) for x in p if x)


def conditional_distribution(w):
    q=m.STATES[0]
    return [m.kernel(q,r,w) for r in m.STATES]


def flip_word_probability(w,word):
    """Exact stationary Markov probability of an invariant F-bit word."""
    if any(bit not in (0,1) for bit in word): raise ValueError('bits only')
    state={q:F(1,6) for q in m.STATES}
    for bit in word:
        state={r:sum(state[q]*m.kernel(q,r,w)*int((r==m.negative(q))==bool(bit))
                     for q in m.STATES) for r in m.STATES}
    return sum(state.values())


def fixed_flip_max(p):
    p=F(p)
    if not 0<=p<=1: raise ValueError('p must be in [0,1]')
    return ((1-p)/5,p,2*(1-p)/5,2*(1-p)/5)


def run():
    q=m.STATES[0]
    sizes={cat:sum(m.category(q,r)==cat for r in m.STATES)*6 for cat in CATS}
    assert sizes==dict(zip(CATS,(6,6,12,12)))
    # Diagonal relabeling preserves F. Independent relabeling of the second
    # snapshot can turn the flip pair into a stay pair; a shared comparison
    # structure is therefore part of the model.
    r=m.negative(q)
    independent=next(m.symmetry(r,p,1) for p in m.PERMS if m.symmetry(r,p,1)==q)
    assert m.category(q,r)=='flip' and m.category(q,independent)=='stay'
    assert fixed_flip_max(F(1,2))==FIXED_F_MAX
    assert fixed_flip_max(F(1,6))==FINE
    for w in (FINE,ORBIT,FIXED_F_MAX,FIXED_F_RIVAL):
        assert all(sum(m.kernel(x,y,w) for y in m.STATES)==1 for x in m.STATES)
        assert all(m.kernel(x,y,w)==m.kernel(y,x,w) for x,y in product(m.STATES,repeat=2))
        for y in m.STATES:
            assert sum(F(1,6)*m.kernel(x,y,w) for x in m.STATES)==F(1,6)
    assert conditional_distribution(FINE)==[F(1,6)]*6
    assert FINE[1]==F(1,6) and ORBIT[1]==F(1,4)
    # Two laws with same full flip-bit word distributions and different
    # invariant stay event; exhaustive through words of length 5.
    for n in range(6):
        for word in product((0,1),repeat=n):
            target=F(1,2**n)
            assert flip_word_probability(FIXED_F_MAX,word)==target
            assert flip_word_probability(FIXED_F_RIVAL,word)==target
    assert FIXED_F_MAX[0]==F(1,10) and FIXED_F_RIVAL[0]==F(2,5)
    assert all(x>0 for x in FIXED_F_MAX+FIXED_F_RIVAL)
    h_fine=entropy(conditional_distribution(FINE))
    h_orbit_fine=entropy(conditional_distribution(ORBIT))
    h_fine_cat=entropy(FINE)
    h_orbit_cat=entropy(ORBIT)
    assert h_fine>h_orbit_fine and h_orbit_cat>h_fine_cat
    return {'status':'passed','arithmetic':'exact rational for probabilities; floating logs for entropy',
        'single_state_orbits':1,'ordered_pair_orbit_sizes':sizes,
        'independent_relabeling_can_change_flip_to_stay':True,
        'fine_uniform_event_class_probabilities':[str(x) for x in FINE],
        'orbit_uniform_event_class_probabilities':[str(x) for x in ORBIT],
        'fine_uniform_flip_probability':str(FINE[1]),'orbit_uniform_flip_probability':str(ORBIT[1]),
        'fine_entropy_fine_uniform_nats':h_fine,'fine_entropy_orbit_uniform_nats':h_orbit_fine,
        'class_entropy_fine_uniform_nats':h_fine_cat,'class_entropy_orbit_uniform_nats':h_orbit_cat,
        'fixed_flip_half_maxentropy_weights':[str(x) for x in FIXED_F_MAX],
        'fixed_flip_half_rival_weights':[str(x) for x in FIXED_F_RIVAL],
        'same_flip_word_law_checked_through_length':5,
        'stay_probabilities_maxentropy_and_rival':['1/10','2/5'],
        'scope':'Finite mathematical control only; not selection of an actual law, absolute probability, time, self-subsistence, or experience.'}


if __name__=='__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
