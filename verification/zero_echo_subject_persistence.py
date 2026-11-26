"""Physical record and conditional ownership controls on the coherent echo.

Ownership partitions are hypotheses over clock-indexed occurrence slots, not
physical observables or evidence that any slot is actually experienced.
The auxiliary memory is a newly stipulated ready register and coupling.
"""
from fractions import Fraction as F
from itertools import product

from verification.zero_joint_quality_incidence_root import R,J,SIGNS
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_quantum_angular_echo import pulse,mass,difference_mass
from verification.zero_stationary_battery_bridge import TICKS as CYCLE, PREFIX, INVERSE, STATES, advance

TICKS=(7,10,13)


def partitions():
    """Three different subject-identity relations on the same three slots."""
    return {'persistent':(0,0,0),'fresh':(0,1,2),'returning':(0,1,0)}


def component_partitions():
    """Ownership hypotheses for transported pair factors, not subject facts.

    Each row corresponds to the six labels in component_slots(). In
    particular, these labels do not establish independent physical copies.
    """
    return {'composite':(0,0,0,0,0,0),
            'two_persistent':(0,1,0,1,0,1),
            'six_momentary':(0,1,2,3,4,5)}


def component_slots():return tuple(product(TICKS,(1,2)))


def same_owner(rule,t,u):
    if rule not in partitions() or t not in TICKS or u not in TICKS:
        raise ValueError('unknown rule or tick')
    owners=partitions()[rule]
    return owners[TICKS.index(t)]==owners[TICKS.index(u)]


def owner(policy,t,x,factor):
    """Two clock-covariant candidate ownership rules on the reduced ledger.

    Seed is the initial state transported to tick t. Factor is a stipulated
    pair-component label; these maps do not establish subjecthood or actuality.
    """
    if policy not in ('worldline','momentary') or t not in range(CYCLE) or x not in STATES or factor not in (1,2):
        raise ValueError('invalid ownership input')
    seed=INVERSE[t][x]
    return (seed,factor) if policy=='worldline' else (t,seed,factor)


def refined_owner(policy,t,x,factor,tag,tag_sensitive=False):
    """Alternative ownership extensions for a separately recorded binary tag.

    The tag is not assumed to be an alias: it can label two distinct physical
    refined outcomes, while whether it splits subjecthood is another input.
    """
    if tag not in (0,1):raise ValueError('invalid refinement tag')
    base=owner(policy,t,x,factor)
    return base+(tag,) if tag_sensitive else base


def shift_slot(t,x,factor):
    if t not in range(CYCLE) or x not in STATES or factor not in (1,2):raise ValueError('invalid slot')
    return (t+1)%CYCLE,advance(t,x),factor


def shift_owner(policy,identity):
    if policy=='worldline':return identity
    if policy=='momentary':return ((identity[0]+1)%CYCLE,)+identity[1:]
    raise ValueError('unknown policy')


def table():
    """Finite physical joint law of (i,s,z,b,j,r), not a path ontology."""
    return {(i,s,R[i]*J[i],R[i],J[i],R[i]):F(1,8)
            for i,s in product(range(4),SIGNS)}


def best_guess(fields,target):
    """Optimal deterministic guess in a specified commuting sign algebra."""
    fields=tuple(fields)
    allowed=('i','s','z','b','j','r')
    if not set(fields)<=set(allowed) or target not in ('now','echo','b'):
        raise ValueError('unknown field or target')
    cells={}
    for row,p in table().items():
        record=dict(zip(allowed,row));key=tuple(record[x] for x in fields)
        value={'now':record['s']*record['j'],
               'echo':record['s']*record['j']*record['r'],
               'b':record['b']}[target]
        if key not in cells:cells[key]={1:F(0),-1:F(0)}
        cells[key][value]+=p
    return sum((max(v.values()) for v in cells.values()),F(0))


def project_j(rows,sign):
    if sign not in SIGNS:raise ValueError('invalid sign')
    return tuple([j_project(v,sign) for v in part] for part in rows)


def add_rows(a,b):
    return tuple([x+y for x,y in zip(p,q)] for p,q in zip(a,b))


def copy_initial_j(rows):
    """Isometry |psi>|ready +> -> P_+psi|+> + P_-psi|->."""
    return {z:project_j(rows,z) for z in SIGNS}


def evolve_record(record,operations):
    out=dict(record)
    for gate in operations:out={z:pulse(v,gate) for z,v in out.items()}
    return out


def compare_j_masses(record):
    """Joint Born masses of preserved initial record z and current J sign."""
    return {(z,j):mass(project_j(rows,j)) for z,rows in record.items() for j in SIGNS}


def erase_record(record):
    """Apply the same J-controlled NOT, now with arbitrary memory inputs.

    The returned slices are indexed by final memory sign. This is valid at
    any time; recovery of the *ready* memory needs J to match the saved value.
    """
    return {m:add_rows(project_j(record[m],1),project_j(record[-m],-1)) for m in SIGNS}


def record_fidelity(record,unrecorded):
    """Fidelity of the old pure state against tracing this extra record."""
    from verification.zero_coherent_clock_angular_history import dot_rows
    total=mass(unrecorded)
    return sum(abs(dot_rows(unrecorded,rows))**2 for rows in record.values())/total**2
