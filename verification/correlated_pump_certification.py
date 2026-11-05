"""Imperfect/correlated finite pump sources and complete verification flags.

Analytic robustness/decoupling results: CORRELATED_PUMP_CERTIFICATION.md.
Small tests use exact finite amplitudes; large clock cases are bound evaluations.
"""
import cmath
import json
import math
from pathlib import Path
if __package__:
    from .finite_reference_pump import mm,maxdiff,readout
    from .reused_reference_clock import packet,overlap
else:
    from finite_reference_pump import mm,maxdiff,readout
    from reused_reference_clock import packet,overlap


def eig_real(a):
    a=[list(map(float,row)) for row in a];n=len(a)
    for _ in range(100*n*n):
        if n==1:break
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-14:break
        apq=a[p][q];tau=(a[q][q]-a[p][p])/(2*apq)
        t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+t*t);s=t*c
        app=a[p][p];aqq=a[q][q]
        for k in range(n):
            if k not in (p,q):
                x,y=a[k][p],a[k][q]
                a[k][p]=a[p][k]=c*x-s*y;a[k][q]=a[q][k]=s*x+c*y
        a[p][p]=app-t*apq;a[q][q]=aqq+t*apq;a[p][q]=a[q][p]=0.
    else:raise AssertionError('Jacobi did not converge')
    return [a[i][i] for i in range(n)]


def distance_real(a,b):
    return .5*sum(abs(x) for x in eig_real([[a[i][j]-b[i][j] for j in range(len(a))] for i in range(len(a))]))


def certificate_checks():
    witnesses=[]
    for epsilon in (1e-6,.001,.1):
        p=1-epsilon
        # Entangled source/rest witness on |b,0>, |orthogonal,1>, |b,1>.
        actual=[[p,math.sqrt(p*epsilon),0.],[math.sqrt(p*epsilon),epsilon,0.],[0.,0.,0.]]
        target=[[p,0.,0.],[0.,0.,0.],[0.,0.,epsilon]]
        dist=distance_real(actual,target)
        exact=(epsilon+math.sqrt(4*epsilon-3*epsilon*epsilon))/2
        assert abs(dist-exact)<1e-12
        assert dist<=math.sqrt(epsilon)+epsilon+1e-12 and dist>epsilon
        witnesses.append(dict(marginal_infidelity=epsilon,actual_decoupling_distance=dist,
                              certified_upper=min(1,math.sqrt(epsilon)+epsilon)))
    general=[]
    for eta in (.0001,.01,.1):
        weights=[[math.sin((p+1)*(r+2))+.3*math.cos(p+3*r) for r in range(2)] for p in range(1,8)]
        norm=math.sqrt(sum(x*x for row in weights for x in row))
        psi=[[math.sqrt(1-eta)*math.sqrt(.7),math.sqrt(1-eta)*math.sqrt(.3)]]
        psi += [[math.sqrt(eta)*x/norm for x in row] for row in weights]
        sigma=[[sum(psi[p][r]*psi[q][r] for r in range(2)) for q in range(8)] for p in range(8)]
        target=[[float(p==0 and q==0) for q in range(8)] for p in range(8)]
        defects=[sum(psi[p][r]**2 for p in range(8) if p&(1<<j) for r in range(2)) for j in range(3)]
        e=sum(defects)
        joint=[[psi[p][r]*psi[q][s] for q in range(8) for s in range(2)] for p in range(8) for r in range(2)]
        rest=[[sum(psi[p][r]*psi[p][s] for p in range(8)) for s in range(2)] for r in range(2)]
        product=[[rest[r][s] if p==0 and q==0 else 0. for q in range(8) for s in range(2)] for p in range(8) for r in range(2)]
        ds=distance_real(sigma,target);dr=distance_real(joint,product)
        assert eta<=e+1e-13 and ds<=math.sqrt(e)+1e-12 and dr<=math.sqrt(e)+e+1e-12
        general.append(dict(actual_joint_source_defect=eta,sum_of_local_infidelities=e,
                            source_product_distance=ds,source_rest_decoupling_distance=dr))
    # A CP initializer can correlate a nearly pure source with the system while
    # disturbing the system. Its marginal channel is dephasing, not identity.
    prep=[]
    for eps in (.001,.1):
        isometry=[[1.,0.],[0.,math.sqrt(1-eps)],[0.,0.],[0.,math.sqrt(eps)]]
        gram=[[sum(isometry[k][i]*isometry[k][j] for k in range(4)) for j in range(2)] for i in range(2)]
        assert maxdiff(gram,[[1.,0.],[0.,1.]])<1e-12
        defect=[[sum(isometry[k][i]*isometry[k][j] for k in (2,3)) for j in range(2)] for i in range(2)]
        assert maxdiff(defect,[[0.,0.],[0.,eps]])<1e-12
        for i in range(2):
            for j in range(2):
                reduced=[[sum(isometry[2*p+r][i]*isometry[2*p+t][j] for p in range(2)) for t in range(2)] for r in range(2)]
                expected=[[float(r==i and t==j)*(1 if i==j else math.sqrt(1-eps)) for t in range(2)] for r in range(2)]
                assert maxdiff(reduced,expected)<1e-12
        v=[1/math.sqrt(2),math.sqrt(1-eps)/math.sqrt(2),0.,math.sqrt(eps)/math.sqrt(2)]
        rho=[[v[i]*v[j] for j in range(4)] for i in range(4)]
        ideal=[[.5 if i<2 and j<2 else 0. for j in range(4)] for i in range(4)]
        marginal_error=(1-math.sqrt(1-eps))/2
        assert distance_real(rho,ideal)<=math.sqrt(eps)+eps+marginal_error
        prep.append(dict(uniform_source_infidelity_bound=eps,
                         actual_system_preparation_half_diamond_error=marginal_error,
                         source_system_distance_from_intended_input=distance_real(rho,ideal)))
    # Four source/anchor qubits: all-pass is (I+S01)(I+S23)/4.
    eta=.02
    tail=[math.sin(j+1) for j in range(1,16)]
    norm=math.sqrt(sum(x*x for x in tail))
    psi=[math.sqrt(1-eta)]+[math.sqrt(eta)*x/norm for x in tail]
    def exchange(index,a,b):
        return index^((1<<a)|(1<<b)) if ((index>>a)^(index>>b))&1 else index
    passed=[(psi[j]+psi[exchange(j,0,1)]+psi[exchange(j,2,3)]+psi[exchange(exchange(j,0,1),2,3)])/4 for j in range(16)]
    rejection=1-sum(x*x for x in passed)
    defect=sum(psi[j]**2*j.bit_count() for j in range(16))
    assert -1e-12<=rejection<=eta+1e-12 and eta<=defect
    return dict(verification_rejection_witness=dict(rejection_probability=rejection,joint_target_defect=eta,sum_local_defects=defect),
                entangled_sqrt_error_witnesses=witnesses,three_source_joint_checks=general,
                correlated_preparation_channel_witnesses=prep)


