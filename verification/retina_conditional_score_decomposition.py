#!/usr/bin/env python3
"""Decompose phase-conditional held-out score gains against shuffled trials.

A descriptive exploratory reanalysis, not causal identification or a new
shuffling methodology. Requires NumPy/SciPy. See accompanying report.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import re
import numpy as np
from scipy.special import logsumexp
from scipy.optimize import minimize

ROOT=Path(__file__).resolve().parent.parent
DATA=ROOT/'sources/uploads/Data_Spike_Trains.txt'
PRIOR=ROOT/'verification/retina_spike_maxent_audit.json'
LAST=ROOT/'verification/retina_stimulus_phase_control.json'
EXPECTED='1bcf28d8ef2bd23663760a4232fd247495c0805714a2a9a7bf78b8af5ec37a54'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(DATA)==EXPECTED
prior=json.loads(PRIOR.read_text()); last=json.loads(LAST.read_text())
assert prior['source_sha256']==last['source_sha256']==EXPECTED
assert last['prior_receipt_sha256']==sha(PRIOR)
names=[]; raw={}
for line in DATA.read_text().splitlines():
    if re.fullmatch(r'c\d+_bush2_spks',line):
        name=line; assert name not in raw
        names.append(name); raw[name]=[]
    elif line.strip(): raw[name].append(float(line))
assert len(names)==40 and sum(map(len,raw.values()))==172521
X=np.zeros((120,1325,40),dtype=np.uint8)
for i,name in enumerate(names):
    idx=np.floor(np.asarray(raw[name])/.02).astype(int)
    assert np.all((idx>=0)&(idx<120*1325))
    X.reshape(-1,40)[idx,i]=1
assert int(X.sum())==prior['source_total_binary_spike_bins']
train=X[:100]; test=X[100:]
S=((np.arange(1024)[:,None] >> np.arange(10)) & 1).astype(float)
pairs=list(combinations(range(10),2))
F=np.column_stack([S,*[S[:,i]*S[:,j] for i,j in pairs]])
ln2=np.log(2.0)

def moments(a):
    f=a.reshape(-1,10).astype(float)
    return np.r_[f.mean(axis=0),[(f[:,i]*f[:,j]).mean() for i,j in pairs]]

def shuffled_moments(a):
    """Exact independent whole-trial-permutation expected features.

    At each phase, each cell's independently sampled trial is marginally
    uniform, with replacement *across cells*. Self-trial matches are allowed.
    """
    p=a.mean(axis=0)
    return np.r_[p.mean(axis=0),[(p[:,i]*p[:,j]).mean() for i,j in pairs]]

# Finite-sample sanity: 2 cells cofire in two out of four trials; independent
# whole-label shuffles give 1/4 coincidence, vs 1/2 observed, 1/6 off-diagonal.
toy=np.zeros((4,1,10),np.uint8); toy[:2,0,:2]=1
m=moments(toy); ms=shuffled_moments(toy)
assert np.isclose(m[10],.5) and np.isclose(ms[10],.25)
rng=np.random.default_rng(89373)
samp=[]
for _ in range(3000):
    x=np.empty_like(toy)
    for i in range(10): x[:,:,i]=toy[rng.permutation(4),:,i]
    samp.append(moments(x)[10])
assert abs(np.mean(samp)-ms[10])<.025


def fit_group(ids,alpha,ridge):
    tr=train[:,:,ids].astype(float); te=test[:,:,ids].astype(float)
    p=(tr.sum(axis=0)+alpha)/(100+2*alpha)
    base=np.log(p)@S.T+np.log1p(-p)@(1-S).T
    target=moments(tr)
    def obj(v):
        logits=base+(F@v)[None,:]
        logz=logsumexp(logits,axis=1)
        mean=(np.exp(logits-logz[:,None]).mean(axis=0)@F)
        return float(logz.mean()-target@v+.5*ridge*(v@v)),mean-target+ridge*v
    def field_obj(v):
        value,grad=obj(np.r_[v,np.zeros(45)])
        return value,grad[:10]
    opts={'maxiter':600,'gtol':1e-8,'ftol':1e-12,'maxls':40}
    f=minimize(field_obj,np.zeros(10),jac=True,method='L-BFGS-B',options=opts)
    full=minimize(obj,np.r_[f.x,np.zeros(45)],jac=True,method='L-BFGS-B',options=opts)
    assert f.success and full.success
    assert np.max(np.abs(obj(full.x)[1]))<2e-5 and np.max(np.abs(field_obj(f.x)[1]))<2e-5
    z_field=logsumexp(base+(S@f.x)[None,:],axis=1)
    z_full=logsumexp(base+(F@full.x)[None,:],axis=1)
    delta=np.r_[full.x[:10]-f.x,full.x[10:]]
    norm=float(np.mean(z_full-z_field))
    def gain(a): return float((moments(a)@delta-norm)/ln2)
    obs=gain(te)
    expected=float((shuffled_moments(te)@delta-norm)/ln2)
    # Restricted independent permutations preserve each cell's phase rates
    # within contiguous five-repeat blocks, accommodating block-level drift.
    block_reference=np.mean([shuffled_moments(te[i:i+5]) for i in range(0,20,5)],axis=0)
    block_expected=float((block_reference@delta-norm)/ln2)
    excess=obs-expected
    # This exact identity is model-specific: score is linear in sufficient
    # statistics and per-phase normalizers do not depend on trial labels.
    assert abs(excess-float((moments(te)[10:]-shuffled_moments(te)[10:])@full.x[10:]/ln2))<1e-12
    assert abs((obs-block_expected)-float((moments(te)[10:]-block_reference[10:])@full.x[10:]/ln2))<1e-12
    blocks=[gain(te[i:i+5]) for i in range(0,20,5)]
    assert np.isclose(np.mean(blocks),obs)
    return {'alpha':alpha,'ridge':ridge,'observed_gain_bits_per_bin':obs,
            'shuffle_expected_gain_bits_per_bin':expected,
            'excess_over_shuffle_expectation_bits_per_bin':excess,
            'within_five_repeat_blocks_shuffle_expected_gain_bits_per_bin':block_expected,
            'excess_over_within_block_shuffle_bits_per_bin':obs-block_expected,
            'five_repeat_block_gains_bits_per_bin':blocks,
            'max_penalized_gradient':float(np.max(np.abs(obj(full.x)[1]))),
            'pair_theta':full.x[10:], 'delta':delta,'norm':norm, 'te':te}

rows=[]
for g in range(5):
    ids=[names.index(s) for s in prior['groups'][g]['cells']]
    assert prior['groups'][g]['cells']==last['ten_cell_predictive_scores'][g]['cells']
    settings=[(.5,.001),(.05,.001),(1.0,.001),(.5,.0001),(.5,.01)]
    results=[]
    for a,r in settings:
        result=fit_group(ids,a,r)
        te=result.pop('te'); delta=result.pop('delta'); norm=result.pop('norm'); result.pop('pair_theta')
        if a==.5 and r==.001:
            assert abs(result['observed_gain_bits_per_bin']-last['ten_cell_predictive_scores'][g]['conditional_pairwise_gain_over_field_calibrated_bits_per_bin'])<3e-7
            # Check exact expectation numerically; diagnostic only, not a p-value.
            samples=[]
            for _ in range(200):
                sh=np.empty_like(te)
                for i in range(10): sh[:,:,i]=te[rng.permutation(20),:,i]
                assert np.array_equal(sh.sum(axis=0),te.sum(axis=0))
                samples.append(float((moments(sh)@delta-norm)/ln2))
            result['monte_carlo_shuffle_mean']=float(np.mean(samples))
            result['monte_carlo_shuffle_min']=float(np.min(samples))
            result['monte_carlo_shuffle_max']=float(np.max(samples))
            result['monte_carlo_shuffle_standard_deviation']=float(np.std(samples))
            assert abs(np.mean(samples)-result['shuffle_expected_gain_bits_per_bin'])<.0002
        results.append(result)
    rows.append({'cells':prior['groups'][g]['cells'],'settings':results})
# Familiar observational-equivalence counterexample, not a model of retina.
# L is fair, independent noisy copies each have accuracy q. Compare to a fair
# X with Y copying it at probability .75. Both yield the same joint table.
q=(1+1/np.sqrt(2))/2
latent=np.array([[.5*(q*q+(1-q)**2),q*(1-q)],
                 [q*(1-q),.5*(q*q+(1-q)**2)]])
directed=np.array([[.375,.125],[.125,.375]])
assert np.allclose(latent,directed) and np.isclose(latent.sum(),1)
mi=float(np.sum(latent*np.log2(latent/.25)))
# do(X=1) leaves L and Y unperturbed in the common-cause model.
assert np.isclose(.5*q+.5*(1-q),.5)
assert np.isclose(mi,.75*np.log2(1.5)+.25*np.log2(.5))

out={'status':'passed','source_sha256':EXPECTED,'previous_receipt_sha256':sha(LAST),
     'prior_receipt_sha256':sha(PRIOR),'seed':89373,
     'protocol':{'fit':'same 100 presumed train repeats, 20 test repeats, 20ms bins; five previously selected groups; exact 1024-state conditional model',
                 'reference':'independent per-phase Beta(alpha,alpha) rates, 10 field offsets versus 10 fields plus 45 pair terms, common L2 ridge on all offsets',
                 'shuffle_expectation':'exact independent per-cell whole-trial permutation expectation, 20 test repeats; same-trial matches allowed',
                 'monte_carlo':'200 label permutations per group for baseline only, shuffles are not independent biological replicates',
                 'sensitivities':'baseline alpha=.5 ridge=.001; vary alpha .05 and 1 and ridge .0001 and .01 one at a time',
                 'blocks':'four sequential nonoverlapping blocks of five heldout repeats, predictors fitted once on first 100 repeats; exact expectation of independent within-block whole-trial permutations'},
     'groups':rows,
     'toy_observational_equivalence':{'both_joint_tables':latent.tolist(),
       'conditional_correlation_score_bits':mi,
       'prob_y_1_under_do_x_1_common_cause':.5,
       'prob_y_1_under_do_x_1_directed':.75,
       'scope':'toy causal models, not a retinal fit'},
     'limitations':'exploratory, same recording/movie, unverified phase and repeat count, no unseen stimulus or intervention; alpha/ridge sensitivity is not exhaustive; permutation variability is not a biological confidence interval; test blocks and groups are dependent; joint latent states and nonstationarity can mimic correlations.'}
(ROOT/'verification/retina_conditional_score_decomposition.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
