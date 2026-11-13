#!/usr/bin/env python3
"""Numerical controls for a conditioned Dirichlet collapse wavepacket.

Finite-dimensional quadrature is not an interval proof, a simulation of
physical measurements, or a test of cosmological realism.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre

ROOT = Path(__file__).resolve().parent.parent
EPS=0.5
LOW,HIGH=0.5,2.0
KLO,KHI=math.sqrt(LOW),math.sqrt(HIGH)


def calc(t, center=1.0, n=1600, nx=1201, window=4.0):
    z,w=roots_legendre(n)
    k=(KHI-KLO)/2*z+(KHI+KLO)/2
    wk=(KHI-KLO)/2*w
    # Initial density is uniform on [LOW,HIGH]; q0 and p0 cancel in normalization.
    f=np.sqrt(2*k)*np.exp(-EPS**2*t*(k*k-center)**2)
    norm2=np.sum(wk*f*f)
    f=f/math.sqrt(norm2)
    mu=float(np.sum(wk*f*f*k*k))
    var=float(np.sum(wk*f*f*(k*k-mu)**2))
    x=np.linspace(-window,window,nx)
    v=2*math.sqrt(center)*t+x*math.sqrt(t)
    # This chosen interval is positive for our times; direct Dirichlet sine transform.
    assert np.min(v)>0
    phase=np.exp(1j*t*(k*k-center))
    wave=math.sqrt(2/math.pi)*(np.sin(v[:,None]*k[None,:]) @ (wk*f*phase))
    scaled_density=math.sqrt(t)*abs(wave)**2
    probability=float(np.trapezoid(scaled_density,x))
    a=4*EPS**2*center
    sd=math.sqrt((a*a+1)/a)
    limit=math.erf(window/(math.sqrt(2)*sd))
    return {'t':t,'lambda_center':center,'lambda_mean':mu,'lambda_variance':var,
            't_times_lambda_variance':t*var,'window_x_halfwidth':window,
            'moving_window_probability':probability,'limiting_probability':limit,
            'absolute_error':abs(probability-limit)}


def main():
    rows=[calc(t) for t in (25,100,400,1600)]
    refined=calc(400,n=2400,nx=1801)
    refinement_error=abs(refined['moving_window_probability']-rows[2]['moving_window_probability'])
    assert refinement_error<1e-6
    assert rows[-1]['absolute_error']<0.002
    assert abs(rows[-1]['t_times_lambda_variance']-1)<0.01
    # At fixed t the full posterior is built from a single observation, not simulated increments.
    # This is the filtering representation: latent lambda uniform, noise independent Gaussian.
    rng=np.random.default_rng(20241031); n_samples=2000
    latent=rng.uniform(LOW,HIGH,n_samples)
    z=rng.standard_normal(n_samples)
    yy=-2*EPS*latent*40+math.sqrt(40)*z
    centers=-yy/(2*EPS*40)
    q,w=roots_legendre(320); lam=(HIGH-LOW)*q/2+(HIGH+LOW)/2; weights=w*(HIGH-LOW)/2
    expo=-2*EPS**2*40*(lam[None,:]-centers[:,None])**2
    expo-=np.max(expo,axis=1,keepdims=True)
    posterior=np.exp(expo)*weights[None,:]
    posterior/=posterior.sum(axis=1,keepdims=True)
    means=posterior@lam
    mean_prior=(LOW+HIGH)/2
    assert abs(float(np.mean(means))-mean_prior)<0.03
    result={'scope':'Floating-point quadrature and seeded finite-sample controls; no external evidence or proof.',
            'epsilon':EPS,'initial_lambda_distribution':'uniform on [0.5,2]',
            'observation_path_for_rows':'Y_t=-2 epsilon t, so center=1; a deterministic control, not a typical full path',
            'rows':rows,'quadrature_refinement_error_at_400':refinement_error,
            'filter_control_t':40,'filter_control_samples':n_samples,
            'filter_control_posterior_mean_average':float(np.mean(means)),
            'prior_mean':mean_prior,'filter_control_seed':20241031}
    (ROOT/'verification/collapse_moving_window.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
