# Would consciousness-triggered collapse be experimentally identifiable?

## Decision

A hypothesis in which an experience produces partial quantum collapse can be given a testable physical form. **But in the simple model tested here, one observed interference experiment cannot separate experience-triggered collapse from ordinary dephasing**. Even complete process tomography on the specified accessible quantum system cannot separate them if both mechanisms implement the same channel in the same unobserved interval. Further, knowing their combined effect does not by itself separate the frequency of the proposed experiential event from its collapse strength.

This is a structural identification result for a **declared toy model**, not evidence that consciousness collapses anything, a proof that all consciousness-collapse theories are untestable, or an inference about the consciousness of the memory qubit. Our subject-first framework does not entail collapse; this is one candidate route being tested against its competitors.

## Relation to established work

Consciousness-triggered collapse is not a new proposal. [Chalmers and McQueen](https://arxiv.org/abs/2105.02314) combine an integrated-information proposal with collapse dynamics, discuss the quantum-Zeno problem for simple versions, and propose possible quantum-computing tests. [McQueen, Durham and Müller (2026)](https://doi.org/10.3390/e28040394) analyze a feedback-dyad proposal and constraints on collapse models designed to track differences in rich conscious states. Those are **specific theoretical proposals**, not evidence that IIT is correct or that their simple circuits are conscious.

Our calculation is a deliberately simpler, single-slot channel and an exact identifiability check tied to the [previous temporary-record gate](TEMPORARY_SUBJECT_RECORD_HISTORY_GATE.md). It is not their full model, CSL, a new collapse mechanism, or a derivation from experience. The general difficulty of separating noise and a physically equivalent process is established channel-identification logic; no general originality claim is made.

## 1. An explicitly declared candidate

Retain the friend-memory qubit `M` and the fixed Alice–Bob measurements from the previous gate. At a specified intermediate point, postulate the following hypothetical mechanism:

- A candidate subject-event occurs with probability `s`, independently of the quantum alternatives and background noise **in this toy model**. No rule for determining a real subject or `s` is supplied.
- If it occurs, an unread `Z_M`-basis collapse is applied with probability `p`; otherwise nothing happens. Its ensemble action is the standard dephasing channel

  `Λ_p(ρ) = (1−p)ρ + p Δ_Z(ρ)`, with `Δ_Z(ρ)=(ρ+Z_MρZ_M)/2`.

- Independently, an ordinary unobserved background acts by `Λ_q` in the same basis and time slot, where `q` is unknown.

This is an unconditional ensemble description; it does not give a detailed single-experience ontology, a relativistic collapse law, an algorithm for finding a subject or an experimentally justified value for any parameter. In particular, an “event” here is a stipulated random trigger, not a claim that a qubit is conscious. The actual mental state in an interacting superposition might not be represented by this basis or by a single independent trigger. Other collapse and environmental dynamics need not satisfy these assumptions.

The probability-`s` mixture applies `Λ_{sp}` to the observable system. Composition gives the exact channel identity

`Λ_q ∘ Λ_{sp} = Λ_t`, where `t = q + sp − qsp`,

and the off-diagonal coherence retention is

`κ = (1−q)(1−sp)`.

Populations in this chosen basis are unchanged. At all times outside the declared slot, all scenarios below use the same physical operations.

## 2. Three different stories, one accessible channel

All three choices yield **exactly** `Λ_{1/4}` and `κ=3/4` on `M`, including its action on states entangled with an accessible reference:

| Model | Event probability `s` | Trigger strength `p` | Ordinary dephasing `q` |
|---|---:|---:|---:|
| A | 1 | 1/6 | 1/10 |
| B | 1/2 | 1/3 | 1/10 |
| C | 0 | irrelevant | 1/4 |

For our fixed circuit, all three predict the same `S=(6+8κ)/5=12/5=2.4`. A and B have the **same calibrated background** but different event probabilities and trigger strengths. C has no event-triggered effect and a different background.

The equality is stronger than equality of one CHSH score. The verifier checks the channels on all four matrix units. By linearity this implies equality of the channel on arbitrary system states and on systems entangled with any untouched accessible reference. Consequently, **no tomography or other protocol that sees only that same input–output slot** can tell the three stories apart. This conclusion is conditional on having the same channel at that slot. It does not exclude distinguishing other models using access to environmental degrees of freedom, interventions during the slot, temporal correlations, additional predicted signatures, or separately justified calibration. Different mechanisms can have different environmental dilations and multi-time predictions; the equality of one reduced channel does not make them universally indistinguishable.

Moreover, if two metaphysical interpretations assign experience versus a purely physical correlate to the **same complete operational dynamics**, those operational predictions alone do not decide the metaphysical attribution. That is a separate interpretive limitation, not a claim that experience is unreal or causally impotent.

## 3. What an interference measurement can bound

Suppose the declared model is valid, `κ≥0` has been determined with phase calibration, and `0≤q≤1`. Even without a detailed background calibration,

`sp ≤ 1−κ`,

because `(1−q)≤1`. Thus sufficiently high retained coherence can **upper-bound the effective trigger `sp`** in this particular model. If the subject-event is independently known to occur with certainty (`s=1`), this also upper-bounds `p`. If no positive lower bound on `s` is available, a small `sp` does not by itself place a useful upper bound on `p`: the trigger could be strong but rare. The comparison is model-specific; additional effects that restore coherence, unmodeled dynamics or a different collapse basis invalidate the simple relation.

An observed *loss* of coherence does not by itself imply an experience-triggered effect: for every `0≤e≤1−κ` with `e<1`, taking `sp=e` and `q=(1−κ−e)/(1−e)` gives the same channel. At the endpoint `κ=0, e=1`, any `q` gives zero retention. If `κ=3/4`, the entire range `0≤sp≤1/4` is compatible with the same observed channel when `q` is unconstrained. This range includes `sp=0`.

### Illustrative calibration, not real data

Suppose an independently justified analysis bounds the ordinary **retention** `r₀=1−q` to `[0.88,0.92]`, and a simultaneous or appropriately combined confidence procedure bounds `κ` to `[0.74,0.76]`. Assuming both bounds and the model are valid in the target condition, `r₀>0` and

`sp=1−κ/r₀ ∈ [3/22, 9/46] ≈ [0.136,0.196]`.

If `s=1`, the same interval applies to `p`. If independent evidence yields `1/2≤s≤1`, the possible `p` values are `[3/22, 9/23] ≈ [0.136,0.391]`. With no positive lower bound on `s`, the upper endpoint can be 1. **These numbers are constructed examples, not measured confidence intervals or consciousness estimates.** The bounds must be jointly valid at a declared coverage level, and their derivation assumes the intervals cover the relevant counterfactual background, not just a convenient control condition.

The important experimental burden is the background `r₀` **in the target condition absent the putative collapse**. A separate control may differ in gates, heat, environment or information processing. It cannot be assumed exchangeable just because it behaves similarly. Nor can a purported conscious and nonconscious pair be assumed physically identical while a fixed supervenience rule assigns them different phenomenal states.

## 4. A preregistered discriminating program

A useful comparison would need all of the following, before looking at the target outcomes:

1. **Selector and dynamics:** specify the candidate subject, physical event, basis or operators, collapse strength/rate, and which states receive which dynamics. Demonstrate why the candidate selector applies; neither language-like behavior nor a qubit record automatically establishes experience.
2. **Operational contrast:** nominate implementable target and controls, predicted channels and timings, primary estimand, and assumptions under which a physically meaningful difference in the proposed conscious structure is not merely a different noise source. This does not require or claim two physically identical states with different consciousness.
3. **Independent noise budget:** constrain background decoherence, calibration drift, control work, leakage and other predicted processes in the target condition; include uncertainty and possible interactions. If this cannot be done, report the partial identification set rather than attributing the residual to experience.
4. **Phenomenology/subject calibration:** specify how event prevalence or relevant phenomenal distinctions could be independently assessed and with what errors. Existing assays do not validate consciousness in the toy circuit; if the selector is uncertain, `s` and `p` are not separately identified.
5. **Quantum outcome:** compare a preregistered collapse model with a background-only or standard-quantum model. An unexplained physical residual would challenge the fitted background model; it would not by itself prove an experiential cause. A null result could constrain that particular model's parameters under the established assumptions, not refute experiential monism in general.
6. **Feasibility and ethics:** assess reversible control, isolation, timing, real-time settings and ethical treatment before proposing tests with any potentially sentient system. The small-circuit calculations here supply no such demonstration.

Operational locality, relativistic compatibility, energy changes, and the effect of repeated collapse on dynamics remain additional obligations for a viable physical theory. This one-slot calculation supplies none of them. Nor does it explain unpleasantness, derive a subject selector, provide a fundamental clock, or establish the user's zero-residue target.

## 5. Verification

Run [`verification/experience_collapse_identifiability.py`](verification/experience_collapse_identifiability.py). It checks channel composition on matrix units for 121 strength pairs, 121 trigger/prevalence pairs, all three identical-channel examples, 101 noise/trigger decompositions of the same channel, and the stated exact rational interval endpoints. The proof of channel equivalence is the displayed algebra; finite tests do not establish any unmodeled system's consciousness or environmental noise.
