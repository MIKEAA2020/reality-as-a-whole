"""Joint-parity report and symmetry-conditioned unity/incidence controls.

The physical code and the proposed incidence extensions are distinct objects.
No operation here establishes subjecthood or an experiential truth interface.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

PHYSICAL=('M','J','L','B','P')
LOGICAL=('M','J','L','P')
# Write N=M*J then K=M*L into the same XOR accumulator P.
JOINT=(('M','P'),('J','P'),('M','P'),('L','P'))
BYPASS=(('B','P'),)
SIGNS=(1,-1)
TYPES=('joint','now','echo')


def encode(row):
    if set(row)!=set(LOGICAL) or any(v not in (0,1) for v in row.values()):
        raise ValueError('invalid logical basis')
    return dict(row)|{'B':row['J']^row['L']}


def flip_now(cell):
    n,k=cell;return -n,k


def flip_echo(cell):
    n,k=cell;return n,-k


def counterpart(cell):
    n,k=cell;return -n,-k


def swap_type(cell):
    n,k=cell;return k,n


def invariant_predicates(operations):
    """Binary unity classifications invariant under given cell permutations."""
    cells=tuple(product(SIGNS,repeat=2));out=[]
    for truth in product((False,True),repeat=len(cells)):
        table=dict(zip(cells,truth))
        if all(table[c]==table[op(c)] for op in operations for c in cells):
            out.append(table)
    return out


def incidence(alpha,beta):
    """Normalized incidence-type extension with a fixed four-cell marginal.

    alpha weights joint-type incidences; remaining weight is split between
    now and echo types by beta. This is not a subject-counting theorem.
    """
    alpha,beta=F(alpha),F(beta)
    if not (0<=alpha<=1 and 0<=beta<=1):raise ValueError('invalid weight')
    weights={'joint':alpha,'now':(1-alpha)*beta,'echo':(1-alpha)*(1-beta)}
    return {(n,k,t):weights[t]/4 for n,k,t in product(SIGNS,SIGNS,TYPES)}


def type_transform(n,k,t):
    return (k,n,{'joint':'joint','now':'echo','echo':'now'}[t])


def physically_summed(table):
    return {(n,k):sum((table[n,k,t] for t in TYPES),F(0))
            for n,k in product(SIGNS,repeat=2)}


def independent_majority_error(trials,error):
    """Exact IID Bernoulli error probability for odd-number majority."""
    if trials<=0 or trials%2!=1:raise ValueError('positive odd trial count required')
    error=F(error)
    if not 0<=error<=F(1,2):raise ValueError('invalid error bound')
    return sum((F(comb(trials,k))*error**k*(1-error)**(trials-k)
                for k in range((trials+1)//2,trials+1)),F(0))


def shared_fault_error(trials,error):
    """Correlated exchangeable errors saturating the majority Markov bound.

    With probability p, exactly ceil(trials/2) positions, chosen uniformly,
    are wrong; otherwise none are wrong. Return marginal error and majority
    error. This is a control distribution, not a physical error model.
    """
    if trials<=0 or trials%2!=1:raise ValueError('positive odd trial count required')
    error=F(error);threshold=(trials+1)//2
    p=F(trials,threshold)*error
    if not 0<=p<=1:raise ValueError('error too large for this construction')
    return p*F(threshold,trials),p


def proposed_signed_total(table):
    """One explicit two-component bookkeeping convention, not felt valence."""
    out=[F(0),F(0)]
    for (n,k,t),p in table.items():
        if t in ('joint','now'):out[0]+=p*n
        if t in ('joint','echo'):out[1]+=p*k
    return tuple(out)
