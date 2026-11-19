#!/usr/bin/env python3
"""Synthetic spacetime, identity, and sequential-Bell controls; not a QPV security proof."""
import itertools
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
C=299_792_458.0


def logsumexp(vals):
    m=max(vals)
    return m+math.log(sum(math.exp(v-m) for v in vals))


def binomial_tail(n,k,q):
    if k>n: return 0.0
    vals=[math.lgamma(n+1)-math.lgamma(j+1)-math.lgamma(n-j+1)
          +j*math.log(q)+(n-j)*math.log1p(-q) for j in range(k,n+1)]
    return math.exp(logsumexp(vals))


def geometry():
    # Symmetric vacuum/light-speed toy. Time zero is challenge release.
    L=200.0; h=10.0; T=(L+2*h)/C
    lo=L-C*T/2; hi=C*T/2
    assert abs(lo-90)<1e-10 and abs(hi-110)<1e-10
    center=L/2
    honest_finish=2*max(center,L-center)/C
    # Colluders stationed next to the two verifiers receive the opposite
    # challenge after L/c, compute XOR, respond locally with negligible latency.
    colluder_finish=L/C
    assert honest_finish<=T and colluder_finish<=T
    assert not (lo<=0<=hi) and not (lo<=L<=hi)
    transcripts=[]
    for a,b in itertools.product((0,1), repeat=2):
        z=a^b
        honest=(a,b,z,z,honest_finish,honest_finish)
        colluders=(a,b,z,z,colluder_finish,colluder_finish)
        assert honest==colluders
        transcripts.append({'challenge_A':a,'challenge_B':b,'response_A':z,'response_B':z})
    # Device P can serve either a nearby or a remote principal without changing
    # any physical input/output in this idealized classical toy.
    assert len(transcripts)==4
    return {'verifier_separation_m':L,'single_station_region_m':[lo,hi],
            'deadline_ns':T*1e9,'honest_response_ns':honest_finish*1e9,
            'colluding_response_ns':colluder_finish*1e9,
            'colluders_at_m':[0,L],'matching_challenge_response_transcripts':len(transcripts),
            'scope':'ideal 1D synchronized toy; no optical fibres, experimental latencies, Bell condition, or security certificate'}


def sequential_bell():
    # Uniform independent CHSH settings; enumerate all local deterministic rules.
    wins=[]
    for a0,a1,b0,b1 in itertools.product((0,1),repeat=4):
        count=sum(((a0,a1)[x]^(b0,b1)[y])==x*y for x,y in itertools.product((0,1),repeat=2))
        wins.append(count/4)
    assert max(wins)==.75
    local=.75; q=(2+math.sqrt(2))/4
    lam=(4*q-3)/3
    win,loss=1+lam,1-3*lam
    assert 0<lam<1/3 and abs(local*win+(1-local)*loss-1)<1e-15
    assert q*win+(1-q)*loss>1
    n=2000; bits=64
    lw,ll=math.log2(win),math.log2(loss)
    k=math.ceil((bits-n*ll)/(lw-ll))
    while k<=n and k*lw+(n-k)*ll<bits: k+=1
    while k>0 and (k-1)*lw+(n-k+1)*ll>=bits: k-=1
    target=binomial_tail(n,k,q)
    local_tail=binomial_tail(n,k,local)
    alpha=2.0**(-bits)
    assert local_tail<=alpha
    return {'scope':'invented perfect CHSH game, not the paper\'s test factor, trial data, or QPV security reduction',
            'local_max_single_trial_win':local,'ideal_quantum_single_trial_win':q,
            'lambda':lam,'test_factor_win':win,'test_factor_loss':loss,
            'trials':n,'threshold_log2_product':bits,'minimum_wins_to_cross':k,
            'iid_quantum_hypothetical_pass_probability':target,
            'iid_optimal_local_pass_probability':local_tail,
            'adversary_class_soundness_upper_from_supermartingale':alpha,
            'quantum_expected_log2_product':n*(q*lw+(1-q)*ll)}


def main():
    out={'status':'passed','geometry_identity_control':geometry(),'sequential_test_factor_control':sequential_bell(),
         'limitation':'synthetic checks; no verification of real devices, experiments, security assumptions, persons, experiences, or paper-specific factors'}
    (ROOT/'verification/qpv_causal_records_gate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
