"""Bilateral-clock chirality write without an erase.

One controlled step, an unbounded ideal clock and all control resources are
stipulated. Finite-support histories have only approximate stationarity.
"""
import numpy as np
from verification.zero_stationary_battery_bridge import STATES,advance,initial_amplitudes
from verification.zero_clocked_chirality_history import INDEX,record_gate


def local_step(block,n,q,chirality,strength=1.):
    if block.shape!=(len(STATES),4,3) or q not in (1,2):raise ValueError('invalid input')
    result=np.zeros_like(block)
    for i,x in enumerate(STATES):
        result[INDEX[advance(n%20,x)]]=np.roll(block[i],q,axis=0)
    if n==9:result=result@record_gate(chirality,strength).T
    return result


def forward_blocks(n,q,chirality,strength=1.):
    if n<1:raise ValueError('positive block count required')
    block=np.zeros((len(STATES),4,3),complex)
    for x,a in initial_amplitudes().items():block[INDEX[x],0,0]=a
    blocks=[block]
    for k in range(n-1):blocks.append(local_step(blocks[-1],k,q,chirality,strength))
    return np.stack(blocks)


def sine_envelope(n):
    if n<1:raise ValueError('positive support required')
    return np.sqrt(2/(n+1))*np.sin(np.pi*np.arange(1,n+1)/(n+1))


def window_history(n,q,chirality,strength=1.):
    f=sine_envelope(n);blocks=forward_blocks(n,q,chirality,strength)
    return f[:,None,None,None]*blocks


def shifted_window(v,q,chirality,strength=1.):
    out=np.zeros((len(v)+1,)+v.shape[1:],complex)
    for n in range(len(v)):out[n+1]=local_step(v[n],n,q,chirality,strength)
    return out


def residual(v,q,chirality,strength=1.):
    a=np.zeros((len(v)+1,)+v.shape[1:],complex);a[:len(v)]=v
    return float(np.linalg.norm(shifted_window(v,q,chirality,strength)-a))
