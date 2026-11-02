"""Exact finite certificates for a conditional dyadic completion.

Infinite completion/measure claims rely on hypotheses and proofs in REPORT.md,
not on extrapolating finite tests. Coordinates here encode a refinement gauge;
rank midpoints are not assumed to be metric midpoints.
"""
from fractions import Fraction as F


def level(n):
    if not isinstance(n,int) or not 0<=n<=8:
        raise ValueError('Diagnostic level must be an integer from zero through eight')
    return 1<<n


def vertex(n,i):
    size=level(n)
    if not isinstance(i,int) or not 0<=i<=size:
        raise ValueError('Vertex index outside this level')
    return F(i,size)


def bracket(n,x):
    size=level(n); x=F(x)
    if not 0<=x<=1:
        raise ValueError('Completion patch is [0,1]')
    i=min(size-1,(x*size).numerator//(x*size).denominator)
    return F(i,size),F(i+1,size)


def binary_prefix(bits):
    if any(b not in (0,1) for b in bits):
        raise ValueError('Binary digits required')
    return sum((F(b,1<<(i+1)) for i,b in enumerate(bits)),F(0))


def uniform(n,i,j):
    return F(1,4**n)


def affine(n,i,j,a=F(1),b=F(1,3),c=F(1,2)):
    size=1<<n
    return (F(a)+F(b)*F(2*i+1,2*size)+F(c)*F(2*j+1,2*size))/size**2


def digit_probability(n,i,p):
    p=F(p)
    if not 0<p<1:
        raise ValueError('Strictly interior digit probability required')
    ones=i.bit_count()
    return p**ones*(1-p)**(n-ones)


def biased(n,i,j,p=F(2,3),q=F(1,3)):
    return digit_probability(n,i,p)*digit_probability(n,j,q)


def late_bias(n,i,j,after=3,p=F(2,3),q=F(1,3)):
    if n<=after:
        return uniform(n,i,j)
    tail=n-after; mask=(1<<tail)-1
    return F(1,4**after)*biased(tail,i&mask,j&mask,p,q)


def boundary_path(n,i,j,epsilon=F(1,4)):
    """Uniform v, u atom on address 0.111..., incompatible with half-open cells."""
    epsilon=F(epsilon)
    if not 0<epsilon<1:
        raise ValueError('Interior mixture weight required')
    if n==0:
        return F(1)
    path=(1<<(n-1))-1
    return ((1-epsilon)*F(1,1<<n)+(epsilon if i==path else 0))*F(1,1<<n)


def jump(n,i,j):
    # rho(u,v)=1 for u<1/2; 2 for u>=1/2.
    return F(3,2) if n==0 else F(1 if i<(1<<(n-1)) else 2,4**n)


def weights(rule,n):
    size=level(n)
    result=tuple(tuple(F(rule(n,i,j)) for j in range(size)) for i in range(size))
    if any(x<=0 for row in result for x in row):
        raise ValueError('Strictly positive cell values required by this model')
    return result


def total(matrix):
    return sum((x for row in matrix for x in row),F(0))


def coarsen(matrix):
    size=len(matrix)
    if size<2 or size%2 or any(len(row)!=size for row in matrix):
        raise ValueError('Even square child matrix required')
    return tuple(tuple(sum((matrix[2*i+di][2*j+dj] for di in (0,1) for dj in (0,1)),F(0))
                       for j in range(size//2)) for i in range(size//2))


def consistency(rule,n):
    if n>=8:
        raise ValueError('Need an available child diagnostic level')
    return weights(rule,n)==coarsen(weights(rule,n+1))


def strip_maxima(matrix):
    n=len(matrix)
    return max(sum(row) for row in matrix),max(sum(matrix[i][j] for i in range(n)) for j in range(n))


def densities(matrix):
    area=F(1,len(matrix)**2)
    return tuple(tuple(x/area for x in row) for row in matrix)


def neighbour_jump(matrix):
    rho=densities(matrix); n=len(rho)
    diffs=[abs(rho[i][j]-rho[i+di][j+dj]) for i in range(n) for j in range(n)
           for di,dj in ((1,0),(0,1)) if i+di<n and j+dj<n]
    return max(diffs,default=F(0))


def density_at(matrix,u,v):
    u,v=F(u),F(v)
    if not (0<=u<=1 and 0<=v<=1):
        raise ValueError('Point outside completion patch')
    n=len(matrix)
    i=min(n-1,int(u*n)); j=min(n-1,int(v*n))
    return matrix[i][j]*n*n


def quantile(n,k,p):
    size=level(n)
    if not isinstance(k,int) or not 0<=k<=size:
        raise ValueError('Dyadic cut index required')
    return sum((digit_probability(n,i,p) for i in range(k)),F(0))


def affine_curvature(u,v,a=F(1),b=F(1,3),c=F(1,2)):
    rho=F(a)+F(b)*F(u)+F(c)*F(v)
    if rho<=0:
        raise ValueError('Positive volume density required')
    # g=2*rho du dv; same curvature convention as step 19.
    return 2*F(b)*F(c)/rho**3
