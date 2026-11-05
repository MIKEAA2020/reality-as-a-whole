"""Finite excited source -> finite programmed clock, inside gravity.

Exact clock diagonalization and finite gate checks; analytic continuum/domain
and finite-window bounds are in FINITE_SOURCE_CLOCK.md. No large matrix stored.
"""
import cmath
import json
import math
from pathlib import Path
if __package__:
    from .internal_reference_event import permutation, bits, index
else:
    from internal_reference_event import permutation, bits, index


def program():
    return [list(range(256)),permutation([0],1),permutation([1],2),
            permutation([2],3),permutation([],4),permutation([4],6),
            permutation([6,2],5),permutation([],7)]


def histories():
    result=[list(range(256))]
    for gate in program():result.append([gate[i] for i in result[-1]])
    return result


def channel_checks():
    w=histories();length=len(program());checks=0
    for n in range(length+1):
        for r in range(2):
            for q in range(2):
                reduced={}
                for e in range(2):
                    a=bits(w[n][index([r,0,0,e,0,0,0,0])])
                    b=bits(w[n][index([q,0,0,e,0,0,0,0])])
                    assert a[7]==(n==length) and b[7]==(n==length)
                    if a[3]==b[3]:
                        key=tuple(a[:3]+a[4:]),tuple(b[:3]+b[4:])
                        reduced[key]=reduced.get(key,0)+.5
                if n==length:
                    expected={}
                    if r==q:
                        k=tuple([r,r,r,1,r,1,1]);expected[k,k]=1.
                    assert reduced==expected
                if n<=1:
                    assert bits(w[n][index([r,0,0,0,0,0,0,0])])[0]==r
                checks+=1
    # Gauge conjugation on every programmed edge/register basis state.
    conjugations=0
    for n,g in enumerate(program()):
        for i in range(256):
            assert g[w[n][i]]==w[n+1][i]
            conjugations+=1
    return dict(history_matrix_units=checks,completed_channel_matrix_units=4,
                exact_programmed_edge_gauge_checks=conjugations,
                program_bonds=length,identity_emission_bonds=1)


def finite_amplitudes(nsites,tau,positions):
    # gamma*t=tau; omit the common exp(-i Ec t).
    out=[0j]*len(positions)
    denom=nsites+1
    for j in range(1,nsites+1):
        theta=math.pi*j/denom
        phase=cmath.exp(-2j*tau*math.cos(theta))
        pref=2/denom*math.sin(theta)*phase
        for k,n in enumerate(positions):out[k]+=pref*math.sin((n+1)*theta)
    return out


def exact_small_chain_checks():
    count=0
    for nsites in (10,17):
        for tau in (0.,.1,1.,5.):
            a=finite_amplitudes(nsites,tau,range(nsites))
            assert abs(sum(abs(v)**2 for v in a)-1)<1e-12
            # Initial source state, not a preloaded carrier packet.
            if tau==0:
                assert abs(a[0]-1)<1e-13 and max(abs(v) for v in a[1:])<1e-13
            # Exact dynamics imply conserved mean hopping energy zero.
            hopping=2*sum((a[n].conjugate()*a[n+1]).real for n in range(nsites-1))
            assert abs(hopping)<1e-12
            count+=1
    return count


