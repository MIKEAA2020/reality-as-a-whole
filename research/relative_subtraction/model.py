"""A common-regulator limit for relative massless conformal stress.

This is continuum point splitting, not a Wilson lattice stress theorem. Exact
cubic remainders avoid catastrophic subtraction. The unsafe cutoff example
intentionally uses different physical cutoff scales in two coordinate charts.
"""
from decimal import Decimal as D, localcontext
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('conformal_stress_reference',Path(__file__).resolve().parents[1]/'conformal_stress'/'model.py')
previous=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(previous)


def parameters(alpha,u):
    if not math.isfinite(alpha) or alpha<0 or not math.isfinite(u):
        raise ValueError('Nonnegative finite alpha and finite midpoint required')


def remainder(alpha,u,separation):
    """D_f-D_id for f(u)=u+alpha*u^3, extended continuously to zero."""
    parameters(alpha,u)
    z=separation; a=1+3*alpha*u*u
    denominator=a+alpha*z*z/4
    if denominator==0:
        raise ValueError('Outside the analytic point-splitting domain')
    return (alpha-6*alpha*alpha*u*u+alpha*alpha*z*z/2)/denominator**2


def quadratic_bound(alpha,u,radius=1.):
    """|F(z)-F(0)| <= C |z|^2 for |z|<=radius, real or complex."""
    parameters(alpha,u)
    if not math.isfinite(radius) or radius<=0:
        raise ValueError('Positive finite bound radius required')
    a=1+3*alpha*u*u; b=alpha/4; n0=alpha-6*alpha*alpha*u*u; n2=alpha*alpha/2
    if a<=b*radius*radius:
        raise ValueError('Radius reaches a possible complex denominator zero')
    return (n2*a*a+2*abs(n0)*a*b+abs(n0)*b*b*radius*radius)/(a*a*(a-b*radius*radius)**2)


def analytic_regulator(alpha,u,h,epsilon):
    if h<0 or epsilon<0 or not math.isfinite(h) or not math.isfinite(epsilon):
        raise ValueError('Nonnegative finite separation and regulator required')
    return remainder(alpha,u,complex(h,-epsilon))


def mollifier_samples(steps=400,variant=0):
    if not isinstance(steps,int) or steps<2 or variant not in (0,1):
        raise ValueError('At least two quadrature cells and a supported smooth kernel required')
    samples=[]
    for j in range(steps):
        s=-1+(j+.5)*2/steps
        weight=math.exp(-1/(1-s*s))*(1+s*s if variant else 1)
        samples.append((s,weight))
    total=sum(weight for _,weight in samples)
    return tuple((s,weight/total) for s,weight in samples)


def mollify(alpha,u,h,epsilon,steps=400,variant=0):
    if epsilon<0 or h<0 or not math.isfinite(h) or not math.isfinite(epsilon):
        raise ValueError('Nonnegative finite separation and regulator required')
    return sum(weight*remainder(alpha,u,h-epsilon*s) for s,weight in mollifier_samples(steps,variant))


def mollify_separately_off_diagonal(alpha,u,h,epsilon,steps=100):
    """Finite smooth off-diagonal quadrature of both kernels, then subtraction.

    Crossing coincidence requires distributional pairing, not this sample code.
    The smooth-remainder algorithm `mollify` has no such restriction.
    """
    if not h>epsilon>=0:
        raise ValueError('Off-diagonal quadrature requires h>epsilon>=0')
    with localcontext() as ctx:
        ctx.prec=80
        f=previous.cubic(str(alpha)); midpoint=D(str(u)); h,epsilon=D(str(h)),D(str(epsilon))
        first=second=norm=D(0)
        for s,weight in mollifier_samples(steps):
            s,weight=D(str(s)),D(str(weight)); separation=h-epsilon*s
            left,lf,_,_=f(midpoint-separation/2); right,rf,_,_=f(midpoint+separation/2)
            first+=weight*lf*rf/(right-left)**2
            second+=weight/separation**2
            norm+=weight
        return float((first-second)/norm)


def naive_affine_real(scale,h,epsilon):
    """Wrong matching: same epsilon in target and reference coordinate lengths."""
    with localcontext() as ctx:
        ctx.prec=80
        a,h,e=map(lambda x:D(str(x)),(scale,h,epsilon))
        if a<=0 or h<0 or e<=0:
            raise ValueError('Positive scale/epsilon and nonnegative separation required')
        def real_inverse_square(x,y):
            return (x*x-y*y)/(x*x+y*y)**2
        return +(a*a*real_inverse_square(a*h,e)-real_inverse_square(h,e))


def matched_affine_real(scale,h,epsilon):
    with localcontext() as ctx:
        ctx.prec=80
        a,h,e=map(lambda x:D(str(x)),(scale,h,epsilon))
        if a<=0 or h<0 or e<=0:
            raise ValueError('Positive scale/epsilon and nonnegative separation required')
        def real_inverse_square(x,y):
            return (x*x-y*y)/(x*x+y*y)**2
        return +(a*a*real_inverse_square(a*h,a*e)-real_inverse_square(h,e))


def relative_stress(alpha,u,h=0.,epsilon=0.,variant=0):
    return -mollify(alpha,u,h,epsilon,variant=variant)/(4*math.pi)
