"""Set-valued physical boundary inference, conditional on a toy law.

No data here are empirical. Exact positive-likelihood support is not a confidence
set or an assertion that all surviving parameters deserve equal weight.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction
    closed_lo: bool = True
    closed_hi: bool = True

    def __post_init__(self):
        object.__setattr__(self,'lo',Fraction(self.lo))
        object.__setattr__(self,'hi',Fraction(self.hi))
        if not 0<=self.lo<=self.hi<=1:
            raise ValueError('Interval must lie in [0,1]')
        if self.lo==self.hi and not (self.closed_lo and self.closed_hi):
            raise ValueError('Empty interval')

    def contains(self,x):
        x=Fraction(x)
        return ((x>self.lo or (x==self.lo and self.closed_lo)) and
                (x<self.hi or (x==self.hi and self.closed_hi)))

    def intersection(self,other):
        lo,hi=max(self.lo,other.lo),min(self.hi,other.hi)
        if lo>hi:
            return None
        cl=self.contains(lo) and other.contains(lo)
        ch=self.contains(hi) and other.contains(hi)
        if lo==hi and not (cl and ch):
            return None
        return Interval(lo,hi,cl,ch)

    def has_positive(self):
        return self.hi>0


SPLIT=frozenset({frozenset({0}),frozenset({1})})
MERGED=frozenset({frozenset({0,1})})


def validate_counts(k,n):
    if not isinstance(k,int) or not isinstance(n,int) or not 0<=k<=n:
        raise ValueError('Need integer counts 0 <= k <= n')


def likelihood(epsilon,k,n,noise=0):
    """Ordered binary record, not unordered count likelihood.

    Changes are observed through a binary symmetric error channel. Omitting
    the common binomial coefficient is exact for an ordered record and cancels
    from the finite-hypothesis posterior used below.
    """
    validate_counts(k,n)
    e,eta=Fraction(epsilon),Fraction(noise)
    if not 0<=e<=1 or not 0<=eta<=Fraction(1,2):
        raise ValueError('Invalid parameter')
    p=eta+(1-2*eta)*e
    return p**k*(1-p)**(n-k)


def likelihood_support(k,n,noise=0):
    validate_counts(k,n)
    eta=Fraction(noise)
    if not 0<=eta<=Fraction(1,2):
        raise ValueError('Invalid noise')
    if n==0 or eta>0:
        return Interval(0,1)
    return Interval(0,1,closed_lo=(k==0),closed_hi=(k==n))


def compatible_parameters(calibration,k,n,noise=0):
    """External calibration interval must be warranted separately."""
    return calibration.intersection(likelihood_support(k,n,noise))


def boundary_set(parameters):
    """EXACT-CORE PHYSICAL boundaries, NOT established phenomenal boundaries."""
    if parameters is None:
        return frozenset()
    result=set()
    if parameters.contains(0):
        result.add(SPLIT)
    if parameters.has_positive():
        result.add(MERGED)
    return frozenset(result)


def partition_links(partition):
    blocks=tuple(partition)
    vertices=frozenset(v for block in blocks for v in block)
    if not vertices or any(not block for block in blocks) or sum(len(b) for b in blocks)!=len(vertices):
        raise ValueError('Need nonempty disjoint blocks')
    return frozenset((a,b) for block in blocks for a in block for b in block)


def link_bounds(boundaries):
    """Must-links are universal; may-links existential across rival models."""
    boundaries=tuple(boundaries)
    if not boundaries:
        raise ValueError('No compatible model: do not infer universal certainty')
    links=[partition_links(p) for p in boundaries]
    universes=[frozenset(a for a,b in link) for link in links]
    if any(u!=universes[0] for u in universes):
        raise ValueError('Different token domains')
    must=set(links[0])
    may=set()
    for link in links:
        must.intersection_update(link)
        may.update(link)
    return frozenset(must),frozenset(may)


def is_transitive(relation):
    return all((a,d) in relation for a,b in relation for c,d in relation if b==c)


def closure(relation):
    result=set(relation)
    while True:
        expanded=result|{(a,d) for a,b in result for c,d in result if b==c}
        if expanded==result:
            return frozenset(result)
        result=expanded


def posterior_zero_atom(prior_zero,alternative,k,n,noise=0):
    """Illustrative TWO-HYPOTHESIS prior: epsilon=0 vs epsilon=alternative.

    This prior is supplied, not justified by symmetry or by observer counting.
    """
    w=Fraction(prior_zero)
    e=Fraction(alternative)
    if not 0<=w<=1 or not 0<e<=1:
        raise ValueError('Invalid prior or alternative')
    a=w*likelihood(0,k,n,noise)
    b=(1-w)*likelihood(e,k,n,noise)
    if a+b==0:
        raise ValueError('Record impossible under supplied prior')
    return a/(a+b)
