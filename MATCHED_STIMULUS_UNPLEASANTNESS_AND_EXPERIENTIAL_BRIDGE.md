# Matched stimulus, reported unpleasantness and the missing bridge

## Result and boundary

The user's idea is that a relevant internal misalignment might be intrinsically uncomfortable. A tempting shortcut is to treat the *external painful stimulus itself* as the mismatch, bypassing identification of the subject's internal state. A new bounded reanalysis of the project's previously used PAINgen dataset shows why that shortcut is insufficient for observed human reports: at the same participant, nominal stimulus modality and nominal level, control and placebo conditions have different average unpleasantness reports.

This is **not a test or refutation of the actual integrated candidate's internal `q`**. The stimulus and `q` are different quantities. Placebo context can change internal physical dynamics, attention, learning, report criteria and other processes. The dataset does not measure the proposed subject-internal phase or spin mismatch. Nor is this an independent discovery of placebo analgesia: the source authors already reported it. What is new here is an explicit matched-pair constraint and exact empirical fit floor for this restricted stimulus-only shortcut.

## 1. Model and source

A restricted model may use an arbitrary participant-specific function of stimulus modality and nominal level, but must give the **same expected report** for placebo and control when those variables are held fixed. Thus it is allowed to know the participant and allow any nonlinear dose response; the feature it lacks is the treatment condition and any internal state changed by it. Noise is permitted in actual measurements. The model's identical outputs are a sharp structural prediction, not an assumption that all people's pain should match.

