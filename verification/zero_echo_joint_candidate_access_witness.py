"""Access and conditional persistence witness on the joint echo candidate.

All sign claims concern the declared supported record table, not universal
quantum measurements or experimentally validated subject reports.
"""
from fractions import Fraction as F
from itertools import combinations
import math

from verification.zero_echo_joint_identity_balance import EVENTS,moment,magnitude,physical_ledger
from verification.zero_joint_quality_incidence_root import J,R,weight


def fields_at(t):
    if t not in range(4):raise ValueError('invalid checkpoint')
    # H is produced by the extra saved-J/current-J comparison at the anchor.
    return ('M','G','J','R','L','B')+(('H',) if t==3 else ())


def record(i,s,t):
    """Supported commuting sign records, with added L and optional H."""
    m=moment(i,s,t);b=R[i];z=b*J[i]
    out={'M':s,'G':magnitude(i),'J':m['j'],'R':m['r'],'L':z,'B':b}
    if t==3:out['H']=b
    return out


def target(i,s,t,name):
    m=moment(i,s,t)
    if name=='event':return i,s
    if name=='content':return m['quality']+(s,magnitude(i))
    if name=='ledger':return physical_ledger(i,s)
    if name=='pointer':return s
    raise ValueError('invalid target')


def partition(fields,t,name):
    if not set(fields)<=set(fields_at(t)):raise ValueError('field unavailable')
    table={}
    for i,s in EVENTS:
        r=record(i,s,t)
        observed=tuple(r[k] for k in fields)
        table.setdefault(observed,{}).setdefault(target(i,s,t,name),F(0))
        table[observed][target(i,s,t,name)]+=weight(i,s)
    return table


def best_guess(fields,t,name):
    return sum((max(values.values()) for values in partition(fields,t,name).values()),F(0))


def minimal_supports(t,name):
    fields=fields_at(t);minimal=[]
    for n in range(len(fields)+1):
        for subset in combinations(fields,n):
            if any(set(prev)<=set(subset) for prev in minimal):continue
            if best_guess(subset,t,name)==1:minimal.append(subset)
    return tuple(minimal)


def access_failure_bound(variation,errors):
    """Union bound for a support-based decoder, with matching error bounds."""
    errors=tuple(errors)
    if not 0<=variation<=1 or any(not 0<=e<=1 for e in errors):
        raise ValueError('invalid error bound')
    return min(1.,variation+sum(errors))


def quality_frequency(i,s,clock_weights):
    weights=tuple(F(x) for x in clock_weights)
    if len(weights)!=4 or min(weights)<0 or sum(weights)!=1:
        raise ValueError('invalid clock sampling law')
    return sum((weights[t] for t in range(4) if moment(i,s,t)['quality'][0]==1),F(0))


def ownership_witness(k,n,delta,false_positive,false_negative):
    """Compare all-persistent vs all-momentary identity for two distinct ticks.

    Report Y=1 means same owner. A two-sided Hoeffding interval for iid reports
    is combined with separately warranted error bounds. Rejecting a candidate
    is conditional on those bounds and on the declared population and target.
    """
    if not (isinstance(k,int) and isinstance(n,int) and n>=1 and 0<=k<=n and
            0<delta<1 and 0<=false_positive<=1 and 0<=false_negative<=1):
        raise ValueError('invalid witness data')
    q=k/n;radius=math.sqrt(math.log(2/delta)/(2*n))
    low=max(0.,q-radius);high=min(1.,q+radius)
    return {'mean':q,'radius':radius,'low':low,'high':high,
            'reject_momentary':low>false_positive,
            'reject_persistent':high<1-false_negative}
