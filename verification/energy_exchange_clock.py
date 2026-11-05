"""Noncommuting-system Hamiltonian clock: exact matrix scattering and analytic bounds.

No external numerical packages. Floating-point quadrature witnesses are distinct
from the uniform analytic estimates derived in ENERGY_EXCHANGE_CLOCK.md.
"""
import cmath
import math
import json
from pathlib import Path
if __package__:
    from .hamiltonian_detector import scattering as scalar_scattering
else:
    from hamiltonian_detector import scattering as scalar_scattering

I=[[1+0j,0j],[0j,1+0j]]
P1=[[.5+0j,-.5+0j],[-.5+0j,.5+0j]]  # Z-system outcome 1 in its X-energy basis


def add(a,b,scale=1):
    return [[x+scale*y for x,y in zip(r,s)] for r,s in zip(a,b)]


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def diag(xs):
    return [[complex(xs[0]),0j],[0j,complex(xs[1])]]


def inverse(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert abs(d)>1e-15
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]


def max_entry(a):
    return max(abs(x) for row in a for x in row)


def hermitian_norm(a):
    assert abs(a[0][0].imag)+abs(a[1][1].imag)+abs(a[0][1]-a[1][0].conjugate())<1e-8
    center=(a[0][0].real+a[1][1].real)/2
    radius=math.sqrt(((a[0][0].real-a[1][1].real)/2)**2+abs(a[0][1])**2)
    return abs(center)+radius


def opnorm(a):
    return math.sqrt(max(0,hermitian_norm(mul(adj(a),a))))


def solve(a,b):
    n=len(b)
    rows=[list(row)+[complex(x)] for row,x in zip(a,b)]
    for j in range(n):
        pivot=max(range(j,n),key=lambda i:abs(rows[i][j]))
        rows[j],rows[pivot]=rows[pivot],rows[j]
        v=rows[j][j]
        assert abs(v)>1e-14
        rows[j]=[x/v for x in rows[j]]
        for i in range(n):
            if i!=j:
                v=rows[i][j]
                rows[i]=[x-v*y for x,y in zip(rows[i],rows[j])]
    return [row[-1] for row in rows]


def transfer(E,m,g,omega,L,y):
    assert E>omega+g and m>0 and g>=0 and omega>=0
    radius=math.hypot(omega,g/2)
    if radius==0:
        raise ValueError('use a nonzero omega or g')
    H=[[omega+0j,-y*g/2],[-y*g/2,-omega+0j]]
    blocks=[]
    for kind in range(3):
        value=[[0j,0j],[0j,0j]]
        for sign in (-1,1):
            lam=y*g/2+sign*radius
            k=math.sqrt(2*m*(E-lam))
            coefficient=(math.cos(k*L),math.sin(k*L)/k,-k*math.sin(k*L))[kind]
            projection=add(I,H,sign/radius)
            value=add(value,projection,coefficient/2)
        blocks.append(value)
    C,D,F=blocks
    momenta=[math.sqrt(2*m*(E-e)) for e in (omega,-omega)]
    K=diag(momenta)
    root=diag([math.sqrt(k) for k in momenta])
    invroot=diag([1/math.sqrt(k) for k in momenta])
    u0=add(mul(C,invroot),mul(D,root),1j)
    u1=add(mul(C,invroot),mul(D,root),-1j)
    v0=add(mul(F,invroot),mul(C,root),1j)
    v1=add(mul(F,invroot),mul(C,root),-1j)
    return momenta,K,root,invroot,u0,u1,v0,v1


def scatter(E,m,g,omega,L,y,independent=False,centered=True):
    ks,K,root,invroot,u0,u1,v0,v1=transfer(E,m,g,omega,L,y)
    if independent:
        outgoing=mul(invroot,diag([cmath.exp(1j*k*L) for k in ks]))
        derivative=mul(root,diag([1j*cmath.exp(1j*k*L) for k in ks]))
        matrix=[u1[i]+[-x for x in outgoing[i]] for i in range(2)]
        matrix += [v1[i]+[-x for x in derivative[i]] for i in range(2)]
        columns=[solve(matrix,[-u0[i][j] for i in range(2)]+[-v0[i][j] for i in range(2)]) for j in range(2)]
        r=[[columns[j][i] for j in range(2)] for i in range(2)]
        t=[[columns[j][i+2] for j in range(2)] for i in range(2)]
    else:
        numerator=add([[1j*x for x in row] for row in mul(K,u0)],v0,-1)
        r=mul(inverse(add(v1,mul(K,u1),-1j)),numerator)
        t=mul(diag([cmath.exp(-1j*k*L)*math.sqrt(k) for k in ks]),add(u0,mul(u1,r)))
    if centered:
        plus=diag([cmath.exp(1j*k*L/2) for k in ks])
        minus=adj(plus)
        t=mul(mul(plus,t),minus)
        r=mul(mul(minus,r),minus)
    return t,r


