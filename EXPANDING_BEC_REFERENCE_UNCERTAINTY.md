# BEC ramp holdout: shared-reference and endpoint audit

> **Follow-up:** [The static-control audit](EXPANDING_BEC_STATIC_CONTROL_AUDIT.md) shows that each 60-shot initial-reference set consists of 30 time strata with two preparations each. The calculations below treat those 60 shots as one exchangeable group; a stratified sensitivity calculation and paired static/reference propagation are now available in the follow-up. The original numbers remain conditional, not final experimental uncertainties.

**Status: exploratory uncertainty diagnosis, not a new friction measurement.** The source data allow us to reconstruct the authors' stored normalized profiles and to propagate a specified part of the shared-reference uncertainty. This corrects an inconsistency in our earlier conditional error calculation and strengthens the reason not to interpret that calculation as a physical significance test. A full experimental covariance remains unavailable in this analysis.

## Reconstructing the stored profiles

Using the 28 dynamic files from the [pinned source repository](https://github.com/JQIamo/hubFrct_2021) for [Banik et al. (2022)](https://doi.org/10.1103/PhysRevLett.128.090401), `verification/hubble_reference_uncertainty.py` groups the released per-preparation **processed 1D profiles** by date, run and time. It reproduces the stored mean profiles at *every* dynamic time slice, including the 56 endpoints left out of the previous audit, to within `2.92 × 10⁻¹¹` in profile units. It also reconstructs the decoded initial, ramp and final reference means. This is a Python reconstruction using the independently decoded fields and source operations, not a run of MATLAB or the original image processing.

Every dynamic file uses 60 initial-reference run IDs, shared within its experimental date:

| Date | Protocols sharing those 60 runs |
|---|---:|
| 2021-02-23 | 5 expansions |
| 2021-02-24 | 6 expansions |
| 2021-02-20 | 5 contractions |
| 2021-02-22 | 6 contractions |
| 2021-02-25 | 6 contractions |

The processed initial-reference arrays are exactly identical across dynamic files within each date. The final reference is different: in all 28 dynamic files the explicit final-reference run list is empty, and the stored final reference is the equal-time-slice average of the unnormalized **post-ramp phonon profiles**. Therefore, final-reference uncertainty and post-ramp training data are correlated.

There is a further reuse: the 60 date/run IDs in the 2021-02-20 initial reference also occur in the static 38 μm control used by the prior fit. However, the saved 1D profiles for these run IDs are not numerically identical between the static and dynamic files: none of the 60 profile pairs is exactly equal. They appear in different processed representations, so the same run identity must not be taken to imply equal arrays. We have not reconstructed the original images or the static fit; our new uncertainty calculation holds the static frequency and Q fixed and does **not** propagate this additional dependence.

## Seven endpoint reference choices and correction to our previous analysis

For 3 expansion and 4 contraction files, the saved normalized profile at the nominal `t₀ + 10 ms` ramp endpoint is reproduced using the **last ramp reference** (the `t₀ + 8 ms` reference), not the saved final-ring reference. At that endpoint, the loaded floating-point time is slightly less than the loaded sum `t₀ + t_exp`; the source normalization loop tests exact inequalities and does not clear the previous reference if it finds no corresponding intermediate reference. This is a plausible code-level explanation of the stored result and is exactly reproduced by the Python reconstruction. We have **not** run MATLAB to establish the complete provenance, author intent, or impact on the paper's published fits; this is not a claim that the paper's conclusions are invalid.

Our previous held-out test used the stored profiles for the point predictions and scores, so **the previously reported RMSEs remain the same**. But its shot-variance helper assigned the final reference to all nominal end slices. For these seven slices that assignment does not match the saved training outcome, and it also missed the shared reference with the held-out 8 ms slice. The earlier conditional interval calculation is therefore inconsistent at these endpoints, in addition to omitting common-reference uncertainty elsewhere. We have added a correction notice to [the prior results](EXPANDING_BEC_HELDOUT_RESULTS.md).

As a post-hoc sensitivity check—not a replacement for the published pipeline—we replaced just those seven stored endpoint training profiles with profiles normalized using the **already saved** final-reference mean, leaving the holdout slices and all fixed model inputs unchanged, and recomputed the linear training fit. We did not recompute the final reference itself or re-run the authors' fit. The branch-level H-minus-Z holdout RMSE difference changes from −54.9 to −57.4 for expansion and from −5.5 to −6.4 for contraction, in stored density units. This particular preprocessing change does not materially alter the earlier **descriptive** model ranking, but does not establish that either normalization choice is correct for a new analysis.

## Conditional shared-reference propagation

We revisited model H (`gamma_H = 0.5`) from the prior held-out test, keeping its oscillator, static-control fits, mean radius curves and atom-number trajectories fixed. For each group, Gaussian multipliers generate mean-profile fluctuations whose conditional covariance is the observed sample covariance divided by group size. Identical initial-reference multipliers are reused for all protocols on the same date. Ramp-reference groups are varied separately; the final reference is recomputed from the same fluctuating post-ramp phonon time slices, preserving their dependence. The full nonlinear scaled-reference subtraction and the non-ramp coefficient refit are recalculated in each of 2,000 draws. The seven endpoint reference choices above are retained as stored.

This is **not a full bootstrap of the apparatus**. It assumes independent preparation groups except for the modeled reuse, treats the small-sample covariance estimates and the remaining model inputs as fixed, and assumes Gaussian mean fluctuations. It does not propagate static-frequency/Q errors, their correlation with reused runs, atom-number and radius fluctuations, camera calibration, drift, reference selection uncertainty, or model discrepancy. There are only about three preparations in each ramp group. These are conditional sensitivity diagnostics, not valid unconditional prediction intervals or evidence for either friction model.

Compared with the earlier shot-only conditional standard deviations for the 4 × 2 held-out components per protocol:

| Branch | Median new/old conditional SD | 10th–90th percentile of ratios | Observed fraction within ±1.96 old SD | Within ±1.96 new SD |
|---|---:|---:|---:|---:|
| Expansion | 1.19 | 1.02–2.38 | 61.4% | 77.3% |
| Contraction | 1.25 | 1.04–1.98 | 74.3% | 89.7% |

The SD ratios also reflect correcting the previous endpoint-variance inconsistency, not only adding a common reference term. The fractions are descriptive comparisons to zero-residual bands; the 88 expansion and 136 contraction components are correlated, and these fractions are **not** demonstrated 95% coverage. Their increase does not validate the assumed Gaussian model or resolve the remaining uncertainty deficit.

The complete `224 × 224` conditional H-residual covariance is saved in the [JSON output](verification/hubble_reference_uncertainty.json), ordered by record, then increasing held-out time, then sine/cosine. The same-day shared-initial-reference contribution alone has mean absolute cross-protocol correlation about **0.007** and maximum about **0.199** under an independent first-order delta calculation. These are model-specific descriptive summaries across many correlated pairs; the maximum is not a significance test. The finite-draw full covariance also includes Monte Carlo noise. Shared preprocessing is real, but these numbers should not be mistaken for a complete estimate of all day-level drift or common calibration.

## Verification and next gate

- All 42 input hashes are checked against the pinned inventory; all 28 dynamic profile reconstructions pass.
- A synthetic shared-multiplier covariance check agrees with its analytical cross-covariance to 7.1% in Frobenius norm (2,000 draws; acceptance threshold 10%). This checks the implementation, not the experiment's Gaussian assumption.
- For all 224 marginal residual SDs, an independently coded finite-difference delta-method calculation agrees with the multiplier SD to within 5.0% relative. Both use the same assumed independent-group sample covariances; this is not independent physical validation.
- Point scores from the new code reproduce the original H and Z RMSEs exactly. The endpoint sensitivity update is checked against a direct changed-training-data calculation.

Reproduce using the Python environment and source location from [the ramp audit](EXPANDING_BEC_RAMP_COVERAGE.md):

```sh
SOURCE=/tmp/hubFrct_2021-source/hubFrct_2021-88c8a87aed5961f589db66a7e7e4e97f161ad51c
OPENBLAS_NUM_THREADS=1 python verification/hubble_reference_uncertainty.py "$SOURCE" > /tmp/hubble_reference_uncertainty.json
```

The random seed is `20261107`. The saved [script](verification/hubble_reference_uncertainty.py) and [output](verification/hubble_reference_uncertainty.json) contain details and per-protocol values. The analysis design was made after the initial held-out results; it is exploratory, not a prospective preregistered test.

The next meaningful step is independent MATLAB replication of the saved profile/reference behavior and the static-control fits, followed by joint propagation of their run-level dependence, radius/atom-number calibration, and drift. If those dependencies cannot be recovered from the published processed profiles, a complete uncertainty budget needs additional apparatus data or collaboration with the authors. Neither the present conditional calculation nor its apparent endpoint behavior tests gravitational time or establishes an unresolved physics problem has been solved.
