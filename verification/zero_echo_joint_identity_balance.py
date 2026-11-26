"""Conditional occurrence content and incidence balance on the old echo.

All equivalence, ownership and factor-weight interpretations are explicitly
stipulated; physical effects, model values and felt qualities are distinct.
"""
from fractions import Fraction as F
from itertools import product

from verification.zero_joint_quality_incidence_root import (
    ANGLES, J, R, quality, weight, echo_checkpoints, event)

EVENTS=tuple(product(range(4),(1,-1)))


def signature(i,s,fields):
    """Recorded physical content available to a chosen interface at anchor."""
    event(i,s)
    n,e=quality(i,s);u=ANGLES[i];b=R[i];z=b*J[i]
    values={'now':n,'echo':e,'pointer':s,'bin':i,'j':J[i],
            'r':b,'saved':z,'magnitude':abs(u*(u+1))}
    try:return tuple(values[f] for f in fields)
    except KeyError as exc:raise ValueError('unknown content field') from exc


def content_classes(fields):
    """Coarsest quotient on these events preserving the selected content."""
    out={}
    for i,s in EVENTS:
        out.setdefault(signature(i,s,fields),[]).append((i,s))
    return out


def optimal_event_guess(fields):
    """Best guess from these specified commuting records, not all POVMs."""
    return sum((max(weight(*x) for x in group)
                for group in content_classes(fields).values()),F(0))


def physical_ledger(i,s):
    """Conserved branch-label candidate; saved-J memory is an added resource."""
    return signature(i,s,('pointer','r','saved','magnitude'))


def moment(i,s,t):
    """Quality and ledger at the four physical T-Q-T checkpoints."""
    if t not in range(4):raise ValueError('invalid checkpoint')
    j,r,n,e=echo_checkpoints(i,s)[t]
    return {'ledger':physical_ledger(i,s),'quality':(n,e),'j':j,'r':r,
            'occurrence_slot':(i,s,t)}


def candidate_slot(i,s,t,clock_weights):
    """One conditional occurrence slot with a proposed common owner ledger.

    Clock weights are an explicit sampling protocol, not a derived actual
    incidence measure. Stored content is structural, not asserted to be felt.
    """
    weights=tuple(F(x) for x in clock_weights)
    if len(weights)!=4 or any(x<0 for x in weights) or sum(weights)!=1:
        raise ValueError('invalid clock sampling law')
    info=moment(i,s,t)
    n,e=info['quality'];g=magnitude(i)
    return {'slot':info['occurrence_slot'],'owner':info['ledger'],
            'content':(n,e,s,g),'weight':weights[t]*weight(i,s),
            'pair':((g*n,g*e),(-g*n,-g*e))}


def scalar_value(i,s,a,b):
    """All counterpart-odd scalar functions on two binary quality coordinates."""
    n,e=quality(i,s);a,b=F(a),F(b)
    return a*F(n+e,2)+b*F(n-e,2)


def magnitude(i):
    u=ANGLES[i]
    return abs(u*(u+1))


def expanded_weight(i,s,factor,lambdas):
    """Supplemental normalized factor incidence, not a subject census."""
    event(i,s)
    if factor not in (1,2):raise ValueError('invalid factor')
    lam=F(lambdas[i,s])
    if not 0<=lam<=1:raise ValueError('invalid incidence split')
    return weight(i,s)*(lam if factor==1 else 1-lam)


def expanded_total(lambdas,selected=EVENTS):
    """Unnormalized selected first moment of the two opposite model vectors."""
    a=b=F(0)
    for i,s in selected:
        n,e=quality(i,s);g=magnitude(i)
        net=expanded_weight(i,s,1,lambdas)-expanded_weight(i,s,2,lambdas)
        a+=net*g*n;b+=net*g*e
    return a,b


def invariant_measure(lambdas):
    """Invariance of this extension under (i,s,factor)->(i,-s,factor)."""
    return all(F(lambdas[i,1])==F(lambdas[i,-1]) for i in range(4))


def factor_swap_invariant(lambdas):
    """Invariance under the abstract factor-label swap at fixed event."""
    return all(F(lambdas[i,s])==F(1,2) for i,s in EVENTS)
