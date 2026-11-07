# Isolated cortex, anesthesia, and the boundary of a subject

## Result and scope

The current evidence distinguishes **physiological organization**, **access to the environment**, **reportable experience**, and **the number of experiencers**. It does not establish an extra subject inside a disconnected hemisphere, or establish that such a subject is absent. Hemispherotomy, callosotomy, and removal of a hemisphere are distinct operations; evidence from one cannot be directly substituted for another.

Two substantive findings sharpen the inquiry:

1. In separate hemispherotomy studies, isolated tissue shows both preserved fMRI default-mode-like correlations and EEG slowing resembling deep non-REM sleep. These observations need not conflict: they measure different features, in different cohorts, and neither alone establishes the presence or absence of experience.
2. The paper reporting the EEG result describes its released MATLAB and Python spectral-fitting implementations as equivalent. **The released versions use different peak-rejection thresholds.** A reproducible synthetic example shows that changing this threshold alone can change the Python output. We do not know whether this affects any patient result, have not run MATLAB, and have not analyzed patient data. This is a bounded reproducibility finding, not a refutation of the study.

The overarching framework remains a conjecture: a self-sufficient, necessarily actual whole with experiential intrinsic nature and genuinely plural subjects. These neuroscience data do not derive that whole, strong possibility = actuality, or a unique subject-constitution rule. A non-agentive plural whole is not the earlier intended universal agentive consciousness.

## 1. Which disconnection?

