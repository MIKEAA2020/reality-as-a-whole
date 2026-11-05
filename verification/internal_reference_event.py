"""Two finite carriers: an autonomous validated internal reference event.

Analytic constraint, preparation and escape bounds: INTERNAL_REFERENCE_EVENT.md.
Only finite gate algebra and bound constants are evaluated, not a gravity PDE.
"""
import json
import math
from pathlib import Path


def bits(i):return [(i>>k)&1 for k in range(7,-1,-1)]
def index(b):return sum(x<<k for x,k in zip(b,range(7,-1,-1)))


def permutation(controls,target):
    result=[]
    for i in range(256):
        b=bits(i)
        if all(b[c] for c in controls):b[target]^=1
        result.append(index(b))
    assert sorted(result)==list(range(256))
    return result


def gate_checks():
    # S,D,M,E,F,R,V,G. Empty control list is an unconditional flag flip.
    recorder=[permutation([0],1),permutation([1],2),
              permutation([2],3),permutation([],4)]
    reader=[permutation([4],6),permutation([6,2],5),permutation([],7)]
    channels={}
    for name,sequence in [('late',recorder+reader),('early',reader+recorder)]:
        checked=0
        for r in range(2):
            for q in range(2):
                reduced={}
                for e in range(2):
                    out=[]
                    for s in (r,q):
                        j=index([s,0,0,e,0,0,0,0])
                        for p in sequence:j=p[j]
                        out.append(bits(j))
                    a,b=out
                    if a[3]==b[3]:
                        ka=tuple(a[:3]+a[4:]);kb=tuple(b[:3]+b[4:])
                        reduced[ka,kb]=reduced.get((ka,kb),0)+.5
                expected={}
                if r==q:
                    x=tuple([r,r,r,1,r,1,1] if name=='late' else [r,r,r,1,0,0,1])
                    expected[x,x]=1.
                assert reduced==expected,(name,r,q,reduced,expected)
                checked+=1
        channels[name]=checked
    return dict(gate_permutations_checked=7,full_basis_states_per_gate=256,
                late_matrix_units=channels['late'],early_matrix_units=channels['early'],
                late_success_probability=1,early_invalid_probability=1,
                early_completed_reader_flag_probability=1)


def packet(a,m,speed):
    f1=math.pi/(math.sqrt(3)*a);f2=math.pi**2/(math.sqrt(3)*a*a)
    return dict(a=a,m=m,speed=speed,p0=m*speed,f1=f1,f2=f2)


def active_second_derivative(p,ell):
    k=2*math.pi/ell;kp=2*math.pi**2/ell**2
    return p['f2']+2*k*p['f1']+kp+k*k


def escape(p,ell,clearance):
    a=p['a'];f1=p['f1'];p0=p['p0'];m=p['m']
    scale=math.sqrt(math.pi/a)
    l0=scale*math.sqrt(1+a*a*f1*f1)
    l1=scale*math.sqrt(a*a+a*a*(1+a*f1)**2)
    l2=scale*math.sqrt(a**4+a*a*(2*a+a*a*f1)**2)
    c1=2*math.pi/p0;c2=8*math.pi**2/p0**2
    h0=l0;h1=l1+c1*l0;h2=l2+2*c1*l1+c2*l0
    pmin=p0/4;vmin=pmin/m
    tail=(h2+3*h1/pmin+3*h0/pmin**2)/math.sqrt(2*math.pi)
    eta=2*f1/p0
    cook=2*p['speed']*(2*math.pi/ell)*tail/(math.sqrt(3)*vmin*math.sqrt(clearance))
    return eta,cook


