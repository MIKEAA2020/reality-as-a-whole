"""Root cause and conditional graph repair for the echo's type reflection.

The graph's topology and kinetic form are mathematical candidates; neither
spacetime locality, actual subjects nor the universe's Hamiltonian is implied.
"""
from fractions import Fraction as F
from math import pi,cos,sin
import numpy as np
from verification.zero_relational_laplacian import generator,type_reflection,type_symmetric_generator


def reflected_angle(u):
    if not -1<u<1:raise ValueError('open interval only')
    return -1-u if u<0 else u


def sym_loop_weight(u):
    """Reflection-invariant averaged p=1-u² on the negative loop."""
    u=F(u)
    if not -1<=u<=0:raise ValueError('expected loop coordinate')
    return F(1,2)-u-u*u


def midpoint_angles(n):
    if n<4 or n%4:raise ValueError('requires a multiple of four')
    return np.array([-1+(2*i+1)/n for i in range(n)])


def shortcut_rate(n):
    if n<4 or n%4:raise ValueError('requires a multiple of four')
    return F(n*n,8)


def quadratic_energy(q,f):
    f=np.asarray(f,dtype=float)
    if q.shape!=(len(f),len(f)):raise ValueError('shape mismatch')
    return float(-f@q@f/len(f))


def graph_f(u):
    """Nonconstant R-odd graph test function, zero on the attached tail."""
    return sin(2*pi*u) if u<0 else 0.


def graph_derivative(u):
    return 2*pi*cos(2*pi*u) if u<0 else 0.


def existing_rates(n):
    q=generator(n);r=type_reflection(n);s=type_symmetric_generator(n)
    return q,r,s
