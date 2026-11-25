"""Joint claim/quality events on the old sphere and two reference clocks.

Clock phases are the previously stipulated q=1 or q=2 correlated reference,
not derived spacetime, a physical subject, or intrinsically available records.
"""
from collections import defaultdict
from fractions import Fraction as F
from verification.zero_stationary_battery_bridge import TICKS,stationary_weights


def joint_at_tick(t):
    if not 0<=t<TICKS:raise ValueError('invalid clock tick')
    table=defaultdict(F)
    for (b,j,r,s),p in stationary_weights()[t].items():
        table[(r==b, s*j!=s*j*r)]+=TICKS*p
    return dict(table)


def conditioned_reference(q,reference):
    if q not in (1,2) or reference not in range(4):raise ValueError('invalid clock input')
    ts=[t for t in range(TICKS) if q*t%4==reference]
    if not ts:raise ValueError('zero probability reference event')
    out=defaultdict(F)
    for t in ts:
        for cell,p in joint_at_tick(t).items():out[cell]+=p/len(ts)
    return dict(out)
