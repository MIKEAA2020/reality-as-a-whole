#!/usr/bin/env python3
"""Periodic two-fluid Maxwell-Poisson testbed for incidence/valence accounting.

Nonrelativistic 1D cold fluids on a fixed background, not a cosmology or a
model of real experience. Periodic 4th-order central differences and RK4.
"""
import argparse
import json
import math
from pathlib import Path
import numpy as np


def derivative(f, dx):
    return (np.roll(f, 2)-8*np.roll(f, 1)+8*np.roll(f, -1)-np.roll(f, -2))/(12*dx)


def initial(n, amplitude=.1, modulation=.5, q=1., k=2):
    if n < 16 or amplitude <= 0 or not 0 <= modulation < 1 or q <= 0 or k <= 0 or not isinstance(k,int):
        raise ValueError('invalid setup')
    x=2*np.pi*(np.arange(n)+0.5)/n
    base=1+modulation*np.cos(k*x)
    delta=0.5*amplitude*np.cos(k*x)
    if np.min(base-abs(delta)) <= 0:
        raise ValueError('initial densities must be positive')
    # Gauss law is imposed exactly for the discrete derivative, not by
    # mistaking a continuum analytic field for an exact discrete solution.
    dx=2*np.pi/n
    kd=(8*np.sin(k*dx)-np.sin(2*k*dx))/(6*dx)
    if abs(kd)<1e-12: raise ValueError('unresolved wave number')
    return np.array([base+delta,base-delta,np.zeros(n),np.zeros(n),q*amplitude/kd*np.sin(k*x)])


def rhs(y,dx,q=1.,mass=1.):
    p,m,up,um,e=y
    return np.array([-derivative(p*up,dx), -derivative(m*um,dx),
                     -up*derivative(up,dx)+q*e/mass,
                     -um*derivative(um,dx)-q*e/mass,
                     -q*(p*up-m*um)])


def evolve(n=128, end=1., cfl=.15, amplitude=.1, modulation=.5, q=1., mass=1., k=2):
    if end < 0 or cfl <= 0 or mass <= 0: raise ValueError('invalid evolution')
    y=initial(n,amplitude,modulation,q,k); dx=2*np.pi/n
    nsteps=max(1,math.ceil(end/(cfl*dx)))
    dt=end/nsteps
    start=y.copy()
    for _ in range(nsteps):
        a=rhs(y,dx,q,mass); b=rhs(y+dt*a/2,dx,q,mass)
        c=rhs(y+dt*b/2,dx,q,mass); d=rhs(y+dt*c,dx,q,mass)
        y=y+dt*(a+2*b+2*c+d)/6
    return {'initial':start,'final':y,'dx':dx,'dt':dt,'steps':nsteps,'q':q,'mass':mass}


def interpolated_negative_fraction(K,J,dx):
    """Integrate linearly interpolated K across intervals where linearly interpolated J<0."""
    negative=0.
    for k0,k1,j0,j1 in zip(K,np.roll(K,-1),J,np.roll(J,-1)):
        if j0 < 0 and j1 < 0:
            negative+=dx*(k0+k1)/2
        elif (j0 < 0) != (j1 < 0):
            t=-j0/(j1-j0)
            kr=k0+t*(k1-k0)
            if j0 < 0:
                negative+=dx*t*(k0+kr)/2
            else:
                negative+=dx*(1-t)*(kr+k1)/2
    return float(negative/(dx*np.sum(K)))


def diagnostics(y,dx,q=1.,mass=1.):
    p,m,up,um,e=y
    K=p+m; J=q*(p-m)
    if np.min(K)<=0: raise ValueError('nonpositive incidence density')
    valence=J/K
    mask=valence<0
    number_flux=p*up+m*um
    charge_flux=q*(p*up-m*um)
    dy=rhs(y,dx,q,mass)
    dN=dy[0]+dy[1]
    dJ=q*(dy[0]-dy[1])
    dt_v=(dJ-valence*dN)/K
    transport_residual=K*(dt_v+(number_flux/K)*derivative(valence,dx))+derivative(charge_flux-valence*number_flux,dx)
    energy=dx*np.sum(.5*e**2+.5*mass*(p*up**2+m*um**2))
    return {'min_species_density':float(min(np.min(p),np.min(m))),
            'max_abs_velocity':float(max(np.max(abs(up)),np.max(abs(um)))),
            'gauss_rms':float(np.sqrt(np.mean((derivative(e,dx)-J)**2))),
            'valence_transport_residual_rms':float(np.sqrt(np.mean(transport_residual**2))),
            'net_charge':float(dx*np.sum(J)), 'incidence':float(dx*np.sum(K)),
            'signed_total':float(dx*np.sum(K*valence)),
            'negative_species_fraction':float(np.sum(m)/np.sum(K)),
            'negative_fraction_grid':float(np.sum(K[mask])/np.sum(K)),
            'negative_fraction_interpolated':interpolated_negative_fraction(K,J,dx),
            'naive_weighted_total':float(dx*np.sum(K*J)),
            'electrostatic_plus_kinetic_energy':float(energy)}


def run(n, **kwargs):
    result=evolve(n,**kwargs)
    return {'n':n,'steps':result['steps'],'dt':result['dt'],
            'initial':diagnostics(result['initial'],result['dx'],result['q'],result['mass']),
            'final':diagnostics(result['final'],result['dx'],result['q'],result['mass'])}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--grids',type=int,nargs='+',default=[64,128,256])
    parser.add_argument('--end',type=float,default=1.)
    parser.add_argument('--receipt',default='verification/two_fluid_incidence_receipt.json')
    args=parser.parse_args()
    data={'description':'1D periodic fixed-background nonrelativistic two-fluid numerical control; no experiential identification or gravity derived',
          'parameters':{'amplitude':.1,'modulation':.5,'q':1.,'mass':1.,'k':2,'end':args.end,'cfl':.15},
          'runs':[run(n,end=args.end) for n in args.grids]}
    Path(args.receipt).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__': main()
