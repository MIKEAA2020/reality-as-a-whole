# BEC static controls and shared-run covariance

**Result:** A Python fit to the released scalar control traces closely reproduces the saved static frequencies and Q values. The controls also overlap run-by-run with one set of dynamic reference images, making calibration and reference errors correlated. We can demonstrate part of that covariance under a specified conditional model, but this is not yet a complete uncertainty budget or a replication of the published global fit.

This is an exploratory continuation after seeing the [held-out results](EXPANDING_BEC_HELDOUT_RESULTS.md) and [reference audit](EXPANDING_BEC_REFERENCE_UNCERTAINTY.md). Neither MATLAB nor Octave is installed in this workspace. The MATLAB audit script provided below has **not** been executed; Python results do not establish exactly how the original MATLAB fit was performed.

## 1. Recovering the saved static fits

The [Banik et al. source repository](https://github.com/JQIamo/hubFrct_2021), pinned at `88c8a87aed5961f589db66a7e7e4e97f161ad51c`, contains seven unique fixed-radius controls (the two directories duplicate them). The decoded objects contain `deltan_avg`, `fi` and `Qi`, among other fields. The released source includes the static damped-sinusoid model, but the precise code path that populated every saved `fi` and `Qi` has not been identified or run here.

As an independent check, fit each saved scalar `deltan_avg` trace by **unweighted** least squares to

```
exp(−γt) [a cos(2π f t) + b sin(2π f t)],    Q = πf/γ.
```

This is the standard static damped-sinusoid form in the published code, not a new derivation. The Python fit profiles out `a,b`, uses multiple starting frequencies below Nyquist, and does not use the saved `fi` or `Qi` to choose its minimum. Across all seven controls, it matches the stored frequency to within **0.00380 Hz** and the stored Q to within **0.00203**. For the 38.37 μm control, the fit gives `f = 19.98498 Hz`, `Q = 8.31346`, versus the stored `19.98461 Hz`, `8.31433`. This agreement is a useful consistency check; it does not by itself prove the provenance, errors, fit options or uncertainty of the stored values.

We also checked the scalar extraction: projecting the stored normalized 1D profiles onto the sinusoid at the *stored azimuthal angle* reproduces `deltan_avg` within 0.00841 profile units across controls. The angle is treated as fixed in the following simulation; its estimation uncertainty is not propagated. For the 38 μm control, grouping and normalization of the individual saved profiles reproduce its mean normalized profiles to `1.46 × 10⁻¹¹` profile units.

For comparison only, a more flexible two-spatial-component fit with independent temporal coefficients and constant offsets yields frequency differences from the stored values up to 2.26% and Q differences up to 42.3%. This is a **different fit model**, not evidence that the saved fits are wrong; it illustrates sensitivity to preprocessing and model specification. In particular, it should not be substituted for the authors' fit without validation.

The source's static `RingStat_phnEv_2D.m` and dynamic `PhnAmpDynamicDiffEq.m` use related but not identical damped-oscillator conventions. The exact interpretation of a stored `fi` as a damped or undamped frequency should be checked against the original workflow. The previous held-out model's convention is an assumption, not established by this fit agreement.

## 2. Sampling aliases: a constraint, not a discovery

All seven fixed-radius control traces are uniformly sampled. For the 38 μm control, the time spacing is 8 ms, giving sampling frequency 125 Hz and Nyquist frequency 62.5 Hz. The sinusoid design matrices at `f ≈ 19.985 Hz` and `125 − f ≈ 105.015 Hz` span the same two-dimensional space on those sample times (including the arbitrary phase); multiplying by the same exponential envelope preserves this equivalence. The script checks the corresponding sampled basis identity numerically for all controls, with max errors below `4 × 10⁻¹⁴`.

This is standard sampling aliasing, not a new physical effect and not evidence the published frequency is wrong. A frequency range, other measurements, or physical calibration can select a branch. Our fits explicitly impose the sub-Nyquist branch; the bootstrap below is conditional on that choice and cannot test alias uncertainty.

## 3. Correcting the reference-noise assumption

Each same-day dynamic initial-reference set consists of **30 recorded times with two preparations per time**, not 60 obviously exchangeable draws from one distribution. The previous reference audit computed its initial-reference noise using the pooled 60-shot sample covariance. Here, as a sensitivity check, we instead hold the observed 30 time strata fixed and sum their within-stratum sample-mean covariances, with each stratum weighted by its observed number of shots. The rest of the first-order H-model residual covariance and all model inputs are held fixed. Two samples per stratum leave very weak information about within-time variance; neither assumption handles day-level drift or all experimental covariance.

| Branch | Median stratified/pooled variance of the initial-reference contribution | Median stratified/pooled **total conditional residual SD** | 10th–90th percentile of total-SD ratio |
|---|---:|---:|---:|
| Expansion | 0.423 | 0.9988 | 0.9771–1.0000 |
| Contraction | 0.662 | 0.9998 | 0.9770–1.0007 |

Thus the initial-reference component changes appreciably under this assumption, while the **marginal total** conditional SD changes little at the median in this model. This is not a demonstration that either method estimates the experiment's true uncertainty. The previous 1.19/1.25 median SD increases referred to a different comparison—adding several shared-reference effects versus a shot-only model—and should not be read as an isolated pooled-initial-reference effect.

## 4. Paired calibration/reference sensitivity

For the 38 μm static control, its 60 date/run IDs match the initial-reference IDs used by five contraction protocols. The static and dynamic files have different saved 1D profile representations for the same run IDs. The paired calculation aligns **identities**, not numerical equality, and uses the corresponding representation for each purpose.

For each of 500 fixed-seed Gaussian multiplier draws, use the same shot multipliers for the paired static and dynamic-reference profiles within each two-shot time stratum. Recompute the static control's mean profile, its self-derived normalization reference and the fixed-azimuth scalar damped-sinusoid fit; simultaneously recompute the dynamic initial-reference mean. Frequencies are restricted to the same sub-Nyquist branch. The resulting static frequency and Q fluctuate together with that reference. Propagate them to the five H-model held-out residual vectors using finite-difference derivatives around the previous **stored-control** fit; the alternate refitted estimator is close but not identical to the original control estimate. Nonlinear parameter propagation and the estimation of the stored azimuthal angle are not included.

Under these conditional assumptions:

- Static fit-draw SDs are approximately **0.327 Hz** for frequency and **1.45** for Q. The 2.5th–97.5th draw quantiles are 19.423–20.628 Hz and Q 6.33–11.98. They describe these draws, **not validated experimental confidence intervals**; they depend on two-shot strata, Gaussian multipliers, the fit and preprocessing choices.
- The draw correlation between fitted frequency and the dynamic reference's sine component is approximately **−0.40**. This is a model-specific covariance estimate, not an independently measured universal correlation.
- For the 40 held-out components in those five protocols, the median ratio of paired versus artificially independent **calibration-plus-initial-reference-only** residual SD is **0.985**; its 10th–90th percentile is **0.898–1.063**. This is not the ratio for total residual uncertainty and says nothing by itself about model preference. Other noise, radius/atom-number uncertainties, drift, static azimuth uncertainty and model mismatch are omitted.

## 5. Reproduction and validation

Use the data acquisition and environment instructions in [the ramp audit](EXPANDING_BEC_RAMP_COVERAGE.md). With `mat-io==1.0.2`, NumPy and SciPy installed:

```sh
SOURCE=/tmp/hubFrct_2021-source/hubFrct_2021-88c8a87aed5961f589db66a7e7e4e97f161ad51c
OPENBLAS_NUM_THREADS=1 python verification/hubble_static_stratified.py "$SOURCE" > /tmp/static_stratified.json
OPENBLAS_NUM_THREADS=1 python verification/hubble_static_joint.py "$SOURCE" > /tmp/static_joint.json
```

Both Python scripts check the 42 source MAT hashes against the saved inventory. Outputs are [static/stratified results](verification/hubble_static_stratified.json) and [paired sensitivity](verification/hubble_static_joint.json). The latter uses seed `20261108`. Checks include reconstruction of static normalized profiles, a noise-free synthetic frequency/damping recovery, ten multi-start checks of bootstrap fits, and an independent paired-multiplier covariance calculation (1.1% relative error in a synthetic case). Calibration derivatives agree with half-step differences to within 0.15% in norm for these five protocols. The simulation checks implementation under assumed noise, not experimental coverage. They do not validate the actual MAT-file generation procedure.

For an independent MATLAB check, [hubble_matlab_audit.m](verification/hubble_matlab_audit.m) loads the original objects, reconstructs reference and normalized profiles, reports the static `fi/Qi` fields and endpoint choices, and asserts reconstruction agreement. Verify the source hashes first and run it in the authors' MATLAB R2020a/b environment. **It has not been run or validated in MATLAB here**, does not execute `main.m`, and does not refit static or global parameters. A MATLAB comparison of the original fits and a full covariance/error model remain open. These results do not test a gravitational clock or solve the problem of time.
