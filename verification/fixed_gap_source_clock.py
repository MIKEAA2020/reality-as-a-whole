"""Finite reservoir lifts a noncommuting measurement into an energy symmetry.

Same finite source/clock amplitudes as finite_source_clock.py, but a NEW
energy-conserving program and explicitly recomputed gravitational spectrum.
No tiny-omega perturbation budget is reused. See FIXED_GAP_SOURCE_CLOCK.md.
"""
import cmath
import json
import math
from pathlib import Path
if __package__:
    from .finite_source_clock import design as clock_design, program, bits, index
else:
    from finite_source_clock import design as clock_design, program, bits, index


def swap(e,n,top):
    if e==0 and n>0:return 1,n-1
    if e==1 and n<top:return 0,n+1
    return e,n


def amplitudes(e,b,d):
    top=len(b)-1;out=[[0j]*(top+1) for _ in range(2)]
    sign=1 if d==0 else -1
    for n,a in enumerate(b):
        out[e][n]+=a/2
        f,m=swap(e,n,top);out[f][m]+=sign*a/2
    return out


def reduced(v,w):
    return [[sum(v[e][n]*w[f][n].conjugate() for n in range(len(v[e])))
             for f in range(2)] for e in range(2)]


def mx(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(*args):return [[sum(a[i][j] for a in args) for j in range(2)] for i in range(2)]
def scale(a,c):return [[c*x for x in row] for row in a]


def reference_checks(top,omega=.1):
    b=[math.sqrt(2/top)*math.sin(math.pi*n/top) if 0<n<top else 0. for n in range(top+1)]
    assert abs(sum(x*x for x in b)-1)<1e-13
    c=sum(b[n]*b[n+1] for n in range(top))
    r=sum(b[n]*b[n+2] for n in range(top-1))
    assert abs(c-math.cos(math.pi/top))<1e-13
    expected_r=math.cos(2*math.pi/top)+2/top*math.sin(math.pi/top)**2
    assert abs(r-expected_r)<1e-13
    swaps=0
    for e in range(2):
        for n in range(top+1):
            f,m=swap(e,n,top)
            assert swap(f,m,top)==(e,n)
            assert e+n==f+m  # exact total energy charge, including boundaries
            swaps+=1
    vs={(d,e):amplitudes(e,b,d) for d in range(2) for e in range(2)}
    x=[[0j,1+0j],[1+0j,0j]];checked=0
    for e in range(2):
        for f in range(2):
            rho=[[complex(i==e and j==f) for j in range(2)] for i in range(2)]
            dr=[[rho[i][j]*(r if i!=j else 1) for j in range(2)] for i in range(2)]
            trace=0j
            for d in range(2):
                actual=reduced(vs[d,e],vs[d,f])
                expected=scale(add(rho,mx(mx(x,dr),x),
                             scale(add(mx(x,rho),mx(rho,x)),(1 if d==0 else -1)*c)),.25)
                assert max(abs(actual[i][j]-expected[i][j]) for i in range(2) for j in range(2))<1e-13
                trace+=actual[0][0]+actual[1][1]
                checked+=1
            assert abs(trace-(e==f))<1e-13
    wrong=[]
    for bit in range(2):
        sign=1 if bit==0 else -1
        d=1-bit
        v=[[ (vs[d,0][e][n]+sign*vs[d,1][e][n])/math.sqrt(2)
             for n in range(top+1)] for e in range(2)]
        p=sum(abs(z)**2 for row in v for z in row)
        assert abs(p-(1-c)/2)<1e-13
        wrong.append(p)
    energy=[]
    for e in range(2):
        es=eb=0.;fid=0.
        for d in range(2):
            v=vs[d,e]
            for f in range(2):
                for n in range(top+1):
                    p=abs(v[f][n])**2
                    es+=(2*f-1)*omega*p;eb+=2*omega*n*p
                fid+=abs(sum(b[n]*v[f][n] for n in range(top+1)))**2
        initial_s=(2*e-1)*omega;initial_b=omega*top
        assert abs(es)<1e-13
        assert abs(eb-initial_b-initial_s)<1e-11
        assert abs((es+eb)-(initial_s+initial_b))<1e-11
        assert abs(fid-(1+c*c)/2)<1e-13
        energy.append(dict(input_energy_level=e,system_energy_change=es-initial_s,
                           reservoir_energy_change=eb-initial_b,reference_fidelity_after_use=fid))
    covariance=0
    for t in (.7,100.,262144.):
        for e in range(2):
            before=[b[n]*cmath.exp(-1j*2*omega*n*t)*cmath.exp(-1j*(2*e-1)*omega*t)
                    for n in range(top+1)]
            for d in range(2):
                actual=amplitudes(e,before,d)
                for f in range(2):
                    for n in range(top+1):
                        expected=vs[d,e][f][n]*cmath.exp(-1j*((2*f-1)*omega+2*omega*n)*t)
                        assert abs(actual[f][n]-expected)<1e-8
                covariance+=1
    eps=(1-r)/4+(1-c)/2
    joint=math.sqrt(1-c)
    var_b=sum((2*omega*n-omega*top)**2*b[n]**2 for n in range(top+1))
    return dict(ladder_maximum_level=top,ladder_dimension=top+1,
                reservoir_mean_initial_energy=omega*top,reservoir_maximum_energy=2*omega*top,
                reservoir_initial_energy_variance=var_b,adjacent_shift_overlap=c,
                opposite_shift_overlap=r,full_output_isometry_error_bound=joint,
                reduced_complete_instrument_half_diamond_bound=eps,
                eigeninput_wrong_record_probability=(1-c)/2,
                energy_charge_involution_checks=swaps,instrument_matrix_unit_outcome_checks=checked,
                free_evolution_covariance_checks=covariance,wrong_record_probabilities=wrong,
                energy_exchange_witnesses=energy)


def design(top,tau,nsites):
    ref=reference_checks(top)
    # Reuse clock dynamics ONLY, which are exactly unchanged by commuting H_f.
    old=clock_design(tau,nsites)
    gamma=old['clock_hopping'];omega=.1;wg=1024.;largest_ladder=512
    plo=.05;phi=.25
    nu_hi=math.sqrt(.25-8*plo*plo/3);nu_lo=math.sqrt(.25-8*phi*phi/3)
    center=wg*(1+(nu_hi+nu_lo)/2);width=wg*(nu_hi-nu_lo)/2
    source=center-omega*largest_ladder  # one fixed source across all three devices
    low=source-2*gamma-omega
    high=source+2*gamma+2*omega*top+omega
    assert 0<low and center-width<low<high<center+width
    inverses=0
    for j in (1,nsites//2,nsites):
        hopping=2*gamma*math.cos(math.pi*j/(nsites+1))
        for q in (0,1,top//2,top,top+1):
            energy=source+hopping-omega+2*omega*q
            nu=energy/wg-1;p=math.sqrt(3/8*(.25-nu*nu))
            assert plo<p<phi
            assert abs(wg*(1+math.sqrt(.25-8*p*p/3))-energy)<1e-9
            jac=8*wg*p/(3*nu)
            h=1e-7
            fd=wg*(math.sqrt(.25-8*(p+h)**2/3)-math.sqrt(.25-8*(p-h)**2/3))/(2*h)
            assert abs((fd+jac)/jac)<1e-7
            inverses+=1
    pending=old['uniform_window_incomplete_program_probability_bound']
    eps=ref['reduced_complete_instrument_half_diamond_bound']
    complete=min(1,pending+(1-pending)*eps)
    return dict(reference=ref,clock_positions=nsites,program_length=8,
                physical_root_dimension=nsites*256*(top+1),
                fixed_system_frequency=omega,fixed_system_energy_gap=2*omega,
                fixed_clock_hopping=gamma,fixed_source_excitation_energy=source,
                gravitational_frequency=wg,cosmological_constant=-4*wg*wg/3,
                scalar_positive_band=[plo,phi],gravitational_radial_level=0,
                total_matter_energy_lower_bound=low,total_matter_energy_upper_bound=high,
                gravitational_center=center,gravitational_half_width=width,
                gravitational_spectral_margin=min(low-(center-width),center+width-high),
                mean_total_initial_energy_for_zero_system_mean=source+omega*top,
                initial_clock_hopping_energy_std=gamma,
                initial_total_energy_variance_upper_bound=gamma*gamma+omega*omega+ref['reservoir_initial_energy_variance'],
                readout_window=[old['minimum_readout_epoch'],old['maximum_readout_epoch']],
                source_pending_probability_bound=old['uniform_window_source_not_depleted_probability_bound'],
                clock_incomplete_probability_bound=pending,
                complete_record_half_diamond_bound=complete,
                conditional_complete_record_half_diamond_bound=eps,
                gravitational_spectrum_inverse_checks=inverses,
                no_omega_times_duration_term=True)



def later_record_transport_checks():
    # Arbitrary D matrix units, with S/B as untouched spectators. The actual
    # first gate may entangle D with S/B; this proves its exact postprocessing.
    gates=program()[2:]
    count=0
    for d in range(2):
        for k in range(2):
            reduced={}
            for e in range(2):
                pair=[]
                for z in (d,k):
                    j=index([0,z,0,e,0,0,0,0])
                    for gate in gates:j=gate[j]
                    pair.append(bits(j))
                a,b=pair
                if a[3]==b[3]:
                    key=tuple(a[:3]+a[4:]),tuple(b[:3]+b[4:])
                    reduced[key]=reduced.get(key,0)+.5
            expected={}
            if d==k:
                x=tuple([0,d,d,1,d,1,1]);expected[x,x]=1.
            assert reduced==expected
            count+=1
    return count


def run():
    return dict(status='passed',later_detector_transport_matrix_units=later_record_transport_checks(),
                cases=[design(n,t,k) for n,t,k in ((32,128,4096),(128,512,16384),(512,2048,65536))],
                scope=['Fixed H_S=0.1 X_S is retained at every clock site.',
                       'Finite reservoir energy and coherence are counted; every programmed gate conserves H_S+H_B.',
                       'Uniform-in-duration reference error, but finite-clock completion window and recurrences remain.',
                       'Target is initial S Z relative to the finite reservoir phase, with exact subsequent free S rotation.',
                       'Reduced instrument and full reservoir-output errors are different; no free repeated reservoir reuse.',
                       'Reservoir/source initial preparation, extraction/reset, local gravity and phenomenal constitution remain open.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: fixed noncommuting system gap, finite energy reservoir, exact source clock and gravity accounting')
    print(path)
