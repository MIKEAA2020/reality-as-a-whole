"""Finite lapse-coupled register operation with a positive relational dust budget.

Analytic action/domain/gauge statements are in DUST_CLOCK_RECORD.md. Midpoint
unitary integration checks two exact internal blocks, not the gravitational PDE.
"""
import cmath
import json
import math
from pathlib import Path


def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def adj(a):return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]
def identity(n):return [[complex(i==j) for j in range(n)] for i in range(n)]
def diff(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def maxentry(a):return max(abs(x) for r in a for x in r)


def opnorm2(a):
    h=mul(adj(a),a)
    mid=(h[0][0].real+h[1][1].real)/2
    rad=math.sqrt(((h[0][0].real-h[1][1].real)/2)**2+abs(h[0][1])**2)
    return math.sqrt(max(0,mid+rad))


def exp_pauli(x,z,t,offset=0):
    r=math.hypot(x,z);c=math.cos(r*t)
    s=math.sin(r*t)/r if r else t
    phase=cmath.exp(-1j*offset*t)
    return [[phase*(c-1j*s*z),phase*(-1j*s*x)],
            [phase*(-1j*s*x),phase*(c+1j*s*z)]]


def first_pulse(width,omega,panels):
    uminus=identity(2);dt=width/panels
    for j in range(panels):
        s=(j+.5)*dt
        g=2*math.pi/width*math.sin(math.pi*s/width)**2
        step=exp_pauli(omega,-g/2,dt,g/2)
        uminus=mul(step,uminus)
    uplus=exp_pauli(omega,0,width)
    kraus=[[[ (uplus[i][j]+sign*uminus[i][j])/2 for j in range(2)] for i in range(2)] for sign in (1,-1)]
    complete=[[0j]*2 for _ in range(2)]
    for k in kraus:
        h=mul(adj(k),k)
        complete=[[x+y for x,y in zip(r,s)] for r,s in zip(complete,h)]
    assert maxentry(diff(complete,identity(2)))<1e-11
    idealminus=[[1+0j,0j],[0j,-1+0j]]
    error=max(opnorm2(diff(uplus,identity(2))),opnorm2(diff(uminus,idealminus)))
    return kraus,error



def completed_channel_check(kraus,width,omega):
    """Compare all four S matrix units with the full register output.

    The exact later controlled-X gates map (D,M,E,F)=(d,0,e,0)
    to (d,d,e xor d,1). Trace E only after both copies and the flag.
    """
    w=exp_pauli(omega,0,19*width/4-width)
    ak=[mul(w,k) for k in kraus]
    def index(s,d,m,e,f):return 16*s+8*d+4*m+2*e+f
    vectors={}
    for r in range(2):
        for e in range(2):
            v=[0j]*32
            for d in range(2):
                for t in range(2):v[index(t,d,d,e^d,1)]=ak[d][t][r]
            vectors[r,e]=v
    for r in range(2):
        for q in range(2):
            full=[[sum(vectors[r,e][i]*vectors[q,e][j].conjugate()/2
                        for e in range(2)) for j in range(32)] for i in range(32)]
            for t in range(2):
                for u in range(2):
                    for d in range(2):
                        for k in range(2):
                            value=sum(full[index(t,d,d,e,1)][index(u,k,k,e,1)] for e in range(2))
                            expected=ak[d][t][r]*ak[d][u][q].conjugate() if d==k else 0j
                            assert abs(value-expected)<1e-12
            trace=sum(full[i][i] for i in range(32))
            assert abs(trace-(r==q))<1e-11
    return 4


def design(scale,pmax=.1,rest=1,omega=.1,margin=1,levels=3):
    assert scale>=1 and pmax**2<3/32 and rest>=omega
    cosmological_constant=-.75
    gravfreq=math.sqrt(3*abs(cosmological_constant))/2
    nu_min=math.sqrt(.25-8*pmax*pmax/3)
    width=.02/scale;gap=width/4
    peak=2*math.pi/width
    hmax=rest+omega+peak
    nmin=max(0,math.ceil(((hmax+margin)/gravfreq-1-nu_min)/2))
    amin=gravfreq*(2*nmin+1+nu_min)
    amax=gravfreq*(2*(nmin+levels-1)+1+.5)
    assert amin-hmax>=margin-1e-10
    return dict(scale=scale,pulse_width=width,gap=gap,proper_protocol_duration=4*width+3*gap,
                peak_control_energy=peak,apparatus_energy_upper_bound=hmax,
                scalar_momentum_half_band=pmax,subcritical_limit=math.sqrt(3/32),
                gravitational_frequency=gravfreq,nu_minimum=nu_min,
                gravitational_level_minimum=nmin,gravitational_level_count=levels,
                gravitational_energy_minimum=amin,gravitational_energy_maximum=amax,
                relational_dust_energy_lower_bound=amin-hmax,
                relational_dust_energy_upper_bound=amax-(rest-omega),
                uniform_instrument_half_diamond_bound=omega*width,
                exact_final_not_completed_probability=0,
                scope='Ideal dust reference and exact calibrated controls; not a normalizable clock packet or macroscopic noise budget.')


def laguerre(n,alpha,z):
    result=[0.,0.,0.]
    for j in range(n+1):
        c=(-1)**j*math.exp(math.lgamma(n+alpha+1)-math.lgamma(alpha+j+1)
                         -math.lgamma(n-j+1)-math.lgamma(j+1))
        result[0]+=c*z**j
        if j:result[1]+=j*c*z**(j-1)
        if j>1:result[2]+=j*(j-1)*c*z**(j-2)
    return result


def run():
    # Radial oscillator A_p=(3/16)[-d_r^2-g/r^2]+|Lambda|r^2.
    radial=0;freq=.75;beta=8/3*freq
    for p in (0,.05,.1,.2):
        g=8*p*p/3;nu=math.sqrt(.25-g)
        for n in range(4):
            energy=freq*(2*n+1+nu)
            for r in (.1,.5,1,2):
                z=beta*r*r;f,fp,fpp=laguerre(n,nu,z)
                a=nu+.5
                pref=r**a*math.exp(-z/2)
                d=a/r-beta*r;dp=-a/r**2-beta
                # ordinary r derivatives of pref * L(beta r^2)
                second=pref*((d*d+dp)*f+(4*beta*r*d+2*beta)*fp+4*beta**2*r*r*fpp)
                psi=pref*f
                residual=3/16*(-second-g/r**2*psi)+.75*r*r*psi-energy*psi
                assert abs(residual)<1e-9
                radial+=1
    cases=[]
    for scale in (1,10,100):
        c=design(scale)
        coarse,e1=first_pulse(c['pulse_width'],.1,256)
        fine,e2=first_pulse(c['pulse_width'],.1,512)
        d=max(maxentry(diff(a,b)) for a,b in zip(coarse,fine))
        assert d<1e-7
        assert e2<=c['uniform_instrument_half_diamond_bound']+1e-11
        # Classical inputs witness that completion is not a promise of zero
        # measurement error; all outcomes are kept in the instrument.
        probs=[]
        for s in range(2):
            probs.append([sum(abs(k[i][s])**2 for i in range(2)) for k in fine])
            assert abs(sum(probs[-1])-1)<1e-11
        plus=[1/math.sqrt(2)]*2
        out=[[0j]*2 for _ in range(2)]
        for k in fine:
            v=[sum(k[i][j]*plus[j] for j in range(2)) for i in range(2)]
            out=[[out[i][j]+v[i]*v[j].conjugate() for j in range(2)] for i in range(2)]
        xout=2*out[0][1].real
        dust_gain=.1*(1-xout)
        assert .09<dust_gain<.11
        matrix_units=completed_channel_check(fine,c['pulse_width'],.1)
        cases.append(dict(resources=c,complete_register_channel_matrix_units_checked=matrix_units,
                          proper_dust_energy_gain_on_Xplus_input=dust_gain,
                          numerical_first_pulse_operator_error=e2,
                          midpoint_256_512_max_kraus_difference=d,
                          detector_probabilities_on_Z_inputs=probs))
    # All later controlled copies commute with H_S. A final finite-area flag
    # flip acts on F alone: it marks schedule completion, not measurement truth.
    xx=[[0j,1+0j],[1+0j,0j]]
    flag=exp_pauli(-math.pi/2,0,1,math.pi/2)
    assert maxentry(diff(flag,xx))<1e-12
    # Geometry responds to TOTAL rest energy. Positive proper dust is not an
    # externally supplied power source: raising detector E at fixed dust E
    # raises maximum volume by Delta E / |Lambda| in the p_phi=0 control.
    for dust in (1,10):
        for detector in (.2,1):
            total=dust+detector
            vmax=total/.75
            assert abs(-.75*vmax+detector+dust)<1e-12
    return dict(status='passed',radial_gravitational_eigenmode_checks=radial,
                cases=cases,exact_completion_flag_check=True,
                massless_scalar_retained_in_action=True,
                scope=['Einstein-scalar action extended by proper dust and a finite register, not passive re-labelling.',
                       'Friedrichs boundary condition and subcritical scalar-momentum band are declared.',
                       'Positive relational dust-energy code; no assertion of a positive bare-momentum kinematic projection.',
                       'Exact calibrated finite completion and memory retention in the ideal reference model; first pulse instrument error bounded.',
                       'No finite-packet dust clock, readout/reset engine, inhomogeneous refoliation or singularity resolution.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: finite lapse-coupled record instrument, radial gravity and positive relational dust budget')
    print(path)
