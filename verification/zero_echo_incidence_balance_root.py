"""Conditional typed incidence balance on the established four-bin echo.

The type weights and felt interpretation are hypotheses. The diagonal
physical table does not establish a full quantum marginal or actual subjects.
"""
from fractions import Fraction as F
from itertools import product
from verification.zero_joint_quality_incidence_root import ANGLES, SIGNS, PORTS, quality, swap, weight

EVENTS=tuple(product(range(4),SIGNS))


def magnitude(i):
    u=ANGLES[i]
    return abs(u*(u+1))


def typed_weights(alpha):
    if set(alpha)!=set(EVENTS):raise ValueError('one type probability per event required')
    out={}
    for i,s in EVENTS:
        a=F(alpha[i,s])
        if not 0<=a<=1:raise ValueError('type probabilities must lie in [0,1]')
        out[i,s,'now']=weight(i,s)*a
        out[i,s,'echo']=weight(i,s)*(1-a)
    return out


def physical_marginal(alpha):
    weights=typed_weights(alpha)
    return {(i,s):sum(weights[i,s,p] for p in PORTS) for i,s in EVENTS}


def total_now_weight(alpha):
    weights=typed_weights(alpha)
    return sum((weights[i,s,'now'] for i,s in EVENTS),F(0))


def signed_total(alpha):
    weights=typed_weights(alpha)
    return sum((weights[i,s,p]*magnitude(i)*quality(i,s)[k]
                for i,s in EVENTS for k,p in enumerate(PORTS)),F(0))


def reduced_formula(alpha):
    typed_weights(alpha) # validate
    d0=F(alpha[0,1])-F(alpha[0,-1])
    d1=F(alpha[1,1])-F(alpha[1,-1])
    return F(3,64)*(d0-d1)


def type_exchange_invariant(alpha):
    weights=typed_weights(alpha)
    return all(weights[i,s,p]==weights[*swap(i,s),PORTS[1-k]]
               for i,s in EVENTS for k,p in enumerate(PORTS))


def counterpart_invariant(alpha):
    weights=typed_weights(alpha)
    return all(weights[i,s,p]==weights[i,-s,p] for i,s in EVENTS for p in PORTS)


def constant_alpha(a):return {(i,s):F(a) for i,s in EVENTS}
