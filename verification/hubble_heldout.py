#!/usr/bin/env python3
"""Exploratory held-out ramp prediction; see EXPANDING_BEC_HOLDOUT_PLAN.md.

Requires mat-io==1.0.2, NumPy, SciPy and pinned public Banik source. Example:
python verification/hubble_heldout.py /path/to/hubFrct_2021 > results.json
Not a test of gravity or a reproduction of the authors' global fit.
"""
import argparse
import hashlib
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import erf
from matio import load_from_mat

TOL = 1e-9
ALPHA = 0.5
SEED = 20261106
SIMULATIONS = 500
BOOTSTRAPS = 2000


def arr(x):
    return np.asarray(x).ravel()


def val(x):
    return float(np.asarray(x).item())


def profiles(data, p, times, t0, duration):
    """Return observed Fourier coefficients and independent-shot variances.

    The variance omits reference noise and is conditional on its profile. At
    nominal endpoints we assign the corresponding plateau reference; reported
    outcomes themselves are taken from the authors' normalized mean profiles.
    """
    theta = arr(p['AzAngle'])
    spatial = np.column_stack((np.sin(theta), np.cos(theta)))
    pin = np.linalg.pinv(spatial)
    observed = (pin @ np.asarray(p['n1D_phnEv_avg'])).T
    runs, tm = arr(data['Runs']), arr(data['time'])
    shot_profiles = np.asarray(data['n1Ds'])
    mask = np.isin(runs, arr(p['RunNos_phnEv']))
    exp_times = arr(p['n1D_ringExpTimes'])
    variances, counts = [], []
    for t in times:
        select = mask & (np.abs(tm - t) <= TOL)
        shots = shot_profiles[:, select]
        n = shots.shape[1]
        if n < 2:
            raise ValueError('Need at least two preparations per time slice')
        if t <= t0 + TOL:
            ref = arr(p['n1D_ringI_avg'])
        elif t >= t0 + duration - TOL:
            ref = arr(p['n1D_ringF_avg'])
        else:
            idx = np.flatnonzero(np.abs(exp_times - t) <= TOL)
            if len(idx) != 1:
                raise ValueError('No unique ramp reference')
            ref = np.asarray(p['n1D_ringExp_avg'])[:, idx[0]]
        normalized = shots - np.outer(ref, shots.sum(axis=0) / ref.sum())
        shot_coeff = (pin @ normalized).T
        var = np.var(shot_coeff, axis=0, ddof=1) / n
        if not np.all(np.isfinite(var)) or np.any(var <= 0):
            raise ValueError('Invalid shot variance')
        variances.append(var)
        counts.append(n)
    return observed, np.array(variances), counts


def load_controls(root):
    controls = []
    for f in sorted((root / 'data/expansions').glob('PhnRuns_*.mat')):
        p = load_from_mat(f)['A'].properties
        if str(arr(p['dataRingType'])[0]) != 'Initial':
            continue
        q = val(p['Qi'])
        f_hz = val(p['fi'])
        if q <= 0.5 or f_hz <= 0:
            raise ValueError('Invalid static oscillation fit')
        controls.append({'filename': f.name, 'radius_um': float(np.mean(arr(p['MeanRad_avg']))),
                         'atom_number_k': float(np.mean(arr(p['AN_phnEv_avg']))),
                         'Q': q, 'frequency_hz': f_hz})
    if len(controls) != 7:
        raise ValueError('Expected seven static controls')
    return controls


