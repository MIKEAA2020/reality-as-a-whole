# First-person affect under stimulation: a quality constraint and a source audit

## Result and status

Yih and colleagues' [*Intensity of affective experience is modulated by magnitude of intracranial electrical stimulation in human orbitofrontal, cingulate and insular cortices*](https://doi.org/10.1093/scan/nsz015) provides unusually direct evidence: clinically administered brain stimulation was followed by patients' verbal descriptions of changes in affective experience. In one selected case the paper reports four increasing degrees of distastefulness at the same electrode pairing. This is relevant to the proposed discomfort bridge because it takes the subject's own experience seriously and asks about **quality**, not merely whether an external stimulus was present.

We make two bounded contributions:

1. An exact **conditional** two-level fit calculation for that published example: even choosing the best two numerical levels after seeing the reported values, the least possible RMSE is about **7.91 percentage points**, assuming the four displayed percentages are comparable and must be represented by the same fixed two-level readout. This tests a strengthened simplified quality package, **not** the original E-L contrast or a measured neural mismatch.
2. A direct arithmetic audit of the paper's [supplementary table 2](https://pmc.ncbi.nlm.nih.gov/articles/instance/6537947/bin/supplementary_data_nsz015.docx): **8 of 30 displayed per-trial charge cells across 4 of 15 paired rows** disagree with the table's own stated multiplication formula and other displayed parameters. Two sets of identical listed parameters also have different printed charge totals in different rows. The underlying delivered charge and actual clinical records are unknown; these are reporting inconsistencies, not proof that the stimulator or authors' analysis was wrong.

The article does not measure the candidate's `q`, establish what constitutes a subject, or derive why any physical state feels unpleasant. The formal battery remains open; C3 is **full structural and experiential intelligibility**, jointly with C1–C7. No new invasive clinical procedure is proposed.

## 1. What was observed and what was not

The authors retrospectively selected **18 people** with medically refractory epilepsy from a pool of 129, with anatomically suitable clinical mapping and parameter variation. They studied 140 electrodes of interest in anterior cingulate, orbitofrontal and insular regions; 65 sites were identified as affective “hot spots.” Stimulation was part of clinical mapping, not a randomized, standardized dose-response study designed for this framework. Anatomical coverage and stimulation schedules were clinically constrained; sites, trials and people are not interchangeable independent observations.

The clinicians asked broad questions such as whether the participant noticed a change and, where needed, additional questions to clarify character and valence. Two raters reviewed reports and video-EEG recordings, according to the paper. The authors attempted to exclude epileptic-zone stimulation, seizures and afterdischarges, and used occasional sham stimulation in **11 of 18 patients**. Their stated criterion excludes sham-induced *similar effects*, but the paper does not establish that every comparison had an informative sham or that all reporting bias was eliminated. Identical prompts do not by themselves demonstrate no demand effects, and absence of a reported effect is not proof of absence of all experience.

The paper reports negative, positive, mixed and unclear valence categories, and describes changes in intensity and content at different sites and settings. Its statement of a positive intensity relationship “in all cases” refers to the authors' selected 65-site set. The figure caption itself describes each selected hot spot as exhibiting a change in intensity; the selection and coding details are not sufficient here to establish an independent denominator of all eligible stimulation trials or a universally monotonic law. Table 3 also includes changes in qualitative content and cases where more than frequency or amplitude may differ. We have not independently reconstructed the original selection or statistical analysis.

## 2. A first-person four-level example

For one participant and one OFC electrode pairing, the main table and supplement report the following adjacent comparisons:

| Frequency | Reported description | Number given in report |
|---:|---|---:|
| 2 Hz | very little smell, distasteful | 10% |
| 5 Hz | bad smell | 20% |
| 10 Hz | distasteful smell | 40% |
| 20 Hz | very distasteful smell | 60% |

The supplement states 5 mA for these comparisons. The first two comparisons used 5-second durations at both endpoints; the final `10→20 Hz` comparison lists **5 seconds versus 3 seconds**. Thus frequency and duration are not fully isolated in the last contrast. The supplement lists `0/1`, `0/1`, and **`1/1`** under “reports during sham / total sham” for the three respective comparisons. It does not give enough information here to determine whether the one sham report in the final comparison was the same effect as the stimulated report, how it entered eligibility, or the complete sequence and blinding history. It should not be silently ignored.

The reports are important first-person evidence, but the four percentages are quoted summaries from a selected case, not four independently replayed trial records, an independently calibrated interval scale of suffering, or proof that all other sensory qualities and contexts were held fixed. Repeated endpoints in adjacent descriptions must not be counted as independent trials. This example cannot establish a population dose-response function or a stimulation-induced change in the candidate's internal mismatch.

## 3. Precisely which binary law would be challenged?

The original E-L pair postulate specifies **an unpleasant-versus-neutral contrast**, and explicitly does not give an intensity magnitude. It is therefore not falsified by four ratings: its unspecified additional experiential qualities or reporting channel could vary. Our later [cross-scale extension](INTEGRATED_CROSS_SCALE_SUBJECT_QUALITY_GATE.md) compared a *stronger* binary intensity law with a graded law in a stipulated four-spin whole, not in a human OFC. That model is not independently linked to this patient or to stimulation frequency.

Consider only a strengthened, explicitly falsifiable **two-level readout package** for this reported case:

* the four compared episodes instantiate one defined subject and the same target quality;
* an internally defined binary physical/phenomenal state fully fixes its numerical unpleasantness on a stable common scale, with **only two possible values**;
* the displayed percentages faithfully reflect those values, apart from a bounded error, with no additional frequency-, duration-, history- or context-dependent change in the readout.

Give this package an oracle: after seeing `10,20,40,60`, it may pick any two real numerical levels and assign each of the four reported values whichever label minimizes the specified error. Enumerating all 16 assignments gives:

