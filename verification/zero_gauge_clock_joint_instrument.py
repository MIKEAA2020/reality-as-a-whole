"""Finite clock, chirality-memory, and holonomy joint instrument.

A coherent clock sensor and loop sensor are specified global multipliers; their
locality, energy, calibration and iid preparations are not derived here.
"""
import math
import numpy as np
from verification.zero_noncyclic_chirality_clock import sine_envelope


def sensor_unitary(probability):
    if not 0<=probability<=1:raise ValueError('probability must lie in [0,1]')
    a=math.sqrt(1-probability);b=math.sqrt(probability)
    return np.array([[a,-b],[b,a]])


def clock_model(n,alpha,beta):
    """alpha: false-late before 10; beta: false-early at/after 10."""
    if n<11 or not (0<=alpha<=1 and 0<=beta<=1):raise ValueError('invalid clock model')
    f=sine_envelope(n);r=np.array([alpha if k<10 else 1-beta for k in range(n)])
    p=float(np.dot(f*f,r));post=float(np.sum(f[10:]**2))
    if p<=0:raise ValueError('late event impossible')
    w=(1-beta)*post/p
    return f,r,p,w


def clock_residuals(n,alpha,beta):
    f,r,p,w=clock_model(n,alpha,beta)
    bare=2-2*float(np.dot(f[:-1],f[1:]))
    sensor=np.column_stack((np.sqrt(1-r),np.sqrt(r)))
    overlaps=np.sum(sensor[:-1]*sensor[1:],axis=1)
    coherent=2-2*float(np.dot(f[:-1]*f[1:],overlaps))
    late=2-2*float(np.dot(f[:-1]*f[1:],np.sqrt(r[:-1]*r[1:])))/p
    return {'bare':math.sqrt(max(0,bare)), 'coherent':math.sqrt(max(0,coherent)),
            'late':math.sqrt(max(0,late)), 'p_late':p, 'w':w}


def chi_unitary(chi,kappa=1.):
    """Outcome + is detector bit 0; E[C|χ]=κχ/3."""
    if not -1-1e-12<=chi<=3+1e-12 or not 0<=kappa<=1:raise ValueError('invalid chi or strength')
    return sensor_unitary((1-kappa*chi/3)/2)


def correlation(eps,strength,kappa,pb,pc,w):
    if not (-1<eps<1 and 0<=strength<=1 and 0<=kappa<=1 and
            0<=pb<=.5 and 0<=pc<=.5 and 0<=w<=1):raise ValueError('invalid model parameters')
    return w*(1-2*pb)*(1-2*pc)*strength*kappa*2*eps/81


def conditional_x_probabilities(eps,strength,kappa,pb,pc,w):
    mu=correlation(eps,strength,kappa,pb,pc,1.)
    # X=B*C, with B=0 when blank; accepted postwrite copies have ±1.
    return np.array([w*(1+mu)/2,1-w,w*(1-mu)/2])


def hoeffding_radius(m,delta):
    if m<1 or not 0<delta<1:raise ValueError('invalid sample size/confidence')
    return math.sqrt(2*math.log(2/delta)/m)


def epsilon_interval(mean,m,delta,strength,kappa,pb,pc,w):
    if not -1<=mean<=1:raise ValueError('invalid empirical mean')
    gain=correlation(.5,strength,kappa,pb,pc,w)*2
    if gain<=0:raise ValueError('zero gain; epsilon cannot be inferred')
    radius=hoeffding_radius(m,delta)
    return max(-1.,(mean-radius)/gain),min(1.,(mean+radius)/gain)


def pure_shift_distance(residual):
    if not 0<=residual<=math.sqrt(2)+1e-12:raise ValueError('requires nonnegative real overlap')
    return math.sqrt(max(0,residual**2-residual**4/4))


def conditional_drift_bound(p,d):
    if not 0<=p<=1 or not 0<=d<=1:raise ValueError('invalid probability or distance')
    if p<=d:return 2.
    return min(2.,3*d/(p-d))
