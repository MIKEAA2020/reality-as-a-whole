# Shelat 2026: reward versus selection in accuracy and RT; R workflow attempt

## Bottom line

Using the shared, hash-checked archives, we independently fitted the paper's pooled reviewer-suggested response-time model and obtained **12.29 ms (SE 5.78)** for reward versus neutral in fast-triggered trials, closely matching the published coefficient. A more specific **reward versus previously selected but unrewarded** comparison was **4.69 ms**, 95% normal Wald CI **[−6.73, 16.10]** in the same trigger condition. In the existing pooled accuracy model at the midpoint of blocks 1–4, reward versus selection was **0.051 log odds**, 95% Wald CI **[−0.091, 0.193]** for fast triggers. These later contrasts are retrospective, unregistered, model-dependent and unadjusted for multiple testing. They do **not** establish that reward and selection are equivalent, or that the paper's mechanism is false.

We attempted to set up R, but no R/lme4 installation was present and Debian package indexes could not be downloaded from the sandbox. The original R workflow was **not executed** and exact processed-row identity is unverified. A plan was recorded [before calculating these new contrasts](SHELAT_2026_REWARD_SELECTION_RT_WORKFLOW_FOLLOWUP_PLAN.md), but the study and some results were already known; none of this is a blind or prospective analysis.

## 1. Data, outcome and original model

The independent readers use the two GitHub dataset ZIPs whose hashes match the OSF file metadata, as documented in the [descriptive audit](SHELAT_2026_EXPERIMENT_ARCHIVES_DESCRIPTIVE_REPLICATION.md). They read only numeric-block learning trial structures for counterbalanced colors and SART response files. No survey records are read, and no participant- or trial-level records are written. Participant folders are namespaced by experiment for pooled fitting; the two archives have disjoint SART subject identifiers.

The authors' `process data MWAC final.R` retains fast/slow triggered trials with RT ≥200 ms and nonmissing accuracy. Our reader requires a response and RT, with the same RT threshold, and verifies accuracy is 0 or 1. In the numeric-block fast/slow response files, response, RT and accuracy were either all present or all absent: present 7,026 / absent 246 in experiment 1, present 6,740 / absent 300 in experiment 2. This supports agreement of those filters **for these response files**, not identity of the whole authors' processed workflow. Trial-structure-only keys in experiment 2 have no response and are not included. Exact join, survey-derived experiment tags and other processing have not been executed or comprehensively validated.

Retained RT analysis includes **both correct and incorrect responses**, not only correct trials: 6,781 trials (3,978 correct) from 50 subjects in experiment 1; 6,447 (3,603 correct) from 50 in experiment 2; pooled 13,228 trials (7,581 correct, 5,647 incorrect) from 100. Missing or <200 ms responses are excluded **after the outcome**, so all results concern retained trials and cannot establish effects on omissions or the excluded fast responses.

The authors' `reviewer3 responses MWAC final.R` lines 33–36 specifies `lmer(rt ~ distractor_feature * trigger + (1 | subjectID))` on pooled data. The code loads `lmerTest` in its processing script; its p values can use Satterthwaite degrees of freedom. The RT analysis was reviewer-suggested and **unregistered**. Unlike the accuracy model, this particular RT formula contains neither block nor experiment nor response accuracy as fixed effects. We fit the stated RT formula as written and separately by experiment, rather than treating reward × accuracy or a correct-only model as equivalent.

## 2. Independent Gaussian random-intercept REML fit

The reviewed [RT implementation](verification/shelat_2026_rt_mixed_reproduction.py) computes per-subject × condition × trigger count, RT sum and sum of squared RT **in memory only**. These sufficient statistics retain the Gaussian random-intercept likelihood for this design. It profiles the residual variance in restricted maximum likelihood (REML), numerically optimizes the intercept/residual variance ratio, and estimates fixed effects and covariance by generalized least squares. Neutral distractor and fast trigger are reference categories; random intercepts are independent across subjects, with one common residual variance. Its two-sided normal Wald intervals and p values are **not** `lmerTest`'s Satterthwaite calculations, and it does not execute R or use its optimizer.

