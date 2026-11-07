"""Localized finite clock: classical ADM matter closure and fixed-background check.

See LOCALIZED_CONSTRAINT_CLOCK.md. No quantum gravitational algebra is claimed.
"""
import cmath
import json
import math
import random
from pathlib import Path


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def eye(n):
    return [[float(i==j) for j in range(n)] for i in range(n)]


def mv(a,v):
    return [sum(x*y for x,y in zip(row,v)) for row in a]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def maxdiff(a,b):
    return max(abs(x-y) for ra,rb in zip(a,b) for x,y in zip(ra,rb))


def inverse(a):
    n=len(a);b=[list(row)+e for row,e in zip(a,eye(n))]
    for j in range(n):
        k=max(range(j,n),key=lambda k:abs(b[k][j]));b[j],b[k]=b[k],b[j]
        pivot=b[j][j];assert abs(pivot)>1e-12
        b[j]=[x/pivot for x in b[j]]
        for k in range(n):
            if k!=j:
                factor=b[k][j];b[k]=[x-factor*y for x,y in zip(b[k],b[j])]
    return [row[n:] for row in b]


def local_bracket_checks():
    rng=random.Random(97858);errors=[];uncorrected=[];cross_errors=[]
    for _ in range(240):
        l=[[rng.uniform(-.3,.3) if j<i else (1+rng.random() if j==i else 0.) for j in range(3)] for i in range(3)]
        q=mm(l,list(map(list,zip(*l))));qi=inverse(q)
        dq=[]
        for k in range(3):
            a=[[rng.uniform(-1,1) for _ in range(3)] for _ in range(3)]
            dq.append([[(a[i][j]+a[j][i])/2 for j in range(3)] for i in range(3)])
        p=[rng.uniform(-3,3) for _ in range(3)];v=mv(qi,p)
        mass=rng.uniform(20,25);energy=math.sqrt(dot(p,v)+mass*mass)
        n,m=rng.uniform(.2,2),rng.uniform(.2,2)
        dn,dm=([rng.uniform(-1,1) for _ in range(3)] for _ in range(2))
        de=[-dot(v,mv(dq[k],v))/(2*energy) for k in range(3)]
        dhn=[dn[k]*energy+n*de[k] for k in range(3)]
        dhm=[dm[k]*energy+m*de[k] for k in range(3)]
        hh=dot(dhn,[m*x/energy for x in v])-dot([n*x/energy for x in v],dhm)
        beta=mv(qi,[n*dm[k]-m*dn[k] for k in range(3)])
        errors.append(abs(hh+dot(p,beta)))
        xi,eta=([rng.uniform(-1,1) for _ in range(3)] for _ in range(2))
        # dxi[a][c] = partial_c xi^a.
        dxi,deta=([[rng.uniform(-1,1) for _ in range(3)] for _ in range(3)] for _ in range(2))
        dd=dot([-sum(p[a]*dxi[a][c] for a in range(3)) for c in range(3)],[-x for x in eta])-dot([-x for x in xi],[-sum(p[a]*deta[a][c] for a in range(3)) for c in range(3)])
        lie=[sum(xi[c]*deta[a][c]-eta[c]*dxi[a][c] for c in range(3)) for a in range(3)]
        errors.append(abs(dd+dot(p,lie)))
        dh_particle=-n/energy*sum(p[a]*dxi[a][c]*v[c] for a in range(3) for c in range(3))+dot(xi,dhn)
        lieq=[[sum(xi[k]*dq[k][a][b]+q[k][b]*dxi[k][a]+q[a][k]*dxi[k][b] for k in range(3)) for b in range(3)] for a in range(3)]
        metric_contribution=n/(2*energy)*dot(v,mv(lieq,v))
        expected=energy*dot(xi,dn)
        errors.append(abs(dh_particle+metric_contribution-expected))
        uncorrected.append(abs(dh_particle-expected))
        # delta H_g[N]/delta pi_ab = N times a local symmetric tensor.
        a=[[rng.uniform(-1,1) for _ in range(3)] for _ in range(3)]
        contraction=sum((a[i][j]+a[j][i])/2*(-v[i]*v[j]/(2*energy)) for i in range(3) for j in range(3))
        cross_errors.append(abs(-n*m*contraction+m*n*contraction))
    assert max(errors)<1e-11 and max(cross_errors)<1e-12
    assert max(uncorrected)>.01
    return dict(spatial_dimension=3,metric_lapse_shift_jet_cases=240,
                bracket_identity_checks=720,maximum_bracket_residual=max(errors),
                maximum_gravity_matter_cross_residual=max(cross_errors),
                maximum_error_if_metric_shift_action_is_omitted=max(uncorrected),
                scope='Matter-sector and mixed local identities on smooth ADM kinematic data, not a discretized Einstein evolution.')


