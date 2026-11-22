#!/usr/bin/env python3
"""Finite-window, unsharp orientation POVM and stipulated dust-control dilation.

The reported figures are quadrature/FFT witnesses, not certified error bounds.
Analytic positivity, resource assumptions and caveats are in the report.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import eval_genlaguerre, gammaln

if __package__:
    from .dust_orientation_record import N,N0,PMAX,BETA,EB,WIDTH,nu,grav_energies,target_state,analytic_bounds
else:
    from dust_orientation_record import N,N0,PMAX,BETA,EB,WIDTH,nu,grav_energies,target_state,analytic_bounds

QLO,QHI=.5,1.5
S=.25
I=np.eye(N,dtype=complex)


def effects(p, points=4096, panels=64, ymin=-20., ymax=4.):
    """Compressed Gaussian phase-space effects for negative/positive D.

    Trapezoidal frequency with zero bin split, Simpson in q. The exact POVM
    is a continuum integral; this function returns an approximation to it.
    """
    if points<=0 or panels<=0 or panels%2 or ymin>=ymax: raise ValueError('invalid quadrature')
    y=ymin+np.arange(points)*(ymax-ymin)/points
    dy=(ymax-ymin)/points
    z=BETA*np.exp(2*y)
    alpha=nu(p)
    fields=np.empty((N,points))
    for j in range(N):
        n=N0+j
        lognorm=.5*(math.log(2)+(alpha+1)*math.log(BETA)+gammaln(n+1)-gammaln(n+alpha+1))
        fields[j]=np.exp(lognorm+(alpha+1)*y-z/2)*eval_genlaguerre(n,alpha,z)
    k=2*math.pi*np.fft.fftfreq(points,d=dy)
    dk=2*math.pi/(ymax-ymin)
    negative=(k<0).astype(float)+.5*(k==0)
    positive=(k>0).astype(float)+.5*(k==0)
    e=np.zeros((N,N),complex);c=np.zeros((N,N),complex)
    dq=(QHI-QLO)/panels
    for j in range(panels+1):
        q=QLO+j*dq
        gaussian=(math.pi*S*S)**(-.25)*np.exp(-(y-q)**2/(2*S*S))
        amplitudes=np.fft.fft(fields*gaussian,axis=1)*dy/math.sqrt(2*math.pi)
        weight=1 if j in (0,panels) else (4 if j%2 else 2)
        e+=weight*(amplitudes.conj()*negative)@amplitudes.T*dk*dq/3
        c+=weight*(amplitudes.conj()*positive)@amplitudes.T*dk*dq/3
    return (e+e.conj().T)/2,(c+c.conj().T)/2


def positive_sqrt(a,tolerance=1e-9):
    v,u=np.linalg.eigh((a+a.conj().T)/2)
    if min(v)<-tolerance: raise ArithmeticError('effect is not positive at this numerical resolution')
    return (u*np.sqrt(np.maximum(v,0)))@u.conj().T


def dilation(e,c):
    """Householder extension of the three-effect square-root instrument."""
    no=I-e-c
    Ks=[positive_sqrt(no),positive_sqrt(e),positive_sqrt(c)]
    q=[np.eye(3,dtype=complex)[:,j:j+1] for j in range(3)]
    J=np.kron(I,q[0])
    V=sum(np.kron(K,qj) for K,qj in zip(Ks,q))
    T=J-V
    # All singular values are positive in this particular numerical code;
    # the analytic definition uses the projection onto the full range.
    u,s,_=np.linalg.svd(T,full_matrices=False)
    if min(s)<1e-8: raise ArithmeticError('singular numerical reflection chart')
    P=u@u.conj().T
    return Ks,J,V,P,float(min(s))


def pulse_check(p,e,c):
    Ks,J,V,P,smin=dilation(e,c)
    A=np.repeat(grav_energies(p),3)
    psi=J@target_state(True)
    def rhs(t,state):
        phase=np.exp(1j*A*t)
        transformed=phase*(P@(phase.conjugate()*state))
        g=2*math.pi/WIDTH*math.sin(math.pi*t/WIDTH)**2
        return -1j*((-A+EB)*state+g*transformed)
    result=solve_ivp(rhs,(0,WIDTH),psi,method='DOP853',rtol=1e-10,atol=1e-12)
    if not result.success: raise RuntimeError(result.message)
    expected=np.exp(1j*A*WIDTH-1j*EB*WIDTH)*(V@target_state(True))
    direct=(np.eye(3*N)-2*P)@J
    return {'state_max_error':float(np.max(abs(result.y[:,-1]-expected))),
            'reflection_max_error':float(np.max(abs(direct-V))),
            'projector_max_error':float(np.max(abs(P@P-P))),
            'completeness_max_error':float(np.max(abs(sum(K.conj().T@K for K in Ks)-I))),
            'minimum_T_singular_value':smin}


def outcome(p,e,c,expanding=True):
    no=I-e-c
    w=target_state(expanding)
    vals=[float(np.vdot(w,A@w).real) for A in (e,c,no)]
    Ks=[positive_sqrt(no),positive_sqrt(e),positive_sqrt(c)]
    A=np.diag(grav_energies(p))
    initial=float(np.vdot(w,A@w).real)
    after=sum(float(np.vdot(K@w,A@(K@w)).real) for K in Ks)
    return {'expanding_label':vals[0],'contracting_label':vals[1],
            'outside_window':vals[2],'delta_mean_A':after-initial}


def run():
    # Actual packet uniform in scalar p, not a fixed-p eigenstate.
    values=[]
    panels_p=8
    sums=np.zeros((2,4))
    sums4=np.zeros((2,4))
    for j in range(panels_p+1):
        p=-PMAX+2*PMAX*j/panels_p
        e,c=effects(p)
        ev=np.linalg.eigvalsh(e);cv=np.linalg.eigvalsh(c);nv=np.linalg.eigvalsh(I-e-c)
        assert min(ev)>-1e-9 and min(cv)>-1e-9 and min(nv)>-1e-9
        pair=[outcome(p,e,c,flag) for flag in (True,False)]
        weight=1 if j in (0,panels_p) else (4 if j%2 else 2)
        for a,row in enumerate(pair):
            v=np.array(list(row.values()))
            sums[a]+=weight*v
            if j%2==0:
                j4=j//2
                weight4=1 if j4 in (0,4) else (4 if j4%2 else 2)
                sums4[a]+=weight4*v
        values.append({'p':p,'minimum_effect_eigenvalues':[float(min(ev)),float(min(cv)),float(min(nv))]})
    sums/=3*panels_p
    sums4/=12
    keys=['expanding_label','contracting_label','outside_window','delta_mean_A']
    packet={name:dict(zip(keys,map(float,sums[i]))) for i,name in enumerate(('expanding','contracting'))}
    for row in packet.values(): assert abs(sum(row[k] for k in keys[:3])-1)<1e-10
    e,c=effects(.05)
    refined=effects(.05,points=8192,panels=128,ymin=-32,ymax=4)
    refinement=max(float(np.max(abs(x-y))) for x,y in zip((e,c),refined))
    refine_norm=max(float(np.linalg.norm(x-y,ord=2)) for x,y in zip((e,c),refined))
    oo=outcome(.05,e,c,True)
    rr=outcome(.05,*refined,True)
    outcome_refine=max(abs(oo[k]-rr[k]) for k in keys[:3])
    pulse=pulse_check(.05,e,c)
    assert refinement<1e-5 and max(pulse[k] for k in ('state_max_error','reflection_max_error',
                                                      'projector_max_error','completeness_max_error'))<1e-8
    pband=analytic_bounds()
    return {'status':'passed',
            'scope':'Unsharp joint POVM with stipulated nonlocal dust control; not a localized crossing detector or B7 pass.',
            'window_y':[QLO,QHI],'corresponding_readout_volume':[math.exp(2*QLO),math.exp(2*QHI)],
            'gaussian_s':S,'q_readout_noise_standard_deviation':S/math.sqrt(2),
            'wrong_sign_marginal_bound_for_abs_D_at_least_8':.5*math.erfc(S*8),
            'outside_expanded_window_accept_bound_for_delta_0_5':.5*math.erfc(.5/S),
            'uniform_scalar_packet_outcomes':packet,'effect_eigenvalue_samples':values,
            'quadrature_refinement_max_effect_entry_difference':refinement,
            'quadrature_refinement_max_effect_operator_difference':refine_norm,
            'midband_refinement_max_outcome_difference':outcome_refine,
            'scalar_packet_simpson_4_vs_8_max_difference':float(np.max(abs(sums-sums4))),
            'abstract_dust_pulse_checks_at_p_0_05':pulse,
            'relational_dust_energy_lower_bound':pband['relational_dust_energy_lower']}


def main():
    r=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__': main()
