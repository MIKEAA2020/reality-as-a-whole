"""Clock-dressed sign counterpart on the actual quantum echo support.

The sign pointer is represented by orthogonal s slices. The clock phase is
essential: the physical Q pulse anticommutes with the old exchange S on the
valid sector. This defines a conditional symmetry, not an experiential law.
"""
from fractions import Fraction as F
from verification.zero_relational_chirality_report_test import apply64
from verification.zero_internal_contextual_reference_test import ss

TICKS=20


def q_count(t):
    if not 0<=t<=TICKS:raise ValueError('invalid tick')
    return int(t>=9)+int(t>=12)


def phase(t):return (-1)**q_count(t)


def exchange(rows,t=None):
    """S on each original quantum vector, optionally dressed by the clock."""
    factor=1 if t is None else phase(t)
    return tuple([factor*apply64(ss,x) for x in part] for part in rows)


def raw_history_overlap():
    # On prepared x with Sx=-x, raw S X_M contributes -(-1)^nQ(t).
    return -sum((F(phase(t),TICKS) for t in range(TICKS)),F(0))


def incidence_weights(epsilon,u,k):
    """Hypothetical normalized non-Born incidence distortion at fixed u.

    K=±1; physical conditional K weights remain 1/2. Their u marginal is
    unchanged by this distortion. It is not an alteration of the quantum state.
    """
    if not -1<epsilon<1 or not -1<u<1 or k not in (1,-1):raise ValueError('invalid input')
    return (1+epsilon*k*u)/2