def design(tau_min,nsites):
    gamma=1/64;wg=1.;plo=.05;phi=.25
    nuhi=math.sqrt(.25-8*plo*plo/3);nulo=math.sqrt(.25-8*phi*phi/3)
    ec=wg*(1+(nuhi+nulo)/2);width=wg*(nuhi-nulo)/2
    assert ec>2*gamma and 2*gamma<width
    length=len(program());sum_squares=length*(length+1)*(2*length+1)/6
    tau_max=2*tau_min;z=2*tau_max;k=nsites
    assert k>z
    log_boundary=math.log(2)+k*(1+math.log(z/k))
    boundary_cap=1e-12
    assert log_boundary<math.log(boundary_cap)
    failure=(math.sqrt(sum_squares)/tau_min+boundary_cap)**2
    source=(1/tau_min+boundary_cap)**2
    samples=[]
    for fraction in (1.,1.5,2.):
        tau=tau_min*fraction
        a=finite_amplitudes(nsites,tau,range(length))
        pending=sum(abs(v)**2 for v in a)
        psource=abs(a[0])**2
        assert pending<=failure+1e-11 and psource<=source+1e-11
        samples.append(dict(scaled_epoch=tau,source_excitation_probability=psource,
                            incomplete_program_probability=pending,
                            emitted_excitation_probability=1-psource,
                            source_energy_depletion=ec*(1-psource)))
    # Every exact finite clock energy fits in the gravitational window.
    jac=0
    for j in (1,nsites//4,nsites//2,3*nsites//4,nsites):
        theta=math.pi*j/(nsites+1);offset=2*gamma*math.cos(theta)
        nu=(ec+offset)/wg-1;p=math.sqrt(3/8*(.25-nu*nu))
        assert plo<p<phi
        slope=8*wg*p/(3*nu)
        assert slope>0
        h=1e-7
        derivative=wg*(math.sqrt(.25-8*(p+h)**2/3)-math.sqrt(.25-8*(p-h)**2/3))/(2*h)
        assert abs(derivative+slope)<1e-7
        f=(.3+.4j)*math.sqrt(slope)
        assert abs(abs(f)**2/slope-.25)<1e-14
        assert abs(wg*(1+math.sqrt(.25-8*p*p/3))-(ec+offset))<1e-14
        jac+=1
    omega=1e-12
    perturb=omega*tau_max/gamma
    assert 2*gamma+omega<width and ec-2*gamma-omega>0
    return dict(clock_positions_including_source=nsites,physical_clock_sites=nsites-1,
                program_length=length,gravitational_radial_level=0,
                gravitational_frequency=wg,cosmological_constant=-4/3,
                scalar_positive_band=[plo,phi],source_excitation_energy=ec,
                clock_hopping=gamma,total_source_energy_lower_bound=ec-2*gamma,
                total_source_energy_upper_bound=ec+2*gamma,
                gravitational_half_window=width,spectral_margin=width-2*gamma,
                degenerate_model_initial_total_energy_variance=gamma*gamma,
                source_only_initial_state=True,minimum_readout_epoch=tau_min/gamma,
                maximum_readout_epoch=tau_max/gamma,scaled_minimum_epoch=tau_min,
                finite_boundary_log_norm_bound=log_boundary,
                certified_positive_boundary_norm_cap=boundary_cap,
                uniform_window_source_not_depleted_probability_bound=source,
                uniform_window_incomplete_program_probability_bound=failure,
                uniform_window_complete_instrument_half_diamond_bound=failure,
                degenerate_model_completed_conditional_record_error=0,
                noncommuting_system_frequency=omega,
                noncommuting_model_uniform_vector_comparison_bound=perturb,
                noncommuting_model_uniform_complete_instrument_error_bound=failure+perturb,
                noncommuting_model_uniform_incomplete_probability_bound=(math.sqrt(failure)+perturb)**2,
                noncommuting_model_uniform_source_pending_probability_bound=(math.sqrt(source)+perturb)**2,
                spectral_inverse_checks=jac,samples=samples)


def recurrence_witness():
    # Three-position source/clock chain energies Ec, Ec +/- sqrt(2) gamma.
    # At tau=2pi/sqrt(2) it returns exactly (apart from a common phase).
    tau=2*math.pi/math.sqrt(2)
    state=finite_amplitudes(3,tau,range(3))
    assert abs(abs(state[0])**2-1)<1e-12
    return dict(clock_positions=3,scaled_recurrence_epoch=tau,
                returned_source_probability=abs(state[0])**2)


def run():
    return dict(status='passed',gate_and_gauge_checks=channel_checks(),
                finite_chain_unitarity_energy_checks=exact_small_chain_checks(),
                cases=[design(tau,n) for tau,n in ((128,4096),(512,16384),(2048,65536))],
                recurrence_witness=recurrence_witness(),
                scope=['Finite two-level excited source, finite lattice clock and finite register.',
                       'Different apparatus model: exact degenerate program plus controlled noncommuting-system perturbation, not the prior two-carrier packet Hamiltonian.',
                       'Entire finite spectrum lies in gravitational window; no polar or incoming packet encoding.',
                       'Autonomous source emission and gate execution; all incomplete/source-pending outcomes retained.',
                       'Finite readout window only: closed finite clock recurs, not a permanent latch.',
                       'Initial physical source state and final extraction/reset are not derived from nothing.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: finite source emission, finite clock program, gravity fit and complete finite-window instrument')
    print(path)
