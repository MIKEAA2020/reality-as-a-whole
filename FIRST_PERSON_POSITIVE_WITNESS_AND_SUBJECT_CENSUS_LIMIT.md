# First-person positive evidence: a less demanding test, and its limit

## Decision and correction

The [previous three-candidate comparison](SUBJECT_CONSTITUTION_THREE_CANDIDATES_CRITICAL_TEST.md) made the problem harder than necessary when it said to stop if no defensible **negative calibration** can be supplied. That is too strong for a one-sided question. To challenge a candidate that says a specified joint experience **never occurs**, a sufficiently well-supported **positive** first-person witness can be enough. We do not also need a validated false-negative rate or complete access to every possible subject.

This does **not** make the test easy. The positive judgment must refer to the target experience in the right window; communication and interpretation must be credible; and the reporting experiencer must actually fall within the domain the candidate claims to cover. For an external statistical conclusion, a relevant upper bound on *false positive reports about that reporter's experience* must be justified, rather than invented. Such a bound may itself require evidence about cases where that particular reporter does not have the target experience. The point is that we need not calibrate **absence across all conceivable subjects**, nor establish sensitivity, to use positive evidence against a no-occurrence prediction.

Equally important: even perfect access to one reporter's actual experience need not reveal additional private subjects. A positive witness can therefore challenge the specified local-only package L, but cannot decide maximal M versus private-nested N, which both allow the same global reporting field. The new result is an asymmetric evidential strategy and a correction to the proposed stop condition, not a new empirical discovery or a solution to subject constitution.

## 1. Which proposition can a person witness?

Fix a particular reporter `r`, a short target window `w`, and two carefully described content-types `A` and `B`. Define:

- `E_r=1`: the reporter actually experiences A and B **together in that window**. This is about experience, not simply whether the stimuli occurred or can later be compared. `E_r=0` means this specified conjunction is absent for this reporter, not absence of all experience.
- `Q=1`: at least one subject in the candidate's **specified population** experiences A and B together in the window.
- `Y=1`: a recorded, affirmative report about that same conjunction under an agreed interpretation; all other responses, including uncertainty and nonresponse, are **not positive reports**, not declarations of `E_r=0`.

If the reporting experiencer is within the candidate's population, `E_r=1` logically entails `Q=1`. This coverage condition is essential: if the candidate describes only two local fields but the reporter might be an additional, unmodeled field, it cannot claim `Q=0` for the larger population without a separate exclusion assumption. One does not need to identify the reporter with a particular anatomical support just to take the report seriously; one does need to show why the theory's asserted no-conjunction domain covers that report.

A first-person judgment is substantive evidence, especially for the person having the experience. It is not merely a behavioral output to be dismissed whenever a preferred model disagrees. At the same time, a third-party record can be affected by task interpretation, timing, memory, communication and error. Neither automatic infallibility nor automatic skepticism is warranted. The proposition is deliberately narrower than “I am one person” or “I see on both sides.” Such broader statements remain important evidence of lived experience but need not assert the precise simultaneity and content specified by `E_r`.

In the earlier toy's coupled condition, L plus its stipulated content and population-closure assumptions asserts `Q=0`, while M and N assert `Q=1`. An independently warranted instance of `E_r=1`, in a case to which the full L package actually applies, contradicts that package. It does not tell us which of its boundary, content, timing, coverage or other premises was wrong; and the toy has not been mapped onto a real person or brain.

## 2. A positive report gives a one-sided bound

For a defined population of comparable windows, let `p=P(E_r=1)`, `q=P(Y=1)`. Suppose a target-specific false-positive bound is independently defensible:

```text
P(Y=1 | E_r=0) ≤ α,   0 ≤ α < 1.
```

Equivalently use the joint-probability inequality `P(Y=1,E_r=0) ≤ α P(E_r=0)` when `P(E_r=0)=0`. No false-negative bound, sensitivity estimate or error independence is required. Since `P(Y=1,E_r=1) ≤ p`,

```text
q ≤ p + α(1−p),     so     p ≥ max(0, (q−α)/(1−α)).
```

By reporter inclusion, `P(Q=1) ≥ p`. Thus an exact population rate `q>α` excludes a package with `Q=0` throughout that population, conditional on the error, inclusion, population and target assumptions. It is possible to have additional Q-positive cases outside the reporter, so this says nothing about an upper bound on the number of subjects. With only this one-sided calibration, even `q=0` cannot rule out `p=1`: every positive experience could be unreported.

