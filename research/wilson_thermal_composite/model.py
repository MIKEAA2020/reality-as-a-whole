"""Massless Wilson Hamiltonian thermal composites on the infinite lattice.

Covariances come from the Hamiltonian Fermi function, not imported continuum
states. Exact integral formulas and error arguments are in REPORT.md. Numerical
integrals truncate only exponentially small thermal tails, stated separately.
"""
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('cell_current_reference',Path(__file__).resolve().parents[1]/'cell_current_limit'/'model.py')
cell=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(cell)
car,previous=cell.car,cell.previous


def parameters(a,n,beta):
    if not math.isfinite(a) or a<=0 or not isinstance(n,int) or n<1 or not math.isfinite(beta) or beta<=0:
        raise ValueError('Positive spacing, integer separation n>=1, and positive inverse temperature required')


def shape(n):
    parameters(1.,n,1.)
    return n*n/(n*n-.25)


def energy(theta,a):
    parameters(a,1,1.)
    if not math.isfinite(theta):raise ValueError('Finite momentum angle required')
    return 2*abs(math.sin(theta/2))/a


def fermi_tail(p,beta):
    if p<0 or beta<=0 or not math.isfinite(p) or not math.isfinite(beta):
        raise ValueError('Nonnegative finite energy and positive finite inverse temperature required')
    x=math.exp(-beta*p)
    return 2*x/(1+x)


def simpson(function,upper,steps=800):
    if not isinstance(steps,int) or steps<2 or steps%2 or upper<0:
        raise ValueError('Even Simpson count >=2 and nonnegative endpoint required')
    h=upper/steps
    return h/3*(function(0)+function(upper)+sum((4 if j%2 else 2)*function(j*h) for j in range(1,steps)))


def qmomentum(p,a):
    return 2*math.asin(min(1,a*p/2))/a


def thermal_ratio(a,n,beta=2.5,steps=800):
    """delta-kappa/h, with the h factor removed before integration."""
    parameters(a,n,beta)
    h=n*a; upper=min(1/a,40/beta)
    def integrand(p):
        q=qmomentum(p,a); z=h*q
        sinc=math.sin(z)/z if z else 1.
        return -q*sinc*fermi_tail(p,beta)
    return simpson(integrand,upper,steps)


def cross_ratio(a,n,beta=2.5,steps=800):
    """delta C_up,down / a^2; same exponentially controlled low-energy truncation."""
    parameters(a,n,beta)
    h=n*a; upper=min(1/a,40/beta)
    def integrand(p):
        return p*math.cos(h*qmomentum(p,a))*fermi_tail(p,beta)/math.sqrt(1-(a*p/2)**2)
    return simpson(integrand,upper,steps)/(4*math.pi)


def moment1(beta):
    if not math.isfinite(beta) or beta<=0:raise ValueError('Positive finite beta required')
    return math.pi**2/(6*beta**2)


def moment3(beta):
    moment1(beta)
    return 7*math.pi**4/(60*beta**4)


def target(beta=2.5):
    return moment1(beta)/(2*math.pi)


def same_chirality_covariance(a,n,beta=None,steps=800):
    parameters(a,n,beta if beta is not None else 1.)
    r=thermal_ratio(a,n,beta,steps) if beta is not None else 0.
    kappa=shape(n)/(n*a)+(n*a)*r
    off=-1j*a*kappa/(2*math.pi)
    return ((.5+0j,off),(off.conjugate(),.5+0j))


def mixed_covariance(a,n,beta=None,steps=800):
    parameters(a,n,beta if beta is not None else 1.)
    off=1/(4*math.pi*(n*n-.25))
    if beta is not None:off+=a*a*cross_ratio(a,n,beta,steps)
    return ((.5+0j,complex(off)),(complex(off),.5+0j))


def current_stress(a,n,beta=2.5,steps=800,calibrated=False):
    parameters(a,n,beta)
    h=n*a; r=thermal_ratio(a,n,beta,steps)
    answer=-(2*shape(n)*r+h*h*r*r)/(4*math.pi)
    return answer/shape(n) if calibrated else answer


def mixed_current(a,n,beta=2.5,steps=800):
    base=1/(4*math.pi*(n*n-.25)); r=cross_ratio(a,n,beta,steps)
    return -math.pi*(2*base*r+a*a*r*r)


def thermal_energy_density(a,beta=2.5,steps=800):
    """Thermal-minus-ground Hamiltonian energy per coordinate length."""
    parameters(a,1,beta); upper=min(1/a,40/beta)
    return simpson(lambda p:p*fermi_tail(p,beta)/math.sqrt(1-(a*p/2)**2),upper,steps)/math.pi


def ratio_bound(a,n,beta=2.5):
    parameters(a,n,beta)
    h=n*a
    tail=2*math.exp(-beta/a)*(1/(a*beta)+1/beta**2)
    return (math.pi**3*h*h/48+a*a/12)*moment3(beta)+(1+math.pi/2)*tail


def current_error_bound(a,n,beta=2.5):
    h=n*a; i1=moment1(beta)
    return shape(n)*ratio_bound(a,n,beta)/(2*math.pi)+h*h*(math.pi*i1/2)**2/(4*math.pi)


def omitted_ratio_tail(a,beta=2.5):
    """Bound for thermal_ratio after truncating at min(1/a,40/beta)."""
    parameters(a,1,beta); k=min(1/a,40/beta)
    return math.pi*math.exp(-beta*k)*(k/beta+1/beta**2)
