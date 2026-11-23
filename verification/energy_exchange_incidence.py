#!/usr/bin/env python3
"""Energy-transfer accounting in the two-fluid fixed-background model.

The sign of work is not identified with actual valence by physics. Numerical
integrals here check an explicitly stipulated finite classical system only.
"""
import argparse
import json
import math
from pathlib import Path
import numpy as np
from verification.two_fluid_incidence_dynamics import initial, rhs, interpolated_negative_fraction


def field_energy(y,dx):
    return float(dx*np.sum(y[4]**2)/2)


def rate(y,dx,q=1.):
    p,m,up,um,e=y
    current=q*(p*up-m*um)
    return float(-dx*np.sum(e*current))


def weighted_rate(y, dx, q=1., strength=.5, scale=.001):
    """Illustrative bounded response factor, not an empirical subject law."""
    p,m,up,um,e=y
    h=-q*(p*up-m*um)*e
    chi=1+strength*h/(scale+np.abs(h))
    return float(dx*np.sum(chi*h))


def integrate(n=128, end=1., amplitude=.1, modulation=.5, cfl=.15):
    if end == 0 or cfl<=0: raise ValueError('end must be nonzero and cfl positive')
    dx=2*np.pi/n
    y=initial(n,amplitude,modulation)
    count=max(1,math.ceil(abs(end)/(cfl*dx)))
    dt=end/count
    U0=field_energy(y,dx)
    work=0.; weighted_work=0.; incidence=0.; negative=0.
    for _ in range(count):
        a=rhs(y,dx); ya=y+dt*a/2
        b=rhs(ya,dx); yb=y+dt*b/2
        c=rhs(yb,dx); yc=y+dt*c
        d=rhs(yc,dx)
        # Use the same RK4 stages to integrate ∫ -jE dt.
        work+=dt*(rate(y,dx)+2*rate(ya,dx)+2*rate(yb,dx)+rate(yc,dx))/6
        weighted_work+=dt*(weighted_rate(y,dx)+2*weighted_rate(ya,dx)+2*weighted_rate(yb,dx)+weighted_rate(yc,dx))/6
        # Trapezoidal time quadrature and linearly interpolated spatial roots.
        def measure(z):
            p,m,up,um,e=z
            K=p+m; h=-(p*up-m*um)*e
            total=dx*np.sum(K)
            return float(total),float(total*interpolated_negative_fraction(K,h,dx))
        total0,neg0=measure(y)
        ynew=y+dt*(a+2*b+2*c+d)/6
        total1,neg1=measure(ynew)
        incidence+=abs(dt)*(total0+total1)/2
        negative+=abs(dt)*(neg0+neg1)/2
        y=ynew
    return {'n':n,'end':end,'steps':count,'initial_field_energy':U0,
            'final_field_energy':field_energy(y,dx),'signed_work_integral':work,
            'response_weighted_work_integral':weighted_work,
            'field_energy_change':field_energy(y,dx)-U0,
            'work_identity_error':work-(field_energy(y,dx)-U0),
            'total_incidence':incidence,'negative_incidence_fraction':negative/incidence,
            'end_density_min':float(min(np.min(y[0]),np.min(y[1]))),
            'end_speed_max':float(max(np.max(abs(y[2])),np.max(abs(y[3]))))}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--grids',type=int,nargs='+',default=[64,128,256,512])
    parser.add_argument('--receipt',default='verification/energy_exchange_incidence_receipt.json')
    args=parser.parse_args()
    rows=[]
    for n in args.grids:
        future=integrate(n,1.)
        past=integrate(n,-1.)
        rows.append({'n':n,'future':future,'past_reversed_orientation':past,
                     'symmetric_endpoint_field_energy_difference':future['final_field_energy']-past['final_field_energy'],
                     'symmetric_response_weighted_integral':future['response_weighted_work_integral']-past['response_weighted_work_integral'],
                     'symmetric_negative_incidence_fraction':(future['negative_incidence_fraction']*future['total_incidence']+past['negative_incidence_fraction']*past['total_incidence'])/(future['total_incidence']+past['total_incidence'])})
    data={'scope':'finite 1D two-fluid classical control, endpoint equality is imposed by time symmetry; no real experience or zero physical energy derived','runs':rows}
    Path(args.receipt).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__': main()
