#!/usr/bin/env python3
"""Finite numerical controls for the Dirichlet spectral-localization gate.

Uses dimensionless units; quadrature is not interval certified and does not
prove the analytic bound, collapse trajectories, or a cosmological model.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent.parent


def packet(sigma, r=2.0):
    # f(k) is the sine-transform coefficient, normalized in dk, k >= 0.
    def raw(k):
        return math.exp(-((k-1.0)**2)/(4*sigma*sigma))
    norm2 = quad(lambda k: raw(k)**2, 0, 2, epsabs=1e-13, points=[1])[0]
    def f(k):
        return raw(k)/math.sqrt(norm2)
    mean = quad(lambda k: k*k*f(k)**2, 0, 2, epsabs=1e-13, points=[1])[0]
    variance = quad(lambda k: (k*k-mean)**2*f(k)**2, 0, 2, epsabs=1e-13, points=[1])[0]
    def psi(v):
        return math.sqrt(2/math.pi)*quad(lambda k: f(k)*math.sin(k*v), 0, 2, epsabs=1e-12, points=[1])[0]
    probability = quad(lambda v: psi(v)**2, 0, r, epsabs=1e-11)[0]
    delta = variance**0.25
    hs2_bound = 2*r/math.pi * math.sqrt(2*delta)
    bound = min(1.0, (math.sqrt(hs2_bound)+math.sqrt(variance)/delta)**2)
    return {'sigma_k':sigma, 'lambda_mean':mean, 'lambda_variance':variance,
            'probability_v_below_R':probability, 'analytic_upper_bound':bound}


def main():
    # The integrals cut off at k=2; for these sigmas the omitted norm is < 3e-7.
    rows = [packet(s) for s in (0.2, 0.1, 0.05, 0.025)]
    assert all(x['probability_v_below_R'] <= x['analytic_upper_bound']+1e-10 for x in rows)
    assert all(a['lambda_variance'] > b['lambda_variance'] and
               a['probability_v_below_R'] > b['probability_v_below_R']
               for a,b in zip(rows,rows[1:]))
    # Master equation and Gaussian random-unitary single-slot equality, including all matrix units.
    lam=np.array([0.2,1.3,2.0]); eps=0.7; t=1.8
    A=np.diag(lam); d=3
    # Column-major vectorization: vec(A X B) = (B.T kron A) vec(X).
    ad=np.kron(np.eye(d),A)-np.kron(A.T,np.eye(d))
    channel=expm(-0.5*eps**2*t*(ad@ad))
    retention=np.exp(-0.5*eps**2*t*(lam[:,None]-lam[None,:])**2)
    largest=0.0
    for i in range(d):
        for j in range(d):
            unit=np.zeros((d,d)); unit[i,j]=1
            actual=(channel@unit.reshape(-1,order='F')).reshape((d,d),order='F')
            largest=max(largest,float(np.max(np.abs(actual-retention[i,j]*unit))))
    assert largest < 1e-12
    r=0.8
    markov=r*r; static=r**4
    assert abs(markov-0.64)<1e-14 and abs(static-0.4096)<1e-14
    # Deterministic clock reparameterization t=s^2 at s=2: old time is 4, not 2.
    transformed=math.exp(-4*0.5); naive=math.exp(-2*0.5)
    assert transformed < naive
    result={'scope':'Finite floating-point controls; no independent proof or data.',
            'R':2.0,'wavepackets_truncated_at_k_2':rows,
            'max_three_level_matrix_unit_error':largest,
            'two_slot_single_slot_retention':r,'two_slot_markov_retention':markov,
            'two_slot_static_retention':static,'two_slot_markov_plus_probability':(1+markov)/2,
            'two_slot_static_plus_probability':(1+static)/2,
            'time_change_true_retention':transformed,'time_change_naive_retention':naive}
    (ROOT/'verification/cosmological_collapse_geometry_gate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
