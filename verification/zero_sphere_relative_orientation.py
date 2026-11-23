"""Parity-even invariant of two null directions relative to three others."""
from fractions import Fraction as F
from itertools import permutations
from math import prod


def null_ray(x,y):
    x,y=F(x),F(y)
    s=x*x+y*y
    return (1+s,2*x,2*y,s-1)


def lorentz_dot(a,b):
    return -a[0]*b[0]+sum(a[i]*b[i] for i in range(1,4))


def det4(matrix):
    if len(matrix)!=4 or any(len(row)!=4 for row in matrix):
        raise ValueError('expected a 4 by 4 matrix')
    result=F(0)
    for perm in permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        result+=(-1)**inversions*prod(matrix[i][perm[i]] for i in range(4))
    return result


def valid_null(k): return len(k)==4 and k[0]>0 and lorentz_dot(k,k)==0


def delta(vectors):
    if len(vectors)!=4 or not all(valid_null(v) for v in vectors):
        raise ValueError('expected four future-directed nonzero null vectors')
    # Vectors as columns; determinant is unchanged by transposition.
    return det4(vectors)


def relative_product(rays):
    if len(rays)!=5: raise ValueError('five rays required')
    return delta(rays[:4])*delta(rays[:3]+[rays[4]])


def mixed_gram_product(rays):
    if len(rays)!=5 or not all(valid_null(v) for v in rays):
        raise ValueError('five future-directed null vectors required')
    left=rays[:4]
    right=rays[:3]+[rays[4]]
    gram=[[lorentz_dot(a,b) for b in right] for a in left]
    return -det4(gram)


def z_boost(v):
    t,x,y,z=v
    return ((5*t-3*z)/4,x,y,(5*z-3*t)/4)


def spatial_reflection(v):
    t,x,y,z=v
    return (t,-x,y,z)
