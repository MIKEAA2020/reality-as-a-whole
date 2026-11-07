"""A declared causal-exclusion proxy, not an implementation of IIT 4.0.
Finite Boolean coordinates and uniform external interventions are supplied.
"""
from functools import lru_cache
from itertools import combinations
import math


def states(n):return range(1<<n)
def extract(x,region):return sum(((x>>j)&1)<<i for i,j in enumerate(region))
def insert(x,region,value):
    for i,j in enumerate(region):x=(x&~(1<<j))|(((value>>i)&1)<<j)
    return x

def validate(kernel):
    n=round(math.log2(len(kernel))) if kernel else 0
    if n<1 or len(kernel)!=(1<<n) or any(len(row)!=len(kernel) or any(not math.isfinite(p) or p<0 for p in row) or abs(sum(row)-1)>1e-10 for row in kernel):raise ValueError('Stochastic power-of-two kernel required')
    return n


def deterministic(n,function):
    return tuple(tuple(float(y==function(x)) for y in states(n)) for x in states(n))


def source_update(x):
    a,b=x&1,(x>>1)&1
    return b|((a^b)<<1)


def source_monitor():
    return deterministic(4,lambda x:source_update(x&3)|(source_update(x&3)<<2))


def coupled_sources(epsilon):
    if not math.isfinite(epsilon) or not 0<=epsilon<=1:raise ValueError('Probability in [0,1] required')
    def uncoupled(x):return source_update(x&3)|(source_update(x>>2)<<2)
    def bridge(y):
        b,c=(y>>1)&1,(y>>2)&1
        return (y&~6)|(c<<1)|(b<<2)
    return tuple(tuple((1-epsilon)*(y==uncoupled(x))+epsilon*(y==bridge(uncoupled(x))) for y in states(4)) for x in states(4))


@lru_cache(maxsize=None)
def regional(kernel,region):
    n=validate(kernel)
    if not region or tuple(sorted(set(region)))!=region or any(i<0 or i>=n for i in region):raise ValueError('Nonempty ordered physical region required')
    size=1<<len(region);outside=2**(n-len(region));rows=[]
    for local in range(size):
        row=[0.]*size
        for x in states(n):
            if extract(x,region)==local:
                for y,p in enumerate(kernel[x]):row[extract(y,region)]+=p/outside
        rows.append(tuple(row))
    return tuple(rows)


def bipartitions(n):
    # Each unordered split appears once, with coordinate 0 on the left.
    for mask in range(1,(1<<n)-1):
        if mask&1:yield tuple(i for i in range(n) if mask>>i&1),tuple(i for i in range(n) if not mask>>i&1)


def cut_kernel(kernel,left,right):
    n=validate(kernel)
    if set(left)&set(right) or set(left)|set(right)!=set(range(n)) or not left or not right:raise ValueError('Nontrivial coordinate partition required')
    a,b=regional(kernel,left),regional(kernel,right)
    return tuple(tuple(a[extract(x,left)][extract(y,left)]*b[extract(x,right)][extract(y,right)] for y in states(n)) for x in states(n))


def distance(first,second):
    if validate(first)!=validate(second):raise ValueError('Kernel dimensions must match')
    return sum(sum(abs(p-q) for p,q in zip(a,b))/2 for a,b in zip(first,second))/len(first)


@lru_cache(maxsize=None)
def irreducibility(kernel):
    n=validate(kernel)
    if n==1:return 0.
    return min(distance(kernel,cut_kernel(kernel,a,b)) for a,b in bipartitions(n))


def scores(kernel):
    n=validate(kernel)
    return {region:irreducibility(regional(kernel,region)) for size in range(1,n+1) for region in combinations(range(n),size)}


def maximal_regions(kernel,tolerance=1e-12):
    # Equal overlapping maxima remain alternatives; not silently counted as subjects.
    values=scores(kernel)
    return {region:score for region,score in values.items() if score>tolerance and not any(set(region)&set(other) and value>score+tolerance for other,value in values.items())}


def compose(first,second):
    if validate(first)!=validate(second):raise ValueError('Dimensions must match')
    return tuple(tuple(sum(first[x][z]*second[z][y] for z in range(len(first))) for y in range(len(first))) for x in range(len(first)))


def power(kernel,steps):
    n=validate(kernel)
    if not isinstance(steps,int) or steps<1:raise ValueError('Positive integer step count required')
    out=deterministic(n,lambda x:x)
    for _ in range(steps):out=compose(out,kernel)
    return out


def feedforward_copy():return deterministic(2,lambda x:(x&1)<<1)