def basis(times, n_values, n_times, radius_i, radius_f, control_i, control_f, t0, duration, hub):
    """Published homogeneous oscillator; state contains two basis solutions."""
    qi, qf = control_i['Q'], control_f['Q']
    # fi is the fitted damped frequency; this conversion follows the authors'
    # PhnAmpDynamicDiffEq.m convention. Atom-number correction uses only the
    # non-ramp trajectory and the initial static control.
    omega_ref = 2 * np.pi * control_i['frequency_hz'] / np.sqrt(1 - 1 / (4 * qi * qi))
    omega_i_ref = omega_ref * (radius_i / control_i['radius_um']) ** (-1 - ALPHA / 2)
    beta = duration / 5.0  # author's sigma=t_exp/2, beta=sigma/2.5
    center = t0 + duration / 2

    def rv(t):
        if t < t0:
            return radius_i, 0.0
        if t > t0 + duration:
            return radius_f, 0.0
        z = (t - center) / beta
        r = radius_i + (radius_f-radius_i) * (1 + erf(z)) / 2
        v = (radius_f-radius_i) * np.exp(-z*z) / (np.sqrt(np.pi)*beta)
        return r, v

    def rhs(t, y):
        r, v = rv(t)
        atom = float(np.interp(t, n_times, n_values))
        omega = omega_i_ref * (r / radius_i) ** (-1-ALPHA/2) * (atom / control_i['atom_number_k']) ** (ALPHA/2)
        q = qi if abs(radius_f-radius_i) < 1e-12 else qi + (qf-qi) * (r-radius_i) / (radius_f-radius_i)
        damping = omega/q + hub*v/r
        return [y[1], -damping*y[1]-omega**2*y[0], y[3], -damping*y[3]-omega**2*y[2]]

    # Scale initial states to produce comparable output columns.
    sol = solve_ivp(rhs, (0, float(times.max()) + 1e-8), [1, 0, 0, omega_i_ref],
                    t_eval=times, rtol=1e-9, atol=1e-10, max_step=0.0005)
    if not sol.success:
        raise ValueError(sol.message)
    radii = np.array([rv(t)[0] for t in times])
    return np.column_stack((sol.y[1], sol.y[3])) / omega_i_ref * (radii[:, None]/radius_i)**ALPHA


def predict(x, train, observed, variance):
    xt, xh = x[train], x[~train]
    column_norm = np.linalg.norm(xt, axis=0)
    scaled = xt/column_norm
    cond = float(np.linalg.cond(scaled))
    if np.linalg.matrix_rank(scaled) != 2 or not np.isfinite(cond):
        raise ValueError('rank-deficient training design')
    pin = np.linalg.pinv(xt)
    coef = pin @ observed[train]
    weights = xh @ pin
    pred = xh @ coef
    pred_var = variance[~train] + (weights**2) @ variance[train]
    return {'prediction': pred, 'pred_var': pred_var, 'coef': coef,
            'pin': pin, 'weights': weights, 'condition': cond}


def process_file(path, root, controls):
    data = load_from_mat(path)
    p = data['A'].properties
    if str(arr(p['dataRingType'])[0]) != 'All':
        return None
    times = arr(p['EvTime'])
    if np.any(np.diff(times) <= 0):
        raise ValueError('Time grid must be strictly increasing')
    t0, duration = val(p['t_phn1']), val(p['t_exp'])
    holdout = (times > t0+TOL) & (times < t0+duration-TOL)
    train = ~holdout
    if holdout.sum() != 4:
        raise ValueError('Expected four ramp observations')
    r = arr(p['MeanRad_avg'])
    ri, rf = float(np.mean(r[times <= t0+TOL])), float(np.mean(r[times >= t0+duration-TOL]))
    if abs(ri-rf) < 1:
        raise ValueError('Degenerate radius profile')
    initial = min(controls, key=lambda c: abs(c['radius_um']-ri))
    final = min(controls, key=lambda c: abs(c['radius_um']-rf))
    atom = arr(p['AN_phnEv_avg'])
    observed, var, counts = profiles(data, p, times, t0, duration)
    fit = {}
    for key, hub in [('H', 0.5), ('Z', 0.0)]:
        x = basis(times, atom[train], times[train], ri, rf, initial, final, t0, duration, hub)
        fit[key] = predict(x, train, observed, var)
        fit[key]['basis'] = x
    # Post-hoc stress test, not a fitted parameter or a calibration interval:
    # perturb the shared initial-frequency calibration by +/-5 percent.
    stress = {}
    for scale in (0.95, 1.05):
        perturbed = dict(initial, frequency_hz=initial['frequency_hz'] * scale)
        stress[str(scale)] = {}
        for key, hub in [('H', 0.5), ('Z', 0.0)]:
            x = basis(times, atom[train], times[train], ri, rf, perturbed, final, t0, duration, hub)
            stress[str(scale)][key] = predict(x, train, observed, var)['prediction']
    return {'path': str(path.relative_to(root)), 'times': times, 't0': t0, 'train': train,
            'observed': observed, 'variance': var, 'counts': counts, 'initial': initial,
            'final': final, 'ri': ri, 'rf': rf, 'fit': fit, 'frequency_stress': stress}


