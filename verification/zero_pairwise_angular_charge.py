"""Charge-conserving paired angular records attached to the original echo.

The finite signed charge, local two-level factors and gates are stipulated
model resources, not derived cosmic energy or actual experiences. The two
angular value registers are distinct; copying their quantum label can dephase
the original angle register when the new records are discarded.
"""
from fractions import Fraction as F
from verification.zero_quantum_angular_echo import latitudes
from verification.zero_sphere_angular_echo import magnitude


def energy_from_values(values,a,b,z1,z2):
    n=len(values)
    if not (0<=a<n and 0<=b<n and z1 in (1,-1) and z2 in (1,-1)):
        raise ValueError('invalid pair register')
    return values[a]*z1+values[b]*z2


def paired_energy(a,b,z1,z2,n,kind):
    return energy_from_values(tuple(magnitude(x,kind) for x in latitudes(n)),a,b,z1,z2)


def copy_angles(i,a,b,z1,z2,n,inverse=False):
    """Controlled shift only within equal-angle, opposite-sign zero sector.

    Elsewhere act as identity. This is a permutation of the complete pair
    basis; active and inactive sets are disjoint and invariant.
    """
    latitudes(n)
    if not (0<=i<n and 0<=a<n and 0<=b<n and z1 in (1,-1) and z2 in (1,-1)):
        raise ValueError('invalid register')
    if a==b and z1==-z2:
        step=-i if inverse else i
        a=(a+step)%n;b=(b+step)%n
    return a,b,z1,z2


def write_sign(k,a,b,z1,z2,n):
    """Controlled pair flip within the matched zero sector; otherwise identity."""
    latitudes(n)
    if not (k in (1,-1) and 0<=a<n and 0<=b<n and z1 in (1,-1) and z2 in (1,-1)):
        raise ValueError('invalid register')
    if k==-1 and a==b and z1==-z2:z1=-z1;z2=-z2
    return a,b,z1,z2


def prepared_output(i,k,n):
    """Both copied magnitudes and the two opposite signed records."""
    state=copy_angles(i,0,0,1,-1,n)
    return write_sign(k,*state,n)


def undo_output(i,k,state,n):
    state=write_sign(k,*state,n)
    return copy_angles(i,*state,n,inverse=True)


def q_anchor_reading(q,r,anchor,length=24):
    """Uniform-anchor stationary-clock readout for a unique anchor."""
    if length%4 or q not in (1,2) or r not in range(4) or not 0<=anchor<length:
        raise ValueError('invalid clock input')
    selected=[t for t in range(length) if (q*t)%4==r]
    if not selected:raise ValueError('zero-probability reference event')
    return F(1,len(selected)) if anchor in selected else F(0)
