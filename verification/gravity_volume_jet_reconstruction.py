#!/usr/bin/env python3
"""Reconstruct, but do not physically implement, a Morse gravity volume frame.

Exact continuum bounds and the operational caveat are in the report. Checks
below use sampled floating-point modes and finite packets, not interval proofs.
"""
import cmath
import json
import math
from pathlib import Path

if __package__:
    from .gravitating_clock_probe import hyper, loggamma, scatter
    from .gravity_volume_clock_obstruction import simpson
else:
    from gravitating_clock_probe import hyper, loggamma, scatter
    from gravity_volume_clock_obstruction import simpson

KAPPAS=(.2,.6)
KMIN,KMAX=2.,8.


def potential_integral(volume,kappa):
    if volume<=0 or kappa<0: raise ValueError('invalid potential domain')
    c=2*kappa
    if volume<=c: return c*volume-volume**2/2
    return volume**2/2-c*volume+c**2


def rigorous_bounds(bmax):
    if bmax<0 or bmax>3: raise ValueError('supported analytic chart is 0 <= b <= 3')
    i=max(potential_integral(math.exp(bmax),kap) for kap in KAPPAS)
    # Gronwall and incoming normalization; these are squared-norm bounds.
    lo=math.exp(-2*i/KMIN)/(math.pi*KMAX)
    hi=math.exp(2*i/KMIN)/(math.pi*KMIN)
    return {'max_integrated_abs_potential':i,'lower_squared_norm':lo,
            'upper_squared_norm':hi,'certified_joint_success_probability':lo/hi}


def jet(k,kappa,b):
    """Value and x-derivative/k, including incoming phase and rigging factor."""
    if not KMIN<=k<=KMAX or not 0<=b<=1 or kappa not in KAPPAS:
        raise ValueError('outside declared spectral or chart domain')
    z=2*math.exp(b)
    value=derivative=0j
    for sign in (1,-1):
        s=sign*1j*k
        coeff=cmath.exp(loggamma(-2*s)-loggamma(.5-kappa-s))
        f,fp,_=hyper(.5+s-kappa,1+2*s,z)
        u=cmath.exp(s*math.log(z)-z/2)
        value+=coeff*u*f
        derivative+=coeff*u*((s-z/2)*f+z*fp)
    norm=math.exp(loggamma(.5-kappa-1j*k).real-loggamma(-2j*k).real)/math.sqrt(2*math.pi)
    loga=loggamma(-2j*k)-loggamma(.5-kappa-1j*k)+1j*k*math.log(2)
    phase=cmath.exp(1j*loga.imag)
    scale=norm/(math.sqrt(2*k)*phase)
    return (scale*value,scale*derivative/k)


def jet_norm2(j): return sum(abs(x)**2 for x in j)


def frame(k,kap,b):
    j=jet(k,kap,b)
    d=math.sqrt(jet_norm2(j))
    return tuple(x/d for x in j)


def inner(a,b): return sum(x.conjugate()*y for x,y in zip(a,b))


def directional(v):
    return ((v[0]-1j*v[1])/math.sqrt(2),(v[0]+1j*v[1])/math.sqrt(2))


def output(vectors,amplitudes):
    # Flatten n=0,1, with two coherent jet slots each.
    return tuple(amplitudes[n]*vectors[n][j] for n in range(2) for j in range(2))


def pullback(vectors,out):
    return tuple(sum(vectors[n][j].conjugate()*out[2*n+j] for j in range(2)) for n in range(2))


def phase_calibrated_overlap(k,b):
    """Remove input-convention phase before tracing spectral and jet slots."""
    fs=[]
    for kap in KAPPAS:
        f=frame(k,kap,b)
        phase=cmath.exp(1j*(loggamma(-2j*k)-loggamma(.5-kap-1j*k)+1j*k*math.log(2)).imag)
        fs.append(tuple(phase*x for x in f))
    return inner(fs[1],fs[0]).real


