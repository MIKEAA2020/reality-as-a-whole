"""Why the echo's sign symmetries do not fix its local magnitude law.

Formal structural assignments only: no subject, experience, physical energy,
actuality or ontological necessity is implied by these calculations.
"""
from fractions import Fraction as F
from itertools import product

SIGNS=(1,-1)
CELLS=tuple(product(SIGNS,repeat=2))


def vector(n,k,agree,disagree):
    """Complete counterpart/type-swap covariant family on four sign cells."""
    if n not in SIGNS or k not in SIGNS:raise ValueError('invalid sign')
    g=F(agree if n==k else disagree)
    return (g*n,g*k)


def flip_now(cell):return (-cell[0],cell[1])
def flip_echo(cell):return (cell[0],-cell[1])
def counterpart(cell):return (-cell[0],-cell[1])
def type_swap(cell):return (cell[1],cell[0])
def vector_flip_now(v):return (-v[0],v[1])
def vector_flip_echo(v):return (v[0],-v[1])
def vector_negate(v):return (-v[0],-v[1])
def vector_swap(v):return (v[1],v[0])


def equivariant(table,operations):
    if set(table)!=set(CELLS):raise ValueError('need all cells')
    return all(table[physical(c)]==output(table[c])
               for c in CELLS for physical,output in operations)


BASIC=((counterpart,vector_negate),(type_swap,vector_swap))
INDEPENDENT=((flip_now,vector_flip_now),(flip_echo,vector_flip_echo),
             (type_swap,vector_swap))


def table(agree,disagree):
    return {c:vector(*c,agree,disagree) for c in CELLS}


def orbit(seed,operations):
    if seed not in CELLS:raise ValueError('invalid seed')
    seen={seed};pending=[seed]
    while pending:
        c=pending.pop()
        for op in operations:
            x=op(c)
            if x not in seen:seen.add(x);pending.append(x)
    return frozenset(seen)


def second_moment(agree,disagree):
    """Per-coordinate Born second moment for the actual uniform cell table."""
    return (F(agree)**2+F(disagree)**2)/2
