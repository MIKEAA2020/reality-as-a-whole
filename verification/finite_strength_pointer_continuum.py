#!/usr/bin/env python3
"""Numerical controls for the finite-strength pointer argument, not a proof.

Requires NumPy, pinned in requirements-framework-battery.txt. The finite-Fock
matrix check is separate from Gaussian and continuum-tail arithmetic.
"""
import json
from math import cos, erf, exp, pi, sin, sqrt
from pathlib import Path
import numpy as np
from continuum_complete_instrument_bound import (
    B0, D, OMEGA0, Y, post_source_energy, source_bound, tails, w,
)


def b(n):
    return B0+sum(w(k)**2*cos(k*Y)**2/pi for k in range(1,n+1))


def probe_bound(n,E,lam):
    z=tails(n)
    return min(2.,2*abs(lam)*sqrt(4*E*z['A_q']+z['T_q']))


def bounds(n,E,g,lam):
    source_first=min(2.,source_bound(n,E,g)+probe_bound(n,post_source_energy(E,g),lam))
    # Fixed ground pointer, independent input, unread pointer measurement.
    probe_first=min(2.,probe_bound(n,E,lam)+source_bound(n,E+lam**2/(6*D),g))
    return source_first,probe_first


def first_sufficient(E,g,lam,target):
    if not 0<target<2:raise ValueError('target must be between 0 and 2')
    lo=hi=1
    while max(bounds(hi,E,g,lam))>target:hi*=2
    while lo<hi:
        mid=(lo+hi)//2
        if max(bounds(mid,E,g,lam))<=target:hi=mid
        else:lo=mid+1
    assert max(bounds(lo,E,g,lam))<=target and (lo==1 or max(bounds(lo-1,E,g,lam))>target)
    return lo


def matrix_control():
    # Two modes: zero and n=2. Low occupation vacuum, with an explicit
    # finite-dimensional approximation to oscillator position and energy.
    L=24
    annih=np.diag(np.sqrt(np.arange(1,L)),1)
    q0=(annih+annih.T)/sqrt(2*OMEGA0)
    q2=(annih+annih.T)/sqrt(4)
    number=np.diag(np.arange(L))
    identity=np.eye(L)
    H=OMEGA0*np.kron(number,identity)+2*np.kron(identity,number)
    h0=sqrt(B0);h2=w(2)*cos(2*Y)/sqrt(pi)
    Q=h0*np.kron(q0,identity)+h2*np.kron(identity,q2)
    # Symmetric diagonalization gives functions of Q, not a displacement formula.
    eigenvalues,eigenvectors=np.linalg.eigh(Q)
    v=np.zeros(L*L);v[0]=1
    coeff=eigenvectors.T@v
    lam=1.
    plus=eigenvectors@((np.cos(lam*eigenvalues)+np.sin(lam*eigenvalues))*coeff)/sqrt(2)
    minus=eigenvectors@((np.cos(lam*eigenvalues)-np.sin(lam*eigenvalues))*coeff)/sqrt(2)
    pp=float(plus@plus);pm=float(minus@minus)
    field_energy=float(plus@(H@plus)+minus@(H@minus))
    prediction=lam**2*(h0*h0+h2*h2)/2
    assert abs(pp+pm-1)<1e-12
    assert abs(field_energy-prediction)<1e-10
    # A non-vacuum complex state has a nonzero momentum expectation. The
    # prepared pointer, not a vanishing field momentum, cancels the cross term.
    excited=np.zeros(L*L,dtype=complex)
    excited[0]=1/sqrt(2);excited[1]=1j/sqrt(2)
    coeff2=eigenvectors.T@excited
    plus2=eigenvectors@((np.cos(lam*eigenvalues)+np.sin(lam*eigenvalues))*coeff2)/sqrt(2)
    minus2=eigenvectors@((np.cos(lam*eigenvalues)-np.sin(lam*eigenvalues))*coeff2)/sqrt(2)
    before2=float(np.vdot(excited,H@excited).real)
    after2=float((np.vdot(plus2,H@plus2)+np.vdot(minus2,H@minus2)).real)
    assert abs(after2-before2-prediction)<1e-10
    flip=.1
    records=[]
    for a in (0,1):
        for c in (0,1):
            records.append(pp*(1-flip)**(2-a-c)*flip**(a+c)+pm*flip**(2-a-c)*(1-flip)**(a+c))
    assert abs(sum(records)-1)<1e-12
    return {'oscillator_levels_per_mode':L,'modes':[0,2],
            'field_energy_after_instrument':field_energy,
            'predicted_energy_increment':prediction,'record_probabilities':records,
            'complex_excited_input_energy':before2,'complex_excited_output_energy':after2}


