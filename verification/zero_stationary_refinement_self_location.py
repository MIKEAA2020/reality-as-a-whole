"""Self-location refinement on the same reduced sphere-echo ledger.

Fine labels are subeffects of coarse outcomes. Whether they represent new
actual subject incidences is not decided by the physical arithmetic.
"""
from fractions import Fraction as F
from verification.zero_stationary_battery_bridge import OLD,SIGNS,PREFIX


def coarse_outcomes():
    out=[]
    for (b,z),p in OLD.items():
        for s in SIGNS:
            state=PREFIX[10][b,z,1,s]
            out.append((state,p/2))
    return out


def refine(split_b):
    """Split each selected physical event into two identical half effects."""
    if split_b not in (-1,1):raise ValueError('split_b must be sign')
    out=[]
    for state,p in coarse_outcomes():
        pieces=2 if state[0]==split_b else 1
        for label in range(pieces):out.append((state,label,p/pieces))
    return out


def disagreement(x):
    b,j,r,s=x
    return s*j != s*j*r


def fractions(outcomes):
    return (F(sum(disagreement(x) for x,_,_ in outcomes),len(outcomes)),
            sum((p for x,_,p in outcomes if disagreement(x)),F(0)))


def incidence_type_given_disagreement(alpha):
    """Strong product incidence extension; alpha is an input, not derived."""
    if not 0<=alpha<=1:raise ValueError('invalid type weight')
    d=sum((p for x,p in coarse_outcomes() if disagreement(x)),F(0))
    return alpha*d/d
