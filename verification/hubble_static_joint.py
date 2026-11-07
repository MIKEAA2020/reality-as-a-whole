#!/usr/bin/env python3
"""Exploratory paired static-fit/reference sensitivity, not a MATLAB fit.

Usage: python verification/hubble_static_joint.py /path/to/hubFrct_2021
See EXPANDING_BEC_STATIC_CONTROL_AUDIT.md for assumptions and limitations.
"""
import argparse
import hashlib
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
from matio import load_from_mat
import hubble_heldout as h
import hubble_reference_uncertainty as ref
import hubble_static_stratified as st

SEED=20261108
DRAWS=500


def paired_draws(data, weights):
    n=len(data)
    return np.mean(data,axis=0)+weights @ (data-np.mean(data,axis=0))/np.sqrt(n*(n-1))


def validate_paired_sampler():
    rows=np.array([[1.,4.,2.],[3.,-1.,0.],[5.,2.,4.],[2.,-3.,1.]])
    transform=np.array([[1.,.2],[-.5,1.],[.1,.7]])
    rng=np.random.default_rng(8374)
    weights=rng.normal(size=(20000,len(rows)))
    a=paired_draws(rows,weights)
    b=paired_draws(rows@transform,weights)
    empirical=np.cov(a.T,b.T,ddof=1)[:3,3:]
    target=np.cov(rows.T,ddof=1)@transform/len(rows)
    error=float(np.linalg.norm(empirical-target)/np.linalg.norm(target))
    if error>0.04:
        raise ValueError('Paired sampler covariance check failed')
    return error


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_root',type=Path)
    root=ap.parse_args().source_root.resolve()
    if version('mat-io')!='1.0.2':
        raise ValueError('Requires mat-io==1.0.2')
    inventory=json.loads(Path(__file__).with_name('hubble_data_inventory.json').read_text())
    for rec in inventory['records']:
        if hashlib.sha256((root/rec['path']).read_bytes()).hexdigest()!=rec['sha256']:
            raise ValueError('Input hash mismatch')
    paired_sampler_check=validate_paired_sampler()
    static_path=root/'data/expansions/PhnRuns_2021-02-20_0042-0101.mat'
    raw=load_from_mat(static_path); p=raw['A'].properties
    t=h.arr(p['EvTime']); runs=h.arr(raw['Runs']); tm=h.arr(raw['time']); profile=np.asarray(raw['n1Ds']).T
    theta=h.arr(p['AzAngle']); P=np.linalg.pinv(np.column_stack((np.sin(theta),np.cos(theta))))
    ph=np.isin(runs,h.arr(p['RunNos_phnEv']))
    groups=[np.flatnonzero(ph & (abs(tm-x)<h.TOL)) for x in t]
    if len(groups)!=30 or any(len(g)!=2 for g in groups):
        raise ValueError('Expected 30 two-shot time groups')
    group_means=np.array([np.mean(profile[g],axis=0) for g in groups])
    ring=np.mean(group_means,axis=0)
    reconstructed=np.array([y-ring*y.sum()/ring.sum() for y in group_means]).T
    profile_error=float(np.max(np.abs(reconstructed-np.asarray(p['n1D_phnEv_avg']))))
    if profile_error>1e-7:
        raise ValueError('Static normalized profiles could not be reconstructed')
    obs=(P@np.asarray(p['n1D_phnEv_avg'])).T
    fmax=1/(2*np.diff(t)[0])-0.01
    phi=h.val(p['AzPhase'])
    direction=np.array([np.cos(phi),np.sin(phi)])
    scalar_obs=obs @ direction
    scalar_projection_error=float(np.max(np.abs(scalar_obs-h.arr(p['deltan_avg']))))
    if scalar_projection_error>0.01:
        raise ValueError('Stored scalar amplitudes do not match fixed-angle projection')
    baseline=st.scalar_model(t,scalar_obs,fmax)
    synthetic_X=np.column_stack((np.exp(-7.5*t)*np.cos(2*np.pi*20.03*t),
                                 np.exp(-7.5*t)*np.sin(2*np.pi*20.03*t)))
    synthetic_y=synthetic_X @ np.array([2.0,1.2])
    synthetic_fit=st.scalar_model(t,synthetic_y,fmax)
    if abs(synthetic_fit['frequency_hz']-20.03)>1e-5 or abs(synthetic_fit['decay_rate_per_s']-7.5)>1e-5:
        raise ValueError('Synthetic static fit recovery failed')
    if baseline['freq_hits_bound'] or baseline['decay_hits_bound']:
        raise ValueError('Baseline fit hits a bound')
    controls=h.load_controls(root)
    dynamic=[]
    for path in sorted((root/'data/contractions').glob('PhnRuns_2021-02-20_*.mat')):
        r=ref.load_dynamic(path,root,controls)
        if r is not None:
            if not np.array_equal(np.sort(r['init_runs']),np.sort(runs[ph])):
                raise ValueError('Overlapping run IDs do not match')
            dynamic.append(r)
    if len(dynamic)!=5:
        raise ValueError('Expected five dynamic protocols')
    # Initial reference data are identical across same-day dynamic files.
    for r in dynamic[1:]:
        if not np.array_equal(r['init_raw'], dynamic[0]['init_raw']):
            raise ValueError('Dynamic initial-reference representations differ')
    dy=dynamic[0]
    dynamic_index={int(run):i for i,run in enumerate(dy['init_runs'])}
    Pd=dy['projector']
    static_draws=np.empty((DRAWS,len(t),3))
    dyn_total=np.zeros((DRAWS,3))
    rng=np.random.default_rng(SEED)
    for k,group in enumerate(groups):
        # Identical multipliers for matched static and dynamic versions of the
        # same shots preserve their empirical cross-representation covariance.
        w=rng.normal(size=(DRAWS,len(group)))
        sf=ref.features(profile[group],P)
        idx=[dynamic_index[int(runs[j])] for j in group]
        df=ref.features(dy['init_raw'][idx],Pd)
        static_draws[:,k,:]=paired_draws(sf,w)
        dyn_total += paired_draws(df,w)/len(groups)
    static_ref=static_draws.mean(axis=1)
    signals=ref.normalize(static_draws,static_ref[:,None,:])
    fits=[]
    for y in signals:
        f=st.scalar_model(t,y @ direction,fmax,starts=[baseline['frequency_hz']])
        if f['freq_hits_bound'] or f['decay_hits_bound']:
            raise ValueError('A bootstrap fit hit a parameter bound')
        fits.append([f['frequency_hz'],f['Q_static_sinusoid']])
    fits=np.asarray(fits)
    grid_checks=[]
    for k in np.linspace(0,DRAWS-1,10,dtype=int):
        broad=st.scalar_model(t,signals[k] @ direction,fmax)
        difference=abs(broad['frequency_hz']-fits[k,0])
        if difference>1e-3:
            raise ValueError('A local bootstrap fit differs from its multi-start check')
        grid_checks.append(difference)
    # Refit point model states after varying the stored initial control fi/Qi
    # to obtain a finite-difference residual sensitivity. These derivatives
    # are evaluated at the original stored controls; variation is estimated
    # from a closely matching fixed-angle scalar fit, not the authors' MATLAB fit.
    result=[]
    for r in dynamic:
        d=load_from_mat(root/r['path']); p=d['A'].properties
        tr=r['train']; ts=r['times']; rad=h.arr(p['MeanRad_avg']); atom=h.arr(p['AN_phnEv_avg'])
        ri=float(np.mean(rad[ts<=r['t0']+h.TOL]));rf=float(np.mean(rad[ts>=r['end']-h.TOL]))
        ci=min(controls,key=lambda c:abs(c['radius_um']-ri))
        cf=min(controls,key=lambda c:abs(c['radius_um']-rf))
        if ci['filename']!=static_path.name:
            raise ValueError('Unexpected initial static control')
        def response(control):
            x=h.basis(ts,atom[tr],ts[tr],ri,rf,control,cf,r['t0'],r['end']-r['t0'],0.5)
            w=x[~tr] @ np.linalg.pinv(x[tr])
            return (r['observed'][~tr]-w @ r['observed'][tr]).ravel()
        derivatives=[]
        derivative_errors=[]
        for key in ('frequency_hz','Q'):
            step=ci[key]*5e-4
            cp,cm=dict(ci),dict(ci)
            cp[key]+=step; cm[key]-=step
            first=(response(cp)-response(cm))/(2*step)
            cp,cm=dict(ci),dict(ci)
            cp[key]+=step/2; cm[key]-=step/2
            second=(response(cp)-response(cm))/step
            err=float(np.linalg.norm(first-second)/max(np.linalg.norm(second),1e-12))
            if err>0.01:
                raise ValueError('Calibration finite difference unstable')
            derivatives.append(second)
            derivative_errors.append(err)
        Jcal=np.column_stack(derivatives)
        _,Jref,_=ref.delta_method_sd(r)
        delta_fq=fits-fits.mean(axis=0)
        delta_ref=dyn_total-dyn_total.mean(axis=0)
        a=delta_fq @ Jcal.T
        b=delta_ref @ Jref.T
        var_cal=np.var(a,axis=0,ddof=1);var_ref=np.var(b,axis=0,ddof=1)
        cov=np.mean((a-a.mean(axis=0))*(b-b.mean(axis=0)),axis=0)*DRAWS/(DRAWS-1)
        joint=np.var(a+b,axis=0,ddof=1)
        if not np.allclose(joint,var_cal+var_ref+2*cov,rtol=1e-10,atol=1e-5):
            raise ValueError('Variance decomposition failed')
        # Compare paired variance to deliberately dropping cross-covariance.
        ratio=np.sqrt(joint/(var_cal+var_ref))
        result.append({'path':r['path'], 'finite_difference_relative_discrepancy':derivative_errors,
                       'calibration_only_sd':np.sqrt(var_cal).tolist(),
                       'reference_only_sd':np.sqrt(var_ref).tolist(),
                       'paired_calibration_reference_sd':np.sqrt(joint).tolist(),
                       'independent_assumption_sd':np.sqrt(var_cal+var_ref).tolist(),
                       'paired_to_independent_sd_ratio':ratio.tolist()})
    ratios=np.concatenate([r['paired_to_independent_sd_ratio'] for r in result])
    correlation=np.corrcoef(np.column_stack((fits,dyn_total)).T)
    print(json.dumps({'source':'https://github.com/JQIamo/hubFrct_2021',
        'warning':'Exploratory paired conditional multiplier sensitivity using a fixed-angle scalar static estimator and linearized residual; not full covariance, not a MATLAB replication.',
        'seed':SEED,'draws':DRAWS,'paired_sampler_synthetic_cross_covariance_relative_error':paired_sampler_check,
        'static_control':str(static_path.relative_to(root)),
        'baseline_fit':baseline,'synthetic_fit':synthetic_fit,
        'scalar_amplitude_projection_max_difference':scalar_projection_error,
        'sampled_multistart_checks':len(grid_checks),
        'sampled_multistart_max_frequency_difference_hz':max(grid_checks),
        'static_profile_max_reconstruction_error':profile_error,
        'stored_fi_hz':h.val(raw['A'].properties['fi']),
        'stored_Q':h.val(raw['A'].properties['Qi']),
        'frequency_draw_sd_hz':float(np.std(fits[:,0],ddof=1)),
        'frequency_draw_quantiles_2_5_50_97_5_hz':np.quantile(fits[:,0],[.025,.5,.975]).tolist(),
        'Q_draw_sd':float(np.std(fits[:,1],ddof=1)),
        'Q_draw_quantiles_2_5_50_97_5':np.quantile(fits[:,1],[.025,.5,.975]).tolist(),
        'correlation_order':['f','Q','reference_sum','reference_sin','reference_cos'],
        'conditional_correlation':correlation.tolist(),
        'paired_to_independent_sd_ratio_median':float(np.median(ratios)),
        'paired_to_independent_sd_ratio_10_90':np.quantile(ratios,[.1,.9]).tolist(),
        'protocols':result},indent=2,allow_nan=False))


if __name__=='__main__':
    main()
