# Expanding-BEC clock comparison: public-data feasibility audit

> **Update:** The MATLAB object fields were subsequently decoded and checked. See [the ramp-coverage follow-up](EXPANDING_BEC_RAMP_COVERAGE.md) for the measured sampling gap and the resulting limits on a matched-radius phase comparison. Statements below about not yet recovering the objects describe the initial audit.

**Status: data inventory and test design, not an experimental result.** The public Banik et al. data support a serious *ensemble-level* analysis in principle. They do not supply a continuous trajectory from repeated imaging of one condensate: the paper reports one image per repetition. I have not recovered the `PhononData` class properties or fitted clock phases, so the proposed analysis has not been shown to be identifiable or statistically powerful in these data. Nothing here tests the FRW internal-POVM construction or establishes a new physical law.

## Source and prior art

- [Banik et al., Phys. Rev. Lett. 128, 090401 (2022)](https://doi.org/10.1103/PhysRevLett.128.090401), [preprint](https://arxiv.org/abs/2107.08097); source [data and MATLAB code](https://github.com/JQIamo/hubFrct_2021) at commit `88c8a87aed5961f589db66a7e7e4e97f161ad51c` (MIT-licensed repository). The preprint lists it as ref. 29; numbering differs in the published version.
- [Eckel et al. (2018)](https://doi.org/10.1103/PhysRevX.8.021021) already model expansion-induced changes in phonon phase and amplitude. Banik et al. explicitly study phase-dependent attenuation and amplification in nonadiabatic expansion/contraction, including fixed-radius controls. Their defined phase at peak is itself an integral of the modeled frequency; a comparison using that very same integral as both prediction and measurement would be circular.
- [Eckel and Jacobson (2021)](https://doi.org/10.21468/SciPostPhys.10.3.064) analyze phonon redshift and expansion friction. [Barontini (2026)](https://doi.org/10.1103/1h9j-df4k) investigates relational/entropic time in a different cold-atom apparatus (see `COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md`). These are substantial prior art. The particular held-out residual comparison below is a **candidate analysis**, not a confirmed novel result; the literature search was targeted, not exhaustive.

## What was verified in the repository

`verification/hubble_data_inventory.py` reads all published `.mat` files using SciPy without decoding MATLAB objects. At the pinned revision it finds:

| Check | Result |
|---|---:|
| Files in expansion / contraction directories | 18 / 24 |
| 100-bin `n1Ds` arrays, aligned with top-level `Runs`, `time`, `AN` | 42 / 42 |
| Non-finite top-level `time` and `n1Ds` values | 0 / 0 |
| Files with an opaque `PhononData` object | 42 / 42 |
| Same filenames in both directories | 7 |
| Of those 7, identical `Runs`, `time`, `AN`, `n1Ds` arrays | 7 / 7 |

The 42 files have different byte-level SHA-256 hashes; this does **not** imply 42 independent datasets. Those seven identically named file pairs share the four accessible numeric arrays despite different MAT-file headers, and the shared data must not be double-counted. Equality of the opaque objects has not been checked. The author's global fit identifies dynamic (`All`) and static (`Initial`) data via properties of those objects; the accessible arrays alone do not validate that classification.

Example: `data/expansions/PhnRuns_2021-02-24_0827-0946.mat` has a `100 × 192` `n1Ds` array and 192 time entries, with 68 distinct time values after rounding to 1 ns. **These are not 192 phonon measurements:** the author's `Det_n1Ds` concatenates phonon and initial/intermediate/final reference-ring runs. Role labels, normalization, angular coordinates, radius estimates, expansion timing, and fit results are properties of the `A` object. The author's normalization subtracts a scaled reference profile, with an appropriate time-dependent reference during the ramp. The raw arrays are processed one-dimensional density profiles and metadata, not the original two-dimensional images. The filename is not sufficient to classify every column.

SciPy exposes `A` as an opaque MCOS object; it does not expose `A.MeanRad_avg`, `A.MeanRad_dev`, `A.EvTime`, `A.t_phn1`, `A.t_exp`, `A.AzAngle`, or the run-role and normalization fields directly in our inventory. The source class lists those properties and the analysis code uses them, but we have not independently decoded and validated their numerical values. The available summaries include radius averages and deviations, not necessarily shot-level radius–phonon covariances. Whether the MAT objects or other accessible files contain sufficient per-shot radius information remains to be verified in MATLAB. The paper's one-image-per-repetition method rules out a directly observed continuous within-condensate trajectory.

## Reproduction

With NumPy, SciPy, `curl`, and `tar` installed, from the root of this repository:

```sh
curl -L --fail https://codeload.github.com/JQIamo/hubFrct_2021/tar.gz/88c8a87aed5961f589db66a7e7e4e97f161ad51c -o /tmp/hubFrct_2021.tar.gz
mkdir -p /tmp/hubFrct_2021-source
tar -xzf /tmp/hubFrct_2021.tar.gz -C /tmp/hubFrct_2021-source
python3 verification/hubble_data_inventory.py /tmp/hubFrct_2021-source/hubFrct_2021-88c8a87aed5961f589db66a7e7e4e97f161ad51c > /tmp/hubble_inventory.json
```

The observed archive SHA-256 was `6025bd5ac8a66e661d0ed1fe2ae3adb9673a0a236f3b441bc0c96df96753f85f`. GitHub archive bytes may change even if the commit contents do not; per-file hashes appear in `verification/hubble_data_inventory.json`. The script prints the expected commit but does **not** independently verify it; verify the source by checkout/commit hash if needed. No source data are vendored here. The repository README calls for MATLAB R2020a/R2020b and runs `main.m` to generate the supplemental fit tables; no MATLAB execution has been performed in this audit.

## Candidate falsifiable comparison

A radius-vs-phonon comparison is only meaningful after specifying how the phase is reconstructed. A single real standing-wave density amplitude does not supply two instantaneous quadratures; simply unwrapping its spatial phase does not recover its temporal phase. Fit an explicitly declared, independently validated oscillator-state estimator to the density profiles, including reference subtraction, angular offset and damping; check that it can resolve cycle count and phase in the short, nonadiabatic ramp. Treat uncertainty and possible zero-amplitude phase failures as part of the result, not as data to silently discard. Laboratory time is required for this reconstruction and calibration, so this is not a test of a timeless quantum constraint.

Let `R_b(t)` be the measured ensemble radius curve for a protocol `b` and let `φ_b(t)` denote the independently reconstructed, unwrapped **temporal** phase under a specified convention. Let `ω_ref(R)` be calibrated from independently held-out fixed-radius runs, with any atom-number dependence explicitly included or controlled. For monotone usable ramp portions, choose a common reference radius `R*` and set

```
E_b(R) = [φ_b(t_b(R)) − φ_b(t_b(R*))]
         − ∫[t_b(R*) to t_b(R)] ω_ref(R_b(u)) du .
D(R) = E_expansion(R) − E_contraction(R).
```

Here `t_b(R)` is the branch-specific inverse curve; the lower integration limit can be later than the upper one on a contraction. The operational null is that the independently estimated phase increments follow this **specified** static-frequency integral in both protocols; then `E_b=0` and `D=0`, within predeclared uncertainties. `D=0` alone is weaker and can hide common residuals. Ordinary branch-dependent elapsed times and redshift are already in the integral; a raw expansion–contraction phase difference alone is not evidence of extra dynamics. The null is an operational reference model, **not** a general prediction for rapid nonadiabatic ramps; established oscillator dynamics can predict nonzero residuals. In particular, the experiment's amplitude depends on initial phase, and an apparent phase shift may be conventional or model-dependent. A rejection would motivate comparison with the already-published dynamical equations, not claim new gravity or new clock physics.

For a real analysis, first inspect the MATLAB object fields and verify that there are enough ramp-region observations and overlapping independently reconstructed phases. Predefine the radius interval away from endpoints, with a lower bound on `|dR/dt|` and a phase-quality threshold. Align at `R*` only when branch-specific phase offsets are identifiable; assess dependence on this choice and on phase conventions. Fit the reference using static controls without using the assessed dynamic traces; compare held-out dynamic time slices or runs to predictions, not a phase computed by integrating the very same `ω_ref`. Evaluate whether the static controls cover the intermediate radius range; if they do not, explicitly label interpolation/extrapolation and its model uncertainty. Use separate expansion and contraction preparations, not a fictitious single reversal.

For uncertainty, propagate radius calibration, reference-frequency fit, normalization and oscillator-estimator uncertainty jointly; resample independent experimental preparations and shared reference datasets as clusters, preserving their reuse and correlations. Include known shared systematic uncertainties separately, and account for multiple radius values with a prespecified simultaneous band or scalar contrast. Report phase ambiguity, missing radius coverage and failed fits; use simulated coverage and alternative reasonable phase estimators as sensitivity checks, **not** experimental measurements. Shared static data must enter only once. Atom number, initial phase, ramp rate and damping should be matched or included in the model; phase-dependent nonadiabatic effects and radial-mode coupling are established confounders. If fit identification or coverage fails, do not report `D` as measured.

## Concrete next step / stopping condition

Run the authors' code in its documented MATLAB environment and export ordinary numeric arrays and the relevant `A` properties with provenance. Cross-check against the published tables, distinguish phonon from reference runs, establish which radius and density observations are paired, and inspect independent ramp-time coverage. Then test estimator recovery on simulations generated from the cited dynamics, including branch-specific sampling and normalization. Only if this validation and the controls support a held-out analysis should numerical `E_b` or `D` be reported with intervals. If they do not, a new experiment should record jointly calibrated radius and two phonon quadratures, or otherwise validated phase information, under separately phase-matched expansion/contraction protocols with repeated preparations and fixed-radius controls.
