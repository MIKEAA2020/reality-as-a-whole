#!/usr/bin/env python3
"""Audit time-stratified reference noise and fit the released static controls.

Usage: python verification/hubble_static_stratified.py /path/to/hubFrct_2021
An exploratory alternative fit, not a MATLAB replication. Requires mat-io 1.0.2.
"""
import argparse
import hashlib
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
from matio import load_from_mat
from scipy.optimize import least_squares
import hubble_heldout as h
import hubble_reference_uncertainty as ref


def static_model(t, signal, fmax, starts=None):
    """Profile linear coefficients of two spatial channels plus offsets."""
    def residual(par):
        freq, gamma = par
        e = np.exp(-gamma*t)
        X = np.column_stack((e*np.cos(2*np.pi*freq*t), e*np.sin(2*np.pi*freq*t), np.ones_like(t)))
        return (X @ np.linalg.lstsq(X, signal, rcond=None)[0] - signal).ravel()
    if starts is None:
        starts = np.linspace(1, fmax-0.01, 24)
    results = [least_squares(residual, [float(f), 25.0], bounds=([0.1, 0.01], [fmax, 500.0]),
                             ftol=1e-10, xtol=1e-10, gtol=1e-10, max_nfev=400)
               for f in starts]
    good = [x for x in results if x.success and np.all(np.isfinite(x.x))]
    if not good:
        raise ValueError('No converged static fit')
    best = min(good, key=lambda x: x.cost)
    f, gamma = best.x
    return {'frequency_hz': float(f), 'decay_rate_per_s': float(gamma),
            'Q_static_sinusoid': float(np.pi*f/gamma), 'rmse_spatial_coefficients': float(np.sqrt(np.mean(best.fun**2))),
            'freq_hits_bound': bool(f < 0.2 or f > fmax-0.1), 'decay_hits_bound': bool(gamma < 0.02 or gamma > 499.9)}


def scalar_model(t, signal, fmax, starts=None):
    """Unweighted static damped sinusoid with no offset, profiled amplitude."""
    def residual(par):
        freq, gamma=par
        e=np.exp(-gamma*t)
        X=np.column_stack((e*np.cos(2*np.pi*freq*t),e*np.sin(2*np.pi*freq*t)))
        return X @ np.linalg.lstsq(X,signal,rcond=None)[0]-signal
    if starts is None:
        starts=np.linspace(1,fmax-0.01,24)
    fits=[least_squares(residual,[float(x),25],bounds=([.1,.01],[fmax,500]),
                        ftol=1e-11,xtol=1e-11,gtol=1e-11,max_nfev=400) for x in starts]
    valid=[x for x in fits if x.success and np.all(np.isfinite(x.x))]
    if not valid:
        raise ValueError('Static scalar fit did not converge')
    fit=min(valid,key=lambda x:x.cost)
    frequency,gamma=fit.x
    return {'frequency_hz':float(frequency),'decay_rate_per_s':float(gamma),
            'Q_static_sinusoid':float(np.pi*frequency/gamma),
            'rmse_scalar_amplitude':float(np.sqrt(np.mean(fit.fun**2))),
            'freq_hits_bound':bool(frequency<0.2 or frequency>fmax-0.1),
            'decay_hits_bound':bool(gamma<.02 or gamma>499.9)}


