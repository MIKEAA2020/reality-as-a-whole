#!/usr/bin/env python3
"""Controls for the 3D quantitative channel certificate; not a proof.

Uses pinned requirements-field-probe.txt, the earlier 3D Bogoliubov solver,
and an independent finite-Fock squeezer/rotation matrix control.
"""
import json
from math import cos, exp, log10, pi, sin, sinh, sqrt
from pathlib import Path
import numpy as np
from scipy.linalg import expm
import two_field_instrument_continuum as one
import three_dimensional_smooth_probe_gate as geom
import three_dimensional_bogoliubov_continuum as prev


def constants(lam):
    base=one.constants(); primitive,delta=prev.primitive_constants()
    f=primitive['F3_Linf'];ma=geom.MA;mb=geom.MB
    h=sqrt(2)*primitive['single_block_primitive_HS_upper']
    chi_inf=base['F_Linf']*geom.D/geom.A
    chi_prime=2*chi_inf
    chi2=base['F_L2_squared']*geom.D/geom.A
    c=f/sqrt(ma*mb)
    L=abs(lam)*c
    nu=exp(L)
    Q=chi_inf+chi_prime+abs(lam)*c*chi2
    B=abs(lam)*h*nu**2*Q
    d0=f*(1/sqrt(ma)+1/sqrt(mb))
    t0=24+2/3
    dd0=sqrt(2)*sqrt(primitive['W_F']*(sqrt(t0*primitive['Z_B4_upper'])+
                                    sqrt(primitive['Z_A4_upper']*t0))/16)
    e0=nu*abs(lam)*d0
    I0=abs(lam)*(dd0*nu*Q+h*e0*Q+h*abs(lam)*d0*nu*chi2)
    db0=nu*(I0+abs(lam)*d0*B)
    a0=nu*e0
    b0=nu*db0+B*e0
    return {'lambda':lam,'c':c,'L':L,'nu':nu,'primitive_HS_upper':h,
            'chi_infinity':chi_inf,'chi_derivative_L1':chi_prime,'chi_L2_squared':chi2,
            'Q':Q,'beta_uniform_upper':B,'D0':d0,'primitive_tail_coefficient':dd0,
            'e0':e0,'beta_difference_coefficient':db0,
            'relative_alpha_coefficient':a0,'relative_beta_coefficient':b0}


def detailed(n,lam):
    if not isinstance(n,int) or n<1:raise ValueError('positive integer cutoff required')
    C=constants(lam);nu=C['nu'];h=C['primitive_HS_upper']
    d=C['D0']/sqrt(n)
    _,dt=prev.primitive_constants();dh=sqrt(2)*dt(n)
    e=nu*abs(lam)*d
    I=abs(lam)*(dh*nu*C['Q']+h*e*C['Q']+h*abs(lam)*d*nu*C['chi_L2_squared'])
    db=nu*(I+abs(lam)*d*C['beta_uniform_upper'])
    return {'generator_tail':d,'primitive_tail_HS':dh,'S_difference_op':e,
            'beta_difference_HS':db,'relative_alpha_minus_identity_op':nu*e,
            'relative_beta_HS':nu*db+C['beta_uniform_upper']*e}


def channel_bound(n,E,R,lam):
    if E<0 or R<=0:raise ValueError('E>=0 and R>0 required')
    v=detailed(n,lam);k=int(R/min(geom.MA,geom.MB))
    a=v['relative_alpha_minus_identity_op'];b=v['relative_beta_HS']
    restricted=b*(k+2)+k*(a+b*b/2)
    return min(2.,2*restricted+4*sqrt(E/R))


def asymptotic_coefficient(E,lam):
    if E<0:raise ValueError('energy must be nonnegative')
    v=constants(lam);a=v['relative_alpha_coefficient'];b=v['relative_beta_coefficient'];m=min(geom.MA,geom.MB)
    return 2*(b*(1/m+2)+a/m+b*b/(2*m))+4*sqrt(E)