The bound is **sharp** for the stated information. For `q≥α`, put `p=(q−α)/(1−α)`, set sensitivity to one and false-positive rate to α; this attains the observed q. For `q<α`, take `p=0` and false-positive rate q. Conversely, `p=1` can produce any q if no sensitivity lower bound is imposed. For invented `q=0.7`, `α=0.1`, the lower bound is `p≥2/3`. These are population quantities in a hypothetical example, not observed frequencies, confidence intervals or a claim that α=0.1 has been calibrated.

Unlike the earlier two-sided illustrative assay, a positive conclusion does not require us to establish that *all negative observations* correctly mean no experience. Nor does it rely on a subjective report being an oracle: the assumed false-positive bound is exactly the point where task, communication and experiential interpretation must be justified. If q and α are estimated, use a **simultaneous lower confidence limit** for q and upper limit for α, with separate uncertainty budgets for sampling and calibration. The formula does not turn unsupported assumptions into data.

## 3. Repetition is not a substitute for calibration or independence

In the earlier hypothetical assay, `n=30` and a positive decision required `K≥16` reports. Under L's target-domain null, assume each trial's marginal chance of an erroneously positive report is at most `α=0.1`. If errors are independent, the binomial upper tail is approximately `3.66×10⁻⁹`, as previously computed. **But marginal bounds alone do not imply independence.**

Without any independence assumption, Markov's inequality gives the sharp bound

```text
P(K ≥ 16) ≤ min(1, nα/16) = 3/16 = 18.75%.
```

This is attainable: with probability `3/16`, choose exactly 16 of the 30 trials uniformly to have positive reports; otherwise none are positive. Every individual trial has marginal positive probability `(3/16)(16/30)=0.1`, yet the decision error is `3/16`. That is a mathematical worst case, not evidence that actual participants have this error pattern. Under merely marginal bounds, making this bound no more than 5% for that threshold would require `α≤2/75≈2.67%`; there is no established reason to assume such an error rate here.

A binomial bound can also be justified by the **stronger per-trial conditional** requirement that the error probability remain at most α given the whole previous observable history, even with adaptive dependence. An average per-trial error rate or repeated agreement does not by itself establish that condition. The analytic threshold, trials, denominator, missingness, stopping and calibration uncertainty must all be set in advance; repeated trials within one person are not independent participants. The prior interface's [dependence control](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) made the same general warning; this calculation gives the exact worst case for this particular 30-trial one-sided decision.

## 4. What current first-person evidence actually contributes

The project's [Pinto 2017 supplement audit](PINTO_2017_SUPPLEMENT_FIRST_PERSON_AND_METHODS_AUDIT.md) records that DDC reported seeing well on both sides, while DDV reported blurred peripheral vision; their bodily and control reports also differed. These are meaningful first-person accounts and should be preserved as such. They were not established as answers to the proposed same-window A-and-B conjunction question, and the supplement's questions were not tied to the individual brief visual trials. The [2023 DDC audit](SPLIT_BRAIN_PRIVATE_SUBJECT_IDENTITY_EVIDENCE_AUDIT.md) reports that his confidence concerned a same/different judgment, not explicitly whether both details were experienced together. Confidence and performance are not interchangeable with this precise target.

Accordingly, existing reports are **not** here recoded into positive or negative `E_r` trials, nor used to estimate q or α. They give reason to take the participant's communicated experience seriously and to avoid simplistic disconnection stories. They do not establish the toy's biological implementation, eliminate other subjects or identify a target-specific error rate. This note relies on those earlier source audits; it does not newly access raw data or conduct a clinical study. The later [real-case application](REAL_CASE_WITNESS_AND_MAXIMAL_RULE_BOUNDARY_TEST.md) spells out which stronger, ordinary-viewing no-experience claim DDC's report does challenge and which trial-specific claim remains untested.

## 5. An ethical positive-witness design to evaluate—not a ready assay

A feasible first step, if later developed by qualified investigators and appropriate ethics review, would be **noninvasive** and initially use consenting adults able to describe their own experiences. It is an operational design question, not a claim that these instructions achieve calibration:

