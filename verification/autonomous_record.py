"""Autonomous spatial registration: exact reference gates and finite-time bounds.

No physical Schrödinger PDE simulation is claimed. Analytic Duhamel estimates
bound the actual quadratic-kinetic Hamiltonian; finite matrix checks independently
verify the ideal detector/memory/environment channel, including entangled inputs.
"""
import cmath
import itertools
import json
import math
from pathlib import Path

N = 16  # S,D,M,E


def bits(n):
    return [(n >> k) & 1 for k in (3, 2, 1, 0)]


def index(b):
    return sum(x << k for x, k in zip(b, (3, 2, 1, 0)))


def gate(control, target):
    u = [[0j] * N for _ in range(N)]
    for i in range(N):
        b = bits(i)
        b[target] ^= b[control]
        u[index(b)][i] = 1
    return u


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return [list(row) for row in zip(*[[x.conjugate() for x in row] for row in a])]


def close(a, b, tol=1e-12):
    assert len(a) == len(b)
    assert max(abs(x-y) for r,s in zip(a,b) for x,y in zip(r,s)) < tol


def bounds(m, v, omega, a=10, ell=20, gap=10, hold=1):
    assert min(m, v, a, ell) > 0 and min(omega, gap, hold) >= 0
    fp = math.pi / (math.sqrt(3) * a)
    fpp = math.pi**2 / (math.sqrt(3) * a*a)
    kmax = 2*math.pi/ell
    kpmax = 2*math.pi**2/(ell*ell)
    c = fpp + 2*kmax*fp + kpmax + kmax*kmax
    travel = 3*ell + 2*gap + 4*a
    passage = travel/v
    write = passage*(c/(2*m)+omega)
    total = write + hold*fpp/(2*m)
    return {'mass':m, 'velocity':v, 'mean_momentum':m*v,
            'system_energy_half_gap':omega, 'packet_half_width':a,
            'region_length':ell, 'gap':gap, 'hold_duration':hold,
            'travel_distance':travel,'passage_duration':passage,
            'packet_first_derivative_norm':fp,'packet_second_derivative_norm':fpp,
            'potential_over_velocity_norm_bound':kmax,
            'potential_derivative_over_velocity_norm_bound':kpmax,
            'reference_second_derivative_bound':c,
            'write_vector_error_bound':write,'hold_vector_error_bound':total,
            'full_record_half_diamond_bound':min(1,total),
            'entropy_production_deviation_bound_nats':
                (-total*math.log(total)-(1-total)*math.log(1-total)+total*math.log(5))
                if 0<total<=.5 else None,
            'record_disagreement_probability_bound':min(1,total*total),
            'missed_outgoing_position_probability_bound':min(1,total*total),
            'conditional_outgoing_state_error_bound':min(1,2*total),
            'carrier_kinetic_energy':m*v*v/2,
            'mean_clock_kinetic_energy':m*v*v/2+fp*fp/(2*m),
            'peak_spatial_coupling':v*kmax}


