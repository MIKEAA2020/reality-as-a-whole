"""Operationally typed, clock-transported sign process on the echo.

This is a candidate process interface. It does not infer actual subjects,
phenomenal character, incidence measure, or unrestricted access.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from verification.zero_stationary_battery_bridge import (
    OLD,STATES,TICKS,PREFIX,INVERSE,relational_effect,
)

EFFECT=relational_effect(10,lambda x:x[3]*x[1]*x[2]==1)
ACCESS=('B','J','R','L','M')


def value(t,x):
    """The anchor MJR sign transported to clock tick t."""
    if t not in range(TICKS) or x not in STATES:raise ValueError('invalid clock or state')
    return 1 if EFFECT[t][x] else -1


def records(t):
    """Physical diagonal weights with L coherently recorded at tick 7.

    Supports the echo interval only; L has not yet been uncomputed at 13.
    These are effects in one specified protocol, not actual experience events.
    """
    if t not in range(7,14):raise ValueError('outside the memory-retention interval')
    out=[]
    for (b,z),p in OLD.items():
        for s in (1,-1):
            x=PREFIX[t][b,z,1,s]
            out.append((dict(zip(('B','J','R','M'),x))|{'L':z},p/2,value(t,x)))
    return out


def success(t,fields):
    fields=tuple(fields);cells={}
    if any(f not in ACCESS for f in fields):raise ValueError('unknown sign')
    for row,w,k in records(t):
        key=tuple(row[f] for f in fields)
        cell=cells.setdefault(key,{1:F(0),-1:F(0)})
        cell[k]+=w
    return sum((max(w.values()) for w in cells.values()),F(0))


def minimal_access(t):
    good=[]
    for n in range(len(ACCESS)+1):
        for fields in combinations(ACCESS,n):
            s=frozenset(fields)
            if not any(p<=s for p in good) and success(t,fields)==1:good.append(s)
    return frozenset(good)


@dataclass(frozen=True)
class EchoContentProcess:
    """One typed candidate: a physical sign algebra + interval + access.

    This object validates its operational interface, not subjecthood. L is
    the previously stipulated memory, and the process uses the actual echo.
    """
    interval: tuple = tuple(range(7,14))
    access: tuple = ('M','L')
    anchor: int = 10

    def validate(self):
        if self.anchor!=10 or self.interval!=tuple(range(7,14)):
            raise ValueError('unsupported anchor or interval')
        if not set(self.access)<=set(ACCESS):raise ValueError('unknown access')
        return all(success(t,self.access)==1 for t in self.interval)

    def physical_window_weights(self):
        """Joint physical clock/sign weights, not subject-incidence weights."""
        if not self.validate():raise ValueError('content inaccessible')
        from verification.zero_stationary_battery_bridge import stationary_weights
        weights=stationary_weights()
        plus=sum((weights[t][x] for t in self.interval for x in STATES if EFFECT[t][x]),F(0))
        minus=sum((weights[t][x] for t in self.interval for x in STATES if not EFFECT[t][x]),F(0))
        return plus,minus


def joint_independent():
    """P(K,X) for a separately stipulated independent fair sign X."""
    return {(k,x):F(1,4) for k,x in product((1,-1),repeat=2)}


def record_components(x):
    """Actual complex post-echo M and saved-J memory slices.

    The s slices carry orthogonal physical pointer states; z slices carry
    orthogonal extra saved-J memory states. The operation is an isometry,
    not a classical sampling of branches.
    """
    from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
    from verification.zero_echo_subject_persistence import copy_initial_j,evolve_record
    result={}
    for s in (1,-1):
        _,_,ticks=quantum_echo_checkpoints(x,s,4)
        saved=evolve_record(copy_initial_j(ticks[0]),('T','Q','T'))
        result.update({(s,z):rows for z,rows in saved.items()})
    return result


def joint_quality_slices(components):
    """Isometric M/J/L report of (now,echo) on actual anchor vectors.

    On the prepared sector, echo=s*z and now=s*b*z. B projection here
    groups amplitudes; it is not an intermediate physical measurement.
    """
    from verification.zero_internal_reference_subject_valence_candidates_test import b_project
    return {(s,z,b,s*b*z,s*z):tuple([b_project(v,b) for v in part] for part in rows)
            for (s,z),rows in components.items() for b in (1,-1)}


def record_k_slices(components):
    """Add a ready physical report C by copying K=s*z."""
    return {(s,z,s*z):part for (s,z),part in components.items()}


def uncompute_k_slices(record):
    """Undo the same physical controlled-X: output key (s,z,C)."""
    return {(s,z,c*s*z):part for (s,z,c),part in record.items()}
