"""Finite algebra controls for the Poincare/energy why-chain.

The affine matrices below are not unitary quantum operators, and these
relations do not establish actual global Poincare symmetry or cosmic energy.
"""
import sympy as sp


def matrix_unit(i,j):
    out=sp.zeros(5);out[i,j]=1;return out


def generators():
    E=matrix_unit
    rotations=(E(3,2)-E(2,3),E(1,3)-E(3,1),E(2,1)-E(1,2))
    boosts=tuple(E(0,i)+E(i,0) for i in range(1,4))
    translations=tuple(E(i,4) for i in range(4))
    return rotations,boosts,translations


def bracket(a,b):return a*b-b*a


def derived_span_rank(items):
    cols=[bracket(a,b).reshape(25,1) for a in items for b in items]
    return sp.Matrix.hstack(*cols).rank()


def boost_01(c,s):
    """Minkowski transformation in the chosen (-,+,+,+) convention."""
    out=sp.eye(4);out[0,0]=c;out[1,1]=c;out[0,1]=s;out[1,0]=s
    return out


def minkowski_metric():return sp.diag(-1,1,1,1)


def finite_rotation_boost_obstruction(J3,K2):
    """The two nonnegative traces a Lorentz algebra would require to sum to 0.

    Under [K1,K2]=-iJ3 and [J3,K1]=iK2, trace cyclicity implies
    Tr(J3²)+Tr(K2²)=0. Does not itself verify those commutators.
    """
    return sp.trace(J3*J3)+sp.trace(K2*K2)