- **Callosotomy** primarily severs the corpus callosum; other commissural and subcortical pathways can remain. Its degree and accompanying surgery matter. Each hemisphere is not automatically deprived of thalamic and brainstem inputs. For behavioral timing and shared-information limitations see the [split-brain evidence review](SPLIT_BRAIN_TIMING_RIVALRY_AND_POOLED_EVIDENCE.md).
- **Hemispherotomy**, as discussed here, aims to disconnect diseased cortex from extensive cortical and subcortical pathways while leaving tissue and vascular supply in place. The extent of disconnection differs among procedures; residual routes, such as olfactory afferents in some cases, require anatomical assessment. It is not a clean experiment removing only the corpus callosum. See [Colombo et al.](https://doi.org/10.1371/journal.pbio.3003060).
- **Hemispherectomy** involves removal rather than leaving a disconnected hemisphere in situ. The connected remainder can support report and behavior, but this does not answer what a retained, disconnected hemisphere experiences.

Shared blood supply is not itself proof of effective neural communication, and an absence of detectable correlations is not proof that all possible communication or phenomenal unity is absent. Anatomical disconnection must be assessed in the individual case.

## 2. The empirical evidence

### A. Network organization after childhood hemispherectomy

[Kliemann et al. (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6914265/) examined six high-functioning adults who underwent hemispherectomy in childhood, six local controls, and a normative sample of 1,482. The connected remaining hemisphere retained recognizable within-network organization; between-network correlations were elevated in most patients. This is evidence of functional organization and possible reorganization in a **connected** surviving hemisphere. Childhood onset, selection of high-functioning participants, developmental plasticity and retained subcortical support limit extrapolation to an isolated adult cortex. Functional connectivity is BOLD correlation, not proof of signal transmission or of one or multiple subjects.

### B. Isolated tissue can retain network-like correlations

[Bauer et al. (2026)](https://doi.org/10.1093/braincomms/fcag211) retained 26 post-hemispherotomy patients after motion exclusions and studied 24 controls. **The isolated-hemisphere seed analysis used only eight of the 26**, selected by the study's lesion-overlap criterion; the connected-hemisphere analysis used 26. The isolated-side default-mode pattern was a *group-level* result, not 26 independent demonstrations or a count of conscious islands. In two patients with pre- and postoperative scans, network-related seed patterns appeared on both sides after surgery, with qualifications described in the paper.

The 26 included varied ages at surgery (median 11.5, range 0–49 years), pathology and time to scan. Nonlinear registration in abnormal anatomy, 6-mm smoothing and possible signal contamination near the midline are important limitations. The authors invoke default-mode activity as a necessary condition for consciousness, but that necessity is a theoretical and empirical claim, not an established general law. The absence of a statistically significant difference in a connectivity comparison does not establish equivalence. BOLD patterns neither demonstrate subjective experience nor count subjects.

### C. Isolated tissue can also show sleep-like electrophysiology

[Colombo et al. (2025)](https://doi.org/10.1371/journal.pbio.3003060) retrospectively analyzed pre/post quiet-wake EEG from ten children with drug-resistant epilepsy: **seven whole-hemisphere and three temporo-parieto-occipital disconnections**. The postoperative recording delay averaged 19.8 months. On the disconnected side the slow-delta power and broadband spectral slope changed toward a slow-wave-dominated pattern; the postoperative spectral exponent was more negative than the homologous connected side in all ten. The typical postoperative exponent lay between pediatric N2 and N3 reference distributions. The authors find that the evidence provisionally favors absent or reduced awareness, without proving either.

This is stronger than merely observing that patients cannot report from the isolated tissue: it shows physiological reorganization compared with both the presurgical and contralateral measurements. But the disconnected cortex was pathological before surgery, participants were clinically selected, EEG is a spatially limited projection, and slow-wave activity and spectral exponents are proxies, not direct readings of experience. The disconnected state was **not identical to ordinary NREM sleep**: its slow waves differed in amplitude and period and spindle activity was absent. The study's EEG markers have a history of empirical use, but their sensitivity and specificity cannot simply be assumed to transport unchanged to an isolated, diseased cortex.

Bauer and Colombo are different studies with different inclusion criteria, techniques and acquisition times. We do not assert patient overlap or independence at the person level. It would be incorrect to place their measurements in the same patient or claim to have observed both patterns simultaneously. A *joint* fMRI–EEG study would test their coexistence rather than assume it.

### D. A wakefulness/sedation difference is not the same as an experience/no-experience difference

[Bajwa et al. (2025)](https://doi.org/10.1038/s41598-025-12695-z) studied 20 healthy adults during propofol deep sedation. Of 52 attempted awakenings, the **combined report classification** yielded 24 experience, five no-experience, and 23 no-information cases. These are awakenings, not 52 independent participants. Some could not be aroused or give interpretable answers. The numbers differ from either single question's counts; the combined scheme should not be conflated with them.

PCIst and single-channel Lempel–Ziv complexity decreased between awake and sedated conditions, but the study found no statistically significant differences among report categories **within** sedation. There were only five no-experience reports, incomplete TMS data, and temporal mismatch: the PCIst acquisition ended about one minute before awakening. Recall, amnesia and the awakening itself may misclassify or alter the relevant experience. A nonsignificant result is not proof that PCIst or LZc have no association with experience, nor is it a validation or invalidation of Colombo's spectral exponent: these are different measurements and populations. It does rule out treating the sedation-state contrast in this study as a demonstrated within-state experience detector.

## 3. A specific code-reproducibility check

Colombo et al.'s [methods](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003060#sec002) link a MATLAB implementation and an equivalent Python translation. The archived [Zenodo release](https://doi.org/10.5281/zenodo.16936516) publishes both, together with individual plotted data in XLSX files; raw pediatric EEG and imaging are not publicly released. We inspected the code at GitHub commit [`4bd4929d3a052d1c7eb0a5fb73ff860c4e4ac421`](https://github.com/milecombo/spectralExponent/tree/4bd4929d3a052d1c7eb0a5fb73ff860c4e4ac421). The downloaded GitHub files' MD5 values match the Zenodo listing: `ebf64a9967ea9d4c49ccbdd871373b6f` for Python and `20f7e850d10501610be30f64d7a522dc` for MATLAB. Python SHA-256 is `45baa3452b2d2830723126e83453e8552370e023f8089ea930d36dfa055438e7`; MATLAB SHA-256 is `5832057ff5e9a613a1d2d64a15b3f117669a3a04dcb5a182ca91cb3fe5d59512`. We checked the GitHub file bytes against **listed** Zenodo MD5 values, not a separate download and hash of the Zenodo binaries.

In the published MATLAB listing, the peak threshold is `max(median absolute deviation of preliminary residuals, 0.1)` and a detected candidate peak is discarded from the peak list if its residual is **below** the threshold (so that peak does not trigger exclusion of its frequency cluster). The Python listing comments out the 0.1 floor and keeps peaks only when residual is **strictly greater** than the median absolute deviation. The equality convention and MATLAB's fallback when a second regression fails are additional differences. This is a code-level comparison, not a complete cross-language audit.

We ran the **original pinned Python**, and then the same Python code with just the 0.1 floor added. The input was a specified synthetic PSD with a small Gaussian peak, not a biological signal:

| Calculation | Peak threshold | Resampled points excluded | Fitted slope |
|---|---:|---:|---:|
| Published Python | 0.00523747 | 24 | −1.49936714 |
| Python with threshold floor added | 0.1 | 0 | −1.48287934 |

The change is **0.01648780** in this constructed example. On the peak-free power law both Python variants return −1.5. The [script](verification/hemispherotomy_spectral_translation_gate.py) validates the original file hash, performs this single-line controlled change in memory, and records the [receipt](verification/hemispherotomy_spectral_translation_gate.json). Dependencies are pinned in [requirements](verification/requirements-spectral-translation.txt). For example:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r verification/requirements-spectral-translation.txt
gh api 'repos/milecombo/spectralExponent/contents/compute_spectral_exponent.py?ref=4bd4929d3a052d1c7eb0a5fb73ff860c4e4ac421' --jq .content | base64 -d > /tmp/compute_spectral_exponent.py
python verification/hemispherotomy_spectral_translation_gate.py /tmp/compute_spectral_exponent.py
```

**Interpretation:** the synthetic comparison establishes potential nonequivalence, not the magnitude, direction, or existence of a discrepancy in real EEG. The floor-modified Python is not a verified MATLAB emulation, and we have not established which implementation generated the published results. No MATLAB interpreter was run; no patient PSDs, figure spreadsheets, slope classifications, significance tests or clinical conclusions were independently replayed. The study's delta-power evidence is separate from this slope-fitting issue. Meaningful follow-up requires the same real or realistic PSDs run through both unmodified implementations, verified settings and versions, plus assessment of the downstream within-patient contrasts. The published spreadsheets contain plotted features, not necessarily the raw PSDs needed for that test.

## 4. The decision gate: what would a finding actually decide?

| Candidate observation | Supports | Does not by itself establish |
|---|---|---|
| Preserved or separated resting BOLD patterns | Persistent organization and correlation at the measured scale | Experience, causal independence, or a subject per network |
| Strong EEG slowing relative to baseline | A changed local electrophysiological regime and, under supported calibration, evidence about experience-related states | Complete absence of experience; identicality to natural sleep |
| A response to a local perturbation | Responsiveness and measured dynamics, conditional on spatial specificity and safety | A report, a validated experience label, or subject number |
| Reliable report of content | Evidence for experience as reported, with time and memory qualifications | All unreported experience, exhaustive localizability, or another subject's absence |
| Separated physiological and behavioral processing | Limits on accessible interactions and possible causal factors | A unique rule for individuating subjects |

The last distinction matters to the project's **intrinsic experience** hypothesis. Even if experience is fundamental, it does not follow that every disconnected patch is a distinct subject, that no tissue lacking a behavioral outlet has experience, or that the larger whole itself is an agentive universal subject. Conversely, cortical slowing would not disprove an intrinsically experiential fundamental reality; a specific bridge from that reality to local experiences must first make testable claims.

A plausible minimal bridge must state separately: (i) its admissible substrate and interventions; (ii) what makes a localized process experiential at all; (iii) what makes experiences belong together to one subject; (iv) persistence and fission conditions; and (v) how observable reports and markers are generated, including error and nonresponse. It must apply consistently to surviving hemispheres, disconnected diseased cortex, callosotomy, and ordinary dreaming; its predictions cannot be chosen after looking at the result. No such bridge is supplied by the present findings.

## 5. Practical research path, not a clinical protocol

1. **Reproducibility first.** Confirm source versions and actual analysis pipeline; run both unmodified spectral implementations on common controlled PSDs and, with permission, the relevant original PSDs. Compare threshold decisions, feature values and the predeclared patient-level contrasts, not just one synthetic example. Obtain the released aggregate figures without treating them as raw EEG. Preregister tolerances and preserve the study's different spectral ranges and electrode aggregations.
2. **Same-participant physiology.** Where ethically feasible, acquire appropriately aligned awake fMRI and EEG in the same participants, with individualized anatomy, lesion masks, vascular and motion controls, and spatial leakage tests. Model the joint measurements rather than multiplying separate likelihood ratios as if EEG and BOLD were independent. Prespecify how selection by preserved tissue affects the population to which results apply. Demonstrating coexistence would resolve a physiological question, not the subjective one.
3. **Calibration with honest labels.** In independent, age-appropriate report-accessible cohorts, compare within-state dream reports and no-experience reports, include no-information outcomes, account for repeated measures by participant, and evaluate calibration and error with held-out participants. Reports are imperfect labels: minimize and model memory and timing error. Predefine alternatives for transfer from intact, responsive tissue to lesioned, deafferented tissue; test sensitivity to their failure. An accurate source-domain classifier alone does not validate its target-domain output.
4. **Perturbation only when justified.** A perturbational measure can add evidence about dynamics, but applying TMS or intracranial stimulation to epilepsy-prone patients has specific risks; [Bayne, Seth and Massimini](https://www.sciencedirect.com/science/article/pii/S0166223619302164) explicitly discuss such practical challenges. No procedure should be undertaken for this project without specialist risk assessment, appropriate consent and ethics approval. Where clinically indicated monitoring already exists, prospective data collection may be considered, without assuming a causal response is a consciousness assay.
5. **Competing constitution rules.** Before collecting results, specify alternatives that predict *different observable signatures* under the same interventions, including the causal leakage and task shortcuts audited in the [joint-access gate](JOINT_ACCESS_COMMON_SOURCE_DECISION_GATE.md). Specify when either result is inconclusive. Existing identifiability limits mean that physiology alone may remain compatible with competing subject assignments even after an improved measurement.

These are research design priorities, not treatment advice. No staged test above is a guaranteed resolution of phenomenal subject number. Broader physics, the timeless absolute and emergence of spacetime remain independent open obligations; this neuroscientific evidence does not solve them.

## Sources and limits

Primary sources: [Kliemann et al. 2019](https://doi.org/10.1016/j.celrep.2019.10.067); [Colombo et al. 2025](https://doi.org/10.1371/journal.pbio.3003060); [Bajwa et al. 2025](https://doi.org/10.1038/s41598-025-12695-z); [Bauer et al. 2026](https://doi.org/10.1093/braincomms/fcag211). The paper-linked [Zenodo materials](https://doi.org/10.5281/zenodo.16936516) and pinned [code](https://github.com/milecombo/spectralExponent/tree/4bd4929d3a052d1c7eb0a5fb73ff860c4e4ac421) support the code check, not a replay of private raw data. [Bayne et al. 2020](https://doi.org/10.1016/j.tins.2019.11.003) discusses islands and their measurement challenges.
