"""Temporal partition symmetry test. Periodic masks are bookkeeping,
not closed physical time loops. No phenomenal labels are supplied.
"""
from itertools import product


def masks(period):
    if not isinstance(period,int) or not 1<=period<=16:raise ValueError('Bookkeeping period in [1,16] required')
    return tuple(product((False,True),repeat=period))


def shift(mask,amount=1):
    if not mask:raise ValueError('Nonempty periodic boundary mask required')
    amount%=len(mask)
    return tuple(mask[(i-amount)%len(mask)] for i in range(len(mask)))


def stabilizer(mask):return tuple(s for s in range(len(mask)) if shift(mask,s)==tuple(mask))


def orbit(mask):return frozenset(shift(mask,s) for s in range(len(mask)))


def is_unit_shift_invariant(mask):return shift(mask)==tuple(mask)


def equal_length_boundaries(length,offset=0):
    if not isinstance(length,int) or length<1 or not isinstance(offset,int):raise ValueError('Positive integer duration and integer phase required')
    return tuple((t-offset)%length==0 for t in range(length))


def same_episode(t,u,length,offset=0):
    if not all(isinstance(v,int) for v in (t,u,length,offset)) or length<1:raise ValueError('Integer events and positive integer duration required')
    return (t-offset)//length==(u-offset)//length


def sliding_windows(length,start,stop):
    if not all(isinstance(v,int) for v in (length,start,stop)) or length<1 or start>stop:raise ValueError('Valid integer interval and positive duration required')
    # All windows whose starting index lies in [start,stop).
    return tuple(frozenset(range(t,t+length)) for t in range(start,stop))


def anchored_boundaries(length,anchor):return equal_length_boundaries(length,anchor)
