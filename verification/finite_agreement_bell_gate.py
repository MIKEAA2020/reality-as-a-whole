#!/usr/bin/env python3
"""Finite no-signaling and conditional confidence illustration; synthetic only.
Relies on the standard Tsirelson inequality rather than deriving it.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import numpy as np

ROOT=Path(__file__).resolve().parent.parent


def box(delta):
    # a XOR b = xy XOR x, so the 11 outputs are perfectly correlated at delta=0.
    return {(a,b,x,y):((1-delta)*(F(1,2) if (a^b)==((x*y)^x) else 0)+delta*F(1,4))
            for x in (0,1) for y in (0,1) for a in (0,1) for b in (0,1)}


def conditional(p,ax,ay,x,y):
    # A0 or B0 outcome fixed; sum over the other party.
    if ax is not None:
        den=sum(p[(ax,b,x,y)] for b in (0,1));return [p[(ax,b,x,y)]/den for b in (0,1)]
    den=sum(p[(a,ay,x,y)] for a in (0,1));return [p[(a,ay,x,y)]/den for a in (0,1)]


def certainty_sets(p,epsilon):
    qa={a:conditional(p,a,None,0,1)[1] for a in (0,1)}
    qb={b:conditional(p,None,b,1,0)[1] for b in (0,1)}
    alpha={a for a in (0,1) if qa[a]==qa[0]}
    beta={b for b in (0,1) if qb[b]==qb[0]}
    path=[(alpha.copy(),beta.copy())]
    for _ in range(8):
        a_next={a for a in alpha if sum(conditional(p,a,None,0,0)[b] for b in beta)>=1-epsilon}
        b_next={b for b in beta if sum(conditional(p,None,b,0,0)[a] for a in alpha)>=1-epsilon}
        if (a_next,b_next)==(alpha,beta):break
        alpha,beta=a_next,b_next;path.append((alpha.copy(),beta.copy()))
    else:raise AssertionError('non-stabilizing')
    return qa,qb,alpha,beta,path


def quantum_endpoint_check():
    # |Phi+>, A0=Z,A1=-X, B0=(Z+X)/sqrt2,B1=(Z-X)/sqrt2.
    Z=np.diag([1.,-1.]);X=np.array([[0.,1.],[1.,0.]])
    A=[Z,-X];B=[(Z+X)/math.sqrt(2),(Z-X)/math.sqrt(2)]
    phi=np.array([1,0,0,1],float)/math.sqrt(2)
    pure=np.outer(phi,phi);I=np.eye(4)
    report=[]
    for visibility in (0.,0.4,1/math.sqrt(2)):
        mixing=visibility*math.sqrt(2)
        rho=mixing*pure+(1-mixing)*I/4
        assert np.min(np.linalg.eigvalsh(rho))>-1e-12
        errors=[]
        for x in (0,1):
            for y in (0,1):
                E=float(np.trace(rho@np.kron(A[x],B[y])))
                expected=visibility*(1 if ((x*y)^x)==0 else -1)
                assert abs(E-expected)<1e-12
                assert abs(float(np.trace(rho@np.kron(A[x],np.eye(2)))))<1e-12
                assert abs(float(np.trace(rho@np.kron(np.eye(2),B[y]))))<1e-12
                errors.append((1-(-1 if ((x*y)^x) else 1)*E)/2)
        assert max(abs(e-(1-visibility)/2) for e in errors)<1e-12
        report.append({'visibility':visibility,'loss_per_setting':errors[0],
                       'chsh':4*visibility,'min_state_eigenvalue':float(np.min(np.linalg.eigvalsh(rho)))})
    return report


def main():
    cases=[]
    for d in (F(0),F(1,10000),F(1,5),F(1,2),F(9,10)):
        p=box(d)
        assert all(sum(p[(a,b,x,y)] for a in (0,1) for b in (0,1))==1 for x in (0,1) for y in (0,1))
        for x in (0,1):
            for y in (0,1):
                for a in (0,1):assert sum(p[(a,b,x,y)] for b in (0,1))==F(1,2)
                for b in (0,1):assert sum(p[(a,b,x,y)] for a in (0,1))==F(1,2)
        qa,qb,ae,be,_=certainty_sets(p,F(0))
        qa2,qb2,ap,bp,_=certainty_sets(p,d/2)
        assert qa==qa2 and qb==qb2
        assert qa[0]==d/2 and qb[0]==1-d/2
        assert qa[1]==1-d/2 and qb[1]==d/2
        assert ap=={0} and bp=={0}
        if d==0:assert ae=={0} and be=={0}
        else:assert not ae and not be
        losses=[]
        for x in (0,1):
            for y in (0,1):
                losses.append(sum(p[(a,b,x,y)] for a in (0,1) for b in (0,1)
                                  if (a^b)!=((x*y)^x)))
        assert losses==[d/2]*4
        s=4-2*sum(losses);assert s==4*(1-d)
        cases.append({'noise_fraction':str(d),'q_A_a0':str(qa[0]),'q_B_b0':str(qb[0]),
                      'perfect_target_failure':str(d/2),'first_order_certainty_failure':str(d/2),
                      'q_gap':str(qb[0]-qa[0]),'exact_common_certainty':bool(ae and be),
                      'approx_fixedpoint_tolerance':str(d/2),'chsh':str(s)})
    n=10000;alpha=0.05;loss=0.1
    radius=math.sqrt(math.log(4/alpha)/(2*n)); upper_sum=4*(loss+radius)
    s_lower=4-2*upper_sum
    assert s_lower>2*math.sqrt(2)
    nzero=1000;delta=0.0001
    null_probability=(1-delta/2)**(2*nzero)
    zero_upper=1-alpha**(1/nzero)
    out={'status':'completed','scope':'synthetic binary no-signaling boxes, exact rational recursion and conditional iid confidence calculations; not experimental results',
        'cases':cases,'quantum_constructed_visibility_controls':quantum_endpoint_check(),
        'white_noise_threshold_beyond_quantum':1-1/math.sqrt(2),
        'zero_count_illustration':{'trials_per_two_checked_contexts':nzero,'noise_fraction':delta,
             'probability_zero_failures_in_both_contexts':null_probability,'one_sided_95pct_upper_per_context':zero_upper},
        'hypothetical_bell_test':{'settings':4,'fixed_trials_per_setting':n,'losses_per_setting':1000,
             'confidence_familywise':0.95,'iid_one_sided_hoeffding_radius':radius,
             'sum_loss_upper':upper_sum,'chsh_lower':s_lower,'tsirelson_bound':2*math.sqrt(2)},
        'assumptions':'fixed preselected settings, all trials reported, iid within each setting; significance does not establish exact common certainty or conscious subjects'}
    (ROOT/'verification/finite_agreement_bell_gate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
