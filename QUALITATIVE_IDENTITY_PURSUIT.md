# Pursuing a warranted qualitative identity
## Frozen target, empirical source screening, and reference-sensitive inference

## 1. Target and present outcome

The current pursuit selects **a bounded visual-content identity**, not a universal theory of redness and not subject counting. A first target is a face-versus-object perceptual-content contrast in a suitable rivalry paradigm, conditional on independently warranted experience of those contents. This is a coarse qualitative-content distinction, not the full intrinsic character of either experience.

**H_Q1:** within a declared domain, the difference between the anchored A and B visual-content occurrences is the intrinsic difference between two independently specified, realized content-maintaining organizations P_A and P_B. The experiences are those actual organizations, not extra observers or meanings attached to decoded symbols.

This is a narrow identity conjecture within [necessary articulated unity](NECESSARY_ARTICULATED_UNITY.md). The proposed recurrent-maintenance mechanisms remain candidates; neither recurrence nor a fitted latent coordinate supplies the identity by itself.

**Present outcome:** no warranted physical–phenomenal identity has yet been obtained. This report makes the target and rival explanations explicit, screens an actual empirical route, and demonstrates a specific obstacle to inferring qualitative identity from latent neural dynamics. It also shows exactly what independently warranted qualitative anchors could resolve—and what they would still leave open.

## 2. Why this target, rather than immediately selecting a subject boundary

Rivalry offers a potential contrast between changing perceptual content and approximately matched sensory input. Actual control of input, gaze, adaptation, attention, task, and report must be established in the chosen experiment; the generic paradigm is not an intervention on only experience.

A coarse content contrast is narrower than determining whether two contents belong to one subject. It can constrain chi without pretending to identify all Gamma, episode duration, or absolute qualitative character. A neural state that predicts a report may reflect the experience, a consequence, a preparation for reporting, or another correlated process.

At least three explanations must be compared:

- **Intrinsic maintenance:** a nominated actual organization constitutes the anchored content.
- **Stimulus/input encoding:** the measurement primarily tracks input or sensory fluctuations rather than the disputed perceptual distinction.
- **Monitoring/report:** the measurement tracks a downstream classification or report process rather than the occurrence's constitution.

These are not exhaustive theories. Their domains, interventions, and predictions must be fixed before interpretation; a generic decoder score does not decide them.

## 3. Actual source screening and its result