def pointer(E,m,g,omega,L):
    tp,rp=scatter(E,m,g,omega,L,1)
    tm,rm=scatter(E,m,g,omega,L,-1)
    scale=lambda a,c:[[c*x for x in row] for row in a]
    return [scale(add(tp,tm),.5),scale(add(tp,tm,-1),.5j),
            scale(add(rp,rm),.5),scale(add(rp,rm,-1),.5j)]


def analytic_bounds(m,g,omega,L,p0,spread):
    pmin,pmax=p0-spread,p0+spread
    Emin=pmin*pmin/(2*m)-omega
    Emax=pmax*pmax/(2*m)+omega
    h=omega+g
    assert pmin>0 and Emin>h
    kmin=math.sqrt(2*m*(Emin-h))
    ratio=math.sqrt((Emin+h)/(Emin-h))
    rho=(ratio-1)/(ratio+1)
    eta=m*g/(2*kmin*kmin)+math.sqrt(ratio)*rho
    interfaces=2*eta+rho*rho/(1-rho*rho)
    reflection=min(1,(2*rho/(1-rho*rho))**2)
    qmin,qmax=math.sqrt(2*m*Emin),math.sqrt(2*m*Emax)
    curvature=L*m*m*(h*h+omega*omega)/(2*qmin**3*(1-h/Emin)**1.5)
    free_dynamics=2*omega*m*L/qmin
    angle=g*m*L*max(abs(1/qmin-1/p0),abs(1/qmax-1/p0))
    transmitted=interfaces+curvature+free_dynamics+angle
    scattering_error=math.sqrt(transmitted**2+reflection)
    derivative=m*(math.pi/(2*spread*pmin)+1/(2*pmin*pmin))
    coherence_upper=min(.5,omega*omega*derivative*derivative)
    disjoint=2*omega>=2*p0*spread/m
    return {'total_energy_min':Emin,'total_energy_max':Emax,
            'interface_reflection_amplitude_rho':rho,'interface_transmission_deviation_eta':eta,
            'slab_interface_error_bound':interfaces,'reflection_probability_bound':reflection,
            'matrix_phase_curvature_bound':curvature,'noncommuting_free_dynamics_bound':free_dynamics,
            'angle_bandwidth_bound':angle,'transmitted_operator_error_bound':transmitted,
            'per_energy_scattering_isometry_error_bound':scattering_error,
            'coherence_penalty_upper_bound':coherence_upper,
            'full_coherent_energy_shift_error_bound':min(1,math.sqrt(2)*omega*derivative),
            'full_outgoing_event_error_upper_bound':min(1,scattering_error+min(1,math.sqrt(2)*omega*derivative)),
            'worst_case_pointer_event_error_upper_bound':min(1,coherence_upper+scattering_error),
            'disjoint_incoming_energy_bands':disjoint,
            'exact_coherence_lower_bound_when_disjoint':.5 if disjoint else None}


