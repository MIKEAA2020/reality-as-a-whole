"""Transport record-dressed rotations through actual echo and apparatus gates.

The pair is encoded in a finite four-bin copy of the spherical step basis.
Its two angular copies are discrete bin labels, not delta-normalized copies
of a continuous direction. All operators are specified model constructions.
"""
from verification.zero_dynamic_subject_memory_echo_test import jwrite
from verification.zero_internal_contextual_reference_test import value_history
from verification.zero_all_sector_noncommuting_sphere_test import I,kron
from verification.zero_relational_chirality_report_test import apply64
from verification.zero_contextual_sign_symmetry_and_dressed_report_test import valid
from verification.zero_upstream_invariant_internal_history_test import factorization
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project
from verification.zero_dressed_sphere_rotations import transport
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import advance
from verification.zero_clock_finite_reservoir_reuse_test import FORWARD
from verification.zero_coherent_clock_angular_history import checkpoint_at


_T=kron(factorization(),I,I,I)
_PHYSICAL_VALID=_T@valid@_T.conj().T


def full_q(v):
    """Actual Q=I-P+O; value_history supplies O, not the full extension."""
    pv=apply64(_PHYSICAL_VALID,v)
    return v-pv+value_history(pv)


def gate(pair,op):
    a,b=pair
    if op=='T':return jwrite(a,b)
    if op=='Q':return full_q(a),full_q(b)
    raise ValueError('unknown echo gate')


PREFIXES=((),('T',),('T','Q'),('T','Q','T'))


def circuit(pair,ops):
    for op in ops:pair=gate(pair,op)
    return pair


def to_anchor(pair,t):
    """C_3 C_t†, maps actual tick t to the post-echo checkpoint 10."""
    ops=PREFIXES[checkpoint_at(t)]
    return circuit(circuit(pair,reversed(ops)),PREFIXES[3])


def from_anchor(pair,t):
    """C_t C_3†, inverse of to_anchor."""
    return circuit(circuit(pair,reversed(PREFIXES[3])),PREFIXES[checkpoint_at(t)])


def move_tick(pair,t,u_from,u_to,s,frames,shape):
    """Old/R part of clock-dressed transfer; apparatus is separately wound."""
    return from_anchor(transport(to_anchor(pair,t),frames,shape,u_from,u_to,s),t)


def apparatus_prefix(state,t,cols,inverse=False):
    """F_t or F_t† on any apparatus basis state, with B bit included.

    Actual 7 forward operations, 6 identity echo intervals, 7 inverses.
    References and purifiers are spectators, outside this basis tuple.
    """
    if not 0<=t<=20:raise ValueError('invalid tick')
    ops=[(op,False) for op in FORWARD]+[(None,False)]*6+[(op,True) for op in reversed(FORWARD)]
    prefix=ops[:t]
    if inverse:prefix=[(op,not rev) for op,rev in reversed(prefix) if op is not None]
    for op,rev in prefix:
        if op is not None:state=advance(state,op,cols,reverse=rev)
    return state


def apparatus_retarget(state,t,target_b,cols):
    """F_t^(target B) (F_t^(source B))† on an apparatus basis state.

    Not a stand-alone unitary on B: it is the block of a joint unitary whose
    old-record transfer also changes the physical B sector.
    """
    base=apparatus_prefix(state,t,cols,inverse=True)
    return apparatus_prefix((target_b,)+base[1:],t,cols)


def bin_at(u,n=4):
    if n!=4 or not -1<u<1:raise ValueError('requires four bins and interior angle')
    x=(u+1)*n/2
    if abs(x-round(x))<1e-12:raise ValueError('bin boundary')
    return int(x)


def encode_pair(pair,i,s):
    """W_i: isometry from old/R pair to finite constrained pair slices.

    Keys (a,b,z1,z2) represent two angular-copy labels and two sign bits;
    values are the two actual R amplitude arrays. K=s*R*J at anchor 10.
    """
    if i not in range(4) or s not in (1,-1):raise ValueError('invalid input')
    out={}
    for j in (1,-1):
        for r,vec in zip((1,-1),pair):
            k=s*r*j;key=(i,i,k,-k)
            if key not in out:out[key]=[0*pair[0],0*pair[1]]
            out[key][0 if r==1 else 1]+=j_project(vec,j)
    return {key:tuple(value) for key,value in out.items()}


def decode_pair(encoded,i,s,shape_template):
    """W_i†, defined also on arbitrary, possibly nonphysical, pair slices."""
    result=[0*shape_template,0*shape_template]
    for j in (1,-1):
        for ri,r in enumerate((1,-1)):
            k=s*r*j;pair=encoded.get((i,i,k,-k))
            if pair is not None:result[ri]+=j_project(pair[ri],j)
    return tuple(result)


def move_encoded_component(encoded,state,t,u_from,u_to,s,frames,shape,cols):
    """Move one coherent apparatus basis component of a physical pair state.

    This supported fast path assumes each sector has sharp B: 0 for u>0,
    1 for u<0. It is the restriction of the joint unitary described in the
    report; it does not represent its full action on nonphysical pair states.
    Source references and purifiers are unchanged spectators.
    """
    source_b=0 if u_from>0 else 1
    target_b=0 if u_to>0 else 1
    if state[0]!=source_b:raise ValueError('inconsistent physical B sector')
    anchored={key:to_anchor(pair,t) for key,pair in encoded.items()}
    template=next(iter(anchored.values()))[0]
    old=decode_pair(anchored,bin_at(u_from),s,template)
    moved=transport(old,frames,shape,u_from,u_to,s)
    out=encode_pair(moved,bin_at(u_to),s)
    return ({key:from_anchor(pair,t) for key,pair in out.items()},
            apparatus_retarget(state,t,target_b,cols))


def pair_permutation(i,s,r,j,a,b,z1,z2,inverse=False):
    """E_i on the finite pair factors controlled by K=s*r*j.

    E_i is a permutation of the complete finite pair basis. Starting from
    (0,0,+,+), it gives (i,i,k,-k), and W_i is E_i on that reference fiber.
    """
    if i not in range(4) or s not in (1,-1) or r not in (1,-1) or j not in (1,-1):
        raise ValueError('invalid control')
    if a not in range(4) or b not in range(4) or z1 not in (1,-1) or z2 not in (1,-1):
        raise ValueError('invalid pair basis')
    k=s*r*j
    if inverse:return ((a-i)%4,(b-i)%4,k*z1,-k*z2)
    return ((a+i)%4,(b+i)%4,k*z1,-k*z2)
