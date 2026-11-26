"""One event, two record-quality coordinates, and a constrained opposite pair.

This is a typed operational model of a candidate incidence interface. It does
not determine whether a bearer is a subject or whether either coordinate is
felt. In particular the one-occurrence interpretation is a stated hypothesis.
"""
from fractions import Fraction as F

SIGNS=(1,-1)
ANGLES=(F(-3,4),F(-1,4),F(1,4),F(3,4))
R=(-1,-1,1,1)
J=(1,-1,1,1)
PORTS=('now','echo')


def event(i,s):
    if i not in range(4) or s not in SIGNS:raise ValueError('invalid event')
    return i,s


def value(i,s,port):
    event(i,s)
    if port not in PORTS:raise ValueError('invalid coordinate')
    now=s*J[i]
    return now if port=='now' else now*R[i]


def quality(i,s):return value(i,s,'now'),value(i,s,'echo')


def reflect(i):
    if i not in range(4):raise ValueError('invalid bin')
    return 1-i if i<2 else i


def echo_checkpoints(i,s):
    """Instantaneous (j,r,now,echo) through the actual T-Q-T echo.

    The pre-echo j sign is z=R[i]*J[i], and B=R[i] on the supported
    post-echo state. This is a structural transport, not subject persistence.
    """
    event(i,s);b=R[i];z=b*J[i]
    states=((z,1),(z,z),(b*z,z),(b*z,b))
    return tuple((j,r,s*j,s*j*r) for j,r in states)


def counterpart(i,s):
    event(i,s)
    return i,-s


def swap(i,s):
    event(i,s)
    return reflect(i),s


def weight(i,s):
    event(i,s)
    return F(1,8)


def measure(labeled_events):
    """One-occurrence hypothesis: query labels are aliases of (i,s)."""
    ids=set()
    for i,s,port in labeled_events:
        event(i,s)
        if port not in PORTS:raise ValueError('invalid query label')
        ids.add((i,s))
    return sum((weight(i,s) for i,s in ids),F(0))


def scalar_after_alias(i,s):
    """A scalar descends to the now/echo alias only when values agree."""
    a,b=quality(i,s)
    if a!=b:raise ValueError('two query values do not define one scalar')
    return a


def twin_vectors(i,s,kind='swap_invariant'):
    """Structural two-coordinate signed values, not claimed experiences."""
    event(i,s);u=ANGLES[i]
    if kind=='swap_invariant':g=abs(u*(u+1))
    elif kind=='absolute':g=abs(u)
    else:raise ValueError('unknown magnitude')
    a,b=quality(i,s)
    return (g*a,g*b),(-g*a,-g*b)


def joint_law():
    out={(a,b):F(0) for a in SIGNS for b in SIGNS}
    for i in range(4):
        for s in SIGNS:out[quality(i,s)]+=weight(i,s)
    return out


def expanded_type_weights(alpha):
    """Alternative disjoint-type incidence hypothesis with same marginal."""
    alpha=F(alpha)
    if not 0<=alpha<=1:raise ValueError('invalid alpha')
    return {(i,s,port):weight(i,s)*(alpha if port=='now' else 1-alpha)
            for i in range(4) for s in SIGNS for port in PORTS}
