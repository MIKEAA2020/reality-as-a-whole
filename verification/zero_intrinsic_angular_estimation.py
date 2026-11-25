"""Best old-carrier reconstruction of angular candidate magnitudes.

Born weights, the added angular record, and the two quality operators are
inputs of a finite model. None is asserted to instantiate felt experience.
Exact continuous moments use Fraction polynomial integration, no quadrature.
"""
from fractions import Fraction as F
from verification.zero_quantum_angular_echo import latitudes
from verification.zero_sphere_angular_echo import magnitude

BANDS=((F(-1),F(-1,2)),(F(-1,2),F(0)),(F(0),F(1)))


def band_index(u):
    if not -1<u<1 or u in (F(-1,2),F(0)):raise ValueError('excluded boundary')
    return 0 if u<F(-1,2) else 1 if u<0 else 2


def polynomial(kind,band):
    if kind=='absolute':return (F(0),F(-1 if band<2 else 1))
    if kind=='swap_invariant':
        q=F(-1 if band<2 else 1)
        return (F(0),q,q)
    raise ValueError('unknown candidate')


def integral(poly,a,b):
    return sum((c*(b**(i+1)-a**(i+1))/F(i+1) for i,c in enumerate(poly)),F(0))


def square(poly):
    out=[F(0)]*(2*len(poly)-1)
    for i,a in enumerate(poly):
        for j,b in enumerate(poly):out[i+j]+=a*b
    return tuple(out)


def continuum_stats(kind):
    means=[];risk=F(0);second=F(0);avg=F(0)
    for i,(a,b) in enumerate(BANDS):
        p=polynomial(kind,i);m=integral(p,a,b)/(b-a);means.append(m)
        res=list(p);res[0]-=m
        risk+=integral(square(res),a,b)/2
        second+=integral(square(p),a,b)/2
        avg+=integral(p,a,b)/2
    baseline=second-avg*avg
    return tuple(means),risk,avg,baseline


def discrete_stats(kind,n):
    u=latitudes(n);bins=[[magnitude(x,kind) for x in u if band_index(x)==i]
                         for i in range(3)]
    means=tuple(sum(v,F(0))/len(v) for v in bins)
    risk=sum((sum(((x-means[i])**2 for x in v),F(0))
              for i,v in enumerate(bins)),F(0))/n
    avg=sum((sum(v,F(0)) for v in bins),F(0))/n
    baseline=sum((sum(((x-avg)**2 for x in v),F(0)) for v in bins),F(0))/n
    return means,risk,avg,baseline
