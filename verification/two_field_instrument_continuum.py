#!/usr/bin/env python3
"""Finite-M controls and conservative constants for two-field continuum bound.

Numerics do not certify the infinite-dimensional estimates in the report.
NumPy/SciPy: requirements-field-probe.txt.
"""
import json
from math import exp, pi, sqrt, tanh
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import two_field_spacetime_probe as model


def constants(quad=512):
    z,w=np.polynomial.legendre.leggauss(quad)
    raw=np.exp(-1/(1-z*z))
    Z=model.D*np.dot(w,raw)
    F2sq=float(model.D*np.dot(w,raw*raw)/Z**2)
    finf=exp(-1)/Z
    wf=F2sq/(2*pi)
    wa=pi/(model.MA*tanh(pi*model.MA))
    wb=pi/(model.MB*tanh(pi*model.MB))
    kappa=sqrt(wf*sqrt(wa*wb)/4)
    fprime1=2*finf
    return {'F_L2_squared':F2sq,'F_Linf':finf,'Fprime_L1':fprime1,
            'W_F':wf,'W_A':wa,'W_B':wb,'kappa_upper':kappa}


def delta_upper(N,c):
    if not isinstance(N,int) or N<1:raise ValueError('positive integer N required')
    return sqrt(c['W_F']*(sqrt(2*c['W_B']/N)+sqrt(2*c['W_A']/N))/4)


def interaction_bound(N,E,c):
    if E<0:raise ValueError('nonnegative energy required')
    delta=delta_upper(N,c);m=min(model.MA,model.MB)
    const=8*abs(model.LAMBDA)*exp(4*abs(model.LAMBDA)*c['kappa_upper'])*delta
    if E==0:
        return min(2.,2*const),0.
    if const==0:return 0.,0.
    # Optimize R>0 for const*(R/m+2)+4*sqrt(E/R).
    R=(2*sqrt(E)*m/const)**(2/3)
    return min(2.,const*(R/m+2)+4*sqrt(E/R)),R


def readout_upper(N,E,c):
    # Two-sided complex Fourier basis, |h_k| <= ||F'||_1/(sqrt(2pi)|k|).
    L=c['Fprime_L1']
    aa=L*L/(3*pi*N**3)
    tt=L*L/(2*pi*N**2)
    return min(2.,2*abs(model.ETA)*sqrt(4*E*aa+tt))


def mats(M,quad):
    x,wx=model.quadrature(model.D,quad)
    basis=model.basis(M,x+model.Y)
    C=(basis*wx)@basis.T
    oa=model.frequency(M,model.MA);ob=model.frequency(M,model.MB)
    pair=C/(2*np.sqrt(np.outer(oa,ob)))
    return C,oa,ob,pair


def evolve(M,N,C,oa,ob,quad=128):
    d=len(oa);size=4*d
    mask=np.arange(d)<=(2*N)
    CN=C*mask[:,None]*mask[None,:]
    z,w=np.polynomial.legendre.leggauss(quad)
    norm=model.A*np.dot(w,np.exp(-1/(1-z*z)))
    J2=np.block([[np.zeros((d,d)),np.eye(d)],[-np.eye(d),np.zeros((d,d))]])
    J=np.zeros((size,size));J[:2*d,:2*d]=J2;J[2*d:,2*d:]=J2
    def rhs(t,v):
        chi=model.duration_bump(t)/norm
        if chi==0:return np.zeros_like(v)
        ra=np.concatenate((np.diag(np.cos(oa*t)),np.diag(np.sin(oa*t)/oa)),axis=1)
        rb=np.concatenate((np.diag(np.cos(ob*t)),np.diag(np.sin(ob*t)/ob)),axis=1)
        cross=model.LAMBDA*chi*(ra.T@CN@rb)
        K=np.zeros((size,size));K[:2*d,2*d:]=cross;K[2*d:,:2*d]=cross.T
        return (J@K@v.reshape(size,size)).ravel()
    sol=solve_ivp(rhs,(model.T-model.A,model.T+model.A),np.eye(size).ravel(),
                  method='DOP853',rtol=2e-11,atol=2e-13,max_step=.004)
    assert sol.success
    S=sol.y[:,-1].reshape(size,size)
    assert np.max(np.abs(S@J@S.T-J))<1e-9
    gamma0=np.concatenate((1/(2*oa),oa/2,1/(2*ob),ob/2))
    return (S*gamma0)@S.T


def finite_fock_operator_control():
    # Six two-level truncated oscillators (three modes per species). This is
    # a finite-dimensional cross-check of the number-relative constants only.
    C,oa,ob,pair=mats(1,192)
    d=len(oa);modes=2*d;local=2
    a=np.diag(np.sqrt(np.arange(1,local)),1)
    I=np.eye(local)
    def embed(op,which):
        out=np.array([[1.]])
        for j in range(modes):out=np.kron(out,op if j==which else I)
        return out
    ops=[embed(a,j) for j in range(modes)]
    size=local**modes
    number=sum((op.T@op for op in ops),np.zeros((size,size)))
    qs=[(op+op.T)/sqrt(2*float(w)) for op,w in zip(ops,np.r_[oa,ob])]
    interaction=np.zeros((size,size))
    for i in range(d):
        for j in range(d):interaction+=C[i,j]*(qs[i]@qs[d+j])
    inv=np.diag(1/(np.diag(number)+2))
    comm=number@interaction-interaction@number
    small=C[0,0]*(qs[0]@qs[d])
    mask=np.arange(d)>0
    delta=float(np.linalg.norm(pair*(mask[:,None]|mask[None,:])))
    kappa=float(np.linalg.norm(pair))
    vals={'interaction_relative_operator_norm':float(np.linalg.norm(interaction@inv,2)),
          'commutator_relative_operator_norm':float(np.linalg.norm(comm@inv,2)),
          'difference_relative_operator_norm':float(np.linalg.norm((interaction-small)@inv,2)),
          'claimed_interaction_and_commutator_upper':4*kappa,'claimed_difference_upper':4*delta,
          'oscillators':modes,'levels_per_oscillator':local}
    assert vals['interaction_relative_operator_norm']<=4*kappa+1e-12
    assert vals['commutator_relative_operator_norm']<=4*kappa+1e-12
    assert vals['difference_relative_operator_norm']<=4*delta+1e-12
    return vals


