# What the residual retinal prediction gain actually measures

## Question

The [previous phase-conditioned analysis](RETINA_PHASE_CONDITIONAL_AND_PAIRWISE_CONTROL.md) found that, for five ten-cell groups, a pairwise-tilted predictor outscored a field-calibrated independent predictor on the last 20 presumed movie repeats. But **a predictive gain need not mean the gain comes wholly from same-trial dependence**. Both models may imperfectly track the per-phase single-cell response; the pairwise model can adjust those marginals as well as their dependence. We therefore compare each model's observed score gain with its expected gain on phase-preserving shuffled test data. We also test sensitivity to the assumed smoothing and regularization.

The mathematical ingredients—exponential-family sufficient statistics and trial-shuffled conditional independence—are established, not new. See Schneidman et al., [*Weak pairwise correlations imply strongly correlated network states in a neural population*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1785327/), whose trial-shuffling methods were inspected in the prior audit, and Wainwright and Jordan, [*Graphical Models, Exponential Families, and Variational Inference*](https://doi.org/10.1561/2200000001), whose abstract and introduction were inspected, not the full monograph or proofs. The specific fitted-score decomposition and checks below are this project's bounded analysis, not a new general theorem.

## An exact decomposition for these fitted models

Let `x_i` be whether cell `i` fired within a bin and `t` its presumed movie phase. The fitted pairwise model has phase-specific baseline rates, ten constant field offsets and 45 constant pair terms `J_ij x_i x_j`. Its independent comparator uses the **same** phase-dependent baseline and fits ten field offsets, but no pair terms. Both models are trained on the first 100 repeats and frozen before the last 20 are scored. The improvement in log score, in bits per bin, is

`G = mean[log q_pair(x|t) − log q_field(x|t)] / ln(2)`.

For independent whole-trial permutations of the held-out data for each cell, the per-cell firing rate at each phase is unchanged. Therefore the field contributions and both phase-specific normalization terms have the **same average** before and after shuffling. The pair-feature terms are the only terms that can change. If `C_ij` is the average observed same-trial coincidence and `Csh_ij` is its exact expected value under independent trial permutations at the same phase, then

`G_observed − E_shuffle[G] = (1/ln 2) Σ_(i<j) J_ij (C_ij − Csh_ij)`.

This is an exact finite-data algebraic identity for the declared model and shuffle, not an approximation or a causal result. Each independently permuted label can happen to select the same original trial as another cell; its probability is 1/20 for a full-test shuffle and 1/5 for the within-five-repeat-block shuffle below. Thus `Csh` here includes these collisions; it is not the strictly unequal-trial statistic reported in the previous note. The code verifies the identity for every fitted setting, along with a toy example and a Monte Carlo check of the shuffle expectation.

## Results and a correction to interpretation

The base setting uses the prior analysis's symmetric Beta(1/2,1/2) phase-rate smoothing and L2 coefficient 0.001. Gains are held-out bits per 20-ms bin; the shuffle columns are **exact expectations**, not re-fitted models or confidence intervals.

| Group | Observed pairwise gain | Expected gain after full-test shuffle | Excess over full shuffle | Expected gain after within-five-repeat-block shuffle | Excess over block shuffle |
|---|---:|---:|---:|---:|---:|
| 1 | 0.006407 | 0.000527 | 0.005880 | 0.001286 | 0.005120 |
| 2 | 0.004578 | 0.001272 | 0.003306 | 0.001809 | 0.002769 |
| 3 | 0.003186 | 0.001412 | 0.001774 | 0.001637 | 0.001549 |
| 4 | 0.004733 | 0.001716 | 0.003018 | 0.002030 | 0.002704 |
| 5 | 0.001005 | 0.000536 | 0.000469 | 0.000773 | 0.000232 |

Thus the previous statement that the *entire* field-controlled gain indicates residual dependence would be too strong. In these fits, some gain remains even in the expected shuffled data. At the same time, all five observed gains exceed both shuffle expectations in the base setting. The more conservative block shuffles preserve phase-specific single-cell rates separately in four consecutive five-repeat blocks, so some slow block-to-block co-variation remains in the shuffled reference; they do not eliminate drift within blocks. Positivity is a descriptive observation, not a significance claim. With only five repeats per block, accidental same-trial matches also attenuate the gap more strongly.

For context, the sampled 200 full-test shuffles gave gain ranges of 0.000059–0.001135 for group 5; its observed gain 0.001005 falls inside that range. The other four observed gains exceed their respective sampled shuffle maxima. These ranges describe random shuffling of the same held-out data; they are not biological confidence intervals or independent replications. Block shuffle expectations were computed exactly, not sampled.

The frozen base-model gain is positive in each of four five-repeat blocks for all five groups, ranging across blocks from 0.00038 to 0.00803 bits/bin. Blocks still belong to the same recording, and groups overlap. This does not establish independence, robustness to other samples, or a reliable effect-size interval.

## Sensitivity

We refit with symmetric Beta phase-smoothing `alpha` of 0.05, 0.5 and 1.0, with L2 fixed at 0.001; and L2 of 0.0001, 0.001 and 0.01 with alpha fixed at 0.5. These are one-at-a-time stress tests, not a comprehensive search and not a preregistered validation protocol. Across all 25 group/settings, **observed gain minus the within-block shuffle expectation remains positive**, from about 0.000095 to 0.006208 bits/bin. The ordinary observed gain itself is slightly negative for group 5 at alpha 0.05: −0.000038 bits/bin. Thus both the apparent magnitude and whether the pair model beats the independent field-only predictor can depend on model choices. Exact values and all optimizer diagnostics are in the [receipt](verification/retina_conditional_score_decomposition.json).

The group-5 result is especially weak: its base-setting excess over the block shuffle is only 0.000232 bits/bin, and no uncertainty analysis has established that this difference would reproduce. We should not promote these five selected, overlapping groups into a population-wide law.

## Why the residual is not causal identification

Even perfect knowledge of an observational joint distribution can fail to determine the causal mechanism. An exact two-bit counterexample is checked in the script:

- **Common cause:** an unobserved fair bit `L` independently drives noisy copies `X` and `Y`, each with accuracy `(1 + 1/√2)/2`.
- **Direct effect:** `X` is fair and `Y` copies it with probability 3/4.

Both give `P(00)=P(11)=3/8` and `P(01)=P(10)=1/8`, so they have the same single-cell probabilities, same-trial excess above the independent baseline, and the same optimal joint-versus-independent log-score gain, about **0.18872 bits**. Yet, in the explicitly specified structural models, `P(Y=1 | do(X=1))` is **1/2** for the common-cause model and **3/4** for the directed model. This is a standard kind of observational-equivalence example, not a fitted explanation of the retina. Phase conditioning, the remaining score improvement, and the score decomposition cannot decide between such structures without additional assumptions or interventions.

The same distinction is decisive for the broader project: even experimentally demonstrated causal influence would not by itself specify a subject boundary or justify an identity between physical structure and experience. A proposed experiential grounding or substrate-independent subject rule still needs its own explicit bridge and discriminating tests; a statistical fit alone does not supply one. Nor do these observations decide whether the larger whole is self-existent or whether genuine possibilities are actual.

## Reproduction and scope

Run `OPENBLAS_NUM_THREADS=1 python3 verification/retina_conditional_score_decomposition.py` with NumPy and SciPy installed. The script checks the input source and prior receipts by SHA-256; reconstructs the same 120 presumed repeats, groups and split; independently refits all 25 settings with exact 1,024-state normalization; verifies previous base scores and the algebraic identity; tests synthetic shuffles; and logs gradients and four held-out blocks. The [machine-readable receipt](verification/retina_conditional_score_decomposition.json) gives all values.

Important limitations remain: the 120 × 26.5-second phase alignment and acquisition duration were not independently validated; the archive README describes 145 repeats. Time-within-repeat is a proxy, not the actual measured stimulus. There is one recording and one repeated movie, no held-out stimulus or animal, no neuronal intervention, no preregistered hypothesis, no biological uncertainty interval, and no correction for temporal dependence or multiple exploratory comparisons. Different timescales of drift, unmeasured common inputs and phase-model error remain viable explanations of the residual. A rigorous follow-up would validate phase timing, compare nested models with training-only hyperparameter selection, reserve unseen stimuli and independent recordings, and, for causal claims, use controlled interventions with an explicit observation model. None alone would settle phenomenal identity.
