"""Shared finite reservoir: exact multi-readout instrument and finite capacity.

No fresh-reference replacement. Dense tests use <=3 systems; large resource
witnesses evaluate analytic bounds only. See REUSED_REFERENCE_CLOCK.md.
"""
import json
import math
from pathlib import Path


def packet(top,guard):
    d=top-2*guard+2
    assert guard>=1 and d>=2
    b=[math.sqrt(2/d)*math.sin(math.pi*(n-guard+1)/d)
       if guard<=n<=top-guard else 0. for n in range(top+1)]
    assert abs(sum(x*x for x in b)-1)<1e-13
    return b,d


def overlap(b,shift):
    k=abs(shift)
    return sum(b[n]*b[n+k] for n in range(max(0,len(b)-k)))


def overlap_formula(d,k):
    k=abs(k)
    if k>=d:return 0.
    theta=math.pi/d
    return ((d-1-k)*math.cos(k*theta)+math.sin((k+1)*theta)/math.sin(theta))/d


def step(v,system,outcome,m):
    dim=len(v);top=len(v[0])-1;mask=1<<(m-1-system)
    sign=1 if outcome==0 else -1
    out=[[z/2 for z in row] for row in v]
    for s in range(dim):
        e=int(bool(s&mask))
        for n,a in enumerate(v[s]):
            if (e==0 and n>0):t,p=s^mask,n-1
            elif (e==1 and n<top):t,p=s^mask,n+1
            else:t,p=s,n
            assert s.bit_count()+n==t.bit_count()+p
            out[t][p]+=sign*a/2
    return out


def actual_branches(top,m,guard):
    b,d=packet(top,guard);dim=1<<m;out={}
    for r in range(dim):
        for bits in range(dim):
            v=[[0j]*(top+1) for _ in range(dim)];v[r]=list(b)
            for j in range(m):v=step(v,j,(bits>>(m-1-j))&1,m)
            out[bits,r]=v
    return b,d,out


def joint_instrument_check(top,m,guard):
    b,d,vs=actual_branches(top,m,guard);dim=1<<m
    cs=[overlap(b,k) for k in range(2*m+1)]
    for k,c in enumerate(cs):assert abs(c-overlap_formula(d,k))<1e-13
    maximum=0.;checked=0
    for r in range(dim):
        for s in range(dim):
            trace=0j
            for bits in range(dim):
                vr=vs[bits,r];vw=vs[bits,s]
                for e in range(dim):
                    for f in range(dim):
                        actual=sum(vr[e][n]*complex(vw[f][n]).conjugate() for n in range(top+1))
                        sign=(-1)**((bits&(e^r)).bit_count()+(bits&(f^s)).bit_count())
                        shift=r.bit_count()-e.bit_count()-s.bit_count()+f.bit_count()
                        expected=sign*cs[abs(shift)]/(dim*dim)
                        maximum=max(maximum,abs(actual-expected))
                        if e==f:trace+=actual
                checked+=1
            assert abs(trace-(r==s))<1e-12
    if guard>=m:assert maximum<1e-12
    # GHZ in the energy basis witnesses joint parity error C_m, not m fresh errors.
    wrong=0.
    for bits in range(dim):
        if bits.bit_count()%2:
            a=vs[bits,0];z=vs[bits,dim-1]
            wrong+=sum(abs((a[e][n]+z[e][n])/math.sqrt(2))**2
                       for e in range(dim) for n in range(top+1))
    if guard>=m:assert abs(wrong-(1-cs[m])/2)<1e-12
    correlations=None
    if m==2 and guard>=m:
        probs=[]
        for bits in range(dim):
            v=[[sum(vs[bits,r][e][n] for r in range(dim))/math.sqrt(dim)
                for n in range(top+1)] for e in range(dim)]
            probs.append(sum(abs(z)**2 for row in v for z in row))
        q1=probs[2]+probs[3];q2=probs[1]+probs[3]
        expected=(3-4*cs[1]+cs[2])/8
        covariance=probs[3]-q1*q2
        assert abs(probs[3]-expected)<1e-12
        assert abs(covariance-math.sin(math.pi/d)**2/(4*d))<1e-12
        assert covariance>0
        correlations=dict(single_wrong_probability=q1,joint_wrong_probability=probs[3],
                          fresh_reference_product_prediction=q1*q2,actual_error_covariance=covariance)
    return dict(ladder_maximum=top,uses=m,initial_guard=guard,
                matrix_unit_outcome_checks=checked,maximum_shared_phase_formula_difference=maximum,
                actual_ghz_wrong_parity_probability=wrong,shared_reference_correlations=correlations)


