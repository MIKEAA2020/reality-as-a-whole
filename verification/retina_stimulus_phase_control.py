#!/usr/bin/env python3
"""Repeated-stimulus controls for the supplied 40-cell retina data.

Uses the already documented 120-repeat timing assumption. Trial shuffling is a
published antecedent in Schneidman et al. (2006), not a new method or an
intervention. Requires numpy; does not import the earlier audit's side effects.
"""
from pathlib import Path
import hashlib, json, re
import numpy as np
from scipy.special import logsumexp
from scipy.optimize import minimize
from itertools import combinations

ROOT=Path(__file__).resolve().parent.parent
DATA=ROOT/'sources/uploads/Data_Spike_Trains.txt'
PRIOR=ROOT/'verification/retina_spike_maxent_audit.json'
EXPECTED='1bcf28d8ef2bd23663760a4232fd247495c0805714a2a9a7bf78b8af5ec37a54'
assert hashlib.sha256(DATA.read_bytes()).hexdigest()==EXPECTED
prior=json.loads(PRIOR.read_text())
assert prior['source_sha256']==EXPECTED
assert prior['protocol']['train_first_repeats']==100 and prior['protocol']['test_last_repeats']==20

cells={}
for line in DATA.read_text().splitlines():
    if re.fullmatch(r'c\d+_bush2_spks',line):
        assert line not in cells
        key=line; cells[key]=[]
    elif line.strip():
        cells[key].append(float(line))
assert len(cells)==40 and sum(map(len,cells.values()))==172521
names=list(cells); X=np.zeros((120,1325,40),dtype=np.uint8)
for i,name in enumerate(names):
    t=np.asarray(cells[name]); idx=np.floor(t/.020).astype(int)
    assert np.all((idx>=0)&(idx<120*1325))
    X.reshape(-1,40)[idx,i]=1
assert int(X.sum())==prior['source_total_binary_spike_bins']
train,test=X[:100],X[100:]


def at_least_k_poisson_binomial(probs,k):
    """Each row has independent heterogeneous Bernoulli probabilities."""
    probs=np.atleast_2d(probs)
    d=np.ones((len(probs),1))
    for i in range(probs.shape[1]):
        p=probs[:,i,None]
        d=np.pad(d*(1-p),((0,0),(0,1)))+np.pad(d*p,((0,0),(1,0)))
    assert np.allclose(d.sum(axis=1),1)
    return float(d[:,k:].sum(axis=1).mean())


def pair_means(arr):
    """Original and all off-diagonal trial-paired coincidence expectations."""
    r,t,n=arr.shape
    z=arr.astype(float); flat=z.reshape(r*t,n)
    count=flat.T@flat
    phase=z.sum(axis=0)
    original=count/(r*t)
    # Average over all r*(r-1) unequal-trial pairings at each phase.
    cross=(phase.T@phase-count)/(t*r*(r-1))
    ind=np.triu_indices(n,1)
    return original[ind],cross[ind]

# Synthetic invariants: shared phase can cause perfect synchrony without
# cross-cell noise dependence; same-trial matching creates residual in another.
a=np.zeros((4,2,2),np.uint8); a[:,0,:]=1
u,v=pair_means(a); assert np.allclose(u,v) and np.allclose(u,.5)
b=np.zeros((4,1,2),np.uint8); b[:2,0,:]=1
u,v=pair_means(b); assert np.allclose(u,.5) and np.allclose(v,1/6)
assert np.isclose(at_least_k_poisson_binomial([[.5,.5]],2),.25)

original,cross=pair_means(test)
mean_pair_original=float(original.mean()); mean_pair_cross=float(cross.mean())
assert np.all(original>=0) and np.all(cross>=-1e-14)
first_a,first_b=pair_means(test[:10]); last_a,last_b=pair_means(test[10:])
threshold=5
original_events=float(np.mean(test.sum(axis=2)>=threshold))
base=at_least_k_poisson_binomial(train.mean(axis=(0,1)),threshold)
phase_base=at_least_k_poisson_binomial(train.mean(axis=0),threshold)
assert abs(base-prior['all_40_heldout_simultaneous_spikes_at_least_5']['independent_model_probability'])<1e-14

