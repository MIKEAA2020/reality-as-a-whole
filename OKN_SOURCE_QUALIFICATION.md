# Primary OKN evidence: a qualified measurement route, not a qualitative identity

## 1. Decision and relevance to the constitution

**Admit this source as an inspectable primary-author measurement method and small recorded-eye-trace demo. Do not admit the demo as a calibrated perceptual dataset or a neural identity test.** This is an advance from screening a model description: actual recorded values and every supplied MATLAB function have now been inspected. No participant-level perceptual correspondence or publication result has been reproduced.

The leading constitution remains that an independently anchored qualitative contrast is intrinsic differentiation of an independently individuated concrete organization, not meaning attached afterward to neural symbols. An eye-movement assay can help locate the contrast while reducing reliance on voluntary reports. It cannot make the contrast, identify its neural basis, or establish identity merely by naming an output `Percept`.

**Target discipline:** [H_Q1](QUALITATIVE_IDENTITY_PURSUIT.md) remains the frozen face/object visual-content candidate. This source concerns opposite horizontal motion. Call the distinct proposed target **H_Q2 (motion-content branch)**: within a declared human visual-rivalry domain, independently anchored leftward/rightward experienced-motion occurrences are intrinsic differences between independently specified realized content-maintaining organizations. H_Q2 is a conjectural research target, not a successful application of H_Q1, a claim about all intrinsic visual character, or a subject-counting law. Eye-trace sign is a candidate evidence channel, not the proposed constitutive organization itself.

## 2. Source, attribution, rights, and coverage

Primary-author supplement: Stepan Aleshin, Gergo Ziman, Ilona Kovacs, and Jochen Braun, *Cumulative smooth pursuit analysis of BR-OKN*, linked by its README to *Perceptual reversals in binocular rivalry: improved detection from OKN*, Journal of Vision (2019).

