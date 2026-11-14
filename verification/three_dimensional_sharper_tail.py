#!/usr/bin/env python3
"""Conditional improved 3D primitive tail and energy-projection numerics.

Relies on the earlier continuum/channel estimates. Finite tests and floating
quadratures do not independently verify the continuum or certify constants.
"""
from math import exp, floor, isfinite, log10, pi, sqrt
from pathlib import Path
import json
import numpy as np
import three_dimensional_bogoliubov_continuum as prev
import three_dimensional_quantitative_channel as earlier
import three_dimensional_smooth_probe_gate as geom
import two_field_instrument_continuum as one


def derivative_norms(quad):
    z,w=np.polynomial.legendre.leggauss(quad)
    raw=np.exp(-1/(1-z*z))
    normal=geom.D*np.dot(w,raw)
    f=raw/normal
    df=raw*(-2*z/(1-z*z)**2)/(geom.D*normal)
    f2=float(geom.D*np.dot(w,f*f))
    df2=float(geom.D*np.dot(w,df*df))
    return {'one_dimensional_L2_squared':f2,'one_dimensional_derivative_L2_squared':df2,
            'D_gradient_squared_over_V':3*df2*f2*f2/geom.V}


def primitive_tail(n, derivative):
    if n<2: raise ValueError('N >= 2 required')
    c,_=prev.primitive_constants()
    q=n//2
    tail=24/q+2/(3*q**3)
    return sqrt((c['W_F']*tail+derivative*sqrt(c['Z_A4_upper']*c['Z_B4_upper'])/(q+1)**2)/8)


def stronger_constants(lam, derivative):
    old=earlier.constants(lam); p,_=prev.primitive_constants()
    wa=p['W_F'];zz=sqrt(p['Z_A4_upper']*p['Z_B4_upper'])
    d_new=sqrt((76.5*wa+2*derivative*zz)/8)
    nu=old['nu']; h=old['primitive_HS_upper']; lam=abs(lam)
    q=old['Q']; d=old['D0'];e=old['e0']; chi2=old['chi_L2_squared']; B=old['beta_uniform_upper']
    I=lam*(d_new*nu*q+h*e*q+h*lam*d*nu*chi2)
    db=nu*(I+lam*d*B)
    relative_b=nu*db+B*e
    return {'primitive_constant':d_new, 'relative_alpha_coefficient':old['relative_alpha_coefficient'],
            'relative_beta_coefficient':relative_b, 'old_relative_beta_coefficient':old['relative_beta_coefficient']}


def optimized(a,b,E,mass):
    # Bound (4) after replacing floor(R/m) <= R/m. Input a,b are
    # nonnegative upper bounds for the relative alpha/beta quantities.
    if E<0 or mass<=0 or a<0 or b<0:raise ValueError('invalid input')
    A=(a+b+b*b/2)/mass
    if E==0:return min(2.,4*b),None
    if A==0:return 0.,None
    R=(sqrt(E)/A)**(2/3)
    return min(2.,6*(A*E)**(1/3)+4*b),R


def main():
    norms=derivative_norms(512); norms256=derivative_norms(256)
    assert abs(norms['D_gradient_squared_over_V']-norms256['D_gradient_squared_over_V'])<1e-10
    derivative=norms['D_gradient_squared_over_V']
    p,old_delta=prev.primitive_constants()
    full,tails=prev.primitive_sum(6,(2,3,4,5))
    # Product bump is normalized: F_0 = integral(F)/V = 1/V. The diagonal
    # k+l=0 provides a lower bound on the *primitive* tail, not on the channel.
    ca=sqrt(3+geom.MA**2); cb=sqrt(3+geom.MB**2)
    diagonal_coeff=sqrt(12/(geom.V**2*ca*cb*(ca+cb)**2))
    C=stronger_constants(1.,derivative)
    rows=[]
    for n in (2,3,4,5):
        new=primitive_tail(n,derivative)
        finite_lower=diagonal_coeff*sqrt(1/(n+1)-1/7)
        assert finite_lower<=sqrt(2)*tails[n]+1e-12
        assert sqrt(2)*tails[n]<=new+1e-12
        assert new<=C['primitive_constant']/sqrt(n)+1e-12
        rows.append({'N':n,'M':6,'finite_tail_doubled_HS':sqrt(2)*tails[n],
                     'finite_diagonal_lower':finite_lower,
                     'new_tail_upper':new,'old_tail_upper':sqrt(2)*old_delta(n)})
    a0=C['relative_alpha_coefficient'];b0=C['relative_beta_coefficient']
    b_old=C['old_relative_beta_coefficient'];mass=min(geom.MA,geom.MB);E=100.
    # Work in base-10 exponents; never allocate an astronomical integer/Fock space.
    comparisons=[]
    for exponent in (70,78,79,80,81):
        alpha=a0*10**(-exponent/2)
        beta=b0*10**(-exponent/2)
        new,R=optimized(alpha,beta,E,mass)
        old_opt,_=optimized(alpha,b_old*10**(-exponent/4),E,mass)
        comparisons.append({'log10_N':exponent,'new_optimized_upper':new,
                            'old_rate_optimized_upper':old_opt,'energy_projection_R':R})
    assert comparisons[-2]['new_optimized_upper']<.01
    assert comparisons[-3]['new_optimized_upper']>.01
    old_at_160,_=optimized(a0*10**(-80),b_old*10**(-40),E,mass)
    assert old_at_160<.01
    # Non-vacuous finite shared-M check at weak coupling, as in the previous
    # numerical control. Compare the complete relative Bogoliubov pair block.
    weak=stronger_constants(.001,derivative)
    an,bn,_=prev.bogoliubov(2,1,.001)
    am,bm,_=prev.bogoliubov(2,2,.001)
    rel_b=am.conj().T@bn-bm.T@an.conj()
    actual=float(np.linalg.norm(rel_b))
    # N=1 is outside the new theorem, so use prior nonperturbative bound here.
    prior=earlier.detailed(1,.001)['relative_beta_HS']
    assert actual<=prior+1e-12
    assert optimized(0.,0.,E,mass)[0]==0.
    assert optimized(0.,.2,0.,mass)[0]==.8
    out={'scope':'Floating quadrature and finite-M controls conditional on the earlier unreviewed continuum/channel argument; not an interval certificate.',
         'derivative_norms_512':norms,'derivative_norms_256':norms256,
         'finite_primitive_tail_controls':rows,'full_strength_constants':C,
         'primitive_diagonal_lower_coefficient':diagonal_coeff,
         'primitive_diagonal_lower_scope':'For normalized product bump, doubled infinite primitive tail >= coefficient/sqrt(N+1); no channel lower bound.',
         'N_power_of_ten_controls':comparisons,
         'old_rate_but_R_optimized_at_1e160':old_at_160,
         'prior_original_simple_coefficient_sufficient_exponent':729,
         'new_round_sufficient_exponent_for_E100_error_0p01':80,
         'interpretation':'N=10^80 is an approximate sufficient upper-bound example only; not necessary, minimal, feasible, or total instrument error.',
         'weak_finite_ODE':{'M':2,'N':1,'lambda':.001,'relative_beta_HS':actual,
                            'prior_bound_N1':prior,'new_N2_plus_theorem_not_applied':True}}
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text);print(text)


if __name__=='__main__':main()
