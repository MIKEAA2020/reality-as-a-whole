"""Causal alternatives and a four-context conditional calibration bound.

All statements are for explicitly stipulated classical readout statistics of
commuting recorded-sign effects. No reference preparation or transportability
assumption is established by this module.
"""
import math

from verification.zero_gauge_clock_joint_instrument import hoeffding_radius

SIGNS = (1, -1)
CONTEXTS = tuple((b, c) for b in SIGNS for c in SIGNS)


def selected_null_tables(r, s, pb, pc):
    """Fair independent true signs; P(late|b,c)=r*(1+s*b*c)."""
    if not (0 < r < 1 and abs(s) <= 1 and 0 <= r*(1-abs(s)) and
            r*(1+abs(s)) <= 1 and 0 <= pb <= 1 and 0 <= pc <= 1):
        raise ValueError('invalid selection or flip probabilities')
    result = {y: {(b,c): 0.0 for b,c in CONTEXTS} for y in (0,1)}
    accept = 0.
    for b,c in CONTEXTS:
        rate = r*(1+s*b*c)
        accept += rate/4
        for y in (0,1):
            select = rate if y else 1-rate
            for eb in (0,1):
                for ec in (0,1):
                    flip = (pb if eb else 1-pb)*(pc if ec else 1-pc)
                    result[y][(b*(-1)**eb,c*(-1)**ec)] += select*flip/4
    for y in (0,1):
        weight = accept if y else 1-accept
        result[y] = {key: value/weight for key,value in result[y].items()}
    return accept,result


def product_mean(table):
    return sum(b*c*p for (b,c),p in table.items())


def robust_interval(mean, shots, delta_data, calibration, delta_cal,
                    w_low, w_high, gain, contamination=0., transport=0.,
                    selection_tv=0., blank_mean_bound=0.):
    """Bound preselection true-sign correlation given stated premises.

    calibration maps each true (b,c) context to (positive-product count,
    accepted sample size). The labels are imperfect by at most contamination
    among accepted references; transport bounds per-context mean mismatch
    between correct references and source; selection_tv bounds TV between
    preselection and accepted-written true-sign distributions. w bounds are
    independently justified, and a blank's conditional mean has absolute bound
    blank_mean_bound. Confidence only covers data/calibration sampling; errors
    in these independent bounds require their own failure budget.
    """
    if not (-1 <= mean <= 1 and shots >= 1 and 0 < delta_data < 1 and
            0 < delta_cal < 1 and set(calibration) == set(CONTEXTS) and
            0 <= w_low <= w_high <= 1 and 0 < gain <= 1 and
            0 <= contamination <= 1 and 0 <= transport <= 2 and
            0 <= selection_tv <= 1 and 0 <= blank_mean_bound <= 1):
        raise ValueError('invalid inputs')
    nmin = None
    discrepancy = 0.
    for (b,c),(positive,n) in calibration.items():
        if n < 1 or not 0 <= positive <= n:
            raise ValueError('invalid calibration count')
        hhat = 2*positive/n - 1
        discrepancy = max(discrepancy,abs(hhat-gain*b*c))
        nmin = n if nmin is None else min(nmin,n)
    # Union bound over four two-sided, bounded [-1,1] sample means.
    rcal = math.sqrt(2*math.log(8/delta_cal)/nmin)
    systematic = min(2.,discrepancy+rcal+2*contamination+transport)
    rdata = hoeffding_radius(shots,delta_data)
    blank = (1-w_low)*blank_mean_bound
    if w_low == 0:
        lo,hi = -1.,1.
    else:
        low_numerator=mean-rdata-blank
        high_numerator=mean+rdata+blank
        lo=max(-1.,min(low_numerator/w_low,low_numerator/w_high)/gain
               - systematic/gain - 2*selection_tv)
        hi=min(1.,max(high_numerator/w_low,high_numerator/w_high)/gain
               + systematic/gain + 2*selection_tv)
    return {'lower':lo,'upper':hi,'data_radius':rdata,'cal_radius':rcal,
            'cal_discrepancy':discrepancy,'systematic':systematic,
            'blank_allowance':blank}
