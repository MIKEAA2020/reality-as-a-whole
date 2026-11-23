"""Closed homogeneous two-fluid oscillator and conditional incidence controls.

Fixed-background nonrelativistic plasma; not an experiential or cosmological model.
"""
import argparse
import json
import math


def state(t, amplitude=0.1):
    return amplitude*math.cos(t), amplitude*math.sin(t)


def organization(e, j, b, mode):
    d=e*e+j*j
    if d <= 0:
        raise ValueError('the zero oscillator has no phase-defined organization')
    if abs(b) >= 1:
        raise ValueError('use |b|<1 for strictly positive response')
    if mode == 'flow':
        return 1+2*b*e*j/d
    if mode == 'energy':
        return 1+b*(e*e-j*j)/d
    raise ValueError('unknown mode')


def rhs(y, b):
    e,j=y[:2]
    h=-e*j
    return (-j,e,h,organization(e,j,b,'flow')*h,organization(e,j,b,'energy')*h)


def rk4(y, dt, b):
    def step(v,k,factor): return [a+factor*dt*x for a,x in zip(v,k)]
    a=rhs(y,b)
    c=rhs(step(y,a,.5),b)
    d=rhs(step(y,c,.5),b)
    e=rhs(step(y,d,1),b)
    return [v+dt*(aa+2*cc+2*dd+ee)/6 for v,aa,cc,dd,ee in zip(y,a,c,d,e)]


def run(steps=512, amplitude=0.1, b=0.5):
    if steps<=0 or amplitude<=0: raise ValueError('positive steps and amplitude required')
    # (field E, current j, unweighted exchange, flow-weighted, energy-weighted)
    y=[amplitude,0.0,0.0,0.0,0.0]
    initial_energy=amplitude*amplitude/2
    dt=2*math.pi/steps
    max_energy_drift=0.0
    for _ in range(steps):
        y=rk4(y,dt,b)
        max_energy_drift=max(max_energy_drift,abs((y[0]**2+y[1]**2)/2-initial_energy))
    target=-b*math.pi*amplitude*amplitude/2
    return {'steps':steps,'amplitude':amplitude,'b':b,
            'initial_physical_energy':initial_energy,
            'endpoint_E':y[0],'endpoint_j':y[1],
            'unweighted_exchange':y[2], 'flow_weighted_exchange':y[3],
            'energy_weighted_exchange':y[4], 'exact_flow_weighted_exchange':target,
            'flow_error':y[3]-target, 'max_energy_drift':max_energy_drift}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, nargs='+', default=[64,128,256])
    parser.add_argument('--amplitude',type=float,default=.1)
    parser.add_argument('--b',type=float,default=.5)
    args=parser.parse_args()
    print(json.dumps([run(n,args.amplitude,args.b) for n in args.steps],indent=2))


if __name__=='__main__': main()