All three one-dimensional fits reported optimizer success with an interior solution, positive local profile curvature and derivative magnitude below 0.00004. Pooled estimated between-subject intercept SD is 68.34 ms and within-subject residual SD 174.35 ms. These are limited numerical checks, not evidence that the normal, homoscedastic and independent-residual assumptions hold. We did not assess full residual distributions, serial dependence, random slopes or sensitivity to alternative outlier filters. An independent dense trial-level calculation on **synthetic data** agrees with the cell-based REML implementation, and the archive integration test recomputes its aggregate results.

### Pooled RT contrasts, milliseconds

A positive contrast means slower RT on reward-colored than comparison-colored trials. Interval and p value calculations use the full fixed-effect covariance.

| Contrast | Estimate | SE | 95% normal Wald CI | Unadjusted normal p |
|---|---:|---:|---:|---:|
| Fast: reward − neutral | 12.29 | 5.78 | [0.96, 23.62] | .0335 |
| Slow: reward − neutral | 13.28 | 6.43 | [0.69, 25.88] | .0387 |
| Slow − fast difference of reward − neutral contrasts | 0.99 | 8.65 | [−15.95, 17.93] | .909 |
| Fast: reward − selection | 4.69 | 5.83 | [−6.73, 16.10] | .421 |
| Slow: reward − selection | 4.69 | 6.43 | [−7.92, 17.30] | .466 |
| Slow − fast difference of reward − selection contrasts | 0.006 | 8.68 | [−17.01, 17.02] | .999 |

The paper reports reward b=12.29 ms, SE=5.78, p=.033 in the interaction model. With neutral/fast reference coding this coefficient is specifically **fast-trigger reward versus neutral**, not an automatically averaged overall effect. Our coefficient and SE closely reproduce the reported values, while the inferential method is not identical. The model-implied slow-trigger contrast above is computed from the **joint interaction model**, not the separate slow-only model from Appendix B; their estimates and SE need not agree. The lack of a significant interaction is not evidence of equal effects across triggers.

The analogous reward-versus-selection estimates in experiment 1 were 9.69 ms fast [−6.02, 25.39] and 6.25 ms slow [−10.87, 23.36]; experiment 2 gave −0.28 ms fast [−16.88, 16.31] and 3.09 ms slow [−15.48, 21.67]. These are separate exploratory fits, not a formal experiment-by-condition interaction test; their differences should not be inferred from their individual p values. Full terms, p values and diagnostics are in [aggregate JSON](verification/shelat_2026_rt_mixed_reproduction.json).

## 3. Direct accuracy contrasts at the block midpoint

The prior [accuracy reproduction](SHELAT_2026_ANALYSIS_CODE_AND_MODEL_REPRODUCTION.md) fits a logistic random-intercept model with `block * distractor * trigger`. Here we specify midpoint **2.5** before computing these contrasts: it lies between observed blocks 2 and 3, and is not itself an observed block. It is a linear-model contrast on the log-odds scale, **not** an empirical trial-weighted average over blocks or a percentage-point change. The equal-spaced midpoint corresponds to the arithmetic average of that model's block-specific log-odds contrasts, not an average probability or a trial-weighted estimand. Pooled model has no experiment fixed effect. The [aggregate output](verification/shelat_2026_laplace_accuracy_reproduction.json) also retains all observed-block estimates and the per-experiment midpoint estimates.

| Pooled full model, block 2.5 | Estimate (log odds) | 95% Wald CI | Unadjusted p |
|---|---:|---:|---:|
| Fast: reward − neutral | 0.193 | [0.051, 0.334] | .0077 |
| Slow: reward − neutral | 0.057 | [−0.128, 0.241] | .547 |
| Slow − fast difference, reward − neutral | −0.136 | [−0.368, 0.097] | .252 |
| Fast: reward − selection | 0.051 | [−0.091, 0.193] | .483 |
| Slow: reward − selection | 0.001 | [−0.186, 0.188] | .991 |
| Slow − fast difference, reward − selection | −0.050 | [−0.285, 0.185] | .677 |

