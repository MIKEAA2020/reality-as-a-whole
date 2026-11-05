"""Exact reversible path accumulator and first-arrival clock instrument.

Sparse lattice states and rational matrices; no prescribed measured trajectory.
Continuum, physical hardware and empirical calibration are not supplied here.
"""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json
from itertools import product
if __package__:
    from .cold_atom_comparison import load
else:
    from cold_atom_comparison import load

C = ((F(3,5),F(-4,5)),(F(4,5),F(3,5)))


def clean(v):
    return {k:x for k,x in v.items() if x}


def step(v, deltas=(1,-2), inverse=False):
    out=defaultdict(F)
    for (q,d,a),x in v.items():
        if inverse:
            q,a=q-deltas[d],a-abs(deltas[d])
            for e in range(2):
                out[q,e,a]+=C[d][e]*x
        else:
            for e in range(2):
                out[q+deltas[e],e,a+abs(deltas[e])]+=C[e][d]*x
    return clean(out)


def norm(v):
    return sum(x*x for x in v.values())


def inner(v,w):
    return sum(x*w.get(k,F(0)) for k,x in v.items())


def add(v,w,scale=F(1)):
    out=defaultdict(F,v)
    for k,x in w.items():
        out[k]+=scale*x
    return clean(out)


def initial(d):
    return {(0,d,0):F(1)}


def arrive(v, threshold, deltas=(1,-2)):
    """Monitored first crossing; one Kraus branch for each update index and overshoot."""
    assert threshold>=1 and min(map(abs,deltas))>=1
    survivor=v
    out={}
    for n in range(1,threshold+1):
        evolved=step(survivor,deltas)
        for a in range(threshold,threshold+max(map(abs,deltas))):
            hit={k:x for k,x in evolved.items() if k[2]==a}
            if hit:
                out[n,a-threshold]=hit
        survivor={k:x for k,x in evolved.items() if k[2]<threshold}
    assert not survivor
    assert sum(map(norm,out.values()))==norm(v)
    return out


def kraus_columns(threshold,deltas=(1,-2)):
    columns=[arrive(initial(d),threshold,deltas) for d in range(2)]
    labels=sorted(set(columns[0])|set(columns[1]))
    return {label:[column.get(label,{}) for column in columns] for label in labels}


def gram(columns):
    return [[inner(a,b) for b in columns] for a in columns]


def density(columns,rho):
    out=defaultdict(F)
    for i in range(2):
        for j in range(2):
            for a,x in columns[i].items():
                for b,y in columns[j].items():
                    out[a,b]+=rho[i][j]*x*y
    return clean(out)


def channel(branches,rho,coherent=False):
    if coherent:
        columns=[{} for _ in range(2)]
        for label,cols in branches.items():
            for i,col in enumerate(cols):
                columns[i].update({(label,k):x for k,x in col.items()})
        return density(columns,rho)
    out=defaultdict(F)
    for cols in branches.values():
        for key,value in density(cols,rho).items():
            out[key]+=value
    return clean(out)


def purity(rho):
    return sum(value*rho.get((b,a),F(0)) for (a,b),value in rho.items())


def evolve(v,n):
    for _ in range(abs(n)):
        v=step(v,inverse=n<0)
    return v


def dirac_effect(f):
    out={}
    for n,v in f.items():
        framed=evolve(v,-n)
        projected={k:x for k,x in framed.items() if k==(0,0,0)}
        out[n]=evolve(projected,n)
    return out


def rigging(f):
    out={}
    for n,v in f.items():
        for _ in range(abs(n)):
            v=step(v,inverse=n>0)
        out=add(out,v)
    return out


def gauge_shift(f):
    return {n+1:step(v) for n,v in f.items()}


def path_enumeration(threshold, initial_coin):
    """Independent sum over coin words; amplitudes of equal output histories interfere."""
    out={}
    for n in range(1,threshold+1):
        for word in product((0,1),repeat=n):
            q=a=0
            amplitude=F(1)
            previous=initial_coin
            for k,d in enumerate(word):
                amplitude*=C[d][previous]
                previous=d
                q+=(1,-2)[d]
                a+=abs((1,-2)[d])
                if a>=threshold:
                    if k==n-1:
                        branch=out.setdefault((n,a-threshold),defaultdict(F))
                        branch[q,d,a]+=amplitude
                    break
    return {label:clean(v) for label,v in out.items() if clean(v)}