def probe_probabilities(b1,b2,top):
    size=top+1;probs=[]
    for d in range(4):
        v=[[[1j**s.bit_count()/2*b1[n]*b2[c] for c in range(size)] for n in range(size)] for s in range(4)]
        v=readout(v,0,d>>1,top)
        v=[[[-1j*v[s][c][n] for c in range(size)] for n in range(size)] for s in range(4)]
        v=readout(v,1,d&1,top)
        probs.append(sum(abs(z)**2 for part in v for row in part for z in row))
    assert abs(sum(probs)-1)<1e-12
    return probs


def correlated_phase_counterexample():
    top=8;alpha=.4;b,_=packet(top,2)
    states={s:[x*cmath.exp(1j*s*alpha*n) for n,x in enumerate(b)] for s in (-1,1)}
    cases={(s,t):probe_probabilities(states[s],states[t],top) for s in (-1,1) for t in (-1,1)}
    corr=[sum(cases[s,s][d] for s in (-1,1))/2 for d in range(4)]
    independent=[sum(cases[s,t][d] for s in (-1,1) for t in (-1,1))/4 for d in range(4)]
    for probs in (corr,independent):
        assert abs(probs[0]+probs[1]-.5)<1e-12 and abs(probs[0]+probs[2]-.5)<1e-12
    covariance=corr[0]-.25
    expected=overlap(b,1)**2*math.sin(alpha)**2/4
    assert abs(covariance-expected)<1e-12 and covariance>0
    f=abs(sum(b[n]*states[1][n] for n in range(top+1)))**2
    assert f<1
    size=top+1
    marginal=[[sum(states[s][n]*states[s][p].conjugate() for s in (-1,1))/2
               for p in range(size)] for n in range(size)]
    source_corr=[[sum(states[s][n]*states[s][c]*states[s][p].conjugate()*states[s][a].conjugate()
                      for s in (-1,1))/2 for p in range(size) for a in range(size)]
                 for n in range(size) for c in range(size)]
    source_ind=[[marginal[n][p]*marginal[c][a] for p in range(size) for a in range(size)]
                for n in range(size) for c in range(size)]
    reduced_corr=[[sum(source_corr[n*size+c][p*size+c] for c in range(size)) for p in range(size)] for n in range(size)]
    reduced_ind=[[sum(source_ind[n*size+c][p*size+c] for c in range(size)) for p in range(size)] for n in range(size)]
    assert maxdiff(reduced_corr,reduced_ind)<1e-12
    assert max(abs(source_corr[j][j]-source_ind[j][j]) for j in range(size*size))<1e-12
    swap_expect=sum(source_corr[n*size+c][c*size+n] for n in range(size) for c in range(size)).real
    swap_pass=(1+swap_expect)/2
    assert abs(swap_pass-1)<1e-12
    return dict(ladder_maximum=top,phase_offsets=[-alpha,alpha],identical_full_pump_marginals=True,
                identical_energy_statistics=True,pure_target_fidelity_of_each_marginal=f,
                unknown_correlated_anchor_swap_pass_probability=swap_pass,
                correlated_source_record_probabilities=corr,independent_source_record_probabilities=independent,
                correlated_record_covariance=covariance,independent_record_covariance=independent[0]-.25,
                record_distribution_total_variation=.5*sum(abs(a-b) for a,b in zip(corr,independent)))


