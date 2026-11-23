#!/usr/bin/env python3
"""Planar classical ADM evolution of the documented zero-charge initial data.

Periodic 4th-order finite differences and RK4; pure Python standard library.
This is a bounded convergence experiment in a symmetry reduction, not a
fundamental theory, an empirical fit, or a demonstrated long-time evolution.
"""
import argparse
import json
import math

NAMES = ('u', 'v', 'kx', 'ky', 'c1', 'c2', 'p1', 'p2', 'ax', 'E', 'T', 'tx', 'pT')


def derivative(a, h):
    n = len(a)
    return [(a[(i-2)%n]-8*a[(i-1)%n]+8*a[(i+1)%n]-a[(i+2)%n])/(12*h)
            for i in range(n)]


def second(a, h):
    n = len(a)
    return [(-a[(i-2)%n]+16*a[(i-1)%n]-30*a[i]+16*a[(i+1)%n]-a[(i+2)%n])/(12*h*h)
            for i in range(n)]


def initial(n, kappa):
    if n < 12:
        raise ValueError('need at least 12 grid points')
    x = [2*math.pi*i/n for i in range(n)]
    k0 = -math.sqrt(15*kappa/2)/3  # expanding, since K_ij=-0.5 dot(h_ij)
    pt, tx = [], []
    for t in x:
        f = math.sin(t)*math.cos(t)
        s = 4-math.sin(t)**2
        p = math.sqrt((s+math.sqrt(s*s-4*f*f))/2)
        pt.append(p)
        tx.append(f/p)
    def clock_value(t):
        # T'=sin(x)cos(x)/pT and T(0)=0. With z=sin²(x),
        # integrate dT/dz=1/(2*pT(z)); periodic and reflection symmetric.
        z = math.sin(t)**2
        count = 128
        dz = z/count
        def integrand(y):
            p = math.sqrt((4-y+math.sqrt(16-12*y+5*y*y))/2)
            return 1/(2*p)
        return dz/3*(integrand(0)+integrand(z)
                     +4*sum(integrand(i*dz) for i in range(1,count,2))
                     +2*sum(integrand(i*dz) for i in range(2,count,2)))
    zero, one = [0.0]*n, [1.0]*n
    return {'u':zero[:], 'v':zero[:], 'kx':[k0]*n, 'ky':[k0]*n,
            'c1':one[:], 'c2':[math.cos(t) for t in x],
            'p1':zero[:], 'p2':[math.cos(t) for t in x], 'ax':zero[:],
            'E':[math.sin(t) for t in x], 'T':[clock_value(t) for t in x],
            'tx':tx, 'pT':pt}


def geometry_and_matter(s, h):
    u,v = s['u'],s['v']
    ux,vx,vxx = derivative(u,h),derivative(v,h),second(v,h)
    c1x,c2x = derivative(s['c1'],h),derivative(s['c2'],h)
    data = {k: [] for k in ('rx','ry','vol','d1','d2','rho','sx','sy','q')}
    for i in range(len(u)):
        au, bv = math.exp(u[i]), math.exp(v[i])
        vol = au*bv*bv
        rx = -2/(au*au)*(vxx[i]+vx[i]**2-ux[i]*vx[i])
        ry = -1/(au*au)*(vxx[i]+2*vx[i]**2-ux[i]*vx[i])
        # D_x chi = partial chi - A_x J chi, e=1.
        d1 = c1x[i]+s['ax'][i]*s['c2'][i]
        d2 = c2x[i]-s['ax'][i]*s['c1'][i]
        kin = (s['p1'][i]**2+s['p2'][i]**2+s['pT'][i]**2)/(vol*vol)
        grad = (d1*d1+d2*d2+s['tx'][i]**2)/(au*au)
        e2 = (s['E'][i]/(bv*bv))**2
        rho = (kin+grad+e2)/2
        sx = (kin+grad-e2)/2
        sy = (kin-grad+e2)/2
        for key,val in (('rx',rx),('ry',ry),('vol',vol),('d1',d1),('d2',d2),
                        ('rho',rho),('sx',sx),('sy',sy),
                        ('q',s['p2'][i]*s['c1'][i]-s['p1'][i]*s['c2'][i])):
            data[key].append(val)
    return data


