"""Finite carrier, gravitational spectral fit and complete outgoing records.

Analytic constraint/rigging and channel bounds: FINITE_REFERENCE_GRAVITY.md.
No gravitational PDE or cosmological data are simulated.
"""
import json
import math
from pathlib import Path
if __package__:
    from .autonomous_record import run as record_checks
else:
    from autonomous_record import run as record_checks


def design(q):
    v=100.;m=q**8;p0=m*v
    a=10/q**2;ell=20/q;gap=10/q;d0=1.
    omega=.1;length=4*ell+3*gap
    f1=math.pi/(math.sqrt(3)*a);f2=math.pi**2/(math.sqrt(3)*a*a)
    k=2*math.pi/ell;kp=2*math.pi**2/ell**2
    cin=f2+2*k*f1+kp+k*k
    pre=(d0-a)/v;done=(length+d0+2*a)/v
    active=done-pre
    delta0=pre*f2/(2*m)+active*(cin/(2*m)+omega)
    clearance=1.;hold=(clearance-2*a)/v
    tc=done+hold;dc=delta0+hold*f2/(2*m)
    s=math.sqrt(math.pi/a)
    l0=s*math.sqrt(1+a*a*f1*f1)
    l1=s*math.sqrt(a*a+a*a*(1+a*f1)**2)
    l2=s*math.sqrt(a**4+a*a*(2*a+a*a*f1)**2)
    c1=2*math.pi/p0;c2=8*math.pi**2/p0**2
    h0=l0;h1=l1+c1*l0;h2=l2+2*c1*l1+c2*l0
    pmin=p0/4;vmin=pmin/m
    tail=(h2+3*h1/pmin+3*h0/pmin**2)/math.sqrt(2*math.pi)
    eta=2*f1/p0
    cook=2*v*k*tail/(math.sqrt(3)*vmin*math.sqrt(clearance))
    # One fixed Lambda and scalar band for all three resource designs.
    wg=1e28;plo=.05;phi=.25
    nu_hi=math.sqrt(.25-8*plo*plo/3)
    nu_lo=math.sqrt(.25-8*phi*phi/3)
    nu_mid=(nu_hi+nu_lo)/2;dnu=(nu_hi-nu_lo)/2
    kinetic=m*v*v/2
    n=max(0,math.ceil(((kinetic+omega)/wg-1-nu_mid)/2))
    center=wg*(2*n+1+nu_mid)
    rest=center-kinetic
    width=wg*dnu
    assert rest>=omega and width>0 and eta<1
    sigma=v*f1+f2/(2*m)+omega
    leak=sigma/width
    assert leak<.01
    # Polar-normalized projected preparation is an isometry; this safe bound
    # avoids cancellation in sqrt(2*(1-sqrt(1-leak**2)))).
    prep=2*leak
    uniform=prep+dc+2*eta+cook
    outgoing=prep+dc+4*eta+cook/(1-eta)
    tolerance={100:.014,1000:.00024,10000:.000013}[q]
    assert uniform<tolerance and outgoing<tolerance
    return dict(scale=q,carrier_mass=m,carrier_mean_momentum=p0,
                mean_velocity=v,packet_half_width=a,region_length=ell,gap=gap,
                device_end=length,completion_epoch=done,clearance_epoch=tc,
                kinetic_center=kinetic,register_rest_energy=rest,
                gravitational_frequency=wg,cosmological_constant=-4*wg*wg/3,
                scalar_positive_band=[plo,phi],radial_level=n,
                spectral_center=center,spectral_half_width=width,
                scaled_half_width=dnu,nu_midpoint=nu_mid,
                initial_energy_deviation_norm_bound=sigma,
                rejected_spectral_norm_bound=leak,preparation_isometry_error_bound=prep,
                preprojection_completion_vector_bound=delta0,
                preprojection_clearance_vector_bound=dc,
                low_momentum_norm_bound=eta,cook_future_norm_bound=cook,
                all_future_record_half_diamond_bound=uniform,
                all_future_not_completed_probability_bound=uniform**2,
                outgoing_record_error_bound=outgoing,
                outside_right_outgoing_sector_probability_bound=(prep+dc+2*eta+cook/(1-eta))**2)


def run():
    inherited=record_checks()
    assert inherited['system_matrix_units_checked']==4
    cases=[design(q) for q in (100,1000,10000)]
    # Invert the gravitational spectrum in scaled coordinates to avoid loss of
    # precision when a narrow band sits on a very large radial level.
    checks=0
    for c in cases:
        for j in range(1,40):
            x=c['scaled_half_width']*(2*j/40-1)
            nu=c['nu_midpoint']+x
            p=math.sqrt(3/8*(.25-nu*nu))
            assert c['scalar_positive_band'][0]<p<c['scalar_positive_band'][1]
            nu_back=math.sqrt(.25-8*p*p/3)
            assert abs(nu_back-nu)<1e-14
            # |d epsilon/dp|=8 omega_g p/(3 nu). Rigging and the
            # unitary root rescaling cancel this positive Jacobian.
            jac=8*c['gravitational_frequency']*p/(3*nu)
            coefficient=math.sqrt(jac)
            assert abs(coefficient*coefficient/jac-1)<1e-14
            h=1e-7
            derivative=(math.sqrt(.25-8*(p+h)**2/3)-math.sqrt(.25-8*(p-h)**2/3))/(2*h)
            assert abs(derivative+8*p/(3*nu))<1e-7
            checks+=1
    # Uniform polar-isometry bound: exact worst-angle distance <=2 leak.
    polar=0
    for eps in (.0001,.01,.1,.5,.9):
        exact=math.sqrt(2*eps*eps/(1+math.sqrt(1-eps*eps)))
        assert exact<=2*eps
        polar+=1
    # A finite energy window gives nonorthogonal phase-reference vectors.
    # Normalized overlap is sinc(W dt), not a delta function.
    overlaps=[]
    for u in (0,.1,1,math.pi):
        overlap=math.sin(u)/u if u else 1.
        overlaps.append(dict(scaled_epoch_difference=u,normalized_overlap=overlap))
    assert overlaps[1]['normalized_overlap']>.99
    return dict(status='passed',cases=cases,spectral_inverse_and_rigging_checks=checks,
                polar_isometry_checks=polar,inherited_record_matrix_units=4,
                finite_band_phase_overlaps=overlaps,
                scope=['No dust or canonical external time field in the action.',
                       'Finite normalizable carrier; projected preparation is correlated, not an unchanged product.',
                       'Declared subcritical scalar sector, Friedrichs domain and one fixed negative Lambda.',
                       'Finite-time local record POVM; conserved outgoing instrument includes failure.',
                       'Single late interrogation, not continuous monitoring or repeated-read stability.',
                       'Spectral phase-reference POVM is nonorthogonal; its physical readout/reset engine is not derived.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: finite reference carrier in gravitational constraint, spectral fit and complete record bounds')
    print(path)
