"""Conditional quality-bridge test with noisy physical sector selection.

The echo signs are physical/model variables. Assigning them phenomenal
meaning and calibrating the proposed witness are explicit extra assumptions.
"""
from fractions import Fraction as F
from itertools import product
import math

from verification.zero_joint_quality_incidence_root import quality,R,weight
from verification.zero_echo_joint_identity_balance import EVENTS,magnitude


def structural_value(i,s,bridge):
    """A: pointer; B: type-invariant average, both scaled by model g."""
    n,e=quality(i,s);g=magnitude(i)
    if bridge=='pointer':return g*s
    if bridge=='symmetric':return g*F(n+e,2)
    raise ValueError('unknown bridge')


def selected_neutral_lower(p_low,e_minus,e_plus):
    """Lower P(R=- | H=-), assuming separately bounded source error rates.

    p_low lower bounds P(R=-) before H selection. e_minus upper bounds
    P(H=+|R=-), e_plus upper bounds P(H=-|R=+). A degenerate bound returns 0.
    """
    if not all(0<=x<=1 for x in (p_low,e_minus,e_plus)):
        raise ValueError('invalid sector calibration')
    numerator=p_low*(1-e_minus)
    denominator=numerator+(1-p_low)*e_plus
    return numerator/denominator if numerator>0 and denominator>0 else 0.


def compatible_report_ranges(p_low,e_minus,e_plus,false_neutral,miss_neutral):
    """Conservative bounds for selected neutral-witness rate q.

    The error premises must apply conditional on H=- in the target population.
    They need not be independent of the physical readout error.
    """
    if not 0<=false_neutral<=1 or not 0<=miss_neutral<=1:
        raise ValueError('invalid witness bounds')
    lower=selected_neutral_lower(p_low,e_minus,e_plus)
    return {'sector_lower':lower, 'pointer_upper':false_neutral,
            'symmetric_lower':lower*(1-miss_neutral)}


def finite_witness(k,n,delta,p_low,e_minus,e_plus,false_neutral,miss_neutral):
    """Separate sampling confidence from source/sector and witness premises."""
    if not (isinstance(k,int) and isinstance(n,int) and n>=1 and
            0<=k<=n and 0<delta<1):raise ValueError('invalid samples')
    bounds=compatible_report_ranges(p_low,e_minus,e_plus,false_neutral,miss_neutral)
    q=k/n;radius=math.sqrt(math.log(2/delta)/(2*n))
    low=max(0.,q-radius);high=min(1.,q+radius)
    return {**bounds,'mean':q,'radius':radius,'low':low,'high':high,
            'reject_pointer':low>bounds['pointer_upper'],
            'reject_symmetric':high<bounds['symmetric_lower']}


def calibrated_finite(k,n,delta,calibration):
    """Six-way confidence budget: data plus five matched calibration rates.

    calibration keys p, e_minus, e_plus, f, g each map to (count, trials).
    p counts true R=-; the rest count their corresponding error events. Each
    batch must have iid trials from its declared matched population, and the
    physical/experiential reference labels must be justified independently.
    A union bound does not require the batches to be mutually independent.
    """
    names=('p','e_minus','e_plus','f','g')
    if not (0<delta<1 and set(calibration)==set(names)):
        raise ValueError('invalid calibration')
    bounds={}
    for name in names:
        count,size=calibration[name]
        if not (isinstance(count,int) and isinstance(size,int) and
                size>=1 and 0<=count<=size):raise ValueError('invalid calibration count')
        radius=math.sqrt(math.log(6/delta)/(2*size))
        observed=count/size
        bounds[name]=(max(0.,observed-radius) if name=='p'
                      else min(1.,observed+radius))
    result=finite_witness(k,n,delta/6,bounds['p'],bounds['e_minus'],
                          bounds['e_plus'],bounds['f'],bounds['g'])
    return {**result,'calibration_bounds':bounds,'total_delta':delta}


def synthetic_joint(bridge,e_minus,e_plus,false_neutral,miss_neutral):
    """Exact rational physical/witness table for a stipulated iid channel.

    Here the witness errors are selected-neutral conditional and independent
    of H given the true structural category. This is only an example; the
    inequality routines do not require independent H and witness errors.
    """
    e_minus,e_plus,f,g=map(F,(e_minus,e_plus,false_neutral,miss_neutral))
    if any(not 0<=x<=1 for x in (e_minus,e_plus,f,g)):
        raise ValueError('invalid probabilities')
    out={}
    for i,s,h,y in product(range(4),(1,-1),(1,-1),(0,1)):
        r=R[i];bad=e_minus if r==-1 else e_plus
        ph=1-bad if h==r else bad
        neutral=structural_value(i,s,bridge)==0
        py=(1-g) if neutral else f
        out[i,s,h,y]=weight(i,s)*ph*(py if y else 1-py)
    return out