def main():
    E=100.;g=lam=1.;M=20000
    bm=b(M); assert abs(bm-1/(3*D))<1e-8
    n=first_sufficient(E,g,lam,.01)
    rows=[]
    order_rows=[]
    for N in (4,8,16,32,64,128):
        vt=sum(w(k)**2*cos(k*Y)**2/(2*pi*k) for k in range(N+1,M+1))
        # Before reading the pointer, this is the exact pure-state distance
        # between two finite-M vacuum output states; CPTP readout can only shrink it.
        exact=2*sqrt(max(0.,1-exp(-lam*lam*vt)))
        limit=probe_bound(N,0.,lam)
        assert exact<=limit+1e-12
        rows.append({'N':N,'finite_M':M,'unread_vacuum_trace_distance':exact,'analytic_bound':limit})
        kappa=B0+sum(w(k)**2*cos(k*Y)/pi for k in range(1,N+1))
        assert abs(kappa)<=16/(3*pi*D**4*N**3)+1e-14
        var_n=B0/(2*OMEGA0)+sum(w(k)**2*cos(k*Y)**2/(2*pi*k) for k in range(1,N+1))
        before_p=(1+exp(-2*lam**2*var_n)*sin(2*lam*g*kappa))/2
        bit_tv=.8*abs(before_p-.5)
        full_order_upper=min(2.,2*abs(sin(lam*g*kappa)))
        assert 2*bit_tv<=full_order_upper+1e-12
        order_rows.append({'N':N,'kappa':kappa,'two_bit_TV':bit_tv,
                           'full_instrument_trace_distance_upper':full_order_upper})
    # A displaced Gaussian with mean 1 is prepared by shifting q_0; its
    # Fock energy is finite and independent of lambda. The fixed variance is
    # the finite-M vacuum variance in the field's Q readout.
    mu=1.
    variance=B0/(2*OMEGA0)+sum(w(k)**2*cos(k*Y)**2/(2*pi*k) for k in range(1,M+1))
    sign_p=.5*(1+erf(mu/sqrt(2*variance)))
    samples=[]
    for coupling in (1.,2.,5.,10.):
        pointer_p=(1+exp(-2*coupling**2*variance)*sin(2*coupling*mu))/2
        samples.append({'lambda':coupling,'pointer_plus_probability':pointer_p,
            'sharp_sign_plus_probability':sign_p,
            'two_noisy_bits_tv_gap':.8*abs(pointer_p-sign_p),
            'continuum_field_energy_increment':coupling**2/(6*D)})
    assert samples[-1]['two_noisy_bits_tv_gap']>.3
    zero_mode_displacement_energy=OMEGA0**2*mu**2/(2*B0)
    result={'status':'passed','scope':'finite oscillator matrices, Gaussian examples, and tail-bound arithmetic only',
        'continuum_readout_B':1/(3*D),'finite_M_readout_B':bm,'matrix_control':matrix_control(),
        'E':E,'g':g,'lambda':lam,'post_source_energy_upper':post_source_energy(E,g),
        'post_pointer_nonselective_field_energy_upper':E+lam**2/(6*D),
        'sufficient_N_for_both_bounds_below_point_01':n,
        'bounds_at_N':bounds(n,E,g,lam),'bounds_at_N_minus_one':bounds(n-1,E,g,lam),
        'finite_M_vacuum_controls':rows,'fixed_cutoff_order_controls':order_rows,
        'sharp_threshold_counterexample':{'mean':mu,'variance_finite_M':variance,
            'finite_input_energy':zero_mode_displacement_energy,'samples':samples}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
