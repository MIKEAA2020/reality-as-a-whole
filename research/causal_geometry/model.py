"""Conditional 1+1 causal/volume reconstruction and scale diagnostics.

Coordinates, smooth-manifold class, and calibrated measures are explicit inputs.
Finite samples do not establish causal faithfulness of an unlabelled AQFT net.
"""
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('spacetime_geometry_reference',Path(__file__).resolve().parents[1]/'spacetime_net'/'model.py')
net=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(net)
w,vac,car=net.w,net.vac,net.car


def null(time,space):
    return time+space,time-space


def cartesian(u,v):
    return (u+v)/2,(u-v)/2


def precedes(p,q,strict=False):
    if strict:
        return p[0]<q[0] and p[1]<q[1]
    return p[0]<=q[0] and p[1]<=q[1]


def order_map(point,alpha=.1,beta=.2):
    if alpha<0 or beta<0 or not all(math.isfinite(x) for x in (*point,alpha,beta)):
        raise ValueError('Finite points and nonnegative monotone-map coefficients required')
    u,v=point
    return u+alpha*u**3,v+beta*v**3


def rectangle(p,q):
    if not precedes(p,q,strict=True):
        raise ValueError('Nondegenerate future null rectangle required')
    return q[0]-p[0],q[1]-p[1]


def flat_interval_squared(p,q):
    return (q[0]-p[0])*(q[1]-p[1])


def positive_scale(scale):
    if not math.isfinite(scale) or scale<=0:
        raise ValueError('Positive finite scale required')


def flat_volume(p,q,scale=1.):
    positive_scale(scale)
    du,dv=rectangle(p,q)
    return scale*scale*du*dv/2


def quadratic_density(u,v,a=1.,b=.2,c=.3):
    if not all(math.isfinite(x) for x in (u,v,a,b,c)) or a<=0 or b<0 or c<0:
        raise ValueError('Positive A and nonnegative B,C required for global positive density')
    return a+b*u*u+c*v*v


def quadratic_volume(p,q,a=1.,b=.2,c=.3):
    du,dv=rectangle(p,q)
    quadratic_density(0,0,a,b,c)
    mean_u2=(p[0]**2+p[0]*q[0]+q[0]**2)/3
    mean_v2=(p[1]**2+p[1]*q[1]+q[1]**2)/3
    return du*dv*(a+b*mean_u2+c*mean_v2)/2


def quadratic_curvature(u,v,a=1.,b=.2,c=.3):
    # Convention: R = -8 exp(-2 sigma) partial_u partial_v sigma.
    density=quadratic_density(u,v,a,b,c)
    return 16*b*c*u*v/density**3


def averaged_density(volume,half_u,half_v):
    positive_scale(half_u); positive_scale(half_v)
    return volume/(2*half_u*half_v)


def reconstruct_quadratic(mean_00,mean_d0,mean_0d,half_width,offset):
    """Exactly identified only within the declared three-parameter family."""
    positive_scale(half_width); positive_scale(offset)
    b=(mean_d0-mean_00)/offset**2
    c=(mean_0d-mean_00)/offset**2
    a=mean_00-(b+c)*half_width**2/3
    return a,b,c


def sine_density(u,v,epsilon=.2):
    if not math.isfinite(epsilon) or abs(epsilon)>=1:
        raise ValueError('Require |epsilon| < 1')
    return 1+epsilon*math.sin(2*math.pi*u)*math.sin(2*math.pi*v)


def sine_volume(p,q,epsilon=.2):
    du,dv=rectangle(p,q)
    sine_density(0,0,epsilon)
    su=(math.cos(2*math.pi*p[0])-math.cos(2*math.pi*q[0]))/(2*math.pi)
    sv=(math.cos(2*math.pi*p[1])-math.cos(2*math.pi*q[1]))/(2*math.pi)
    return (du*dv+epsilon*su*sv)/2


def sine_curvature(u,v,epsilon=.2):
    d=sine_density(u,v,epsilon); k=2*math.pi
    du=epsilon*k*math.cos(k*u)*math.sin(k*v)
    dv=epsilon*k*math.sin(k*u)*math.cos(k*v)
    duv=epsilon*k*k*math.cos(k*u)*math.cos(k*v)
    return -4*(d*duv-du*dv)/d**3


def poisson_probability(count,density,volume):
    if not isinstance(count,int) or count<0 or not all(math.isfinite(x) and x>0 for x in (density,volume)):
        raise ValueError('Nonnegative integer count and positive finite density/volume required')
    mean=density*volume
    return math.exp(-mean+count*math.log(mean)-math.lgamma(count+1))


def projection_intertwiner(old,new):
    """Two-dimensional fibre example: state covariance without localization."""
    old_minus=vac.occupied_spinor(old); new_minus=vac.occupied_spinor(new)
    old_plus=vac.occupied_spinor(w.add(w.I,w.scale(-1,old)))
    new_plus=vac.occupied_spinor(w.add(w.I,w.scale(-1,new)))
    return tuple(tuple(new_minus[i]*complex(old_minus[j]).conjugate()+new_plus[i]*complex(old_plus[j]).conjugate()
                       for j in range(2)) for i in range(2))
