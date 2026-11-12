#!/usr/bin/env python3
"""Finite-mode Gaussian controls for the two-field probe report.

Run with NumPy/SciPy from requirements-field-probe.txt. Numerical convergence
and finite-dimensional symplectic calculations are not continuum QFT proofs.
"""
from math import exp, pi, sin, sqrt
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp

D=.4
A=.08
Y=pi/2
T=.3
T_READ=.55
MA=.5
MB=.7
G=1.
LAMBDA=1.
ETA=1.
FLIP=.1


def quadrature(width, count):
    z,w=np.polynomial.legendre.leggauss(count)
    raw=w*np.exp(-1/(1-z*z))
    return width*z,raw/raw.sum()


def basis(nmax,x):
    cols=[np.ones_like(x)/sqrt(2*pi)]
    for n in range(1,nmax+1):
        cols.extend((np.cos(n*x)/sqrt(pi),np.sin(n*x)/sqrt(pi)))
    return np.array(cols)


def frequency(nmax,mass):
    return np.array([mass]+[sqrt(k*k+mass*mass) for k in range(1,nmax+1) for _ in (0,1)])


def duration_bump(t):
    z=(t-T)/A
    return 0. if abs(z)>=1 else exp(-1/(1-z*z))


def calc(N,quad=128,rtol=2e-10,source_center=0.):
    x,wx=quadrature(D,quad)
    st,wt=quadrature(A,quad)
    b0=basis(N,x)
    by=basis(N,x+Y)
    d=b0.shape[0];size=4*d
    fs=basis(N,x+source_center)@wx
    hr=by@wx
    C=(by*wx)@by.T
    oa=frequency(N,MA);ob=frequency(N,MB)
    ha=np.cos(np.outer(oa,st))@wt
    hb=np.cos(np.outer(ob,st))@wt
    # χ_d(t) = smooth normalized bump centered at T.
    z,zweights=np.polynomial.legendre.leggauss(quad)
    norm=A*np.dot(zweights,np.exp(-1/(1-z*z)))
    J2=np.block([[np.zeros((d,d)),np.eye(d)],[-np.eye(d),np.zeros((d,d))]])
    J=np.zeros((size,size));J[:2*d,:2*d]=J2;J[2*d:,2*d:]=J2
    eye=np.eye(size)
    def rhs(t,flat):
        chi=duration_bump(t)/norm
        if chi==0:return np.zeros_like(flat)
        ra=np.concatenate((np.diag(np.cos(oa*t)),np.diag(np.sin(oa*t)/oa)),axis=1)
        rb=np.concatenate((np.diag(np.cos(ob*t)),np.diag(np.sin(ob*t)/ob)),axis=1)
        cross=LAMBDA*chi*(ra.T@C@rb)
        K=np.zeros((size,size));K[:2*d,2*d:]=cross;K[2*d:,:2*d]=cross.T
        return (J@K@flat.reshape(size,size)).ravel()
    sol=solve_ivp(rhs,(T-A,T+A),eye.ravel(),method='DOP853',
                  rtol=rtol,atol=rtol/100,max_step=.004)
    if not sol.success:raise RuntimeError(sol.message)
    S=sol.y[:,-1].reshape(size,size)
    symplectic=float(np.max(np.abs(S@J@S.T-J)))
    assert symplectic<5e-9
    # Integrated source A_s = sum f_n hat(ω_n) p_n, since χ_s is even.
    av=np.zeros(size);av[d:2*d]=fs*ha
    delta=(S.T-eye)@av
    u=np.concatenate((delta[:d],delta[2*d:3*d]))
    v=np.concatenate((delta[d:2*d],delta[3*d:]))
    omegas=np.concatenate((oa,ob))
    c=float(np.sum(u*u/(omegas*omegas)+v*v))
    d0=float(np.sum(u*u/omegas+omegas*v*v))
    def full_order_bound(E):
        return min(2.,2*abs(G)*(sqrt(2*E*c)+sqrt(d0/2)))
    # Probe readout: localized probe-field smear, smooth temporal profile
    # centered T_READ, followed by an idealized finite-strength qubit readout.
    ell=np.zeros(size)
    ell[2*d:3*d]=hr*hb*np.cos(ob*T_READ)
    ell[3*d:]=hr*hb*np.sin(ob*T_READ)/ob
    covdiag=np.concatenate((1/(2*oa),oa/2,1/(2*ob),ob/2))
    cov=(S*covdiag)@S.T
    variance=float(ell@cov@ell)
    shift=float(ell@S@J@av*G)
    before=.5*(1+exp(-2*ETA*ETA*variance)*sin(2*ETA*shift))
    after=.5
    tv=(1-2*FLIP)*abs(before-after)
    assert 2*tv<=full_order_bound(0)+1e-9
    freq_h=np.concatenate((oa*oa,np.ones(d),ob*ob,np.ones(d)))
    output_diag=np.diag(cov)
    baseline=covdiag
    sys_energy=.5*float(np.dot(freq_h[:2*d],(output_diag-baseline)[:2*d]))
    probe_energy=.5*float(np.dot(freq_h[2*d:],(output_diag-baseline)[2*d:]))
    energy_inject=sys_energy+probe_energy
    assert sys_energy>=-1e-8 and probe_energy>=-1e-8
    source_vac_energy=.5*G*G*float(np.sum(oa*oa*fs*fs*ha*ha))
    readout_energy=.5*ETA*ETA*float(np.sum(hr*hr*hb*hb))
    return {'N':N,'modes_per_field':d,'symplectic_defect_max':symplectic,
            'source_response_coefficient_energy_C':c,'source_response_vacuum_D0':d0,
            'complete_order_trace_upper_E0':full_order_bound(0),
            'complete_order_trace_upper_E100':full_order_bound(100),
            'vacuum_pointer_mean_shift':shift,'vacuum_two_noisy_bits_tv':tv,
            'vacuum_probe_readout_variance':variance,
            'vacuum_interaction_system_energy':sys_energy,
            'vacuum_interaction_probe_energy':probe_energy,
            'vacuum_interaction_total_energy':energy_inject,
            'source_vacuum_energy':source_vac_energy,
            'probe_readout_additional_energy':readout_energy}


