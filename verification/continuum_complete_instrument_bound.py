#!/usr/bin/env python3
"""Arithmetic and Gaussian controls for the analytic common-Fock-space bound.

Does not prove Fock-domain, Sobolev, channel or Gaussian claims; see report.
"""
from math import acos, cos, exp, pi, sin, sqrt
from pathlib import Path
import json

D=.4
Y=pi/2
OMEGA0=.5
B0=1/(2*pi)
# Integral-test majorant for sum_{n>=1} n^{-3} <= 3/2.
CH_UPPER=OMEGA0*B0+24/(pi*D**4)


def w(n):
    u=n*D/2
    return (sin(u)/u)**2


def tails(n):
    if not isinstance(n,int) or n<1:raise ValueError('cutoff must be positive integer')
    return {'A_q':16/(5*pi*D**4*n**5), 'T_q':4/(pi*D**4*n**4),
            'F_p':16/(3*pi*D**4*n**3), 'G_p':8/(pi*D**4*n**2)}


def measurement_bound(n,E):
    if E<0:raise ValueError('energy must be nonnegative')
    z=tails(n)
    M=sqrt(2*E/B0)+sqrt(CH_UPPER/(2*B0**2))
    Dtail=4*E*z['A_q']+z['T_q']
    probability=min(1.,3*(4*M*M*Dtail)**(1/3))
    return min(2.,2*sqrt(2*probability))


def source_bound(n,E,g=1.):
    if E<0:raise ValueError('energy must be nonnegative')
    z=tails(n)
    return min(2.,2*abs(g)*(sqrt(2*E*z['F_p'])+sqrt(z['G_p']/2)))


def post_source_energy(E,g=1.):
    if E<0:raise ValueError('energy must be nonnegative')
    coherent_energy=g*g*(1/D**3+1/(16*pi))
    return (sqrt(E)+sqrt(coherent_energy))**2


def complete_bounds(n,E,g=1.):
    s=source_bound(n,E,g)
    return {'source_then_measurement':min(2.,s+measurement_bound(n,post_source_energy(E,g))),
            'measurement_then_source':min(2.,s+measurement_bound(n,E))}


def first_sufficient(E,g,target):
    if not 0<target<2:raise ValueError('target outside (0,2)')
    def bound(n):return max(complete_bounds(n,E,g).values())
    lo,hi=1,1
    while bound(hi)>target:hi*=2
    while lo<hi:
        mid=(lo+hi)//2
        if bound(mid)<=target:hi=mid
        else:lo=mid+1
    assert bound(lo)<=target and (lo==1 or bound(lo-1)>target)
    return lo


def main():
    E=100.;g=1.;M=20000
    for n in (1,4,8,16,32,128,512):
        z=tails(n);aa=tt=ff=gg=0.
        for k in range(n+1,M+1):
            f2=w(k)**2/pi;h2=f2*cos(k*Y)**2
            aa+=h2/k**2;tt+=h2/k;ff+=f2;gg+=k*f2
        assert aa<=z['A_q']+1e-14 and tt<=z['T_q']+1e-14
        assert ff<=z['F_p']+1e-14 and gg<=z['G_p']+1e-14
    ch=OMEGA0*B0+sum(k*w(k)**2*cos(k*Y)**2/pi for k in range(1,M+1))
    assert ch<=CH_UPPER
    # Vacuum source energy; the zero-mode q potential is added as an energy
    # constraint regulator and is absent from the original kinetic-only bound.
    es=OMEGA0**2*B0/2+sum(k*k*w(k)**2/(2*pi) for k in range(1,M+1))
    es_inf=1/D**3+1/(16*pi)
    assert es <= es_inf+1e-11 and es_inf-es <= 8/(pi*D**4*M)+1e-11
    # Centered vacuum: exact finite-M sign-disagreement of two commuting
    # Gaussian readouts; record-only noise omitted to challenge the bound.
    rows=[]
    for n in (4,8,16,32,64,128):
        v0=B0/(2*OMEGA0)
        vn=v0+sum(w(k)**2*cos(k*Y)**2/(2*pi*k) for k in range(1,n+1))
        vm=v0+sum(w(k)**2*cos(k*Y)**2/(2*pi*k) for k in range(1,M+1))
        mismatch=acos(min(1.,sqrt(vn/vm)))/pi
        vacuum_cq_trace=2*sqrt(2*mismatch-mismatch*mismatch)
        bound=measurement_bound(n,0.)
        assert vacuum_cq_trace<=bound+1e-12
        gtail=sum(k*w(k)**2/pi for k in range(n+1,M+1))
        vacuum_source_trace=2*sqrt(1-exp(-g*g*gtail/2))
        source_limit=source_bound(n,0.,g)
        assert vacuum_source_trace<=source_limit+1e-12
        rows.append({'N':n,'finite_M':M,'sign_mismatch':mismatch,
                     'vacuum_cq_trace_distance':vacuum_cq_trace,'bound':bound,
                     'vacuum_source_trace_distance':vacuum_source_trace,
                     'source_bound':source_limit})
    n=first_sufficient(E,g,.01)
    bounds=complete_bounds(n,E,g)
    assert source_bound(4,E,0)==0
    assert complete_bounds(4,E,0)['source_then_measurement']==measurement_bound(4,E)
    result={'status':'passed','scope':'arithmetic and finite-M vacuum controls only; analytic proof is in report',
        'dimension':'1D even-cosine Fock sector','zero_mode_frequency':OMEGA0,
        'energy_constraint':E,'source_g':g,'source_displacement_energy_bound':es_inf,
        'post_source_input_energy_upper':post_source_energy(E,g),'conservative_Ch_upper':CH_UPPER,
        'conservative_N_for_both_unhalved_norm_bounds_below_0_01':n,
        'bounds_at_N':bounds,'bounds_at_N_minus_1':complete_bounds(n-1,E,g),
        'finite_M_vacuum_controls':rows}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
