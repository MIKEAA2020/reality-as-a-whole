"""Finite energy-conserving reference exchange with correlation transport.

Exact small-register pump and two-readout channels; large clock/resource cases
are analytic bound evaluations. No discarded pump or implicit fresh reset.
"""
import cmath
import json
import math
from pathlib import Path
if __package__:
    from .reused_reference_clock import packet, overlap
    from .fixed_gap_source_clock import amplitudes, reduced
else:
    from reused_reference_clock import packet, overlap
    from fixed_gap_source_clock import amplitudes, reduced


def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def maxdiff(a,b):return max(abs(a[i][j]-b[i][j]) for i in range(len(a)) for j in range(len(a)))


def partial_exchange_checks():
    top=4;d=top+1;rsize=2;b,_=packet(top,1)
    psi=[[complex(math.sin((n+1)*(r+2)),math.cos((n+2)*(r+1))) for r in range(rsize)] for n in range(d)]
    norm=math.sqrt(sum(abs(z)**2 for row in psi for z in row));psi=[[z/norm for z in row] for row in psi]
    sigma=[[psi[n][r]*psi[p][s].conjugate() for p in range(d) for s in range(rsize)] for n in range(d) for r in range(rsize)]
    marginal_r=[[sum(psi[n][r]*psi[n][s].conjugate() for n in range(d)) for s in range(rsize)] for r in range(rsize)]
    tauid=[[b[n]*b[p]*int(r==s) for p in range(d) for s in range(rsize)] for n in range(d) for r in range(rsize)]
    target=[[b[n]*b[p]*marginal_r[r][s] for p in range(d) for s in range(rsize)] for n in range(d) for r in range(rsize)]
    st=mm(sigma,tauid);ts=mm(tauid,sigma)
    initial_b_energy=sum(.2*n*sum(abs(psi[n][r])**2 for r in range(rsize)) for n in range(d))
    initial_c_energy=sum(.2*n*b[n]*b[n] for n in range(d))
    cases=[]
    for label,cosine,sine in [('identity',1.,0.),('partial',math.cos(.37),math.sin(.37)),
                               ('half',math.sqrt(.5),math.sqrt(.5)),('full',0.,1.)]:
        u=[[complex(cosine*(i==j))-1j*sine*int(i//d==j%d and i%d==j//d)
            for j in range(d*d)] for i in range(d*d)]
        for i in range(d*d):
            for j in range(d*d):
                inner=sum(u[k][i].conjugate()*u[k][j] for k in range(d*d))
                assert abs(inner-(i==j))<1e-12
                ei=.2*(i//d+i%d);ej=.2*(j//d+j%d)
                assert abs((ei-ej)*u[i][j])<1e-12
        if label=='full':
            twice=mm(u,u)
            assert max(abs(twice[i][j]+int(i==j)) for i in range(d*d) for j in range(d*d))<1e-12
        v=[[[cosine*psi[n][r]*b[p]-1j*sine*psi[p][r]*b[n] for r in range(rsize)]
             for p in range(d)] for n in range(d)]
        assert abs(sum(abs(z)**2 for row in v for col in row for z in col)-1)<1e-12
        br=[[sum(v[n][c][r]*v[p][c][s].conjugate() for c in range(d))
             for p in range(d) for s in range(rsize)] for n in range(d) for r in range(rsize)]
        cr=[[sum(v[c][n][r]*v[c][p][s].conjugate() for c in range(d))
             for p in range(d) for s in range(rsize)] for n in range(d) for r in range(rsize)]
        expected=[[cosine*cosine*sigma[i][j]+sine*sine*target[i][j]+
                   1j*cosine*sine*(st[i][j]-ts[i][j]) for j in range(d*rsize)] for i in range(d*rsize)]
        assert maxdiff(br,expected)<1e-12
        oldr=[[sum(br[n*rsize+r][n*rsize+s] for n in range(d)) for s in range(rsize)] for r in range(rsize)]
        assert maxdiff(oldr,marginal_r)<1e-12
        eb=sum(.2*n*sum(br[n*rsize+r][n*rsize+r].real for r in range(rsize)) for n in range(d))
        ec=sum(.2*n*sum(cr[n*rsize+r][n*rsize+r].real for r in range(rsize)) for n in range(d))
        assert abs(eb+ec-initial_b_energy-initial_c_energy)<1e-12
        naive=[[cosine*cosine*sigma[i][j]+sine*sine*target[i][j] for j in range(d*rsize)] for i in range(d*rsize)]
        discrepancy=maxdiff(br,naive)
        if label=='half':assert discrepancy>.001
        if label=='full':
            assert maxdiff(br,target)<1e-12 and maxdiff(cr,sigma)<1e-12
        cases.append(dict(exchange=label,formula_matrix_entries=(d*rsize)**2,
                          unitarity_column_pairs_checked=d**4,energy_commutator_entries_checked=d**4,
                          omitted_commutator_max_entry_error=discrepancy,
                          reset_decoupling_error_upper=min(1.,cosine*cosine+abs(cosine*sine)),
                          working_energy=eb,pump_energy=ec,
                          exact_full_correlation_transport=(label=='full')))
    return dict(pump_dimension=d,minimum_universal_pump_dimension=d,cases=cases)


def ground_partial_pump(top=12,uses=2):
    b,_=packet(top,uses);size=top+1
    tau=[[b[n]*b[p] for p in range(size)] for n in range(size)]
    rho=[[0j]*size for _ in range(size)]
    for k in range(uses+1):
        weight=math.comb(uses,k)/2**uses
        shifted=[b[n+k] if n+k<size else 0. for n in range(size)]
        for n in range(size):
            for p in range(size):rho[n][p]+=weight*shifted[n]*shifted[p]
    rt=mm(rho,tau);tr=mm(tau,rho)
    out=[[.5*rho[i][j]+.5*tau[i][j]+.5j*(rt[i][j]-tr[i][j]) for j in range(size)] for i in range(size)]
    old=sum(.2*n*rho[n][n].real for n in range(size));new=sum(.2*n*out[n][n].real for n in range(size))
    assert abs(new-old-.5*uses*.1)<1e-12
    coherence=sum(out[n+1][n] for n in range(top))
    assert abs(coherence.imag)>1e-5
    assert abs(coherence.real-overlap(b,1))<1e-12
    return dict(ladder_maximum=top,ground_readouts_before_pump=uses,
                old_mean_energy=old,partially_replenished_mean_energy=new,
                restored_energy_fraction=.5,adjacent_coherence_real=coherence.real,
                adjacent_coherence_imaginary=coherence.imag,
                phase_bias_radians=cmath.phase(coherence))


def readout(v,system,outcome,top):
    dim=len(v);size=top+1;mask=1<<(1-system);sign=1 if outcome==0 else -1
    out=[[[z/2 for z in row] for row in part] for part in v]
    for s in range(dim):
        e=int(bool(s&mask))
        for n in range(size):
            if e==0 and n>0:t,p=s^mask,n-1
            elif e==1 and n<top:t,p=s^mask,n+1
            else:t,p=s,n
            assert s.bit_count()+n==t.bit_count()+p
            for c in range(size):out[t][p][c]+=sign*v[s][n][c]/2
    return out


def two_block_checks(top=8):
    b,_=packet(top,2);size=top+1;dim=4
    one={(d,r,s):reduced(amplitudes(r,b,d),amplitudes(s,b,d))
         for d in range(2) for r in range(2) for s in range(2)}
    results=[]
    for label,cosine,sine in [('none',1.,0.),('partial',math.sqrt(.5),math.sqrt(.5)),('full',0.,1.)]:
        vs={}
        for r in range(dim):
            for d in range(dim):
                v=[[[0j]*size for _ in range(size)] for _ in range(dim)]
                v[r]=[[b[n]*b[c] for c in range(size)] for n in range(size)]
                v=readout(v,0,d>>1,top)
                v=[[[cosine*v[s][n][c]-1j*sine*v[s][c][n] for c in range(size)]
                    for n in range(size)] for s in range(dim)]
                v=readout(v,1,d&1,top);vs[d,r]=v
        maximum=0.;checks=0
        for r in range(dim):
            for s in range(dim):
                trace=0j
                for d in range(dim):
                    vr=vs[d,r];vw=vs[d,s]
                    for e in range(dim):
                        for f in range(dim):
                            actual=sum(vr[e][n][c]*vw[f][n][c].conjugate() for n in range(size) for c in range(size))
                            expected=one[d>>1,r>>1,s>>1][e>>1][f>>1]*one[d&1,r&1,s&1][e&1][f&1]
                            maximum=max(maximum,abs(actual-expected))
                            if e==f:trace+=actual
                    checks+=1
                assert abs(trace-(r==s))<1e-12
        if label=='full':assert maximum<1e-12
        else:assert maximum>1e-5
        probs=[]
        for d in range(dim):
            probs.append(sum(abs(sum(vs[d,r][e][n][c] for r in range(dim))/2)**2
                             for e in range(dim) for n in range(size) for c in range(size)))
        q1=probs[2]+probs[3];q2=probs[1]+probs[3]
        covariance=probs[3]-q1*q2
        if label=='full':assert abs(covariance)<1e-12
        results.append(dict(exchange=label,joint_matrix_unit_outcome_checks=checks,
                            factorized_channel_max_entry_difference=maximum,
                            record_error_covariance_on_product_inputs=covariance))
    return results


def resource(blocks,top=512,total_readouts=8):
    assert total_readouts%blocks==0
    g=total_readouts//blocks;pumps=blocks-1
    b,d=packet(top,g)
    eps=min(1.,math.pi**2/2*g*g*(1-overlap(b,1)))
    reference=min(1.,blocks*eps)
    tau=16384.;k=524288;gamma=1/64;omega=.1
    length=1+7*total_readouts+pumps
    sumsq=length*(length+1)*(2*length+1)/6
    log_boundary=math.log(2)+k*(1+math.log(4*tau/k))
    assert log_boundary<math.log(1e-12)
    pending=(math.sqrt(sumsq)/tau+1e-12)**2
    complete=pending+(1-pending)*reference
    wg=4096.;nuhi=math.sqrt(.25-8*.05**2/3);nulo=math.sqrt(.25-8*.25**2/3)
    center=wg*(1+(nuhi+nulo)/2);width=wg*(nuhi-nulo)/2
    ec=center-.1*2048
    low=ec-2*gamma-total_readouts*omega
    high=ec+2*gamma+2*omega*blocks*top+total_readouts*omega
    assert center-width<low<high<center+width and low>0
    inverses=0
    for hop in (-2*gamma,0.,2*gamma):
        for q in (0,blocks*top//2,blocks*top,blocks*top+total_readouts):
            energy=ec+hop-total_readouts*omega+2*omega*q
            nu=energy/wg-1;p=math.sqrt(3/8*(.25-nu*nu))
            assert .05<p<.25
            assert abs(wg*(1+math.sqrt(.25-8*p*p/3))-energy)<1e-8
            inverses+=1
    return dict(readouts=total_readouts,readouts_per_block=g,initial_reference_packets=blocks,
                precharged_pumps=pumps,each_ladder_maximum=top,each_ladder_dimension=top+1,
                exact_full_exchange_pump_gates=pumps,per_block_reference_error_bound=eps,
                completed_all_block_instrument_error_bound=reference,
                ghz_wrong_parity_probability=(1-overlap(b,g)**blocks)/2,
                total_initial_reference_mean_energy=blocks*omega*top,
                total_initial_reference_max_energy=blocks*2*omega*top,
                restored_working_reference_energy_per_ground_block=g*omega,
                energy_lost_by_each_used_pump_on_ground_blocks=g*omega,
                total_ground_input_reference_energy_depletion=total_readouts*omega,
                remaining_reference_mean_energy_after_ground_readouts=blocks*omega*top-total_readouts*omega,
                necessary_ground_input_use_capacity_at_error_point01=blocks*top/.98,
                source_clock_positions=k,program_length=length,
                source_clock_window=[tau/gamma,2*tau/gamma],
                clock_noncompletion_probability_bound=pending,complete_operation_error_bound=complete,
                source_pending_probability_bound=(1/tau+1e-12)**2,
                fixed_source_excitation_energy=ec,fixed_system_frequency=omega,
                gravitational_frequency=wg,cosmological_constant=-4*wg*wg/3,
                scalar_positive_band=[.05,.25],radial_level=0,total_energy_lower_bound=low,
                total_energy_upper_bound=high,gravitational_margin=min(low-(center-width),center+width-high),
                gravitational_inverse_checks=inverses,
                physical_root_dimension=k*(top+1)**blocks*2**(8*total_readouts))


def equal_energy_comparison():
    big,d=packet(2048,8);small,e=packet(512,2)
    shared=math.pi**2/2*64*(1-overlap(big,1))
    pumped=4*(math.pi**2/2*4*(1-overlap(small,1)))
    shared_parity=(1-overlap(big,8))/2
    pumped_parity=(1-overlap(small,2)**4)/2
    assert pumped>shared and pumped_parity>shared_parity
    return dict(equal_initial_reference_mean_energy=204.8,
                one_large_shared_reference_ghz_error=shared_parity,
                four_packet_pump_scheme_ghz_error=pumped_parity,
                one_large_shared_reference_upper=shared,four_packet_pump_scheme_upper=pumped,
                optimized_energy_efficiency_claimed=False)


def run():
    return dict(status='passed',partial_exchange=partial_exchange_checks(),
                partial_ground_replenishment=ground_partial_pump(),two_readout_channel_tests=two_block_checks(),
                cases=[resource(b) for b in (1,2,4)],equal_mean_energy_comparison=equal_energy_comparison(),
                scope=['Explicit finite coherent pumps, physical unitary exchanges and all final pump states retained.',
                       'Full exchange moves old correlations to pump and exactly decouples working reference.',
                       'Channel factorization across blocks does not imply independent outcomes on entangled inputs.',
                       'Partial energy restoration can leave quantum memory and introduce reference phase bias.',
                       'All pumps enter one gravitational constraint and one finite source/clock program.',
                       'No pump regeneration, free cycle, optimal pump cost, adaptive protocol or completed phenomenal constitution.'])


if __name__=='__main__':
    result=run();path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: finite coherent pumps, exact correlation transport, complete block instruments and gravitational budget')
    print(path)