def integral_effect(m,g,omega,L,p0,spread,n):
    low,high=(p0-spread)**2/(2*m),(p0+spread)**2/(2*m)
    cuts=sorted(set([low-omega,low+omega,high-omega,high+omega]))
    def f(p):
        return math.cos(math.pi*(p-p0)/(2*spread))/math.sqrt(spread) if p0-spread<p<p0+spread else 0
    def integrand(E):
        ks=[math.sqrt(2*m*(E-e)) for e in (omega,-omega)]
        fs=[math.sqrt(m/k)*f(k) for k in ks]
        if not any(fs):
            return [0j]*14
        ops=pointer(E,m,g,omega,L)
        M=add(mul(adj(ops[1]),ops[1]),mul(adj(ops[3]),ops[3]))
        total=[[0j,0j],[0j,0j]]
        for op in ops:
            total=add(total,mul(adj(op),op))
        assert max_entry(add(total,I,-1))<2e-10
        assert abs(M[0][1])<=.5+1e-10
        # Actual energy transitions, summed over pointer and exit direction.
        transitions=[fs[i]**2*sum(abs(op[1-i][i])**2 for op in ops) for i in range(2)]
        overlaps=[]
        for psi in ((1,0),(1/math.sqrt(2),1/math.sqrt(2)),(1/math.sqrt(2),-1/math.sqrt(2)),(1/math.sqrt(2),1j/math.sqrt(2))):
            incoming=[fs[i]*psi[i] for i in range(2)]
            overlap=0j
            for j,projector in enumerate((add(I,P1,-1),P1)):
                exact=[sum(ops[j][s][i]*incoming[i] for i in range(2)) for s in range(2)]
                ideal=[fs[s]*sum(projector[s][i]*psi[i] for i in range(2)) for s in range(2)]
                overlap+=sum(a.conjugate()*b for a,b in zip(ideal,exact))
            overlaps.append(overlap)
        return [fs[i]*M[i][j]*fs[j] for i in range(2) for j in range(2)]+[fs[0]*fs[1],fs[0]**2,fs[1]**2]+transitions+[fs[0]**2*ops[1][0][0]*ops[1][1][0].conjugate()]+overlaps
    out=[0j]*14
    for a,b in zip(cuts,cuts[1:]):
        step=(b-a)/n
        for j in range(n+1):
            value=integrand(a+j*step)
            weight=(1 if j in (0,n) else 4 if j%2 else 2)*step/3
            out=[x+weight*y for x,y in zip(out,value)]
    effect=[out[:2],out[2:4]]
    delta=hermitian_norm(add(effect,P1,-1))
    V=out[4].real
    assert abs(out[5]-1)<1e-7 and abs(out[6]-1)<1e-7
    assert delta+1e-8>=(1-V)/2
    return {'effect':[[[z.real,z.imag] for z in row] for row in effect],
            'full_outgoing_trace_distances_for_energy_plus_Z0_Z1_complex_inputs':[math.sqrt(max(0,1-abs(z)**2)) for z in out[10:14]],
            'worst_case_pointer_event_error':delta,'energy_overlap_visibility':V,
            'coherence_error_floor':max(0,(1-V)/2),
            'incoming_energy_norms':[out[5].real,out[6].real],
            'energy_transition_probabilities_plus_to_minus_and_reverse':[out[7].real,out[8].real],
            'T1_unnormalized_energy_frame_offdiag_for_energy_plus_input':[out[9].real,out[9].imag],
            'physical_reduced_offdiag_for_same_event_if_bands_disjoint':0 if 2*omega>=high-low else None,
            'click_probability_on_Z0':((out[0]+out[3]+out[1]+out[2])/2).real,
            'click_probability_on_Z1':((out[0]+out[3]-out[1]-out[2])/2).real}


