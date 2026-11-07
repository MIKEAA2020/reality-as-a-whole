#!/usr/bin/env python3
"""Conditional shared-reference uncertainty diagnostic for Banik ramp holdout.

Run: python verification/hubble_reference_uncertainty.py /path/to/hubFrct_2021
See EXPANDING_BEC_REFERENCE_UNCERTAINTY.md for assumptions and limitations.
No correction to the published MATLAB pipeline or gravity inference is claimed.
"""
import argparse
from collections import Counter
import hashlib
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
from matio import load_from_mat
import hubble_heldout as h

SEED = 20261107
DRAWS = 2000


def features(shots, projector):
    # Shape (shots, 3): total density, sine coefficient, cosine coefficient.
    return np.column_stack((shots.sum(axis=1), shots @ projector.T))


def mean_draws(rows, rng, weights=None):
    """Gaussian multiplier for mean; conditional covariance is sample_cov/n."""
    n = rows.shape[0]
    if n < 2:
        raise ValueError('Each group must have at least two observations')
    if weights is None:
        weights = rng.normal(size=(DRAWS, n))
    if weights.shape != (DRAWS, n):
        raise ValueError('Shared weights have incompatible shape')
    mean = np.mean(rows, axis=0)
    return mean + weights @ (rows - mean) / np.sqrt(n * (n-1))


def validate_multiplier():
    # Test covariance of a mean and paired reuse under a linear transformation.
    rows = np.array([[1., 2., 4.], [2., -1., 1.], [4., 3., 0.],
                     [-1., 4., 2.], [3., 1., 7.]])
    transform = np.array([[1., 0.2], [-0.5, 1.], [0.1, 0.7]])
    rng = np.random.default_rng(1847)
    weights = rng.normal(size=(DRAWS, len(rows)))
    a = mean_draws(rows, rng, weights)
    b = mean_draws(rows @ transform, rng, weights)
    empirical = np.cov(a.T, b.T, ddof=1)[:3, 3:]
    expected = np.cov(rows.T, ddof=1) @ transform / len(rows)
    rel = float(np.linalg.norm(empirical - expected)/np.linalg.norm(expected))
    if rel > 0.10:
        raise ValueError('Shared-multiplier covariance test failed')
    return {'relative_cross_covariance_frobenius_error': rel, 'max_allowed': 0.10}


def normalize(y, ref):
    if np.any(np.abs(ref[..., 0]) < 1e-8):
        raise ValueError('Near-zero reference total')
    return y[..., 1:] - (y[..., 0] / ref[..., 0])[..., None] * ref[..., 1:]


