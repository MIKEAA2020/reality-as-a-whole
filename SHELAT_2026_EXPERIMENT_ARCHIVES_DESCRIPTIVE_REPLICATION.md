# Shelat 2026: experiment archives and a limited descriptive replication

## What changed

The user pointed to [the repository's `main/uploads` folder](https://github.com/MIKEAA2020/reality-as-a-whole/tree/main/uploads) and supplied `ud5v4-datacite.json`. The folder contains the two study archives. We downloaded them without changing branches and compared their SHA-256 hashes with OSF's previously retrieved metadata: **both match**. The attachment is citation metadata naming `analysis scripts.zip`; it is **not** that ZIP and contains no analysis code. The repository folder, at the time inspected, had `exp1.zip`, `exp2.zip` and a one-byte file named `1`, not the analysis ZIP. Original [analysis scripts.zip](https://osf.io/ud5v4/) and the [experiment-2 registration](https://osf.io/sev9k/) remain needed for the planned code/registration verification. We have not established why the latter link was inaccessible.

This is not yet a replication of the paper's logistic regressions or a test of the proposed mechanism. We reconstructed a narrow descriptive subset from the raw CSVs using a [fixed retrospective plan](SHELAT_GIESBRECHT_2026_MATERIALS_CHECK_PLAN.md), written after the findings were known and before the files were supplied. The reproducible [independent archive reader](verification/shelat_2026_archive_descriptives.py) and [aggregate output](verification/shelat_2026_archive_descriptives.json) do not require copying the sensitive survey files or participant records into this branch. We did not read survey contents, inspect every trial, run the authors' code or fit mixed models. The reading assigns categories using the trial-structure color fields; it is an independently stated reconstruction, not a claim to know the authors' exact code.

## 1. Provenance and archive coverage

| Source file | SHA-256 of retrieved archive | OSF metadata agreement |
|---|---|---|
| [exp1.zip](https://github.com/MIKEAA2020/reality-as-a-whole/blob/main/uploads/exp1.zip) | `3b7f349012efd0a6b6acdc89f902de429860b22b324f81a986bfce9787b875de` | matches [OSF file metadata](https://osf.io/6thsg/) |
| [exp2.zip](https://github.com/MIKEAA2020/reality-as-a-whole/blob/main/uploads/exp2.zip) | `1b036ddcd105799e7a288e2a7479396398dc621a94c44a8249339d3815db0ea0` | matches [OSF file metadata](https://osf.io/qg3cm/) |

Hashes verify identity with the published metadata, not independent scientific validity. ZIPs contain learning, sustained-attention (`sart`), visual-working-memory and survey CSVs, plus incidental files. The audit reads only numeric-block learning trial-structure CSVs to map colors, and numeric-block SART data CSVs; ZIP files are read in place without extraction. There are **50 distinct SART data folders per experiment**. Experiment 1 contains 199 SART data blocks (49 subjects with four, one with three); experiment 2 contains 193 (46 with four, two with three, one with two, one with one), consistent with the published completion counts. Learning data files likewise have 49 full ten-block records and one partial eight-block record in experiment 1, and 49 full ten-block records and one partial six-block record in experiment 2. These are counts of file paths, not an independent audit of recruitment, demographics or data completeness.

The learning trial-structure columns `counterbalance_condition` and `condition_nonrew` each contain a single consistent pair per SART folder, here interpreted as rewarded and previously selected colors. Among red, green and blue the remaining color is classified novel; `neutral` remains neutral. The existing `infreq_trigger` field distinguishes `fast`, `slow`, and `fixed`; this check uses only fast and slow, as the paper specifies for its trigger validation. Fixed rare trials are excluded. Neither the experimental software that generated triggers nor the original analysis scripts were inspected.

## 2. Sequential exclusions reproduce the paper's percentages

Reconstruction filters the fast/slow triggered records first for missing response or RT, then for RT below 200 ms; the second percentage uses the **remaining** records as denominator:

| Experiment | Fast/slow records | Missing response/RT | Percent of raw | RT <200 ms after first filter | Percent of remaining | Retained |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7,272 | 246 | 3.38% | 245 | 3.49% | 6,781 |
| 2 | 7,040 | 300 | 4.26% | 293 | 4.35% | 6,447 |

The four percentages agree, to the paper's displayed rounding, with its p. 7 trigger-validation exclusions. This is evidence that this particular filtering reconstruction is plausible; it does not prove every preprocessing decision or validate using a post-outcome RT cutoff. These rates describe exclusions, not the probability of absent experience. Excluding very fast and unanswered rare trials changes the estimand to retained responses and should be kept explicit.

## 3. Table 1 reproduced descriptively

The article's Table 1 gives each person's number of retained trials per trigger and distractor type, summarized as mean ± sample SD. Using all 50 SART data folders per experiment and the mapping/filter above, **all 16 published cells** match to the printed two decimal places:

| Trigger and distractor | Experiment 1 | Experiment 2 |
|---|---:|---:|
| Fast, neutral | 18.04 ± 3.78 | 19.08 ± 5.81 |
| Fast, novel | 18.34 ± 5.30 | 17.28 ± 4.79 |
| Fast, reward | 18.18 ± 5.72 | 18.02 ± 5.76 |
| Fast, selection | 18.58 ± 5.51 | 17.46 ± 5.18 |
| Slow, neutral | 16.02 ± 4.54 | 14.42 ± 4.78 |
| Slow, novel | 15.56 ± 4.94 | 14.36 ± 4.78 |
| Slow, reward | 15.16 ± 4.86 | 13.68 ± 4.25 |
| Slow, selection | 15.74 ± 5.48 | 14.64 ± 5.10 |

This verifies a concrete table, not the accuracy model in Table 2. Counts per participant are repeated observations, not independent people.

As a separate **unadjusted descriptive** check, the retained-record pooled correct proportions were 43.20% fast versus 76.76% slow in experiment 1 and 38.81% fast versus 77.37% slow in experiment 2. Equal-person averages were 43.11% versus 76.03%, and 39.35% versus 75.84%, respectively. All 50 folders had retained trials in both trigger types. These numbers are consistent with Figure 5's direction but are not the paper's mixed-effect estimates, confidence intervals, causal effects, or a measurement of any one person's mental state. They do not distinguish mind wandering from response strategy. The experiment-2 slow reward and selection pooled proportions and other per-cell values can be found in the aggregate output, but without model-based adjustment or uncertainty they should not be used as definitive reward-effect tests.

## 4. Verification, limitations and next step

From the repository root, with the two original archives accessible:

```sh
python verification/shelat_2026_archive_descriptives.py /path/to/exp1.zip /path/to/exp2.zip > aggregate.json
python verification/shelat_2026_archive_descriptives_test.py
```

The archive reader checks both expected SHA-256 hashes, rejects inconsistent color mappings and unexpected codes, and outputs only aggregate quantities. The test checks color coding, accounting invariants and agreement of the **saved** aggregate output with all printed Table 1 cells; it does not re-read the archives or verify authors' statistical models. Comparing a newly generated output with the saved output requires a separate comparison; the archive paths above are examples, not tracked copies. Our input archives and temporary reading workspace are excluded from the repository. No participant-level records, survey content or original ZIPs were added to this branch.

Next obtain the actual [analysis scripts.zip](https://osf.io/ud5v4/) rather than its DataCite JSON; then check original filtering, exact block coding, excluded observations, subject handling, model fit and convergence and attempt reproduction in an appropriate R environment. An accessible frozen copy of the experiment-2 registration is also needed to verify its preplanned status directly. We have neither, so no regression replication is claimed. No author request has been sent.

These two neurotypical student samples provide evidence about task performance, not direct observations of split-brain subject incidence, same-window phenomenal conjunction or q-quality. P remains a private-token, distinct-subject hypothesis; matching types are not shared tokens. The L selector is not identified with IIT, and no IIT value is computed. C3, B4–B5/F2, B9/F3 and B10 remain open. PAINgen's 21 mean discrepancies require its own actual conversion/export code, not filters fitted to the discrepancies.