def rhs(s, h, kappa, lapse=1.0):
    n = len(s['u'])
    data = geometry_and_matter(s,h)
    u,v = s['u'],s['v']
    output = {name: [0.0]*n for name in NAMES}
    flux1 = [math.exp(2*v[i]-u[i])*data['d1'][i] for i in range(n)]
    flux2 = [math.exp(2*v[i]-u[i])*data['d2'][i] for i in range(n)]
    flux_t = [math.exp(2*v[i]-u[i])*s['tx'][i] for i in range(n)]
    dflux1,dflux2,dfluxt = derivative(flux1,h),derivative(flux2,h),derivative(flux_t,h)
    clock_rate = [s['pT'][i]/data['vol'][i] for i in range(n)]
    dclock = derivative(clock_rate,h)
    for i in range(n):
        kx,ky=s['kx'][i],s['ky'][i]
        trace=kx+2*ky
        sx,sy,rho=data['sx'][i],data['sy'][i],data['rho'][i]
        trace_s=sx+2*sy
        output['u'][i]=-kx
        output['v'][i]=-ky
        output['kx'][i]=data['rx'][i]+trace*kx-kappa*(sx-(trace_s-rho)/2)
        output['ky'][i]=data['ry'][i]+trace*ky-kappa*(sy-(trace_s-rho)/2)
        output['c1'][i]=s['p1'][i]/data['vol'][i]
        output['c2'][i]=s['p2'][i]/data['vol'][i]
        # D_x of vector flux; m=0, e=1.
        output['p1'][i]=dflux1[i]+s['ax'][i]*flux2[i]
        output['p2'][i]=dflux2[i]-s['ax'][i]*flux1[i]
        output['ax'][i]=math.exp(u[i]-2*v[i])*s['E'][i]
        output['E'][i]=flux1[i]*(-s['c2'][i])+flux2[i]*s['c1'][i]
        output['T'][i]=clock_rate[i]
        output['tx'][i]=dclock[i]
        output['pT'][i]=dfluxt[i]
    return {name: [lapse*x for x in output[name]] for name in NAMES}


def add_scaled(a, b, scale):
    return {name:[x+scale*y for x,y in zip(a[name],b[name])] for name in NAMES}


def step(s, dt, h, kappa, lapse=1.0):
    a=rhs(s,h,kappa,lapse)
    b=rhs(add_scaled(s,a,dt/2),h,kappa,lapse)
    c=rhs(add_scaled(s,b,dt/2),h,kappa,lapse)
    d=rhs(add_scaled(s,c,dt),h,kappa,lapse)
    return {name:[x+dt*(v1+2*v2+2*v3+v4)/6
                  for x,v1,v2,v3,v4 in zip(s[name],a[name],b[name],c[name],d[name])]
            for name in NAMES}


def diagnostics(s, h, kappa):
    data=geometry_and_matter(s,h)
    vx=derivative(s['v'],h)
    kyx=derivative(s['ky'],h)
    ex=derivative(s['E'],h)
    clock_derivative=derivative(s['T'],h)
    ham, mom, gauss, norm_clock = [], [], [], []
    for i in range(len(s['u'])):
        kx,ky=s['kx'][i],s['ky'][i]
        tr=kx+2*ky
        ham.append(data['rx'][i]+2*data['ry'][i]+tr*tr-kx*kx-2*ky*ky
                   -2*kappa*data['rho'][i])
        mom.append(2*vx[i]*(kx-ky)-2*kyx[i]
                   +kappa*(s['p1'][i]*data['d1'][i]+s['p2'][i]*data['d2'][i]
                           +s['pT'][i]*s['tx'][i])/data['vol'][i])
        gauss.append(ex[i]-data['q'][i])
        norm_clock.append((s['pT'][i]/data['vol'][i])**2
                          -(s['tx'][i]/math.exp(s['u'][i]))**2)
    rms=lambda xs: math.sqrt(sum(x*x for x in xs)/len(xs))
    return {'ham_rms':rms(ham), 'mom_rms':rms(mom), 'gauss_rms':rms(gauss),
            'ham_max':max(map(abs,ham)), 'mom_max':max(map(abs,mom)),
            'gauss_max':max(map(abs,gauss)), 'total_charge':(2*math.pi)**2*h*sum(data['q']),
            'min_clock_timelike_margin':min(norm_clock),
            'clock_gradient_rms':rms([a-b for a,b in zip(clock_derivative,s['tx'])]),
            'charge_rms':rms(data['q']), 'charge_at_x0':data['q'][0],
            'proper_charge_density_at_x0':data['q'][0]/data['vol'][0],
            'clock_at_x0':s['T'][0], 'area_factor_at_x0':math.exp(2*s['v'][0]),
            'mean_u':sum(s['u'])/len(s['u']), 'mean_v':sum(s['v'])/len(s['v']),
            'proper_area_mean':sum(math.exp(2*z) for z in s['v'])/len(s['v'])}


