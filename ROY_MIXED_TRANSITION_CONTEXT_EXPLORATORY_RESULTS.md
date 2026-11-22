# Mixed reports, transition controls and EEG-window context

## Bottom line

I reused the already supplied S01, S02 and S09 rivalry EEG files to investigate the [weak frozen S02 mixed-report result](ROY_S02_FROZEN_REPORT_CENTER_TRANSFER_RESULTS.md). **No additional participant files are needed for this diagnostic.** All three participants were already inspected, so these are exploratory observations, not an independent test or a statistically established cause of failure.

- **Window context differs greatly across participants.** At clean mixed-report centers, the mean fraction of the surrounding two-second EEG window carrying the reconstructed mixed code was **16.2% for S01, 53.1% for S02 and 63.8% for S09**. A mixed label at the center therefore does not imply a uniformly mixed two-second window; this is especially pronounced for S01.
- **Timing matters under the assumed labels.** For selected mixed segments with matched controls, only **15.8%** of S01 center labels remained mixed 0.2 seconds earlier and **12.9%** remained mixed 0.2 seconds later. The corresponding values were **43.1%/43.6% for S02** and **69.7%/72.3% for S09**. This is sensitivity of the reconstructed label to a hypothetical shift, not a measurement of actual report latency or a reason to choose a favorable lag.
- **The matched EEG contrast was not consistent across the three people.** The mean mixed-minus-control POz log-power-ratio difference was **+0.038 for S01, −0.068 for S02 and +0.159 for S09**. Matching was partial and the observations remain dependent. These signed differences cannot establish a reliable mixed-specific signal or identify why the original model failed.

**Decision:** Do not use these findings to claim that a redesigned mixed detector is validated or to request another participant yet. This diagnostic did not establish a sufficiently credible, specified replacement candidate. The previous negative S02 result stands. Other EEG methods might work, but this analysis does not show which one would.

## 1. Scope and source integrity

The [exploratory plan](ROY_MIXED_TRANSITION_CONTEXT_EXPLORATORY_PLAN.md) was written after the earlier participants and S02 test had been inspected. It is a descriptive follow-up, not prospective preregistration. The six S01 rivalry scans 1,3,5,7,10,12 and five S09 rivalry scans 1,2,3,5,7 were re-fetched from the previously supplied Dropbox files; S01 sizes and content hashes matched the previous listing and S09 SHA-256 values matched prior committed inspections. S02 scans 1,2,4,6,8,11 matched the [prior SHA-256 receipt](verification/roy_s02_dropbox_integrity_receipt.json). Raw files remain in ignored private storage and are not published. These checks verify consistency with prior inputs, not authenticity against the original public archives.

All analyses reuse the previous provisional reconstruction: 250 Hz sampling, five assumed 42-second trials per run, report code carried forward after each marker, 0.2-second centers and two-second POz EEG windows. Scan condition and onset assumptions are not independently verified acquisition logs. Reported codes are not independently observed private experiences. No S03 data, fMRI alignment or author correspondence was used.

## 2. Window context and artifact coverage

Each row describes windows whose *center* was labeled mixed. Sample fractions and squared-Hann taper fractions describe the reconstructed report states under the EEG window; they are not measures of phenomenal content or additive allocations of spectral power. Mean-centering, Fourier phases and interference prevent interpreting taper weight as the amount of tag power caused by a state.

| Participant | Clean mixed centers | Mean mixed sample fraction in 2 s | Median mixed sample fraction | Mean squared-Hann weight on mixed samples |
|---|---:|---:|---:|---:|
| S01 | 399 | 16.2% | 11.6% | 33.8% |
| S02 | 736 | 53.1% | 55.8% | 70.9% |
| S09 | 1,057 | 63.8% | 62.6% | 80.1% |

Averaging over overlapping centers weights long segments more heavily. The analogous midpoint-selected paired segments below have different composition and denominators. The 16.2% S01 mean shows a clear context-mixing problem for this target; S02 and S09 are less extreme but can still include substantial neighboring states. These differences do not establish that window mixing caused the failed classifier.

Artifact exclusion also varies, but does not alone explain the failure:

| Participant | Artifact windows at mixed centers | Artifact windows at code-1/2 centers |
|---|---:|---:|
| S01 | 1/400 (0.3%) | 54/5,625 (1.0%) |
| S02 | 76/812 (9.4%) | 577/5,203 (11.1%) |
| S09 | 48/1,105 (4.3%) | 155/3,909 (4.0%) |

Here a center is artifact-excluded if *any* sample of its two-second window is marked bad. These fractions share highly overlapping windows and cannot be read as independent observations or an unbiased estimate of artifact-free perception.

## 3. Matched nonmixed transition comparison

For each contiguous mixed-code segment, I selected the nearest valid 0.2-second-grid center to its midpoint. Controls were pure-code centers within 0.2 seconds of a change into or out of a mixed-code segment. A clean control from the same trial was chosen without reuse, 2–6 seconds from the mixed center, nearest in time, with a deterministic earlier-center tie rule. **The two windows in each pair do not overlap**, but windows from different pairs can overlap. Matching is greedy, not optimal, and does not match transition direction, episode length, stimulus, time since onset, eye assignment, motor behavior or all surrounding states. A control's two-second EEG window may itself contain mixed-report samples.

