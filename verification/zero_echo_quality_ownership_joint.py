"""Joint conditional quality/ownership witness on the existing echo.

The two additional truth variables and their calibrations are hypotheses,
not quantities established by the physical echo or evidence of experience.
"""
from fractions import Fraction as F
from itertools import product
import math

from verification.zero_echo_quality_bridge_discrimination import (
    selected_neutral_lower,structural_value)
from verification.zero_joint_quality_incidence_root import R,weight


def positive_joint_lower(q_lower,fy,fw):
    """Conservative lower P(D=1 and O=1) from joint affirmative rate.

    fy and fw bound false-affirmative rates in the same selected population
    and joint protocol for the same reporter. No miss-rate or error-independence
    assumption is needed; the sum bound need not be sharp.
    """
    if any(not 0<=x<=1 for x in (q_lower,fy,fw)):
        raise ValueError('invalid probability')
    total=fy+fw
    return max(0.,(q_lower-total)/(1-total)) if total<1 else 0.


def calibrated_positive(k11,n,delta,calibration):
    """One-sided positive test: data and two matched false-positive batches.

    No false-negative calibration is used. Batches must have iid trials and
    independently justified, target-matched truth labels; their mutual
    independence is not required by the union bound.
    """
    if not (isinstance(k11,int) and isinstance(n,int) and n>=1 and
            0<=k11<=n and 0<delta<1 and set(calibration)=={'fy','fw'}):
        raise ValueError('invalid data')
    bounds={}
    for name in ('fy','fw'):
        count,size=calibration[name]
        if not (isinstance(count,int) and isinstance(size,int) and size>=1 and 0<=count<=size):
            raise ValueError('invalid calibration count')
        bounds[name]=min(1.,count/size+math.sqrt(math.log(3/delta)/(2*size)))
    radius=math.sqrt(math.log(3/delta)/(2*n))
    q_low=max(0.,k11/n-radius)
    return {'q_low':q_low,'radius':radius,'calibration_bounds':bounds,
            'joint_truth_lower':positive_joint_lower(q_low,bounds['fy'],bounds['fw']),
            'total_delta':delta}


def joint_rates(k11,k10,k01,k00,delta,p_low,e_minus,e_plus,fy,gy,fw,gw):
    """Bounds and candidate survival for three simultaneous Bernoulli rates.

    Counts are accepted selected-run outputs (Y,W). Y means neutral valence;
    W means same owner at two distinct times. Physical selection and both
    witness calibrations must apply in the same target population and joint
    measurement protocol. Individual report errors may be correlated.
    """
    counts=(k11,k10,k01,k00)
    if not all(isinstance(k,int) and k>=0 for k in counts):
        raise ValueError('invalid counts')
    n=sum(counts)
    if n<1 or not 0<delta<1 or any(not 0<=x<=1 for x in (fy,gy,fw,gw)):
        raise ValueError('invalid probability inputs')
    sel=selected_neutral_lower(p_low,e_minus,e_plus)
    neutral_lower=sel*(1-gy)
    owner_lower=1-gw
    means={'y':(k11+k10)/n,'w':(k11+k01)/n,'both':k11/n}
    # Three two-sided Hoeffding events, each with failure delta/3.
    radius=math.sqrt(math.log(6/delta)/(2*n))
    low={k:max(0.,v-radius) for k,v in means.items()}
    high={k:min(1.,v+radius) for k,v in means.items()}
    survive={}
    for quality,owner in product(('pointer','symmetric'),('persistent','momentary')):
        qok=(low['y']<=fy) if quality=='pointer' else (high['y']>=neutral_lower)
        ook=(high['w']>=owner_lower) if owner=='persistent' else (low['w']<=fw)
        survive[quality,owner]=qok and ook
    direct=positive_joint_lower(low['both'],fy,fw)
    quality_lower=max(0.,(low['y']-fy)/(1-fy)) if fy<1 else 0.
    owner_truth_lower=max(0.,(low['w']-fw)/(1-fw)) if fw<1 else 0.
    frechet=max(0.,quality_lower+owner_truth_lower-1)
    return {'n':n,'means':means,'radius':radius,'low':low,'high':high,
            'sector_lower':sel,'symmetric_lower':neutral_lower,
            'persistent_lower':owner_lower,'survive':survive,
            'direct_joint_lower':direct,'frechet_joint_lower':frechet,
            'joint_truth_lower':max(direct,frechet)}