def three_dimensional_diagonal_obstruction():
    # Only k+l=0 is counted, so this is a lower bound on the 3D instantaneous
    # pair-kernel HS square, not a bound on the time-evolved channel.
    rows=[]
    for N in (4,8,16,32,64):
        axis=np.arange(-N,N+1,dtype=float)
        r2=axis[:,None,None]**2+axis[None,:,None]**2+axis[None,None,:]**2
        inside=r2<=N*N
        total=np.sum(1/np.sqrt((r2[inside]+model.MA**2)*(r2[inside]+model.MB**2)))
        diagonal=float(total/(4*(2*pi)**6))
        rows.append({'N':N,'instantaneous_pair_kernel_HS_squared_lower':diagonal})
    assert all(a['instantaneous_pair_kernel_HS_squared_lower']<b['instantaneous_pair_kernel_HS_squared_lower'] for a,b in zip(rows,rows[1:]))
    return rows


def main():
    c=constants();M=128
    _,oa,ob,pair=mats(M,384)
    full=float(np.linalg.norm(pair))
    assert full<=c['kappa_upper']+1e-11
    rows=[]
    for N in (1,4,8,16,32,64,96):
        mask=np.arange(len(oa))>(2*N)
        tail=pair*(mask[:,None]|mask[None,:])
        actual=float(np.linalg.norm(tail))
        upper=delta_upper(N,c)
        assert actual<=upper+1e-12
        ib,R=interaction_bound(N,100.,c)
        rows.append({'N':N,'finite_M':M,'finite_M_kernel_tail_HS':actual,
                     'analytic_infinite_tail_HS_upper':upper,
                     'interaction_channel_bound_E100':ib,'optimized_R':R,
                     'readout_channel_bound_E100':readout_upper(N,100.,c)})
    # Two independent Gaussian vacuum outputs in the common M=4 Fock space.
    # Pure Gaussian fidelity is 1/sqrt(det(gamma_N+gamma_M)).
    K=4;C,oa,ob,pair=mats(K,192)
    gm=evolve(K,K,C,oa,ob)
    gaussian=[]
    for N in (0,1,2,3,4):
        gn=evolve(K,N,C,oa,ob)
        sign,logdet=np.linalg.slogdet(gn+gm)
        assert sign>0
        fidelity=min(1.,exp(-logdet/2))
        trace=2*sqrt(max(0.,1-fidelity))
        mask=np.arange(len(oa))>(2*N)
        tail=float(np.linalg.norm(pair*(mask[:,None]|mask[None,:])))
        # Vacuum-specific proof bound using exact finite-M kernel norms.
        vac_bound=min(2.,16*abs(model.LAMBDA)*exp(4*abs(model.LAMBDA)*float(np.linalg.norm(pair)))*tail)
        assert trace<=vac_bound+2e-7
        gaussian.append({'N':N,'finite_M':K,'vacuum_pure_state_trace_distance':trace,
                         'finite_M_vacuum_proof_bound':vac_bound})
    # The same Gaussian-vacuum control at weak coupling has a non-vacuous
    # finite-M bound; N=M also checks the identical-channel limit above.
    original_lambda=model.LAMBDA
    model.LAMBDA=.02
    weak_m=evolve(K,K,C,oa,ob)
    weak_n=evolve(K,2,C,oa,ob)
    sign,ld=np.linalg.slogdet(weak_m+weak_n)
    assert sign>0
    weak_trace=2*sqrt(max(0.,1-min(1.,exp(-ld/2))))
    mask=np.arange(len(oa))>4
    weak_tail=float(np.linalg.norm(pair*(mask[:,None]|mask[None,:])))
    weak_bound=min(2.,16*abs(model.LAMBDA)*exp(4*abs(model.LAMBDA)*float(np.linalg.norm(pair)))*weak_tail)
    assert weak_trace<=weak_bound+2e-7 and weak_bound<2
    model.LAMBDA=original_lambda
    # A round, extremely conservative illustrative sufficient cutoff. The
    # floating-point bound is not accurate enough to locate a minimum integer.
    N=10**52
    assert interaction_bound(N,100.,c)[0]<.01
    result={'status':'passed','scope':'finite-M Gaussian/numerical kernel controls and analytic-constant arithmetic, not an independent proof',
        'constants':c,'finite_M_full_kernel_HS':full,'E':100.,'tail_rows':rows,
        'finite_fock_operator_control':finite_fock_operator_control(),
        'three_dimensional_instantaneous_kernel_lower_bound':three_dimensional_diagonal_obstruction(),
        'vacuum_common_M_gaussian_controls':gaussian,
        'weak_coupling_finite_M_control':{'lambda':.02,'N':2,'M':K,
            'vacuum_trace_distance':weak_trace,'vacuum_bound':weak_bound},
        'interaction_only_illustrative_sufficient_N':N,
        'interaction_only_bound_at_N':interaction_bound(N,100.,c)[0],
        'N_is_not_a_minimum':'round and deliberately enormous; bound is not interval-certified'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
