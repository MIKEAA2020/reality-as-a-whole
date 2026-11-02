"""Physical structural candidate, not a consciousness detector.

All domains, clocks, and surgical coordinate interventions are stipulated.
Static state recoding tests use a broader encoding class than coordinate renaming;
causal-graph invariance is NOT claimed for arbitrary mixed-coordinate encodings.
"""
from itertools import product, permutations


def states(n):
    return tuple(product((0,1),repeat=n))


def source(s):
    x,y=s
    return (y,x^y)


def circuit(s):
    x,y,u,v=s
    a,b=source((x,y))
    return (a,b,a,b)


def iterate(step,s,n):
    if n<0:
        raise ValueError('Nonnegative step count required')
    for _ in range(n):
        s=step(s)
    return s


def surgical(s,index,value):
    result=list(s)
    result[index]=value
    return tuple(result)


def influence_edges(step,n):
    edges=set()
    for s in states(n):
        base=step(s)
        for i in range(n):
            changed=step(surgical(s,i,1-s[i]))
            edges.update((i,j) for j in range(n) if base[j]!=changed[j])
    return frozenset(edges)


def strongly_connected(edges,n):
    reach={(i,i) for i in range(n)}|set(edges)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i,k) in reach and (k,j) in reach:
                    reach.add((i,j))
    return frozenset(frozenset(j for j in range(n) if (i,j) in reach and (j,i) in reach)
                     for i in range(n))


def autonomous_sets(step,n):
    """Nonempty coordinate sets whose next values depend only on themselves."""
    result=[]
    for mask in product((False,True),repeat=n):
        indices=tuple(i for i,include in enumerate(mask) if include)
        if not indices:
            continue
        outputs={}
        for s in states(n):
            key=tuple(s[i] for i in indices)
            value=tuple(step(s)[i] for i in indices)
            outputs.setdefault(key,set()).add(value)
        if all(len(v)==1 for v in outputs.values()):
            result.append(frozenset(indices))
    return frozenset(result)


def projection_commutes(step,project,projected_step,n):
    return all(project(step(s))==projected_step(project(s)) for s in states(n))


def factorization_encodings(step):
    """All static bijections of four states yielding two independent bit maps.

    Enumerates 24 encodings and 16 pairs of unary maps = 384 comparisons.
    This concerns the supplied transition map, not phenomenal decomposition.
    """
    domain=states(2)
    unary=tuple(product((0,1),repeat=2))
    matches=[]
    for encoded_states in permutations(domain):
        encode=dict(zip(domain,encoded_states))
        for f,g in product(unary,repeat=2):
            if all(encode[step(s)]==(f[encode[s][0]],g[encode[s][1]]) for s in domain):
                matches.append((encoded_states,f,g))
    return tuple(matches)


def to_error_coordinates(s):
    x,y,u,v=s
    return (x,y,u^x,v^y)


def from_error_coordinates(s):
    # This particular invertible transformation is its own inverse.
    return to_error_coordinates(s)


def error_coordinate_step(s):
    return to_error_coordinates(circuit(from_error_coordinates(s)))


def rename_coordinates(step,order):
    """New coordinate i stores old coordinate order[i]."""
    def renamed(s):
        old=[0]*len(order)
        for i,old_i in enumerate(order):
            old[old_i]=s[i]
        advanced=step(tuple(old))
        return tuple(advanced[old_i] for old_i in order)
    return renamed


def paired_sources(s):
    return source(s[:2])+source(s[2:])
