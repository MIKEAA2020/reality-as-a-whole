# A worked reported-content reference case

## 1. Positive result: a reference independent of a neural decoder

The identity pursuit now includes an inspectable **primary-author report-event record**, not only an eye-trace classifier. In a source-selected face-rivalry trial, the log contains seven dominance-report onsets, alternating **B, A, B, A, B, A, B**. Its same-directory parameter workbook associates pair 1 with two named face stimuli and distinguishes *percept* event codes from *image-on* codes. This supplies a concrete, defeasible reference route to a content contrast without fitting a neural latent state and then defining its output to be the experience.

The constructive lesson is not that reports are experiences. **Ordinary first-person discrimination is admissible evidence for experience**, with known limitations. Independent reference means independence from the candidate neural feature's selection and interpretation, not a physically uncaused or infallible oracle. We need not postpone every experiential reference until a completed consciousness theory exists. Stronger intervention-dependent claims, however, require stronger evidence that the reference remains reliable under the intervention.

This case is **face identity A versus face identity B**. It is not the frozen face/object H_Q1 target, not the motion-content H_Q2 branch, and not their empirical validation. It is a worked reference case, not an additional constitutive law. No physical maintaining organization has been matched to these events, and no qualitative identity or subject-incidence identity is claimed.

## 2. Primary source and bounded selection

