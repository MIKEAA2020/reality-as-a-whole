"""Unbounded continuum momentum support with summable excitation moments.
The actual Wilson state retains whole bands with a*(N+1)<=1.
"""
import cmath
import math
import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location('infinite_rank_reference',Path(__file__).resolve().parents[1]/'wilson_infinite_rank'/'model.py')
r=importlib.util.module_from_spec(s);s.loader.exec_module(r)
w=r.w
RAW=(1,3,11,51,299)


def validate(a,n,count):
    w.parameters(a,n,1.)
    if not isinstance(count,int) or not 1<=count<=256 or a*(count+1)>1:
        raise ValueError('Numerical count in [1,256] and a*(count+1)<=1 required')


def occupation(i):
    if not isinstance(i,int) or i<0:raise ValueError('Nonnegative integer mode index required')
    return 2.**(-i-1)


def packet(i,x,t=0.,a=None,j=0,component=0,steps=400):
    occupation(i)
    if a is not None:validate(a,1,i+1)
    if not math.isfinite(x) or not math.isfinite(t) or not isinstance(j,int) or j<0 or component not in (0,1):raise ValueError('Invalid packet arguments')
    def f(z):
        k=i+1+z
        spin=(math.cos(a*k/4) if component==0 else math.sin(a*k/4)) if a is not None else (1 if component==0 else 0)
        e=2*math.sin(a*k/2)/a if a is not None else k
        return math.sqrt(30)*z*(1-z)*spin*(1j*k)**j*cmath.exp(1j*(k*x-e*t))
    return w.simpson(f,1.,steps)/math.sqrt(2*math.pi)


def S(q):
    if not isinstance(q,int) or not 0<=q<=4:raise ValueError('Moment order in [0,4] required')
    return RAW[q]/(2*math.pi)


def target(x,t=0.,count=40):
    if not isinstance(count,int) or not 1<=count<=256:raise ValueError('Numerical count in [1,256] required')
    return sum(occupation(i)*(packet(i,x,t).conjugate()*packet(i,x,t,j=1)).imag for i in range(count))


def target_tail(count):
    if not isinstance(count,int) or count<0:raise ValueError('Nonnegative integer cutoff required')
    return 2.**(-count)*(count+3)/(2*math.pi)


def terms(a,n,x,t=0.,count=8):
    validate(a,n,count);h=a*n
    v=[(packet(i,x+h/2,t,a),packet(i,x-h/2,t,a)) for i in range(count)]
    linear=w.shape(n)*sum(occupation(i)*(minus.conjugate()*plus).imag/h for i,(plus,minus) in enumerate(v))
    gram=math.pi*sum(occupation(i)*occupation(j)*abs(v[i][0]*v[j][1]-v[j][0]*v[i][1])**2 for i in range(count) for j in range(i))
    return linear,gram


def current(a,n,x,t=0.,count=8):return sum(terms(a,n,x,t,count))


def error_bound(a,n,t=0.,count=8):
    validate(a,n,count);h=a*n
    finite=w.shape(n)*(h*h*S(3)/6+a*a*(S(3)/16+abs(t)*S(4)/12))+(w.shape(n)-1)*S(1)+2*math.pi*h*h*S(0)*S(2)
    return finite+target_tail(count)


def covariance(a,n,x,t=0.,count=8):
    validate(a,n,count);sites=(x+a*n/2,x-a*n/2);base=w.same_chirality_covariance(a,n)
    return tuple(tuple(base[i][j]+a*sum(occupation(k)*packet(k,sites[i],t,a)*packet(k,sites[j],t,a).conjugate() for k in range(count)) for j in range(2)) for i in range(2))


def total_energy(count=40):
    if not isinstance(count,int) or not 1<=count<=256:raise ValueError('Numerical count in [1,256] required')
    return sum(occupation(i)*(i+1.5) for i in range(count))


def wilson_energy(a,count=8):
    validate(a,1,count)
    return sum(occupation(i)*w.simpson(lambda z:30*z*z*(1-z)**2*(2*math.sin(a*(i+1+z)/2)/a),1.,800) for i in range(count))


def energy_bound(a,count=8):
    validate(a,1,count)
    return a*a*RAW[3]/24+2.**(-count)*(count+3)


def local_energy(a,x,t=0.,count=8):
    validate(a,1,count);total=0.
    for i in range(count):
        for c in (0,1):
            def f(z):
                k=i+1+z;e=2*math.sin(a*k/2)/a
                spin=math.cos(a*k/4) if c==0 else math.sin(a*k/4)
                return math.sqrt(30)*z*(1-z)*spin*e*cmath.exp(1j*(k*x-e*t))
            hv=w.simpson(f,1.,400)/math.sqrt(2*math.pi)
            total+=occupation(i)*(packet(i,x,t,a,component=c).conjugate()*hv).real
    return total
