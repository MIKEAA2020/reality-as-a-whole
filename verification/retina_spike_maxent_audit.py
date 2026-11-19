#!/usr/bin/env python3
"""Bounded held-out pairwise MaxEnt check on the supplied retinal spike trains.

Requires numpy and scipy. This is our independent implementation of a standard
maximum-entropy model, NOT original authors' code and NOT a full reproduction.
"""
from pathlib import Path
import hashlib, json, re
from itertools import combinations
import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'sources/uploads/Data_Spike_Trains.txt'
EXPECTED = '1bcf28d8ef2bd23663760a4232fd247495c0805714a2a9a7bf78b8af5ec37a54'
N, BINS, REPEATS, TRAIN = 40, 1325, 120, 100
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == EXPECTED
cells = {}
for line in DATA.read_text().splitlines():
    if re.fullmatch(r'c\d+_bush2_spks', line):
        assert line not in cells
        key = line
        cells[key] = []
    elif line.strip():
        cells[key].append(float(line))
assert len(cells) == N and sum(map(len, cells.values())) == 172521
for x in cells.values():
    assert all(0 <= t < 3180 for t in x)
    assert all(a <= b for a,b in zip(x,x[1:]))
names = list(cells)
# 120 repeat slots of 26.5 s; 20 ms bins divide each repeat exactly.
# Interpret the file as the 120-repeat subset described by Cocco & Monasson;
# trailing silent time cannot be ruled out from spike times alone.
X = np.zeros((REPEATS, BINS, N), dtype=np.uint8)
for col, name in enumerate(names):
    t = np.asarray(cells[name])
    # Assign on the absolute 20 ms grid, avoiding phase-reset floating drift.
    idx = np.floor(t / .020).astype(int)
    assert np.all((idx >= 0) & (idx < REPEATS * BINS))
    X.reshape(-1,N)[idx,col] = 1
assert X.sum() <= sum(map(len,cells.values()))

n = 10
states = ((np.arange(1 << n)[:,None] >> np.arange(n)) & 1).astype(np.float64)
pairs = list(combinations(range(n),2))
features = np.column_stack([states, *[states[:,i]*states[:,j] for i,j in pairs]])
assert features.shape == (1024,55)

def hist(d):
    codes = d.astype(np.int64) @ (1 << np.arange(n))
    return np.bincount(codes, minlength=1 << n).astype(float)/len(d)

def entropy(p):
    p = p[p>0]
    return float(-np.dot(p,np.log2(p)))

def analyze(ids):
    train=X[:TRAIN,:,ids].reshape(-1,n)
    test=X[TRAIN:,:,ids].reshape(-1,n)
    pt,pe=hist(train),hist(test)
    mu=pt@features
    p_single=mu[:n]
    assert np.all((p_single>0)&(p_single<1))
    x0=np.r_[np.log(p_single/(1-p_single)),np.zeros(len(pairs))]
    def objective(x):
        z=features@x
        lz=logsumexp(z)
        prob=np.exp(z-lz)
        return float(lz-mu@x), features.T@prob-mu
    fit=minimize(objective,x0,jac=True,method='L-BFGS-B',
                 options={'maxiter':3000,'ftol':1e-14,'gtol':1e-9,'maxls':40,'maxcor':30})
    logp2=features@fit.x-logsumexp(features@fit.x)
    p2=np.exp(logp2)
    logp1=states@np.log(p_single)+(1-states)@np.log1p(-p_single)
    p1=np.exp(logp1)
    err=float(np.max(np.abs(p2@features-mu)))
    assert np.isclose(p1.sum(),1) and np.isclose(p2.sum(),1) and err<2e-5
    hp1=entropy(p1); hp2=entropy(p2); ht=entropy(pt)
    train_info=hp1-ht
    htest=entropy(pe)
    ce1=float(-pe@logp1/np.log(2)); ce2=float(-pe@logp2/np.log(2))
    return {'cells':[names[i] for i in ids], 'optimizer_success':bool(fit.success),
            'optimizer_message':str(fit.message), 'iterations':int(fit.nit),
            'max_training_constraint_error':err,
            'training_total_correlation_plugin_bits_per_bin':train_info,
            'training_pairwise_fraction_plugin':(hp1-hp2)/train_info,
            'heldout_entropy_plugin_bits_per_bin':htest,
            'heldout_independent_cross_entropy_bits_per_bin':ce1,
            'heldout_pairwise_cross_entropy_bits_per_bin':ce2,
            'heldout_gain_bits_per_bin':ce1-ce2,
            'heldout_gain_over_saturated_plugin_gap':(ce1-ce2)/(ce1-htest)}

rng=np.random.default_rng(20240620)
groups=[list(range(10))]+[sorted(rng.choice(N,size=n,replace=False).tolist()) for _ in range(4)]
rows=[analyze(ids) for ids in groups]
# As in the source, compare simultaneous firing distribution to a fitted
# product-Bernoulli baseline for all 40 cells, without assuming identical rates.
train=X[:TRAIN].reshape(-1,N); test=X[TRAIN:].reshape(-1,N)
rates=train.mean(axis=0)
expected=np.array([1.0])
for p in rates: expected=np.convolve(expected,[1-p,p])
k=test.sum(axis=1)
observed=np.bincount(k,minlength=N+1)/len(k)
assert abs(expected.sum()-1)<1e-12
out={'status':'passed','source_sha256':EXPECTED,
     'source_cells':len(cells),'source_total_spikes':sum(map(len,cells.values())),
     'source_max_spike_time_seconds':max(max(x) for x in cells.values()),
     'source_total_binary_spike_bins':int(X.sum()),
     'protocol':{'movie_repeat_seconds':26.5,'assumed_complete_repeats':REPEATS,
       'train_first_repeats':TRAIN,'test_last_repeats':REPEATS-TRAIN,
       'bin_ms':20,'bins_per_repeat':BINS,'ten_cell_groups':len(groups),
       'group_selection':'first 10 listed then four numpy RNG groups, seed 20240620; selected before observing computed fits',
       'model':'55-parameter unregularized pairwise binary maximum entropy, exactly enumerating 1024 patterns',
       'interpretation':'same repeated movie; held-out repeats are not a new stimulus, animal, experiment, or causal intervention; plugin entropy is not bias corrected'},
     'groups':rows,
     'all_40_heldout_simultaneous_spikes_at_least_5':{
       'observed_probability':float(observed[5:].sum()),
       'independent_model_probability':float(expected[5:].sum())},
     'limitations':'exploratory finite-group check; no confidence intervals or estimator-bias correction; source sorting/stimulus timing not independently audited; may differ from original paper methods, groups, sample selection and temporal analysis.'}
(ROOT/'verification/retina_spike_maxent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
