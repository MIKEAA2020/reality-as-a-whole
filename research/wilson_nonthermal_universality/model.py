"""Stationary quasifree, compact-energy excitations of the Wilson ground state."""
import importlib.util
import math
from pathlib import Path
s=importlib.util.spec_from_file_location('wilson_thermal_reference',Path(__file__).resolve().parents[1]/'wilson_thermal_composite'/'model.py')
w=importlib.util.module_from_spec(s); s.loader.exec_module(w)


def validate(amplitude, cutoff):
    if not math.isfinite(amplitude) or not 0<=amplitude<=.5 or not math.isfinite(cutoff) or cutoff<=0:
        raise ValueError('Require 0<=amplitude<=1/2 and finite positive energy cutoff')


def occupation(p, amplitude=.5, cutoff=1.):
    validate(amplitude,cutoff)
    if not math.isfinite(p) or p<0: raise ValueError('Nonnegative finite energy required')
    return amplitude*max(0,1-p/cutoff)


def moment(k,amplitude=.5,cutoff=1.):
    validate(amplitude,cutoff)
    if not isinstance(k,int) or k<0: raise ValueError('Nonnegative integer moment required')
    return 2*amplitude*cutoff**(k+1)/((k+1)*(k+2))


def parameters(a,n,amplitude,cutoff):
    w.parameters(a,n,1); validate(amplitude,cutoff)
    if a*cutoff>1: raise ValueError('This controlled low-energy family requires a*cutoff<=1')


def ratios(a,n,amplitude=.5,cutoff=1.,steps=800):
    parameters(a,n,amplitude,cutoff); h=a*n
    def f(p): return 2*occupation(p,amplitude,cutoff)
    def kernel(p):
        q=w.qmomentum(p,a); z=h*q
        return -q*(math.sin(z)/z if z else 1)*f(p)
    r=w.simpson(kernel,cutoff,steps)
    cross=w.simpson(lambda p:p*math.cos(h*w.qmomentum(p,a))*f(p)/math.sqrt(1-(a*p/2)**2),cutoff,steps)/(4*math.pi)
    return r,cross


def target(amplitude=.5,cutoff=1.): return moment(1,amplitude,cutoff)/(2*math.pi)


def current(a,n,amplitude=.5,cutoff=1.,steps=800):
    r,_=ratios(a,n,amplitude,cutoff,steps)
    return -(2*w.shape(n)*r+(a*n*r)**2)/(4*math.pi)


def mixed(a,n,amplitude=.5,cutoff=1.):
    _,b=ratios(a,n,amplitude,cutoff)
    base=1/(4*math.pi*(n*n-.25))
    return -math.pi*(2*base*b+a*a*b*b)


def energy(a,amplitude=.5,cutoff=1.,steps=800):
    parameters(a,1,amplitude,cutoff)
    return w.simpson(lambda p:2*p*occupation(p,amplitude,cutoff)/math.sqrt(1-(a*p/2)**2),cutoff,steps)/math.pi


def ratio_bound(a,n,amplitude=.5,cutoff=1.):
    parameters(a,n,amplitude,cutoff)
    return (math.pi**3*(a*n)**2/48+a*a/12)*moment(3,amplitude,cutoff)


def energy_bound(a,amplitude=.5,cutoff=1.):
    parameters(a,1,amplitude,cutoff)
    return a*a*moment(3,amplitude,cutoff)/(4*math.pi)


def covariance(a,n,amplitude=.5,cutoff=1.):
    r,_=ratios(a,n,amplitude,cutoff)
    off=-1j*a*(w.shape(n)/(a*n)+a*n*r)/(2*math.pi)
    return ((.5+0j,off),(off.conjugate(),.5+0j))