| Loss on the four displayed values | Best possible two-level result |
|---|---:|
| Root mean squared error | `sqrt(125/2) ≈ 7.906` percentage points |
| Mean absolute error | `7.5` percentage points |
| Maximum absolute error | `10` percentage points |

For squared loss, one optimal assignment groups `10,20` at `15` and `40,60` at `50`. Each error criterion is optimized separately; the numbers are in-sample, not confidence intervals. The calculation does not establish that the retrospective report is accurate to any of those thresholds. For example, a fixed maximum error **strictly below 10 points** would be inconsistent with this two-value package on all four displayed values, but no such independently validated error bound has been supplied. An unconstrained lookup with four labels fits the four numbers exactly and offers no out-of-sample explanation.

A binary latent contrast plus a richer report channel, extra background qualities or context dependence can reproduce more than two reports; those additions must be stated and independently motivated rather than hidden. A graded E-L+ would also require a justified brain-state realization and scale. Neither extension is verified or refuted by an unmeasured spin-model variable. The empirical challenge is not that this patient “proves a continuum of qualia,” but that a universal binary-*intensity* account with a fixed accurate readout has a sharper obligation than the original binary contrast.

## 4. Supplement charge discrepancies

Supplementary table 2 defines a per-trial charge as **charge per pulse × frequency × duration** and lists the factors for 15 paired comparisons. The audit transcribes all 30 cells, checks them with exact arithmetic and finds 8 mismatches in 4 rows. The discrepancy counts include repeated entries of the same displayed setting, so they are **not eight independent experimental errors**.

| Participant / listed comparison | Per pulse and duration | Printed total | Product of the displayed factors |
|---|---|---:|---:|
| 10, OFC1–OFC3, 50 Hz | 1 µC, 1 s | 100 µC | 50 µC |
| 10, same pairing, 2 Hz | 1 µC, 5 s | 50 µC | 10 µC |
| 10, same pairing, 5 Hz | 1 µC, 5 s | 125 µC | 25 µC |
| 10, same pairing, 10 Hz | 1 µC, 5 s | 250 µC | 50 µC |
| 12, OFC1–OFC2, 5 Hz | 1.2 µC, 1 s | 36 µC | 6 µC |
| 12, same pairing, 2 Hz | 1.2 µC, 1 s | 14.4 µC | 2.4 µC |

Several values recur across rows. In particular, the supplement prints **250 µC and 50 µC** for the same subject-10 pairing, `10 Hz`, `5 s`, `1 µC/pulse` in different comparisons; it prints **36 µC and 6 µC** for the same subject-12 pairing, `5 Hz`, `1 s`, `1.2 µC/pulse`. These contradictions are visible without assuming a specific physiology or pulse-width interpretation. The paper describes charge-balanced stimulation, and its displayed “charge per trial” formula is not the same as saying a charge-balanced waveform has nonzero net delivered charge. Our comparison uses **the source's own definition**, not an independently validated charge-density convention.

The actual pulse counts, hardware settings, raw clinical logs and waveforms were not inspected. Alternative transcription errors or omitted settings may explain the numbers; the record is insufficient to select which fields are correct or to conclude that any patient received a particular dose. The discrepancies warrant caution when using these rows for charge–experience dose-response calculations. They do not erase the reported experiences, invalidate all findings, or establish that frequency itself had no effect.

## 5. What can make the next test informative?

A defensible next step using only ethically collected clinical data would first reconcile stimulation logs, waveforms, electrode pairing, sham sequence and the report transcript. For a fixed, report-accessible person and target, independently define a physical state or dynamical relation, with time grain and reference conditions chosen without fitting the held-out ratings. Compare a graded rule, a binary rule **with an explicitly constrained report channel**, and experience-respecting non-mismatch rivals using the same episodes. Include null/sham, duration, site, frequency, order, attention and prior-report controls where data permit, with person-level or session-level held-out evaluation and predeclared report-calibration assumptions. Selectivity and safety restrictions may make such a comparison impossible with the available records. Electrical stimulation and behavioral reports are not direct measures of preferred interactions or the intrinsic nature of a subject.

A convincing outcome could constrain a particular calibrated bridge or reject its joint assumptions; it would not alone establish a self-sufficient experiential whole, subject persistence, quantum weights or gravity. Conversely, inability to establish a calibration is not evidence that experience is illusory.

## 6. Scope and reproduction

For [Yih et al.](https://doi.org/10.1093/scan/nsz015), the full main prose through the discussion, the visible main tables and figure captions were read, and both supplementary table texts were inspected via the linked DOCX. **The figure images, supplementary video, individual clinical recordings, stimulation logs, original analysis code and raw EEG were not inspected.** The cited earlier works were not independently re-read for this audit. The manuscript is peer reviewed; our arithmetic and conditional model comparison are retrospective, not preregistered and not independent empirical replication.

The [fixed plan](DIRECT_STIMULATION_AFFECT_AND_CHARGE_AUDIT_PLAN.md), [verifier](verification/direct_stimulation_affect_audit.py), [tests](verification/direct_stimulation_affect_audit_test.py) and [receipt](verification/direct_stimulation_affect_audit.json) give the transcription and exact calculations. Run `PYTHONPATH=verification python -m unittest -v direct_stimulation_affect_audit_test` and `python verification/direct_stimulation_affect_audit.py`. These are checks on a manually transcribed table, so transcription remains a source of error; compare against the original supplement.

**Battery:** B4–B5/F2 remain open: a reported quality contrast is not yet a constitutive derivation or subject-incidence law. B9/F3 and B10 remain open; the paper is evidence relevant to an interface, not a validated test of the complete framework. No external battery replay is claimed.