def load_dynamic(path, root, controls):
    data = load_from_mat(path)
    p = data['A'].properties
    if str(h.arr(p['dataRingType'])[0]) != 'All':
        return None
    times, t0, dur = h.arr(p['EvTime']), h.val(p['t_phn1']), h.val(p['t_exp'])
    end = t0 + dur
    runs, tm, raw = h.arr(data['Runs']), h.arr(data['time']), np.asarray(data['n1Ds']).T
    is_ph = np.isin(runs, h.arr(p['RunNos_phnEv']))
    is_init = np.isin(runs, h.arr(p['RunNos_ring_I']))
    is_ramp = np.isin(runs, h.arr(p['RunNos_ring_Exp']))
    if len(h.arr(p['RunNos_ring_F'])) or not np.any(is_init):
        raise ValueError('Unexpected reference configuration')
    angle = h.arr(p['AzAngle'])
    proj = np.linalg.pinv(np.column_stack((np.sin(angle), np.cos(angle))))
    order = np.argsort(runs[is_init])
    init_runs, init_raw = runs[is_init][order], raw[is_init][order]
    per_time = [raw[is_ph & (np.abs(tm-t) <= h.TOL)] for t in times]
    if any(len(group) < 2 for group in per_time):
        raise ValueError('At least two phonon shots per time needed')
    exp_times = h.arr(p['n1D_ringExpTimes'])
    exp_raw = [raw[is_ramp & (np.abs(tm-t) <= h.TOL)] for t in exp_times]
    if any(len(group) < 2 for group in exp_raw):
        raise ValueError('At least two ramp reference shots per time needed')
    # Replicate the source fallback: equal weighting of post-transition time
    # slices, not weighting by their numbers of shots.
    post = np.flatnonzero(times >= end)
    if len(post) == 0:
        raise ValueError('Missing final reference')
    means_full = np.array([np.mean(group, axis=0) for group in per_time])
    final_full = np.mean(means_full[post], axis=0)
    initial_full = np.mean(init_raw, axis=0)
    final_error = np.max(np.abs(final_full-h.arr(p['n1D_ringF_avg'])))
    initial_error = np.max(np.abs(initial_full-h.arr(p['n1D_ringI_avg'])))
    if max(initial_error, final_error) > 1e-7:
        raise ValueError('Reference reconstruction mismatch')
    exp_full = np.array([np.mean(group, axis=0) for group in exp_raw])
    if np.max(np.abs(exp_full.T-np.asarray(p['n1D_ringExp_avg']))) > 1e-7:
        raise ValueError('Ramp reference reconstruction mismatch')

    # The source code does not clear the last reference between iterations.
    # Keep the previous choice if the timestamp is neither a plateau nor an
    # exact ramp-reference time (notably some roundoff-affected endpoints).
    refs, previous, reused_end = [], None, False
    for t in times:
        if t <= t0:
            previous = ('initial', None)
        elif t >= end:
            previous = ('final', None)
        else:
            matches = np.flatnonzero(exp_times == t)
            if len(matches) > 1:
                raise ValueError('Ambiguous ramp reference time')
            if len(matches) == 1:
                previous = ('ramp', int(matches[0]))
            elif previous is None:
                raise ValueError('No previous normalization reference')
            elif abs(t-end) <= h.TOL:
                reused_end = True
            else:
                raise ValueError('Unexpected missing interior reference')
        refs.append(previous)
    rebuilt = []
    for i, (kind, k) in enumerate(refs):
        ref = initial_full if kind == 'initial' else final_full if kind == 'final' else exp_full[k]
        y = means_full[i]
        rebuilt.append(y - ref * (y.sum()/ref.sum()))
    error = float(np.max(np.abs(np.array(rebuilt).T-np.asarray(p['n1D_phnEv_avg']))))
    if error > 1e-7:
        raise ValueError(f'{path}: normalized profiles do not match source: {error}')

    observed, old_var, _ = h.profiles(data, p, times, t0, dur)
    train = ~((times > t0+h.TOL) & (times < end-h.TOL))
    if sum(~train) != 4:
        raise ValueError('Expected four holdout slices')
    r, atom = h.arr(p['MeanRad_avg']), h.arr(p['AN_phnEv_avg'])
    ri, rf = float(np.mean(r[times<=t0+h.TOL])), float(np.mean(r[times>=end-h.TOL]))
    ci = min(controls, key=lambda x: abs(x['radius_um']-ri))
    cf = min(controls, key=lambda x: abs(x['radius_um']-rf))
    x = h.basis(times, atom[train], times[train], ri, rf, ci, cf, t0, dur, 0.5)
    fit = h.predict(x, train, observed, old_var)
    xz = h.basis(times, atom[train], times[train], ri, rf, ci, cf, t0, dur, 0.0)
    fit_z = h.predict(xz, train, observed, old_var)
    ref_effect = None
    if reused_end:
        j = int(np.argmin(np.abs(times-end)))
        yy = means_full[j]
        assumed = yy-final_full*(yy.sum()/final_full.sum())
        ref_effect = (proj @ (np.array(rebuilt)[j]-assumed)).tolist()
    return {'path': str(path.relative_to(root)), 'date': str(h.arr(p['dateFile'])[0]),
            'times': times, 't0': t0, 'end': end, 'train': train, 'post': post,
            'projector': proj, 'init_runs': init_runs, 'init_raw': init_raw,
            'per_time': per_time, 'exp_raw': exp_raw, 'refs': refs, 'reused_end': reused_end,
            'endpoint_delta': ref_effect, 'reconstruction_error': error,
            'observed': observed, 'fit': fit, 'fit_z': fit_z}


