# What the public expanding-BEC data resolve during the ramp

**Result: the proposed matched-radius phase comparison is not directly supported by the sampled radius/phonon observations.** Decoding the authors' MATLAB objects shows a 2 ms sampling gap across the central ramp in every dynamic data set. In particular, none of the recorded interior time-slice mean radii lies between 20 and 30 μm. This is an observation about the published ensemble averages, not a claimed experimental phase shift or an impossibility theorem for model-based inference.

This continues and updates [the feasibility audit](EXPANDING_BEC_DATA_FEASIBILITY.md). Previously the relevant objects were opaque to our SciPy loader. The third-party BSD-licensed [mat-io](https://github.com/foreverallama/matio) 1.0.2 reads their properties without MATLAB. It is an independent decoder, not an execution of the authors' MATLAB code.

## Data and cross-checks

Source: Banik et al., [Phys. Rev. Lett. 128, 090401 (2022)](https://doi.org/10.1103/PhysRevLett.128.090401), and their [MIT-licensed data/code repository](https://github.com/JQIamo/hubFrct_2021) at commit `88c8a87aed5961f589db66a7e7e4e97f161ad51c`. The independently decoded `A.dataRingType` identifies 11 dynamic expansion and 17 dynamic contraction files (`All`). There are seven static-control files in each directory (`Initial`); their accessible numeric data are duplicated across the two directories, not fourteen independent controls. Equality of all class properties across duplicates has not been established.

To check the decoding and grouping without taking the object's labels on faith, the script:

1. Uses decoded `RunNos_phnEv` to group the separately stored top-level `Runs`, `time`, and `AN` by decoded `EvTime`. The resulting atom-number means reproduce every stored `AN_phnEv_avg` exactly to printed floating-point precision.
2. Independently groups the top-level 1D density profiles and applies the scaled-reference subtraction specified in the authors' `PhononData.m`, using decoded initial/final/ramp reference profiles. It reproduces 1,490 stored normalized profile slices, maximum absolute difference `2.92 × 10⁻¹¹` in the stored profile units. It excludes 56 near-endpoint slices to avoid floating-point ambiguity in assigning their references. This is a cross-check of mapping and arithmetic, **not** a replication of the published fit, a MATLAB comparison, or a verification of calibration and errors.
3. Confirms that SHA-256 hashes of all 42 input files match the previously saved pinned-source inventory. Radius, uncertainty and transition-time properties themselves have not been independently compared with MATLAB or the original images. Individual radius measurements were not among the accessible top-level numeric arrays checked here.

## Sampling result

The object's programmed ramp duration is 10 ms; the paper's quoted **3.6 ms** is the 10–90% rise time, not the full programmed interval. We use a 1 ns tolerance to distinguish the strictly interior ramp samples from endpoints. Each of the 28 dynamic protocols has four interior time slices at offsets **2, 4, 6 and 8 ms** after the programmed start, with three phonon preparations at each such slice. These preparations are repetitions, not four views of one condensate.

The 3.6 ms window centered on the programmed midpoint contains only the 4 and 6 ms slices. Across the dynamic protocols:

| Branch | Dynamic files | Interior mean-radius slices in [20, 30] μm | Closest mean below 25 μm | Closest mean above 25 μm |
|---|---:|---:|---:|---:|
| Expansion | 11 | 0 | 19.950 μm | 35.274 μm |
| Contraction | 17 | 0 | 15.084 μm | 30.200 μm |

The limits in the final columns are extrema over **all interior slices in that branch**, not the two observations from one chosen protocol. They are decoded `MeanRad_avg` point estimates; they do not account for radius calibration systematics, fluctuations or uncertainty. No claim is made that each individual condensate was definitely outside 20–30 μm. These central points lie on different days and under different initial-phase preparations: combining them does not manufacture an observed same-state trajectory or a direct matched-radius phase measurement. The seven static controls span several radii, including intermediate values; they do not fill the missing dynamic ramp images. The static frequencies are fitted quantities, not error-free calibrations.

**Consequence:** any phase evaluated near `R = 25 μm` in either branch must rely on temporal/radius interpolation and a dynamical or phase-reconstruction model, rather than a measurement at that radius. The matching proposed in the earlier audit cannot be represented as an independently observed, model-free radius/phase comparison. The absence of samples in this narrow interval does *not* prohibit fitting the published equations to the full data or predicting held-out ramp observations.

## A synthetic identifiability check—not an experimental result

`verification/hubble_phase_identifiability.py` takes the actual time grid from one expansion and one contraction file. It generates two **synthetic**, monotone phases

```
φ±(t) = ω(t − t₀) ± ε sin²[π(t − tL)/(tR − tL)]  for tL < t < tR,
φ±(t) = ω(t − t₀)                               otherwise,
q±(t) = sin φ±(t).
```

Here the gap `[tL,tR]` is 4–6 ms after ramp start, `ω = 2π × 50 s⁻¹`, and `ε = 0.1 rad`. The 50 Hz is illustrative, not a fit. At all the sampled times in either selected file, the two `q` values agree exactly; their derivatives agree there as well. At the midpoint their phases differ by 0.2 rad, while both phase rates stay positive (analytical lower bound ≈157 rad/s). These toy signals are **not fitted to the observed profiles**, and 0.2 rad is neither an experimental measurement nor an uncertainty estimate.

The general point is narrower and stronger than a numerical example: finite samples do not, by continuous differentiability and monotonicity alone, determine the phase between samples. Restricting the oscillator to a specified differential equation, calibrated initial state, and error model can select an interpolant; then the conclusion is conditional on those assumptions. The synthetic test does not show that the two signals solve the authors' homogeneous oscillator equation or fit their actual data, nor that their fitted model is wrong. Eckel et al. already discuss phase changes and Banik et al. study phase-dependent nonadiabatic attenuation, so neither a modeled shift nor a branch difference would by itself be a new discovery.

## Reproduction

First obtain the pinned source using the command in the [previous audit](EXPANDING_BEC_DATA_FEASIBILITY.md). Install `mat-io==1.0.2` in an isolated Python environment (its dependencies include NumPy ≥2.2.2, SciPy ≥1.15, pandas ≥2.2 and h5py ≥3.13). Then:

```sh
SOURCE=/tmp/hubFrct_2021-source/hubFrct_2021-88c8a87aed5961f589db66a7e7e4e97f161ad51c
python verification/hubble_ramp_coverage.py "$SOURCE" > /tmp/ramp_coverage.json
python verification/hubble_phase_identifiability.py "$SOURCE" > /tmp/phase_example.json
```

The saved outputs are [ramp coverage](verification/hubble_ramp_coverage.json) and [synthetic check](verification/hubble_phase_identifiability.json). The scripts record expected source provenance but do not themselves verify the Git revision; compare file hashes with [the pinned inventory](verification/hubble_data_inventory.json). Runtime versions used here: Python 3.11.2, mat-io 1.0.2, NumPy 2.4.6, SciPy 1.17.1, pandas 2.3.3, h5py 3.16.0.

## Next test if continuing with these data

**Follow-up:** An exploratory held-out test was subsequently run. See [the results](EXPANDING_BEC_HELDOUT_RESULTS.md); real-data conditional intervals under-cover and the model comparison is sensitive to calibration.

A more defensible target is **model-dependent held-out prediction of measured density amplitudes**, rather than claiming a direct phase observation at 25 μm. Specify the authors' published oscillator/radius model and competing reference models in advance; train on fixed-radius controls and non-ramp samples, holding out the four interior time slices of each selected protocol. Check whether initial phase and nuisance parameters can be identified from training data alone—especially for short pre-ramp expansion records—before examining holdout residuals. Avoid leakage through shared normalization references and account for their covariance and duplicated controls. Use synthetic data generated from the cited dynamics and the actual sampling/noise model to test recovery and coverage. If training does not identify the phase without the held-out slices, report that failure; do not turn a same-data fit into a prediction. Only after those checks would experimental residuals and uncertainty bands be meaningful.

This would test a specified analogue-oscillator model, not internal POVM clocks, the Einstein equations, or the problem of time in quantum gravity. Its novelty relative to the published global analysis remains unverified.
