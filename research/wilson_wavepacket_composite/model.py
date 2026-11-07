"""A rank-one positive-energy excitation; spatially varying and nonstationary."""
import cmath
import math
import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location('wavepacket_wilson_reference',Path(__file__).resolve().parents[1]/'wilson_thermal_composite'/'model.py')
w=importlib.util.module_from_spec(s);s.loader.exec_module(w)
LOW,HIGH=1.,3.
# f(k)=sqrt(15) (k-1)(3-k)/4 on [1,3], with integral |f|^2 dk=1.
def amplitude(k):return math.sqrt(15)*(k-1)*(3-k)/4 if LOW<=k<=HIGH else 0.

def integral(f,steps=800):return w.simpson(lambda z:f(LOW+z),HIGH-LOW,steps)

def validate(a,weight=1.):
    if not math.isfinite(a) or a<=0 or a*HIGH>=math.pi or not math.isfinite(weight) or not 0<=weight<=1:
        raise ValueError('Require positive spacing with a*HIGH<pi and 0<=weight<=1')

def packet(x,t=0.,a=None,derivative=0,component=0,steps=800):
    if not math.isfinite(x) or not math.isfinite(t) or not isinstance(derivative,int) or derivative<0 or component not in (0,1):raise ValueError('Invalid packet argument')
    if a is not None:validate(a)
    def f(k):
        spin=(math.cos(a*k/4) if component==0 else math.sin(a*k/4)) if a is not None else (1 if component==0 else 0)
        energy=2*math.sin(a*k/2)/a if a is not None else k
        return amplitude(k)*spin*(1j*k)**derivative*cmath.exp(1j*(k*x-energy*t))
    return integral(f,steps)/math.sqrt(2*math.pi)

def B(j):return integral(lambda k:amplitude(k)*k**j)/math.sqrt(2*math.pi)
def D(j,t):return B(j+2)/32+abs(t)*B(j+3)/24

def target(x,t=0.,weight=1.):
    validate(.1,weight)
    return weight*(packet(x,t).conjugate()*packet(x,t,derivative=1)).imag

def current(a,n,x,t=0.,weight=1.):
    validate(a,weight);w.parameters(a,n,1);h=a*n
    plus=packet(x+h/2,t,a);minus=packet(x-h/2,t,a)
    return weight*w.shape(n)*(minus.conjugate()*plus).imag/h

def error_bound(a,n,t=0.,weight=1.):
    validate(a,weight);w.parameters(a,n,1);h=a*n
    k=B(0)*B(3)/24+B(1)*B(2)/8
    return weight*(w.shape(n)*(h*h*k+a*a*(D(0,t)*B(1)+B(0)*D(1,t)))+(w.shape(n)-1)*B(0)*B(1))

def covariance(a,n,x,t=0.,weight=1.):
    validate(a,weight);w.parameters(a,n,1);h=a*n
    # Row coordinates x+h/2, x-h/2; covariance is <c_j^* c_i>.
    v=(packet(x+h/2,t,a),packet(x-h/2,t,a))
    base=w.same_chirality_covariance(a,n)
    return tuple(tuple(base[i][j]+weight*a*v[i]*v[j].conjugate() for j in range(2)) for i in range(2))

def local_energy(a,x,t=0.,weight=1.):
    """Symmetrized one-particle spectral energy density, both spin components."""
    validate(a,weight)
    total=0.
    for c in (0,1):
        v=packet(x,t,a,component=c)
        hv=integral(lambda k:amplitude(k)*(math.cos(a*k/4) if c==0 else math.sin(a*k/4))*(2*math.sin(a*k/2)/a)*cmath.exp(1j*(k*x-2*math.sin(a*k/2)*t/a)))/math.sqrt(2*math.pi)
        total+=(v.conjugate()*hv).real
    return weight*total

def total_energy(a=None,weight=1.):
    validate(a if a is not None else .1,weight)
    return weight*integral(lambda k:amplitude(k)**2*(2*math.sin(a*k/2)/a if a is not None else k))


def eigenvalues(cov):
    u,v=cov[0][0].real,cov[1][1].real
    gap=math.sqrt((u-v)**2+4*abs(cov[0][1])**2)
    return ((u+v-gap)/2,(u+v+gap)/2)


def density_matrix(cov):
    """General gauge-invariant two-mode density; not restricted to half filling."""
    if any(z< -1e-12 or z>1+1e-12 for z in eigenvalues(cov)):raise ValueError('Positive contraction required')
    u,v=cov[0][0].real,cov[1][1].real;z=cov[0][1];d=u*v-abs(z)**2
    return {(0,0):complex(1-u-v+d),(1,1):complex(u-d),(2,2):complex(v-d),(3,3):complex(d),(1,2):z,(2,1):z.conjugate()}