def swap_test_instrument():
    top=4;size=top+1;rs=2;b,_=packet(top,1)
    psi=[[complex(math.sin((n+1)*(r+2)),math.cos((n+2)*(r+1))) for r in range(rs)] for n in range(size)]
    norm=math.sqrt(sum(abs(z)**2 for row in psi for z in row));psi=[[z/norm for z in row] for row in psi]
    sigma=[[psi[n][r]*psi[p][s].conjugate() for p in range(size) for s in range(rs)] for n in range(size) for r in range(rs)]
    rest=[[sum(psi[n][r]*psi[n][s].conjugate() for n in range(size)) for s in range(rs)] for r in range(rs)]
    tid=[[b[n]*b[p]*int(r==s) for p in range(size) for s in range(rs)] for n in range(size) for r in range(rs)]
    fresh=[[b[n]*b[p]*rest[r][s] for p in range(size) for s in range(rs)] for n in range(size) for r in range(rs)]
    st=mm(sigma,tid);ts=mm(tid,sigma)
    fidelity=sum(abs(sum(b[n]*psi[n][r] for n in range(size)))**2 for r in range(rs))
    total=[[0j]*(size*rs) for _ in range(size*rs)];totalenergy=0.;cases=[]
    for sign in (1,-1):
        v=[[[.5*(psi[n][r]*b[c]+sign*psi[c][r]*b[n]) for r in range(rs)] for c in range(size)] for n in range(size)]
        out=[[sum(v[n][c][r]*v[p][c][s].conjugate() for c in range(size))
              for p in range(size) for s in range(rs)] for n in range(size) for r in range(rs)]
        expected=[[(sigma[i][j]+fresh[i][j]+sign*(st[i][j]+ts[i][j]))/4 for j in range(size*rs)] for i in range(size*rs)]
        assert maxdiff(out,expected)<1e-12
        prob=sum(out[i][i].real for i in range(size*rs))
        assert abs(prob-(1+sign*fidelity)/2)<1e-12
        for i in range(size*rs):
            for j in range(size*rs):total[i][j]+=out[i][j]
        totalenergy+=sum(.2*(n+c)*abs(v[n][c][r])**2 for n in range(size) for c in range(size) for r in range(rs))
        conditional_rest=[[sum(out[n*rs+r][n*rs+s] for n in range(size))/prob for s in range(rs)] for r in range(rs)]
        cases.append(dict(sign=sign,probability=prob,formula_matrix_entries=(size*rs)**2,
                          conditional_old_record_max_entry_change=maxdiff(conditional_rest,rest)))
    assert maxdiff(total,[[(sigma[i][j]+fresh[i][j])/2 for j in range(size*rs)] for i in range(size*rs)])<1e-12
    oldenergy=sum(.2*n*sum(abs(psi[n][r])**2 for r in range(rs)) for n in range(size))+sum(.2*n*b[n]**2 for n in range(size))
    assert abs(totalenergy-oldenergy)<1e-12
    assert max(c['conditional_old_record_max_entry_change'] for c in cases)>1e-4
    return dict(initial_source_target_fidelity=fidelity,cases=cases,
                nonselective_source_state_change=maxdiff(total,sigma),complete_energy_conservation=True)


