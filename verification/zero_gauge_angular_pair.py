"""Gauge-constrained angular pair: no fixed auxiliary ready state.

The gauge group, physical-sector constraints and pair factorization are
model inputs. The isometry shows the pair introduces no independent physical
state degrees on the constrained domain; it does not establish subjects.
"""
from fractions import Fraction as F
from itertools import product
import cmath
import math
from verification.zero_quantum_angular_echo import latitudes
from verification.zero_sphere_angular_echo import magnitude
from verification.zero_stationary_battery_bridge import PREFIX,INVERSE,TICKS

SIGNS=(1,-1)


def basis(n):
    latitudes(n)
    return product(SIGNS,range(n),range(n),range(n),SIGNS,SIGNS)


def constraints(k,i,a,b,z1,z2):
    """Gauge generator eigenvalues: Q0, D1, D2, and Z2 involution G."""
    return z1+z2,a-i,b-i,k*z1


def physical(k,i,a,b,z1,z2):
    q,d1,d2,g=constraints(k,i,a,b,z1,z2)
    return int(q==0 and d1==0 and d2==0 and g==1)


def encode(k,i,n):
    latitudes(n)
    if k not in SIGNS or not 0<=i<n:raise ValueError('invalid old label')
    return k,i,i,i,k,-k


def phase_filter(value,modulus):
    """Average of a finite subgroup of a compact U(1)."""
    return sum(cmath.exp(2j*math.pi*j*value/modulus) for j in range(modulus))/modulus


def subgroup_twirl(k,i,a,b,z1,z2,n):
    q,d1,d2,g=constraints(k,i,a,b,z1,z2)
    return phase_filter(q,3)*phase_filter(d1,n)*phase_filter(d2,n)*(1+g)/2


def charges(k,i,a,b,z1,z2,n,kind):
    u=latitudes(n)
    return (magnitude(u[a],kind)*z1,
            magnitude(u[b],kind)*z2,
            magnitude(u[i],kind)*k)


def anchor_sign(t,x,anchor=10):
    if not 0<=t<TICKS or not 0<=anchor<TICKS:raise ValueError('invalid tick')
    b,j,r,s=PREFIX[anchor][INVERSE[t][x]]
    return s*j*r


def stationary_physical(t,x,i,a,b,z1,z2,anchor=10):
    return physical(anchor_sign(t,x,anchor),i,a,b,z1,z2)


def scale_ratios(n,kind,i,j):
    u=latitudes(n);den=magnitude(u[j],kind)
    if den==0:raise ValueError('undefined ratio')
    return magnitude(u[i],kind)/den
