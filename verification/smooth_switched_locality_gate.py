#!/usr/bin/env python3
"""Finite-mode controls for smooth spacetime switching, not a causality proof.

Pinned NumPy dependency: requirements-framework-battery.txt. All spectral sums
are numerical approximations and the endpoint energy is only the free field.
"""
import json
from math import cos, expm1, pi, sin, sqrt
from pathlib import Path
import numpy as np

D=.4
A=.08
Y=pi/2
T=.3
MASS=.5
G=LAMBDA=1.


def bump_nodes(width,count):
    x,w=np.polynomial.legendre.leggauss(count)
    density=np.exp(-1/(1-x*x))
    weights=w*density
    weights=weights/weights.sum()
    return width*x,weights


def spectra(nmax,quadrature):
    x,xw=bump_nodes(D,quadrature)
    t,tw=bump_nodes(A,quadrature)
    n=np.arange(nmax+1,dtype=float)
    spatial=np.cos(np.outer(n,x))@xw
    f=spatial/np.sqrt(pi); f[0]=1/np.sqrt(2*pi)
    h=f*np.cos(n*Y)
    omega=np.sqrt(n*n+MASS*MASS)
    hat=np.cos(np.outer(omega,t))@tw
    oldomega=n.copy();oldomega[0]=MASS
    oldhat=np.cos(np.outer(oldomega,t))@tw
    return n,f,h,omega,hat,oldomega,oldhat


def vals(nmax,quadrature):
    n,f,h,omega,hat,oldomega,oldhat=spectra(nmax,quadrature)
    prod=f*h
    term_mass=prod*hat*hat*np.cos(omega*T)
    term_old=prod*oldhat*oldhat*np.cos(oldomega*T)
    # Continuum field-energy change from pointer interaction in a product
    # |0_z> pointer state; source value is energy of its coherent vacuum shift.
    read_energy=.5*np.sum(h*h*hat*hat)
    source_energy=.5*np.sum(omega*omega*f*f*hat*hat)
    return {'n':n,'f':f,'h':h,'omega':omega,'hat':hat,
            'mass_terms':term_mass,'old_terms':term_old,
            'field_probe_energy':float(read_energy),'source_vacuum_energy':float(source_energy),
            'qubit_variance':float(np.sum(h*h*hat*hat/(2*omega))),
            'old_qubit_variance':float(np.sum(h*h*oldhat*oldhat/(2*oldomega)))}


def matrix_energy_control(data):
    # Finite-Fock matrix check of the rotated quadrature, independently of
    # the spectral energy sum. Use vacuum and a state with nonzero momentum.
    levels=24
    a=np.diag(np.sqrt(np.arange(1,levels)),1)
    I=np.eye(levels)
    number=np.diag(np.arange(levels))
    H=np.zeros((levels**2,levels**2),dtype=complex)
    B=np.zeros_like(H)
    for k,mode in enumerate((0,2)):
        omega=float(data['omega'][mode]); h=float(data['h'][mode]); r=float(data['hat'][mode])
        q=(a+a.T)/np.sqrt(2*omega)
        p=1j*np.sqrt(omega/2)*(a.T-a)
        local=h*r*(q*np.cos(omega*T)+(p/omega)*np.sin(omega*T))
        B+=np.kron(local,I) if k==0 else np.kron(I,local)
        H+=omega*(np.kron(number,I) if k==0 else np.kron(I,number))
    eig,V=np.linalg.eigh(B)
    expected=.5*LAMBDA**2*sum(float(data['h'][n]*data['hat'][n])**2 for n in (0,2))
    increments=[]
    for excited in (False,True):
        state=np.zeros(levels**2,dtype=complex)
        state[0]=1 if not excited else 1/np.sqrt(2)
        if excited:state[1]=1j/np.sqrt(2)
        coeff=V.conj().T@state
        plus=V@((np.cos(LAMBDA*eig)+np.sin(LAMBDA*eig))*coeff)/np.sqrt(2)
        minus=V@((np.cos(LAMBDA*eig)-np.sin(LAMBDA*eig))*coeff)/np.sqrt(2)
        before=float(np.vdot(state,H@state).real)
        after=float((np.vdot(plus,H@plus)+np.vdot(minus,H@minus)).real)
        increments.append(after-before)
        assert abs(after-before-expected)<1e-10
    return {'levels_per_mode':levels,'modes':[0,2],
            'expected_increment':expected,'vacuum_and_excited_increments':increments}


