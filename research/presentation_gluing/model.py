"""Finite gluing tests. These are descriptions/probability models, not experiences.

No physical probability is identified with a phenomenal or self-location
measure. 'Admissible' assignments and occurrence witnesses are supplied.
"""
from fractions import Fraction
from itertools import product
from math import log2

BITS = tuple(product((0,1), repeat=3))
PAIRS = ((0,1),(0,2),(1,2))


def compatible_sections(sections):
    return all(all(a[k]==b[k] for k in a.keys() & b.keys())
               for a in sections for b in sections)


def glue_sections(sections):
    sections=tuple(dict(s) for s in sections)
    if not compatible_sections(sections):
        return None
    result={}
    for section in sections:
        result.update(section)
    return result


def admissible_glue(sections, allowed):
    glued=glue_sections(sections)
    if glued is None:
        return ()
    return tuple(state for state in allowed if all(state[k]==v for k,v in glued.items()))


def parity_family(t):
    """All distributions with uniform two-bit marginals: p_t=(1+t parity)/8.

    The generality claim is justified by the rank/nullspace check, not naming.
    """
    t=Fraction(t)
    if not -1<=t<=1:
        raise ValueError('Nonnegative probabilities require -1 <= t <= 1')
    return {s:(1+t*((-1)**sum(s)))/8 for s in BITS}


def marginal(distribution, indices):
    indices=tuple(indices)
    result={values:Fraction(0) for values in product((0,1),repeat=len(indices))}
    for state,weight in distribution.items():
        result[tuple(state[i] for i in indices)]+=weight
    return result


def correlation(distribution, indices=(0,1,2)):
    return sum(weight*((-1)**sum(state[i] for i in indices))
               for state,weight in distribution.items())


def entropy(distribution):
    return -sum(float(p)*log2(float(p)) for p in distribution.values() if p)


def anticorrelated_pair():
    return {(0,0):Fraction(0),(0,1):Fraction(1,2),
            (1,0):Fraction(1,2),(1,1):Fraction(0)}


def supported_global_assignments(pair_supports):
    """A necessary condition for a global joint with the specified zero patterns."""
    return tuple(s for s in BITS if all(tuple(s[i] for i in pair) in support
                                       for pair,support in pair_supports.items()))


def uniform_pair_constraints():
    rows=[]
    for pair in PAIRS:
        for outcome in product((0,1),repeat=2):
            rows.append([Fraction(int(tuple(s[i] for i in pair)==outcome)) for s in BITS])
    return rows


def rref(matrix):
    m=[list(map(Fraction,row)) for row in matrix]
    if not m:
        return [],()
    pivots=[]
    row=0
    for col in range(len(m[0])):
        pivot=next((r for r in range(row,len(m)) if m[r][col]),None)
        if pivot is None:
            continue
        m[row],m[pivot]=m[pivot],m[row]
        scale=m[row][col]
        m[row]=[x/scale for x in m[row]]
        for r in range(len(m)):
            if r!=row and m[r][col]:
                factor=m[r][col]
                m[r]=[a-factor*b for a,b in zip(m[r],m[row])]
        pivots.append(col)
        row+=1
        if row==len(m):
            break
    return m,tuple(pivots)


def parity_readout(state):
    """Ordinary physical joint computation; not a phenomenal-unity witness."""
    return sum(state)%2


def duplicate_occurrence_records(record,copies):
    """Supplied distinct records, with matching contents. No inferred subjects."""
    if copies<1:
        raise ValueError('Positive copy number required')
    return tuple((f'occurrence-{i}',record) for i in range(copies))
