"""Three independent frames, gauge-covariant tree links and loop controls.

The round spheres, SO(3) links, Haar measure and written memory are model
inputs; no spacetime gauge connection or detector is derived.
"""
import numpy as np
from verification.zero_spherical_invariant_echo import unit


def gauge_tree(directions,l12,l13,rotations):
    n1,n2,n3=map(unit,directions);r1,r2,r3=rotations
    return ((r1@n1,r2@n2,r3@n3),r1@l12@r2.T,r1@l13@r3.T)


def tree_vectors(directions,l12,l13):
    n1,n2,n3=map(unit,directions)
    return n1,l12@n2,l13@n3


def invariants(directions,l12,l13):
    a,b,c=tree_vectors(directions,l12,l13)
    return np.array([a@b,b@c,c@a,a@np.cross(b,c)])


def tree_gauge_fix(directions,l12,l13):
    return gauge_tree(directions,l12,l13,(np.eye(3),l12,l13))


def gauge_loop(directions,l12,l13,l23,rotations):
    ds,a,b=gauge_tree(directions,l12,l13,rotations)
    return ds,a,b,rotations[1]@l23@rotations[2].T


def holonomy(l12,l13,l23):
    return l12@l23@l13.T


def loop_observables(directions,l12,l13,l23):
    h=holonomy(l12,l13,l23);v=tree_vectors(directions,l12,l13)[0]
    return np.array([np.trace(h),v@h@v])


def correlated_density(chirality,trace_h,eps):
    if not -1<eps<1:raise ValueError('require |eps|<1 for strict positivity')
    if abs(chirality)>1+1e-12 or not -1-1e-12<=trace_h<=3+1e-12:
        raise ValueError('outside proper rotation domain')
    return 1+eps*chirality*trace_h/3
