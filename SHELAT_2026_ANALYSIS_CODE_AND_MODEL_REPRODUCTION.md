# Shelat & Giesbrecht 2026: supplied code and independent accuracy-model reproduction

**Status:** the experiment-2 registration itself remains inaccessible and its title/DOI unverified. The supplied original analysis scripts have been inspected, not executed. An independently written Python logistic mixed-effects analysis has now been **run** on the supplied study data and closely reproduces the paper's main accuracy results. This is a numerical reproduction of selected model results, **not** an execution or complete validation of the authors' R workflow, preregistration, or mechanistic interpretation. The work is retrospective: the paper and its results were known before the [analysis plan](SHELAT_2026_SUPPLIED_ANALYSIS_SCRIPTS_REPRODUCTION_PLAN.md).

## 1. Registration and sources

The paper explicitly identifies [OSF `sev9k`](https://osf.io/sev9k/) as its experiment-2 preregistration. That link redirected to sign-in, and attempts to fetch the OSF registration and node APIs failed; a [DataCite search for `sev9k`](https://api.datacite.org/dois?query=sev9k) returned no results. These checks do **not** show that the registration or a DOI does not exist. We cannot independently establish its title, contents, registration date, public status or DOI. Access may require the authors' public registration link, an exported copy, or appropriate authorization. The article itself is *Value-driven attentional capture prevents commission errors in real time*, DOI [10.3758/s13423-026-02930-7](https://doi.org/10.3758/s13423-026-02930-7); this is **the paper's** title and DOI, not a confirmed registration title or DOI. References to experiment-2 preregistration below are the authors' descriptions, not independent confirmation.

The user-supplied [analysis scripts ZIP](https://github.com/MIKEAA2020/reality-as-a-whole/blob/main/uploads/analysis%20scripts.zip) has SHA-256 `709b09527693d0c89f2e1ef6f72f4808853d120945cfdfafa2d31e8daf54e640`, matching [OSF file metadata](https://osf.io/ud5v4/). It contains seven R scripts and an RStudio project, with macOS metadata. Both data ZIPs similarly match their OSF metadata; see the [descriptive audit](SHELAT_2026_EXPERIMENT_ARCHIVES_DESCRIPTIVE_REPLICATION.md) for hashes and coverage. Hash agreement establishes file identity with that metadata, not correctness or authenticity beyond that link.

## 2. What the original code says

Line numbers below refer to the named R scripts inside `analysis zip/`:

- `process data MWAC final.R` full-joins SART trial structure and response data by subject, block and trial (377–379), removes practice and converts block to a number (390–403), keeps fast/slow triggers (418–420), then retains RT at least 200 ms and nonmissing accuracy (464–474). The separate independent reader takes retained response records with nonmissing response/RT and RT ≥200; this is not a line-for-line R NA-handling reproduction. On key-level archive inspection, numeric-block SART response keys all had matching structure keys; experiment 2 had 2,400 additional structure-only keys that have no response and cannot enter our fit. We did not run the authors' join to prove identical row membership.
- The processing script derives reward/selection/novel/neutral by subject's counterbalanced colors (510–586), consistent with the independent mapping. Original processing also uses survey-based experiment tags and manual corrections for missing survey or training IDs; our separate experiment ZIPs/folder identifiers avoid reading surveys, so the whole workflow is not verified. The 50 SART subject-folder IDs in each ZIP are disjoint across experiments; the independent pooled model additionally namespaces them by experiment.
- `analyze test MWAC final.R` fits `accuracy ~ block_number * distractor_feature * trigger + (1 | subjectID)` using `lme4::glmer`, binomial logit, `bobyqa`, `maxfun=1e5` (383–406). Its pooled simpler model omits trigger (370–374); trigger validation fits `accuracy ~ trigger + (1 | subjectID)` separately (237–249). Wald intervals are requested by its helper (44–65). `block_number` is numeric, not a factor. The code labels the experiment-2 hypothesis preregistered, but the registration was inaccessible.
- `analyze training MWAC final.R` specifies training RT as `reward_condition * trial_number_all + (1 | subjectID)` (21–27). `reviewer3 responses MWAC final.R` includes trigger-stratified fits and random-slope checks (129–188), and other scripts address simulation and exclusions. None of these other analyses was reproduced here. The original files refer to a personal cloud path, rely on R packages and in parts process survey data or write files; they were not run wholesale. R and `Rscript` were not installed in this sandbox. We did not install R/lme4 or reproduce the authors' package versions, locale and session settings.

## 3. Independent model and numerical checks

The reviewed [Python analysis](verification/shelat_2026_laplace_accuracy_reproduction.py) reads only the hash-checked learning trial structures needed for color mapping and numeric-block SART response files, and writes aggregate model output only. No surveys or participant-level outputs are saved. It aggregates successes and trials by subject × block × distractor × trigger; these are sufficient counts for this fitted model's likelihood because the predictors and subject random intercept are constant within each cell.

It independently fits a binomial-logit mixed model with a normal random intercept per subject, using a **Laplace approximation** to the integrated likelihood, Newton solution for the conditional intercepts and SciPy BFGS for fixed effects and log random-intercept SD. It uses neutral distractor and fast trigger as explicit reference levels, with raw block numbers 1–4. It forms SEs from the inverse numerical Hessian of the approximated marginal negative log-likelihood and uses two-sided normal Wald tests/intervals. This is the same intended random-intercept model family and fixed-effect specification as the inspected code, but a different implementation, optimizer, numerical derivative and environment. We did not verify R's effective runtime contrasts or establish that every original processed row agrees; numerical agreement supports but does not prove identity of the data pipelines.

Six fits—two trigger-only, the three full models, and the simpler pooled block × distractor model—used 50, 50 and 100 subjects with 6,781, 6,447 and 13,228 retained trials, respectively. All BFGS runs reported success under a gradient tolerance of `1e-5`; maximum absolute gradient was below `8.9e-6`, all finite-difference vs analytic gradient maximum discrepancies below `1.4e-7`, and all numerical Hessians had positive minimum eigenvalues (>1.8). Random-intercept SD estimates were positive. These are checks of this implementation, not the authors' convergence diagnostics or a guarantee of global optimality. At a stricter `1e-7` optimizer setting, BFGS reported precision loss despite small gradients; the success labels are therefore tolerance-dependent. No random-slope or learning-magnitude model is fitted here.

### Selected results (log-odds coefficients)

| Model / term | Independent b | SE | 95% Wald CI | p | Article comparison |
|---|---:|---:|---:|---:|---|
| Exp 1, reward vs neutral | 0.7548 | 0.2558 | [0.2534, 1.2562] | .00317 | b=.75, p=.0032 |
| Exp 1, block × reward | −0.2270 | 0.0939 | [−0.4111, −0.0429] | .01564 | b=−.23, p=.016 |
| Exp 2, reward vs neutral | 0.4084 | 0.2404 | [−0.0628, 0.8796] | .08933 | b=.41, p=.089 |
| Exp 2, reward × slow | −0.8710 | 0.4340 | [−1.7217, −0.0204] | .04474 | b=−.87, p=.045 |
| Exp 2, block × reward × slow | 0.2822 | 0.1552 | [−0.0220, 0.5863] | .06904 | p=.069 |
| Pooled, reward vs neutral | 0.5709 | 0.1750 | [0.2279, 0.9139] | .00110 | b=.57, CI [.23, .91], p=.0011 |
| Pooled, block × reward | −0.1513 | 0.0652 | [−0.2791, −0.0235] | .02028 | b=−.15, p=.020 |
| Pooled, reward × slow | −0.6545 | 0.3027 | [−1.2478, −0.0611] | .03063 | b=−.65, p=.030 |
| Pooled, block × reward × slow | 0.2074 | 0.1074 | [−0.0031, 0.4179] | .05342 | b=.21, p=.053 |

Selected comparisons closely match the publication but are not bit-identical: e.g. our pooled reward z is 3.262 and the article prints 3.27; the three-way CI lower limit is −.0031 versus its −.0029. The independently fitted full set of coefficients, uncertainty estimates and diagnostics are in the [aggregate JSON](verification/shelat_2026_laplace_accuracy_reproduction.json); the table above is a selected comparison, not a claim that every published table entry was independently checked. A later [reward/selection follow-up](VALUE_CAPTURE_REWARD_SELECTION_PERSISTENCE_FOLLOWUP.md) adds explicitly exploratory, unadjusted reward-versus-selection and reward-versus-neutral contrasts at observed blocks to the same implementation and output. The simpler pooled model gives reward b=0.2288, p=.0832 and block × reward b=−0.0471, p=.3216, matching the paper's non-significant results. Experiment-1 novel b=0.5383, p=.0387; experiment-2 novel b=0.0825, p=.7301. Trigger-only fits give slow vs fast b=1.6854 and 1.8324 respectively.

Because block is **uncentered**, the isolated reward term is the reward–neutral contrast at fast trigger and **block 0**, outside the observed blocks 1–4; it is not the overall reward effect or a percentage-point gain. In the pooled model, the model-implied reward–neutral log-odds contrast at block `b` is approximately `0.5709 − 0.1513b` for fast and `−0.0835 + 0.0561b` for slow; slow-minus-fast is `−0.6545 + 0.2074b`. These derived contrasts are not independently tested here. Nor does one significant experiment versus one nonsignificant experiment establish a difference between experiments.

## 4. How to rerun

Requires Python 3.11 and NumPy/SciPy (this run: NumPy 2.4.6, SciPy 1.17.1), plus the exact ZIPs linked in the [descriptive audit](SHELAT_2026_EXPERIMENT_ARCHIVES_DESCRIPTIVE_REPLICATION.md). Put them at `.arena/shelat2026/exp1.zip` and `exp2.zip`, or pass other locations. Archives are read locally, not committed by this analysis. For the sandbox dependency location used here:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH="$PWD/.arena/python-deps:$PWD/verification" \
  python verification/shelat_2026_laplace_accuracy_reproduction.py \
  .arena/shelat2026/exp1.zip .arena/shelat2026/exp2.zip > output.json
OPENBLAS_NUM_THREADS=1 SHELAT_ARCHIVE_INTEGRATION=1 \
  PYTHONPATH="$PWD/.arena/python-deps:$PWD/verification" \
  python -m unittest -v shelat_2026_laplace_accuracy_reproduction_test shelat_2026_archive_descriptives_test
```

Tests cover coding, selected published comparisons, diagnostics and fresh recomputation from both archives. Small variation across numerical libraries/platforms is possible. This reproduction is limited to selected accuracy models; it does not independently reproduce training, RT, random slopes, working memory, learned-magnitude moderation, or simulations. In particular, it does not resolve the paper's reported nonconvergence of its pooled learning-magnitude model.

## 5. Interpretive boundary

These are behavioral results in two samples, not split-brain patients. They strengthen confidence that selected published accuracy coefficients can be recovered from the shared data under a closely matching model, not that a reward cue directly measures subjective mind-wandering, neural recoupling, phenomenal unity or number/identity of subjects. Fast/slow are behavioral triggers, and omission/fast-response exclusions affect the estimand. Warning/anticipation and speed–accuracy or response-bias alternatives remain live; neither the code nor these model fits establishes the framework's D/G/N values or a cross-hemispheric experiential bridge. The conditional P/C alternatives and the distinctions between token, quality and subject remain as in the [original paper audit](SHELAT_GIESBRECHT_2026_SUSTAINED_ATTENTION_AUDIT.md) and [comparison](PRIVATE_NESTED_FIELDS_AND_EXPERIENTIAL_CONTENT_COMPARISON.md).
