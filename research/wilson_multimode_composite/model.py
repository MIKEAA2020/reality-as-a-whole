"""Two orthonormal positive-energy packets; finite-rank local composite control."""
import math
import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location('rank_one_reference',Path(__file__).resolve().parents[1]/'wilson_wavepacket_composite'/'model.py')
p=importlib.util.module_from_spec(s);s.loader.exec_module(p)
w=p.w


def weights(values):
    if len(values)!=2 or any(not math.isfinite(v) or not 0<=v<=1 for v in values):
        raise ValueError('Two occupations in [0,1] required')


def amplitude(k,mode):
    if mode not in (0,1):raise ValueError('Two packet modes available')
    return p.amplitude(k)*(1 if mode==0 else math.sqrt(7)*(k-2))


def packet(mode,x,t=0.,a=None,derivative=0,component=0):
    if mode==0:return p.packet(x,t,a,derivative,component)
    if mode!=1:raise ValueError('Two packet modes available')
    return math.sqrt(7)*(-1j*p.packet(x,t,a,derivative+1,component)-2*p.packet(x,t,a,derivative,component))


def B(mode,j):
    # Split at the absolute-value cusp k=2.
    return sum(w.simpson(lambda z:abs(amplitude(base+z,mode))*(base+z)**j,1.,800) for base in (1.,2.))/math.sqrt(2*math.pi)


def D(mode,j,t):return B(mode,j+2)/32+abs(t)*B(mode,j+3)/24


def kernel(x,y,t=0.,a=None,occupations=(1.,1.)):
    weights(occupations)
    return sum(v*packet(i,x,t,a)*packet(i,y,t,a).conjugate() for i,v in enumerate(occupations))


def terms(a,n,x,t=0.,occupations=(1.,1.)):
    weights(occupations);p.validate(a);w.parameters(a,n,1);h=a*n
    plus,minus=x+h/2,x-h/2
    linear=w.shape(n)*sum(v*(packet(i,minus,t,a).conjugate()*packet(i,plus,t,a)).imag/h for i,v in enumerate(occupations))
    wedge=packet(0,plus,t,a)*packet(1,minus,t,a)-packet(1,plus,t,a)*packet(0,minus,t,a)
    exchange=math.pi*occupations[0]*occupations[1]*abs(wedge)**2
    return linear,exchange


def current(a,n,x,t=0.,occupations=(1.,1.)):return sum(terms(a,n,x,t,occupations))


def target(x,t=0.,occupations=(1.,1.)):
    weights(occupations)
    return sum(v*(packet(i,x,t).conjugate()*packet(i,x,t,derivative=1)).imag for i,v in enumerate(occupations))


def exchange_bound(a,n,occupations=(1.,1.)):
    weights(occupations);p.validate(a);w.parameters(a,n,1)
    return math.pi*occupations[0]*occupations[1]*(a*n)**2*(B(0,0)*B(1,1)+B(1,0)*B(0,1))**2


def error_bound(a,n,t=0.,occupations=(1.,1.)):
    weights(occupations);p.validate(a);w.parameters(a,n,1);h=a*n;total=exchange_bound(a,n,occupations)
    for i,v in enumerate(occupations):
        k=B(i,0)*B(i,3)/24+B(i,1)*B(i,2)/8
        total+=v*(w.shape(n)*(h*h*k+a*a*(D(i,0,t)*B(i,1)+B(i,0)*D(i,1,t)))+(w.shape(n)-1)*B(i,0)*B(i,1))
    return total


def covariance(a,n,x,t=0.,occupations=(1.,1.)):
    weights(occupations);p.validate(a);w.parameters(a,n,1);h=a*n;sites=(x+h/2,x-h/2);base=w.same_chirality_covariance(a,n)
    return tuple(tuple(base[i][j]+a*kernel(sites[i],sites[j],t,a,occupations) for j in range(2)) for i in range(2))


def local_energy(a,x,t=0.,occupations=(1.,1.)):
    weights(occupations);p.validate(a);total=0.
    import cmath
    for i,v in enumerate(occupations):
        for c in (0,1):
            hv=p.integral(lambda k:amplitude(k,i)*(math.cos(a*k/4) if c==0 else math.sin(a*k/4))*(2*math.sin(a*k/2)/a)*cmath.exp(1j*(k*x-2*math.sin(a*k/2)*t/a)))/math.sqrt(2*math.pi)
            total+=v*(packet(i,x,t,a,component=c).conjugate()*hv).real
    return total
