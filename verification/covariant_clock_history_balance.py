#!/usr/bin/env python3
"""Clock-slice fluxes from the existing nonlinear planar Einstein–matter run.

Linear interpolation between time steps is deliberately used, so slice output
is expected to converge at second order, despite fourth-order field evolution.
These physical current integrals are not claims about actual experience.
"""
import argparse
import json
import math
from verification import evolve_covariant_zero_initial_data as ev


def snapshot(s, h):
    data = ev.geometry_and_matter(s, h)
    values = []
    for i in range(len(s['u'])):
        volume = data['vol'][i]
        rate = s['pT'][i]/volume
        gradient = s['tx'][i]
        margin = rate**2-(gradient/math.exp(s['u'][i]))**2
        if rate <= 0 or margin <= 0:
            raise ValueError('clock ceases to be future-timelike at a sampled point')
        # Maxwell equation E_dot = -j, with j = sqrt(-g) J^x.
        flux = -math.exp(2*s['v'][i]-s['u'][i]) * (
            -data['d1'][i]*s['c2'][i] + data['d2'][i]*s['c1'][i])
        values.append((s['T'][i], data['q'][i], flux, gradient, rate,
                       math.sqrt(margin)))
    return values


def clock_slices(n=128, targets=(.3, .6, 1.0), kappa=.02, end=1.0, cfl=.1):
    if n < 12 or kappa < 0 or end <= 0 or cfl <= 0 or not targets:
        raise ValueError('invalid arguments')
    targets=tuple(targets)
    if any(targets[i] >= targets[i+1] for i in range(len(targets)-1)):
        raise ValueError('targets must be strictly increasing')
    h=2*math.pi/n
    steps=math.ceil(end/(cfl*h)); dt=end/steps
    s=ev.initial(n,kappa)
    prev=snapshot(s,h)
    if targets[0] <= max(row[0] for row in prev):
        raise ValueError('all targets must lie strictly above all initial clock readings')
    slices=[[None]*n for _ in targets]
    for _ in range(steps):
        s=ev.step(s,dt,h,kappa)
        curr=snapshot(s,h)
        for i, (old,new) in enumerate(zip(prev,curr)):
            if new[0] <= old[0]:
                raise ValueError('clock is not increasing at a sampled grid point')
            for k,target in enumerate(targets):
                if old[0] <= target <= new[0] and slices[k][i] is None:
                    f=(target-old[0])/(new[0]-old[0])
                    slices[k][i]=tuple(a+f*(b-a) for a,b in zip(old[1:],new[1:]))
        prev=curr
    if any(any(row is None for row in sl) for sl in slices):
        raise ValueError('end time must be after every clock crossing')
    area=(2*math.pi)**2
    results=[]
    for target,sl in zip(targets,slices):
        # dΣ J = (q + j T_x/T_t) dx dy dz, for t=t(T,x).
        fluxes=[q+j*tx/rate for q,j,tx,rate,scale in sl]
        naive=[v/row[4] for v,row in zip(fluxes,sl)]
        weight=[1+.5*math.cos(i*h) for i in range(n)]
        integrate=lambda a: area*h*sum(a)
        results.append({'T':target, 'charge':integrate(fluxes),
                        'omitting_tilt_flux':integrate([row[0] for row in sl]),
                        'tilt_flux_rms':math.sqrt(sum((v-row[0])**2 for v,row in zip(fluxes,sl))/n),
                        'unscaled_density_history_integrand':integrate(naive),
                        'weighted_incidence_integrand':integrate([w*q for w,q in zip(weight,fluxes)]),
                        'min_local_slice_flux_density':min(fluxes),
                        'max_local_slice_flux_density':max(fluxes),
                        'sampled_min_clock_scale':min(row[4] for row in sl)})
    return {'grid':n,'steps':steps,'dt':dt,'kappa':kappa,'slices':results}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--grids',nargs='+',type=int,default=[64,128,256])
    args=p.parse_args()
    print(json.dumps({'method':'planar RK4, fourth-order differences, linear time interpolation on T slices',
                      'results':[clock_slices(n) for n in args.grids]},indent=2,allow_nan=False))

if __name__ == '__main__':
    main()
