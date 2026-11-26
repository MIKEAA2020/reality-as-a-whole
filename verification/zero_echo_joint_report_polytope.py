"""Joint-report feasibility with arbitrary dependence, not an experience assay.

All probabilities are conditional on the same selected joint protocol. The
16-state latent table is a relaxation of the full physical echo, not a new
physical or phenomenal validation. LP results are numerical, not exact proofs.
"""
from itertools import product
import math
import numpy as np
from scipy.optimize import linprog

from verification.zero_echo_quality_bridge_discrimination import selected_neutral_lower

STATES=tuple(product((0,1),repeat=4))  # D, O, Y, W
EVENTS={
    'y':lambda d,o,y,w:y==1,
    'w':lambda d,o,y,w:w==1,
    'both':lambda d,o,y,w:y==1 and w==1,
}


def _vec(predicate):
    return np.array([float(predicate(*s)) for s in STATES])


def _probability(x):
    if not math.isfinite(x) or not 0<=x<=1:
        raise ValueError('invalid probability')
    return float(x)


def model(intervals,fy,gy,fw,gw,h,sector_lower=0.,candidate=None):
    """Build an outer feasible set, using joint failure h on D=O=1.

    intervals map y, w, both to [lower,upper]. Conditional error bounds are
    homogeneous and thus also valid when their conditioning mass is zero.
    candidate is (quality, owner), or None for general prevalence inference.
    """
    fy,gy,fw,gw,h,sector_lower=map(_probability,(fy,gy,fw,gw,h,sector_lower))
    if set(intervals)!=set(EVENTS):raise ValueError('three intervals required')
    rows=[];rhs=[]
    for name,event in EVENTS.items():
        if len(intervals[name])!=2:raise ValueError('invalid interval')
        lo,hi=map(_probability,intervals[name])
        if lo>hi:raise ValueError('invalid interval')
        v=_vec(event)
        rows.extend((v,-v));rhs.extend((hi,-lo))
    # P(error, condition) <= bound * P(condition)
    definitions=(
        (lambda d,o,y,w:d==0,lambda d,o,y,w:y==1,fy),
        (lambda d,o,y,w:d==1,lambda d,o,y,w:y==0,gy),
        (lambda d,o,y,w:o==0,lambda d,o,y,w:w==1,fw),
        (lambda d,o,y,w:o==1,lambda d,o,y,w:w==0,gw),
        (lambda d,o,y,w:d==1 and o==1,
         lambda d,o,y,w:y==0 or w==0,h),
    )
    for condition,error,limit in definitions:
        c=_vec(condition)
        e=_vec(lambda d,o,y,w:condition(d,o,y,w) and error(d,o,y,w))
        rows.append(e-limit*c);rhs.append(0.)
    if candidate is not None:
        if (not isinstance(candidate,tuple) or len(candidate)!=2 or
            candidate[0] not in ('pointer','symmetric') or
            candidate[1] not in ('persistent','momentary')):
            raise ValueError('invalid candidate')
        quality,owner=candidate
        # Pointer has D=0. Symmetric has D=1 on R=-, at least L.
        d=_vec(lambda d,o,y,w:d==1)
        rows.append(d if quality=='pointer' else -d)
        rhs.append(0. if quality=='pointer' else -sector_lower)
        o=_vec(lambda d,o,y,w:o==1)
        rows.append(-o if owner=='persistent' else o)
        rhs.append(-1. if owner=='persistent' else 0.)
    return np.array(rows),np.array(rhs)


def assess(intervals,fy,gy,fw,gw,h,sector_lower=0.,candidate=None,tolerance=1e-8):
    """Numerical feasibility and, when feasible, minimum joint truth mass.

    A common nonnegative relaxation slack is minimized over all inequalities,
    while positivity and normalization remain exact. Slack > tolerance gives
    a numerical rejection; solver failures raise. A near-boundary solution is
    classified indeterminate rather than confidently rejected. A minimizer is
    returned only for a successful unrelaxed LP. Results are subject to solver
    floating point tolerances and must not be treated as exact certificates.
    """
    if not math.isfinite(tolerance) or tolerance<=0:raise ValueError('invalid tolerance')
    a,b=model(intervals,fy,gy,fw,gw,h,sector_lower,candidate)
    equality=np.ones((1,len(STATES)))
    relaxed=linprog(np.r_[np.zeros(len(STATES)),1.],
                    A_ub=np.c_[a,-np.ones(len(a))],b_ub=b,
                    A_eq=np.c_[equality,[[0.]]],b_eq=[1.],
                    bounds=[(0,None)]*(len(STATES)+1),method='highs')
    if not relaxed.success:raise RuntimeError('slack LP failed: '+relaxed.message)
    slack=max(0.,float(relaxed.fun))
    if slack>tolerance:
        return {'status':'rejected','slack':slack,'joint_min':None,'witness':None}
    target=_vec(lambda d,o,y,w:d==1 and o==1)
    optimal=linprog(target,A_ub=a,b_ub=b,A_eq=equality,b_eq=[1.],
                    bounds=[(0,None)]*len(STATES),method='highs')
    if optimal.status==2:
        return {'status':'indeterminate','slack':slack,'joint_min':None,'witness':None}
    if not optimal.success:raise RuntimeError('prevalence LP failed: '+optimal.message)
    return {'status':'feasible','slack':slack,'joint_min':max(0.,float(optimal.fun)),
            'witness':optimal.x}


def calibrated_assessment(counts,delta,calibration,tolerance=1e-8):
    """Eleven-event budget: eight one-sided calibrations, three data rates.

    h counts failures of (Y=W=1) among independently justified D=O=1
    references in the same selected joint protocol. Trials must be independent
    within each batch, but need not have identical distributions. In that
    case inference concerns their average target table, and the reference-batch
    mean error rates must transfer to the relevant pooled target conditionals.
    Different batches need not be mutually independent. Candidate and general
    LPs use one simultaneous event; no candidate multiplicity is needed.
    """
    names=('p','em','ep','fy','gy','fw','gw','h')
    if (len(counts)!=4 or not all(isinstance(k,int) and k>=0 for k in counts)
        or sum(counts)==0 or not 0<delta<1 or set(calibration)!=set(names)):
        raise ValueError('invalid input')
    bounds={}
    for name in names:
        k,n=calibration[name]
        if not isinstance(k,int) or not isinstance(n,int) or n<1 or not 0<=k<=n:
            raise ValueError('invalid calibration')
        r=math.sqrt(math.log(11/delta)/(2*n))
        bounds[name]=max(0.,k/n-r) if name=='p' else min(1.,k/n+r)
    n=sum(counts);k11,k10,k01,k00=counts
    means={'y':(k11+k10)/n,'w':(k11+k01)/n,'both':k11/n}
    radius=math.sqrt(math.log(22/delta)/(2*n))
    intervals={k:(max(0.,v-radius),min(1.,v+radius)) for k,v in means.items()}
    L=selected_neutral_lower(bounds['p'],bounds['em'],bounds['ep'])
    args=(intervals,bounds['fy'],bounds['gy'],bounds['fw'],bounds['gw'],bounds['h'])
    candidates={(q,o):assess(*args,L,(q,o),tolerance)
                for q,o in product(('pointer','symmetric'),('persistent','momentary'))}
    return {'calibration_bounds':bounds,'intervals':intervals,'radius':radius,
            'sector_lower':L,'candidates':candidates,
            'general':assess(*args,tolerance=tolerance),'total_delta':delta}