def run():
    bound=rigorous_bounds(1)
    b0=rigorous_bounds(0)
    all_turn_max=math.log(.6+math.sqrt(KMAX*KMAX+.6*.6))
    all_turn_bound=rigorous_bounds(all_turn_max)
    max_fd=max_inverse_error=max_transport_error=max_witness_error=0.
    sampled=[]
    for b in (0.,.5,1.):
        for i in range(61):
            k=KMIN+(KMAX-KMIN)*i/60
            for kap in KAPPAS:
                j=jet(k,kap,b)
                j2=jet_norm2(j)
                sampled.append(j2)
                assert bound['lower_squared_norm']<=j2<=bound['upper_squared_norm']
                # Unit change of slots to locally defined directional components.
                q=directional(j)
                assert abs(jet_norm2(q)-j2)<1e-10
                assert abs(abs(q[0])**2-abs(q[1])**2)<1e-10
                # A separate symmetric difference checks the analytic derivative.
                if 0<b<1:
                    h=1e-5
                    fd=(jet(k,kap,b+h)[0]-jet(k,kap,b-h)[0])/(2*h*k)
                    max_fd=max(max_fd,abs(fd-j[1]))
            v=[frame(k,kap,b) for kap in KAPPAS]
            s=[scatter(k,kap) for kap in KAPPAS]
            psi=tuple(x.conjugate()/math.sqrt(2) for x in s)
            out=output(v,psi)
            rec=pullback(v,out)
            max_inverse_error=max(max_inverse_error,max(abs(x-y) for x,y in zip(rec,psi)))
            # Root F+ and its isometrically represented effect produce the
            # same result; number record then +/- gives 4 branches of 1/4.
            for n in range(2):
                post=[0j,0j];post[n]=psi[n]
                outpost=output(v,post)
                postback=pullback(v,outpost)
                for sign in (1,-1):
                    eigen=(s[0].conjugate()/math.sqrt(2),sign*s[1].conjugate()/math.sqrt(2))
                    p=abs(inner(eigen,post))**2
                    pframe=abs(inner(eigen,postback))**2
                    max_witness_error=max(max_witness_error,abs(p-.25),abs(p-pframe))
            other=[frame(k,kap,1-b) for kap in KAPPAS]
            moved=output(other,pullback(v,out))
            target=output(other,psi)
            max_transport_error=max(max_transport_error,max(abs(x-y) for x,y in zip(moved,target)))
    assert max_fd<1e-8 and max_inverse_error<1e-12
    assert max_transport_error<1e-12 and max_witness_error<1e-12
    # Uniform-band states, with declared spectral/reference phase calibration.
    lo,hi=2.49,2.50
    overlap=simpson(lambda k:phase_calibrated_overlap(k,0),lo,hi,512)/(hi-lo)
    overlap_hi=simpson(lambda k:phase_calibrated_overlap(k,0),lo,hi,1024)/(hi-lo)
    assert abs(overlap-overlap_hi)<1e-9
    assert 0<overlap_hi<.9
    return {'status':'passed', 'scope':'Conditional mathematical jet reconstruction, not a physical volume-clock instrument or B7 pass.',
            'uniform_chart_bounds_b_0_to_1':bound, 'bounds_at_b_0':b0,
            'all_classical_turns_chart_b_max':all_turn_max,
            'all_classical_turns_analytic_bound':all_turn_bound,
            'sampling':{'count':len(sampled),'squared_norm_min':min(sampled),
                        'squared_norm_max':max(sampled)},
            'max_derivative_finite_difference_error':max_fd,
            'max_frame_inverse_error':max_inverse_error,
            'max_chart_transport_error':max_transport_error,
            'max_two_event_probability_error':max_witness_error,
            'phase_calibrated_uniform_packet_band':[lo,hi],
            'distinguishability_after_tracing_jet_and_k':abs(overlap_hi)}


def main():
    r=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__': main()
