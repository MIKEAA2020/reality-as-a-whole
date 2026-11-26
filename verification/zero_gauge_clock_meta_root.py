"""Observable-specific clock drift and an indistinguishable calibration rival.

These are statements for the prior stipulated noncyclic clock, sign sensors,
and rho-epsilon family. A restricted output equivalence is not a claim that
all physical observables or actual experimental implementations coincide.
"""
import math
import numpy as np
from verification.zero_gauge_clock_joint_instrument import clock_model,correlation
from verification.zero_stationary_battery_bridge import STATES,advance
from verification.zero_clocked_chirality_history import INDEX,record_gate
from verification.zero_noncyclic_chirality_clock import local_step,window_history


def selected_weight(n,alpha,beta,steps):
    f,r,p,_=clock_model(n,alpha,beta)
    return float(np.dot(f*f*r,np.array([int(k+steps>=10) for k in range(n)]))/p)


def shifted_correlation(n,alpha,beta,steps,eps,lam=1.,kappa=1.,pb=.05,pc=.1):
    return correlation(eps,lam,kappa,pb,pc,selected_weight(n,alpha,beta,steps))


def target_post_mu(q,eps,lam,kappa,pb,pc):
    """q=E[t²|the chosen angular condition], including a fixed u or bin."""
    return (1-2*pb)*(1-2*pc)*lam*kappa*eps*q/9


def counterfeit_a(q,eps,lam,kappa,pb):
    """Context-dependent B flip pb+a*b*c; C flip independent."""
    return -(1-2*pb)*lam*kappa*eps*q/18


def adversarial_output(pb,pc,a):
    """Null-state B,C independent fair ±; B error depends jointly on b*c."""
    if not (0<=pb<=.5 and 0<=pc<=.5 and abs(a)<=min(pb,1-pb)):
        raise ValueError('invalid error channel')
    joint={(b,c):0. for b in (1,-1) for c in (1,-1)}
    err_b=err_c=0.
    for b,c in joint:
        flip_b=pb+a*b*c
        for eb in (0,1):
            for ec in (0,1):
                p=.25*(flip_b if eb else 1-flip_b)*(pc if ec else 1-pc)
                joint[(b*(-1)**eb,c*(-1)**ec)]+=p
                err_b+=p*eb;err_c+=p*ec
    return joint,err_b,err_c


def target_output(mu):
    if not -1<=mu<=1:raise ValueError('invalid sign correlation')
    return {(b,c):(1+b*c*mu)/4 for b in (1,-1) for c in (1,-1)}


def calibration_context_bound(k_plus,k_minus,m,delta):
    """Estimate a=(p_plus-p_minus)/2 and its two-sided Hoeffding radius.

    Each batch contains m iid Bernoulli trials in the matched bc=+1 or -1
    context. A union bound covers both rates with failure probability delta.
    """
    if not (m>=1 and 0<=k_plus<=m and 0<=k_minus<=m and 0<delta<1):
        raise ValueError('invalid calibration data')
    estimate=(k_plus-k_minus)/(2*m)
    radius=math.sqrt(math.log(4/delta)/(2*m))
    return estimate,radius


def systematic_sign_margin(mean,m,data_delta,kplus,kminus,cal_m,cal_delta,w,pc):
    """Lower sign margin for an independent-channel signal with additive a.

    Requires the same a in matched calibration and the accepted written data,
    exact w and pc, independent C flips, and no other systematic errors. The
    data and calibration confidence failures sum to at most data_delta +
    cal_delta; the function does not establish those physical assumptions.
    """
    from verification.zero_gauge_clock_joint_instrument import hoeffding_radius
    if not 0<=w<=1 or not 0<=pc<=.5:raise ValueError('invalid calibration')
    ahat,arad=calibration_context_bound(kplus,kminus,cal_m,cal_delta)
    return mean-hoeffding_radius(m,data_delta)-2*w*(1-2*pc)*(abs(ahat)+arad)


def coherent_sensor_window(n,q,h,alpha,beta):
    v=window_history(n,q,h);_,r,_,_=clock_model(n,alpha,beta)
    sensor=np.column_stack((np.sqrt(1-r),np.sqrt(r)))
    return {i:v[i,...,None]*sensor[i] for i in range(n)}


def inverse_step(block,n,q,h):
    """Inverse of local_step at source n; arbitrary reference/sensor amplitudes."""
    if n==9:block=block@record_gate(h)
    out=np.zeros_like(block)
    for i,x in enumerate(STATES):
        out[i]=np.roll(block[INDEX[advance(n%20,x)]],-q,axis=0)
    return out


def move_window(window,q,h,steps):
    current={k:v.copy() for k,v in window.items()}
    for _ in range(abs(steps)):
        out={}
        for n,v in current.items():
            if steps>0:
                # local_step expects old,reference,qutrit; sensor is spectator.
                z=np.stack([local_step(v[...,i],n,q,h) for i in (0,1)],axis=-1)
                out[n+1]=z
            else:
                # Pointer multiplication requires the pointer last.
                z=np.stack([inverse_step(v[...,i],n-1,q,h) for i in (0,1)],axis=-1)
                out[n-1]=z
        current=out
    return current


def measured_fixed_fiber(window,chi,lam,kappa,pb,pc):
    """Conditional X=B*C on a fixed t,χ fiber after coherent sensor readout."""
    p=numerator=0.
    for v in window.values():
        late=v[...,1]
        masses=np.sum(abs(late)**2,axis=(0,1)) # qutrit blank,+,-
        p+=float(masses.sum())
        numerator+=(1-2*pb)*float(masses[1]-masses[2])*(1-2*pc)*kappa*chi/3
    if p<=0:raise ValueError('late event impossible')
    return p,numerator/p
