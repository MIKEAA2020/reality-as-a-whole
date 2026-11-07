"""Finite dynamical locality across three slices; not relativistic QFT.

Reuses the prior construction's matrix primitives in a distinct import namespace.
All supplied states/gates use small exactly representable dyadic Gaussian entries.
"""
from dataclasses import dataclass
from functools import lru_cache
import importlib.util
from itertools import product
from pathlib import Path

_spec=importlib.util.spec_from_file_location('framework_overlap_reference',Path(__file__).resolve().parents[1]/'framework_overlap'/'model.py')
_ref=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ref)
matrix,identity,mul,adjoint,kron,scale,add,trace,exact_real=(getattr(_ref,name) for name in
    ('matrix','identity','mul','adjoint','kron','scale','add','trace','exact_real'))
P1,ZERO,ONE,PLUS,MINUS=_ref.P1,_ref.ZERO,_ref.ONE,_ref.PLUS,_ref.MINUS
I8=identity(8)
STATES=tuple(product((0,1),repeat=3))
SCHEDULE=((0,1),(1,2))
PAULI={''.join(labels):kron(kron(P1[labels[0]],P1[labels[1]]),P1[labels[2]])
       for labels in product('IXYZ',repeat=3)}


def tensor3(a,b,c):
    return kron(kron(a,b),c)


def cnot(control,target):
    if control==target or control not in range(3) or target not in range(3):
        raise ValueError('Distinct sites required')
    result=[[0]*8 for _ in range(8)]
    for column,state in enumerate(STATES):
        output=list(state)
        output[target]^=state[control]
        row=4*output[0]+2*output[1]+output[2]
        result[row][column]=1
    return matrix(result)


GATES=tuple(cnot(c,t) for c,t in SCHEDULE)
INITIAL=tensor3(ZERO,ZERO,ZERO)
PLUS_INITIAL=tensor3(PLUS,PLUS,ZERO)


def validate_interval(start,end):
    if not isinstance(start,int) or not isinstance(end,int) or not 0<=start<=end<=2:
        raise ValueError('Need 0 <= start <= end <= 2')


@lru_cache(None)
def unitary(start,end):
    validate_interval(start,end)
    result=I8
    for gate in GATES[start:end]:
        result=mul(gate,result)
    return result


def evolve(rho,start,end):
    u=unitary(start,end)
    return mul(mul(u,rho),adjoint(u))


def pullback(observable,start,end):
    u=unitary(start,end)
    return mul(mul(adjoint(u),observable),u)


@lru_cache(None)
def at_origin(label,time):
    return pullback(PAULI[label],0,time)


@lru_cache(None)
def signed_pullback(label,start,end):
    translated=pullback(PAULI[label],start,end)
    for candidate,op in PAULI.items():
        for sign in (1,-1):
            if translated==scale(sign,op):
                return sign,candidate
    raise AssertionError('Clifford schedule should preserve signed Pauli labels')


def support(label):
    return frozenset(i for i,value in enumerate(label) if value!='I')


def local_label(site,value):
    if site not in range(3) or value not in 'IXYZ' or len(value)!=1:
        raise ValueError('Unknown site or Pauli')
    return ''.join(value if i==site else 'I' for i in range(3))


def net_basis(region):
    region=frozenset(region)
    if not region<=frozenset(range(3)):
        raise ValueError('Unknown site')
    return frozenset(label for label in PAULI if support(label)<=region)


def past_cone(region,start,end):
    validate_interval(start,end)
    result=set(region)
    if not result<=set(range(3)):
        raise ValueError('Unknown site')
    for pair in reversed(SCHEDULE[start:end]):
        if result.intersection(pair):
            result.update(pair)
    return frozenset(result)


@dataclass(frozen=True,order=True)
class Event:
    time: int
    site: int

    def __post_init__(self):
        if self.time not in range(3) or self.site not in range(3):
            raise ValueError('Unknown wire-time event')


EVENTS=tuple(Event(t,i) for t in range(3) for i in range(3))


def precedes(a,b):
    return a.time<b.time and a.site in past_cone({b.site},a.time,b.time)


def causally_disconnected(a,b):
    return a!=b and not precedes(a,b) and not precedes(b,a)


def commute(a,b):
    return mul(a,b)==mul(b,a)


def embed(local_operator,site):
    factors=[P1['I']]*3
    if site not in range(3):
        raise ValueError('Unknown site')
    factors[site]=local_operator
    return tensor3(*factors)


def apply_kraus(rho,kraus):
    result=scale(0,I8)
    for k in kraus:
        result=add(result,mul(mul(k,rho),adjoint(k)))
    return result


def reset_kraus(site):
    return (embed(ZERO,site),embed(matrix(((0,1),(0,0))),site))


def intervene(rho,time,site,kind):
    state=evolve(rho,0,time)
    if kind=='reset':
        return apply_kraus(state,reset_kraus(site))
    if kind in ('X','Z'):
        k=embed(P1[kind],site)
        return mul(mul(k,state),adjoint(k))
    raise ValueError('Unknown intervention')


def perturbed_evolve(rho,intervention_time,site,kind,end):
    validate_interval(intervention_time,end)
    changed=intervene(rho,intervention_time,site,kind)
    return evolve(changed,intervention_time,end)


def expectation(rho,observable):
    return exact_real(trace(mul(rho,observable)))


def region_reduce(rho,region):
    """Partial trace in fixed site order, including empty and full regions."""
    keep=tuple(sorted(region))
    if len(set(keep))!=len(keep) or not set(keep)<=set(range(3)):
        raise ValueError('Unknown or repeated region site')
    omitted=tuple(i for i in range(3) if i not in keep)
    values=tuple(product((0,1),repeat=len(keep)))
    def index(kept,rest):
        assignment=dict(zip(keep,kept))|dict(zip(omitted,rest))
        return sum(assignment[i]*2**(2-i) for i in range(3))
    return tuple(tuple(sum(rho[index(a,rest)][index(b,rest)] for rest in product((0,1),repeat=len(omitted)))
                       for b in values) for a in values)


def transported_mermin_products(time):
    # Prior two-qubit parity square on sites 0/1, identity on site 2.
    contexts=_ref.MERMIN_ROWS+_ref.MERMIN_COLUMNS
    result=[]
    for context in contexts:
        op=I8
        for label in context:
            op=mul(op,at_origin(label+'I',time))
        result.append(op)
    return tuple(result)
