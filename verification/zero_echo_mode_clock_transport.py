"""Clock transport of echo-mode Lüders instruments on the record algebra.

The 20-tick finite matrix model is a record-algebra representation of the
specified echo, not the full apparatus or a physical–experiential bridge.
"""
from itertools import product
import numpy as np

from verification.zero_coherent_clock_angular_history import checkpoint_at

BASIS=tuple(product((1,-1),repeat=3))  # (B,J,R)
INDEX={state:i for i,state in enumerate(BASIS)}
COARSE=(-1,0,1)
FINE=((-1,0),(0,-1),(0,1),(1,0))


def logical_pulse(state,gate):
    b,j,r=state
    if gate=='T':return b,j,j*r
    if gate=='Q':return b,b*j,r
    raise ValueError('invalid gate')


def logical_circuit(state,ops):
    for gate in ops:state=logical_pulse(state,gate)
    return state


PREFIXES=((),('T',),('T','Q'),('T','Q','T'))


def mode_values(j,r,sign):
    if j not in (-1,1) or r not in (-1,1) or sign not in (-1,1):
        raise ValueError('expected sign bits')
    n=sign*j;k=sign*j*r
    return ((n+k)//2,(n-k)//2)


def past_labels(checkpoint,b,j,r):
    """Anchor J,R in terms of commuting B,J,R at an earlier checkpoint.

    Q transports J to BJ only on the specified valid physical sector.
    T is the full J-controlled R flip. The reduced model acts faithfully on
    the record algebra but does not represent all old-system degrees of freedom.
    """
    if checkpoint not in range(4) or any(x not in (-1,1) for x in (b,j,r)):
        raise ValueError('invalid label')
    return ((b*j,b*r),(b*j,b*j*r),(j,j*r),(j,r))[checkpoint]


def permutation(ops):
    matrix=np.zeros((8,8))
    for column,state in enumerate(BASIS):matrix[INDEX[logical_circuit(state,ops)],column]=1.
    return matrix


def anchor_projector(sign,kind,outcome):
    if sign not in (-1,1):raise ValueError('invalid sign')
    allowed=COARSE if kind=='coarse' else FINE if kind=='fine' else ()
    if outcome not in allowed:raise ValueError('invalid mode outcome')
    values=[]
    for b,j,r in BASIS:
        s,t=mode_values(j,r,sign)
        values.append(float(s==outcome if kind=='coarse' else (s,t)==outcome))
    return np.diag(values)


def forward(t):
    """Record permutation from tick 0 to t of the 20-step echo cycle."""
    if t not in range(21):raise ValueError('invalid clock tick')
    return permutation(PREFIXES[checkpoint_at(t)])


def clock_shift():
    """W maps |t>⊗state to |t+1>⊗U_t state, including wrap."""
    w=np.zeros((160,160))
    for t in range(20):
        to=(t+1)%20
        step=forward(t+1)@forward(t).T
        w[8*to:8*(to+1),8*t:8*(t+1)]=step
    return w


def anchored_history_projector(sign,kind,outcome):
    """Twirl of the anchor-10 effect; an invariant 160-dimensional projector."""
    e=anchor_projector(sign,kind,outcome)
    p0=forward(10).T@e@forward(10)
    out=np.zeros((160,160))
    for t in range(20):
        f=forward(t)
        out[8*t:8*(t+1),8*t:8*(t+1)]=f@p0@f.T
    return out


def write_unitary(sign,kind):
    """Invariant global readout with a distinct ready state and outcome states.

    The clock-controlled operation is a specified algebraic construction; its
    localization, autonomous control, resources and experiential semantics are
    not derived. Pointer basis is ready=0 and outcome indices 1,...,m.
    """
    outcomes=COARSE if kind=='coarse' else FINE if kind=='fine' else None
    if outcomes is None:raise ValueError('invalid instrument')
    dim=len(outcomes)+1
    unitary=np.zeros((160*dim,160*dim))
    for i,outcome in enumerate(outcomes,1):
        swap=np.eye(dim)
        swap[[0,i]]=swap[[i,0]]
        unitary+=np.kron(anchored_history_projector(sign,kind,outcome),swap)
    return unitary


def bare_anchor_projector(sign,kind,outcome):
    out=np.zeros((160,160))
    out[80:88,80:88]=anchor_projector(sign,kind,outcome)
    return out


def instantaneous_history_projector(sign,kind,outcome):
    """Naive fixed effect at each tick: generally not transported/invariant."""
    e=anchor_projector(sign,kind,outcome)
    return np.kron(np.eye(20),e)


def uniform_history(psi0):
    """Normalized stationary history of a normalized 8-dimensional record ket."""
    psi=np.asarray(psi0,dtype=complex)
    if psi.shape!=(8,) or not np.isclose(np.vdot(psi,psi),1.):
        raise ValueError('expected normalized eight-dimensional ket')
    return np.concatenate([forward(t)@psi for t in range(20)])/np.sqrt(20)