def copy_program():
    gamma=.05;ec=2.;m0=20.;d=12
    gate=[[float(j==(i^int(bool(i&2)))) for j in range(4)] for i in range(4)]
    assert maxdiff(mm(gate,gate),eye(4))<1e-15
    q=eye(d)
    for i in range(4):
        for j in range(4):q[8+i][8+j]=gate[i][j]
    free=[[ec*float(i==j)+gamma*float(abs(i//4-j//4)==1 and i%4==j%4) for j in range(d)] for i in range(d)]
    h=mm(mm(q,free),q)
    delta=[[h[i][j]-ec*float(i==j) for j in range(d)] for i in range(d)]
    delta2=mm(delta,delta);delta3=mm(delta2,delta);a=math.sqrt(2)*gamma
    assert maxdiff(delta3,[[a*a*x for x in row] for row in delta])<1e-15
    projectors=[[[((delta2[i][j]/(a*a)+s*delta[i][j]/a)/2) if s else (float(i==j)-delta2[i][j]/(a*a)) for j in range(d)] for i in range(d)] for s in (-1,0,1)]
    def evolve(phase,psi):
        return [sum(phase(s*a)*mv(proj,psi)[i] for s,proj in zip((-1,0,1),projectors)) for i in range(d)]
    # Functional calculus commutes with the internal program dressing.
    free_delta=[[free[i][j]-ec*float(i==j) for j in range(d)] for i in range(d)]
    free_delta2=mm(free_delta,free_delta)
    free_projectors=[[[((free_delta2[i][j]/(a*a)+s*free_delta[i][j]/a)/2) if s else (float(i==j)-free_delta2[i][j]/(a*a)) for j in range(d)] for i in range(d)] for s in (-1,0,1)]
    mass=m0+ec
    mass_matrix=[[m0*float(i==j)+h[i][j] for j in range(d)] for i in range(d)]
    mass_square=mm(mass_matrix,mass_matrix)
    mass_functional_residuals=[]
    for p in (0.,1.,11.,22.):
        values=[math.sqrt(p*p+(mass+s*a)**2) for s in (-1,0,1)]
        moving=[[sum(value*proj[i][j] for value,proj in zip(values,projectors)) for j in range(d)] for i in range(d)]
        moving_free=[[sum(value*proj[i][j] for value,proj in zip(values,free_projectors)) for j in range(d)] for i in range(d)]
        residual=maxdiff(moving,mm(mm(q,moving_free),q))
        square_residual=maxdiff(mm(moving,moving),[[p*p*float(i==j)+mass_square[i][j] for j in range(d)] for i in range(d)])
        assert residual<1e-11 and square_residual<1e-9
        mass_functional_residuals.append(max(residual,square_residual))
    initial=[0j]*d;initial[0]=initial[2]=1/math.sqrt(2)
    target=[0j]*d;target[8]=target[11]=-1/math.sqrt(2)
    tau=math.pi/a
    for bit in range(4):
        seed=[complex(i==bit) for i in range(d)]
        result=evolve(lambda lam:cmath.exp(-1j*tau*lam),seed)
        expected=[-gate[i-8][bit] if i>=8 else 0. for i in range(d)]
        assert max(abs(x-y) for x,y in zip(result,expected))<1e-12
    final=evolve(lambda lam:cmath.exp(-1j*tau*lam),initial)
    assert max(abs(x-y) for x,y in zip(final,target))<1e-12
    assert abs(sum(abs(z)**2 for z in final)-1)<1e-12
    energy0=dot([x.conjugate() for x in initial],mv(h,initial))
    energy1=dot([x.conjugate() for x in final],mv(h,final))
    assert abs(energy0-energy1)<1e-12
    recurrence=evolve(lambda lam:cmath.exp(-2j*tau*lam),initial)
    assert max(abs(x-y) for x,y in zip(recurrence,initial))<1e-12
    mass=m0+ec;minmass=mass-a;rows=[]
    for p0,dp in ((0.,0.),(11.,0.),(11.,.01),(11.,.1)):
        alpha0=mass/math.sqrt(p0*p0+mass*mass);t=tau/alpha0
        lo,hi=p0-dp,p0+dp
        alphas=[mass/math.sqrt(p*p+mass*mass) for p in (lo,hi)]
        alpha_error=max(abs(x-alpha0) for x in alphas)
        if lo<=0<=hi:alpha_error=max(alpha_error,abs(1-alpha0))
        ps=[lo,hi]
        for critical in (-math.sqrt(2)*minmass,math.sqrt(2)*minmass):
            if lo<=critical<=hi:ps.append(critical)
        curvature=max(p*p/(p*p+minmass*minmass)**1.5 for p in ps)
        raw_bound=t*(a*alpha_error+.5*a*a*curvature)
        bound=min(1.,raw_bound)
        exact_max=0.;record_errors=[]
        for j in range(81):
            p=lo+(hi-lo)*j/80
            e0=math.sqrt(p*p+mass*mass)
            phase=lambda lam:cmath.exp(-1j*t*(math.sqrt(p*p+(mass+lam)**2)-e0))
            exact_max=max(exact_max,max(abs(phase(lam)-cmath.exp(-1j*tau*lam)) for lam in (-a,0.,a)))
            actual=evolve(phase,initial)
            actual_norm=math.sqrt(sum(abs(x)**2 for x in actual))
            target_norm=math.sqrt(sum(abs(x)**2 for x in target))
            actual_unit=[x/actual_norm for x in actual]
            target_unit=[x/target_norm for x in target]
            overlap=sum(x.conjugate()*y for x,y in zip(target_unit,actual_unit))
            # Stable pure-state distance: norm of the perpendicular component.
            record_errors.append(math.sqrt(sum(abs(y-overlap*x)**2 for x,y in zip(target_unit,actual_unit))))
        assert exact_max<=raw_bound+1e-11
        # Pure-state distance <= unitary operator error; roundoff tolerance.
        assert max(record_errors)<=bound+1e-11
        rows.append(dict(momentum_center=p0,momentum_half_width=dp,
                         coordinate_duration=t,nominal_proper_duration=tau,
                         uniform_joint_half_diamond_error_bound=bound,
                         uniform_raw_unitary_operator_error_bound=raw_bound,
                         sampled_maximum_operator_error=exact_max,
                         sampled_maximum_full_state_trace_distance=max(record_errors)))
    return dict(hilbert_dimension=d,clock_sites=3,register_bits=2,hopping=gamma,
                internal_source_offset=ec,additional_rest_mass=m0,
                minimum_total_mass=minmass,maximum_total_mass=mass+a,
                rest_copy_proper_duration=tau,exact_rest_copy=True,
                full_register_basis_copy_checks=4,
                relativistic_mass_functional_calculus_checks=4,
                maximum_mass_functional_calculus_residual=max(mass_functional_residuals),
                initial_internal_energy=energy0.real,final_internal_energy=energy1.real,
                finite_clock_recurrence_proper_duration=2*tau,
                moving_body_fixed_flat_background_cases=rows)


def run():
    return dict(status='passed',classical_local_algebra=local_bracket_checks(),
                finite_carried_program=copy_program(),
                scope=['Localized worldline matter with an internal finite Hamiltonian.',
                       'Classical hypersurface-deformation identities include the metric transformation and dynamical particle position.',
                       'Point-source self-gravity needs a regularization or finite-body completion.',
                       'The quantum calculation is on a fixed flat background; no anomaly-free quantum Einstein algebra is claimed.',
                       'Moving mass superpositions need not run at one sharp proper-time rate.',
                       'No source synthesis, singularity resolution, permanent latch or phenomenal constitution.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: localized classical constraint identities and finite carried-clock checks')
    print(path)
