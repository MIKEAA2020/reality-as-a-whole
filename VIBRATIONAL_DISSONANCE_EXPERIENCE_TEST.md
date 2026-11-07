# Vibrational dissonance and discomfort: a precise first test

## Result

**String-theory follow-up:** The [duality/subject-selection audit](STRING_DUALITY_SUBJECT_SELECTION.md) tests whether an experiential rule remains consistent under T-dual descriptions. It does not derive this effective oscillator model from quantum strings.

The user's proposal can be sharpened without assuming that all differences in frequency or phase are unpleasant. A **frustrated vibrational network** is one in which the interaction-preferred relationships of its components cannot all be satisfied together. That provides a physically interpretable candidate for “fundamental dissonance.” It does **not**, by itself, show that such a system feels discomfort, or that brain oscillations are fundamental strings.

The distinction matters because a network can be stably phase-locked and still have unavoidable frustration; conversely, a system can have the same observed phases without frustration if its interactions are different. We therefore need **interactions and their preferred relationships**, not simply a synchrony or frequency score. There is an additional problem: a fixed network's minimum frustration is constant as its state changes, so that number alone cannot explain changing discomfort unless the network parameters or boundary also change. State-dependent mismatch is a separate candidate.

The mathematics of phase frustration, 120-degree triangular order, and related neuroscience models is **known**, not a new physics discovery. In particular, [Le (2026), an arXiv preprint](https://arxiv.org/abs/2606.02512), explicitly studies the same antiphase triangle as a model of frustrated neural timing. The contribution here is the careful application to the user's experiential hypothesis, together with its identification and empirical gate audit.

## 1. Three candidate meanings of “misalignment”

Take a *finite classical effective model* of coupled phase variables. The phases are relative dynamical variables; they need not all be equal for the system to be coordinated. This is not a derivation from microscopic string theory.

For each physical or effective interaction `i–j`, choose an orientation once and suppose an independently specified preferred phase difference `a_ij`, coupling strength `k_ij ≥ 0`, and instantaneous phases `φ_i, φ_j`. Reversing the edge changes `a_ij` to `−a_ij` modulo `2π`. A common reciprocal potential model uses the nonnegative mismatch cost

```text
E(φ) = Σ_(i,j) k_ij [1 − cos(φ_i − φ_j − a_ij)].
```

Three distinct possible physical correlates are:

1. **Structural frustration:** `F = min_φ E(φ)`. This is the residual mismatch even after optimizing phase configuration. It is a property of the fixed interaction graph and parameters, not of a particular episode's current phase alone.
2. **State excess:** `D = E(φ) − F`. This is additional mismatch in the current state above the best configuration for that fixed graph. It can vary as phases change.
3. **Relaxational dissipation:** for the special model `dφ_i/dt = −γ ∂E/∂φ_i`, with `γ > 0`, the decrease rate `P = −dE/dt = γ Σ_i (∂E/∂φ_i)²`. This is a mathematical loss rate in that gradient-flow model, not automatically physical heat, bodily friction or real nervous-system power consumption.

These scores need not agree. A candidate experiential rule must say which, what physical system and timescale, and what else determines a subject. Equating any of them with unpleasantness is an additional conjecture. A fixed nonzero F permits a stable state and zero P; persistent structural incompatibility is **not** automatically an ongoing dissipative force.

The proposed cost assumes pairwise interactions of the stated symmetric, single-harmonic form and meaningful phases at a common scale. Real nervous systems may involve asymmetric couplings, common input, delays, changing amplitudes, noise, multiple frequencies and non-gradient dynamics. For cross-frequency resonance a candidate relation might involve `nφ_i − mφ_j`, and the simple cycle rule below then need not apply unchanged. The mere existence of different frequencies is not evidence of the stipulated energy or unpleasantness.

## 2. Known example: a triangle that cannot align all three relationships

Let three components form a triangle and let every pair favor **opposite phase**: `a_ij = π` and `k_ij = k > 0`. If the first is opposite the second and the second opposite the third, the first and third align, contradicting their opposite-phase preference. The cycle's preferred differences add to π modulo `2π`, not zero, so all three cannot be met simultaneously.

The known optimum spaces phases at `0, 2π/3, 4π/3`. Each pair compromises; the minimum cost is

```text
F = 3k/2 > 0.
```

The elementary identity behind this result is `E/k = (3 + |Σ_j exp(iφ_j)|²)/2`, whose lower bound is saturated by that configuration. Under the stated gradient dynamics, the gradient at the minimum vanishes and `P=0`, despite `F>0`. If the oscillators share a common natural frequency, the phase-locked pattern may rotate together while retaining the same relative configuration; one can analyze it in a co-rotating effective frame.

Compare this with the **same actual phases** but preferred directed offsets `−2π/3` on each edge. Their sum is `−2π`, equivalent to zero; all three relationships are satisfied and `E=F=0`. In both cases the ordinary global coherence magnitude `R = |Σ_j exp(iφ_j)|/3` is zero. So the same phase pattern and the same R can correspond to either frustrated or unfrustrated interactions. This is not evidence of two actual brain states; it is a counterexample to inferring incompatibility from phase pattern or low global synchrony alone.

For a general finite connected graph in this particular model, **all** edge constraints can be simultaneously satisfied iff the oriented sum of preferred offsets is zero modulo `2π` around every cycle. Tree edges alone impose no such closed-loop obstruction. The condition follows by adding relations around a cycle and, conversely, assigning phases along a spanning tree. A change of local phase convention `φ_i → φ_i + θ_i` accompanied by `a_ij → a_ij + θ_i − θ_j` leaves every mismatch and cycle sum unchanged. This mathematical phase-reference invariance is not a claim that all changes of physical phase are unobservable.

The [verifier](verification/phase_frustration_audit.py) checks the triangle and 2,000 phase-reference changes numerically, and exhaustively checks 1,728 discrete triangle offset assignments; 144 are compatible. It confirms a model calculation, not a new phase theory, a prediction about people, or a phenomenal identity.

## 3. What follows for the user's identity idea?

A properly scoped hypothesis might be:

> For a specified subject and regulatory context, some independently identifiable mismatch organization in that subject's relevant coupled dynamics is the unpleasant aspect of experience.

This is an **identity conjecture**, not necessarily an extra process converting physical oscillations into feelings. It still needs to say whether the candidate is F, D, P, an interaction of these, or a different physical invariant altogether. These are different theories, and fitting a flexible function after seeing ratings is not a decisive test.

For example, a deliberately strong trial-level rule `U = g(F)` with fixed parameters and a fixed subject would predict the same unpleasantness U across all phase configurations. Ordinary varying experience can be accommodated only by changing the independently measured interaction parameters/boundary, adding state variables, or narrowing the domain—not by silently redefining F. Conversely `U = g(E)` could vary with state, but would treat every equal E as equally unpleasant in its declared domain; contextual or sensory differences would be potential counterexamples. Neither function nor subject boundary is established.

Relative-phase geometry can improve on the previous [goal-conflict proxy](FRICTION_AND_UNPLEASANTNESS_AUDIT.md): if the individual couplings and their preferred offsets are independently physically defined, cycle frustration is invariant under a change of phase convention and is not an arbitrary partition of a supplied aggregate control cost. It does **not** eliminate the need to identify the actual edges, their weights, the relevant organization or its experiential subject. Those are substantive physical and metaphysical conditions.

## 4. What actual human observations say

[Lyu et al. (2022)](https://doi.org/10.3389/fneur.2021.695187) studied 21 healthy adults with randomized emotional-picture primes, painful electrical stimulation and separate intensity/unpleasantness ratings, recording 64-channel EEG. The authors report unpleasantness differed between prime conditions while intensity did not significantly differ. This is not an equivalence result for sensory intensity or preservation of the physical pain basis. The later gamma-band **amplitude** differed by prime; a particular negative-versus-positive modulation was correlated with the corresponding unpleasantness contrast (`rho=.511`, `p=.027`, `n=19` after the authors' outlier exclusion). Other contrasts and the average late-amplitude/average-unpleasantness correlation were not significant. It is a small study with multiple analytic choices, not a validated trial-level predictor.

Crucially, **gamma power and intertrial coherence are not our F, D or P**. Intertrial coherence concerns consistency of phase relative to events across repeated trials, not the preferred phase differences of a whole interacting brain network on a single trial. The paper does not establish a coupling graph, edge-preferred offsets, frustration or the physical identity of unpleasantness. The authors state that raw data will be made available; we did not obtain or reanalyze it.

[De Martino et al. (2024)](https://doi.org/10.1002/hbm.26679) studied 24 healthy participants using TMS–EEG under painful versus non-noxious heat, and reported condition differences in alpha intertrial coherence after motor-cortex stimulation. Again, it does not calculate this model's interaction frustration and does not isolate pain from all stimulus, attention and arousal differences.

Nor is physical musical dissonance itself a universal pain law: [McDermott et al. (2016)](https://doi.org/10.1038/nature18635) report differences between Tsimane’ and comparison populations in preference for consonant over dissonant chords. Musical chord ratings concern external sound and learned perception, **not** a measurement of fundamental or subject-internal phase frustration. They caution against a simplistic auditory analogy, not against every more specific identity conjecture.

## 5. The empirical bottleneck and next experiment

The next concrete task is **not** to equate low EEG synchrony with suffering. To put any version at risk, an existing dataset or future ethically reviewed design would need:

1. independently localized and justified dynamical components and a physically meaningful phase extraction; a prespecified interaction model, scale and relevant interval;
2. independently validated estimates or defensible bounds on effective coupling strengths and preferred offsets—ideally with suitable perturbations—and a full treatment of hidden nodes, common inputs and measurement leakage;
3. separately anchored unpleasantness ratings, sensory intensity and context, with uncertainty and without defining the phase variables from the target ratings;
4. a prespecified F-only versus state-dependent D/E (and other non-frustration) comparison, subject-level held-out evaluation, and analyses of positive/neutral states as well as painful states;
5. falsifiable margins and model inadequacy tests. If the data cannot bound edge parameters or alternative routes, declare F unidentified rather than estimate it from low synchrony alone.

EEG phase associations can be distorted by volume conduction, common reference, common input, signal-to-noise ratio and finite samples; see [Bastos and Schoffelen's methodological review](https://doi.org/10.3389/fnsys.2015.00175). Removing zero-lag effects can also remove genuine interactions. Even successfully estimating this *effective* neural model would not reveal fundamental strings or establish an experiential identity.

A sensible immediate research step is a data-availability and identifiability assessment of the Lyu protocol: request or locate the EEG and ratings, specify in advance whether intervention and sensors can actually identify interaction preferences, and stop if they cannot. No human pain experiment or new data analysis was performed here; no ethically risky intervention is recommended. Such an analysis would test predictive constraints on a particular effective model, not prove the metaphysical identity.

## 6. Compatibility with the global plan

Literal fundamental strings, effective neural rhythms and this classical mathematical model are three different things. String-theoretic excitations are not established as the physical substrate of human affect; no mapping from a quantum string state to these classical oscillators, a human brain, or a subject has been constructed. The abstract phases are also not a universal external clock. Any `t` in the illustrative relaxation equation is an effective relational or laboratory time parameter, and it does not establish fundamental time or emergent spacetime.

Likewise, the minimization over configurations is a mathematical counterfactual operation, not a claim that unactualized possibilities exist in the user's strongest modal sense. A locally frustrated subsystem can be part of one actual totality without deciding whether that totality is one subject. The qualitative character of unpleasantness, a defensible subject selector, and the separate quantum-gravity/continuum obligations all remain open.