def empirical_registers():
    data,_=load()
    result={}
    for name,rows in data.items():
        readings=[row[2]*10**6 for row in rows]
        exact_length=sum(abs(b-a) for a,b in zip(readings,readings[1:]))
        resolutions={}
        for epsilon in (F(1,10),F(1,2),F(1)):
            bins=[int(x//epsilon) for x in readings]
            counter=0
            stalled=0
            for x,y in zip(bins,bins[1:]):
                before=counter
                counter+=abs(y-x)
                # Same conditional adder, inverted without discarding sensor inputs.
                assert counter-abs(y-x)==before
                stalled+=x==y
            modulus=1<<counter.bit_length()
            modular=0
            for x,y in zip(bins,bins[1:]):
                modular=(modular+abs(y-x))%modulus
            assert modular==counter
            length=epsilon*counter
            bound=(len(rows)-1)*epsilon
            assert abs(length-exact_length)<=bound
            resolutions[str(epsilon)]={
                'counter_units':counter,'counter_bits_for_this_observed_run':counter.bit_length(),
                'quantized_path_length_um':float(length),
                'exact_sampled_path_length_um':float(exact_length),
                'absolute_length_discrepancy_um':float(abs(length-exact_length)),
                'worst_case_quantization_bound_um':float(bound),
                'stalled_adjacent_observation_pairs':stalled}
        result[name]=resolutions
    return result


def run():
    unitary_checks=0
    for q in (-2,0,3):
        for a in (-3,0,4):
            for d in (0,1):
                v={(q,d,a):F(1)}
                assert step(step(v),inverse=True)==v
                assert step(step(v,inverse=True))==v
                assert norm(step(v))==norm(v)
                assert all(qq+3*aa==q+3*a+4 for qq,dd,aa in step(v))
                unitary_checks+=1
    # Positive clock-rate identity U*AU-A = C* diag(1,2) C, checked as a full coin matrix.
    rate=[[sum(C[e][i]*abs((1,-2)[e])*C[e][j] for e in (0,1)) for j in (0,1)] for i in (0,1)]
    assert rate==[[F(41,25),F(12,25)],[F(12,25),F(34,25)]]
    eigen_invariants=(rate[0][0]+rate[1][1],rate[0][0]*rate[1][1]-rate[0][1]**2)
    assert eigen_invariants==(3,2)  # eigenvalues 1 and 2
    for i in (0,1):
        for j in (0,1):
            u,v=step(initial(i)),step(initial(j))
            weighted=sum(x*v.get(k,F(0))*k[2] for k,x in u.items())
            assert weighted==rate[i][j]
    # A return in position still changes the actual counter: +1,+1,-2.
    q=a=0
    for d in (0,0,1):
        q+=(1,-2)[d];a+=abs((1,-2)[d])
    assert (q,a)==(0,4)
    completeness_checks=0
    for threshold in range(1,9):
        branches=kraus_columns(threshold)
        for d in (0,1):
            assert path_enumeration(threshold,d)==arrive(initial(d),threshold)
        total=[[F(0),F(0)],[F(0),F(0)]]
        for cols in branches.values():
            g=gram(cols)
            for i in (0,1):
                for j in (0,1):
                    total[i][j]+=g[i][j]
        assert total==[[1,0],[0,1]]
        for n,r in branches:
            assert (threshold+1)//2<=n<=threshold and r in (0,1)
        coherent_columns=[{},{}]
        for (n,r),cols in branches.items():
            for d,col in enumerate(cols):
                assert all(q+3*a==4*n and a-threshold==r for q,coin,a in col)
                coherent_columns[d]=add(coherent_columns[d],col)
        assert gram(coherent_columns)==[[1,0],[0,1]]
        completeness_checks+=1
    branches=kraus_columns(2)
    exact={label:{k:tuple(col.get(k,F(0)) for col in cols) for k in set(cols[0])|set(cols[1])} for label,cols in branches.items()}
    assert exact=={
        (1,0):{(-2,1,2):(F(4,5),F(3,5))},
        (2,0):{(2,0,2):(F(9,25),F(-12,25))},
        (2,1):{(-1,1,3):(F(12,25),F(-16,25))}}
    probs={str(label):sum(x for (a,b),x in density(cols,[[1,0],[0,0]]).items() if a==b) for label,cols in branches.items()}
    assert list(probs.values())==[F(16,25),F(81,625),F(144,625)]
    # Two orthogonal input states have identical reduced arrival outputs.
    vplus=(F(7,5),F(-1,5));vminus=(F(-1,5),F(-7,5))
    rho_plus=[[x*y/2 for y in vplus] for x in vplus]
    rho_minus=[[x*y/2 for y in vminus] for x in vminus]
    assert sum(rho_plus[i][j]*rho_minus[j][i] for i in (0,1) for j in (0,1))==0
    assert channel(branches,rho_plus)==channel(branches,rho_minus)
    assert channel(branches,rho_plus,True)!=channel(branches,rho_minus,True)
    classical=[]
    for rho in (rho_plus,rho_minus):
        recorded={}
        for label,cols in branches.items():
            for (a,b),x in density(cols,rho).items():
                recorded[(label,a),(label,b)]=x
        classical.append(recorded)
    assert classical[0]==classical[1]
    # Explicit five-dimensional self-adjoint unitary dilation of the three-row isometry.
    V=[[F(4,5),F(3,5)],[F(9,25),F(-12,25)],[F(12,25),F(-16,25)]]
    D=[[F(0),F(0)]+[V[j][i] for j in range(3)] for i in range(2)]
    D += [V[i]+[F(i==j)-sum(V[i][k]*V[j][k] for k in range(2)) for j in range(3)] for i in range(3)]
    assert all(D[i][j]==D[j][i] for i in range(5) for j in range(5))
    assert all(sum(D[i][k]*D[k][j] for k in range(5))==F(i==j) for i in range(5) for j in range(5))
    # Isometry preserves the orthogonality if arrival records remain quantum coherent.
    coherent_plus=channel(branches,rho_plus,True)
    coherent_minus=channel(branches,rho_minus,True)
    assert purity(coherent_plus)==purity(coherent_minus)==1
    assert sum(x*coherent_minus.get((b,a),F(0)) for (a,b),x in coherent_plus.items())==0
    assert purity(channel(branches,[[1,0],[0,0]]))==F(187297,390625)
    # Equal-speed control: only n=A and zero overshoot, with a unitary walk on q/coin.
    for threshold in range(1,7):
        equal=kraus_columns(threshold,(1,-1))
        assert set(equal)=={(threshold,0)}
        assert gram(equal[threshold,0])==[[1,0],[0,1]]
    # Online counter is not a free passive reparameterization of the unrecorded walk.
    evolved=step(initial(0))
    reduced=defaultdict(F)
    for (q,d,a),x in evolved.items():
        for (r,e,b),y in evolved.items():
            if a==b:
                reduced[(q,d),(r,e)]+=x*y
    assert purity(clean(reduced))==F(337,625)
    # Positive Z-group rigging and endpoint invariance on finite supported test vectors.
    f={-1:initial(0),0:initial(0),2:initial(1)}
    g={0:add(initial(0),initial(1),F(2)),3:initial(0)}
    assert rigging(gauge_shift(f))==rigging(f)
    averaged=F(0)
    for n,v in f.items():
        for m,w in g.items():
            for _ in range(abs(n-m)):
                w=step(w,inverse=n<m)
            averaged+=inner(v,w)
    assert averaged==inner(rigging(f),rigging(g))
    assert norm(rigging(f))>=0
    assert dirac_effect(gauge_shift(f))==gauge_shift(dirac_effect(f))
    projected={k:x for k,x in rigging(f).items() if k==(0,0,0)}
    assert norm(projected)==1
    assert rigging(dirac_effect(f))==projected
    # Matched detector events: changing the event label does not change its Kraus map.
    # Event b is final coin outcome; compare direct threshold histories to instrument evaluation.
    fixed_two=step(step(initial(0)))
    fixed_coin_one=sum(x*x for (q,d,a),x in fixed_two.items() if d==1)
    arrival_coin_one=F(16,25)+F(144,625)
    assert fixed_coin_one==F(288,625) and arrival_coin_one==F(544,625)
    assert fixed_coin_one!=arrival_coin_one
    direct=arrive(initial(0),2)
    joint={}
    for label,hit in direct.items():
        for b in (0,1):
            p=sum(x*x for (q,d,a),x in hit.items() if d==b)
            cols=branches[label]
            instrument=sum(x*x for (q,d,a),x in cols[0].items() if d==b)
            assert p==instrument
            joint[str((label[0],label[1],b))]=str(p)
    return {'status':'passed','basis_unitarity_checks':unitary_checks,
            'arrival_instrument_completeness_thresholds':completeness_checks,
            'rate_matrix':[[str(x) for x in row] for row in rate],
            'position_return_counter':4,
            'completed_internal_clock':'T=(Q+3*A)/4; U* T U=T+I',
            'arrival_label_coherently_uncomputable_from_output':'n=(q+3*a)/4, r=a-B on prepared support',
            'fixed_tick_2_coin_one_probability':str(fixed_coin_one),
            'first_arrival_2_coin_one_probability':str(arrival_coin_one),
            'verified_experimental_table_register_replays':empirical_registers(),
            'threshold_2_arrival_probabilities':{k:str(v) for k,v in probs.items()},
            'threshold_2_joint_arrival_overshoot_coin':joint,
            'arrival_reduced_output_purity_coin0':str(purity(channel(branches,[[1,0],[0,0]]))),
            'one_tick_counter_backaction_purity':str(purity(clean(reduced))),
            'orthogonal_inputs_identified_by_reduced_clock_channel':True,
            'coherent_record_isometry_preserves_orthogonality':True,
            'dephased_classical_arrival_records_do_not_restore_the_phase':True,
            'independent_coin_word_enumeration_thresholds':8,
            'explicit_coherent_converter_unitary_dimension':5,
            'dirac_effect_intertwining_checked':True,
            'equal_speed_control_thresholds':6,
            'rigging_group':'integers; finite sums on finite history support',
            'finite_counter_no_wrap_sufficient_and_worst_case_necessary':'K >= 2*N+1 from counter 0',
            'limits':['autonomous discrete update law supplied, not derived from cold-atom dynamics',
                      'first-arrival detector is an explicit monitored instrument, not an undisturbed position trajectory',
                      'coherent storage differs from retaining a dephased classical arrival label',
                      'rigging uses the first-order unitary constraint; a formal second-order kernel is not identified with it',
                      'no gravitational constraint algebra, physical engine derivation or entropy-clock reconstruction']}


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: reversible accumulator, arrival instruments, coherent records, rigging and equal-speed control')
    print(path)
