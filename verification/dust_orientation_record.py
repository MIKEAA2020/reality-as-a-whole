#!/usr/bin/env python3
"""Geometry-sensitive, internally driven record in the existing dust model.

This is an explicitly engineered, nonlocal spectral-control model. Analytic
bounds, domain and physical limitations are in DUST_ORIENTATION_RECORD.md.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import eval_genlaguerre, gammaln

N0=6
N=10
PMAX=.1
WGRAV=.75
BETA=2.
EB=1.
WIDTH=1.


def nu(p):
    if abs(p)>PMAX: raise ValueError('outside selected scalar momentum band')
    return math.sqrt(.25-8*p*p/3)


def grav_energies(p):
    return WGRAV*(2*np.arange(N0,N0+N)+1+nu(p))


def dilation_matrix(p):
    a=nu(p)
    mat=np.zeros((N,N),dtype=complex)
    for j in range(N-1):
        n=N0+j
        c=math.sqrt((n+1)*(n+a+1))
        mat[j+1,j]=-1j*c
        mat[j,j+1]=1j*c
    return mat


def target_state(expanding=True):
    phase=1j if expanding else -1j
    return np.array([math.sqrt(2/(N+1))*math.sin((j+1)*math.pi/(N+1))*phase**j
                     for j in range(N)],dtype=complex)


def projectors(p):
    d=dilation_matrix(p)
    ev,U=np.linalg.eigh(d)
    if min(abs(ev))<1e-10: raise ArithmeticError('code sign gap is absent')
    exp=U[:,ev<0]@U[:,ev<0].conj().T
    con=U[:,ev>0]@U[:,ev>0].conj().T
    return exp,con,ev


def full_dilation_moments(p,expanding=True):
    a=nu(p);w=target_state(expanding)
    d=dilation_matrix(p)
    mean=float(np.vdot(w,d@w).real)
    nlast=N0+N-1
    lower=N0*(N0+a)*abs(w[0])**2
    upper=(nlast+1)*(nlast+1+a)*abs(w[-1])**2
    second=float(np.linalg.norm(d@w)**2+lower+upper)
    return mean,second


def radial_mode(n,alpha,r):
    z=BETA*r*r
    lognorm=.5*(math.log(2)+(alpha+1)*math.log(BETA)+gammaln(n+1)-gammaln(n+alpha+1))
    return math.exp(lognorm)*r**(alpha+.5)*math.exp(-z/2)*eval_genlaguerre(n,alpha,z)


def radial_wave(p,r,expanding=True):
    w=target_state(expanding);a=nu(p)
    return sum(w[j]*radial_mode(N0+j,a,r) for j in range(N))


def analytic_bounds():
    # For 0<=nu<=1/2: n+1 <= a_n <= n+5/4. These produce an
    # analytic lower bound on |<D>| and upper bound on <D^2>.
    w=np.abs(target_state())
    meanlo=2*sum((N0+j+1)*w[j]*w[j+1] for j in range(N-1))
    secondhi=0.
    for j in range(-1,N+1):
        v=0.
        if 0<=j-1<N: v+=(N0+j+.25)*w[j-1]
        if 0<=j+1<N: v+=(N0+j+1.25)*w[j+1]
        secondhi+=v*v
    amin=WGRAV*(2*N0+1+nu(PMAX))
    amax=WGRAV*(2*(N0+N-1)+1+.5)
    hmax=EB+2*math.pi/WIDTH
    return {'mean_absolute_lower':float(meanlo),'second_moment_upper':float(secondhi),
            'cantelli_wrong_sign_upper':float(1-meanlo**2/secondhi),
            'A_min':amin,'A_max':amax,'h_max':hmax,
            'relational_dust_energy_lower':amin-hmax,
            'relational_dust_energy_upper':amax-EB}


def sampled_model(p):
    ep,cp,ev=projectors(p)
    energies=grav_energies(p)
    A=np.diag(energies)
    results=[]
    for expand in (True,False):
        w=target_state(expand)
        probs=[float(np.vdot(w,P@w).real) for P in (ep,cp)]
        mean,second=full_dilation_moments(p,expand)
        before=float(np.vdot(w,A@w).real)
        after=sum(float(np.vdot(P@w,A@(P@w)).real) for P in (ep,cp))
        results.append({'prepared':'expanding' if expand else 'contracting',
                        'p_expanding':probs[0],'p_contracting':probs[1],
                        'mean_full_dilation':mean,'full_dilation_second_moment':second,
                        'free_volume_slope':-.75*mean,
                        'A_mean_before':before,'A_mean_after_nonselective':after,
                        'A_mean_change':after-before})
    return {'p':p,'nu':nu(p),'minimum_code_sign_gap':float(min(abs(ev))), 'cases':results}


def pulse_control(p,panels_tolerance=1e-10):
    exp,con,_=projectors(p)
    energies=grav_energies(p)
    # Two transpositions in a three-level pointer initially |0>.
    i3=np.eye(3,dtype=complex)
    s01=i3.copy();s01[[0,1]]=s01[[1,0]]
    s02=i3.copy();s02[[0,2]]=s02[[2,0]]
    b1=(i3-s01)/2;b2=(i3-s02)/2
    B=np.kron(exp,b1)+np.kron(con,b2)
    A=np.repeat(energies,3)
    ptr=np.array([1,0,0],complex)
    initial=np.kron(target_state(True),ptr)

    def rhs(t,state):
        z=np.exp(1j*A*t)
        drive=z*(B@(z.conjugate()*state))
        pulse=2*math.pi/WIDTH*math.sin(math.pi*t/WIDTH)**2
        return -1j*((-A+EB)*state+pulse*drive)

    sol=solve_ivp(rhs,(0,WIDTH),initial,method='DOP853',
                  rtol=panels_tolerance,atol=panels_tolerance/100)
    if not sol.success: raise RuntimeError(sol.message)
    state=sol.y[:,-1]
    w=target_state(True)
    ideal=np.kron(exp@w,np.array([0,1,0]))+np.kron(con@w,np.array([0,0,1]))
    ideal=np.exp(1j*A*WIDTH-1j*EB*WIDTH)*ideal
    return {'max_state_error':float(np.max(abs(state-ideal))),
            'state_norm_error':float(abs(np.vdot(state,state).real-1)),
            'qutrit_probabilities':[float(np.linalg.norm(state[j::3])**2) for j in range(3)],
            'pointers_are_complete':float(np.linalg.norm(state)**2)}


def run():
    bounds=analytic_bounds()
    assert bounds['cantelli_wrong_sign_upper']<.078
    assert bounds['relational_dust_energy_lower']>2.8
    cases=[sampled_model(p) for p in (-PMAX,0.,PMAX)]
    for row in cases:
        for c in row['cases']:
            assert abs(c['mean_full_dilation'])>=bounds['mean_absolute_lower']
            assert c['full_dilation_second_moment']<=bounds['second_moment_upper']
            correct=c['p_expanding'] if c['prepared']=='expanding' else c['p_contracting']
            assert correct>.99999 and abs(c['p_expanding']+c['p_contracting']-1)<1e-12
    # A genuine normalized continuous p packet, integrated with fixed Simpson weights.
    m=40; weighted=np.zeros(3)
    for j in range(m+1):
        p=-PMAX+2*PMAX*j/m
        c=sampled_model(p)['cases'][0]
        w=1 if j in (0,m) else (4 if j%2 else 2)
        weighted+=w*np.array([c['p_expanding'],c['p_contracting'],c['A_mean_change']])
    weighted/=3*m
    # Matched volume distributions for opposite complex-conjugate preparations.
    p=.06
    maxdiff=0.
    for r in np.linspace(.1,7,100):
        a=radial_wave(p,float(r),True);b=radial_wave(p,float(r),False)
        maxdiff=max(maxdiff,abs(abs(a)**2-abs(b)**2))
    norm,err=quad(lambda r:abs(radial_wave(p,r,True))**2,0,12,epsabs=2e-10,limit=200)
    assert maxdiff<1e-12 and abs(norm-1)<1e-8
    pulse=pulse_control(p)
    assert pulse['max_state_error']<1e-8 and pulse['state_norm_error']<1e-8
    return {'status':'passed',
            'scope':'Engineered dust-model readout of code-projected dilation; not a crossing-triggered device or B7 pass.',
            'model':{'n_range':[N0,N0+N-1],'p_band':[-PMAX,PMAX],
                     'lambda':-.75,'pulse_width':WIDTH,'pointer_reference_energy':EB},
            'analytic_bounds':bounds,'band_endpoint_and_midpoint':cases,
            'uniform_p_packet':{'p_expanding':float(weighted[0]),
                                'p_contracting':float(weighted[1]),
                                'delta_mean_A':float(weighted[2])},
            'volume_density_control':{'p':p,'integral_r_0_to_12':norm,
                    'quadrature_error_estimate':err,'max_pointwise_difference':maxdiff},
            'midband_pulse_ode_control':pulse}


def main():
    r=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__': main()
