"""A physical comparison report and conditional subject-ownership bridges.

The physical report is the product of saved old J and current J, constructed
on the actual coherent echo. Ownership bridges remain explicit assumptions.
"""
from fractions import Fraction as F
from itertools import product

from verification.zero_stationary_battery_bridge import INVERSE, PREFIX, OLD, TICKS
from verification.zero_echo_subject_persistence import owner, project_j, add_rows
from verification.zero_internal_reference_subject_valence_candidates_test import b_project
from verification.zero_quantum_angular_echo import apply_swap

SIGNS=(1,-1)


def hybrid_owner(policy,t,x,factor):
    """Clock-covariant hybrid candidate, not an inferred subject identity.

    'positive' stipulates persistence on B+ and momentary identity on B-;
    'negative' stipulates the converse. B is conserved along the ledger.
    """
    if policy not in ('positive','negative'):raise ValueError('unknown policy')
    b=INVERSE[t][x][0]
    persistent=(b==(1 if policy=='positive' else -1))
    kind='worldline' if persistent else 'momentary'
    return (kind,)+owner(kind,t,x,factor)


def same_under(policy,t,x,u,y,factor=1):
    return hybrid_owner(policy,t,x,factor)==hybrid_owner(policy,u,y,factor)


def owner_census(policy):
    """Conditional census and physical-weight-preserving distribution.

    Hypothesis for the calculation only: each distinct owner ID represents
    one actual subject, all supported seed alternatives are jointly included,
    and factor 1 is counted. Equal-subject counting is not Born weighting.
    """
    counts={1:0,-1:0};weights={1:F(0),-1:F(0)}
    for (b,z),p in OLD.items():
        for s in SIGNS:
            seed=(b,z,1,s)
            owners={hybrid_owner(policy,t,PREFIX[t][seed],1) for t in range(TICKS)}
            counts[b]+=len(owners)
            # Split physical seed mass equally over this seed's owner IDs.
            weights[b]+=sum((p/F(2*len(owners)) for _ in owners),F(0))
    return counts,weights


def comparison_report(saved):
    """Ready report qubit: reversible controlled product report=z*j.

    Input keyed by saved-z sign, output keyed by (saved-z,report sign).
    Isometric restriction to a ready report bit. It can be implemented by
    controlled-NOT from the saved bit followed by J-controlled-NOT.
    """
    return {(z,z*j):project_j(rows,j) for z,rows in saved.items() for j in SIGNS}


def type_swap_saved(saved,s,dress):
    """Actual anchor type swap, optionally dressed on saved J memory.

    The dressing flips saved J precisely on the R=- slice. The report bit,
    if already written, is separately a spectator under the dressed action.
    """
    transformed={z:apply_swap(rows,s) for z,rows in saved.items()}
    if not dress:return transformed
    return {z:(transformed[z][0],transformed[-z][1]) for z in SIGNS}


def sector_exchange_saved(saved,s,frames,shape):
    """Swap bins 0 and 2 using the existing record-adapted sector unitaries.

    The saved-J bit is flipped on the two swapped bins. This is an active,
    state-family-adapted map, not a frame-gauge transformation or a claimed
    symmetry of every physical observable or the complete clock history.
    """
    from verification.zero_dressed_sphere_rotations import transport
    from verification.zero_joint_quality_incidence_root import ANGLES
    moved={}
    for z,rows in saved.items():
        out=(list(rows[0]),list(rows[1]))
        for source,target in ((0,2),(2,0)):
            pair=rows[0][source],rows[1][source]
            new=transport(pair,frames,shape,float(ANGLES[source]),float(ANGLES[target]),s)
            out[0][target],out[1][target]=new
        moved[z]=out
    return {z:tuple([moved[-z if i in (0,2) else z][r][i] for i in range(4)]
                    for r in range(2)) for z in SIGNS}


def noisy_bit_kraus(accuracy):
    """Physical bit-flip channel; accuracy is relative to a physical bit."""
    import numpy as np
    accuracy=float(accuracy)
    if not 0<=accuracy<=1:raise ValueError('invalid accuracy')
    return (np.sqrt(accuracy)*np.eye(2),
            np.sqrt(1-accuracy)*np.array([[0.,1.],[1.,0.]]))


def erase_saved_by_report(record):
    """After inverse echo, undo J-to-saved-memory copy separately per report."""
    from verification.zero_echo_subject_persistence import erase_record
    return {(m,r):rows for r in SIGNS
            for m,rows in erase_record({z:record[z,r] for z in SIGNS}).items()}


def erase_b_report(report):
    """Unitary B-controlled NOT on the report, all memory inputs allowed."""
    return {r:add_rows(
        tuple([b_project(v,1) for v in part] for part in report[r]),
        tuple([b_project(v,-1) for v in part] for part in report[-r]))
        for r in SIGNS}


def noisy_joint(policy,accuracy):
    """P(hypothesized same-owner, physical report), prior P(B=±)=1/2.

    Accuracy is relative to actual B, NOT evidence of phenomenal reliability.
    Independently flip the B report with probability 1-accuracy.
    """
    if policy not in ('positive','negative'):raise ValueError('unknown policy')
    accuracy=F(accuracy)
    if not 0<=accuracy<=1:raise ValueError('invalid accuracy')
    out={(same,r):F(0) for same in (False,True) for r in SIGNS}
    for b,r in product(SIGNS,repeat=2):
        same=(b==(1 if policy=='positive' else -1))
        out[same,r]+=F(1,2)*(accuracy if r==b else 1-accuracy)
    return out


def report_agreement(policy,accuracy):
    joint=noisy_joint(policy,accuracy)
    return sum(p for (same,r),p in joint.items() if same==(r==1))