The published experiment by Botvinik-Nezer et al., [*Placebo treatment affects brain systems related to affective and cognitive processes, but not nociceptive pain*](https://doi.org/10.1038/s41467-024-50103-8), provides thermal and mechanical conditions, treatment conditions, and unpleasantness ratings. The authors already discuss strong correlations between sensory intensity and unpleasantness and caution against assuming an affect-specific neural signature. We reuse their pinned condition-mean table and interpret self-reports as important evidence, not as infallible recordings of every aspect of experience. The full raw trial history, independently validated physiological mismatch and neural phase data are not provided by this table.

The [analysis plan](PAINGEN_STIMULUS_ONLY_VALENCE_STRESS_TEST_PLAN.md) was fixed before this calculation but after the authors' publication and the project's previous exploration. It is **retrospective, not preregistered or blinded**. The source's published analyses and this calculation are not independent replications. The earlier [out-of-family benchmark](PAINGEN_UNPLEASANTNESS_BASELINE_AND_MISMATCH_GATE.md) used the same data for a different prediction comparison.

From 4,687 condition rows, 307 have missing unpleasantness. Among 2,352 participant × modality × level cells represented in the table, 2,155 have usable means in both control and placebo, while 197 do not. The complete pairs involve 369 people in 236 families; each person contributes multiple cells, so the cells are not independent people. Matching is by **nominal coded modality and level**, not independently verified equality of every delivered waveform, exposure history, body site, neural state or temporal context. The experiment's treatment, conditioning and ordering are not interchangeable; the comparison alone cannot isolate a single cause.

## 2. Actual matched observations

For each matched cell let `d = control report − placebo report`, in the source's numeric unpleasantness scale. Positive values mean a higher control report. The intervals below are descriptive 95% percentile intervals from 5,000 resamples of whole families, not cells. They are conditional on sampling assumptions and complete-case selection; they do not remove the study's fixed design, ordering, measurement limitations or possible biases.

| Subset | Pairs | Mean `d` | Family-bootstrap interval for mean `d` | Positive / negative / exact ties | Oracle equal-output RMSE floor |
|---|---:|---:|---:|---:|---:|
| All | 2,155 | 0.04466 | [0.03516, 0.05418] | 1,349 / 664 / 142 | 0.07158 |
| Thermal | 1,080 | 0.05258 | [0.04137, 0.06372] | 696 / 351 / 33 | 0.06972 |
| Mechanical | 1,075 | 0.03670 | [0.02423, 0.04933] | 653 / 313 / 109 | 0.07339 |

These are **condition means**, not individual trial observations; the signs and ties describe observed cell differences, not the fraction of individuals for whom placebo worked. A numeric mean or RMSE treats the recorded scale as approximately interval-valued. The sources' labels are not cardinal physical units of suffering; report scales, memory, condition order and response strategies remain relevant. The signs provide less scale-dependent information but do not solve those issues.

The overall nonzero direction is consistent with the authors' published placebo finding, and the exploratory bootstrap intervals do not include zero under their assumptions. This challenges a model that predicts no *population-average* context difference in the selected cells, if its report channel is otherwise unbiased in both conditions. It does not establish equality or difference in every participant, identify an internal mechanism, or by itself tell us whether the report difference fully reflects a phenomenal difference. Experience is valid data; communication can nonetheless be imperfect.

## 3. What the fit floor proves—and does not

Let the two observed condition means in pair `i` be `a_i` and `b_i`, and let the model output the same number `p_i` for both. Then

```text
[(a_i−p_i)² + (b_i−p_i)²]/2
  = (a_i−b_i)²/4 + [p_i−(a_i+b_i)/2]².
```

Therefore its RMSE across the `2N` rows is at least

```text
(1/2) sqrt[(1/N) Σ_i (a_i−b_i)²].
```

The result above is **0.07158** for all pairs. This bound lets an oracle inspect *both outcomes* and choose a different optimal midpoint for every matched pair. It is an in-sample algebraic lower bound for equal-output models, not held-out performance, irreducible biological noise, evidence of a meaningful clinical threshold, or a lower bound on error in feelings. Any noisy stochastic model's realization may differ; the equality constraint applies to its point prediction, not necessarily to individual observed reports. Nonzero in-sample floor alone does not disprove equality of latent means: measurement noise can create it. The family-bootstrap comparison addresses a different quantity, the observed mean contrast, with the stated assumptions.

Neither these averages nor a well-fitting context predictor identify the thing that constitutes an experience. A context variable could predict reports through multiple rival causal paths. Nor does identifying an association require denying consciousness: the first-person datum is preserved while its external measurement and interpretation are evaluated.

## 4. Consequences for the integrated candidate

1. **Do not silently substitute the stimulus for q.** The source table does not measure preferred offsets, channel-specific phases or the subject boundary. The external stimulus-only rule is much narrower than the user's proposed relational mismatch. It is inadequate to reproduce the observed average contrast in this study under an unbiased-report model, but internal-mismatch identity remains untested.
2. **Specify context physically.** A revised bridge should say in advance how the same nominal input plus different treatment contexts generate independently measurable subject-internal relations. A free context adjustment learned directly from these unpleasantness outcomes may improve prediction without identifying the relevant relation.
3. **Connect the representation to the subject.** The same person is an experimental identifier, not a derived phenomenal unity or persistence certificate. The [horizon audit](INTEGRATED_SUBJECT_HORIZON_AND_VALENCE_AUDIT.md) showed that the present L rule can select different sets at different causal horizons; this empirical comparison does not decide between them.
4. **Demand a discriminating positive test.** Define physical channels, preferred offsets, subject boundary and time grain without using the held-out unpleasantness outcome. Then compare the candidate with an external stimulus/context baseline and established physical predictors on independently collected or appropriately held-out observations, including matched-stimulus conditions where they make different prespecified predictions. The report channel and uncertainty need independent support. A failed physical readout is inconclusive about the identity; a verified prediction is evidence for the bounded model, not a proof that its structure is what unpleasantness *is*.

The PAINgen condition table cannot execute step 4 because it contains neither the requisite phase-resolved relations nor their independently validated preferred offsets. Existing fMRI signatures are comparators, not mismatch measurements. Defining `q` from the same outcome would make the intended bridge circular. A new data source or demonstrably available suitable measurements are required for that particular test; none is claimed here.

## 5. Battery, source scope and reproduction

This is a concrete empirical constraint on a **restricted proxy** and a clearer identification requirement, not a substantive B5/F2 pass or a new demonstration of placebo analgesia. B4 subjects and persistence, B5 qualitative identity, and the self-sufficient experiential ground remain open. C3 remains **full structural and experiential intelligibility**, required jointly with all seven criteria; this result does not satisfy it. The external battery's unavailable preregistration, program, JSON and freeze artifacts still prevent independent replay.

For this analysis, we revisited the abstract and introduction (chunks 0–2 of 36) of Botvinik-Nezer et al.'s [published article](https://doi.org/10.1038/s41467-024-50103-8), plus the specific source table and the project's prior source and protocol audits; we have not fully re-read its full text, all methods, figures, supplements, raw MRI, trial records, preprocessing or original program in this turn. The aggregate source file is authored by the same study team, not independent evidence. The later user-supplied PDF of Rainville et al., [*Pain Affect Encoded in Human Anterior Cingulate But Not Somatosensory Cortex*](https://doi.org/10.1126/science.277.5328.968), has now been fully read, including its notes, Table 1 and both figures; the [full-paper audit](RAINVILLE_PAIN_AFFECT_FULL_PAPER_AUDIT.md) records its selection and statistical limitations. Its underlying data and code were not inspected. That study is not used as a numerical input here.

Run `PYTHONPATH=/path/to/numpy python verification/paingen_stimulus_only_valence_test.py` after installing `verification/requirements-framework-battery.txt`, or use `--data PATH` for the exact pinned local CSV. The script downloads at most the single fixed 3,728,915-byte file, checks its SHA-256 and size, and writes only an [aggregate receipt](verification/paingen_stimulus_only_valence_test.json). No participant IDs or rows are saved to this repository. Deterministic bootstrap and pair construction are reproducibility checks, not independent evidence for the wider framework.
