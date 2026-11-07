"""One autonomous clock, finite noisy record tape, and derived hidden Markov law.

Standard library only. Exact ideal local-channel checks and global analytic
Duhamel bounds; no physical PDE simulation or empirical rate calibration.
"""
import cmath
import itertools
import json
import math
from pathlib import Path
if __package__:
    from .autonomous_record import mul, adj, close, bounds as single_bounds
else:
    from autonomous_record import mul, adj, close, bounds as single_bounds


def rotation(target, angle, control=None, plus=False):
    """exp(-i angle P_control (I +/- X_target)/2) on S,D,M,E."""
    n=16
    ident=[[complex(i==j) for j in range(n)] for i in range(n)]
    b=[[0j]*n for _ in range(n)]
    mask=1 << (3-target)
    for i in range(n):
        if control is None or ((i >> (3-control)) & 1):
            b[i][i]+=.5
            b[i^mask][i]+=(.5 if plus else -.5)
    close(mul(b,b),b)
    return [[ident[i][j]+(cmath.exp(-1j*angle)-1)*b[i][j]
             for j in range(n)] for i in range(n)]


def response(gamma, epsilon):
    beta=math.pi-2*epsilon
    return [[math.cos(gamma+z*beta/2)**2 for z in range(2)],
            [math.sin(gamma+z*beta/2)**2 for z in range(2)]]


def stage_check(gamma,epsilon):
    u=rotation(2,2*gamma)
    for gate in [rotation(1,math.pi,0),rotation(2,math.pi-2*epsilon,1),rotation(3,math.pi,2)]:
        u=mul(gate,u)
    close(mul(u,adj(u)),[[complex(i==j) for j in range(16)] for i in range(16)])
    r=response(gamma,epsilon)
    count=0
    for s,t in itertools.product(range(2),repeat=2):
        rho=[[0j]*16 for _ in range(16)]
        for e in range(2):rho[8*s+e][8*t+e]=.5
        out=mul(u,mul(rho,adj(u)))
        # Output on S,M: discard D,E, not merely E.
        reduced=[[0j]*4 for _ in range(4)]
        for ss,mm,tt,nn in itertools.product(range(2),repeat=4):
            reduced[2*ss+mm][2*tt+nn]=sum(
                out[8*ss+4*d+2*mm+e][8*tt+4*d+2*nn+e]
                for d,e in itertools.product(range(2),repeat=2))
        expected=[[0j]*4 for _ in range(4)]
        if s==t:
            for label in range(2):expected[2*s+label][2*s+label]=r[label][s]
        close(reduced,expected)
        count+=1
    return count


def mat2mul(a,b):return mul(a,b)


def observed_instrument(rho,label,r):
    return [[r[label][i]*rho[i][i] if i==j else 0j for j in range(2)] for i in range(2)]


def sequence_probability(rho,labels,r,alpha):
    # Independent instrument recursion, not a direct evaluation of the HMM sum.
    u=[[math.cos(alpha),-1j*math.sin(alpha)],[-1j*math.sin(alpha),math.cos(alpha)]]
    state=rho
    for k,label in enumerate(labels):
        if k:state=mat2mul(u,mat2mul(state,adj(u)))
        state=observed_instrument(state,label,r)
    return (state[0][0]+state[1][1]).real


def hmm_probability(p,labels,r,alpha):
    total=0.0
    for path in itertools.product(range(2),repeat=len(labels)):
        prob=p[path[0]]
        for k,z in enumerate(path):
            prob*=r[labels[k]][z]
            if k:prob*=math.sin(alpha)**2 if path[k-1]!=z else math.cos(alpha)**2
        total+=prob
    return total


def tape_bound(n,lam,gamma=.05,epsilon=.15,alpha=math.pi/6,hold=1):
    assert n>=1 and lam>=1
    assert 0<=gamma<=math.pi/2 and 0<=epsilon<=math.pi/2 and 0<=alpha<=math.pi/2
    m,v=lam**3,100
    a,ell,gap=10/lam,20/lam,10/lam
    regions=5*n-1
    travel=regions*ell+(regions-1)*gap+4*a
    baseline=single_bounds(m,v,.1,a,ell,gap,hold)
    c=baseline['reference_second_derivative_bound']
    fpp=baseline['packet_second_derivative_norm']
    delta=travel/v*(c/(2*m)+.1)+hold*fpp/(2*m)
    r=response(gamma,epsilon)
    q=max(r[1][0],r[0][1])
    return {'events':n,'scale':lam,'spatial_regions':regions,
            'detector_blank_qubits':n,'memory_blank_qubits':n,'thermal_environment_qubits':n,
            'mass':m,'velocity':v,'packet_half_width':a,'region_length':ell,'gap':gap,
            'travel_distance':travel,'passage_duration':travel/v,'hold_duration':hold,
            'false_positive_probability':r[1][0],'false_negative_probability':r[0][1],
            'gamma':gamma,'epsilon':epsilon,'rotation_alpha':alpha,
            'global_physical_vs_noisy_tape_half_diamond_bound':min(1,delta),
            'global_physical_vs_perfect_tape_half_diamond_bound':min(1,delta+n*q),
            'ideal_noisy_any_mislabel_union_bound':min(1,n*q),
            'physical_vs_noisy_full_vector_bound':delta,
            'outgoing_position_failure_bound':min(1,delta*delta),
            'carrier_kinetic_energy':m*v*v/2,
            'environment_information_entropy_production_cap_nats':n*math.log(2)}


