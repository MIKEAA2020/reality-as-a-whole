#!/usr/bin/env python3
"""Exact weak-coupling, noisy-readout and hidden-state diagnostics; standard library."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math

import subject_factorization_redescription_gate as base

S = base.STATES
I = base.INDEX
p, q, t, eta = F(1, 4), F(1, 3), F(1, 16), F(1, 8)


def weak_kernel():
    out = []
    for x, y in S:
        qx = q + t * (1 - 2*q) * x
        out.append(tuple((p if a != x else 1-p) * (qx if b != y else 1-qx)
                         for a, b in S))
    return tuple(out)


def channel(eta):
    return tuple(tuple((eta if x != a else 1-eta) * (eta if y != b else 1-eta)
                       for a, b in S) for x, y in S)


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def tv(a, b):
    return sum(abs(x-y) for x, y in zip(a, b)) / 2


def project_simplex(v):
    # Positive-part normalization is an L1 nearest probability vector if sum(v)=1.
    w = tuple(max(F(0), a) for a in v)
    total = sum(w)
    assert sum(v) == 1 and total >= 1
    return tuple(a/total for a in w)


def prefix_policy_histories(K, policy):
    # Start x=0, y uniformly. Actions 0/1 clamp x, 2 leaves x unchanged.
    # At each step the action depends on the available observed x-history only.
    dist = {((0, y), (0,)): F(1, 2) for y in (0, 1)}
    for step in range(3):
        new = {}
        for (s, hist), weight in dist.items():
            a = policy[hist]
            clamped = (s[0] if a == 2 else a, s[1])
            for out in S:
                mass = weight * K[I[clamped]][I[out]]
                key = (out, hist + (out[0],))
                new[key] = new.get(key, F(0)) + mass
        dist = new
    by_history = {}
    for (_, hist), weight in dist.items():
        by_history[hist] = by_history.get(hist, F(0)) + weight
    return by_history


def main():
    K = weak_kernel()
    assert all(sum(row) == 1 and min(row) >= 0 for row in K)
    xp = base.observable_partition(tuple(s[0] for s in S))
    yp = base.observable_partition(tuple(s[1] for s in S))
    zp = base.observable_partition(tuple(s[0] ^ s[1] for s in S))
    pairs = {'XY': frozenset((xp, yp)), 'XZ': frozenset((xp, zp)),
             'YZ': frozenset((yp, zp))}
    scores = {name: base.defect(K, f) for name, f in pairs.items()}
    print('scores', scores)
    gap = min(scores['XZ'], scores['YZ']) - scores['XY']
    assert scores['XY'] == F(1, 48) and scores['XZ'] == F(1, 8)
    assert scores['YZ'] == F(527, 2304) and gap == F(5, 48)
    for perm in base.PERMS:
        kp = base.conjugate_kernel(K, perm)
        for candidate in pairs.values():
            assert base.defect(kp, base.permute_factors(candidate, perm)) == base.defect(K, candidate)

    M = channel(eta)
    one_inv = ((F(7, 6), F(-1, 6)), (F(-1, 6), F(7, 6)))
    Minv = tuple(tuple(one_inv[x][a] * one_inv[y][b] for a, b in S) for x, y in S)
    ident = matmul(M, Minv)
    assert ident == tuple(tuple(F(int(i == j)) for j in range(4)) for i in range(4))
    kappa = max(sum(abs(a) for a in row) for row in Minv)
    assert kappa == F(16, 9)
    observed = matmul(K, M)
    assert matmul(observed, Minv) == K
    # Make a valid deterministic perturbation of the output frequencies,
    # then invert and L1-project; this is one check, not a Monte Carlo study.
    observed_perturbed = []
    for row in observed:
        row = list(row)
        row[0] += F(1, 512)
        row[1] -= F(1, 512)
        assert min(row) >= 0 and sum(row) == 1
        observed_perturbed.append(tuple(row))
    observed_perturbed = tuple(observed_perturbed)
    estimated = tuple(project_simplex(row) for row in matmul(observed_perturbed, Minv))
    obs_delta = max(tv(a, b) for a, b in zip(observed, observed_perturbed))
    estimate_error = max(tv(a, b) for a, b in zip(K, estimated))
    assert obs_delta == F(1, 512) and estimate_error <= 2*kappa*obs_delta
    assert min((base.defect(estimated, f), name) for name, f in pairs.items())[1] == 'XY'
    # Local influence in y given x, at fixed y: exactly t(1-2q).
    cross = (q + t*(1-2*q)) - q
    assert cross == F(1, 48)
    delta = F(1, 512)
    epsilon = 2*kappa*delta
    assert epsilon == F(1, 144) and epsilon < gap/6 and epsilon < cross/2
    n = math.ceil(1024**2 * math.log(32/.05)/2)
    assert 32*math.exp(-2*n/1024**2) <= .05
    # Additional protocol: a calibrated y sensor reports on one quarter of
    # trials and independently flips its bit with probability 1/8.
    r = F(1, 4)
    visible_y0 = r * (eta + (1 - 2*eta) * q)
    visible_y1 = r * (eta + (1 - 2*eta) * (q + cross))
    observable_contrast = visible_y1 - visible_y0
    assert observable_contrast == F(1, 256)
    pair_n = math.ceil(4 * 256**2 * math.log(40))
    assert math.exp(-pair_n / (4*256**2)) <= .025

    # With only x observed and controlled, these three completions have the
    # same x transition law but differ in their full kernels and decompositions.
    K0 = base.kernel(p, q)
    enc = tuple(I[base.xy_to_uv(s)] for s in S)
    Kmix = base.conjugate_kernel(K, enc)
    mixscores = {name: base.defect(Kmix, f) for name, f in pairs.items()}
    assert min(mixscores, key=mixscores.get) == 'XZ'
    assert K0 != K and K != Kmix
    for candidate in (K0, K, Kmix):
        for x, y in S:
            for outx in (0, 1):
                assert sum(candidate[I[(x, y)]][I[(outx, outy)]] for outy in (0, 1)) == (p if outx != x else 1-p)
    # Exhaust deterministic adaptive policies through 3 transitions. Longer
    # histories follow by induction from the same x marginal for each x clamp.
    histories = [(0,)] + [(0,) + h for k in (1, 2) for h in product((0, 1), repeat=k)]
    policies = 0
    for actions in product((0, 1, 2), repeat=len(histories)):
        policy = dict(zip(histories, actions))
        a = prefix_policy_histories(K, policy)
        assert a == prefix_policy_histories(K0, policy) == prefix_policy_histories(Kmix, policy)
        policies += 1
    assert policies == 3**7
    receipt = {
        'status': 'passed',
        'weak_coupling_parameter': str(t),
        'one_step_conditional_y_flip_difference': str(cross),
        'factor_defects_weak_kernel': {k: str(v) for k, v in scores.items()},
        'unique_minimum_defect_gap': str(gap),
        'maximum_row_tv_error_for_guaranteed_unique_minimum_exclusive': str(gap/6),
        'readout_bit_flip_error': str(eta),
        'inverse_l1_operator_norm': str(kappa),
        'known_channel_estimated_frequency_tv_error': str(delta),
        'upper_bound_on_postprojection_row_tv_error': str(epsilon),
        'sufficient_n_per_prepared_state_for_joint_factor_and_coupling_margin': n,
        'sampling_union_failure_upper_bound': 32*math.exp(-2*n/1024**2),
        'one_deterministic_perturbation_reconstruction_tv_error': str(estimate_error),
        'occasional_y_readout_rate': str(r),
        'partial_readout_binary_contrast': str(observable_contrast),
        'partial_readout_two_arm_sufficient_n_per_arm': pair_n,
        'partial_readout_two_arm_per_hypothesis_error_bound': math.exp(-pair_n / (4*256**2)),
        'hidden_completion_factor_defects': {k: str(v) for k, v in mixscores.items()},
        'adaptive_deterministic_policies_checked_three_steps': policies,
        'scope': 'Exact finite diagnostics, strong full-state preparation and known independent readout assumed for recovery; hidden-state no-go only for specified x-only operations. No actual subjects, human data, quantum or gravity result.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