- [Upstream repository at the inspected revision](https://github.com/cognitive-biology/Cumulative-smooth-pursuit-analysis-of-BR-OKN/tree/e97626c304e378123219f9dd5e002b503db23e37).
- Commit: `e97626c304e378123219f9dd5e002b503db23e37`.
- [Local attribution and coverage](sources/external/rivalry_okn/ATTRIBUTION.md), [file hashes](sources/external/rivalry_okn/provenance.json), and [complete upstream tree listing](sources/external/rivalry_okn/tree.json).
- Preserved without modification: README, LICENSE, `demo.mat`, and all ten `.m` functions. Upstream images and editor backup files are not copied. The recursive tree has 28 entries and is not truncated.
- License: **CC BY-NC-ND 4.0**, retained in full. These are third-party materials, not relicensed by this repository. Attribution is not endorsement. Noncommercial/no-derivatives restrictions matter for reuse; this is not an unrestricted software license.

Coverage is bounded: README and all ten function bodies read; demo decoded and audited; full license read. The linked primary article has **not** been retrieved or read. No paper-level performance estimates, subject counts, intervention outcomes, or reporting calibration are asserted from the README or title. No full participant dataset, account access, or additional consent documentation has been obtained. The public demo is used only for the bounded technical audit below; public availability is not a general authorization for other participant-data uses.

## 3. What the supplied recording actually contains

The MAT file has exactly one non-metadata variable, `gx`, a `1 × 121021` float64 array. The README identifies it as left-eye horizontal position recorded with an EyeLink 1000 at 1 kHz. Sampling rate, display bounds, and instrument identity are **README metadata**, not fields independently recovered from the MAT file.

| Directly checked property | Result |
|---|---:|
| Position samples | 121,021 |
| Finite numeric samples | 121,021 |
| Position minimum / maximum | 197.39999389648438 / 100,000,000 |
| Samples outside the README display interval [0, 1200] | 131 |
| Contiguous outside-interval runs | 3 |
| Samples in their independently computed ±50-sample neighborhood union | 431 |
| Nominal first-to-last sample span, conditional on 1 kHz | 121.020 s |

All samples being finite does **not** make all samples valid gaze measurements: the large out-of-display values still require handling. The 431-sample number is our own interval-union diagnostic, not a claim to have executed or reproduced the MATLAB cleaning function. It is not the number of samples ultimately retained by the full pipeline, which also filters and excludes other movements.

There are **no stored percept reports, stimulus-event timestamps, trial identifiers, neural recordings, or independent validation labels** in this demo. Nor is there a stored timebase against which to verify synchrony or dropped acquisitions. These are precise package-content findings, not assertions that the authors never collected such observations elsewhere.

## 4. Where the inferred labels come from

The source-defined dependency path is:

\[
\texttt{gx}\longrightarrow\text{movement selection and cumulative pursuit}
\longrightarrow\text{resampled interpolants}
\longrightarrow\text{velocity quantiles}
\longrightarrow\text{crossing events and \texttt{Percept}}.
\]

| Source stage | Inspected operation | Evidential role and limitation |
|---|---|---|
| `removeOffscale`, `filterEMT` | Exclude out-of-display values and adjoining samples; combine forward/backward moving averages | Movement-data processing, not phenomenal discrimination |
| `extractPursuit` | Select slow segments using filtered velocity/acceleration and duration; retain raw positions at selected times | Original retained values are not the same thing as an unprocessed/unselected record |
| `shiftPursuits`, `fitOffset` | Shift pursuit segments using quadratic-fit error minimized with `fmincon` | Reconstruct cumulative pursuit, not observed position throughout interruptions; Optimization Toolbox dependency |
| `splineEMT` | Random retained-point subsampling and PCHIP interpolation | A stochastic estimator; no local RNG seed call appears in this function |
| `getVelocity` | Numerically differentiate, take 0.025/0.5/0.975 quantiles, interpolate derivative timing | Distribution across fitted curves, not an independently calibrated probability of reported content |
| `getReversals` | Find median threshold crossings, select events adjacent to conclusive all-quantile intervals, assign event state | `Percept = sign(Switches(:,2)+Switches(:,3))`; event labels are generated by the procedure, not imported ground truth |

The README's example uses 1,000 splines, a 1/100 subsample factor, and ±0.1 pixel/ms velocity thresholds. These are described settings, **not settings executed in this audit**. No MATLAB runtime was used and no Python reproduction of these functions is claimed. Details such as threshold boundary cases, interpolation behavior around gaps, stochastic variability, and parity with the author's environment remain execution/validation tasks.

The README calls the velocity-quantile envelope a confidence interval. Whatever its validity as an eye-velocity estimator, **95% coverage for a resampling envelope is not a measured 95% accuracy for phenomenal content**. The source itself lists non-reversal reasons for low/zero velocity: slowing, attention/perception lapses, return transitions, mixed motion, and processing artifacts. Transition/uncertain states must therefore not be silently forced into a binary experiential truth label.

## 5. What this does and does not warrant

The useful positive premise is conditional and testable: under specified opposite-motion rivalry conditions, slow OKN direction may provide evidence about experienced direction without requiring a contemporaneous voluntary button press. The package makes the physical measurement procedure inspectable. It does not itself furnish the independently checked reliability relation needed to use that procedure as a qualitative anchor in a new condition.

Write the proposed relationship as

\[
Q\longrightarrow O,\qquad Q\longrightarrow R,
\]

where Q is the anchored content occurrence, O the ocular observation, and R a voluntary report. This is an intended measurement architecture, **not a causal result proved by these files**. Attention, input, motor preparation, and an intervention can affect O and R through other paths. Agreement between two outputs is not independent corroboration unless common causes and error dependence are addressed. Training a neural decoder on O-derived labels and then validating against those same labels tests prediction of the ocular classifier, not an independent identification of Q.

An intervention that changes eye movement directly can change O without changing Q. An intervention that changes reporting directly can change R without changing Q. Neither channel can be presumed reliable under its own disruption; this is why a no-report method is valuable without becoming a report-free foundation for identity. The earlier [observation-identifiability conditions](DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md) still apply. No empirical sensitivity, specificity, or intervention-transport bound is estimated from this single unlabelled trace.

| Warrant | Qualification result |
|---|---|
| Accessible physical observation and analysis description | **Met**, within this small demo and inspected source revision |
| Independent qualitative reference | **Not met by demo**; algorithmic labels alone cannot supply it |
| Time-aligned independent validation of the ocular classifier | **Not supplied** |
| Independently individuated neural maintaining organizations | **Not supplied**; eye positions are not neural recordings |
| Intervention separating maintenance, input, and downstream monitoring | **Not established by this package audit** |
| Constitutive identity / subject incidence / absolute closure | **Not established** |

These are warrant boundaries, not a refutation of H_Q1, H_Q2, the published method, or the complete-absolute account. Incompleteness does not make the candidate false. Conversely, the governing endpoint does not authorize promoting an uncalibrated observation channel into its missing constitution.

## 6. The now-specific empirical gate

The next admissible motion-branch evidence is a documented validation/calibration record with synchronized ocular signals, independently anchored direction judgments (including mixed/uncertain/missing cases), stimulus conditions and timestamps, and the provenance/terms needed for analysis. If it also contains neural observations, define the candidate maintaining organization independently of the labels and distinguish input, maintenance, and monitoring pathways before inspecting target outcomes.

The decisive comparison is **not simply a higher OKN classification score**. First establish a bounded evidence relation in held-out participants/blocks or conditions without temporal leakage. Report delay, gaps, mixed percepts, and agreement failures remain explicit. Then assess transport to a report-reduced condition; do not learn calibration solely in that condition from the same neural feature being claimed as the constitution. A replay condition can help constrain an assay's physical behavior but does not, just by fixing the stimulus, guarantee identical rivalrous experience. Only after these steps can a maintenance-sensitive intervention support the qualitative correspondence; identity still requires the constitutive argument.

For H_Q1 specifically, retain the face/object target and seek its own independent reference; motion-based OKN calibration cannot be imported as though it already applied to object content. For H_Q2, seek the primary study's actual validation observations before fitting a new latent model. This is a concrete acquisition requirement established by inspecting the demo, not another synthetic assignment of qualitative labels.

## 7. Reproducibility and connection to the unified account

Run the supplemental audit with Python and SciPy installed:

```sh
python -m pip install -r verification/requirements-rivalry-okn.txt
python verification/rivalry_okn_source_audit.py
```

The [script](verification/rivalry_okn_source_audit.py) verifies 13 pinned file hashes, MAT variables/shape/type, the numerical diagnostics, and the source statements identifying the label-generation path. The [retained result](verification/rivalry_okn_source_audit.json) is deterministic. Python 3.11.2, NumPy 2.4.6, and SciPy 1.17.1 were used for the recorded run. These supplemental source/data checks are **not** additions to the historical 1,149-test core suite and not a reproduction of the article's results.

The [workspace/algebra/channel bridge](WORKSPACE_ALGEBRA_CHANNEL_BRIDGE.md) explains how an independently specified finite dynamics can support compatible observable and channel presentations. This audit supplies a different missing piece: a physically realized **measurement channel must have a warranted relation to the experiential target**, not merely a well-defined mathematical output. The bridge does not identify ocular states with experiences, nor does this eye trace establish a brain-to-AQFT reduction. A unified constitution must explain the same concrete actuality's physical organization and qualitative disclosure without an extra independent selector. The present evidence improves the choice of empirical route while leaving that identity obligation explicit.