Source: Tom Salomon and colleagues, *The reciprocal effect of value and arousal on conscious awareness in binocular rivalry task*, [public author repository](https://github.com/tomsalomon/BinocularRivalry/tree/fb86674524005027e8e9eb77b66f695d1df6d25f), pinned at `fb86674524005027e8e9eb77b66f695d1df6d25f`.

The README credits Tom Salomon, Yael Solar Priel, Yarden Shir, Keren Shoval, Rinat Kiperman, Liad Mudrik, and Tom Schonberg. It describes raw trial workbooks, associated stimulus parameters, and preprocessing. It explicitly permits reuse of data and scripts, requests academic credit, and points to an in-preparation manuscript. A published paper and its findings have **not** been retrieved or inferred from that description. The actual root license is `LICENSE` (MIT), although the README's link says `LICENSE.md`.

Before opening the event values, selection was fixed as the lexicographically first file matching `BR_Celebrities/BR_Data/**/rivalry_pair_01_sess_1.xlsx`, followed by `BR_params_default.xlsx` in that file's directory. There are 26 eligible first-trial files in the complete, non-truncated 27,130-entry source tree. This is a convenience/schema selection, **not** a random sample, a valid-subject selection, or a representative trial. No population inference follows from its report pattern.

[Five unmodified upstream files](sources/external/reported_rivalry_case/ATTRIBUTION.md) are archived: README, MIT license, `analysis/Script1_merge_BR_data.m`, one trial workbook, and its parameter workbook. [Provenance](sources/external/reported_rivalry_case/provenance.json) records original paths, sizes, and SHA256 hashes. No demographic records, subjective-value/arousal ratings, face images, IAPS images, eye recordings, or neural recordings were acquired. Public reuse statements are not a separate audit of participant consent or recruitment. The analysis is restricted to the small, pseudonymously filed behavioral record; no reidentification is attempted.

## 3. Establishing what the event labels denote

The trial's `Default` worksheet contains columns **Time** and **TTL**. Its first worksheet is empty; reading only that sheet would miss the record. The parameter workbook's `TTLs` sheet distinguishes:

| Code | Parameter description | Treatment in this audit |
|---|---|---|
| 1 / 2 | images on / images off | Trial boundaries |
| 11 / 12 | `<StimA> percept` / `<StimB> percept` | Source-designated dominance reports, not physical stimulus onsets |
| 21 / 22 | A-to-B / B-to-A piecemeal | End of the preceding exclusive dominance-report interval; subsequent time remains separately classified |
| 31 / 32 | `<StimA> on` / `<StimB> on` | Distinct physical image-event labels; neither occurs in this selected log |

The inspected merger script calls 11/12 *perception onsets*, calls 21/22 *stim1/stim2 end*, and checks for corrupted sequences due to simultaneous presses or unidentified keypresses. This supports reading these as intended report-derived perceptual events, rather than labels produced by the OKN algorithm or stimulus identities alone. **The task implementation, participant instructions, actual key-to-content mapping, and acquisition hardware timing have not been independently traced.** The interpretation is source-grounded, not fully protocol-validated.

For pair 1 the `Pairs` sheet lists A = `Tom_Hanks`, B = `Justin_Bieber`. These are names of the *stimulus identities*, not participant identities or a claim that the subject was representing every semantic attribute of the people. The matching filename and the source's pair-indexing convention support this intended reference. They do not verify the pixels actually displayed at every time point.

Parameter-file cautions matter. The workbook is named **default**, and its `Sessions` sheet says `Passive`. An `OldExpParams` entry gives trial length 30 with a seconds-based description that also contains an inconsistent legacy minimum-36-seconds comment. These fields are not proof of the executed condition, timing calibration, or absence of reporting demands. The merger's current default selects experiment 4 and capitalized `*Sub*` directory patterns, unlike this older celebrities-file path. We therefore do not claim to have rerun the author's current analysis successfully on this trial. None of these bounded documentation observations establishes a defect in the study's published findings.

## 4. Recorded event accounting

The log contains 15 events, strictly increasing timestamps, and only codes 1, 2, 11, 12, 21, 22. The source-defined dominance onsets are:

| Dominance onset order | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Reported label | B | A | B | A | B | A | B |

There are six changes between successive dominance reports. **That is not an independently measured count of phenomenal reversals**: unresolved intervals, return transitions, report delay, and unreported changes cannot be eliminated from these files alone. The final B report runs to the trial-end code; a separate B-termination event is not required at that boundary.

Following the source's next-event duration convention, every interval between consecutive logged events is allocated exactly once:

| Recorded interval category | Duration, rounded to 6 decimals |
|---|---:|
| After A-dominance onset until its next event | 14.847927 |
| After B-dominance onset until its next event | 5.020502 |
| Other/unresolved: initial latency and after piecemeal/termination events | 10.131873 |
| Total first-to-last span | 30.000302 |

The audit retains exact decimal differences of the stored timestamps. The table uses **recorded time units**; nominal seconds are suggested by the parameter description, but the clock, synchronization, and latency are not independently calibrated. Decimal precision must not be mistaken for biological or instrumentation accuracy.

The upstream merger pools time outside codes 11/12 into a variable called `fusion_time`. Here it remains **other/unresolved**. In particular, the roughly 2.019640-unit interval between images-on and the first dominance report could include sensory settling, decision/report latency, unreported dominance, or mixed content. We cannot allocate all 10.131873 units to actual mixed experience, to unconsciousness, or to either exclusive content. The 21/22 event descriptions are positive source labels for piecemeal transitions, but do not settle every instant of the subsequent interval.

This is a descriptive reference/accounting result. No arousal/value effect, dominance preference, alternation-rate population estimate, significance test, or neural decoder was fitted. The selection did not use outcome values. The observed A-duration excess is not interpreted as an experimental effect.

## 5. What has improved in the warrant ladder

The useful advance is **a content-referencing observation with a dictionary that was not learned from a neural feature**. Conditional on the ordinary evidential standing of the intended reports, A/B now have source-designated, discriminable reference rather than being arbitrary names attached to two hidden states. A harmless code renaming must transport that dictionary; exchanging fixed face references without transporting their evidence would be a substantive reassignment.

This makes a real, narrow correspondence test conceptually possible: independently select candidate physical organizations, estimate their relation to these source-anchored report intervals, preserve unresolved cases, and hold out appropriate blocks/conditions. We have **not** conducted that test, because no synchronized candidate neural basis is available in the selected files. Merely treating codes 11/12 as the basis would replace a constitution with its observation channel.

The six-rung [identity warrant ladder](QUALITATIVE_IDENTITY_PURSUIT.md#6-from-correspondence-toward-identity-the-warrant-ladder) therefore has the following local status:

1. **Reference:** an inspectable, prima facie content-report route in this worked case; instructions/runtime mapping and intervention validity remain to be checked.
2. **Physical individuation:** no independently selected content-maintaining organization yet.
3. **Correspondence:** no paired neural analysis or cross-channel calibration yet.
4. **Causal discrimination:** no maintenance/input/report-separating intervention established here.
5. **Identity:** the intrinsic-common-constitution conjecture remains to be justified, not inferred from report alternation.
6. **Whole-account closure:** one perfect complete actuality remains the governing account; the particular constitutive law must explain, not merely stipulate, this finite differentiation.

A report is a real physical event and defeasible evidence of the reported experience; these are compatible descriptions. The unified account must explain why such actual discriminations arise from the same concrete constitution as their experiential content. Its no-independent-selector obligation is sharpened by a fixed reference, not discharged by it. The incomplete local bridge does not downgrade the adopted complete-absolute endpoint or prove that constitution is impossible.

## 6. Why the two acquired sources cannot be spliced into calibration

The [OKN source](OKN_SOURCE_QUALIFICATION.md) supplies gaze positions and an inspectable classifier for motion rivalry, but no independent reports in its demo. This case supplies source-designated reports for face rivalry, but no paired gaze trace. They are different records, contents, and experimental settings. There is no justified event matching, shared timebase, common participant, or common calibration condition between them.

Consequently we cannot calculate sensitivity/specificity, delay, or report–OKN agreement by combining their separate outputs. Matching label counts or time fractions would not create a joint distribution. Nor can a classifier trained on eye-derived labels be treated as independently validated by these unrelated face reports. **The next required acquisition is paired validation evidence, not a fabricated join.**

For the motion branch the paired report/ocular validation protocol must be obtained under usable terms and transport assessed. For the frozen face/object target, source-specific instructions, content judgments and synchronized neural observations are needed; this face/face case cannot be silently substituted for it. A source-labeled `calibration` field or familiar methodological name alone is not an estimate of phenomenal error.

## 7. Reproducibility and scope

Run, with the Python standard library only:

```sh
python verification/reported_rivalry_case_audit.py
```

The [audit](verification/reported_rivalry_case_audit.py) checks all five source hashes, resolves named worksheets through workbook relationships, reads literal cells without executing formulas/macros, checks the event dictionary, rejects malformed/nonmonotonic/overlapping sequences, and exactly accounts for every recorded interval. Its [retained result](verification/reported_rivalry_case_audit.json) is deterministic. These are supplemental source/data diagnostics, not additions to the historical 1,149-test core suite and not an empirical discovery of a constitutive identity.

**Surviving conclusion:** independently source-anchored content reference is feasible without defining experience by a neural decoder. This worked case advances that reference task while keeping intervention-valid calibration, physical individuation, causal discrimination, and the identity argument distinct.