A GitHub repository search for binocular-rivalry data located exploratory analysis resources. The inspected [engellab/2D-Langevin-rotation README](https://github.com/engellab/2D-Langevin-rotation/blob/a2a03cc0585cdc445f07062e30bced8338e6a4e0/README.md), pinned at `a2a03cc0585cdc445f07062e30bced8338e6a4e0`, describes latent dynamical inference using neural firing data, alternative neuron selections, and face/object stimulus trials.

Its own caveats include dependence on neuron selection, changes in inferred dynamics when learning force and firing functions jointly, uncertainty about some trial labels, and comparison between posterior transitions and face/object representations as a future direction. These statements are evidence about the exploratory analysis's stated status, not verified findings about experience.

A [README snapshot](sources/external/rivalry_identity_screen/README.upstream.md) and [provenance](sources/external/rivalry_identity_screen/provenance.json) are retained. Coverage is **README only**: code, images, recordings, subject/species metadata, original article, consent/access conditions, and trial labels were not assessed. No recording was downloaded or analyzed. No source model was executed.

A second search result, `Davidson-MJ/BinocularRivalry_Coherency`, had a tree containing only `Coh_Onetrial.m` at `0d7f6dc1e2591106fbf5767bb1b15c218f638df2`; no README was available through the queried endpoint. The script itself was not read or run, and no empirical result is inferred from its title.

**Screening decision:** neither resource as inspected establishes independently anchored qualitative identity, admissible subject-incidence evidence, or the intervention needed for H_Q1. The first is a possible modeling lead, not a warranted neural basis for A/B. This negative screening result prevents presenting an attractive inferred geometry as an already validated quality map.

## 4. Particular identity cannot be read from unanchored latent coordinates

Consider a two-state hidden Markov model for a measured binary signal. With initial probabilities pi, transition matrix T, and emission probabilities B, an observed sequence y has likelihood

    L(y) = sum over hidden paths h of
           pi(h_1) B(h_1,y_1) product_t T(h_t,h_(t+1)) B(h_(t+1),y_(t+1)).

Let g exchange the two hidden-state names and transport pi, T, and B accordingly. Each hidden path corresponds bijectively to its renamed path with the same term in the sum. Therefore every observed-sequence likelihood is unchanged, at every length.

This is a standard hidden-state label invariance, applied here as a reference audit, not claimed as a new statistical discovery. It proves a **re-presentation invariance**, not that there are two different qualitative realities. Counting the two parameterizations as two experiences would duplicate notation. The finite check verifies an illustrative implementation; the path-bijection proof supplies the all-length result.

But a further claim—that state 0 is anchored experience A rather than B—requires evidence or an identity argument outside the bare index convention. If A and B are independently fixed, swapping their assignment while retaining the same physical model is a substantive candidate change. Data that concern only the unanchored measured sequence do not establish which assignment is correct.

The same discipline applies to a fitted continuous latent geometry: coordinate shape and physical or phenomenal reference must be separated. This report proves the finite permutation case; it does not claim that every geometric feature of every latent model is gauge or that an arbitrary coordinate transformation preserves a model's stated constraints.

## 5. What calibrated anchors can contribute

Suppose an independently justified assay reports anchored content A. For the intervention and domain of interest, let

    Pr(report A | experience A) >= 1-beta,
    Pr(report A | experience B) <= alpha,
    alpha+beta < 1.

These assumptions concern the two nominated alternatives, not consciousness in general or every mixed percept. They require independent warrant for what A/B mean and for assay reliability/transport under intervention. Mixed or unclassifiable cases must be handled explicitly in a real study.

If the probabilities of reporting A conditional on the independently selected physical organizations fall into the respective disjoint bands, this can select a correspondence within the declared binary candidate class, provided its mapping and evidence assumptions hold. It does not by itself establish constitution, exclude every causal confound, or derive why the quality is what it is.

The [exact check](verification/qualitative_anchor_check.py) illustrates this with supplied probabilities 9/10 and 1/10 and error bounds 1/5. One anchored mapping survives; after a pure latent-state renaming, the mapping transports accordingly. With no informative error bounds both anchored assignments remain compatible. These numbers are **not empirical calibrations**.

The result respects the earlier [observation-identifiability analysis](DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md). A reliable baseline does not establish reliability under an access-disrupting intervention, and neural prediction of the report is not an independent calibration of the report's phenomenal reference. Multiple channels cannot be multiplied as independent evidence without modeling their common causes.

## 6. From correspondence toward identity: the warrant ladder

A warranted identity requires more than a uniquely fitting decoder:

| Obligation | Required advance | Current status |
|---|---|---|
| Qualitative reference | Independently fixed A/B experiential contrast with limitations and mixed cases stated | Proposed target; no new phenomenological observations |
| Physical individuation | P_A/P_B selected by actual state, dynamics, localization, and interventions, not chosen merely to maximize fit to A/B labels | Not supplied by the screened README |
| Robust correspondence | Held-out prediction with input, report, attention, history, and measurement confounds addressed | No participant/model analysis performed here |
| Causal discrimination | Target changes or persists under interventions that separate maintaining organization from input encoding and downstream monitoring | Evidence and preservation premises open |
| Identity argument | Explain why the qualitative contrast is intrinsic to this concrete occurrence rather than an additional matched property | Preferred common-constitution direction; argument incomplete |
| Whole-account closure | Explain the nature's actuality, scope, and necessity without an independent selector | Governing objective, not a result of the finite HMM audit |

Even successful causal prediction may establish a useful physical correlate or determinant rather than numerical identity. Such progress would still matter; it must be named accurately. Non-additive efficacy can motivate identity or constitution without choosing between every remaining account.

## 7. Predeclared next empirical decision

Before accepting a dataset as evidence for H_Q1, obtain and inspect primary protocol and provenance establishing:

1. whether subjects' content reports or other judgments are actually available and time-aligned, rather than stimulus labels being called percept labels;
2. what is recorded and what sensory/task/report conditions change;
3. whether raw or sufficiently documented processed observations are accessible under applicable terms;
4. how transition timing, mixed percepts, delayed reports, missing trials, and source-specific confounds are handled;
5. whether an intervention distinguishes the proposed physical basis from monitoring, and what warrants transport of the evidence relation.

A dataset lacking the last item may support a correspondence study but not the stronger intervention-dependent identity claim. A study lacking direct subject-incidence evidence must not be promoted to a test of Gamma merely because it concerns consciousness.

For model fitting, predeclare a physical region/feature selection rule and hold out conditions or interventions, not only randomly interleaved samples with shared temporal history. Record stability to neuron selection and jointly learned observation functions; a changed latent coordinate is not automatically a changed experience. No fit is reported in this update.

## 8. Executable checks and bounds of the result

Run:

    python verification/qualitative_anchor_check.py

[Retained results](verification/qualitative_anchor_check.json) verify 510 observed sequences across lengths 1–8 in an exact illustrative two-state model, normalization, state-renaming invariance, and conditional transport of a calibrated qualitative assignment. The script assigns no experience to a real physical system, supplies no neural data, and selects no subject boundary. These are supplemental mathematical checks, not additions to the core research-suite total.

**Actual advance:** the candidate now has a specific empirical route, screened source provenance, a reference/gauge test, and an explicit distinction between selecting an anchored correspondence and warranting identity. An unanchored inferred neural state or latent geometry cannot serve as the particular qualitative identity merely because its dynamics look organized.

**Remaining bottleneck:** independent experiential anchors and a physically discriminating intervention in a declared real domain. No warranted Gamma–chi law has been discovered in this update. The next move is primary-evidence qualification and bounded causal analysis, not another free assignment of experiential labels to a synthetic process.
