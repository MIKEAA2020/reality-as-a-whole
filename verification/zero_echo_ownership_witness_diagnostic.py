"""Conditional calibration diagnostics for ownership on the existing echo.

The extra identity witness/report, its meaning and error bounds are not
supplied by the physical echo. No subject or real first-person report is
inferred from this formal probability model.
"""
from fractions import Fraction as F
from itertools import product


def probability(x):
    x=F(x)
    if not 0<=x<=1:raise ValueError('probability must be in [0,1]')
    return x


def compatible_bridges(qplus,qminus,false_positive_bound,false_negative_bound):
    """Which B-dependent truth bridges satisfy fixed per-truth error bounds?"""
    qp,qm,f,g=map(probability,(qplus,qminus,false_positive_bound,false_negative_bound))
    return {'positive':qp>=1-g and qm<=f,
            'negative':qm>=1-g and qp<=f}


def error_joint(e,d,overlap):
    """Joint errors for H vs B and W vs O, allowing arbitrary correlation."""
    e,d,t=map(probability,(e,d,overlap))
    if not max(F(0),e+d-1)<=t<=min(e,d):raise ValueError('incompatible error overlap')
    return {(0,0):1-e-d+t,(1,0):e-t,(0,1):d-t,(1,1):t}


def modeled_joint(bridge,e,d,overlap):
    """Synthetic P(B,H,W,O): W is a hypothesized identity-linked witness."""
    if bridge not in ('positive','negative'):raise ValueError('unknown bridge')
    errors=error_joint(e,d,overlap);out={}
    for b,eh,ew in product((1,-1),(0,1),(0,1)):
        truth=b if bridge=='positive' else -b
        h=b*(-1 if eh else 1)
        w=truth*(-1 if ew else 1)
        out[b,h,w,truth]=out.get((b,h,w,truth),F(0))+errors[eh,ew]/2
    return out


def agreement_bounds(physical_error_bound,witness_error_bound):
    """A lower bound for positive bridge, upper bound for negative bridge.

    No independence between the two error events is assumed.
    """
    e,d=map(probability,(physical_error_bound,witness_error_bound))
    s=min(F(1),e+d)
    return 1-s,s


def agreement(joint):
    return sum((p for (b,h,w,o),p in joint.items() if h==w),F(0))
