"""Finite intervention-equivalence audit; no phenomenal measurements.

Candidate functions annotate a single physical circuit. They do not change its
physical equations. Observing E requires an additional warranted observation
bridge; the simulator does not provide one.
"""
from dataclasses import dataclass
from itertools import product, combinations


@dataclass(frozen=True)
class Intervention:
    x: int
    c: int | None = None
    m: int | None = None
    emit: bool = True

    def __post_init__(self):
        if self.x not in (0,1) or self.c not in (None,0,1) or self.m not in (None,0,1):
            raise ValueError('Binary inputs and overrides required')
        if not isinstance(self.emit,bool):
            raise ValueError('Emission gate must be Boolean')


@dataclass(frozen=True)
class Physical:
    x: int
    c: int
    m: int
    r: int | None


def physical(intervention):
    """C tracks input, M copies C, R reads C directly; overrides cut edges."""
    c=intervention.x if intervention.c is None else intervention.c
    m=c if intervention.m is None else intervention.m
    return Physical(intervention.x,c,m,c if intervention.emit else None)


@dataclass(frozen=True)
class Candidate:
    # Entries at (C,M) = 00,01,10,11. E is a binary TARGET CONTRAST,
    # not necessarily the whole phenomenal episode.
    table: tuple

    def __post_init__(self):
        if len(self.table)!=4 or any(v not in (0,1) for v in self.table):
            raise ValueError('Need binary truth table of length four')

    def evaluate(self,state):
        return self.table[2*state.c+state.m]


CANDIDATES=tuple(Candidate(t) for t in product((0,1),repeat=4))
SOURCE=Candidate((0,0,1,1))
MONITOR=Candidate((0,1,0,1))
CONJUNCTION=Candidate((0,0,0,1))
DISJUNCTION=Candidate((0,1,1,1))


def interventions():
    return tuple(Intervention(*v) for v in product((0,1),(None,0,1),(None,0,1),(False,True)))


def public_signature(candidate,protocols):
    # Deliberately independent of the annotation: the physical model is fixed.
    # A calibrated physical E-readout would be EXTRA structure, not this function.
    return tuple(physical(p) for p in protocols)


def filter_evidence(candidates,evidence):
    """Evidence consists of (physical state, admissible E-values).

    The admissible values must be independently warranted. No likelihood or
    assumption of report faithfulness is inferred from the physical circuit.
    """
    return tuple(f for f in candidates
                 if all(f.evaluate(state) in allowed for state,allowed in evidence))


def baseline_evidence():
    # Stipulated SYNTHETIC calibration: E=0 at 00 and E=1 at 11.
    return tuple((physical(Intervention(x)),frozenset({x})) for x in (0,1))


def minimal_contrast_designs(candidates):
    """Smallest sets of (C,M) states distinguishing all supplied tables."""
    candidates=tuple(candidates)
    states=tuple(product((0,1),repeat=2))
    for size in range(5):
        solutions=[]
        for design in combinations(states,size):
            signatures=[tuple(f.table[2*c+m] for c,m in design) for f in candidates]
            if len(set(signatures))==len(candidates):
                solutions.append(design)
        if solutions:
            return tuple(solutions)
    return ()


def essential_coordinates(candidate):
    """Coordinate dependence over FULL four-state domain, not a subject boundary."""
    result=set()
    for c,m in product((0,1),repeat=2):
        original=candidate.table[2*c+m]
        if candidate.table[2*(1-c)+m]!=original:
            result.add('C')
        if candidate.table[2*c+1-m]!=original:
            result.add('M')
    return frozenset(result)