The fast reward − selection midpoint estimates by experiment were 0.091 [−0.111, 0.293] and 0.011 [−0.189, 0.212]. No claim of equal effects is supported by these intervals. **Significant reward−neutral but nonsignificant reward−selection is not itself a test that those contrasts differ**, nor proof that reward and selection are interchangeable. Contrasts in both tables are post hoc and numerous; confidence intervals and p values are unadjusted and should be used as exploratory quantification, not confirmatory evidence. The separate preregistration for experiment 2 remains inaccessible, and the pooled analyses were not preregistered.

## 4. R/lme4 attempt and reproducibility

`Rscript` and R were absent, no `libR`/`lme4` installation was found in the checked standard locations, and the Debian package-list cache was empty. An actual `sudo apt-get -o Acquire::Retries=0 -o Acquire::http::Timeout=5 update` attempt returned warnings for failed connections to `deb.debian.org` for bookworm, bookworm-updates and bookworm-security; the command itself nevertheless exited zero, so its warnings and empty indexes—not its exit status—establish that it did not obtain the packages. This environment permits outbound connections only to a limited host set. We did not install an unverified alternative binary or execute original R files. An accessible preprovisioned R environment or a verified portable distribution with `lme4` and `lmerTest` would allow a further reviewed, minimal model-only comparison; the package-install route has not been exhaustively investigated.

For the Python work, run with Python 3.11, NumPy 2.4.6, SciPy 1.17.1 and hash-matching archives at the paths below. Output files contain only aggregated fixed-effect/model diagnostics:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH="$PWD/.arena/python-deps:$PWD/verification" \
  python verification/shelat_2026_rt_mixed_reproduction.py \
  .arena/shelat2026/exp1.zip .arena/shelat2026/exp2.zip > rt-results.json
OPENBLAS_NUM_THREADS=1 PYTHONPATH="$PWD/.arena/python-deps:$PWD/verification" \
  python verification/shelat_2026_laplace_accuracy_reproduction.py \
  .arena/shelat2026/exp1.zip .arena/shelat2026/exp2.zip > accuracy-results.json
OPENBLAS_NUM_THREADS=1 SHELAT_ARCHIVE_INTEGRATION=1 \
  PYTHONPATH="$PWD/.arena/python-deps:$PWD/verification" \
  python -m unittest -v shelat_2026_rt_mixed_reproduction_test \
  shelat_2026_laplace_accuracy_reproduction_test shelat_2026_archive_descriptives_test value_capture_followup_test
```

## 5. Interpretation and next discriminating test

These results make a narrower point than the paper's mechanistic conclusion: an irrelevant reward-history color is associated with slower responses compared with **neutral** in the specified retained-trial model; a direct comparison with **previous selection without reward** is smaller and uncertain. Accuracy and speed are jointly determined; adding accuracy as a control or filtering to correct trials would change the estimand and may condition on a post-outcome variable, not automatically resolve speed–accuracy tradeoffs. The experiment's distractor colors occur on rare trials, making rapid or stable warning/response-preparation learning plausible. The archive analysis cannot identify a unique neural recoupling mechanism, subjective mind-wandering, or the counterfactual effect of breaking color–rare-trial predictiveness.

A future design could orthogonally counterbalance prior reward, prior selection and color–rare-trial predictiveness, with sufficient trials and prespecified interaction contrasts. Measuring gaze, response bias, speed–accuracy tradeoffs and time-anchored subjective reports would help discriminate accounts, while probe and selection effects remain important. Even that would not by itself establish phenomenal conjunction or subject identity, and none of this study uses split-brain participants. The [P/C/L experiential comparison](PRIVATE_NESTED_FIELDS_AND_EXPERIENTIAL_CONTENT_COMPARISON.md) therefore remains underdetermined.
