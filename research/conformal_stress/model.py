"""Massless conformal Dirac stress EXPECTATIONS in a stated Ward prescription.

Not the massive lattice stress tensor. The central charge and locally covariant
anomaly prescription are declared physical/renormalization inputs in REPORT.md.
Decimal arithmetic controls the singular-kernel subtraction diagnostics.
"""
from decimal import Decimal as D, localcontext
import math


def decimal(x):
    return x if isinstance(x,D) else D(str(x))


def cubic(alpha):
    a=decimal(alpha)
    if a<0:
        raise ValueError('Nonnegative cubic coefficient required')
    def jets(x):
        x=decimal(x)
        return x+a*x**3,1+3*a*x*x,6*a*x,6*a
    return jets


def affine(scale=1,shift=0):
    a,b=decimal(scale),decimal(shift)
    if a<=0:
        raise ValueError('Increasing map required')
    return lambda x:(a*decimal(x)+b,a,D(0),D(0))


def exponential(kappa):
    k=decimal(kappa)
    if k<=0:
        raise ValueError('Positive exponential rate required')
    def jets(x):
        e=(k*decimal(x)).exp()
        return e/k,e,k*e,k*k*e
    return jets


def mobius(a=1,b=0,c=1,d=1):
    a,b,c,d=map(decimal,(a,b,c,d)); determinant=a*d-b*c
    if determinant<=0:
        raise ValueError('Positive Mobius determinant required')
    def jets(x):
        den=c*decimal(x)+d
        if den==0:
            raise ValueError('Map pole is outside the source chart')
        return (a*decimal(x)+b)/den,determinant/den**2,-2*c*determinant/den**3,6*c*c*determinant/den**4
    return jets


def schwarzian(jets):
    _,first,second,third=jets
    if first<=0:
        raise ValueError('Positive derivative required')
    return third/first-D('1.5')*(second/first)**2


def compose_jets(f,g,x):
    y,g1,g2,g3=g(x); z,f1,f2,f3=f(y)
    return z,f1*g1,f2*g1*g1+f1*g2,f3*g1**3+3*f2*g1*g2+f1*g3


def split_finite_kernel(f,x,separation,precision=80):
    with localcontext() as ctx:
        ctx.prec=precision
        x,h=decimal(x),decimal(separation)
        if h<=0:
            raise ValueError('Positive point separation required')
        left,lf,_,_=f(x-h/2); right,rf,_,_=f(x+h/2)
        return +(lf*rf/(left-right)**2-1/h**2)


def split_stress(f,x,separation,central_charge=1.):
    return -central_charge*float(split_finite_kernel(f,x,separation))/(4*math.pi)


def state_stress(f,x,central_charge=1.):
    with localcontext() as ctx:
        ctx.prec=80
        return -central_charge*float(schwarzian(f(decimal(x))))/(24*math.pi)


def flat_jet():
    return dict(sigma=0.,u=0.,v=0.,uu=0.,uv=0.,vv=0.,uuv=0.,uvv=0.)


def static_jet(x,epsilon=.2,q=1.):
    if abs(epsilon)>=1 or q<=0 or not all(math.isfinite(y) for y in (x,epsilon,q)):
        raise ValueError('Smooth positive static metric parameters required')
    om=1+epsilon*math.cos(q*x)
    d1=-epsilon*q*math.sin(q*x); d2=-epsilon*q*q*math.cos(q*x); d3=epsilon*q**3*math.sin(q*x)
    s1=d1/om; s2=d2/om-s1*s1; s3=d3/om-3*d1*d2/om**2+2*d1**3/om**3
    return dict(sigma=math.log(om),u=s1/2,v=-s1/2,uu=s2/4,uv=-s2/4,vv=s2/4,uuv=-s3/8,uvv=s3/8)


def affine_density_jet(u,v,a=1.,b=1/3,c=1/2):
    rho=a+b*u+c*v
    if rho<=0:
        raise ValueError('Positive density required')
    return dict(sigma=.5*math.log(2*rho),u=b/(2*rho),v=c/(2*rho),uu=-b*b/(2*rho*rho),uv=-b*c/(2*rho*rho),vv=-c*c/(2*rho*rho),uuv=b*b*c/rho**3,uvv=b*c*c/rho**3)


def curvature(jet):
    return -8*math.exp(-2*jet['sigma'])*jet['uv']


def stress(jet,tu=0.,tv=0.,central_charge=1.,cosmological=0.):
    a=central_charge/(12*math.pi)
    return (a*(jet['uu']-jet['u']**2)+tu,
            -a*jet['uv']+cosmological*math.exp(2*jet['sigma'])/2,
            a*(jet['vv']-jet['v']**2)+tv)


def trace(jet,tensor):
    return 4*math.exp(-2*jet['sigma'])*tensor[1]


def ward_residuals(jet,central_charge=1.,cosmological=0.,tu_v=0.,tv_u=0.):
    a=central_charge/(12*math.pi); su,sv=jet['u'],jet['v']; uv=jet['uv']
    tuv=stress(jet,central_charge=central_charge,cosmological=cosmological)[1]
    du_tuv=-a*jet['uuv']+cosmological*math.exp(2*jet['sigma'])*su
    dv_tuv=-a*jet['uvv']+cosmological*math.exp(2*jet['sigma'])*sv
    return (a*(jet['uuv']-2*su*uv)+tu_v+du_tuv-2*su*tuv,
            a*(jet['uvv']-2*sv*uv)+tv_u+dv_tuv-2*sv*tuv)


def reparametrize_jet(jet,fjets,gjets):
    _,f1,f2,f3=map(float,fjets); _,g1,g2,g3=map(float,gjets)
    if f1<=0 or g1<=0:
        raise ValueError('Increasing null-coordinate charts required')
    return dict(sigma=jet['sigma']-.5*math.log(f1*g1),
                u=(jet['u']-.5*f2/f1)/f1,v=(jet['v']-.5*g2/g1)/g1,
                uu=(jet['uu']-(f2/f1)*jet['u']-.5*f3/f1+(f2/f1)**2)/f1**2,
                uv=jet['uv']/(f1*g1),
                vv=(jet['vv']-(g2/g1)*jet['v']-.5*g3/g1+(g2/g1)**2)/g1**2)