def controls_analysis(root):
    result = []
    for path in sorted((root/'data/expansions').glob('PhnRuns_*.mat')):
        d = load_from_mat(path)
        p = d['A'].properties
        if str(h.arr(p['dataRingType'])[0]) != 'Initial':
            continue
        t = h.arr(p['EvTime'])
        steps = np.diff(t)
        if not np.allclose(steps, steps[0], rtol=0, atol=1e-12):
            raise ValueError('Expected uniform static time grid')
        fs = 1.0/steps[0]
        ang = h.arr(p['AzAngle'])
        P = np.linalg.pinv(np.column_stack((np.sin(ang),np.cos(ang))))
        signal = (P @ p['n1D_phnEv_avg']).T
        fit = static_model(t, signal, fs/2-0.01)
        scalar = scalar_model(t,h.arr(p['deltan_avg']),fs/2-0.01)
        phi=h.val(p['AzPhase'])
        projected=signal[:,0]*np.cos(phi)+signal[:,1]*np.sin(phi)
        amplitude_difference=float(np.max(np.abs(projected-h.arr(p['deltan_avg']))))
        f = fit['frequency_hz']
        # sin/cos at f and fs-f have the same span at t=t0+n/fs.
        design = lambda fr: np.column_stack((np.cos(2*np.pi*fr*t),np.sin(2*np.pi*fr*t)))
        resid = design(fs-f) - design(f) @ np.linalg.lstsq(design(f),design(fs-f),rcond=None)[0]
        alias_error = float(np.max(np.abs(resid)))
        if alias_error > 1e-10:
            raise ValueError('Aliasing invariant failed')
        result.append({'path': str(path.relative_to(root)), 'radius_um': float(np.mean(h.arr(p['MeanRad_avg']))),
                       'sample_spacing_s': float(steps[0]), 'sampling_rate_hz': float(fs),
                       'nyquist_hz': float(fs/2), 'fitted': fit,
                       'alias_hz': float(fs-f), 'alias_design_max_error': alias_error,
                       'stored_frequency_hz': h.val(p['fi']), 'stored_Q': h.val(p['Qi']),
                       'scalar_deltan_fit':scalar,
                       'scalar_minus_stored_frequency_hz':scalar['frequency_hz']-h.val(p['fi']),
                       'scalar_minus_stored_Q':scalar['Q_static_sinusoid']-h.val(p['Qi']),
                       'max_abs_scalar_projection_difference':amplitude_difference,
                       'frequency_relative_difference_percent': float(100*(f/h.val(p['fi'])-1)),
                       'Q_relative_difference_percent': float(100*(fit['Q_static_sinusoid']/h.val(p['Qi'])-1))})
    if len(result) != 7:
        raise ValueError('Expected seven distinct static controls')
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_root',type=Path)
    root=ap.parse_args().source_root.resolve()
    if version('mat-io')!='1.0.2':
        raise ValueError('Requires mat-io==1.0.2')
    inv=json.loads(Path(__file__).with_name('hubble_data_inventory.json').read_text())
    for r in inv['records']:
        if hashlib.sha256((root/r['path']).read_bytes()).hexdigest()!=r['sha256']:
            raise ValueError(f"Source hash mismatch: {r['path']}")
    controls=h.load_controls(root)
    result=[]
    for branch in ('expansions','contractions'):
        for path in sorted((root/'data'/branch).glob('PhnRuns_*.mat')):
            r=ref.load_dynamic(path,root,controls)
            if r is None:
                continue
            data=load_from_mat(path)
            raw_runs=h.arr(data['Runs'])
            raw_time=h.arr(data['time'])
            ids=r['init_runs']
            indices=[np.flatnonzero(raw_runs == rid) for rid in ids]
            if not all(len(x)==1 for x in indices):
                raise ValueError('Reference run ID not unique')
            times=np.array([raw_time[x[0]] for x in indices])
            unique, inv_idx=np.unique(np.round(times,9),return_inverse=True)
            counts=np.bincount(inv_idx)
            if len(unique)!=30 or not np.all(counts==2):
                raise ValueError('Unexpected initial-reference time strata')
            sd,jac,features=ref.delta_method_sd(r)
            n=len(features)
            cov_iid=np.cov(features.T,ddof=1)/n
            cov_strat=np.zeros((3,3))
            for ix in range(len(unique)):
                sub=features[inv_idx==ix]
                # Mean is weighted by observed stratum count / total count.
                cov_strat+=(len(sub)/n)**2 * np.cov(sub.T,ddof=1)/len(sub)
            vi=np.einsum('ij,jk,ik->i',jac,cov_iid,jac)
            vs=np.einsum('ij,jk,ik->i',jac,cov_strat,jac)
            total=sd.ravel()**2
            revised=total-vi+vs
            if np.any(revised<=0):
                raise ValueError('Negative total variance')
            result.append({'path': r['path'],'date':r['date'],'reference_shots':n,
                           'reference_time_strata':len(unique),'shots_per_stratum':2,
                           'iid_reference_variance':vi.tolist(), 'stratified_reference_variance':vs.tolist(),
                           'iid_total_residual_sd':sd.ravel().tolist(),
                           'stratified_total_residual_sd':np.sqrt(revised).tolist(),
                           'total_sd_ratio_stratified_to_iid':(np.sqrt(revised)/sd.ravel()).tolist()})
    if len(result)!=28:
        raise ValueError('Expected 28 dynamic protocols')
    summary={}
    for branch in ('expansions','contractions'):
        subset=[r for r in result if r['path'].startswith('data/'+branch+'/')]
        ratios=np.concatenate([r['total_sd_ratio_stratified_to_iid'] for r in subset])
        v0=np.concatenate([r['iid_reference_variance'] for r in subset])
        v1=np.concatenate([r['stratified_reference_variance'] for r in subset])
        summary[branch]={'protocols':len(subset),'median_total_sd_ratio_stratified_to_iid':float(np.median(ratios)),
                         'total_sd_ratio_10_90':np.quantile(ratios,[.1,.9]).tolist(),
                         'median_reference_variance_ratio_stratified_to_iid':float(np.median(v1/v0)),
                         'fraction_components_reference_variance_reduced':float(np.mean(v1<v0))}
    print(json.dumps({'source':'https://github.com/JQIamo/hubFrct_2021',
        'warning':'Exploratory independent sinusoid fits and conditional stratification sensitivity; not a MATLAB replication or total experimental uncertainty.',
        'static_controls':controls_analysis(root),'summary':summary,'dynamic_protocols':result},indent=2,allow_nan=False))


if __name__=='__main__':
    main()
