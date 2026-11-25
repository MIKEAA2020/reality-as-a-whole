"""Executable reduced stationary interface for the existing sphere echo.

This is a retrospective finite physical-model integration, not a new
registered battery or an experiential/actuality constitution.  B,J,R,S are
commuting physical signs.  The forward source/reservoir operations have been
coarse-grained out, not derived to be absent from the full physical model.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

SIGNS=(1,-1)
STATES=tuple(product(SIGNS,repeat=4)) # b,j,r,s
TICKS=20
# Physical Born weights on the old supported sector; s is equally weighted.
OLD={(1,1):F(1,2),(-1,1):F(1,4),(-1,-1):F(1,4)}


def advance(t,state):
    """Step t -> t+1 of the already-specified reduced echo-label action."""
    if not 0<=t<TICKS or state not in STATES:raise ValueError('outside domain')
    b,j,r,s=state
    if t in (7,9,10,12):r*=j  # T: echo bit controlled by j
    elif t in (8,11):j*=b      # Q: j bit controlled by B
    return b,j,r,s


def prefixes():
    """Maps each initial reduced basis label to its label at each tick."""
    out=[{x:x for x in STATES}]
    for t in range(TICKS):out.append({x:advance(t,out[-1][x]) for x in STATES})
    assert out[-1]==out[0]
    return out


PREFIX=prefixes()
INVERSE=[{v:k for k,v in d.items()} for d in PREFIX]


def relational_effect(anchor,predicate):
    """Diagonal of 20*twirl(|anchor><anchor| tensor predicate).

    Row n and state x is the predicate's value at anchor after mapping x
    backward to the initial reduced label, then forward to anchor.  The
    result is a stationary diagonal projection for a Boolean predicate.
    """
    if not 0<=anchor<TICKS:raise ValueError('invalid anchor')
    result=[]
    for n in range(TICKS):
        row={}
        for x in STATES:
            val=predicate(PREFIX[anchor][INVERSE[n][x]])
            if val not in (False,True,0,1):raise ValueError('Boolean predicate required')
            row[x]=int(val)
        result.append(row)
    return result


def stationary_weights(ready=1):
    """Exact diagonal weights of the uniformly clock-labeled history.

    This is also the diagonal of a coherent pure reduced history, because
    different clock/basis labels are orthogonal.  It cannot establish any
    non-diagonal claim about the original full sphere/reservoir state.
    """
    if ready not in SIGNS:raise ValueError('invalid ready sign')
    out=[]
    for t in range(TICKS):
        row={x:F(0) for x in STATES}
        for (b,z),p in OLD.items():
            for s in SIGNS:row[PREFIX[t][b,z,ready,s]]+=p/F(2*TICKS)
        out.append(row)
    return out


def expectation(weights,effect):
    return sum((weights[t][x]*effect[t][x] for t in range(TICKS) for x in STATES),F(0))


def initial_amplitudes(ready=1):
    """Amplitudes for one coherent reduced pure-state realization."""
    if ready not in SIGNS:raise ValueError('invalid ready sign')
    return {(b,z,ready,s):sqrt(float(p)/2) for (b,z),p in OLD.items() for s in SIGNS}


def predicates():
    """Typed claim bits refer to B; proposed quality signs remain hypotheses."""
    return {
        'ready':lambda x:x[2]==1,
        'normal_correct':lambda x:x[2]==x[0],
        'normal_error':lambda x:x[2]!=x[0],
        'inverted_correct':lambda x:-x[2]==x[0],
        'quality_changed':lambda x:x[3]*x[1] != x[3]*x[1]*x[2],
        'now_positive':lambda x:x[3]*x[1]==1,
        'echo_positive':lambda x:x[3]*x[1]*x[2]==1,
    }