def main():
    global LAMBDA
    assert Y-2*D>T+2*A
    rows=[calc(n) for n in (0,1,2,3,4,6,8,10,12)]
    LAMBDA=0.
    zero=calc(4)
    LAMBDA=1.
    assert zero['source_response_coefficient_energy_C']<1e-26
    assert zero['vacuum_interaction_total_energy']<1e-12
    assert zero['vacuum_two_noisy_bits_tv']<1e-12
    LAMBDA=-1.
    negative=calc(4)
    LAMBDA=1.
    positive=next(row for row in rows if row['N']==4)
    for key in ('source_response_vacuum_D0','vacuum_interaction_total_energy'):
        assert abs(negative[key]-positive[key])<1e-10
    assert abs(negative['vacuum_pointer_mean_shift']+positive['vacuum_pointer_mean_shift'])<1e-10
    # Positive control: source colocated with the interaction, so its earlier
    # support is not spacelike from the probe coupling.
    local=calc(12,source_center=Y)
    assert local['vacuum_two_noisy_bits_tv']>1e-3
    fine=calc(8,quad=192,rtol=2e-12)
    coarse=next(r for r in rows if r['N']==8)
    for key in ('source_response_vacuum_D0','vacuum_pointer_mean_shift',
                'vacuum_interaction_total_energy','vacuum_probe_readout_variance'):
        assert abs(fine[key]-coarse[key])<2e-9, (key,fine[key],coarse[key])
    for row in rows:
        assert row['symplectic_defect_max']<5e-9
        assert 2*row['vacuum_two_noisy_bits_tv']<=row['complete_order_trace_upper_E0']+1e-9
    result={'status':'passed',
            'scope':'finite-mode ODE/quadrature, vacuum controls, not a certified continuum or gravity result',
            'source_probe_support_minimum_spatial_gap':Y-2*D,
            'source_probe_support_maximum_time_separation':T+2*A,
            'source_mass':MA,'probe_mass':MB,'source_strength':G,'coupling':LAMBDA,
            'readout_strength':ETA,'smooth_probe_readout_center_time':T_READ,
            'rows':rows,'N8_refined':fine,'zero_coupling_control':zero,
            'negative_coupling_control_N4':negative,
            'timelike_colocated_source_positive_control_N12':local}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