def delta_method_sd(r):
    """Independent finite-difference covariance of the identical residual.

    Treat each phonon slice and each reference group as independent; the final
    reference is correctly a function of post-ramp phonon means. Across-file
    shared references affect joint covariance, not an individual marginal SD.
    """
    P = r['projector']
    groups = [features(v, P) for v in r['per_time']]
    groups.append(features(r['init_raw'], P))
    groups.extend(features(v, P) for v in r['exp_raw'])
    n_times = len(r['times'])
    means = np.concatenate([np.mean(g, axis=0) for g in groups])

    def residual(z):
        a = z.reshape(-1, 3)
        ys, initial, ramp = a[:n_times], a[n_times], a[n_times+1:]
        final = np.mean(ys[r['post']], axis=0)
        out = np.array([normalize(ys[i], initial if kind == 'initial' else final if kind == 'final' else ramp[k])
                        for i, (kind, k) in enumerate(r['refs'])])
        train = r['train']
        return (out[~train] - r['fit']['weights'] @ out[train]).ravel()

    jac = np.empty((8, len(means)))
    for j in range(len(means)):
        step = max(abs(means[j]), 1.0)*1e-5
        plus, minus = means.copy(), means.copy()
        plus[j] += step
        minus[j] -= step
        jac[:, j] = (residual(plus)-residual(minus))/(2*step)
    var = np.zeros(8)
    for k, group in enumerate(groups):
        cov = np.cov(group.T, ddof=1)/len(group)
        J = jac[:, 3*k:3*k+3]
        var += np.einsum('ij,jk,ik->i', J, cov, J)
    if np.any(var <= 0):
        raise ValueError('Invalid delta-method variance')
    initial_jacobian = jac[:, 3*n_times:3*n_times+3]
    return np.sqrt(var).reshape(4, 2), initial_jacobian, groups[n_times]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_root', type=Path)
    root = ap.parse_args().source_root.resolve()
    if version('mat-io') != '1.0.2':
        raise ValueError('Requires mat-io==1.0.2')
    inv = json.loads(Path(__file__).with_name('hubble_data_inventory.json').read_text())
    expected = {r['path'] for r in inv['records']}
    actual = {str(p.relative_to(root)) for branch in ('expansions', 'contractions')
              for p in (root/'data'/branch).glob('PhnRuns_*.mat')}
    if expected != actual:
        raise ValueError('MAT file set differs from pinned inventory')
    for r in inv['records']:
        if hashlib.sha256((root/r['path']).read_bytes()).hexdigest() != r['sha256']:
            raise ValueError(f"Hash mismatch: {r['path']}")
    multiplier_check = validate_multiplier()
    controls = h.load_controls(root)
    recs = []
    for branch in ('expansions', 'contractions'):
        for path in sorted((root/'data'/branch).glob('PhnRuns_*.mat')):
            r = load_dynamic(path, root, controls)
            if r is not None:
                recs.append(r)
    if len(recs) != 28:
        raise ValueError('Expected 28 dynamic protocols')
    # Verify raw initial reference profiles are literally identical across all
    # same-day dynamic files before sharing the same random multipliers.
    groups = {}
    for r in recs:
        if r['date'] in groups:
            g = groups[r['date']]
            if not np.array_equal(g['runs'], r['init_runs']) or not np.array_equal(g['raw'], r['init_raw']):
                raise ValueError('Same-day initial reference data differ')
        else:
            groups[r['date']] = {'runs': r['init_runs'], 'raw': r['init_raw']}
    # Static 38 um control reuses run identities from the 2021-02-20
    # contraction reference. Compare representations without assuming equality.
    static_file = root/'data/expansions/PhnRuns_2021-02-20_0042-0101.mat'
    static = load_from_mat(static_file)
    sruns = h.arr(static['Runs'])
    sr = np.asarray(static['n1Ds']).T
    representative = groups['2021_02_20']
    static_differences = []
    for run, dynamic_profile in zip(representative['runs'], representative['raw']):
        pos = np.flatnonzero(sruns == run)
        if len(pos) != 1:
            raise ValueError('Cannot align static/control reference run identity')
        static_differences.append(float(np.max(np.abs(sr[pos[0]]-dynamic_profile))))
    static_overlap = {'static_file': str(static_file.relative_to(root)),
                      'paired_date_run_ids': len(static_differences),
                      'identical_profile_pairs': sum(v == 0 for v in static_differences),
                      'max_absolute_profile_difference': max(static_differences),
                      'note': 'The same run IDs have differing stored processed profiles; identity does not imply identical extracted arrays.'}
    rng = np.random.default_rng(SEED)
    for g in groups.values():
        g['weights'] = rng.normal(size=(DRAWS, len(g['runs'])))

    detail = []
    residual_draws = []
    delta_details = []
    for r in recs:
        P = r['projector']
        initial = mean_draws(features(r['init_raw'], P), rng, groups[r['date']]['weights'])
        y = np.stack([mean_draws(features(v, P), rng) for v in r['per_time']], axis=1)
        ramp = [mean_draws(features(v, P), rng) for v in r['exp_raw']]
        final = np.mean(y[:, r['post'], :], axis=1)
        out = np.empty((DRAWS, len(r['times']), 2))
        for j, (kind, k) in enumerate(r['refs']):
            ref = initial if kind == 'initial' else final if kind == 'final' else ramp[k]
            out[:, j, :] = normalize(y[:, j, :], ref)
        tr, fit = r['train'], r['fit']
        boot_resid = out[:, ~tr, :] - np.einsum('ht,btc->bhc', fit['weights'], out[:, tr, :])
        residual_draws.append(boot_resid.reshape(DRAWS, -1))
        sd = np.std(boot_resid, axis=0, ddof=1)
        old_sd = np.sqrt(fit['pred_var'])
        delta_sd, initial_jac, initial_features = delta_method_sd(r)
        delta_details.append((delta_sd.ravel(), initial_jac, initial_features))
        max_relative_delta_difference = float(np.max(np.abs(sd/delta_sd-1)))
        if max_relative_delta_difference > 0.12:
            raise ValueError('Joint multiplier and delta-method SD disagree')
        residual = r['observed'][~tr]-fit['prediction']
        zresidual = r['observed'][~tr]-r['fit_z']['prediction']
        endpoint_fixed_H, endpoint_fixed_Z = residual.copy(), zresidual.copy()
        if r['reused_end']:
            j = int(np.argmin(np.abs(r['times']-r['end'])))
            training_idx = np.flatnonzero(np.flatnonzero(tr) == j)
            if len(training_idx) != 1:
                raise ValueError('Endpoint is unexpectedly not in training set')
            # Corrected training outcome = stored outcome - delta; residual
            # increases by W[:,j] * delta. Holdout outcomes remain unchanged.
            effect = np.asarray(r['endpoint_delta'])
            endpoint_fixed_H += np.outer(fit['weights'][:, training_idx[0]], effect)
            endpoint_fixed_Z += np.outer(r['fit_z']['weights'][:, training_idx[0]], effect)
            altered = r['observed'][tr].copy()
            altered[training_idx[0]] -= effect
            direct_h = r['observed'][~tr] - fit['weights'] @ altered
            direct_z = r['observed'][~tr] - r['fit_z']['weights'] @ altered
            if not (np.allclose(endpoint_fixed_H, direct_h, rtol=1e-11, atol=1e-8)
                    and np.allclose(endpoint_fixed_Z, direct_z, rtol=1e-11, atol=1e-8)):
                raise ValueError('Endpoint sensitivity update failed direct refit check')
        detail.append({'path': r['path'], 'date': r['date'],
                       'endpoint_reused_ramp_reference': r['reused_end'],
                       'stored_minus_final_reference_endpoint_sine_cosine': r['endpoint_delta'],
                       'original_profile_max_reconstruction_error': r['reconstruction_error'],
                       'holdout_residual_H': residual.tolist(),
                       'holdout_residual_Z': zresidual.tolist(),
                       'posthoc_final_reference_endpoint_sensitivity_residual_H': endpoint_fixed_H.tolist(),
                       'posthoc_final_reference_endpoint_sensitivity_residual_Z': endpoint_fixed_Z.tolist(),
                       'old_conditional_sd_H': old_sd.tolist(),
                       'joint_conditional_sd_H': sd.tolist(),
                       'delta_method_conditional_sd_H': delta_sd.tolist(),
                       'max_relative_multiplier_vs_delta_sd_difference': max_relative_delta_difference,
                       'joint_to_old_sd_ratio_H': (sd / old_sd).tolist()})
    summary = {}
    for branch in ('expansions','contractions'):
        subset = [r for r in detail if r['path'].startswith('data/'+branch+'/')]
        ratios = np.concatenate([np.ravel(r['joint_to_old_sd_ratio_H']) for r in subset])
        oldsd = np.concatenate([np.ravel(r['old_conditional_sd_H']) for r in subset])
        newsd = np.concatenate([np.ravel(r['joint_conditional_sd_H']) for r in subset])
        residual = np.concatenate([np.ravel(r['holdout_residual_H']) for r in subset])
        rmse = lambda field: float(np.sqrt(np.mean(np.concatenate([np.ravel(r[field]) for r in subset])**2)))
        original_h, original_z = rmse('holdout_residual_H'), rmse('holdout_residual_Z')
        fixed_h = rmse('posthoc_final_reference_endpoint_sensitivity_residual_H')
        fixed_z = rmse('posthoc_final_reference_endpoint_sensitivity_residual_Z')
        summary[branch] = {'protocols': len(subset),
            'original_rmse_H': original_h, 'original_rmse_Z': original_z,
            'posthoc_endpoint_final_reference_rmse_H': fixed_h, 'posthoc_endpoint_final_reference_rmse_Z': fixed_z,
            'posthoc_endpoint_final_reference_rmse_H_minus_Z': fixed_h-fixed_z,
            'endpoint_reuses_last_ramp_reference': sum(r['endpoint_reused_ramp_reference'] for r in subset),
            'median_joint_to_old_conditional_sd_ratio': float(np.median(ratios)),
            'ratio_quantiles_10_90': np.quantile(ratios,[0.1,0.9]).tolist(),
            'fraction_within_old_1_96_sd': float(np.mean(np.abs(residual)<=1.959963984540054*oldsd)),
            'fraction_within_joint_1_96_sd': float(np.mean(np.abs(residual)<=1.959963984540054*newsd))}
    # Preserve the complete conditional cross-protocol covariance. Flattening
    # order is record order, then four holdout times, then sine/cosine.
    draw_matrix = np.concatenate(residual_draws, axis=1)
    covariance = np.cov(draw_matrix, rowvar=False, ddof=1)
    scale = np.sqrt(np.diag(covariance))
    correlation = covariance / np.outer(scale, scale)
    same_day, different_day = [], []
    for i, a in enumerate(recs):
        for j in range(i+1, len(recs)):
            values = np.abs(correlation[8*i:8*i+8, 8*j:8*j+8]).ravel()
            (same_day if a['date']==recs[j]['date'] else different_day).extend(values)
    analytical_shared = []
    for i, a in enumerate(recs):
        for j in range(i+1, len(recs)):
            if a['date'] != recs[j]['date']:
                continue
            sdi, ji, fi = delta_details[i]
            sdj, jj, fj = delta_details[j]
            n = len(fi)
            crosscov = (fi-fi.mean(axis=0)).T @ (fj-fj.mean(axis=0)) / (n*(n-1))
            shared_corr = (ji @ crosscov @ jj.T) / np.outer(sdi, sdj)
            analytical_shared.extend(np.abs(shared_corr).ravel())
    cross_summary = {
        'delta_method_same_day_distinct_protocol_mean_abs_correlation': float(np.mean(analytical_shared)),
        'delta_method_same_day_distinct_protocol_max_abs_correlation': float(np.max(analytical_shared)),
        'same_day_distinct_protocol_mean_abs_correlation': float(np.mean(same_day)),
        'different_day_distinct_protocol_mean_abs_correlation': float(np.mean(different_day)),
        'note': 'Monte Carlo correlations conditional on the modeled shot/reference fluctuations; different-day nonzero values reflect finite-draw noise under the model.'}
    print(json.dumps({'source': 'https://github.com/JQIamo/hubFrct_2021',
        'seed': SEED, 'draws': DRAWS,
        'warning': 'Exploratory multiplier diagnostic conditional on fixed radius, atom trajectory, static calibration and model. Not full experimental uncertainty or a physical significance test.',
        'dynamic_protocols': len(recs),
        'synthetic_shared_multiplier_check': multiplier_check,
        'static_control_overlap': static_overlap,
        'max_abs_profile_reconstruction_error': max(r['reconstruction_error'] for r in recs),
        'same_day_initial_reference_groups': {d: {'unique_run_ids': len(g['runs']),
            'protocols': sum(r['date']==d for r in recs)} for d,g in groups.items()},
        'summary': summary, 'cross_protocol_correlation_summary': cross_summary,
        'covariance_order': 'records order; four heldout times ascending; sine then cosine',
        'conditional_residual_covariance_H': covariance.tolist(),
        'records': detail}, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
