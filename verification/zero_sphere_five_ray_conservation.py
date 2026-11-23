"""Intrinsic 2+3 partition of five generic future null rays in 3+1D."""
from fractions import Fraction as F
from verification.zero_sphere_relative_orientation import delta, valid_null, lorentz_dot


def add(vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(4))


def scale(c,v): return tuple(c*x for x in v)


def cofactor_null_relation(rays):
    if len(rays)!=5 or not all(valid_null(v) for v in rays):
        raise ValueError('five future-directed null vectors required')
    c=[(-1)**i*delta(rays[:i]+rays[i+1:]) for i in range(5)]
    if any(x==0 for x in c):
        raise ValueError('generic configuration requires all 4-ray determinants nonzero')
    if add([scale(ci,ki) for ci,ki in zip(c,rays)]) != (0,0,0,0):
        raise ArithmeticError('null relation failed')
    positive=[i for i,x in enumerate(c) if x>0]
    negative=[i for i,x in enumerate(c) if x<0]
    if sorted([len(positive),len(negative)]) != [2,3]:
        raise ArithmeticError('future null directions should yield a 2+3 partition')
    pair=positive if len(positive)==2 else negative
    triple=negative if len(positive)==2 else positive
    if c[pair[0]]<0: c=[-x for x in c]
    return {'coefficients':c,'pair':pair,'triple':triple}


def total_pair_momentum(rays,coefficients,pair):
    return add([scale(coefficients[i],rays[i]) for i in pair])


def center_frame_energy_numerators(rays,coefficients,pair):
    """Return positive -p_i·P and P^2; divide numerators by sqrt(-P^2)."""
    P=total_pair_momentum(rays,coefficients,pair)
    mass2=-lorentz_dot(P,P)
    if mass2<=0: raise ValueError('incoming total must be future timelike')
    return [-lorentz_dot(scale(abs(c),k),P) for c,k in zip(coefficients,rays)],mass2
