"""Invariant and antisymmetric modes of the two echo records.

The operators and measurement instruments are physical/model constructions,
not an identity of either sign mode with experience or subject incidence.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

from verification.zero_joint_quality_incidence_root import quality,weight


def modes(i,s):
    """Exact S,T for the same supported echo event."""
    n,k=quality(i,s)
    return F(n+k,2),F(n-k,2)


def mode_law():
    out=defaultdict(F)
    for i,s in product(range(4),(1,-1)):
        out[modes(i,s)]+=weight(i,s)
    return dict(out)


def fixed_pointer_law(s):
    """Physical sector probabilities in the specified normalized sign slice."""
    if s not in (-1,1):raise ValueError('invalid pointer sign')
    out=defaultdict(F)
    for i in range(4):out[modes(i,s)]+=2*weight(i,s)
    return dict(out)


def coarse_law(joint):
    out=defaultdict(F)
    for (s,t),p in joint.items():out[s]+=p
    return dict(out)


def lueders_fidelity(probabilities):
    """Overlap with input pure state after a nonselective projective readout.

    Only applies to a pure input and the specified Lüders instrument, not an
    arbitrary instrument with the same outcome probabilities.
    """
    ps=tuple(F(p) for p in probabilities)
    if any(p<0 for p in ps) or sum(ps)!=1:raise ValueError('invalid law')
    return sum((p*p for p in ps),F(0))


def reported_pair_balance(i,s,lambda_):
    """Hypothetical normalized weights for the two opposite mode vectors."""
    lam=F(lambda_)
    if not 0<=lam<=1:raise ValueError('invalid share')
    S,T=modes(i,s)
    # Common G, positive on this support, intentionally omitted here.
    return ((2*lam-1)*S,(2*lam-1)*T)
