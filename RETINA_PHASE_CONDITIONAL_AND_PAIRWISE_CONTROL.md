# Retinal collective activity after a stimulus-phase control

## Question and provenance

How much of the earlier apparent collective signal survives accounting for repeated movie phase? The answer matters because a shared stimulus can make cells fire together even if their responses are conditionally independent. The published Schneidman et al. paper **already used independently shuffled trials to construct a stimulus-conditioned independent model**; the present analysis is an independent, limited replay, not a discovery of a neglected confound or a novel shuffling method. See [the paper and methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC1785327/) and [the prior source and data audit](RETINA_SUPPLEMENTS_DATA_AND_EFT_THESIS_AUDIT.md).

Stimulus-dependent pairwise modeling also has an established literature: Granot-Atedgi et al., [*Stimulus-dependent Maximum Entropy Models of Neural Population Codes*](https://doi.org/10.1371/journal.pcbi.1002922), describe an SDME model and report improved prediction over uncoupled models in another salamander-retina dataset. The abstract and selected introductory text were inspected here, not its full methods, figures, data or code. Our simple phase-plus-tilt calculation below is **not a reproduction of their model**.

The supplied spike file contains 40 cells and 172,521 spikes. As in the prior audit, we **assume**, rather than independently verify, 120 consecutive 26.5-second movie repeats aligned at zero, each with 1,325 bins of 20 ms. Archive documentation describes 145 repeats, whereas the file's extent and spike count match a published 120-repeat description; provenance and a possible silent tail remain unresolved. The first 100 presumed repeats train the predictors; the last 20 provide held-out scores. These are repeats of the **same movie and recording**, not a new movie, animal or laboratory. Phase index is a time-within-repeat proxy, not the measured visual input: even if the assumed slots are right, slow time-locked changes or other unmeasured variables can mimic stimulus locking.

## Forty-cell coactivity

For each bin, count how many distinct cells fired at least once. The following are probabilities of at least five of 40 cells being active:

| Estimate | Rate |
|---|---:|
| Held-out observed | 0.043472 |
| Independent cells, stationary training-average rates | 0.002249 |
| Independent cells *given movie phase*, estimated from the 100 training repeats | 0.037057 |
| 200 phase-preserving trial shuffles of the held-out repeats: mean | 0.037160 |
| Same shuffles: minimum to maximum | 0.035434–0.038642 |

The phase-conditioned estimate reduces the observed excess over the stationary independent baseline by about **84%** for this one threshold and dataset. This is a descriptive subtraction, not the fraction of all correlation or collective information explained, and it is not a causal attribution. There remains a difference of roughly 0.006415 in this event probability. Its robustness to sampling, repeat alignment and recording drift has not been established.

The shuffles independently permute whole repeat labels for each cell, preserving every cell's complete individual trial trains and its exact phase-wise spike counts. Pairwise trial labels may coincide by chance, with expected frequency 1/20; the shuffle is not an exact zero-collision construction. The displayed range is **Monte Carlo shuffle variability**, not a confidence interval or a significance test. The phase estimate instead uses training-repeat cell probabilities and the exact independent Bernoulli count distribution; it does not use the held-out permutations.

As a separate pairwise statistic, the 780 cell pairs have mean same-trial coincidence 0.00144949 versus 0.00132594 for the exact average over **all unequal-trial** pairings at the same phase; the difference is 0.00012355 per 20-ms bin. It is positive in 475 of 780 pairs. The mean differences in the first and last ten held-out repeats are 0.00011619 and 0.00013212 respectively. These are not independent experiments, and pairs share cells. Trial-to-trial covariation, nonstationarity and other latent common inputs can all contribute; no direct connection is identified.

## Held-out pattern prediction: give the models the same information

For the five prior ten-cell groups, the score is mean negative log probability of the observed 10-bit pattern in **bits per 20-ms bin**; lower is better. The stationary independent and stationary pairwise maximum-entropy models are the previously fitted models. The phase-mixture model independently estimates every cell's firing probability for each phase and **marginalizes the unknown phase** uniformly. It thus predicts a time-averaged pattern without being told which phase produced the test bin, as do the stationary models. A symmetric Beta(1/2,1/2) smoothing prior is applied per cell and phase.

| Group | Stationary independent | Phase mixture | Stationary pairwise | Given-phase independent | Given-phase field-calibrated | Given-phase pairwise |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1.86369 | 1.77676 | 1.76652 | 1.07139 | 1.06120 | 1.05479 |
| 2 | 1.47841 | 1.44126 | 1.43006 | 0.79101 | 0.77889 | 0.77431 |
| 3 | 1.55945 | 1.51978 | 1.50897 | 0.86922 | 0.85794 | 0.85475 |
| 4 | 1.40936 | 1.35775 | 1.34581 | 0.75514 | 0.74374 | 0.73901 |
| 5 | 1.76743 | 1.73891 | 1.73312 | 1.05189 | 1.04282 | 1.04181 |

The stationary pairwise model scores better than this particular phase mixture in these five groups, but the ordering is **sensitive to smoothing**: with Beta(0.05,0.05), the mixture scores 1.76638, 1.42926, 1.50782, 1.34418 and 1.73045, slightly better than the stationary pairwise model in all five. With Beta(1,1), the mixture scores 1.79837, 1.46618, 1.54525, 1.38451 and 1.75950. These sensitivities are exploratory; neither prior nor predictor was selected by a separate validation set, and the five overlapping groups do not furnish five independent replications. Smoothing affects the direct conditional scores too; all results are in the receipt. Therefore this analysis does not support a general ranking of the model classes.

The last three columns **do know the phase**, so their absolute scores cannot fairly be compared against stationary predictions as if the available information were identical. Within those three columns, however, they use the same phase information. Starting with the Beta(1/2,1/2) independent model, we fit ten constant field offsets on the training repeats; a second model adds 45 constant pairwise tilts. Both use the same fixed L2 coefficient 0.001. All optimization uses training data only. The held-out improvement from adding pair terms to the field-calibrated baseline is respectively **0.00641, 0.00458, 0.00319, 0.00473 and 0.00101 bits/bin**. The improvement over the *uncalibrated* phase model would be larger but would partly credit a correction to single-cell firing rates to pairwise structure. The conditional pairwise fits converge to small penalized gradients and include both positive and negative tilts. This is a useful in-sample-design/held-out-repeat predictive comparison, not evidence that those tilts are anatomical connections, interventions or a subject boundary. Different regularization, phase smoothing, drift and unseen stimuli need evaluation before generalization.

## Implication for the wider framework

The prior ~19-fold coactivity excess over a stationary independent model was real as a descriptive comparison, but is **not by itself strong evidence for intrinsic integration**: much of that contrast is predictable from phase-dependent individual rates. The remaining cross-trial and conditional-predictive differences show that the chosen independent controls are incomplete for this sample; they do not establish that the remaining dependence is caused by direct cellular interactions rather than other shared inputs, latent state, timing errors or model misspecification. Nor do statistical or causal dependencies identify phenomenal subjects. Accordingly, this narrows what the retinal evidence can support; it does not solve the framework's experiential-identity or subject-selection gaps.

## Reproduction and limits

Run `OPENBLAS_NUM_THREADS=1 python3 verification/retina_stimulus_phase_control.py` with NumPy and SciPy installed. The script pins the supplied source and earlier receipt by hashes, checks raw binary count, verifies per-phase counts for every shuffle, tests two synthetic pair-coincidence controls and a Bernoulli probability, verifies normalization of the predictive mixtures, and records optimization gradient diagnostics in [`verification/retina_stimulus_phase_control.json`](verification/retina_stimulus_phase_control.json). Raw parsing and model selection are specified in the script. The previous 10-cell groups and stationary fitted scores are taken from the pinned prior receipt; the script checks that receipt's source and split.

This was exploratory, not preregistered; no uncertainty interval, multiple-testing analysis, held-out stimulus, correction for sampling phase uncertainty, intervention, or independent recording is supplied. A stronger next step is to compare independently validated stimulus-conditioned and coupled predictors on unseen movies or recordings, with repeat/block-aware uncertainty and phase validation, then use intervention only if the scientific question requires causal influence. Even that would not alone establish experience.