def resource(q):
    m=8;top=512;g=m//q;pumps=q-1;anchors=q;source_factors=2*q
    b,d=packet(top,g);epsref=min(1.,q*math.pi**2/2*g*g*(1-overlap(b,1)))
    eps_each=1e-8;e=source_factors*eps_each
    source_independent=min(1.,math.sqrt(e));source_correlated=min(1.,math.sqrt(e)+e)
    length=1+7*m+pumps+2*q
    tau=16384.;k=524288;gamma=1/64;omega=.1
    boundary_log=math.log(2)+k*(1+math.log(4*tau/k))
    assert boundary_log<math.log(1e-12)
    pending=(math.sqrt(length*(length+1)*(2*length+1)/6)/tau+1e-12)**2
    independent_error=pending+(1-pending)*min(1.,epsref+source_independent)
    correlated_state_error=pending+(1-pending)*min(1.,epsref+source_correlated)
    wg=8192.;nuhi=math.sqrt(.25-8*.05**2/3);nulo=math.sqrt(.25-8*.25**2/3)
    center=wg*(1+(nuhi+nulo)/2);width=wg*(nuhi-nulo)/2
    ec=center-.1*4096
    low=ec-2*gamma-m*omega;high=ec+2*gamma+2*omega*source_factors*top+m*omega
    assert center-width<low<high<center+width and low>0
    count=0
    for hop in (-2*gamma,0.,2*gamma):
        for charge in (0,source_factors*top//2,source_factors*top,source_factors*top+m):
            energy=ec+hop-m*omega+2*omega*charge
            nu=energy/wg-1;p=math.sqrt(3/8*(.25-nu*nu))
            assert .05<p<.25 and abs(wg*(1+math.sqrt(.25-8*p*p/3))-energy)<1e-8
            assert 8*wg*p/(3*nu)>0
            count+=1
    return dict(readouts=m,blocks=q,working_and_pump_ladders=q,verification_anchor_ladders=anchors,
                precharged_pumps=pumps,total_reference_anchor_factors=source_factors,
                each_ladder_dimension=top+1,each_target_infidelity_upper=eps_each,
                total_local_infidelity_upper=e,source_product_distance_upper=source_independent,
                source_rest_decoupling_distance_upper=source_correlated,
                ideal_completed_reference_error_bound=epsref,all_verification_flags_retained=True,
                verification_rejection_probability_upper=e,
                pending_or_verification_failure_upper=pending+(1-pending)*e,
                source_clock_positions=k,program_length_with_tests=length,
                readout_window=[tau/gamma,2*tau/gamma],clock_noncompletion_probability_bound=pending,
                source_independent_complete_instrument_error_bound=independent_error,
                correlated_state_error_against_actual_system_marginal=correlated_state_error,
                ideal_initial_reference_anchor_mean_energy=source_factors*omega*top,
                initial_reference_anchor_mean_energy_deviation_upper=source_factors*2*omega*top*math.sqrt(eps_each),
                initial_reference_anchor_maximum_energy=source_factors*2*omega*top,
                fixed_source_excitation_energy=ec,gravitational_frequency=wg,
                cosmological_constant=-4*wg*wg/3,scalar_positive_band=[.05,.25],radial_level=0,
                total_energy_lower_bound=low,total_energy_upper_bound=high,
                gravitational_margin=min(low-(center-width),center+width-high),
                gravitational_inverse_checks=count,physical_root_dimension=k*2**(8*m+q)*(top+1)**source_factors)


def run():
    return dict(status='passed',source_certificates=certificate_checks(),
                equal_marginal_counterexample=correlated_phase_counterexample(),
                complete_swap_test=swap_test_instrument(),cases=[resource(q) for q in (1,2,4)],
                scope=['Marginal fidelities to pure finite targets certify the whole batch without source-source independence.',
                       'System-correlated source statements preserve the actual system marginal; diamond claims need a CP initialization map.',
                       'Exact local marginals/energy statistics alone do not justify independent mixed sources.',
                       'Finite-anchor verification has backaction and retained pass/fail flags, not free noninvasive certification.',
                       'All reference/anchor energies and extra test gates enter the gravitational/source-clock budget.',
                       'No unmodelled finite-data guarantee, ideal phase anchor, pump regeneration or phenomenal constitution.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: correlated finite sources, pure-marginal certification, complete swap tests and gravitational budget')
    print(path)
