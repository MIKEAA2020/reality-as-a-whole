# Frozen S09-to-S08 EEG/report transfer protocol

## Status and purpose

This protocol and its implementation were written **before obtaining or scoring any S08 EEG in this work**. The S09 model and its development were post-hoc; this is not a preregistered experiment, an independent study, or proof of experience. The aim is a bounded, participant-held-out *feasibility* check of a fixed report predictor from the same published dataset. S09 and S08 are different participants, but share a study, acquisition system and preprocessing; one additional participant cannot establish population generalization.

A filename search of the connected Dropbox on preparation found S09 filtered EEG files but **no S08 files**. No S08 participant data or results are claimed here. The selected scans 1, 3 and 5 are listed as rivalry in the pinned [Lyu reanalysis condition file](https://github.com/Aubrey-Lyu/BR-project/blob/b8ca204024a4f7151645c6c2e908eb564203ac66/info_scans_conditions.m) (`s8`). This is a public secondary source, not independent verification of actual trial stimuli; confirm against original documentation or records. The three scans were requested before this protocol, without having verified their S08 condition in the preceding answer; the source check now supports that selection. Do not change the three based on their outcomes. S08 scans 7 and 9 are also listed as rivalry in that file, but are outside this bounded first check.

## Fixed analysis

- **Training:** use the stored fit from S09 rivalry scans 1–3, not S08 or S09 test scans. Code-1 centroid `0.01598754217666589`, code-2 centroid `0.2368399778715139`, majority class 2 and 21 fixed per-position majority labels are copied from [the earlier result](verification/roy_s09_eeg_report_transfer.json). No S08 normalization, recalibration, direction flip, feature selection or refitting. Equal distances go to code 1. Absolute cross-person transfer is a deliberately stringent benchmark, not the only valid decoding method.
- **Selection and feature:** use the unchanged [S09 extraction/scoring implementation](verification/roy_s09_eeg_report_transfer.py). From five assumed 42-second trials per scan, reconstruct report codes from the recorded latency events, unknown before the first event in each trial and carried forward thereafter. Split each trial into 21 two-second windows; use only windows wholly in code 1 or 2 with no marked bad sample. POz feature is the log10 lower-to-higher stored-tag power ratio, using mean subtraction, symmetric Hann taper and frequency projections. The inherited implementation checks 250 Hz, the POz label, expected sample dimensions, tag frequencies near 6.6667 and 8.5714 Hz, trial bounds and marker ordering. Different acquisition, trial structure, event meaning or tag assignment is a **stop for this fixed analysis**, not an invitation to adapt it after viewing results.
- **Mapping gate:** before scoring, document from trustworthy study records that S08 codes 1/2 have the same meanings as S09 codes 1/2 and code 3 has the same mixed-state semantics. A color or eye interpretation is not inferred from code numbers. If the coding correspondence cannot be substantiated, do not report a primary cross-person score: record the blocker and seek records. The program requires an explicit attestation and its provenance but cannot independently verify it. Identical numeric tag values alone do not establish matching event-code semantics or stimulus assignment.
- **Comparators:** the frozen S09 training-majority rule and frozen 21-position time-only rule use no S08 EEG and no S08 fit. Identical selection and abstentions apply to all three. The time-only baseline may reflect task structure, not a causal control.
- **Outcomes:** report each of the three scans and the combined descriptive counts, without selecting the best. For each rule show pure-clean confusion matrix, both class denominators, accuracy and balanced accuracy when both classes occur. Also show all 105 windows per scan and full-grid correct/105 and `1 − correct/105`. The latter counts unresolved, mixed, transition and bad-epoch windows as failures by convention; it is not a measured experience-error rate. Report unresolved and pure-but-bad counts separately. Pooled 315-window fractions are descriptive, not independent observations; the participant, runs and within-run windows are correlated. No p-value, confidence interval or generalization claim from treating windows as independent.
- **Interpretation:** predefined qualitative comparison is per-run and pooled EEG versus each baseline; no post-hoc success threshold, selective exclusion, statistical significance claim or retuning. A small or negative advantage is a finding about this fixed rule and selected reports, not proof that EEG decoding is impossible. Positive agreement does not validate experience accuracy, causal consciousness theories, replay independence or fMRI alignment.

## Inputs, stops and reproducibility

Retrieve only individual S08 EEG `.mat` files 1, 3 and 5 if available. Do not download a whole subject archive. Keep raw data, manifest with private paths, and potentially identifying metadata out of Git. Check noncommercial research terms and cite [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024). Record provenance and a SHA-256 for each input; compare to an independently supplied authoritative checksum if available. A self-computed hash by itself only fixes file identity, not authenticity. Stop on absent scans, unverified correspondence, malformed inputs or failed hashes; report why rather than swapping scans or guessing parameters. Do not expose event sequences or raw metadata.

The runner takes a private JSON manifest with this exact shape (illustrative strings below are **not evidence or usable hashes**):

```json
{
  "participant": "S08",
  "event_code_mapping": "same_as_S09",
  "event_mapping_evidence": "cite actual source and relevant page or record",
  "condition_evidence": "cite actual source and relevant page or record",
  "files": {
    "1": {"path": "/private/S08_scan1_filtered_gac_cbc.mat", "sha256": "actual lowercase 64-hex digest"},
    "3": {"path": "/private/S08_scan3_filtered_gac_cbc.mat", "sha256": "actual lowercase 64-hex digest"},
    "5": {"path": "/private/S08_scan5_filtered_gac_cbc.mat", "sha256": "actual lowercase 64-hex digest"}
  }
}
```

Once the gates are met, run `python verification/roy_s08_fixed_transfer.py /private/manifest.json`; it emits aggregates only. The evidence strings are not emitted and should be documented separately in a privacy-safe report. Synthetic tests are `python verification/roy_s08_fixed_transfer_test.py` and `python verification/roy_s09_eeg_report_transfer_test.py` with NumPy and SciPy installed. Successful tests demonstrate the implementation on fixtures, not actual S08 compatibility or event semantics.

## Framework significance and next scale

This check probes a necessary measurement link—whether a fixed physical signal predictor tracks another participant's **reports**—not the metaphysical claim that intrinsic reality is experiential. Even perfect report agreement would leave report-to-experience correspondence and subject individuation unproved. For meaningful generalization, predefine a larger subject-level held-out analysis using all eligible participants, participant-level uncertainty, and replay-lineage grouping where relevant; first resolve missing files and mapping. A separate prospective intervention and independently justified assay-error bounds would be needed for the stronger experiential/constitution gate described in [the feasibility audit](RIVALRY_EEG_FMRI_FEASIBILITY_AND_REANALYSIS_GATE.md).