def validate_static_limit():
    """Independent closed-form constant-radius, constant-Q oscillator check."""
    t = np.linspace(0, 0.06, 31)
    q, fd, radius, atom = 5.0, 50.0, 20.0, 100.0
    control = {'Q': q, 'frequency_hz': fd, 'radius_um': radius, 'atom_number_k': atom}
    x = basis(t, np.array([atom, atom]), np.array([0.0, 0.06]), radius, radius,
              control, control, 0.01, 0.01, 0.5)
    w = 2*np.pi*fd / np.sqrt(1 - 1/(4*q*q))
    gamma, wd = w/(2*q), 2*np.pi*fd
    expected = np.column_stack((-w/wd*np.exp(-gamma*t)*np.sin(wd*t),
                                np.exp(-gamma*t)*(np.cos(wd*t)-gamma/wd*np.sin(wd*t))))
    error = float(np.max(np.abs(x-expected)))
    if error > 1e-8:
        raise ValueError('Constant-radius analytic oscillator check failed')
    return {'max_absolute_basis_error': error, 'tolerance': 1e-8}


def validate_synthetic(records, rng):
    coverage, errors = [], []
    for rec in records:
        tr, var = rec['train'], rec['variance']
        m = rec['fit']['H']
        x, pin, w = m['basis'], m['pin'], m['weights']
        for c in range(2):
            signal = x @ m['coef'][:, c]
            noise = rng.normal(size=(SIMULATIONS, len(tr))) * np.sqrt(var[:, c])
            simulated = signal + noise
            beta_hat = simulated[:, tr] @ pin.T
            beta_sigma = np.sqrt((pin**2) @ var[tr, c])
            errors.extend(np.mean((beta_hat-m['coef'][:, c])/beta_sigma, axis=0))
            pred = simulated[:, tr] @ w.T
            errors_pred = simulated[:, ~tr] - pred
            standardized = errors_pred / np.sqrt(m['pred_var'][:, c])
            coverage.extend((np.abs(standardized) <= 1.959963984540054).ravel())
    fraction = float(np.mean(coverage))
    max_bias = float(np.max(np.abs(errors)))
    if not (0.92 <= fraction <= 0.98) or max_bias >= 0.2:
        raise ValueError('Synthetic validation failed')
    return {'draws_per_protocol_channel': SIMULATIONS, 'pooled_95pct_prediction_coverage': fraction,
            'max_abs_mean_coefficient_error_in_conditional_se_units': max_bias,
            'warning': 'Conditional Gaussian simulation, estimated shot variances treated as exact; not validation of real-data error model.'}


