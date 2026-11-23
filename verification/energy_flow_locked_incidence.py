#!/usr/bin/env python3
"""Energy-aligned and independently transported incidence markers.

External longitudinally varying transverse Maxwell source, fixed Minkowski
background; no subject law or source dynamics are derived. 4th-order centered
space differences and RK4 time stepping of marker and incidence density.
"""
import argparse
import json
import math
from pathlib import Path
import numpy as np
from verification.two_fluid_incidence_dynamics import derivative


def physical_fields(t,x,A=.1):
    E=1+A*np.sin(t)*np.cos(2*x)
    B=-2*A*np.cos(t)*np.sin(2*x)
    energy=.5*(E**2+B**2)
    flux=E*B
    current=3*A*np.cos(t)*np.cos(2*x)
    h=-current*E
    return energy,flux,h


def marker(t,x,a=.4):
    theta=2*x-t
    return 1+a*np.cos(theta), a*np.sin(theta),-2*a*np.sin(theta)


def evaluate(t,state,x,dx,A,a):
    chi,N=state
    u,S,h=physical_fields(t,x,A)
    v=S/u
    dchi=-v*derivative(chi,dx)
    dN=-derivative(N*v,dx)
    moving,dt_moving,dx_moving=marker(t,x,a)
    Q_aligned=dx*np.sum(chi*h)
    Q_moving=dx*np.sum(moving*h)
    correction=dx*np.sum(u*dt_moving+S*dx_moving)
    incidence=dx*np.sum(N*chi)
    return np.array([dchi,dN]),np.array([Q_aligned,Q_moving,correction,incidence])


def run(n=128,A=.1,a=.4,cfl=.15,end=2*math.pi):
    if n<16 or not 0<A<.49 or not 0<a<1 or cfl<=0 or end<=0:
        raise ValueError('invalid parameters')
    dx=2*np.pi/n; x=(np.arange(n)+.5)*dx
    steps=math.ceil(end/(cfl*dx)); dt=end/steps
    chi0,_dt,_dx=marker(0,x,a)
    state=np.array([chi0,np.ones(n)])
    initial_energy=physical_fields(0,x,A)[0]
    initial_boundary=float(dx*np.sum(chi0*initial_energy))
    integrals=np.zeros(4)
    minN=1.; minChi=float(np.min(chi0)); maxV=0.
    for i in range(steps):
        t=i*dt
        f1,z1=evaluate(t,state,x,dx,A,a)
        f2,z2=evaluate(t+dt/2,state+dt*f1/2,x,dx,A,a)
        f3,z3=evaluate(t+dt/2,state+dt*f2/2,x,dx,A,a)
        f4,z4=evaluate(t+dt,state+dt*f3,x,dx,A,a)
        state+=dt*(f1+2*f2+2*f3+f4)/6
        integrals+=dt*(z1+2*z2+2*z3+z4)/6
        minN=min(minN,float(np.min(state[1])))
        minChi=min(minChi,float(np.min(state[0])))
        u,S,h=physical_fields(t+dt,x,A)
        maxV=max(maxV,float(np.max(np.abs(S/u))))
    final_u,_,_=physical_fields(end,x,A)
    chi,N=state
    aligned_final=float(dx*np.sum(chi*final_u))
    moving_final_marker=marker(end,x,a)[0]
    moving_final=float(dx*np.sum(moving_final_marker*final_u))
    return {'n':n,'end':end,'steps':steps,'initial_weighted_energy':initial_boundary,
            'aligned_final_weighted_energy':aligned_final,
            'aligned_balance_residual':float(integrals[0]-(aligned_final-initial_boundary)),
            'aligned_weighted_exchange':float(integrals[0]),
            'aligned_incidence_integral':float(integrals[3]),
            'aligned_marker_return_rms':float(np.sqrt(np.mean((chi-chi0)**2))),
            'aligned_number_return_rms':float(np.sqrt(np.mean((N-1)**2))),
            'aligned_final_number':float(dx*np.sum(N)),
            'min_N_sampled':minN,'min_chi_sampled':minChi,'max_energy_speed_sampled':maxV,
            'moving_weighted_exchange':float(integrals[1]),
            'moving_final_weighted_energy':moving_final,
            'moving_marker_correction':float(integrals[2]),
            'moving_balance_residual':float(integrals[1]-(moving_final-initial_boundary)+integrals[2]),
            'moving_full_cycle_analytic_exchange':float(-3*A*a*math.pi**2)}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--grids',type=int,nargs='+',default=[64,128,256])
    p.add_argument('--receipt',default='verification/energy_flow_locked_incidence_receipt.json')
    args=p.parse_args()
    data={'scope':'fixed-background Maxwell fields and external current with stipulated incidence, not actual subject dynamics, gravity, or zero total physical energy',
          'parameters':{'A':.1,'a':.4,'cfl':.15},
          'full_cycle':[run(n) for n in args.grids],
          'partial_interval':[run(n,end=1.1) for n in args.grids]}
    Path(args.receipt).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__': main()
