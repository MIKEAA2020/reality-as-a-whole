"""A finite common construction, not full QFT, quantum gravity, or consciousness.

Entries used here are dyadic Gaussian rationals (0, +/-1, +/-i and halves).
Python complex arithmetic is exact for these small operations; no tolerances or
numerical eigenvalue routines are used. Probabilities are converted to Fraction.
"""
from fractions import Fraction
from itertools import product, combinations


def matrix(rows):
    return tuple(tuple(complex(x) for x in row) for row in rows)


def identity(n):
    return matrix([[int(i==j) for j in range(n)] for i in range(n)])


def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def adjoint(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a))) for i in range(len(a[0])))


def scale(value,a):
    return tuple(tuple(value*x for x in row) for row in a)


def add(a,b):
    return tuple(tuple(x+y for x,y in zip(row_a,row_b)) for row_a,row_b in zip(a,b))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def exact_real(x):
    z=complex(x)
    if z.imag!=0:
        raise ValueError('Expected a real dyadic value')
    return Fraction(z.real)


def kron(a,b):
    return tuple(tuple(a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


I2=identity(2)
I4=identity(4)
P1={'I':I2,'X':matrix(((0,1),(1,0))),'Y':matrix(((0,-1j),(1j,0))),
    'Z':matrix(((1,0),(0,-1)))}
PAULI={a+b:kron(P1[a],P1[b]) for a,b in product('IXYZ',repeat=2)}
LABELS=tuple(label for label in PAULI if label!='II')
V=matrix(((1,0),(0,0),(0,0),(0,1)))
PLUS=matrix(((.5,.5),(.5,.5)))
MINUS=matrix(((.5,-.5),(-.5,.5)))
ZERO=matrix(((1,0),(0,0)))
ONE=matrix(((0,0),(0,1)))
CNOT=matrix(((1,0,0,0),(0,1,0,0),(0,0,0,1),(0,0,1,0)))


def dilated_prepare(rho):
    # The extra output degree of freedom is a supplied |0> ancilla, not creation
    # of a physical resource from a bare mathematical map.
    return mul(mul(CNOT,kron(rho,ZERO)),adjoint(CNOT))


def prepare(rho):
    return mul(mul(V,rho),adjoint(V))


def pullback(observable):
    return mul(mul(adjoint(V),observable),V)


BELL_PLUS=prepare(PLUS)
BELL_MINUS=prepare(MINUS)
CLASSICAL_MIXTURE=scale(.5,add(prepare(ZERO),prepare(ONE)))


def reduced(rho,side):
    if side=='B':
        return tuple(tuple(sum(rho[2*i+k][2*j+k] for k in (0,1)) for j in (0,1)) for i in (0,1))
    if side=='C':
        return tuple(tuple(sum(rho[2*k+i][2*k+j] for k in (0,1)) for j in (0,1)) for i in (0,1))
    raise ValueError('Unknown output subsystem')


def expectation(rho,label):
    return exact_real(trace(mul(rho,PAULI[label])))


def tomography(rho):
    result=scale(0,I4)
    for label,op in PAULI.items():
        result=add(result,scale(float(expectation(rho,label)/4),op))
    return result


def net_basis(region):
    region=frozenset(region)
    if not region<=frozenset({'B','C'}):
        raise ValueError('Only final-slice regions B and C are modeled')
    return frozenset(a+b for a,b in product('IXYZ',repeat=2)
                     if ('B' in region or a=='I') and ('C' in region or b=='I'))


# Strict partial order of PROCESS EVENTS. This is not an algebra at every event.
EVENTS=frozenset({'a','b','c'})
PRECEDES=frozenset({('a','b'),('a','c')})


def commutes(p,q):
    return mul(PAULI[p],PAULI[q])==mul(PAULI[q],PAULI[p])


def signed_product(p,q):
    result=mul(PAULI[p],PAULI[q])
    for label,op in PAULI.items():
        for sign in (1,-1):
            if result==scale(sign,op):
                return sign,label
    raise ValueError('Product is not Hermitian signed Pauli; use commuting inputs')


def contexts():
    maximal=set()
    for p,q in combinations(LABELS,2):
        if commutes(p,q):
            sign,r=signed_product(p,q)
            maximal.add(frozenset({p,q,r}))
    return tuple(sorted({frozenset()}|{frozenset({p}) for p in LABELS}|maximal,
                        key=lambda c:(len(c),sorted(c))))


CONTEXTS=contexts()


def outcomes(context):
    """Characters of each selected commutative algebra and their projectors.

    Contexts use nonidentity positive Pauli labels. Product signs are retained.
    The empty context represents scalar observables, not an empty algebra.
    """
    if context not in CONTEXTS:
        raise ValueError('Unknown context')
    labels=sorted(context)
    if not labels:
        return ((frozenset(),I4),)
    if len(labels)==1:
        p=labels[0]
        return tuple((frozenset({(p,a)}),scale(.5,add(I4,scale(a,PAULI[p])))) for a in (-1,1))
    p,q,r=labels
    sign,third=signed_product(p,q)
    assert third==r
    return tuple((frozenset({(p,a),(q,b),(r,sign*a*b)}),
                  scale(.25,mul(add(I4,scale(a,PAULI[p])),add(I4,scale(b,PAULI[q])))))
                 for a,b in product((-1,1),repeat=2))


def restrict(character,context):
    return frozenset((label,value) for label,value in character if label in context)


def distribution(rho,context):
    return {character:exact_real(trace(mul(rho,projector))) for character,projector in outcomes(context)}


def restrict_distribution(probabilities,context):
    result={character:Fraction(0) for character,projector in outcomes(context)}
    for character,p in probabilities.items():
        result[restrict(character,context)]+=p
    return result


def global_valuations():
    """All compatible deterministic +/-1 assignments, brute-force over 2^15."""
    constraints=[]
    for context in CONTEXTS:
        if len(context)==3:
            p,q,r=sorted(context)
            sign,third=signed_product(p,q)
            assert third==r
            constraints.append((p,q,r,sign))
    result=[]
    for values in product((-1,1),repeat=len(LABELS)):
        assignment=dict(zip(LABELS,values))
        if all(assignment[p]*assignment[q]*assignment[r]==sign for p,q,r,sign in constraints):
            result.append(frozenset(assignment.items()))
    return tuple(result)


MERMIN_ROWS=(('XI','IX','XX'),('IZ','ZI','ZZ'),('XZ','ZX','YY'))
MERMIN_COLUMNS=tuple(tuple(row[i] for row in MERMIN_ROWS) for i in range(3))


def context_product(labels):
    result=I4
    for label in labels:
        result=mul(result,PAULI[label])
    return result


def local_reset_B(rho):
    # Trace-preserving reset |0><0| and |0><1| on B; C left untouched.
    kraus=(kron(ZERO,I2),kron(matrix(((0,1),(0,0))),I2))
    result=scale(0,I4)
    for k in kraus:
        result=add(result,mul(mul(k,rho),adjoint(k)))
    return result


def selective_z_B(rho,value):
    if value not in (0,1):
        raise ValueError('Binary measurement outcome required')
    k=kron(ZERO if value==0 else ONE,I2)
    unnormalized=mul(mul(k,rho),adjoint(k))
    probability=exact_real(trace(unnormalized))
    conditional=None if probability==0 else scale(float(1/probability),unnormalized)
    return probability,conditional