# Random whole-trial label permutations per cell: exact preservation of each
# cell's phase profile and each entire trial train, but same-trial collisions
# occur for pairs (1/20 in expectation). Not a permutation significance test.
rng=np.random.default_rng(44721); surrogate=[]
for _ in range(200):
    shuffled=np.empty_like(test)
    for i in range(40):
        shuffled[:,:,i]=test[rng.permutation(20),:,i]
    assert np.array_equal(shuffled.sum(axis=0),test.sum(axis=0))
    surrogate.append(float(np.mean(shuffled.sum(axis=2)>=threshold)))

# Proper held-out log scores. Jeffreys smoothing prevents log(0). The direct
# phase score uses known movie-phase; the phase-mixture marginalizes it out,
# so its score has the same information as the stationary pairwise model.
models=[]
phase_counts=train.sum(axis=0).astype(float)
states=((np.arange(1024)[:,None] >> np.arange(10)) & 1).astype(float)
pairs=list(combinations(range(10),2))
features=np.column_stack([states,*[states[:,i]*states[:,j] for i,j in pairs]])
assert features.shape==(1024,55)
ridge=.001  # Fixed exploratory regularization strength; no test-set tuning.
for prev in prior['groups']:
    ids=[names.index(s) for s in prev['cells']]
    y=test[:,:,ids].astype(float)
    codes=y.reshape(-1,10).astype(np.int64)@(1 << np.arange(10))
    sensitivity={}
    for alpha in (.05,.5,1.0):
        p=(phase_counts[:,ids]+alpha)/(100+2*alpha)
        ce=float(-np.mean(np.sum(y*np.log2(p)+(1-y)*np.log2(1-p),axis=2)))
        log_phase=np.log(p)@states.T+np.log1p(-p)@(1-states).T
        log_mix=logsumexp(log_phase,axis=0)-np.log(len(p))
        assert np.isclose(np.exp(log_mix).sum(),1)
        ce_mix=float(-np.mean(log_mix[codes])/np.log(2))
        sensitivity[str(alpha)]={'conditional_bits_per_bin':ce,'phase_mixture_bits_per_bin':ce_mix}
    ce=sensitivity['0.5']['conditional_bits_per_bin']
    ce_mix=sensitivity['0.5']['phase_mixture_bits_per_bin']
    # Conditional pairwise model: phase-dependent independent reference times
    # a common exponential tilt (10 field offsets, 45 pair terms). Fitting uses
    # only the same 100 training repeats and a fixed L2 penalty.
    p=(phase_counts[:,ids]+.5)/101.0
    base_log=np.log(p)@states.T+np.log1p(-p)@(1-states).T
    tr=train[:,:,ids].reshape(-1,10).astype(float)
    target=np.r_[tr.mean(axis=0),np.array([(tr[:,i]*tr[:,j]).mean() for i,j in pairs])]
    def objective(theta):
        weights=base_log+(features@theta)[None,:]
        norm=logsumexp(weights,axis=1)
        distribution=np.exp(weights-norm[:,None])
        mean_features=distribution.mean(axis=0)@features
        return float(norm.mean()-target@theta+ridge*(theta@theta)/2), mean_features-target+ridge*theta
    def field_objective(field):
        val,gradient=objective(np.r_[field,np.zeros(45)])
        return val,gradient[:10]
    field_fit=minimize(field_objective,np.zeros(10),jac=True,method='L-BFGS-B',
                       options={'maxiter':600,'gtol':1e-8,'ftol':1e-12,'maxls':40})
    field_delta=features[:,:10]@field_fit.x
    field_norm=logsumexp(base_log+field_delta[None,:],axis=1)
    phases=np.broadcast_to(np.arange(1325),(20,1325))
    test_codes=codes.reshape(20,1325)
    field_ce=float(-np.mean(base_log[phases,test_codes]+field_delta[test_codes]-field_norm[phases])/np.log(2))
    assert np.max(np.abs(field_objective(field_fit.x)[1]))<2e-5
    fit=minimize(objective,np.r_[field_fit.x,np.zeros(45)],jac=True,method='L-BFGS-B',
                 options={'maxiter':600,'gtol':1e-8,'ftol':1e-12,'maxls':40})
    val,grad=objective(fit.x)
    assert np.isfinite(val) and np.max(np.abs(grad))<2e-5
    delta=features@fit.x
    norms=logsumexp(base_log+delta[None,:],axis=1)
    logq=base_log[None,:,:]+delta[None,None,:]-norms[None,:,None]
    phases=np.broadcast_to(np.arange(1325),(20,1325))
    test_codes=codes.reshape(20,1325)
    coupled_ce=float(-np.mean(logq[0,phases,test_codes])/np.log(2))
    models.append({'cells':prev['cells'],
        'phase_conditional_independent_cross_entropy_bits_per_bin':ce,
        'phase_conditional_independent_field_calibrated_cross_entropy_bits_per_bin':field_ce,
        'phase_conditional_pairwise_cross_entropy_bits_per_bin':coupled_ce,
        'conditional_pairwise_gain_over_field_calibrated_bits_per_bin':field_ce-coupled_ce,
        'conditional_pairwise_gain_over_uncalibrated_bits_per_bin':ce-coupled_ce,
        'conditional_field_fit_optimizer_success':bool(field_fit.success),
        'conditional_fit_iterations':int(fit.nit),
        'conditional_fit_optimizer_success':bool(fit.success),
        'conditional_fit_max_penalized_gradient':float(np.max(np.abs(grad))),
        'conditional_fit_pair_terms_positive':int(np.sum(fit.x[10:]>0)),
        'conditional_fit_pair_terms_negative':int(np.sum(fit.x[10:]<0)),
        'phase_mixture_cross_entropy_bits_per_bin':ce_mix,
        'stationary_pairwise_cross_entropy_bits_per_bin':prev['heldout_pairwise_cross_entropy_bits_per_bin'],
        'stationary_independent_cross_entropy_bits_per_bin':prev['heldout_independent_cross_entropy_bits_per_bin'],
        'mixture_minus_pairwise_bits_per_bin':ce_mix-prev['heldout_pairwise_cross_entropy_bits_per_bin'],
        'phase_minus_pairwise_bits_per_bin':ce-prev['heldout_pairwise_cross_entropy_bits_per_bin'],
        'symmetric_beta_sensitivity':sensitivity})

