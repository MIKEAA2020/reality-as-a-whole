"""Observer-covariant angular record for the sphere/quantum echo.

The null cone, an observer T and an oriented spacelike axis M are extra
assumptions. Their covariant transport is not a derivation of spacetime.
"""
from fractions import Fraction as F
import math
import numpy as np


def boost_angle(v,beta):
    if not -1<v<1 or not -1<beta<1:raise ValueError('outside open domain')
    return (v-beta)/(1-beta*v)


def inverse_angle(v,beta):
    if not -1<v<1 or not -1<beta<1:raise ValueError('outside open domain')
    return (v+beta)/(1+beta*v)


def transported_density(v,beta):
    """Pushforward of uniform du/2 under the aberration map."""
    return (1-beta*beta)/(2*(1+beta*v)**2)


def transported_counterpart(v,beta):
    return boost_angle(-inverse_angle(v,beta),beta)


def counterpart_abs_derivative(v,beta):
    return (1-beta*beta)**2/(1+beta*beta+2*beta*v)**2


def transported_sign(v,beta):
    x=inverse_angle(v,beta)
    if x==0:raise ValueError('sign on zero boundary')
    return 1 if x>0 else -1


def naive_sign(v):
    if v==0:raise ValueError('sign on zero boundary')
    return 1 if v>0 else -1


def conditional_angle(T,M,K):
    """-K·M/K·T in (+---), with future K, unit T and unit M⊥T."""
    eta=np.diag([1.,-1.,-1.,-1.])
    T=np.asarray(T);M=np.asarray(M);K=np.asarray(K)
    denominator=T@eta@K
    if denominator<=0:raise ValueError('nonpositive observer frequency')
    return -(M@eta@K)/denominator


def lorentz_z(beta):
    if not -1<beta<1:raise ValueError('invalid boost')
    gamma=1/math.sqrt(1-beta*beta)
    return np.array([[gamma,0,0,-gamma*beta],
                     [0,1,0,0],[0,0,1,0],
                     [-gamma*beta,0,0,gamma]])
