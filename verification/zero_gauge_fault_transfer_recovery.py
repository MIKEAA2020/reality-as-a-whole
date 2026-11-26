"""Explicit finite environment/fault coupling and written-record recovery.

Carrier order: chirality qutrit B (blank,+,-), loop sign C (+,-), hidden
qubit E, ready fault qubit A. All carriers and gates are stipulated; no spatial
locality, autonomous switching, or physical calibration is inferred here.
"""
import math
import numpy as np
from scipy.linalg import expm

from verification.zero_gauge_clock_joint_instrument import clock_model
from verification.zero_gauge_clock_meta_root import coherent_sensor_window
from verification.zero_noncyclic_chirality_clock import local_step

I2=np.eye(2,dtype=complex)
I3=np.eye(3,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
P0=np.diag([1.,0.]).astype(complex)
P1=np.diag([0.,1.]).astype(complex)
XB=np.array([[0,0,0],[0,0,1],[0,1,0]],dtype=complex)
FB=XB+np.diag([1.,0.,0.])
SIGNS=(1,-1)
CONTEXTS=tuple((b,c) for b in SIGNS for c in SIGNS)


def kron(*args):
    out=np.array([[1.]],dtype=complex)
    for x in args:out=np.kron(out,x)
    return out


def apparatus(theta):
    """U: conditional B/A flip. W: fault-controlled coherent correction."""
    generator=kron(XB,I2,P1,X)
    u=expm(-1j*theta*generator)
    w=kron(I3,I2,I2,P0)+kron(FB,I2,I2,P1)
    return u,w


def prepare_reference(b,c,t):
    """Prepare an explicit sign reference and diagonal environmental state.

    B readiness and sign-control permutations, C readiness, E mixture, and A
    reset are supplied inputs, not a physical preparation derivation.
    """
    if b not in SIGNS or c not in SIGNS or not 0<=t<=1:
        raise ValueError('invalid reference')
    rb=np.zeros((3,3),complex);rb[0,0]=1
    idx=1 if b==1 else 2
    perm=I3.copy();perm[[0,idx]]=perm[[idx,0]]
    rb=perm@rb@perm.conj().T
    rc=P0 if c==1 else X@P0@X
    re=np.diag([1-t,t]).astype(complex)
    return kron(rb,rc,re,P0)


def raw_output(theta,b,c,t,corrected=False):
    u,w=apparatus(theta)
    rho=prepare_reference(b,c,t)
    v=w@u if corrected else u
    out=v@rho@v.conj().T
    diag=out.diagonal().real.reshape(3,2,2,2).sum(axis=(2,3))
    return {(sign,c2):float(diag[i,j]) for i,sign in enumerate((0,1,-1))
            for j,c2 in enumerate(SIGNS)}


def reported_output(theta,b,c,t,pb,pc,corrected=False):
    """Apply separately stipulated independent classical output flips."""
    if not (0<=pb<=1 and 0<=pc<=1):raise ValueError('invalid sign flip')
    source=raw_output(theta,b,c,t,corrected)
    out={(s,c2):0. for s in (0,1,-1) for c2 in SIGNS}
    for (s,c2),prob in source.items():
        for eb in (0,1):
            for ec in (0,1):
                weight=(pb if eb else 1-pb)*(pc if ec else 1-pc)
                sout=s*(-1)**eb if s else 0
                out[sout,c2*(-1)**ec]+=prob*weight
    return out


def mixture_output(theta,context_probs,t_by_context,pb,pc,corrected=False):
    if set(context_probs)!=set(CONTEXTS) or set(t_by_context)!=set(CONTEXTS):
        raise ValueError('four contexts required')
    if any(p<0 for p in context_probs.values()) or not np.isclose(sum(context_probs.values()),1):
        raise ValueError('invalid context probabilities')
    out={(s,c):0. for s in (0,1,-1) for c in SIGNS}
    for ctx in CONTEXTS:
        table=reported_output(theta,*ctx,t_by_context[ctx],pb,pc,corrected)
        for key in out:out[key]+=context_probs[ctx]*table[key]
    return out


def t_transfer_bound(theta,pb,pc,max_diff,delta_q=0.):
    """Response mean bound for this gate, conditional on all other controls."""
    if not (0<=pb<=.5 and 0<=pc<=.5 and 0<=max_diff<=1 and 0<=delta_q<=1):
        raise ValueError('invalid transfer parameters')
    eta=(1-2*pb)*(1-2*pc)
    return min(2.,2*eta*(math.sin(theta)**2*max_diff+delta_q))


def written_ready_bias_bound(pb,pc,wrong_ready):
    """Product-mean bias with arbitrary correlations and bounded A=1 weight.

    Applies only on the written sector, with the declared U/W and independent
    output flips. The bound on wrong_ready must hold in the selected ensemble.
    """
    if not (0<=pb<=.5 and 0<=pc<=.5 and 0<=wrong_ready<=1):
        raise ValueError('invalid ready-state parameters')
    return 2*(1-2*pb)*(1-2*pc)*wrong_ready


def recovered_sensor_residual(n,chirality,step_q,alpha,beta,theta):
    """Actual coherent fixed-effect history shift, E=1 and A initially ready.

    Apply the prescribed U and W throughout the history. The environment is a
    fixed spectator in |1>; its fault qubit is retained, not traced out.
    """
    window=coherent_sensor_window(n,step_q,chirality,alpha,beta)
    recovered={}
    for k,v in window.items():
        zero=v.copy();zero[:,:,1:,:]*=math.cos(theta)
        one=v.copy();one[:,:,0,:]=0;one[:,:,1:,:]*=-1j*math.sin(theta)
        recovered[k]=np.stack((zero,one),axis=-1)
    shifted={}
    for k,v in recovered.items():
        z=np.stack([np.stack([local_step(v[...,s,a],k,step_q,chirality)
                              for a in (0,1)],axis=-1)
                    for s in (0,1)],axis=-2)
        shifted[k+1]=z
    residual=0.
    zero=np.zeros_like(recovered[0])
    for k in range(n+1):
        delta=shifted.get(k,zero)-recovered.get(k,zero)
        residual+=float(np.vdot(delta,delta).real)
    return math.sqrt(max(0.,residual))


def analytic_recovered_residual(n,alpha,beta,theta):
    """Same residual, using the declared coherent readout and E=1."""
    from verification.zero_gauge_clock_joint_instrument import clock_residuals
    f,_,_,_=clock_model(n,alpha,beta)
    gamma=math.sqrt((1-alpha)*beta)+math.sqrt(alpha*(1-beta))
    prior=clock_residuals(n,alpha,beta)['coherent']
    return math.sqrt(prior*prior+2*f[9]*f[10]*gamma*(1-math.cos(theta)))
