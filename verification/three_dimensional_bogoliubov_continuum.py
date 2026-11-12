#!/usr/bin/env python3
"""Finite-cutoff controls for the nonperturbative 3D Bogoliubov argument.

The implemented calculations do not prove the continuum statement. Dependencies:
requirements-field-probe.txt. Work in the real oscillator basis from the prior
3D verifier, and use a shared M-mode space for both cutoffs.
"""
import json
from math import exp, pi, sqrt
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import three_dimensional_smooth_probe_gate as model
import two_field_instrument_continuum as previous


def primitive_constants():
    base=previous.constants()
    f2_3=base['F_L2_squared']**3
    finf_3=base['F_Linf']**3
    wf=f2_3/model.V
    def z4_upper(m):return m**-4+4*pi*pi+pi**4/45
    za,zb=z4_upper(model.MA),z4_upper(model.MB)
    h=sqrt(wf*sqrt(za*zb)/16)
    def delta(n):
        tail=24/n+2/(3*n**3)
        return sqrt(wf*(sqrt(tail*zb)+sqrt(za*tail))/16)
    return {'F3_L2_squared':f2_3,'F3_Linf':finf_3,'W_F':wf,
            'Z_A4_upper':za,'Z_B4_upper':zb,'single_block_primitive_HS_upper':h},delta


def primitive_sum(M,check_N):
    k,oa,ob=model.labels(M);G,_=model.spectral_functions(2*M)
    tail2={n:0. for n in check_N};full=0.
    high={n:np.max(np.abs(k),axis=1)>n for n in check_N}
    for i in range(0,len(k),64):
        plus=k[i:i+64,None,:]+k[None,:,:]
        fh=np.prod(G[np.abs(plus)],axis=2)/model.V
        den=2*np.sqrt(oa[i:i+64,None]*ob[None,:])*(oa[i:i+64,None]+ob[None,:])
        q=(fh/den)**2
        full+=float(np.sum(q))
        for n in check_N:
            tail2[n]+=float(np.sum(q*(high[n][i:i+64,None]|high[n][None,:])))
    return sqrt(full),{n:sqrt(v) for n,v in tail2.items()}


def bogoliubov(M,N,lam,rtol=1e-9):
    C,oa,ob,_,_=model.quadratures3(M,0.)
    d=len(oa);size=4*d
    # Real cosine/sine basis ordering comes from pairing +k,-k. Their cube
    # membership is identical, recover it from frequencies for cubic M<=2 by
    # using the explicit unitary basis construction instead of a radial mask.
    k,_,_=model.labels(M)
    used=set();keep=[True]
    for vec in k:
        key=tuple(vec);neg=tuple(-vec)
        if key==(0,0,0) or key in used:continue
        flag=max(abs(int(x)) for x in key)<=N
        keep.extend((flag,flag));used.update((key,neg))
    mask=np.array(keep)
    assert len(mask)==d
    C=C*mask[:,None]*mask[None,:]
    K=C/(2*np.sqrt(np.outer(oa,ob)))
    z,w=np.polynomial.legendre.leggauss(128)
    norm=model.A*np.dot(w,np.exp(-1/(1-z*z)))
    def rhs(t,flat):
        S=flat.reshape(size,size)
        s0,s1,s2,s3=np.split(S,4,axis=0)
        chi=model.old.duration_bump(t)/norm
        if chi==0:return np.zeros_like(flat)
        phase_a=np.exp(1j*oa*t);phase_b=np.exp(1j*ob*t)
        m=K*phase_a[:,None]*phase_b.conj()[None,:]
        p=K*phase_a[:,None]*phase_b[None,:]
        result=np.concatenate((-1j*lam*chi*(m@s1+p@s3),
            -1j*lam*chi*(m.conj().T@s0+p.T@s2),
            1j*lam*chi*(m.conj()@s3+p.conj()@s1),
            1j*lam*chi*(m.T@s2+p.conj().T@s0)),axis=0)
        return result.ravel()
    initial=np.eye(size,dtype=complex).ravel()
    sol=solve_ivp(rhs,(model.T-model.A,model.T+model.A),initial,method='DOP853',
                  rtol=rtol,atol=rtol/100,max_step=.01)
    if not sol.success:raise RuntimeError(sol.message)
    S=sol.y[:,-1].reshape(size,size)
    alpha=S[:2*d,:2*d];beta=S[:2*d,2*d:]
    ccr1=float(np.max(np.abs(alpha@alpha.conj().T-beta@beta.conj().T-np.eye(2*d))))
    ccr2=float(np.max(np.abs(alpha@beta.T-beta@alpha.T)))
    assert ccr1<2e-8 and ccr2<2e-8
    return alpha,beta,{'M':M,'N':N,'lambda':lam,'modes_per_field':d,
        'beta_HS_squared':float(np.linalg.norm(beta)**2),
        'CCR_diagonal_defect':ccr1,'CCR_pair_defect':ccr2}


def main():
    constants,delta=primitive_constants()
    full,tails=primitive_sum(6,(1,2,4,5))
    assert full<=constants['single_block_primitive_HS_upper']+1e-12
    primitive=[]
    for n in (1,2,4,5):
        assert tails[n]<=delta(n)+1e-12
        primitive.append({'N':n,'M':6,'finite_M_single_block_tail_HS':tails[n],
                          'infinite_tail_HS_majorant':delta(n)})
    a1,b1,row1=bogoliubov(1,1,1.)
    a2,b2,row2=bogoliubov(2,2,1.)
    a12,b12,row12=bogoliubov(2,1,1.)
    assert abs(row1['beta_HS_squared']-row12['beta_HS_squared'])<1e-9
    _,_,negative=bogoliubov(1,1,-1.)
    _,_,zero=bogoliubov(1,1,0.)
    _,_,refined=bogoliubov(1,1,1.,rtol=2e-11)
    assert abs(negative['beta_HS_squared']-row1['beta_HS_squared'])<1e-11
    assert zero['beta_HS_squared']<1e-26
    assert abs(refined['beta_HS_squared']-row1['beta_HS_squared'])<1e-9
    weak_a,weak_b,weak=bogoliubov(1,1,.02)
    pair=model.first_order_pairs(1)['first_order_pair_norm_squared']
    leading=2*.02**2*pair
    assert abs(weak['beta_HS_squared']/leading-1)<.01
    result={'status':'passed','scope':'finite-M primitive sums and finite-mode nonperturbative Bogoliubov ODE controls, not a continuum proof',
        'primitive_constants':constants,'finite_M6_single_block_primitive_HS':full,
        'primitive_tail_controls':primitive,
        'full_coupling_bogoliubov_rows':[row1,row12,row2],
        'zero_coupling_control':zero,'sign_reversed_coupling_control':negative,
        'N1_ODE_refinement':refined,
        'common_M2_beta_difference_HS':float(np.linalg.norm(b12-b2)),
        'common_M2_alpha_difference_operator_norm':float(np.linalg.norm(a12-a2,2)),
        'weak_coupling':{'result':weak,'first_order_expected_beta_HS_squared':leading,
                         'ratio':weak['beta_HS_squared']/leading}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
