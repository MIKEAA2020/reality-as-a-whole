# Exploratory held-out ramp prediction

> **Follow-up and correction:** [The reference-uncertainty audit](EXPANDING_BEC_REFERENCE_UNCERTAINTY.md) reconstructed all stored profiles and found that seven nominal ramp-end training slices use the last ramp reference. The variance calculation below assigned those seven slices the final-ring reference, which was inconsistent with the stored outcome preprocessing. The original RMSEs use the stored outcomes and are unchanged; their conditional interval diagnostics and bootstrap should not be treated as a complete or reliable uncertainty analysis. The follow-up propagates shared references under explicit conditional assumptions.

**Decision: the simplified model comparison is not reliable enough to claim a new experimental result or distinguish the physical friction coefficient.** Nominal 95% prediction intervals substantially under-cover the held-out measurements, and a simple calibration stress test changes the model ranking for expansion. The bootstrap intervals reported below omit shared calibration and reference uncertainties. This is a diagnostic analysis of published analogue-oscillator data, not a solution of the problem of time.

The procedure was recorded before scoring the held-out data in [EXPANDING_BEC_HOLDOUT_PLAN.md](EXPANDING_BEC_HOLDOUT_PLAN.md). It is an exploratory in-workspace plan, **not** externally preregistered or an independent experiment; the dataset and prior publications were already known. The later frequency stress test was added after the initial scores were seen.

## What was tested

For each of 11 expansion and 17 contraction protocols, hold out the four density-profile slices strictly inside the programmed ramp. Project profiles independently onto spatial sine and cosine components, and fit two initial-state coefficients for each component using the remaining slices. The fit uses both pre- and post-ramp observations, so it is a **model-dependent interpolation**, not a prediction from pre-ramp data alone. The data remain ensembles of distinct preparations.

The two models share the oscillator and error-function ramp from [Banik et al. (2022)](https://doi.org/10.1103/PhysRevLett.128.090401) and [their published source code](https://github.com/JQIamo/hubFrct_2021), with harmonic-reference `alpha = 0.5`. Model H uses `gamma_H = 0.5`; model Z uses `gamma_H = 0`. Frequency and initial/final quality factors come from nearest-radius fixed-ring control fits, using each control once, with atom-number scaling from non-ramp observations. Plateau radii and N(t) are obtained from non-ramp slices. No published full-dataset `gamma_H`, temporal phase, or angular phase is imported. The source's static-fit `fi` and `Qi` fields are treated as plug-in estimates; their fitting and preprocessing have not been independently reproduced. The two spatial components are not two directly measured temporal clock quadratures.

This simplifies the paper's 2D global fit: it fits initial states per trace and omits, among other things, a complete shared-error model and the paper's full atom-number-dependent amplitude treatment. A discrepancy is therefore not by itself a failure of the published model. The prior art already measures attenuation/amplification and phase dependence; our holdout scores do not establish novelty.

## Numerical checks

- The constant-radius, constant-Q limit agrees with an independent analytic damped oscillator to `5.27 × 10⁻¹⁰` in dimensionless basis amplitude.
- All 28 designs are full rank. The condition number after scaling columns is at most **2.41** across both models. This is a numerical rank check, **not** proof that the initial phase is statistically well determined under realistic errors.
- In a conditional synthetic experiment, 500 Gaussian draws per protocol and spatial component at the actual time grids give **94.98%** marginal coverage for nominal 95% intervals. The largest mean coefficient error was 0.107 conditional standard errors. These draws use the fitted initial states and observed shot-variance estimates as fixed inputs; passing does not validate Gaussianity, independence, the real error estimates or the physical oscillator.
- The script verifies SHA-256 hashes of all 42 original MAT files against the pinned inventory before calculation. See [script](verification/hubble_heldout.py) and [machine-readable output](verification/hubble_heldout.json).

## Held-out results

RMSE uses both spatial Fourier components and four ramp slices per protocol, in the repository's stored 1D-density-profile units. Lower is better; a negative difference favors H. The observations share controls and reference processing, so the component counts are not independent replications.

| Branch | Protocols | RMSE H | RMSE Z | H − Z | Conditional protocol-bootstrap 95% interval for H − Z |
|---|---:|---:|---:|---:|---:|
| Expansion | 11 | 638.0 | 692.8 | −54.9 | [−103.0, −14.5] |
| Contraction | 17 | 1183.2 | 1188.7 | −5.5 | [−40.0, 23.6] |

The bootstrap resamples complete protocols within a branch, but holds the shared static controls, fitted control frequencies, Q values, radius calibration and reference processing fixed. Its interval is conditional on those choices and is **not** a complete confidence interval or a physical significance test. It should not be read as evidence for H merely because one conditional interval excludes zero.

The fractions of held-out Fourier components inside their nominal 95% marginal prediction intervals were:

| Branch | H | Z |
|---|---:|---:|
| Expansion | 61.4% | 64.8% |
| Contraction | 74.3% | 72.1% |

These intervals propagate estimated per-slice phonon-shot variance and fitted linear-coefficient uncertainty conditional on fixed calibration. They omit shared reference-profile noise, other covariance, calibration/systematic uncertainty and model discrepancy; with approximately three preparations per ramp time, each variance estimate is itself imprecise. The fractions are descriptive and their components are correlated. Nevertheless, the discrepancy from the synthetic calibration warns that these conditional intervals are not adequate as real-data uncertainty statements. It does not uniquely identify the cause.

## Post-hoc sensitivity check

Keeping the procedure unchanged, uniformly scale each selected initial static-control frequency by ±5% for both models, then refit the non-ramp coefficients. This is a deliberately illustrative stress test chosen **after** the first scores, not a measured 5% calibration uncertainty and not a new model-selection search.

| Branch | Frequency scale | RMSE H − RMSE Z |
|---|---:|---:|
| Expansion | 0.95 | −115.2 |
| Expansion | 1.00 | −54.9 |
| Expansion | 1.05 | +9.2 |
| Contraction | 0.95 | −0.9 |
| Contraction | 1.00 | −5.5 |
| Contraction | 1.05 | −16.1 |

The expansion ranking reverses at the +5% stress setting; the contraction difference remains small relative to the scores. This does not establish that a 5% shift is physically allowed. It does show that the conditional bootstrap, which held calibration fixed, cannot support a robust conclusion about relative performance on its own.

## Reproduce and limitations

Obtain the pinned data and install `mat-io==1.0.2` as described in [the ramp audit](EXPANDING_BEC_RAMP_COVERAGE.md), then run:

```sh
SOURCE=/tmp/hubFrct_2021-source/hubFrct_2021-88c8a87aed5961f589db66a7e7e4e97f161ad51c
OPENBLAS_NUM_THREADS=1 python verification/hubble_heldout.py "$SOURCE" > /tmp/hubble_heldout.json
```

The pseudorandom seed is `20261106`. Software and source dependencies are described in the ramp audit; the input files are checked against `verification/hubble_data_inventory.json`. The 95% synthetic threshold, split, two models, and score were set in the plan before scoring; ±5% sensitivity was post-hoc. No new raw experimental data are stored here.

A credible continuation would first reconstruct the complete authors' preprocessing and fit in MATLAB, obtain or estimate covariance from the shared reference-ring preparations, and propagate static-frequency/Q, atom-number, radius and systematic uncertainty jointly. It should test coverage on realistic synthetic data including shared references and evaluate whether pre-ramp data alone identify phase. Until then, no claim of a measured phase residual, a new friction measurement, an independent confirmation, or new gravity physics is warranted.
