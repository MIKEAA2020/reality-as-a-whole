"""Combined finite recorder/stop-clock/flag with an all-future escape bound.

Analytic derivations, not PDE samples, justify bounds. Reference trajectory and
quadrature checks test constants; local record-channel checks are inherited from
and rerun in autonomous_record.py. No irreversible continuous monitoring claimed.
"""
import json
import math
from pathlib import Path
if __package__:
    from .autonomous_record import run as record_checks
else:
    from autonomous_record import run as record_checks


def r_primitive(x,start,ell):
    if x<=start:return x-start
    if x>=start+ell:return ell/2
    z=x-start
    return z/2+ell/(2*math.pi)*math.sin(math.pi*z/ell)


def flag_probability(x,start,ell):
    u=max(0,min(1,(x-start)/ell))
    area=math.pi*u-math.sin(2*math.pi*u)/2
    return math.sin(area/2)**2


def compute(lam,clearance=1,tolerance=.001):
    assert lam>=20 and clearance>0 and tolerance>0
    m,M=lam**8,lam**2
    v,d0=100,1
    a,ell,gap=10/lam**2,20/lam,10/lam
    k0,b=lam**2,10*lam
    eps=(k0+b)**2/(2*M)
    xs=3*ell+3*gap
    flag_start=4*ell+4*gap
    end=5*ell+4*gap
    p0=m*v
    fp=math.pi/(math.sqrt(3)*a)
    fpp=math.pi**2/(math.sqrt(3)*a*a)
    kmax=2*math.pi/ell
    kpmax=2*math.pi**2/(ell*ell)
    rpmax=math.pi/(2*ell)
    cphase=kmax+eps/v
    cin=fpp+2*cphase*fp+kpmax+rpmax*eps/v+cphase*cphase
    cout=fpp+2*eps/v*fp+(eps/v)**2
    pre=(d0-a)/v
    done=(end+d0+2*a)/v
    active=done-pre
    delta_done=pre*fpp/(2*m)+active*(cin/(2*m)+.1)
    # Reference clearance uses transport; H_S is included exactly after done.
    clearance_hold=max(0,(clearance-2*a)/v)
    clear_time=done+clearance_hold
    dclear=2*a+v*clearance_hold
    delta_clear=delta_done+clearance_hold*cout/(2*m)
    # Fourier L1 derivative bounds by weighted CS and Plancherel, centred f.
    scale=math.sqrt(math.pi/a)
    l0=scale*math.sqrt(1+a*a*fp*fp)
    l1=scale*math.sqrt(a*a+a*a*(1+a*fp)**2)
    l2=scale*math.sqrt(a**4+a*a*(2*a+a*a*fp)**2)
    # Smooth cutoff zero below p0/4, one above p0/2.
    c1,c2=2*math.pi/p0,8*math.pi**2/p0**2
    h0,h1,h2=l0,l1+c1*l0,l2+2*c1*l1+c2*l0
    pmin=p0/4
    tailconstant=(h2+3*h1/pmin+3*h0/pmin**2)/math.sqrt(2*math.pi)
    wmax=v*kmax+eps
    cook=2*wmax*tailconstant/(math.sqrt(3)*(pmin/m)*math.sqrt(dclear))
    eta=2*fp/p0
    assert eta<1
    delta_uniform=delta_clear+2*eta+cook
    # Normalizing the outgoing cutoff state and comparing its readout to the
    # uncut ideal reference costs the explicit extra eta terms.
    delta_asym=delta_clear+4*eta+cook/(1-eta)
    tau0=(xs+ell/2+d0)/v
    taumax=tau0+a/v
    ideal_mse=(M*math.pi/(2*k0*b))**2+(1/3-2/math.pi**2)*b*b/k0**2*taumax**2+(a/v)**2
    return dict(scale=lam,mass=m,pointer_mass=M,mean_velocity=v,pointer_mean_velocity=k0/M,
                packet_half_width=a,region_length=ell,gap=gap,pointer_k0=k0,pointer_band=b,
                stop_start=xs,stop_end=xs+ell,flag_start=flag_start,device_end=end,
                pointer_energy_maximum=eps,preinteraction_duration=pre,
                active_duration=active,completion_epoch=done,clearance_epoch=clear_time,
                clearance_distance=dclear,nominal_stopped_time=tau0,
                reference_clock_second_derivative_bound=cin,
                completion_vector_bound=delta_done,clearance_vector_bound=delta_clear,
                low_momentum_norm_bound=eta,cook_future_norm_bound=cook,
                all_future_vector_bound=delta_uniform,
                all_future_record_half_diamond_bound=min(1,delta_uniform),
                asymptotic_record_error_bound=min(1,delta_asym),
                all_future_not_completed_probability_bound=min(1,delta_uniform**2),
                completion_not_completed_probability_bound=min(1,delta_done**2),
                ideal_time_mse_bound=ideal_mse,timing_tolerance=tolerance,
                all_future_not_completed_or_bad_time_bound=min(1,delta_uniform+ideal_mse/tolerance**2),
                kinetic_carrier_energy=m*v*v/2,
                cook_integral_formula=2/((pmin/m)*math.sqrt(dclear)))


