"""On-shell incoming preparation for the two-carrier gravitational recorder.

Uses the SAME H_2/compact-packet comparison as internal_reference_event.py.
Replaces its assumed polar encoding by finite-band incoming scattering states.
Analytic statements: INCOMING_CONSTRAINT_PREPARATION.md.
"""
import json
import math
from pathlib import Path
if __package__:
    from .internal_reference_event import design, gate_checks
else:
    from internal_reference_event import design, gate_checks


def cutoff(z):
    a=abs(z)
    if a<=.5:return 1.,0.,0.
    if a>=1:return 0.,0.,0.
    t=math.pi*(a-.5)
    return math.cos(t)**2,-math.copysign(1,z)*math.pi*math.sin(2*t),-2*math.pi**2*math.cos(2*t)


def incoming_constants(a,m,v,ell,d,band_factor=1e12):
    f1=math.pi/(math.sqrt(3)*a)
    delta=band_factor*f1;p0=m*v
    assert delta<p0/2
    removed=2*f1/delta
    norm_lower=1-removed
    scale=math.sqrt(math.pi/a)
    l0=scale*math.sqrt(1+a*a*f1*f1)
    l1=scale*math.sqrt(a*a+a*a*(1+a*f1)**2)
    l2=scale*math.sqrt(a**4+a*a*(2*a+a*a*f1)**2)
    c1=math.pi/delta;c2=2*math.pi**2/(delta*delta)
    h0=l0/norm_lower
    h1=(l1+c1*l0)/norm_lower
    h2=(l2+2*c1*l1+c2*l0)/norm_lower
    pmin=p0-delta;vmin=v*(1-delta/p0)
    tail=(h2+3*h1/pmin+3*h0/pmin**2)/math.sqrt(2*math.pi)
    constant=2*v*(2*math.pi/ell)*tail/(math.sqrt(3)*vmin)
    return dict(momentum_half_band=delta,momentum_half_band_fraction=delta/p0,
                removed_packet_norm_bound=removed,normalized_packet_error_bound=2*removed,
                cutoff_normalization_lower_bound=norm_lower,minimum_incoming_velocity=vmin,
                incoming_tail_constant=tail,incoming_integrated_constant=constant,
                initial_upstream_distance=d,finite_upstream_dressing_norm_bound=constant/math.sqrt(d))


def preparation(q,schedule):
    old=design(q,schedule)
    m=old['each_carrier_mass'];v=old['each_mean_velocity']
    a=old['each_packet_half_width'];ell=old['region_length']
    x=incoming_constants(a,m,v,ell,1.)
    y=incoming_constants(a,m,v,ell,old['reader_initial_distance'])
    bandcost=x['normalized_packet_error_bound']+y['normalized_packet_error_bound']
    incoming=x['finite_upstream_dressing_norm_bound']+y['finite_upstream_dressing_norm_bound']
    prep=bandcost+incoming
    dx=x['momentum_half_band'];dy=y['momentum_half_band']
    # Exact, cancellation-free sufficient bound on |H_0-E_c| on both bands.
    offset=v*dx+dx*dx/(2*m)+v*dy+dy*dy/(2*m)+.1
    width=old['spectral_half_width']
    assert offset<width
    delta=(prep+old['two_carrier_transport_norm_bound']+
           2*old['low_momentum_norm_sum']+old['recorder_cook_bound']+old['reader_cook_bound'])
    eta=old['low_momentum_norm_sum']
    sector=(prep+old['two_carrier_transport_norm_bound']+2*eta+
            (old['recorder_cook_bound']+old['reader_cook_bound'])/(1-eta))
    outgoing=sector+2*eta
    tolerance={100:.04,1000:.0005,10000:.000015}[q]
    assert delta<tolerance and outgoing<tolerance
    # Actual incoming state becomes arbitrarily close to ready free packets
    # at a finite earlier epoch; no compact-position state is called on-shell.
    readiness=[]
    for target in (1e-3,1e-5,1e-7):
        times=[((2*c['incoming_integrated_constant']/target)**2-
                c['initial_upstream_distance'])/c['minimum_incoming_velocity'] for c in (x,y)]
        past=max([0.]+times)
        bound=sum(c['incoming_integrated_constant']/math.sqrt(c['initial_upstream_distance']+
                   c['minimum_incoming_velocity']*past) for c in (x,y))
        assert bound<=target*(1+1e-12)
        readiness.append(dict(target_norm_error=target,finite_past_duration=past,
                              certified_ready_packet_norm_error=bound))
    return dict(scale=q,schedule=schedule,radial_level=old['radial_level'],
                gravitational_frequency=old['gravitational_frequency'],
                spectral_half_width=width,free_energy_support_offset_bound=offset,
                spectral_support_margin=width-offset,carrier_X=x,carrier_Q=y,
                product_band_preparation_error_bound=bandcost,
                incoming_dressing_error_at_reference_origin=incoming,
                total_preparation_comparison_cost=prep,
                all_future_record_channel_error=delta,
                expected_flag_pattern_deviation_probability_bound=delta**2,
                outgoing_record_channel_error=outgoing,
                outside_joint_right_outgoing_sector_probability_bound=sector**2,
                common_late_comparison_epoch=old['common_clearance_epoch'],
                finite_past_readiness_certificates=readiness)


def run():
    derivative_checks=0
    for j in range(-100,101):
        z=j/100
        c,d,dd=cutoff(z)
        assert 0<=c<=1 and abs(d)<=math.pi+1e-14 and abs(dd)<=2*math.pi**2+1e-14
        if .51<abs(z)<.99:
            h=1e-5
            fm=cutoff(z-h)[0];fp=cutoff(z+h)[0]
            assert abs((fp-fm)/(2*h)-d)<1e-7
            assert abs((fp-2*c+fm)/(h*h)-dd)<1e-5
            derivative_checks+=1
    # Scaled phase IBP condition holds for finite earlier epochs and x>=0.
    phase=0
    for p in (1.,2.,10.):
        for d in (.1,1.,10.):
            for s in (0.,.1,10.):
                for x in (0.,1.,10.):
                    m=2.;derivative=x+d+p*s/m
                    assert derivative>=d+p*s/m
                    assert (s/m)/derivative<=1/p+1e-14
                    phase+=1
    return dict(status='passed',smooth_cutoff_samples=201,
                cutoff_derivative_checks=derivative_checks,incoming_phase_checks=phase,
                gate_channels=gate_checks(),
                cases=[preparation(q,s) for s in ('late','early') for q in (100,1000,10000)],
                scope=['Physical incoming free seeds already satisfy the free gravitational constraint.',
                       'Wave operator intertwines free/interacting constraints; no polar encoding or off-shell projection.',
                       'Smooth finite momentum bands give normalizable finite-energy source packets.',
                       'Finite-past readiness is an error certificate, not exact finite-time state synthesis.',
                       'All outgoing failures retained; no ideal clock controller, time prior or omitted pulse energy.',
                       'Boundary/source state selection, reset, inhomogeneous gravity and phenomenal constitution remain open.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: on-shell finite-band incoming preparation, finite-past readiness and complete records')
    print(path)