def evolve(n=64, end=0.25, kappa=0.02, cfl=0.1, lapse=1.0):
    if n < 12 or end <= 0 or kappa < 0 or cfl <= 0 or lapse <= 0:
        raise ValueError('require n>=12, nonnegative kappa and positive end, cfl and lapse')
    h=2*math.pi/n
    nsteps=math.ceil(lapse*end/(cfl*h))
    dt=end/nsteps
    s=initial(n,kappa)
    start=diagnostics(s,h,kappa)
    min_clock=start['min_clock_timelike_margin']
    max_abs_charge=abs(start['total_charge'])
    min_marker_rate=s['pT'][0]/math.exp(s['u'][0]+2*s['v'][0])
    for _ in range(nsteps):
        s=step(s,dt,h,kappa,lapse)
        clock_margin=min((s['pT'][i]/math.exp(s['u'][i]+2*s['v'][i]))**2
                         -(s['tx'][i]/math.exp(s['u'][i]))**2 for i in range(n))
        min_clock=min(min_clock,clock_margin)
        charge=(2*math.pi)**2*h*sum(s['p2'][i]*s['c1'][i]-s['p1'][i]*s['c2'][i] for i in range(n))
        max_abs_charge=max(max_abs_charge,abs(charge))
        min_marker_rate=min(min_marker_rate,s['pT'][0]/math.exp(s['u'][0]+2*s['v'][0]))
    return {'grid':n, 'end':end, 'kappa':kappa, 'lapse':lapse, 'steps':nsteps, 'dt':dt,
            'sampled_min_clock_timelike_margin':min_clock,
            'sampled_min_marker_clock_rate_per_proper_time':min_marker_rate,
            'sampled_max_abs_total_charge':max_abs_charge,
            'initial':start, 'final':diagnostics(s,h,kappa)}, s


def evolve_to_clock(n=128, target=1.0, kappa=0.02, cfl=0.1, lapse=1.0, max_time=2.0):
    """Advance the x=0 marker to a target scalar-clock reading.

    Bracket the target and use fractional RK4 substeps, not linear state
    interpolation. The marker is defined by the initial coordinate symmetry;
    this is not a constructed complete Dirac observable.
    """
    if n < 12 or target <= 0 or kappa < 0 or cfl <= 0 or lapse <= 0 or max_time <= 0:
        raise ValueError('invalid grid, target, parameters or max_time')
    h=2*math.pi/n
    dt=cfl*h/lapse
    s=initial(n,kappa)
    t=0.0
    while t < max_time:
        next_dt=min(dt,max_time-t)
        candidate=step(s,next_dt,h,kappa,lapse)
        if candidate['T'][0] >= target:
            lo,hi=0.0,next_dt
            for _ in range(32):
                mid=(lo+hi)/2
                trial=step(s,mid,h,kappa,lapse)
                if trial['T'][0] < target:
                    lo=mid
                else:
                    hi=mid
            final_dt=(lo+hi)/2
            s=step(s,final_dt,h,kappa,lapse)
            t += final_dt
            return {'grid':n, 'clock_target':target, 'coordinate_time':t,
                    'kappa':kappa, 'lapse':lapse, 'diagnostics':diagnostics(s,h,kappa)}, s
        s=candidate
        t+=next_dt
    raise ValueError('target clock reading not reached within max_time')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grids', nargs='+', type=int, default=[32,64,128])
    parser.add_argument('--end', type=float, default=.25)
    parser.add_argument('--kappa', type=float, default=.02)
    parser.add_argument('--cfl', type=float, default=.1)
    parser.add_argument('--lapse', type=float, default=1.0)
    parser.add_argument('--clock-target', type=float, default=None,
                        help='also compare gravity with the kappa=0 fixed-metric limit at this local clock reading')
    args=parser.parse_args()
    runs=[evolve(n,args.end,args.kappa,args.cfl,args.lapse)[0] for n in args.grids]
    receipt={'method':'periodic 4th-order finite differences, RK4',
             'units':'L=2π, e=1, m=0, shift=0, A0=0; constant positive lapse',
             'runs':runs}
    if args.clock_target is not None:
        receipt['matched_clock_comparison'] = {
            'gravity':evolve_to_clock(args.grids[-1],args.clock_target,args.kappa,args.cfl,args.lapse)[0],
            'fixed_metric_limit':evolve_to_clock(args.grids[-1],args.clock_target,0,args.cfl,args.lapse)[0]}
    print(json.dumps(receipt, indent=2, allow_nan=False))


if __name__=='__main__':
    main()
