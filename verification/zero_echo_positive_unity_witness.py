"""One-sided positive unity witness on the existing joint-sign echo.

All experience/report channels below are hypotheses. A physical Born cell
is not automatically an actual subject or a first-person observation.
"""
from fractions import Fraction as F
from itertools import product

SIGNS=(1,-1)
CELLS=tuple(product(SIGNS,repeat=2))


def lower_prevalence(q,false_positive_bound):
    """Sharp lower bound on P(E=1), with no false-negative constraint."""
    q,f=F(q),F(false_positive_bound)
    if not (0<=q<=1 and 0<=f<=1):raise ValueError('invalid probability')
    if f==1:return F(0)
    return max(F(0),(q-f)/(1-f))


def cell_bounds(q_by_cell,false_positive_bound):
    if set(q_by_cell)!=set(CELLS):raise ValueError('need all joint sign cells')
    return {c:lower_prevalence(q_by_cell[c],false_positive_bound) for c in CELLS}


def weighted_lower(q_by_cell,false_positive_bound,physical_cell_weights):
    """Weighted bound only if the supplied weights are reporter sampling weights.

    Physical Born weights may be used here only with a separate coverage and
    sampling premise; they are not automatically subject-incidence weights.
    """
    if set(physical_cell_weights)!=set(CELLS):raise ValueError('need all cell weights')
    w={c:F(physical_cell_weights[c]) for c in CELLS}
    if min(w.values())<0 or sum(w.values())!=1:raise ValueError('invalid weights')
    bound=cell_bounds(q_by_cell,false_positive_bound)
    return sum((w[c]*bound[c] for c in CELLS),F(0))


def report_table(q_by_cell,false_positive_bound,mode):
    """Construct exact compatible formal (cell,E,Y) probability tables.

    Modes: per-cell lower bound, all-positive latent unity, or a common
    latent prevalence (smallest consistent with the cell-specific bounds).
    Values q and false-positive bounds are synthetic unless measured.
    """
    if mode not in ('minimal','all','symmetric'):
        raise ValueError('unknown mode')
    f=F(false_positive_bound);lb=cell_bounds(q_by_cell,f)
    symmetric=max(lb.values());out={}
    for c in CELLS:
        q=F(q_by_cell[c])
        p=lb[c] if mode=='minimal' else F(1) if mode=='all' else symmetric
        if p==0:t=F(0);fp=q
        elif p==1:t=q;fp=F(0)
        elif q<=p:t=q/p;fp=F(0)
        else:t=F(1);fp=(q-p)/(1-p)
        if not (0<=t<=1 and 0<=fp<=f):raise ValueError('inconsistent model')
        out[c,1,1]=p*t/4
        out[c,1,0]=p*(1-t)/4
        out[c,0,1]=(1-p)*fp/4
        out[c,0,0]=(1-p)*(1-fp)/4
    return out


def uncalibrated_no_witness(q_by_cell):
    """Formal rival: E=0, physical report distribution unchanged."""
    if set(q_by_cell)!=set(CELLS):raise ValueError('need all joint sign cells')
    out={}
    for c in CELLS:
        q=F(q_by_cell[c])
        if not 0<=q<=1:raise ValueError('invalid q')
        out[c,0,1]=q/4;out[c,0,0]=(1-q)/4
        out[c,1,1]=F(0);out[c,1,0]=F(0)
    return out


def observable_marginal(table):
    return {(c,y):sum((table[c,e,y] for e in (0,1)),F(0))
            for c in CELLS for y in (0,1)}


def fields(mode,reporter_joint):
    """Formal represented fields, not an actual physical subject census.

    Each occurrence token is distinct. The reporter has the stipulated joint
    aspects iff reporter_joint; private tokens are not inferred from data.
    """
    if mode not in ('reporter_only','nested_private'):
        raise ValueError('unknown field model')
    out={'reporter':frozenset(('N_r','K_r') if reporter_joint else ('N_r',))}
    if mode=='nested_private':
        out.update({'private_N':frozenset(('N_private',)),
                    'private_K':frozenset(('K_private',))})
    return out