def main():
    data=vals(256,256); doubled=vals(256,384)
    mass=data['mass_terms'];old=data['old_terms']; h=data['h'];om=data['omega'];hat=data['hat']
    # This is a numerical resolution control, not a certified quadrature error.
    assert np.max(np.abs(mass-doubled['mass_terms']))<2e-14
    assert abs(mass.sum())<1e-11
    x,tw=bump_nodes(A,256)
    zero_hat=float(np.dot(tw,np.cos(MASS*x)))
    analytic_old=(cos(MASS*T)*zero_hat**2-1)/(2*pi)
    assert abs(old.sum()-analytic_old)<1e-11
    assert abs(analytic_old)>1e-4
    sep=Y-2*D
    max_time_separation=T+2*A
    assert sep>max_time_separation
    # Complete pointer record distinguishability in the vacuum. Source
    # shifts integrated detector field by g*kappa; a source applied afterwards
    # does not change the record probabilities. Flip rate is 0.1.
    def record_tv(kappa,variance):
        return .8*abs(np.exp(-2*LAMBDA**2*variance)*sin(2*LAMBDA*G*kappa)/2)
    bound_rows=[]
    f=data['f']
    for N in (0,2,4,8,16,32,64,128,256):
        km=float(mass[:N+1].sum());ko=float(old[:N+1].sum())
        vn=float(np.sum((h*h*hat*hat/(2*om))[:N+1]))
        tv=record_tv(km,vn)
        bound=2*abs(sin(G*LAMBDA*km))
        assert 2*tv<=bound+1e-13
        # Exact vacuum overlaps against finite M=256, versus the E=0 tail
        # bounds; the unmeasured pointer controls the postprocessed instrument.
        gp=float(np.sum((om*f*f*hat*hat)[N+1:]))
        tp=float(np.sum((h*h*hat*hat/om)[N+1:]))
        source_vacuum=2*sqrt(-expm1(-G*G*gp/2))
        pointer_vacuum=2*sqrt(-expm1(-LAMBDA*LAMBDA*tp/2))
        source_upper=min(2.,2*abs(G)*sqrt(gp/2))
        pointer_upper=min(2.,2*abs(LAMBDA)*sqrt(tp))
        assert source_vacuum<=source_upper+1e-14
        assert pointer_vacuum<=pointer_upper+1e-14
        bound_rows.append({'N':N,'local_mass_kappa':km,'old_zero_mode_kappa':ko,
                           'mass_record_tv':tv,'full_instrument_trace_bound':bound,
                           'finite_M_vacuum_source_distance':source_vacuum,
                           'source_vacuum_tail_bound':source_upper,
                           'finite_M_vacuum_unread_pointer_distance':pointer_vacuum,
                           'pointer_vacuum_tail_bound':pointer_upper})
    # Positive normalized smooth time switching obeys |Fourier transform|<=1.
    assert np.max(np.abs(hat))<=1+1e-14
    assert data['field_probe_energy']<=.5*np.sum(h*h)+1e-14
    result={'status':'passed','scope':'quadrature and finite-mode controls only; locality follows from PDE support, not numerics',
        'spatial_halfwidth':D,'switch_halfwidth':A,'readout_center':Y,'switch_center_difference':T,'mass':MASS,
        'minimal_spatial_separation':sep,'maximal_temporal_separation':max_time_separation,
        'local_mass_integrated_kappa_N256':float(mass.sum()),
        'old_regulator_integrated_kappa_N256':float(old.sum()),
        'old_regulator_exact_kappa':analytic_old,
        'old_regulator_example_two_bit_tv':record_tv(analytic_old,data['old_qubit_variance']),
        'old_vacuum_smeared_readout_variance':data['old_qubit_variance'],
        'field_probe_energy_increment':data['field_probe_energy'],
        'matrix_energy_control':matrix_energy_control(data),
        'source_vacuum_field_energy_increment':data['source_vacuum_energy'],
        'vacuum_smeared_readout_variance':data['qubit_variance'],
        'switch_hat_zero_frequency_mode':zero_hat,'quadrature_mode_sum_controls':bound_rows}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