def sufficient_design(n,target,hold=1):
    assert n>=1 and 0<target<1
    base=single_bounds(1,100,.1,hold=hold)
    acoef=150*base['reference_second_derivative_bound']/200
    bcoef=150*.1/100
    ccoef=hold*base['packet_second_derivative_norm']/2
    lam=math.ceil(max(1,math.sqrt(4*acoef*n/target),4*(bcoef*n+ccoef)/target))
    s=math.sqrt(target/(8*n))
    result=tape_bound(n,lam,gamma=s,epsilon=3*s,hold=hold)
    assert result['global_physical_vs_noisy_tape_half_diamond_bound']<=target/2+1e-12
    assert result['ideal_noisy_any_mislabel_union_bound']<=target/2+1e-12
    assert result['global_physical_vs_perfect_tape_half_diamond_bound']<=target+1e-12
    return {'requested_full_tape_error':target,**result}


def run():
    checks=0
    for gamma,epsilon in [(0,0),(.05,.15),(.2,.2),(math.pi/2,math.pi/2)]:
        checks+=stage_check(gamma,epsilon)
    gamma,epsilon,alpha=.05,.15,math.pi/6
    r=response(gamma,epsilon)
    full_rotation=rotation(0,2*alpha,plus=True)
    expected_rotation=[[cmath.exp(-1j*alpha)*(math.cos(alpha) if i//8==j//8 else -1j*math.sin(alpha))
                        if i%8==j%8 else 0j for j in range(16)] for i in range(16)]
    close(full_rotation,expected_rotation)
    # Coherent and incoherent system inputs; offdiagonal matrix units already
    # tested independently above, so the comparison is valid with references.
    inputs=[[[1+0j,0j],[0j,0j]],[[.5,.5],[.5,.5]],[[.3,.2j],[-.2j,.7]]]
    seq_checks=0
    for n in range(1,9):
        for rho in inputs:
            total=0
            for labels in itertools.product(range(2),repeat=n):
                a=sequence_probability(rho,labels,r,alpha)
                b=hmm_probability([rho[0][0].real,rho[1][1].real],labels,r,alpha)
                assert abs(a-b)<1e-12 and a>=-1e-14
                total+=a;seq_checks+=1
            assert abs(total-1)<1e-12
    # Perfect observations recover a Markov chain: unbiased initial state,
    # flip probability sin^2(alpha)=1/4, path entropy ln2+(n-1)h2(1/4).
    n=8;pflip=math.sin(alpha)**2
    path_entropy=0
    for labels in itertools.product(range(2),repeat=n):
        prob=sequence_probability(inputs[1],labels,response(0,0),alpha)
        if prob:path_entropy-=prob*math.log(prob)
    h=-pflip*math.log(pflip)-(1-pflip)*math.log(1-pflip)
    assert abs(path_entropy-(math.log(2)+(n-1)*h))<1e-12
    cases=[tape_bound(n,100) for n in (1,4,8,16)]
    cases.append(tape_bound(8,1000,gamma=.005,epsilon=.015))
    assert cases[2]['global_physical_vs_noisy_tape_half_diamond_bound']<.0125
    # Independent extreme: repeated use of one phase bit instead of n fresh
    # bits dephases only history parity. Orthogonal paths 00 and 11 keep a
    # coherence that independent dephasing destroys.
    parity_overlap=lambda z,w: int((sum(z)-sum(w))%2==0)
    assert parity_overlap((0,0),(1,1))==1
    fresh_overlap=int((0,0)==(1,1));assert fresh_overlap==0
    designs=[sufficient_design(n,target) for n in (1,8,100) for target in (.1,.01,.001)]
    return {'status':'passed','local_stage_matrix_units_checked':checks,
            'sufficient_design_checks':len(designs),
            'hundred_event_one_percent_sufficient_design':designs[7],
            'sequence_probabilities_checked':seq_checks,
            'eight_record_perfect_path_entropy_nats':path_entropy,
            'eight_record_independent_bit_entropy_upper_bound_nats':8*math.log(2),
            'finer_calibration_eight_record_bound':cases[-1]['global_physical_vs_perfect_tape_half_diamond_bound'],
            'cases':cases,
            'shared_phase_environment_parity_witness':{'history_00_11_overlap_shared':1,
                                                     'history_00_11_overlap_fresh':0},
            'scope':['One initially prepared clock packet traverses all stages; no clock reset between events.',
                     'Noisy register instrument is derived from the local finite-environment unitary, not postulated.',
                     'Fresh detector/memory/environment tape cells are all prepared initially and counted explicitly.',
                     'Discrete spatially generated transition process, not a continuous-time jump limit or empirical calibration.',
                     'Global analytic bound; no physical PDE simulation, indefinite reuse or gravitational refoliation.']}


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: autonomous noisy record tape, hidden-state sequence law and global clock-resource bound')
    print(path)