1. **Predefine the personal target.** With participant input, distinguish “I experienced two specified features together during the display” from “the features were physically simultaneous,” “I remember both,” “I inferred the answer,” and “I can compare them afterward.” Specify which feature-types and window count, and preserve an explicit uncertain/unable-to-answer option. Avoid requiring agreement with an investigator's theory of subjects.
2. **Separate judgments from accuracy.** Randomize and blind the feature values and stimulus timing where appropriate; obtain a conjunction judgment and then a separate feature report. Compare simultaneous, sequential and delayed-cue controls; record timing, gaze and missingness. Correct feature reports help constrain guessing and access, but can result from serial processing or memory and **do not certify** simultaneous experience. Physical sequential controls are not automatically experiential-negative controls: persistence, imagery or memory can themselves be co-present.
3. **Seek target-relevant evidence for false positives.** Use independent within-person introspective judgments where meaningful, comprehension and timing checks, responses elicited before accuracy feedback or revealing the hidden stimulus values, and controls for post-cue reconstruction. Examine disagreements, rather than declaring a physical stimulus to be experiential ground truth. These steps may strengthen or weaken confidence in a report, but no numerical bound follows automatically. Report what the participant can genuinely judge and what remains uncheckable; agreement among proxies alone is insufficient.
4. **Fix a real candidate application.** A human study can test a specified L-like claim only after the theory maps actual conditions into its domain and says which experiential conjunction is impossible. Define that mapping and counterpredictions before outcomes, and compare nonexclusive alternatives including a single partially unified subject, local processing plus later reconstruction, and a global field. Controls may rule out some operational mechanisms without settling the ontology.
5. **Use a one-sided decision only when justified.** For positive rejection, prespecify an α bound for the reporter's target, include its uncertainty, justify the sampling/dependence model, and require the rate or individual witness to exceed that bound under the relevant null. Without a defensible bound, communicate a qualitative evidential judgment with its reasons and limitations—not a fabricated p-value. A decisive observed contradiction challenges the full package; it does not automatically choose M or N.

Applying anything like this to existing clinical participants would need patient-specific anatomy and abilities, clinically led ethics and consent, a defensible mapping and safeguards against fatigue and distress. It would not justify surgery or invasive procedures for research. This sketch is neither a preregistered protocol nor a recruitment or medical recommendation.

## 6. Why even a perfect positive anchor does not count subjects

Consider two completed versions of the coupled toy, stipulated to have the **same physical dynamics and the very same global reporting field with the same full first-person experience and correct reports**. In M that is the only designated field. In N it is accompanied by two additional private local fields, with their own occurrences; assume those fields add no separate accessible record in the stipulated physical sector. Both contain the reporter's genuine joint A-and-B experience. One has one designated subject and the other three.

Under the stipulated equivalence, every observation confined to the shared physical records and that reporter's first-person experience agrees, even if that experience could be communicated perfectly and even across all allowed physical interventions. This does not make the extra fields real or prove they are metaphysically possible. It shows that **a full positive account of one subject is not, by itself, a complete census**. N's additional fields could be excluded only by a justified exclusivity principle, access or identity evidence about those fields, or a separately specified physical consequence on which the complete theories differ. Lack of their report is not sufficient. Conversely, their mere formal stipulation does not establish their existence.

This is also why the positive-witness improvement does not solve qualitative grounding. Even a correct identification of co-presence does not by itself explain why a particular color or affect has its felt character, how its occurrence is individuated, or why the ground exists. The challenge to L is a targeted test of a **completed** candidate, not derivation of the project's experiential constitution rule.

## 7. What changed and what remains

The earlier plan's requirement of a negative calibration is withdrawn **for positive rejection of a universal no-conjunction claim**. For demonstrating absence, estimating full prevalence, validating both directions of an assay, or excluding unreporting subjects, additional sensitivity/coverage and possibly negative evidence remain necessary. The main remaining practical blocker for the positive strategy is a justified target-specific false-positive bound or credible individual witness **plus** a non-arbitrary mapping from a real case to a sufficiently specific candidate.

The work therefore establishes a real improvement in the evidential route, not an achieved major theory advance. Without that bridge, a clinical analogue, or a meaningful confrontation with data, more arithmetic examples would be diminishing returns. The next decisive work is to formulate a concrete candidate's mapping and seek an independently defensible positive-witness procedure, or to show why that cannot be done; there is no basis yet for claiming the central problem solved.

## Reproduction

`python verification/positive_experience_witness_gate.py` reproduces the [exact-arithmetic receipt](verification/positive_experience_witness_gate.json); `python -m unittest discover -s verification -p 'positive_experience_witness_gate_test.py'` checks the population bound on a rational grid, attaining constructions, the dependence witness, tail arithmetic and validation. The sharp continuous bounds follow from the arguments in sections 2–3, not from the grid. No actual experiential observations, error bounds or subject assignments are supplied by the code.
