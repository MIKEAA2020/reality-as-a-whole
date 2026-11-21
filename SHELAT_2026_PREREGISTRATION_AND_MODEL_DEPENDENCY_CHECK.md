# Shelat 2026: registration, model dependence and material access

## Bottom line

The published 2026 attention study provides a suggestive, task-specific performance effect, but neither the experiment-2 preregistration nor its data and code could be independently checked in this environment. The accessible experiment-1 registration substantiates the paper's distinction between its originally planned suppression analyses and its exploratory recoupling analyses. The reported pooled reward coefficient is a **conditional parameter in an interaction model**, not a single average improvement that applies uniformly across blocks and triggers.

This is a [retrospective check](SHELAT_GIESBRECHT_2026_MATERIALS_CHECK_PLAN.md), planned after the results were known. It builds on the [full-main-text and supplement audit](SHELAT_GIESBRECHT_2026_SUSTAINED_ATTENTION_AUDIT.md). It is not a replication or an audit of the actual scripts and participant records.

## 1. What is actually registered for experiment 1

The [public registration](https://osf.io/58hyw/) and its [OSF API record](https://api.osf.io/v2/registrations/58hyw/) give a registration date of 3 April 2024. The study entry states data collection had not yet begun, estimated starting 8 April 2024. We checked the frozen registration's hypotheses, design, exclusions, sample plan and analytic models; the registration's statement and timestamp are not independent proof of the actual data-collection timeline.

Its two principal hypotheses concern RT differences for reward-associated distractors on inaccurate versus accurate rare trials and moderation by working-memory capacity. It specifies `rt ~ distractor_feature * accuracy + (1 | subjectID)` and the three-way model including `k`; it also specifies training learning, trigger validation, and accuracy-by-block/distractor checks for possible color anticipation. It does **not** specify the later reward-by-trigger-by-block accuracy analysis as the experiment-1 primary recoupling test, consistent with the authors' explicit exploratory label. A registration can contain multiple analyses of accuracy; the absence here concerns that specific later model, not all accuracy analyses.

The plan specified 48 viable participants, stopping at 48, and reporting analyzed 50 without excluding performance outliers. This is a visible deviation from the planned stop count; its reason is not established by the registration or the main paper. It is not evidence of outcome-dependent stopping, and we did not inspect recruitment or raw timestamps. The authors report their 12-person pilot power estimate was inflated, and they used 50 new participants for experiment 2.

The [experiment-2 registration link cited in the paper](https://osf.io/sev9k/) redirected the page-fetcher to sign-in; a later query returned page-not-found and its API retrieval failed. This is an **access problem**, not evidence that no registration exists or that its content differs from the authors' account. An authorized copy or accessible frozen link would be needed for direct verification. The paper states its experiment-2 recoupling analysis was registered before new data collection; treat that as the authors' report for now.

## 2. Why the pooled coefficient needs its interaction context

Paper Table 2 fits `accuracy ~ block × trigger × distractor + (1 | subjectID)`. With `b` the numeric block covariate *as actually coded in the fitted model*, and fast and neutral the reference levels implied by the table, the reported rounded coefficients give these contrasts in **log-odds**, not percentage points:

| Reward versus neutral contrast | Implied expression from Table 2 |
|---|---|
| Fast-triggered | `0.57 − 0.15 b` |
| Slow-triggered | `(0.57 − 0.65) + (−0.15 + 0.21)b = −0.08 + 0.06 b` |
| Slow minus fast reward contrast | `−0.65 + 0.21 b` |

This is algebra on rounded printed coefficients, not a refit or a new empirical result. The individual coefficients are conditioned on reference levels; reward `b=0.57` is the fast-trigger reward contrast at covariate **zero**, which may or may not correspond to an observed block depending on coding. The value of `b` and whether it is centered require the inaccessible script/data. Predicted probability differences further depend on baseline logits. Interactions' uncertainty and covariances are needed for confidence intervals on the contrasts; individual coefficient p-values do not determine the significance of each simple effect. The three-way interaction has `p=.053`: this is not evidence the interaction is zero, nor conventionally significant at .05.

The separate block-by-distractor model, which omits trigger, reports pooled reward `p=.083` and reward-by-block `p=.32`, while the full model reports coefficients at specified reference levels with interactions. Differences are not logically inconsistent and cannot be reduced to a single unqualified pooled average. The paper's experiment-2 interaction estimate `p=.045` supports that model's differential-by-trigger contrast, not a replicated significant reward main effect or verified mechanism.

The study's fast-trigger selection uses preceding RT, but an induced rare-trial manipulation could alter RT and response thresholds. Moreover, the reward, selected and novel special colors all appear on rare trials, unlike neutral colors from the ordinary pool. No rising accuracy trend across blocks is a useful check on *gradual* anticipation, but cannot rule out quick or stable learning of color as a rare-trial signal. Reward versus selected or novel contrast and trial-by-trial response-policy checks would be informative, subject to exact preregistration, coding and uncertainty. Neither anticipation nor speed–accuracy policy is demonstrated as the cause.

## 3. Precise file access and next gate

The [authors' OSF project](https://osf.io/anwzx/) and metadata list the following files. The web service gave HTTP 500 for the three direct ZIP downloads; the workspace's ordinary outbound network restrictions also do not permit direct OSF download. Metadata and an OSF ZIP-content preview are **not the contents** and are not independent verification of hashes or analyses.

| Listed file | Link | Metadata size and SHA-256 | Observed access |
|---|---|---|---|
| `analysis scripts.zip` | [OSF file page](https://osf.io/ud5v4/) / [download](https://osf.io/download/ud5v4/) | 21,500 B; `709b09527693d0c89f2e1ef6f72f4808853d120945cfdfafa2d31e8daf54e640` | file page lists filenames, including processing, test and training R scripts; ZIP download failed; scripts not read |
| `exp1.zip` | [OSF file page](https://osf.io/6thsg/) / [download](https://osf.io/download/6thsg/) | 7,930,558 B; `3b7f349012efd0a6b6acdc89f902de429860b22b324f81a986bfce9787b875de` | metadata only; ZIP download failed; contents not checked |
| `exp2.zip` | [OSF file page](https://osf.io/qg3cm/) / [download](https://osf.io/download/qg3cm/) | 7,771,323 B; `1b036ddcd105799e7a288e2a7479396398dc621a94c44a8249339d3815db0ea0` | metadata only; ZIP download failed; contents not checked |

Metadata source: [experiment 1 folder](https://api.osf.io/v2/nodes/anwzx/files/osfstorage/69de6e4fd405f0b36517d2cf/), [experiment 2 folder](https://api.osf.io/v2/nodes/anwzx/files/osfstorage/69de6e63d405f0b36517d2f2/) and [scripts folder](https://api.osf.io/v2/nodes/anwzx/files/osfstorage/69de70e762e36387bc17da09/). A pilot archive is also listed, but is not needed for the initial main-results reproduction. If these three archives are supplied, check hashes and contents, then inspect scripts and reproduce the reported counts, coding, preprocessing, convergence and coefficients before attempting any sensitivity analysis. Handle potential personal information conservatively; no permission to publish participant-level files is assumed. If the experiment-2 frozen registration can be opened by the user, a copy would enable direct comparison of registered and published analyses. No author request has been sent.

## 4. Implications for the project

Even a successful numerical reproduction would only establish that a reported behavioral analysis follows from particular records and code. It would not itself identify the subjects of experience, a same-window experiential conjunction, experienced centrality or q-dependent quality. P's local/global subjects retain numerically distinct private tokens; type correspondence is not token sharing. The L selector is not equated to IIT and no IIT quantity is computed. C3, B4–B5/F2, B9/F3 and B10 remain open, and PAINgen's 21 mean discrepancies still require its own actual conversion/export code. The 2026 study is not a split-brain study and supplies no direct patient-to-four-spin map.