def run():
    # Pointwise identity behind the full coherent recoil term, on the full S/D space.
    kron=lambda a,b:[[a[i//2][j//2]*b[i%2][j%2] for j in range(4)] for i in range(4)]
    pointer_rotation=[[0j,-1+0j],[1+0j,0j]]
    U=add(kron(add(I,P1,-1),I),kron(P1,pointer_rotation))
    identity4=[[complex(i==j) for j in range(4)] for i in range(4)]
    assert max_entry(add(mul(adj(U),U),identity4,-1))<1e-14
    for a,b in ((1,.3),(.2,1.7),(0,1)):
        F=kron(diag((a,b)),I)
        commutator=add(mul(U,F),mul(F,U),-1)
        target=[[.5*(a-b)**2*x for x in row] for row in identity4]
        assert max_entry(add(mul(adj(commutator),commutator),target,-1))<1e-14
    matching=0
    for omega in (0,.1,1):
        for g in (.1,1,3):
            for E in (10,40,100):
                for L in (.7,3):
                    for y in (-1,1):
                        t,r=scatter(E,1,g,omega,L,y)
                        tt,rr=scatter(E,1,g,omega,L,y,independent=True)
                        assert max_entry(add(t,tt,-1))<1e-11 and max_entry(add(r,rr,-1))<1e-11
                        assert max_entry(add(add(mul(adj(t),t),mul(adj(r),r)),I,-1))<1e-11
                        if omega==0:
                            ts,rs=scalar_scattering(math.sqrt(2*E),1,g,L,y)
                            target=add(I,P1,ts-1)
                            reflect=[[rs*cmath.exp(-1j*math.sqrt(2*E)*L)*x for x in row] for row in P1]
                            assert max_entry(add(t,target,-1))<1e-11
                            assert max_entry(add(r,reflect,-1))<1e-11
                        matching+=1
    for y in (-1,1):
        t,r=scatter(20,1,0,1,2,y)
        assert max_entry(add(t,I,-1))<1e-11 and max_entry(r)<1e-11
    cases=[]
    for p0,g,spread in ((10,1,.002),(10,1,.1),(40,4,.1),(160,16,.1),(640,64,.1)):
        m,omega=1,.1
        L=math.pi*p0/(2*m*g)
        bound=analytic_bounds(m,g,omega,L,p0,spread)
        for j in range(25):
            E=bound['total_energy_min']+(bound['total_energy_max']-bound['total_energy_min'])*j/24
            for y in (-1,1):
                t,r=scatter(E,m,g,omega,L,y)
                ideal=add(I,P1,cmath.exp(-1j*y*math.pi/2)-1)
                difference=add(t,ideal,-1)
                assert opnorm(difference)<=bound['transmitted_operator_error_bound']+1e-9
                assert opnorm(r)**2<=bound['reflection_probability_bound']+1e-9
                full=add(mul(adj(difference),difference),mul(adj(r),r))
                assert hermitian_norm(full)<=bound['per_energy_scattering_isometry_error_bound']**2+1e-9
            energies=(omega,-omega)
            ks=[math.sqrt(2*m*(E-e)) for e in energies]
            assert abs(ks[0]**2/(2*m)+energies[0]-ks[1]**2/(2*m)-energies[1])<1e-8
        coarse=integral_effect(m,g,omega,L,p0,spread,128)
        fine=integral_effect(m,g,omega,L,p0,spread,256)
        discrepancy=max(abs(fine[k]-coarse[k]) for k in ('worst_case_pointer_event_error','energy_overlap_visibility','click_probability_on_Z0','click_probability_on_Z1'))
        assert discrepancy<1e-7
        assert max(fine['full_outgoing_trace_distances_for_energy_plus_Z0_Z1_complex_inputs'])<=bound['full_outgoing_event_error_upper_bound']+1e-7
        assert fine['coherence_error_floor']<=bound['coherence_penalty_upper_bound']+1e-7
        assert fine['worst_case_pointer_event_error']<=bound['worst_case_pointer_event_error_upper_bound']+1e-7
        assert all(x>0 for x in fine['energy_transition_probabilities_plus_to_minus_and_reverse'])
        if bound['disjoint_incoming_energy_bands']:
            assert (p0+spread)**2 <= (p0-spread)**2+4*m*omega+1e-10
            assert abs(complex(*fine['T1_unnormalized_energy_frame_offdiag_for_energy_plus_input']))>.1
            assert fine['energy_overlap_visibility']==0
            assert abs(fine['click_probability_on_Z0']-fine['click_probability_on_Z1'])<1e-12
        cases.append({'p0':p0,'g':g,'omega':omega,'momentum_half_band':spread,'length':L,
                      'clock_mean_kinetic_energy':(p0*p0+spread**2*(1/3-2/math.pi**2))/(2*m),
                      'minimum_free_packet_position_spread':math.pi/(2*spread),
                      'analytic_bounds':bound,'quadrature_128_256_discrepancy':discrepancy,
                      'numerical_effect':fine})
    return {'status':'passed','independent_matrix_matching_checks':matching,
            'full_coherent_energy_shift_commutator_identity_checked':True,
            'hamiltonian':'P^2/(2m) + omega X_S + g 1_[-L/2,L/2](X) P1_Z tensor Y_D',
            'energy_basis':'X_S eigenstates, energies +omega,-omega',
            'energy_exchange_quanta':'plus or minus 2*omega; outgoing momenta depend on system energy',
            'prepared_clock':'product incoming cosine momentum packet and arbitrary system state; ready pointer |0>',
            'target_event':'Z-system outcome 1 at free reference epoch T=0, packet focused at detector center',
            'cases':cases,
            'limits':['analytic formulas provide model bounds; reported floating evaluations are not interval-certified',
                      'energy quadrature computes pointer effects, not a post-system channel obtained by wrongly tracing total energy',
                      'complete instrument retains outgoing energy coherences and maps back to physical momentum as derived in report',
                      'asymptotic readout, not finite-time first arrival or a cold-atom calibration',
                      'no gravitational refoliation or derivation of the supplied Hamiltonian']}


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: noncommuting energy-exchange scattering, flux, product preparation and coherence/accuracy bounds')
    print(path)
