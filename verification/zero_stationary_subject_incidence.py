"""Two hypothetical incidence ports on the existing stationary echo.

A fixed-anchor active physical swap exchanges the two quality operators in
this reduced model.  Subjects, physical realization of the swap, phenomenal
values, and all-effect incidence consistency are additional assumptions.
"""
from fractions import Fraction as F
from verification.zero_stationary_battery_bridge import (
    STATES,TICKS,PREFIX,INVERSE,stationary_weights,
)

ANCHOR=10


def anchor_flip(x):
    """D:(b,j,r,s)->(b,j*r,r,s); exchanges s*j with s*j*r."""
    b,j,r,s=x
    return b,j*r,r,s


def stationary_flip(n,x):
    """Lift D to a time-independent permutation in the stationary history."""
    return PREFIX[n][INVERSE[ANCHOR][anchor_flip(PREFIX[ANCHOR][INVERSE[n][x]])]]


def quality_at_anchor(n,x,port):
    _,j,r,s=PREFIX[ANCHOR][INVERSE[n][x]]
    if port=='now':return s*j
    if port=='echo':return s*j*r
    raise ValueError('invalid incidence type')


def incidence_weights(alpha):
    """Physical marginal fixed, two types weighted alpha and 1-alpha."""
    if not 0<=alpha<=1:raise ValueError('invalid type weight')
    w=stationary_weights()
    return {(n,x,p):w[n][x]*(alpha if p=='now' else 1-alpha)
            for n in range(TICKS) for x in STATES for p in ('now','echo')}


def joint_swap(n,x,port):
    return n,stationary_flip(n,x),('echo' if port=='now' else 'now')