def ground_depletion_check(top,m):
    b,d=packet(top,m);size=top+1
    rho=[[b[n]*b[k] for k in range(size)] for n in range(size)]
    initial_var=sum((.2*n-.1*top)**2*b[n]**2 for n in range(size))
    history=[]
    for j in range(1,m+1):
        assert abs(rho[0][0])<1e-13
        rho=[[.5*rho[n][k]+(.5*rho[n+1][k+1] if n<top and k<top else 0)
              for k in range(size)] for n in range(size)]
        expected=[[0.]*size for _ in range(size)]
        for k in range(j+1):
            prob=math.comb(j,k)/2**j
            shifted=[b[n+k] if n+k<size else 0. for n in range(size)]
            for n in range(size):
                for p in range(size):expected[n][p]+=prob*shifted[n]*shifted[p]
        assert max(abs(rho[n][p]-expected[n][p]) for n in range(size) for p in range(size))<1e-13
        mean=sum(.2*n*rho[n][n] for n in range(size))
        var=sum((.2*n-mean)**2*rho[n][n] for n in range(size))
        c1=sum(rho[n+1][n] for n in range(top))
        fidelity=sum(b[n]*rho[n][p]*b[p] for n in range(size) for p in range(size))
        assert abs(mean-(.1*top-.1*j))<1e-12
        assert abs(var-(initial_var+.01*j))<1e-12
        assert abs(c1-overlap(b,1))<1e-12
        assert abs(fidelity-sum(math.comb(j,k)/2**j*overlap(b,k)**2 for k in range(j+1)))<1e-12
        history.append(dict(use=j,reservoir_mean_energy=mean,energy_variance=var,
                            adjacent_coherence=c1,fidelity_with_initial_reference=fidelity))
    bottom=rho[0][0]
    assert abs(bottom-2**(-m)*b[m]**2)<1e-13 and bottom>0
    # The next fresh-ground readout meets a REAL unmatched boundary block.
    # It remains complete; mean energy transfer and detector statistics change.
    previous_mean=sum(.2*n*rho[n][n] for n in range(size))
    next_rho=[[.5*rho[n][k]+(.5*rho[n+1][k+1] if n<top and k<top else 0)
               +(.5*bottom if n==0 and k==0 else 0) for k in range(size)] for n in range(size)]
    assert abs(sum(next_rho[n][n] for n in range(size))-1)<1e-12
    next_mean=sum(.2*n*next_rho[n][n] for n in range(size))
    assert abs(next_mean-previous_mean+.1*(1-bottom))<1e-12
    return dict(ladder_maximum=top,planned_uses=m,updates=history,
                bottom_population_after_planned_uses=bottom,
                next_ground_readout_zero_label_bias=bottom/2,
                next_ground_readout_system_energy_gain=.1*(1-bottom))