def branch_summary(records, branch, rng):
    part = [r for r in records if r['path'].startswith('data/'+branch+'/')]
    mh = np.array([np.mean((r['observed'][~r['train']]-r['fit']['H']['prediction'])**2) for r in part])
    mz = np.array([np.mean((r['observed'][~r['train']]-r['fit']['Z']['prediction'])**2) for r in part])
    bootidx = rng.integers(0, len(part), size=(BOOTSTRAPS, len(part)))
    boot = np.sqrt(np.mean(mh[bootidx], axis=1)) - np.sqrt(np.mean(mz[bootidx], axis=1))
    cover = {}
    for k in ['H', 'Z']:
        flags = [np.abs(r['observed'][~r['train']]-r['fit'][k]['prediction']) <=
                 1.959963984540054*np.sqrt(r['fit'][k]['pred_var']) for r in part]
        cover[k] = float(np.mean(flags))
    sensitivity = {}
    for scale in ('0.95', '1.05'):
        sq = {k: np.array([np.mean((r['observed'][~r['train']]-r['frequency_stress'][scale][k])**2)
                           for r in part]) for k in ('H', 'Z')}
        sensitivity[scale] = {'rmse_H': float(np.sqrt(np.mean(sq['H']))),
                              'rmse_Z': float(np.sqrt(np.mean(sq['Z']))),
                              'rmse_H_minus_Z': float(np.sqrt(np.mean(sq['H']))-np.sqrt(np.mean(sq['Z'])))}
    return {'protocols': len(part), 'heldout_components': len(part)*8,
            'posthoc_frequency_scale_sensitivity': sensitivity,
            'rmse_H': float(np.sqrt(np.mean(mh))), 'rmse_Z': float(np.sqrt(np.mean(mz))),
            'rmse_H_minus_Z': float(np.sqrt(np.mean(mh))-np.sqrt(np.mean(mz))),
            'conditional_protocol_bootstrap_95pct_interval': list(map(float,np.percentile(boot,[2.5,97.5]))),
            'nominal_95pct_conditional_interval_coverage': cover,
            'warning': 'Bootstrap and intervals condition on shared calibration and estimated shot noise; not a significance test.'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_root', type=Path)
    root = ap.parse_args().source_root.resolve()
    if version('mat-io') != '1.0.2':
        raise ValueError('This analysis requires mat-io==1.0.2')
    inventory = json.loads(Path(__file__).with_name('hubble_data_inventory.json').read_text())
    expected = {r['path'] for r in inventory['records']}
    actual = {str(p.relative_to(root)) for branch in ('expansions', 'contractions')
              for p in (root/'data'/branch).glob('PhnRuns_*.mat')}
    if actual != expected:
        raise ValueError('MAT file list does not match the pinned inventory')
    for record in inventory['records']:
        path = root / record['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
            raise ValueError(f'Pinned inventory hash mismatch: {path}')
    analytic_check = validate_static_limit()
    controls = load_controls(root)
    records = []
    for branch in ('expansions','contractions'):
        for path in sorted((root/'data'/branch).glob('PhnRuns_*.mat')):
            result = process_file(path, root, controls)
            if result is not None:
                records.append(result)
    if len(records) != 28:
        raise ValueError('Expected 28 dynamic traces')
    rng = np.random.default_rng(SEED)
    simulation = validate_synthetic(records, rng)  # Must pass before scoring data.
    summary = {branch: branch_summary(records, branch, rng) for branch in ('expansions','contractions')}
    detail = []
    for r in records:
        idx = ~r['train']
        detail.append({'path': r['path'], 'radius_initial_um': r['ri'], 'radius_final_um': r['rf'],
                       'initial_control': r['initial']['filename'], 'final_control': r['final']['filename'],
                       'holdout_offset_ms': ((r['times'][idx]-r['t0'])*1000).tolist(),
                       'heldout_observed_sin_cos': r['observed'][idx].tolist(),
                       'shot_variance_of_mean_sin_cos': r['variance'][idx].tolist(),
                       'holdout_prediction_H': r['fit']['H']['prediction'].tolist(),
                       'holdout_prediction_Z': r['fit']['Z']['prediction'].tolist(),
                       'scaled_design_condition_H': r['fit']['H']['condition'],
                       'scaled_design_condition_Z': r['fit']['Z']['condition']})
    print(json.dumps({'source': 'https://github.com/JQIamo/hubFrct_2021',
                      'expected_source_commit': '88c8a87aed5961f589db66a7e7e4e97f161ad51c',
                      'seed': SEED, 'plan': 'EXPANDING_BEC_HOLDOUT_PLAN.md',
                      'static_controls': controls, 'analytic_static_limit_check': analytic_check, 'synthetic_validation': simulation,
                      'summary': summary, 'records': detail}, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
