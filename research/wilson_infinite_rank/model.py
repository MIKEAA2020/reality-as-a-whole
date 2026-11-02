"""Trace-class infinite-rank positive-energy packets on disjoint compact bands.
Numerical values truncate modes; explicit bounds control the omitted local tail.
"""
import cmath
import math
import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location('finite_rank_reference',Path(__file__).resolve().parents[1]/'wilson_multimode_composite'/'model.py')
r=importlib.util.module_from_spec(s);s.loader.exec_module(r)
w=r.w


def validate(a,n,count):
    w.parameters(a,n,1.)
    if a*2>=math.pi or not isinstance(count,int) or not 1<=count<=128:
        raise ValueError('Require 2a<pi and numerical mode count in [1,128]')


def band(i):
    if not isinstance(i,int) or not 0<=i<=127:raise ValueError('Numerical index in [0,127] required')
    width=2.**(-i-1)
    return 1+width,width


def occupation(i):return band(i)[1]


def packet(i,x,t=0.,a=None,j=0,steps=200):
    low,width=band(i)
    if a is not None:validate(a,1,1)
    if not math.isfinite(x) or not math.isfinite(t) or not isinstance(j,int) or j<0:raise ValueError('Invalid position, time, or derivative')
    # Integrate on a fixed unit interval: no small-width cancellation.
    def integrand(z):
        k=low+width*z
        energy=2*math.sin(a*k/2)/a if a is not None else k
        spin=math.cos(a*k/4) if a is not None else 1.
        return math.sqrt(30*width)*z*(1-z)*spin*(1j*k)**j*cmath.exp(1j*(k*x-energy*t))
    return w.simpson(integrand,1.,steps)/math.sqrt(2*math.pi)


def B(i,j):
    low,width=band(i)
    return math.sqrt(30*width/(2*math.pi))*sum(math.comb(j,k)*low**(j-k)*width**k/((k+2)*(k+3)) for k in range(j+1))


def target(x,t=0.,count=16):
    validate(.1,1,count)
    return sum(occupation(i)*(packet(i,x,t).conjugate()*packet(i,x,t,j=1)).imag for i in range(count))


def terms(a,n,x,t=0.,count=16):
    validate(a,n,count);h=a*n
    values=[(packet(i,x+h/2,t,a),packet(i,x-h/2,t,a)) for i in range(count)]
    linear=w.shape(n)*sum(occupation(i)*(minus.conjugate()*plus).imag/h for i,(plus,minus) in enumerate(values))
    gram=math.pi*sum(occupation(i)*occupation(j)*abs(values[i][0]*values[j][1]-values[j][0]*values[i][1])**2 for i in range(count) for j in range(i))
    return linear,gram


def current(a,n,x,t=0.,count=16):return sum(terms(a,n,x,t,count))


def tail_moment(N,j):
    """Bound on sum_{i>=N} lambda_i B_i,0 B_i,j, also cross powers."""
    if not isinstance(N,int) or N<0 or not isinstance(j,int) or j<0:raise ValueError('Nonnegative integer cutoff and moment required')
    return 2.**j*4.**(-N)/(6*math.pi)


def tail_bound(a,n,count):
    validate(a,n,count);h=a*n
    return w.shape(n)*tail_moment(count,1)+2*math.pi*h*h*(tail_moment(count,0)*tail_moment(0,2)+tail_moment(0,0)*tail_moment(count,2))


def target_tail(count):return tail_moment(count,1)


def error_bound(a,n,t=0.):
    """Whole infinite-rank lattice current versus whole continuum target."""
    validate(a,n,1);h=a*n
    # sum lambda B_j B_k <= 2^(j+k)/(6pi)
    M=lambda j:tail_moment(0,j)
    Q=M(3)*(1/24+1/8)
    dispersion=M(3)/16+abs(t)*M(4)/12
    gram=2*math.pi*h*h*M(0)*M(2)
    return w.shape(n)*(h*h*Q+a*a*dispersion)+(w.shape(n)-1)*M(1)+gram


def kernel(a,x,y,t=0.,count=16):
    validate(a,1,count)
    return sum(occupation(i)*packet(i,x,t,a)*packet(i,y,t,a).conjugate() for i in range(count))


def covariance(a,n,x,t=0.,count=16):
    validate(a,n,count);sites=(x+a*n/2,x-a*n/2);base=w.same_chirality_covariance(a,n)
    return tuple(tuple(base[i][j]+a*kernel(a,sites[i],sites[j],t,count) for j in range(2)) for i in range(2))


def particle_number(count):return 1-2.**(-count)

def total_energy(count=16):
    validate(.1,1,count)
    return sum(occupation(i)*(1+1.5*band(i)[1]) for i in range(count))


def wilson_energy(a,count=16):
    """Independent integrated spectral Hamiltonian energy, truncated in modes."""
    validate(a,1,count)
    total=0.
    for i in range(count):
        low,width=band(i)
        total+=occupation(i)*w.simpson(lambda z:30*z*z*(1-z)**2*2*math.sin(a*(low+width*z)/2)/a,1.,400)
    return total