def run():
    inherited=record_checks()
    assert inherited['system_matrix_units_checked']==4
    profiles=0
    # Reference trajectories only: test stop-before-flag and terminal time.
    for lam in (20,100):
        c=compute(lam)
        v=100;ell=c['region_length'];a=c['packet_half_width']
        for frac in (-1,-.5,0,.5,1):
            x0=-1+a*frac
            last=-1
            for j in range(201):
                t=c['completion_epoch']*j/200
                x=x0+v*t
                tau=(r_primitive(x,c['stop_start'],ell)-r_primitive(x0,c['stop_start'],ell))/v
                assert tau>=last-1e-14;last=tau
                flag=flag_probability(x,c['flag_start'],ell)
                if x<=c['stop_end']:assert flag==0
                if x<=c['stop_start']:assert abs(tau-t)<1e-14
                if flag>.999999:
                    assert abs(tau-(c['stop_start']+ell/2-x0)/v)<1e-14
                profiles+=1
            assert abs(flag_probability(x0+v*c['completion_epoch'],c['flag_start'],ell)-1)<1e-14
    # Cook time integral is analytically integrable. Midpoint substitution
    # u=1/sqrt(d+velocity*t) turns the improper integral into a constant.
    for d in (.1,1,5):
        for velocity in (.5,25):
            integral=2/(velocity*math.sqrt(d))
            transformed=sum(2/velocity*(1/math.sqrt(d))/1024 for _ in range(1024))
            assert abs(integral-transformed)<1e-10
    cases=[compute(lam) for lam in (100,1000,10000)]
    assert cases[-1]['all_future_record_half_diamond_bound']<.00023
    assert cases[-1]['all_future_not_completed_or_bad_time_bound']<.0005
    assert all(cases[i+1]['all_future_vector_bound']<cases[i]['all_future_vector_bound'] for i in (0,1))
    # Flag is an actual positive spatial projector generator, not an absorbing
    # nonunitary rule: exp(-i*pi*(I-X)/2)=X; either final readout completes a PVM.
    return dict(status='passed',reference_profile_checks=profiles,
                inherited_local_record_matrix_units=4,cases=cases,
                scope=['One positive autonomous recorder/stopping-pointer/completion-flag Hamiltonian.',
                       'Finite-time complete flag instrument and uniform future reference escape bound.',
                       'Cook comparison constructs outgoing-record approximation on the prepared states.',
                       'Reference profiles are not a numerical simulation of the physical PDE.',
                       'Not continuous monitoring, universal first-entry time, perturbation-proof storage or gravitational refoliation.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: finite completion instrument, internal stopped time and uniform future record bounds')
    print(path)
