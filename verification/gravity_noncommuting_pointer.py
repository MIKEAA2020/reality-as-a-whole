#!/usr/bin/env python3
"""Two-channel spin-pointer scattering in the backreacting Morse model.

Numerical solution of a declared self-adjoint homogeneous model. Exact Morse
solutions match both tails; solver comparisons are not rigorous error bounds.
Install requirements-gravity-spin-pointer.txt into an isolated environment.
"""
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

if __package__:
    from .gravitating_clock_probe import hyper, scatter
else:
    from gravitating_clock_probe import hyper, scatter

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Z=np.diag([1.,-1.]).astype(complex)
OMEGA=.6
EPS=.6
AMP=.8


def profile(x,amplitude):
    if x<=-1: return 0.
    if x>=1: return amplitude
    t=(x+1)/2
    return amplitude*(10*t**3-15*t**4+6*t**5)


def rotation(x,amplitude):
    a=profile(x,amplitude)
    return math.cos(a)*I+1j*math.sin(a)*X


def potential(x,amplitude,energy,epsilon):
    h=epsilon*(I+Z)/2
    u=rotation(x,amplitude)
    return math.exp(2*x)*I-(4/3)*math.exp(x)*(energy*I+u.conj().T@h@u)


def jost(k,kap,x):
    """Incoming small-volume Morse solution and its x derivative."""
    z=2*math.exp(x)
    f,fp,_=hyper(.5+1j*k-kap,1+2j*k,z)
    pref=np.exp(1j*k*x-z/2)
    return pref*f,pref*((1j*k-z/2)*f+z*fp)


def reflection(k,amplitude=AMP,energy=.3,epsilon=EPS,right=1.6,
               rtol=1e-10,method='DOP853',segment=.2):
    if k<=0 or energy<0 or epsilon<0 or right<=1 or rtol<=0 or segment<=0:
        raise ValueError('invalid parameters or right boundary outside constant-G tail')
    left=-1.
    # x>=1 has constant U, so both decaying channels have exact Morse tails.
    # Working precision is local, to avoid changing caller's mpmath context.
    kappas=(2/3*(energy+epsilon),2/3*energy)
    with mp.workdps(35):
        slopes=[]
        for kap in kappas:
            def mode(x):
                z=2*mp.exp(x)
                return mp.whitw(kap,1j*k,z)/mp.sqrt(z)
            value=mode(right)
            if abs(value)<mp.mpf('1e-30'): raise ArithmeticError('right tail mode node')
            ratio=mp.diff(mode,right)/value
            if abs(mp.im(ratio))>mp.mpf('1e-25'): raise ArithmeticError('nonreal tail derivative')
            slopes.append(float(mp.re(ratio)))
    u=rotation(right,amplitude)
    d=u.conj().T@np.diag(slopes)@u
    basis=np.linalg.qr(np.vstack([I,d]))[0]

    def ode(x,y):
        f=y.reshape(4,2)
        return np.vstack([f[2:],(potential(x,amplitude,energy,epsilon)-k*k*I)@f[:2]]).ravel()

    # QR on the complete value-and-derivative columns preserves the decaying
    # solution subspace, including where a value matrix is singular.
    x=right
    while x>left+1e-12:
        x2=max(left,x-segment)
        solution=solve_ivp(ode,(x,x2),basis.ravel(),method=method,rtol=rtol,atol=rtol/100)
        if not solution.success: raise RuntimeError(solution.message)
        basis=np.linalg.qr(solution.y[:,-1].reshape(4,2))[0]
        x=x2

    # x<=-1 is exactly the uncoupled Morse tail. The conjugate incoming
    # solution is outgoing; their Wronskian is nonzero for k>0.
    modes=[jost(k,kap,left) for kap in kappas]
    matching=np.block([[np.diag([v[0] for v in modes]),np.diag([v[0].conjugate() for v in modes])],
                       [np.diag([v[1] for v in modes]),np.diag([v[1].conjugate() for v in modes])]])
    coefficients=np.linalg.solve(matching,basis)
    incoming,outgoing=coefficients[:2],coefficients[2:]
    return np.linalg.solve(incoming.T,outgoing.T).T


def flip(k,**kwargs):
    return float(abs(reflection(k,**kwargs)[0,1])**2)


def packet(energy=.3,panels=8,**kwargs):
    # Uniform, normalized scalar spectral packet on [2,2.01]. Both outcomes
    # are calculated independently, not forced to sum to one.
    if panels<=0 or panels%2: raise ValueError('positive even panel count required')
    totals=np.zeros(2)
    for j in range(panels+1):
        s=reflection(2+.01*j/panels,energy=energy,**kwargs)
        w=1 if j in (0,panels) else (4 if j%2 else 2)
        totals+=w*np.abs(s[:,1])**2
    totals/=3*panels
    return {'up':float(totals[0]),'down':float(totals[1])}


def run():
    k=2.005
    s=reflection(k)
    sr=reflection(k,amplitude=0)
    sexact=np.diag([scatter(k,2/3*(.3+EPS)),scatter(k,2/3*.3)])
    szero=reflection(k,epsilon=0)
    sexact_zero=scatter(k,.2)*I
    sminus=reflection(k,amplitude=-AMP)
    unitary_error=float(np.max(np.abs(s.conj().T@s-I)))
    reference_error=float(np.max(np.abs(sr-sexact)))
    degenerate_error=float(np.max(np.abs(szero-sexact_zero)))
    sign_error=float(np.max(np.abs(sminus-Z@s@Z)))
    assert max(unitary_error,reference_error,degenerate_error,sign_error)<1e-8
    base=packet(panels=8)
    fine=packet(panels=16)
    excited=packet(energy=.9,panels=8)
    assert .25<base['up']<.30
    assert abs(base['up']-fine['up'])<1e-8
    assert .32<excited['up']<.37
    assert max(abs(p['up']+p['down']-1) for p in (base,fine,excited))<1e-9
    control=flip(k,amplitude=0)
    degenerate=flip(k,epsilon=0)
    assert control<1e-20 and degenerate<1e-20
    stability=[]
    for method,rtol,right in [('DOP853',1e-9,1.1),('DOP853',1e-11,2.),('RK45',1e-10,1.6)]:
        s2=reflection(k,method=method,rtol=rtol,right=right)
        stability.append({'method':method,'rtol':rtol,'right_match':right,
                          'flip':float(abs(s2[0,1])**2),
                          'max_amplitude_difference':float(np.max(np.abs(s2-s)))})
    assert max(x['max_amplitude_difference'] for x in stability)<1e-8
    return {'status':'passed',
            'scope':'Exploratory numerical homogeneous spin-pointer scattering; not an orientation test, observation, or B7 pass.',
            'parameters':{'k_band':[2,2.01],'initial_pointer':'Z=-1','amplitude':AMP,
                          'pointer_energy_gap':EPS,'oscillator_energy':.3,
                          'right_whittaker_match':1.6,'left_jost_match':-1},
            'complete_ground_channel_packet_outcomes':fine,
            'complete_excited_channel_packet_outcomes':excited,
            'matched_reference_pointer_flip':control,'zero_gap_pointer_flip':degenerate,
            'midband_flip':float(abs(s[0,1])**2),'midband_unitarity_max_error':unitary_error,
            'midband_reference_vs_exact_morse_max_error':reference_error,
            'midband_zero_gap_vs_exact_morse_max_error':degenerate_error,
            'midband_sign_reversal_matrix_error':sign_error,
            'midband_solver_and_right_match_checks':stability,
            'simpson_8_vs_16_panel_difference':abs(base['up']-fine['up'])}


def main():
    r=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__': main()
