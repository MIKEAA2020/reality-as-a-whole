"""Dynamical smooth clock matter: constraints, initial data, flat recovery.

Analytic claims and scope: SMOOTH_FIELD_CLOCK.md. Numerical radial estimates
are not interval certificates or a coupled spacetime evolution.
"""
import cmath
import json
import math
import random
from pathlib import Path
if __package__:
    from .localized_constraint_clock import mm,mv,dot,eye,inverse,maxdiff
else:
    from localized_constraint_clock import mm,mv,dot,eye,inverse,maxdiff


def program():
    d=12;gamma=.05;ec=2.;m0=20.;a=math.sqrt(2)*gamma
    gate=[[float(j==(i^int(bool(i&2)))) for j in range(4)] for i in range(4)]
    q=eye(d)
    for i in range(4):
        for j in range(4):q[8+i][8+j]=gate[i][j]
    h0=[[ec*float(i==j)+gamma*float(abs(i//4-j//4)==1 and i%4==j%4) for j in range(d)] for i in range(d)]
    h=mm(mm(q,h0),q)
    mass=[[m0*float(i==j)+h[i][j] for j in range(d)] for i in range(d)]
    k=mm(mass,mass)
    delta=[[h[i][j]-ec*float(i==j) for j in range(d)] for i in range(d)]
    delta2=mm(delta,delta)
    projectors=[[[((delta2[i][j]/(a*a)+s*delta[i][j]/a)/2) if s else (float(i==j)-delta2[i][j]/(a*a)) for j in range(d)] for i in range(d)] for s in (-1,0,1)]
    v=[0.]*d;v[0]=v[2]=1/math.sqrt(2)
    mu=dot(v,mv(mass,v));kappa=dot(v,mv(k,v))
    assert abs(mu-22)<1e-12 and abs(kappa-(22**2+gamma**2))<1e-10
    return dict(d=d,gamma=gamma,ec=ec,m0=m0,mass=mass,k=k,h=h,q=q,h0=h0,
                a=a,projectors=projectors,v=v,mu=mu,kappa=kappa)


def determinant3(q):
    return q[0][0]*(q[1][1]*q[2][2]-q[1][2]*q[2][1])-q[0][1]*(q[1][0]*q[2][2]-q[1][2]*q[2][0])+q[0][2]*(q[1][0]*q[2][1]-q[1][1]*q[2][0])


def bracket_checks(p):
    rng=random.Random(3_291);hh_errors=[];density_errors=[]
    # One real half of the complex multiplet; the second is an identical sum.
    n=p['d'];k=p['k']
    for _ in range(160):
        l=[[rng.uniform(-.2,.2) if j<i else (1+rng.random() if j==i else 0.) for j in range(3)] for i in range(3)]
        q=mm(l,list(map(list,zip(*l))));qi=inverse(q);root=math.sqrt(determinant3(q))
        phi,pi=([rng.uniform(-.2,.2) for _ in range(n)] for _ in range(2))
        grad=[[rng.uniform(-.2,.2) for _ in range(n)] for _ in range(3)]
        dpi=[[rng.uniform(-.2,.2) for _ in range(n)] for _ in range(3)]
        hessian=[[[0.]*n for _ in range(3)] for _ in range(3)]
        for a in range(3):
            for b in range(a,3):
                value=[rng.uniform(-.2,.2) for _ in range(n)]
                hessian[a][b]=value;hessian[b][a]=value
        dq=[]
        for c in range(3):
            z=[[rng.uniform(-.2,.2) for _ in range(3)] for _ in range(3)]
            dq.append([[(z[a][b]+z[b][a])/2 for b in range(3)] for a in range(3)])
        w=[[root*sum(qi[a][b]*grad[b][j] for b in range(3)) for j in range(n)] for a in range(3)]
        divw=[rng.uniform(-1,1) for _ in range(n)]
        kp=mv(k,phi)
        lapse,other=rng.uniform(.1,2),rng.uniform(.1,2)
        dn,dl=([rng.uniform(-1,1) for _ in range(3)] for _ in range(2))
        variation_n=[lapse*(root*kp[j]-divw[j])-sum(dn[a]*w[a][j] for a in range(3)) for j in range(n)]
        variation_l=[other*(root*kp[j]-divw[j])-sum(dl[a]*w[a][j] for a in range(3)) for j in range(n)]
        actual=dot(variation_n,[other*x/root for x in pi])-dot([lapse*x/root for x in pi],variation_l)
        beta=mv(qi,[lapse*dl[a]-other*dn[a] for a in range(3)])
        expected=sum(beta[a]*dot(pi,grad[a]) for a in range(3))
        hh_errors.append(abs(actual-expected))
        grad2=sum(qi[a][b]*dot(grad[a],grad[b]) for a in range(3) for b in range(3))
        potential=dot(phi,kp);pi2=dot(pi,pi)
        density=pi2/(2*root)+root*(grad2+potential)/2
        metric_derivative=[[(-pi2/(4*root)+root*(grad2+potential)/4)*qi[a][b]
                            -root/2*sum(qi[a][c]*qi[b][e]*dot(grad[c],grad[e]) for c in range(3) for e in range(3)) for b in range(3)] for a in range(3)]
        def variation(dphi,dpi_,dgrad,dq_):
            return dot(pi,dpi_)/root+root*dot(kp,dphi)+sum(dot(w[a],dgrad[a]) for a in range(3))+sum(metric_derivative[a][b]*dq_[a][b] for a in range(3) for b in range(3))
        xi=[rng.uniform(-1,1) for _ in range(3)]
        dxi=[[rng.uniform(-1,1) for _ in range(3)] for _ in range(3)]
        divergence=sum(dxi[a][a] for a in range(3))
        lie_phi=[sum(xi[a]*grad[a][j] for a in range(3)) for j in range(n)]
        lie_pi=[sum(xi[a]*dpi[a][j] for a in range(3))+divergence*pi[j] for j in range(n)]
        lie_grad=[[sum(dxi[b][a]*grad[b][j]+xi[b]*hessian[a][b][j] for b in range(3)) for j in range(n)] for a in range(3)]
        lie_q=[[sum(xi[c]*dq[c][a][b]+q[c][b]*dxi[c][a]+q[a][c]*dxi[c][b] for c in range(3)) for b in range(3)] for a in range(3)]
        actual=variation(lie_phi,lie_pi,lie_grad,lie_q)
        spatial=[variation(grad[c],dpi[c],hessian[c],dq[c]) for c in range(3)]
        expected=dot(xi,spatial)+divergence*density
        density_errors.append(abs(actual-expected))
    assert max(hh_errors)<1e-9 and max(density_errors)<1e-9
    return dict(metric_field_jet_cases=160,hamiltonian_bracket_checks=160,
                shift_density_covariance_checks=160,maximum_hh_residual=max(hh_errors),
                maximum_shift_covariance_residual=max(density_errors),
                mixed_gravity_matter_cancellation='Analytic: local metric derivative times antisymmetric lapse product.')


def radial_initial_data(p,steps):
    radius=20.;amplitude=.001;b=.1;kappa=p['kappa'];mu=p['mu']
    coefficient=amplitude**2/8;end=8*radius;dr=end/steps
    r=[i*dr for i in range(steps+1)]
    f2=[math.exp(-(x/radius)**2) for x in r]
    fp2=[x*x/radius**4*y for x,y in zip(r,f2)]
    map_upper=amplitude**2/16*((1+b)+2*kappa*radius**2*(1+b)**5)
    contraction=amplitude**2/16*(1+10*kappa*radius**2*(1+b)**4)
    assert map_upper<b and contraction<1
    def integral(values):
        return dr*(sum(values[1:-1])+(values[0]+values[-1])/2)
    def green(values):
        source=[x*y+2*kappa*x**5*z for x,y,z in zip(values,fp2,f2)]
        inner=[0.];outer=[0.]*(steps+1)
        for i in range(1,steps+1):inner.append(inner[-1]+dr*(r[i-1]**2*source[i-1]+r[i]**2*source[i])/2)
        for i in range(steps-1,-1,-1):outer[i]=outer[i+1]+dr*(r[i]*source[i]+r[i+1]*source[i+1])/2
        updated=[1+coefficient*(inner[i]/x+outer[i] if i else outer[0]) for i,x in enumerate(r)]
        return updated,inner
    conformal=[1.]*(steps+1)
    for iteration in range(80):
        updated,inner=green(conformal)
        residual=max(abs(x-y) for x,y in zip(updated,conformal))
        conformal=updated
        if residual<2e-14:break
    else:raise AssertionError('radial Picard iteration did not converge')
    updated,inner=green(conformal)
    residual=max(abs(x-y) for x,y in zip(updated,conformal))
    assert residual<1e-12 and min(conformal)>=1 and max(conformal)<1+b
    c=coefficient*inner[-1]
    c_lower=coefficient*(3*math.sqrt(math.pi)*radius/8+kappa*math.sqrt(math.pi)*radius**3/2)
    c_upper=coefficient*((1+b)*3*math.sqrt(math.pi)*radius/8+(1+b)**5*kappa*math.sqrt(math.pi)*radius**3/2)
    assert c_lower<c<c_upper
    adm=16*math.pi*c
    proper=4*math.pi*amplitude**2*integral([x*x*(y*y*z/2+kappa*y**6*f) for x,y,z,f in zip(r,conformal,fp2,f2)])
    charge=4*math.pi*amplitude**2*mu*integral([x*x*y**6*z for x,y,z in zip(r,conformal,f2)])
    round_factor=min(1-2*coefficient*inner[i]/(x*conformal[i]) for i,x in enumerate(r) if i)
    assert proper>adm and round_factor>0
    rho_center=amplitude**2*kappa
    return dict(radial_steps=steps,profile_radius=radius,field_amplitude=amplitude,
                assumed_conformal_strip_upper=1+b,analytic_map_increment_upper=map_upper,
                analytic_contraction_constant=contraction,estimated_conformal_center=conformal[0],
                estimated_green_residual=residual,picard_iterations=iteration+1,
                tail_truncation_radius=end,estimated_asymptotic_coefficient=c,
                analytic_asymptotic_coefficient_lower=c_lower,analytic_asymptotic_coefficient_upper=c_upper,
                estimated_adm_energy=adm,estimated_proper_matter_energy=proper,
                estimated_gravitational_binding_energy=adm-proper,estimated_positive_charge=charge,
                exact_center_normal_energy_density=rho_center,
                estimated_minimum_round_sphere_expansion_factor=round_factor,
                momentum_constraint_zero='Exact: real field profile and purely imaginary normal derivative.')


def flat_recovery(p):
    # Radial momentum quadrature for a normalized 3D spatial Gaussian.
    radius=20.;a=p['a'];mass=p['m0']+p['ec'];mmin=mass-a;t=math.pi/a
    moment4=15/(4*radius**4)
    motion_bound=t*a*math.sqrt(moment4)/(2*mmin*mmin)
    negative_branch_bound=math.sqrt(moment4)/(4*mmin*mmin)
    configuration_bound=motion_bound+2*negative_branch_bound
    steps=1600;dx=8/steps
    motion2=0.;negative2=0.;configuration2=0.;normalization=0.
    weights=[dot(p['v'],mv(proj,p['v'])) for proj in p['projectors']]
    for i in range(steps+1):
        x=i*dx;momentum=x/radius;weight=4/math.sqrt(math.pi)*x*x*math.exp(-x*x)
        quadrature=dx*(.5 if i in (0,steps) else 1.)
        normalization+=quadrature*weight
        e0=math.sqrt(momentum**2+mass**2)
        for s,w in zip((-1,0,1),weights):
            lam=s*a;mu=mass+lam;energy=math.sqrt(momentum**2+mu*mu)
            # Factor out the common center-of-mass phase for stable subtraction.
            actual=cmath.exp(-1j*t*(energy-e0))
            target=cmath.exp(-1j*t*lam)
            beta=(1-mu/energy)/2
            classical=(1-beta)*actual+beta*cmath.exp(1j*t*(energy+e0))
            factor=quadrature*weight*w
            motion2+=factor*abs(actual-target)**2
            negative2+=factor*beta*beta
            configuration2+=factor*abs(classical-target)**2
    assert abs(normalization-1)<1e-12
    assert math.sqrt(motion2)<=motion_bound+1e-11
    assert math.sqrt(negative2)<=negative_branch_bound+1e-11
    assert math.sqrt(configuration2)<=configuration_bound+1e-11
    return dict(gaussian_spatial_radius=radius,program_duration=t,
                gaussian_momentum_fourth_moment=moment4,
                analytic_joint_quantum_vector_error_upper=motion_bound,
                analytic_negative_frequency_configuration_norm_upper=negative_branch_bound,
                analytic_classical_configuration_relative_error_upper=configuration_bound,
                estimated_joint_quantum_vector_error=math.sqrt(motion2),
                estimated_negative_frequency_configuration_norm=math.sqrt(negative2),
                estimated_classical_configuration_relative_error=math.sqrt(configuration2),
                scope='Fixed flat background only; L2 configuration norm is not a particle probability.')


def field_dressing_checks(p):
    q=p['q'];mass0=[[p['m0']*float(i==j)+p['h0'][i][j] for j in range(p['d'])] for i in range(p['d'])]
    k0=mm(mass0,mass0)
    assert maxdiff(p['k'],mm(mm(q,k0),q))<1e-10
    delta0=[[p['h0'][i][j]-p['ec']*float(i==j) for j in range(p['d'])] for i in range(p['d'])]
    delta02=mm(delta0,delta0);a=p['a'];d=p['d']
    free_proj=[[[((delta02[i][j]/(a*a)+s*delta0[i][j]/a)/2) if s else (float(i==j)-delta02[i][j]/(a*a)) for j in range(d)] for i in range(d)] for s in (-1,0,1)]
    residuals=[]
    for momentum in (0.,.1,2.,11.):
        for t in (0.,.3,4.,math.pi/a):
            frequencies=[math.sqrt(momentum**2+(22+s*a)**2) for s in (-1,0,1)]
            coefficients=[math.sin(e*t)/e for e in frequencies]
            propagator=[[sum(c*proj[i][j] for c,proj in zip(coefficients,p['projectors'])) for j in range(d)] for i in range(d)]
            free=[[sum(c*proj[i][j] for c,proj in zip(coefficients,free_proj)) for j in range(d)] for i in range(d)]
            residuals.append(maxdiff(propagator,mm(mm(q,free),q)))
    assert max(residuals)<1e-12
    return dict(mass_matrix_rotation=True,fourier_causal_propagator_rotation_checks=16,
                maximum_rotation_residual=max(residuals),
                scope='Matrix identities; causal support follows analytically from the Klein-Gordon propagators, not Fourier sampling.')


def run():
    p=program();radial=[radial_initial_data(p,n) for n in (2048,4096,8192)]
    assert abs(radial[-1]['estimated_conformal_center']-radial[-2]['estimated_conformal_center'])<1e-7
    assert abs(radial[-1]['estimated_adm_energy']-radial[-2]['estimated_adm_energy'])<1e-6
    return dict(status='passed',internal_dimension=p['d'],mean_mass=p['mu'],mass_second_moment=p['kappa'],
                smooth_field_brackets=bracket_checks(p),radial_initial_data=radial,
                flat_clock_recovery=flat_recovery(p),local_field_dressing=field_dressing_checks(p),
                scope=['Smooth dynamical complex multiplet, not fixed coordinate smearing.',
                       'Analytic contraction proves nonlinear classical constraint initial data in a declared strip.',
                       'Radial numbers and Fourier integrals are estimates, not interval certificates.',
                       'AQFT bridge is on fixed globally hyperbolic backgrounds, independent of a chosen Fock representation.',
                       'No coupled Einstein-field evolution record bound, quantum Einstein baseline or stable bound body is supplied.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: smooth clock matter, local brackets, gravitational initial data and flat recovery')
    print(path)