def resource(top,m,tau,k):
    b,d=packet(top,m);c1=overlap(b,1);cm=overlap(b,m)
    for j in range(2*m+1):assert abs(overlap(b,j)-overlap_formula(d,j))<1e-12
    epsilon=min(1.,math.pi**2/2*m*m*(1-c1))
    lower=(1-cm)/2
    one_use=(1-overlap(b,2))/4+(1-c1)/2
    fresh_sum=m*one_use
    if m>=4:assert lower>fresh_sum
    assert 0<=lower<=epsilon
    length=1+7*m;sumsq=length*(length+1)*(2*length+1)/6
    tau_max=2*tau;z=2*tau_max
    log_boundary=math.log(2)+k*(1+math.log(z/k))
    assert k>z and log_boundary<math.log(1e-12)
    pending=(math.sqrt(sumsq)/tau+1e-12)**2
    source=(1/tau+1e-12)**2
    assert pending<1
    complete=pending+(1-pending)*epsilon
    omega=.1;gamma=1/64;wg=4096.;max_top=2048
    nu_hi=math.sqrt(.25-8*.05**2/3);nu_lo=math.sqrt(.25-8*.25**2/3)
    center=wg*(1+(nu_hi+nu_lo)/2);width=wg*(nu_hi-nu_lo)/2
    ec=center-omega*max_top
    low=ec-2*gamma-m*omega;high=ec+2*gamma+2*omega*top+m*omega
    assert center-width<low<high<center+width and low>0
    inverses=0
    for hop in (-2*gamma,0.,2*gamma):
        for q in (0,top//2,top,top+m):
            energy=ec+hop-m*omega+2*omega*q
            nu=energy/wg-1;p=math.sqrt(3/8*(.25-nu*nu))
            assert .05<p<.25
            assert abs(wg*(1+math.sqrt(.25-8*p*p/3))-energy)<1e-8
            inverses+=1
    return dict(ladder_maximum_level=top,ladder_dimension=top+1,readouts=m,
                guard=m,effective_sine_denominator=d,adjacent_coherence=c1,
                ghz_parity_overlap=cm,completed_joint_instrument_error_upper=epsilon,
                fresh_reference_sum_of_one_use_error_bounds=fresh_sum,
                fresh_reference_ghz_wrong_parity_probability=(1-c1**m)/2,
                completed_joint_instrument_error_lower=lower,
                clock_positions=k,program_length=length,
                clock_readout_window=[tau/gamma,tau_max/gamma],
                clock_boundary_log_norm_bound=log_boundary,
                clock_noncompletion_probability_bound=pending,
                source_pending_probability_bound=source,complete_joint_record_error_upper=complete,
                reservoir_initial_mean_energy=omega*top,reservoir_maximum_energy=2*omega*top,
                all_ground_input_mean_reservoir_depletion=m*omega,
                all_ground_input_reservoir_fidelity_after_uses=sum(math.comb(m,j)/2**m*overlap(b,j)**2 for j in range(m+1)),
                necessary_ground_input_use_capacity_at_marginal_error_point01=top/(1-2*.01),
                fixed_system_frequency=omega,fixed_clock_hopping=gamma,
                fixed_source_excitation_energy=ec,gravitational_frequency=wg,
                cosmological_constant=-4*wg*wg/3,gravitational_radial_level=0,
                scalar_positive_band=[.05,.25],total_matter_energy_lower_bound=low,
                total_matter_energy_upper_bound=high,
                gravitational_margin=min(low-(center-width),center+width-high),
                physical_root_dimension=k*(top+1)*2**(8*m),
                gravitational_inverse_checks=inverses)


def run():
    guarded=[joint_instrument_check(12,2,2),joint_instrument_check(18,3,3)]
    breached=joint_instrument_check(8,2,1)
    assert breached['maximum_shared_phase_formula_difference']>1e-6
    return dict(status='passed',guarded_joint_instrument_checks=guarded,
                unguarded_boundary_counterexample=breached,
                exact_updated_reservoir_checks=[ground_depletion_check(12,2),ground_depletion_check(18,3)],
                cases=[resource(n,m,t,k) for n,m,t,k in ((128,2,1024,32768),(512,4,4096,131072),(2048,8,16384,524288))],
                scope=['Same finite reservoir reused, full outcome histories retained; no fresh-state replacement.',
                       'Exact guarded common-phase channel identity is not a prior over interrogation times.',
                       'Joint entangled-input error and explicit error correlations differ from marginal visibility.',
                       'Planned-use guard has a real initial preparation cost; unguarded boundary dynamics are retained.',
                       'One source/clock program executes all readouts without reset; finite retention window only.',
                       'No arbitrary adaptive reuse, source/refill pump, reset engine or completed phenomenal constitution.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: shared finite-reference reuse, correlated joint instrument, depletion and constrained resource bounds')
    print(path)