def matrix_squeezer(levels,r,theta,K):
    a=np.diag(np.sqrt(np.arange(1,levels)),1);I=np.eye(levels)
    A=np.kron(a,I);B=np.kron(I,a)
    number=A.T@A+B.T@B
    G=r*(A.T@B.T-A@B)
    W=expm(G)@np.diag(np.exp(-1j*theta*np.diag(number)))
    idx=np.flatnonzero(np.diag(number)<=K)
    distance=float(np.linalg.norm((W-np.eye(levels**2))[:,idx],2))
    alpha=abs(cos(theta)*np.cosh(r)+1j*sin(theta)*np.cosh(r)-1)
    beta=sqrt(2)*sinh(abs(r))
    bound=beta*(K+2)+K*(alpha+beta*beta/2)
    assert distance<=bound+1e-12
    return {'levels_per_oscillator':levels,'r':r,'theta':theta,'particle_cutoff':K,
            'restricted_unitary_operator_distance':distance,'squeeze_rotation_bound':bound,
            'relative_alpha_op':alpha,'relative_beta_HS':beta}


def main():
    checks=[matrix_squeezer(12,.01,.02,2),matrix_squeezer(14,.01,.02,2)]
    assert abs(checks[0]['restricted_unitary_operator_distance']-checks[1]['restricted_unitary_operator_distance'])<1e-10
    # Low but nonzero coupling yields a nonvacuous numerical application of
    # the same all-input analytic bounds, for a common finite 3D mode space.
    lam=.001
    an,bn,_=prev.bogoliubov(2,1,lam)
    am,bm,_=prev.bogoliubov(2,2,lam)
    ar=am.conj().T@an-bm.T@bn.conj()
    br=am.conj().T@bn-bm.T@an.conj()
    actual_a=float(np.linalg.norm(ar-np.eye(len(ar)),2))
    actual_b=float(np.linalg.norm(br))
    bd=detailed(1,lam)
    assert actual_a<=bd['relative_alpha_minus_identity_op']+1e-12
    assert actual_b<=bd['relative_beta_HS']+1e-12
    sign,ld=np.linalg.slogdet(ar)
    assert abs(sign)>0
    fidelity=min(1.,exp(-ld))
    vac_trace=2*sqrt(max(0.,1-fidelity))
    vac_bound=channel_bound(1,0.,.1,lam)
    assert vac_trace<=vac_bound+1e-7
    full=constants(1.)
    coefficient=asymptotic_coefficient(100.,1.)
    log10_suff=12*(log10(coefficient)-log10(.01))
    # This decimal exponent is rounded UP; no integer minimality is claimed.
    exponent=int(np.ceil(log10_suff+1e-8))
    assert coefficient*10**(-exponent/12)<.01
    assert channel_bound(1,0.,.1,0.)==0
    result={'status':'passed','scope':'finite-dimensional matrix and finite-mode ODE controls, plus floating-point arithmetic; not a proof or interval certificate',
        'full_strength_constants':full,'E100_asymptotic_coefficient':coefficient,
        'interaction_only_round_base10_sufficient_exponent_for_0_01':exponent,
        'interaction_only_bound_at_that_power':coefficient*10**(-exponent/12),
        'finite_fock_squeezing_controls':checks,
        'weak_3d_control':{'lambda':lam,'N':1,'M':2,'actual_relative_alpha_op':actual_a,
            'bound_relative_alpha_op':bd['relative_alpha_minus_identity_op'],
            'actual_relative_beta_HS':actual_b,'bound_relative_beta_HS':bd['relative_beta_HS'],
            'vacuum_trace_distance':vac_trace,'vacuum_channel_upper':vac_bound},
        'sample_full_strength_interaction_bounds':[{'N':n,'E':100,'R':10,
            'bound':channel_bound(n,100.,10.,1.)} for n in (1,4,16,64)]}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
