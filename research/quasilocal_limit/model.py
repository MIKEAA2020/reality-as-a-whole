"""Finite-support Pauli algebra on the integer lattice.

Exact symbolic phases and supports; no infinite matrix or global infinite product
unitary is assumed. The quasi-local completion argument is in REPORT.md, not
established by finite tests alone.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Pauli:
    # Represents i**phase X**x Z**z, with all X factors ordered before Z.
    phase: int = 0
    x: frozenset = frozenset()
    z: frozenset = frozenset()

    def __post_init__(self):
        object.__setattr__(self,'phase',self.phase%4)
        object.__setattr__(self,'x',frozenset(self.x))
        object.__setattr__(self,'z',frozenset(self.z))
        if any(not isinstance(i,int) for i in self.x|self.z):
            raise ValueError('Integer lattice sites required')

    @property
    def support(self):
        return self.x|self.z

    def __mul__(self,other):
        return Pauli(self.phase+other.phase+2*len(self.z&other.x),
                     self.x^other.x,self.z^other.z)

    def adjoint(self):
        return Pauli(-self.phase+2*len(self.x&self.z),self.x,self.z)

    def hermitian(self):
        return self==self.adjoint()

    def translated(self,offset):
        if not isinstance(offset,int):
            raise ValueError('Integer shift required')
        return Pauli(self.phase,{i+offset for i in self.x},{i+offset for i in self.z})

    def word(self,sites):
        sites=tuple(sites)
        if len(set(sites))!=len(sites) or not self.support<=set(sites):
            raise ValueError('Word domain must contain support without repeats')
        label=''.join('Y' if i in self.x&self.z else 'X' if i in self.x else 'Z' if i in self.z else 'I' for i in sites)
        coefficient=(1,1j,-1,-1j)[(self.phase-len(self.x&self.z))%4]
        return coefficient,label


def from_word(word,start=0):
    if any(c not in 'IXYZ' for c in word):
        raise ValueError('Unknown Pauli character')
    return Pauli(word.count('Y'),{start+i for i,c in enumerate(word) if c in 'XY'},
                 {start+i for i,c in enumerate(word) if c in 'YZ'})


ONE=Pauli()


def cnot_conjugate(p,control,target):
    if control==target:
        raise ValueError('Distinct sites required')
    x,z=set(p.x),set(p.z)
    if control in x:
        x.symmetric_difference_update({target})
    if target in z:
        z.symmetric_difference_update({control})
    return Pauli(p.phase,x,z)


def pair_left(site,parity):
    if parity not in (0,1):
        raise ValueError('Parity is zero or one')
    return site if site%2==parity else site-1


def layer(p,parity):
    # Infinite disjoint layer acts on a local operator through finitely many gates.
    lefts=sorted({pair_left(i,parity) for i in p.support})
    result=p
    for left in lefts:
        result=cnot_conjugate(result,left,left+1)
    return result


def alpha(p):
    # State evolution: even layer THEN odd layer.
    # Observable pullback therefore conjugates odd layer THEN even layer.
    return layer(layer(p,1),0)


def inverse_alpha(p):
    return layer(layer(p,0),1)


def evolve(p,periods):
    if not isinstance(periods,int):
        raise ValueError('Integer number of periods required')
    transform=alpha if periods>=0 else inverse_alpha
    for _ in range(abs(periods)):
        p=transform(p)
    return p


def cone(region,periods):
    if not isinstance(periods,int):
        raise ValueError('Integer number of periods required')
    result=set(region)
    parities=(1,0) if periods>=0 else (0,1)
    for _ in range(abs(periods)):
        for parity in parities:
            result.update(j for i in tuple(result) for j in (pair_left(i,parity),pair_left(i,parity)+1))
    return frozenset(result)


def validate_window(window):
    lo,hi=window
    if not isinstance(lo,int) or not isinstance(hi,int) or lo>hi:
        raise ValueError('Nonempty inclusive integer interval required')


def embed(p,small,large):
    validate_window(small)
    validate_window(large)
    if not large[0]<=small[0]<=small[1]<=large[1] or any(not small[0]<=i<=small[1] for i in p.support):
        raise ValueError('Inclusion and operator support must agree')
    return p  # Identity extension preserves global site anchors.


def finite_layer(p,parity,window):
    validate_window(window)
    lo,hi=window
    if any(not lo<=i<=hi for i in p.support):
        raise ValueError('Operator outside finite window')
    result=p
    for left in range(lo,hi):
        if left%2==parity:
            result=cnot_conjugate(result,left,left+1)
    return result


def finite_evolve(p,periods,window):
    validate_window(window)
    if not isinstance(periods,int):
        raise ValueError('Integer number of periods required')
    if any(not window[0]<=i<=window[1] for i in p.support):
        raise ValueError('Operator outside finite window')
    parities=(1,0) if periods>=0 else (0,1)
    for _ in range(abs(periods)):
        for parity in parities:
            p=finite_layer(p,parity,window)
    return p


def commutes(a,b):
    return a*b==b*a


@dataclass(frozen=True)
class ProductState:
    # Supplied states: Z +/- eigenstates 0/1, X +/- eigenstates +/-.
    default: str = '0'
    overrides: tuple = ()

    def __post_init__(self):
        valid={'0','1','+','-'}
        if self.default not in valid or any(v not in valid for i,v in self.overrides):
            raise ValueError('Unknown one-site state')
        if len({i for i,v in self.overrides})!=len(self.overrides):
            raise ValueError('Conflicting site overrides')
        if any(not isinstance(i,int) for i,v in self.overrides):
            raise ValueError('Integer lattice sites required')

    def expectation(self,p):
        result=(1,1j,-1,-1j)[p.phase]
        chosen=dict(self.overrides)
        for i in p.support:
            value=chosen.get(i,self.default)
            x,z=i in p.x,i in p.z
            if x and z:
                return 0
            if x:
                if value not in ('+','-'):
                    return 0
                result*=1 if value=='+' else -1
            if z:
                if value not in ('0','1'):
                    return 0
                result*=1 if value=='0' else -1
        return result

    def evolved_expectation(self,p,periods):
        return self.expectation(evolve(p,periods))


def mermin_contexts(start=0):
    words=(('XI','IX','XX'),('IZ','ZI','ZZ'),('XZ','ZX','YY'))
    rows=tuple(tuple(from_word(word,start) for word in row) for row in words)
    columns=tuple(tuple(row[i] for row in rows) for i in range(3))
    return rows+columns


def context_products(contexts,periods):
    result=[]
    for context in contexts:
        value=ONE
        for p in context:
            value=value*evolve(p,periods)
        result.append(value)
    return tuple(result)
