"""Clock-controlled chirality write/store/erase on the old cyclic carrier.

The extra long cyclic clock, direction, pointer and switching are specified
resources. Matrix-free reduced-basis checks complement, but do not replace,
the original quantum echo and purified-apparatus factorization.
"""
import numpy as np
from verification.zero_stationary_battery_bridge import STATES,advance,initial_amplitudes
from verification.zero_sphere_chirality_echo_test import readout

INDEX={s:i for i,s in enumerate(STATES)}


def record_gate(chirality,strength=1.):
    """Qutrit |blank>→a|+>+b|−>; extend to a full real unitary."""
    u=readout(chirality,strength);a,b=u[:,0]
    return np.array([[0.,1.,0.],[a,0.,-b],[b,0.,a]])


def period(cycles):
    if not isinstance(cycles,int) or cycles<1:raise ValueError('positive integer cycles required')
    return 20*cycles


def dressing(n,chirality,strength=1.):
    """Pointer has been written at clock readings 10,...,N-1."""
    if n<0:raise ValueError('invalid clock reading')
    return record_gate(chirality,strength) if n>=10 else np.eye(3)


def dress(v,chirality,strength=1.,inverse=False):
    result=np.empty_like(v)
    for n in range(len(v)):
        d=dressing(n,chirality,strength)
        if inverse:d=d.conj().T
        result[n]=v[n]@d.T
    return result


def old_shift(v,q):
    if q not in (1,2) or len(v)%20:raise ValueError('invalid cycle or clock rate')
    out=np.zeros_like(v)
    for n in range(len(v)):
        for i,x in enumerate(STATES):
            out[(n+1)%len(v),INDEX[advance(n%20,x)]]=np.roll(v[n,i],q,axis=0)
    return out


def step(v,q,chirality,strength=1.):
    """W'=D W D†, with gate at 9→10 and inverse at N−1→0."""
    return dress(old_shift(dress(v,chirality,strength,inverse=True),q),chirality,strength)


def history(cycles,q,chirality,strength=1.):
    n=period(cycles)
    if q not in (1,2):raise ValueError('invalid clock rate')
    initial=np.zeros((n,len(STATES),4,3),complex)
    for x,amp in initial_amplitudes().items():initial[0,INDEX[x],0,0]=amp
    current=initial;out=np.zeros_like(initial)
    for _ in range(n):
        out+=current/np.sqrt(n)
        current=step(current,q,chirality,strength)
    return out


def twirled_anchor(v,q,anchor,reference,effect,chirality,strength=1.):
    """Apply sum_k W'^k (|a,r><a,r|⊗effect) W'^−k.

    The old reduced labels are unrestricted: the effect acts as identity on
    them, and old evolution is a permutation. Clock-block formula holds for any
    3×3 pointer effect, including its non-diagonal dressed representatives.
    """
    n=len(v)
    if not (0<=anchor<n and 0<=reference<4):raise ValueError('invalid anchor')
    effect=np.asarray(effect,complex)
    if effect.shape!=(3,3):raise ValueError('expected pointer effect')
    da=dressing(anchor,chirality,strength)
    out=np.zeros_like(v)
    for tick in range(n):
        k=(tick-anchor)%n
        ref=(reference+q*k)%4
        dt=dressing(tick,chirality,strength)
        trans=dt@da.conj().T
        block=trans@effect@trans.conj().T
        out[tick,:,ref,:]=v[tick,:,ref,:]@block.T
    return out


def averaged_effect(v,q,reference,effect,chirality,strength=1.):
    return sum((twirled_anchor(v,q,a,reference,effect,chirality,strength)
                for a in range(len(v))),np.zeros_like(v))/len(v)


def selected(cycles,q,reference):
    return tuple(n for n in range(period(cycles)) if q*n%4==reference)