def calibrated_joint(counts,delta,calibration):
    """Ten-event confidence budget: seven calibrations and three data rates.

    Calibration keys p, em, ep, fy, gy, fw, gw map to (count, trials).
    p counts R=-; other counts are corresponding error events. All batches
    require valid iid matched populations and independently justified labels.
    Their joint independence is unnecessary for the union bound.
    """
    names=('p','em','ep','fy','gy','fw','gw')
    if not 0<delta<1 or set(calibration)!=set(names) or len(counts)!=4:
        raise ValueError('invalid calibration')
    bounds={}
    for name in names:
        count,n=calibration[name]
        if not (isinstance(count,int) and isinstance(n,int) and n>=1 and 0<=count<=n):
            raise ValueError('invalid calibration count')
        radius=math.sqrt(math.log(10/delta)/(2*n))
        q=count/n
        bounds[name]=max(0.,q-radius) if name=='p' else min(1.,q+radius)
    result=joint_rates(*counts,3*delta/10,bounds['p'],bounds['em'],bounds['ep'],
                       bounds['fy'],bounds['gy'],bounds['fw'],bounds['gw'])
    return {**result,'calibration_bounds':bounds,'total_delta':delta}


def coupled_bernoulli(py,pw,coupling):
    """Exact coupling with given marginals; 0/1 are Fréchet extremes."""
    py,pw,c=map(F,(py,pw,coupling))
    if any(not 0<=x<=1 for x in (py,pw,c)):raise ValueError('invalid coupling')
    lo=max(F(0),py+pw-1);hi=min(py,pw)
    p11=lo+c*(hi-lo)
    return {(1,1):p11,(1,0):py-p11,(0,1):pw-p11,(0,0):1-py-pw+p11}


def synthetic_joint(quality,owner,em,ep,fy,gy,fw,gw,coupling):
    """One specified synthetic source, selector and coupled-witness channel.

    The coupling applies within each latent category. It is not an actual
    experiential instrument or a calibration of any human reporter.
    """
    if quality not in ('pointer','symmetric') or owner not in ('persistent','momentary'):
        raise ValueError('invalid candidate')
    em,ep,fy,gy,fw,gw,c=map(F,(em,ep,fy,gy,fw,gw,coupling))
    if any(not 0<=x<=1 for x in (em,ep,fy,gy,fw,gw,c)):
        raise ValueError('invalid probabilities')
    out={}
    for i,s,h,y,w in product(range(4),(1,-1),(1,-1),(0,1),(0,1)):
        r=R[i];err=em if r==-1 else ep
        ph=1-err if h==r else err
        neutral=structural_value(i,s,quality)==0
        same=owner=='persistent'
        py=1-gy if neutral else fy
        pw=1-gw if same else fw
        joint=coupled_bernoulli(py,pw,c)[y,w]
        out[i,s,h,y,w]=weight(i,s)*ph*joint
    return out


def selected_truth_errors(table,quality,owner):
    """Error rates for the same physical report table under a truth hypothesis.

    Undefined conditional error rates are returned as None. This diagnostic
    cannot validate which truth hypothesis corresponds to actual experience.
    """
    if quality not in ('pointer','symmetric') or owner not in ('persistent','momentary'):
        raise ValueError('invalid candidate')
    den={key:F(0) for key in ('y_false','y_miss','w_false','w_miss')}
    num=dict(den)
    for (i,s,h,y,w),prob in table.items():
        if h!=-1:continue
        d=structural_value(i,s,quality)==0
        o=owner=='persistent'
        key='y_miss' if d else 'y_false'
        den[key]+=prob
        if y!=(1 if d else 0):num[key]+=prob
        key='w_miss' if o else 'w_false'
        den[key]+=prob
        if w!=(1 if o else 0):num[key]+=prob
    return {key:(num[key]/den[key] if den[key] else None) for key in den}


def selected_table(table):
    """Return probabilities for (Y,W), conditional on physical H=-."""
    den=sum(p for (i,s,h,y,w),p in table.items() if h==-1)
    if den<=0:raise ValueError('no accepted runs')
    return {(y,w):sum(p for (i,s,h,yy,ww),p in table.items()
                      if h==-1 and (yy,ww)==(y,w))/den
            for y,w in product((0,1),repeat=2)}
