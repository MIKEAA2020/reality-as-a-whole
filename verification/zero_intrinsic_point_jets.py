"""Finite first-order pointed algebras and echo-angle representations.

These are mathematical models, not claims about actual infinitesimals,
experience, subjecthood, probability, or a self-sufficient ontology.
"""
from fractions import Fraction as F


def jet(constant,coefficients=()):
    return F(constant),tuple(F(c) for c in coefficients)


def add(a,b):
    if len(a[1])!=len(b[1]):raise ValueError('different dimensions')
    return jet(a[0]+b[0],(x+y for x,y in zip(a[1],b[1])))


def multiply(a,b):
    """A=R⊕m, with all products in m² zero."""
    if len(a[1])!=len(b[1]):raise ValueError('different dimensions')
    return jet(a[0]*b[0],(a[0]*y+b[0]*x for x,y in zip(a[1],b[1])))


def evaluate(a):
    """The unique real character fixing scalars: annihilate nilpotents."""
    return a[0]


def derivative(a,v):
    if len(a[1])!=len(v):raise ValueError('different dimensions')
    return sum((x*F(y) for x,y in zip(a[1],v)),F(0))


def dot(a,b):
    if len(a)!=len(b):raise ValueError('different dimensions')
    return sum((F(x)*F(y) for x,y in zip(a,b)),F(0))


def cosine_squared(a,b):
    aa,bb=dot(a,a),dot(b,b)
    if not aa or not bb:raise ValueError('zero has no direction')
    return dot(a,b)**2/(aa*bb)


def diagonal(v,scales):
    if len(v)!=len(scales):raise ValueError('different dimensions')
    return tuple(F(a)*F(b) for a,b in zip(v,scales))


def truncated_multiply(a,b):
    """Product in R[e]/(e^k); coefficients are low order first."""
    if not a or len(a)!=len(b):raise ValueError('different or empty truncations')
    n=len(a)
    return tuple(sum((F(a[i])*F(b[j]) for i in range(n) for j in range(n)
                      if i+j==k),F(0)) for k in range(n))


def shear_ratio_interval(ratio,integer):
    """Shear x1→x1+k*x2 translates x1/x2 when x2≠0."""
    return F(ratio)+int(integer)
