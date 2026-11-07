"""Different senses of independence and a two-sorted structural match.

Phenomenal episode descriptions below are stipulated formal targets, not observed
experience or established metaphysical possibilities. No state map derives their
incidence. The physical source repeats the previous round's two-bit map.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product

STATES=tuple(product((0,1),repeat=2))


def source(s):
    x,y=s
    return (y,x^y)


def inverse(s):
    p,q=s
    return (p^q,p)


def reset(s,axis,value):
    out=list(s)
    out[axis]=value
    return tuple(out)


def operation_table(operation):
    return tuple(operation(s) for s in STATES)


def native_resets():
    return tuple(operation_table(lambda s,i=i,v=v:reset(s,i,v))
                 for i in (0,1) for v in (0,1))


def transported_resets():
    return tuple(operation_table(lambda s,i=i,v=v:source(reset(inverse(s),i,v)))
                 for i in (0,1) for v in (0,1))


def pushforward(distribution,step):
    out={s:Fraction(0) for s in STATES}
    for s,p in distribution.items():
        out[step(s)]+=p
    return out


def statistically_independent(distribution):
    if set(distribution)!=set(STATES) or sum(distribution.values())!=1 or any(p<0 for p in distribution.values()):
        raise ValueError('Need normalized nonnegative distribution on all four states')
    marginals=[{v:sum(p for s,p in distribution.items() if s[i]==v) for v in (0,1)} for i in (0,1)]
    return all(distribution[s]==marginals[0][s[0]]*marginals[1][s[1]] for s in STATES)


def product_dynamics(step):
    unary=tuple(product((0,1),repeat=2))
    return tuple((f,g) for f in unary for g in unary
                 if all(step(s)==(f[s[0]],g[s[1]]) for s in STATES))


def square_maps():
    # Exactly the eight Hamming-square isometries: two axis orders x four flips.
    maps=[]
    for swap in (False,True):
        for a,b in STATES:
            table=tuple(((s[1],s[0]) if swap else s) for s in STATES)
            maps.append(tuple((u^a,v^b) for u,v in table))
    return tuple(maps)


def map_value(table,s):
    return table[2*s[0]+s[1]]


def dynamic_matches(physical_step,target_step):
    return tuple(h for h in square_maps()
                 if all(map_value(h,physical_step(s))==target_step(map_value(h,s)) for s in STATES))


@dataclass(frozen=True)
class ContentOccurrence:
    run: str
    tick: int
    feature: int
    value: int


@dataclass(frozen=True)
class EpisodeDescription:
    contents: frozenset
    supports: frozenset

    def __post_init__(self):
        if any(not support or not support<=self.contents for support in self.supports):
            raise ValueError('Supports must contain supplied content occurrences')
        if frozenset(c for support in self.supports for c in support)!=self.contents:
            raise ValueError('This fixture requires every content to have a support')

    def values(self):
        return tuple(c.value for c in sorted(self.contents,key=lambda c:c.feature))

    def co_present(self,a,b):
        return any({a,b}<=support for support in self.supports)


def describe(state,*,joint,run='fixture',tick=0):
    contents=tuple(ContentOccurrence(run,tick,i,v) for i,v in enumerate(state))
    supports=(frozenset(contents),) if joint else tuple(frozenset({c}) for c in contents)
    return EpisodeDescription(frozenset(contents),frozenset(supports))


def marginal_evidence(description):
    # Explicitly drops incidence and occurrence provenance, keeping feature values.
    return description.values()


def compatibility_from_marginals(state):
    return tuple(describe(state,joint=joint) for joint in (False,True))