| Participant | Mixed segments | No valid grid center | Midpoint artifact-excluded | Eligible midpoint segments | Matched pairs | Eligible but unmatched | Median pair separation |
|---|---:|---:|---:|---:|---:|---:|---:|
| S01 | 523 | 219 | 1 | 303 | 303 | 0 | 2.2 s |
| S02 | 299 | 50 | 24 | 225 | 202 | 23 | 2.6 s |
| S09 | 229 | 19 | 8 | 202 | 188 | 14 | 3.8 s |

The grid exclusion includes episodes too brief to hit a valid grid center **and** those outside the required trial margins; it does not mean those reports were absent. S02's 225 eligible midpoint segments differ from the prior S02 result's 226 segments with *any* clean center: the present diagnostic requires a clean **selected midpoint**. Similarly, S09 has 202 midpoint-eligible segments versus 204 with any clean center in the earlier receipt. This is a different selection rule, not a contradiction.

The fixed POz feature is log10(low-tag power / high-tag power). Positive paired differences mean that this ratio was larger at the mixed center than at its matched nonmixed center; they do not carry an independently validated color, eye or phenomenal interpretation.

| Participant | Pairs | Mean mixed − control log10 ratio | Median difference | Fraction of pair differences positive | Controls code 1 / code 2 |
|---|---:|---:|---:|---:|---:|
| S01 | 303 | +0.038 | +0.031 | 51.5% | 152 / 151 |
| S02 | 202 | −0.068 | −0.115 | 45.0% | 94 / 108 |
| S09 | 188 | +0.159 | +0.167 | 55.9% | 93 / 95 |

Control centers were before the mixed center in 140/303 S01 pairs, 91/202 S02 pairs and 84/188 S09 pairs. These are **descriptive summaries**, not independent-pair inference. Different direction across participants and the incomplete matching mean that neither a common difference nor its absence can be established. No classifier was fitted or selected using these differences.

The mean mixed-code sample fraction in the *selected mixed* windows was 11.8%, 30.8%, 43.3% for S01/S02/S09; in their matched *nonmixed-center* windows it was 9.9%, 20.2%, 33.5%. Thus the controls do not represent windows wholly free of mixed-report context, and the comparison cannot cleanly separate a center state from its surroundings.

## 4. Timing and spectral cautions

For the matched mixed midpoints, the table below shows the fraction retaining the same mixed code if the label sample were displaced 0.2 seconds, without moving or recomputing the EEG feature. The state changes may reflect short reported episodes, the grid and marker conventions, or timing uncertainty; the calculation does not determine which.

| Participant | Same mixed code 0.2 s earlier | Same mixed code 0.2 s later |
|---|---:|---:|
| S01 | 15.8% | 12.9% |
| S02 | 43.1% | 43.6% |
| S09 | 69.7% | 72.3% |

In the matched windows, mean tag-to-±1-Hz-flank contrasts in dB for the mixed centers were **+0.21 / −0.29** (low/high tag) for S01, **−1.24 / −0.24** for S02, and **−0.34 / −0.51** for S09. These are deliberately rough local spectral comparisons; choice of flanks, preprocessing, the short Hann window, leakage and neighboring oscillations can affect them. Near-zero or negative values here do **not** establish absent tags, quantify true SSVEP signal-to-noise, or settle whether a different feature would work. The full per-participant values for controls and medians are in the [aggregate receipt](verification/roy_mixed_transition_context.json).

## 5. Consequences and verification

The diagnostic makes the target's temporal-context problem concrete, especially for S01. It also shows selection and timing sensitivity and fails to produce a consistent signed matched contrast across these three already-inspected participants. It **does not causally attribute** the frozen S02 model's failure to any single issue, rule out other features, or show that report transitions are experiences. The experiential and subject-constitution bridge remains open.

A genuinely new attempt would need its own explicit design addressing report latency, temporally localized signals, neighboring states, transition and motor controls, artifact selection, and participant-level evaluation. It must not present S01, S02 or S09 as untouched tests. Before asking for further data, first specify a scientifically defensible candidate and failure criteria; no such validated candidate was established here.

The [diagnostic script](verification/roy_mixed_transition_context.py), [synthetic tests](verification/roy_mixed_transition_context_test.py) and [aggregate receipt](verification/roy_mixed_transition_context.json) contain no raw EEG, raw event sequences or private links. Tests cover midpoint/grid boundaries, artifact exclusion, matching distance and no reuse, taper weighting, local spectral arithmetic, timing sensitivity and empty results. The real-data receipt was reproduced byte-for-byte; all three participants' center-class counts, artifact counts and scoreable totals matched the earlier committed receipts, and matching totals balance. These software checks do not validate marker semantics, subjective reports or population generalization.
