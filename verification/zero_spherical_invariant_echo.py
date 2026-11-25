"""Relational S²×S² lift of the original scalar angular echo.

The sphere, normalized area measure and chosen symmetries are model inputs.
A common rotation of both directions is not automatically a gauge redundancy.
"""
import math
import numpy as np
from verification.zero_quantum_angular_echo import latitudes


def unit(v):
    v=np.asarray(v,dtype=float)
    if v.shape!=(3,):raise ValueError('expected a 3-vector')
    n=float(np.linalg.norm(v))
    if n<1e-15:raise ValueError('zero vector has no direction')
    return v/n


def angle(m,n):
    return float(np.clip(np.dot(unit(m),unit(n)),-1.,1.))


def rodrigues(axis,theta):
    a=unit(axis);x,y,z=a
    c=math.cos(theta);s=math.sin(theta)
    cross=np.array([[0,-z,y],[z,0,-x],[-y,x,0]])
    return c*np.eye(3)+(1-c)*np.outer(a,a)+s*cross


def h(u):
    if not -1<=u<=1:raise ValueError('invalid cosine')
    return -1-u if u<0 else u


def reflected_direction(m,n):
    """Lift h(u) to n at fixed m, preserving its tangent azimuth.

    The negative pole has no azimuth and is excluded as a measure-zero set.
    The equator convention also concerns only a measure-zero boundary.
    """
    m=unit(m);n=unit(n);u=angle(m,n)
    if u>=0:return n
    if 1-u*u<1e-14:raise ValueError('negative pole has no tangent azimuth')
    target=h(u)
    return target*m+math.sqrt((1-target*target)/(1-u*u))*(n-u*m)


def bin_index(u,n):
    latitudes(n)
    if not -1<u<1:raise ValueError('pole excluded')
    value=(u+1)*n/2
    if abs(value-round(value))<1e-12:raise ValueError('bin boundary excluded')
    return min(n-1,int(value))


def spherical_bin_amplitude(u,n):
    """|i> ↦ sqrt(N) 1_bin(n·m) in normalized product-area measure."""
    return bin_index(u,n),math.sqrt(n)


def symmetric_density(u,epsilon):
    if not -1<=u<=1 or not -1<epsilon<1:raise ValueError('invalid density input')
    return 1+epsilon*math.cos(2*math.pi*u)


def density_reweight(rows,epsilon):
    """Change angular marginal on actual complex old/echo slices.

    N=4m midpoint bands have equal unweighted and weighted mass for this
    density. The state changes; it is not a passive coordinate relabeling.
    """
    n=len(rows[0]);u=latitudes(n)
    return tuple([math.sqrt(symmetric_density(float(u[i]),epsilon))*x
                  for i,x in enumerate(part)] for part in rows)
