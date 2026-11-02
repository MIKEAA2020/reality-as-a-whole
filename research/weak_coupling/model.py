"""Exact finite weak-coupling audit, not a phenomenal boundary detector."""
from fractions import Fraction
from itertools import product, permutations
from math import comb

STATES=tuple(product((0,1),repeat=2))


def validate(epsilon):
    e=Fraction(epsilon)
    if not 0<=e<=1:
        raise ValueError('Coupling probability outside [0,1]')
    return e


def source(s):
    return (s[1],s[0]^s[1])


def kernel(epsilon,s):
    e=validate(epsilon)
    result={t:Fraction(0) for t in STATES}
    result[s]+=1-e
    result[source(s)]+=e
    return result


def tv(p,q):
    return sum(abs(p.get(s,0)-q.get(s,0)) for s in set(p)|set(q))/2


def kernel_distance(epsilon):
    return max(tv(kernel(epsilon,s),kernel(0,s)) for s in STATES)


def influence(epsilon,i,j):
    values=[]
    for s in STATES:
        changed=list(s)
        changed[i]=1-changed[i]
        a,b=kernel(epsilon,s),kernel(epsilon,tuple(changed))
        pa={v:sum(p for t,p in a.items() if t[j]==v) for v in (0,1)}
        pb={v:sum(p for t,p in b.items() if t[j]==v) for v in (0,1)}
        values.append(tv(pa,pb))
    return max(values)


def influence_edges(epsilon):
    return frozenset((i,j) for i in (0,1) for j in (0,1) if influence(epsilon,i,j)>0)


def strongly_connected(edges,n):
    reach=set(edges)|{(i,i) for i in range(n)}
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i,k) in reach and (k,j) in reach:
                    reach.add((i,j))
    return frozenset(frozenset(j for j in range(n) if (i,j) in reach and (j,i) in reach) for i in range(n))


def product_encodings(epsilon):
    """Static bijections admitting independent stochastic binary transitions."""
    result=[]
    for images in permutations(STATES):
        encode=dict(zip(STATES,images))
        rows={encode[s]:{encode[t]:p for t,p in kernel(epsilon,s).items()} for s in STATES}
        marg={s:tuple(tuple(sum(p for t,p in rows[s].items() if t[i]==v) for v in (0,1)) for i in (0,1)) for s in STATES}
        local=all(marg[s][i]==marg[t][i] for s,t in product(STATES,repeat=2) for i in (0,1) if s[i]==t[i])
        independent=all(rows[s][t]==marg[s][0][t[0]]*marg[s][1][t[1]] for s,t in product(STATES,repeat=2))
        if local and independent:
            result.append(images)
    return tuple(result)


def path_detection(epsilon,horizon):
    """Exact TV from the zero-coupling path law, given a nonfixed initial state.

    Tests equality of full paths, not just the endpoint. Initial 00 is excluded
    from this formula: its path is constant at every coupling probability.
    """
    e=validate(epsilon)
    if not isinstance(horizon,int) or horizon<0:
        raise ValueError('Need nonnegative integer horizon')
    return 1-(1-e)**horizon


def endpoint_detection(epsilon,horizon):
    path_detection(epsilon,horizon)  # validation
    e=validate(epsilon)
    return sum(Fraction(comb(horizon,n))*e**n*(1-e)**(horizon-n)
               for n in range(horizon+1) if n%3!=0)


def propagate(epsilon,start,horizon):
    path_detection(epsilon,horizon)
    distribution={s:Fraction(int(s==start)) for s in STATES}
    for _ in range(horizon):
        distribution={t:sum(p*kernel(epsilon,s)[t] for s,p in distribution.items()) for t in STATES}
    return distribution


def threshold_components(epsilon,threshold):
    """Illustrative two-core graph; threshold is an EXTERNAL convention.

    Within-core edges have unit weight. Reciprocal between-core bridges have
    weight epsilon. Edge admission uses strictly greater than threshold.
    """
    e=validate(epsilon)
    threshold=validate(threshold)
    weights={(0,1):Fraction(1),(1,0):Fraction(1),(2,3):Fraction(1),(3,2):Fraction(1),
             (1,2):e,(3,0):e}
    edges={edge for edge,w in weights.items() if w>threshold}
    return strongly_connected(edges,4)