def run():
    ident = [[complex(i == j) for j in range(N)] for i in range(N)]
    gates = [gate(0,1),gate(1,2),gate(2,3)]
    for u in gates:
        close(mul(u,adj(u)),ident)
        # B=(I-CNOT)/2 is exactly the positive controlled projector.
        b = [[(ident[i][j]-u[i][j])/2 for j in range(N)] for i in range(N)]
        close(mul(b,b),b)
        close(adj(b),b)
        # exp(-i*pi*B) = I+(exp(-i*pi)-1)B = CNOT.
        close([[ident[i][j]+(cmath.exp(-1j*math.pi)-1)*b[i][j]
                for j in range(N)] for i in range(N)],u)
    assert any(abs(x-y) > 1e-12 for r,s in zip(mul(gates[0],gates[1]),mul(gates[1],gates[0])) for x,y in zip(r,s))
    # Conservation of X_E makes the actual spatial Hamiltonian block diagonal
    # in the environment's X basis, not just its ideal gate product.
    xe = [[0j]*N for _ in range(N)]
    for i in range(N):
        b=bits(i);b[3]^=1;xe[index(b)][i]=1
    for gate_u in gates:close(mul(gate_u,xe),mul(xe,gate_u))
    u = mul(gates[2],mul(gates[1],gates[0]))
    # Derive reduced SDM channel on every system matrix unit |s><t|.
    # Environment is maximally mixed, thermal for H_E=0. The off-diagonal
    # matrix units test coherences; linearity then includes any reference.
    checked = 0
    for s,t in itertools.product(range(2),repeat=2):
        full = [[0j]*N for _ in range(N)]
        for e in range(2):
            full[index([s,0,0,e])][index([t,0,0,e])] = .5
        out = mul(u,mul(full,adj(u)))
        reduced = [[sum(out[2*i+e][2*j+e] for e in range(2))
                    for j in range(8)] for i in range(8)]
        expected = [[0j]*8 for _ in range(8)]
        if s == t:
            expected[7*s][7*s] = 1
        close(reduced,expected)
        checked += 1
    # Explicit Bell input with an external reference R: input |Phi>_SR,
    # output 1/2 |0000><0000| + 1/2 |1111><1111| on S,D,M,R.
    amplitudes = {}
    for e in range(2):
        state = [0j]*32  # SDME,R
        for s in range(2):
            col = index([s,0,0,e])
            for row in range(N):
                state[2*row+s] += u[row][col]/math.sqrt(2)
        amplitudes[e] = state
    bell_reduced = [[0j]*16 for _ in range(16)]  # SDM,R
    for state in amplitudes.values():
        for i,j in itertools.product(range(16),repeat=2):
            # Interleave SDM and R, trace E.
            for eout in range(2):
                ii = 2*(2*(i//2)+eout)+(i%2)
                jj = 2*(2*(j//2)+eout)+(j%2)
                bell_reduced[i][j] += .5*state[ii]*state[jj].conjugate()
    expected = [[0j]*16 for _ in range(16)]
    expected[0][0]=expected[15][15]=.5
    close(bell_reduced,expected)
    # Reuse witness: a single random X-basis phase bit dephases a memory once,
    # but the same controlled-X collision twice is identity, NOT two fresh baths.
    c4 = [[complex(i==j) for j in range(4)] for i in (0,1,3,2)]
    initial = [[complex((i%2)==(j%2))*.25 for j in range(4)] for i in range(4)]
    collided = mul(c4,mul(initial,adj(c4)))
    twice = mul(c4,mul(collided,adj(c4)))
    close(mul(c4,c4),[[complex(i==j) for j in range(4)] for i in range(4)])
    close(twice,initial)
    def reduced_memory(rho):
        return [[sum(rho[2*i+e][2*j+e] for e in range(2)) for j in range(2)] for i in range(2)]
    one_collision = reduced_memory(collided)
    reused_twice = reduced_memory(twice)
    close(one_collision,[[.5,0j],[0j,.5]])
    close(reused_twice,[[.5,.5],[.5,.5]])
    # Apply the independently derived single-collision dephasing map again.
    fresh_twice = [[one_collision[i][j] if i==j else 0j for j in range(2)] for i in range(2)]
    assert abs(reused_twice[0][1]-fresh_twice[0][1]) == .5
    # Binary pure-system inputs: local record entropy equals H(p), NOT 2H(p).
    entropy_examples=[]
    for p in (0,.1,.5,.9,1):
        entropy=-sum(x*math.log(x) for x in (p,1-p) if x)
        entropy_examples.append({'probability_1':p,'joint_detector_memory_entropy_nats':entropy,
                                 'sum_of_separate_record_entropies_nats':2*entropy,
                                 'record_mutual_information_nats':entropy})
    # Independent midpoint quadrature checks the profile/packet constants;
    # it is not a simulation or certificate of physical propagation.
    count,a,ell=4096,10,20
    amp=2/math.sqrt(3*a)
    integrals=[0.0,0.0,0.0]
    area=0.0
    for n in range(count):
        y=-a+(n+.5)*2*a/count
        phase=math.pi*y/(2*a)
        vals=[amp*math.cos(phase)**2,
              -amp*math.pi/(2*a)*math.sin(2*phase),
              -amp*math.pi**2/(2*a*a)*math.cos(2*phase)]
        for j,val in enumerate(vals):integrals[j]+=val*val*2*a/count
        x=(n+.5)*ell/count
        area+=2*math.pi/ell*math.sin(math.pi*x/ell)**2*ell/count
    for actual,expected in zip(integrals,[1,math.pi**2/(3*a*a),math.pi**4/(3*a**4)]):
        assert abs(actual-expected)<1e-12
    assert abs(area-math.pi)<1e-12
    # Fixed mean speed: grow mass and shrink spatial apparatus/packet.
    # This avoids relying on unbounded velocity in the ideal-limit family.
    cases=[bounds(lam**3,100,.1,a=10/lam,ell=20/lam,gap=10/lam)
           for lam in (1,10,100,1000)]
    assert cases[2]['full_record_half_diamond_bound'] < .00151
    assert cases[3]['full_record_half_diamond_bound'] < .00015
    assert all(cases[i+1]['hold_vector_error_bound'] < cases[i]['hold_vector_error_bound']
               for i in range(len(cases)-1))
    # Along m=lambda^3, v=100, lengths=base/lambda,
    # bound=A/lambda^2+B/lambda exactly, at fixed mean velocity.
    for lam,case in zip((1,10,100,1000),cases):
        c=cases[0]['reference_second_derivative_bound']
        fpp=cases[0]['packet_second_derivative_norm']
        travel=cases[0]['travel_distance']
        expected=travel*c/(200*lam*lam)+(travel*.1/100+fpp/2)/lam
        assert abs(expected-case['hold_vector_error_bound']) < 1e-14
    return {'status':'passed','system_matrix_units_checked':checked,
            'bell_reference_channel_check':True,
            'positive_projector_gate_checks':3,
            'packet_and_spatial_profile_quadrature_checks':4,
            'cases':cases,'record_entropy_examples':entropy_examples,
            'same_environment_reuse_witness':{'one_collision_offdiag':0,
                 'two_same_environment_collisions_offdiag':.5,
                 'two_fresh_environment_collisions_offdiag':0,
                 'state_trace_distance_reuse_vs_fresh':.5},
            'scope':['Finite-time analytic bound for an autonomous bounded-below quadratic-kinetic Hamiltonian.',
                     'Exact reference transport is a proof tool; its linear momentum Hamiltonian is not the proposed physical clock.',
                     'Dimensionless models, not double-dot or cold-atom calibration.',
                     'Finite degenerate thermal ancilla, not a macroscopic mixing reservoir or a steady-state heat engine.',
                     'No raw PDE simulation, physical collapse, infinite retention, unlimited reuse or gravitational refoliation claim.']}


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: autonomous registration channel, finite-time bounds and finite-environment reuse obstruction')
    print(path)
