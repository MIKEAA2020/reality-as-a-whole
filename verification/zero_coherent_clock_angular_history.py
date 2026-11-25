"""The angular quantum echo composed with the actual purified reservoir clock.

Sparse factorization exploits the conserved B sectors. The x/f/e labels are
orthogonal source references and reservoir purifiers, not classical outcomes.
The two B vectors occupy orthogonal subspaces of the original physical system;
there is no added B-copy register. All structures are specified model inputs.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import numpy as np

from verification.zero_clock_finite_reservoir_reuse_test import BITS3, FORWARD, Q, energy
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import advance, distribution, words
from verification.zero_internal_reference_subject_valence_candidates_test import b_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed_before_echo, pulse, mass, difference_mass
from verification.zero_sphere_angular_echo import magnitude

TICKS=20
PULSES=('T','Q','T','T','Q','T')


def apparatus_path(bbit,x,f,e,cols):
    """Actual seven forward steps, six identity echo intervals, and inverses."""
    k=len(e)
    if bbit not in (0,1) or len(cols)!=2 or any(len(col)!=k for col in cols):
        raise ValueError('invalid apparatus input')
    state=(bbit,x,(0,)+f,3,e,k);out=[state]
    for op in FORWARD:
        state=advance(state,op,cols);out.append(state)
    out.extend([state]*6)
    for op in reversed(FORWARD):
        state=advance(state,op,cols,reverse=True);out.append(state)
    return tuple(out)


def apparatus_weight(f,e,aux):
    return F(1,8)*distribution(Q,f)*distribution(aux,e)


def apparatus_overlap(t,u,bbit,cols,aux):
    """Overlap of normalized coherent apparatus states at t,u in one B sector.

    The source references x and reservoir purifiers f,e are retained as
    orthogonal factors in the state, even when they are later traced. Current
    apparatus basis labels are compared, not the entire path or probability law.
    """
    if not (0<=t<TICKS and 0<=u<TICKS):raise ValueError('invalid tick')
    k=len(cols[0]);total=F(0)
    for x,f,e in product(BITS3,BITS3,words(k)):
        path=apparatus_path(bbit,x,f,e,cols)
        if path[t][1:]==path[u][1:]:total+=apparatus_weight(f,e,aux)
    return total


def quantum_event_moments(rows, u, total):
    """Born probabilities and unnormalized positive g-moments on old vectors.

    Joint C=(B equals echo R), D=(R negative); no intermediate measurements.
    A separate query on each clock block defines these commuting effects.
    """
    out=defaultdict(float)
    for r,part in zip((1,-1),rows):
        for i,vec in enumerate(part):
            for b in (1,-1):
                w=norm2(b_project(vec,b))/total
                out[(b==r,r==-1)]+=w
                if r==-1:
                    for kind in ('absolute','swap_invariant'):
                        out[kind]+=w*float(magnitude(u[i],kind))
    return dict(out)


def dot_rows(left,right):
    return sum(np.vdot(a,b) for x,y in zip(left,right) for a,b in zip(x,y))


def quantum_echo_checkpoints(x,s,n):
    """Four actual coherent old-system/echo/angular states, in pulse order."""
    u,v,initial=embed_before_echo(x,s,n);total=norm2(v)
    if total<=0:raise ValueError('zero prepared sign branch')
    first=pulse(initial,'T');second=pulse(first,'Q');third=pulse(second,'T')
    return u,total,(initial,first,second,third)


def checkpoint_at(t):
    if not 0<=t<=TICKS:raise ValueError('invalid tick')
    return (t-7 if 7<=t<=10 else 13-t if 11<=t<=12 else 0)


def clock_selection(q,reference):
    if q not in (1,2) or reference not in range(4):raise ValueError('invalid clock input')
    selected=tuple(t for t in range(TICKS) if q*t%4==reference)
    if not selected:raise ValueError('zero-probability clock event')
    return selected


def stationary_povm_joint(checkpoint_moments,q,reference):
    """Uniform-anchor average of twirled relational effects, conditioned on R.

    This is not a claim that bare |R=reference><R=reference| is stationary.
    The anchor is sampled uniformly, and matching twirled effects are averaged.
    """
    selected=clock_selection(q,reference)
    result=defaultdict(float)
    for t in selected:
        for key,value in checkpoint_moments[checkpoint_at(t)].items():
            result[key]+=value/len(selected)
    return len(selected)/TICKS,dict(result)


def clock_coherence_factor(q,t,u):
    if q not in (1,2) or not (0<=t<TICKS and 0<=u<TICKS):raise ValueError('invalid clock input')
    return int(q*(t-u)%4==0)