out={'status':'passed','source_sha256':EXPECTED,
     'prior_receipt_sha256':hashlib.sha256(PRIOR.read_bytes()).hexdigest(),
     'protocol':{'sample':'same 40 cells and presumed first 120 movie repeats as prior audit',
      'train_repeats':100,'test_repeats':20,'bin_ms':20,'bins_per_repeat':1325,
      'phase_control':'100-trial training per-phase independent Bernoulli rates; unsmoothed for K>=5 and symmetric Beta(alpha,alpha) posterior means for log scores with alpha=0.05,0.5,1; phase-mixture marginalizes phase uniformly',
      'conditional_pairwise':'alpha=0.5 base with 10 time-independent field offsets and 45 pair tilts; compares against 10-field-only calibrated model; L2 coefficient 0.001, all estimated on 100 train repeats; no test-set tuning',
      'shuffle':'200 independent within-test random permutations of whole trials for each cell; same-trial matches between any pair occur about 1/20 on average',
      'pairwise_cross_trial':'exact mean over all unequal trial pairs at same phase; no sampling or smoothing',
      'warning':'same stimulus, one recording; no randomized stimulus or neuron intervention, no biological confidence intervals'},
     'heldout_40_cell_k_at_least_5':{'observed':original_events,'stationary_independent':base,
       'phase_conditionally_independent_from_training':phase_base,
       'trial_shuffle_mean':float(np.mean(surrogate)),'trial_shuffle_min':float(np.min(surrogate)),
       'trial_shuffle_max':float(np.max(surrogate))},
     'heldout_pair_coincidence':{'pairs':len(original),'observed_mean':mean_pair_original,
       'different_trial_same_phase_mean':mean_pair_cross,'difference':mean_pair_original-mean_pair_cross,
       'positive_differences':int(np.sum(original>cross)),
       'first_ten_repeat_difference':float(np.mean(first_a-first_b)),
       'last_ten_repeat_difference':float(np.mean(last_a-last_b))},
     'ten_cell_predictive_scores':models,
     'scope':'These are descriptive, exploratory estimates; finite-trial mismatches, drift, phase error and latent inputs may contribute to residual correlations. More successful prediction with phase information does not prove a common-input mechanism or subject structure. Shuffle range is Monte Carlo variation, not a confidence interval or p-value.'}
(ROOT/'verification/retina_stimulus_phase_control.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
