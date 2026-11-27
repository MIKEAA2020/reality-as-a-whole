"""A closed relativistic plasma + neutral scalar, with stipulated even response.

Uses fixed effective Minkowski time and no gravity. Numerical output checks a
mathematical toy, not physical incidence or experience. The neutral scalar's
mass is deliberately tuned to twice the selected plasma orbit frequency.
"""
from math import cos, sin, sqrt, pi
import numpy as np
from scipy.integrate import solve_ivp, quad


def solve(amplitude=.8, n=1., m=1., magnetic=1., scalar_amplitude=1.,
          contrast=.6, phase=pi/4, rtol=1e-11):
    if not (amplitude>0 and n>0 and m>0 and magnetic>0 and scalar_amplitude>0
            and 0<contrast<1 and 0<rtol<1e-4):
        raise ValueError('positive parameters, 0<contrast<1 and 0<rtol<1e-4 required')
    a=amplitude; d=scalar_amplitude
    pmax=a*sqrt(m/(2*n)+a*a/(16*n*n))
    frequency=sqrt(2*n/m)
    def plasma(t,y):
        E,p=y
        return [-2*n*p/sqrt(m*m+p*p),E]
    def half_period(t,y): return y[1]
    half_period.direction=-1
    half_period.terminal=True
    first=solve_ivp(plasma,(0,100/frequency),[a,0],events=half_period,
                    rtol=rtol,atol=rtol*1e-2)
    if not first.success or len(first.t_events[0])!=1:
        raise RuntimeError('failed to determine plasma period')
    period=2*first.t_events[0][0]
    scalar_mass=4*pi/period  # scalar makes two cycles per plasma cycle
    omega=scalar_mass
    def deriv(t,y):
        E,p,phi,Pi,W=y
        j=2*n*p/sqrt(m*m+p*p)
        alpha=contrast*E*p/(a*pmax)*(2*omega*phi*Pi/d**2)
        return [-j,E,Pi,-omega**2*phi,alpha*(-j*E)]
    start=np.array([a,0,d*sin(phase)/omega,d*cos(phase),0.])
    full=solve_ivp(deriv,(0,period),start,rtol=rtol,atol=rtol*1e-2,dense_output=True)
    if not full.success: raise RuntimeError('failed to integrate coupled state')
    # Separate post-hoc quadrature, using the dense trajectory and the exact
    # harmonic scalar instead of the integrated W variable.
    def separate(t):
        E,p=full.sol(t)[:2]
        phi=d*sin(omega*t+phase)/omega; Pi=d*cos(omega*t+phase)
        alpha=contrast*E*p/(a*pmax)*(2*omega*phi*Pi/d**2)
        return -alpha*2*n*p*E/sqrt(m*m+p*p)
    W_quad,error=quad(separate,0,period,epsabs=1e-11,epsrel=1e-11,limit=150)
    return {'period':period,'scalar_mass':omega,'pmax':pmax,'start':start,
            'end':full.y[:,-1], 'trajectory':full.sol,
            'quadrature':W_quad,'quadrature_error':error,
            'parameters':{'amplitude':a,'n':n,'m':m,'magnetic':magnetic,
                          'scalar_amplitude':d,'contrast':contrast,'phase':phase}}