def design(q,schedule="late"):
    m=q**8;v=u=100.;a=b=10/q**2;ell=ellr=20/q;gap=gapr=10/q
    x=packet(a,m,v);y=packet(b,m,u)
    lx=4*ell+3*gap;ly=3*ellr+2*gapr
    omega=.1;d0=1.;separation=.01
    prex=(d0-a)/v;donex=(lx+d0+2*a)/v
    clearx=donex+(1-2*a)/v
    assert schedule in ("late","early")
    prey=clearx+separation if schedule=="late" else .001
    dref=u*prey+b
    doney=(ly+dref+2*b)/u
    final=max(donex+(1-2*a)/v,doney+(1-2*b)/u)
    dx=v*final-d0-lx;dy=u*final-dref-ly
    assert dx>2*a and dy>2*b
    assert (prey>donex if schedule=="late" else doney<prex)
    tx=donex-prex;ty=doney-prey
    cx=active_second_derivative(x,ell);cy=active_second_derivative(y,ellr)
    transport=(final*x['f2']+tx*(cx-x['f2']))/(2*m)
    transport+=(final*y['f2']+ty*(cy-y['f2']))/(2*m)+omega*tx
    etax,cookx=escape(x,ell,dx);etay,cooky=escape(y,ellr,dy)
    eta=etax+etay;cook=cookx+cooky
    assert eta<1
    wg=1e28;plo=.05;phi=.25
    nu_hi=math.sqrt(.25-8*plo*plo/3);nu_lo=math.sqrt(.25-8*phi*phi/3)
    mid=(nu_hi+nu_lo)/2;half=(nu_hi-nu_lo)/2
    kinetic=m*v*v/2+m*u*u/2
    n=max(0,math.ceil(((kinetic+omega)/wg-1-mid)/2))
    center=wg*(2*n+1+mid);rest=center-kinetic;width=wg*half
    sigma=v*x['f1']+x['f2']/(2*m)+u*y['f1']+y['f2']/(2*m)+omega
    eps=sigma/width;alpha=2*eps
    assert eps<1 and rest>=omega
    uniform=alpha+transport+2*eta+cook
    sector=alpha+transport+2*eta+cook/(1-eta)
    outgoing=sector+2*eta
    tolerance={100:.03,1000:.0005,10000:.000014}[q]
    assert uniform<tolerance and outgoing<tolerance
    return dict(scale=q,schedule=schedule,each_carrier_mass=m,each_packet_half_width=a,
                each_mean_velocity=v,region_length=ell,gap=gap,
                recorder_end=lx,reader_end=ly,reader_initial_distance=dref,
                recorder_comparison_completion=donex,reader_earliest_comparison_entry=prey,
                reader_comparison_completion=doney,common_clearance_epoch=final,
                recorder_clearance=dx,reader_clearance=dy,
                reader_active_window=ty,recorder_active_window=tx,
                gravitational_frequency=wg,cosmological_constant=-4*wg*wg/3,
                scalar_positive_band=[plo,phi],radial_level=n,
                spectral_center=center,spectral_half_width=width,register_rest_source=rest,
                energy_deviation_bound=sigma,spectral_encoding_norm_bound=alpha,
                two_carrier_transport_norm_bound=transport,
                low_momentum_norm_sum=eta,recorder_cook_bound=cookx,reader_cook_bound=cooky,
                all_future_complete_record_error=uniform,
                all_future_expected_flag_pattern_deviation_bound=uniform**2,
                validated_success_probability_lower_bound=1-uniform**2 if schedule=="late" else 0,
                validated_success_probability_upper_bound=1 if schedule=="late" else uniform**2,
                reader_memory_disagreement_upper_bound=uniform**2 if schedule=="late" else 1,
                outgoing_record_error=outgoing,
                outside_joint_right_outgoing_sector_probability_bound=sector**2)


def gauge_covariance_checks():
    # A finite joint-energy degeneracy model checks the algebraic distinction:
    # conserved record effects can act nontrivially inside one energy fiber.
    energies=[1.,1.,2.,2.];theta=.73
    import cmath
    phase=[cmath.exp(-1j*e*theta) for e in energies]
    effect=[[0j]*4 for _ in range(4)]
    effect[0][0]=effect[1][1]=effect[0][1]=effect[1][0]=.5
    effect[3][3]=1
    for i in range(4):
        for j in range(4):
            transported=phase[i].conjugate()*effect[i][j]*phase[j]
            assert abs(transported-effect[i][j])<1e-14
    return 16


def run():
    return dict(status='passed',gate_channels=gate_checks(),
                gauge_covariance_entries=gauge_covariance_checks(),
                cases=[design(q,schedule) for schedule in ('late','early') for q in (100,1000,10000)],
                scope=['Both finite quadratic carriers and every gate enter the lapse constraint.',
                       'Reader validates F before copying M; early reader is a retained invalid outcome.',
                       'No sampling density or uniform prior over interrogation times.',
                       'Physical preparation is spectrally encoded; its Hamiltonian implementation remains open.',
                       'Uniform single late interrogation and conserved joint outgoing effects, not monitored arrival histories.',
                       'No localized inhomogeneous apparatus, reset engine or phenomenal constitution.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: two finite gravitating carriers, validated internal readout and complete record bounds')
    print(path)
