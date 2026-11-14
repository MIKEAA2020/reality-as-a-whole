# Microtubules, anesthesia and quantum consciousness: a causal discrimination gate

## Decision

Microtubule-related interventions and optical measurements provide a legitimate empirical research direction. They do not yet identify the quantum physical feature of a microtubule as a cause of conscious experience, establish objective reduction, or establish an experiential universal subject. The most useful next step is not another correlation between an anesthetic, microtubules and behavior. It is a **selective-intervention and rival-pathway test** with an independently validated quantum-sensitive measurement and independently anchored behavioral endpoints.

The concrete contribution below is an exact three-rival counterexample for this evidence chain and a conditional quantitative sensitivity criterion for a proposed intervention. The counterexample is a deliberately simple mathematical construction, not an established result about neural microtubules or proof that the empirical alternatives are physically realizable. The logic of mediator confounding is established, not a new discovery; see [Imai, Keele and Tingley](https://imai.fas.harvard.edu/research/files/mediationR2.pdf).

**Status:** no animal experiment, spectroscopic measurement, original-data reanalysis, independently calibrated assay, or evidence for Orch OR is produced here. The toy checks run exactly in rational arithmetic.

## 1. What the reported results constrain

- [Khan et al. (2024)](https://www.eneuro.org/content/11/8/ENEURO.0291-24.2024) observed a 69-second mean increase in latency to loss of righting reflex (LORR) after epothilone B in eight male rats, with 7/8 increases and a reported two-sided permutation-test p-value of 0.0016. Pre-treatment sessions always preceded post-treatment sessions; a separate four-rat tolerance group provided a limited control. This is a finding about a pharmacological intervention and a behavioral proxy, not a direct measurement of subjective experience, microtubule coherence, collapse or entanglement. The published p-value is reported, not independently replayed here.
- [Huang et al. (2026)](https://doi.org/10.1016/j.neuropharm.2026.110834) report a 29-second within-subject increase in mice at 8 mg/kg epothilone B on the day after injection; it is a follow-up by an overlapping team, not an independent replication. [Li et al. (2025)](https://doi.org/10.1186/s12871-025-02956-9) report increased isoflurane sensitivity on a dose-response measure after a different microtubule stabilizer, epothilone D. Species, dose, treatment duration and endpoints differ, so it is not a direct replication or refutation.
- [Kalra et al. (2023)](https://doi.org/10.1021/acscentsci.2c01114) report UV-excited energy migration in prepared, paclitaxel-stabilized microtubules in solution and a reduction of estimated exciton diffusion length under etomidate and isoflurane. Their roughly 6.6 nm estimate is based on an analysis of fluorescence quenching, not a direct measurement of a long-lived, conscious, in-vivo superposition. They note that an additional convulsant also reduced quenching in experiments not reported in detail. An optical excited-state population lifetime alone is not a coherence lifetime: for a simple two-level system their relation depends on pure dephasing, and cannot be transplanted uncritically to a complex biological sample; see [optical-coherence example](https://doi.org/10.1038/s41467-025-61884-x).
- [Liu, Chen and Ao (2024)](https://doi.org/10.1103/PhysRevE.110.024402) model entangled photon-pair generation in a myelin cavity; this is not a demonstration of inter-brain entanglement. The article's proposed jump from such physics to a shared cosmic consciousness needs further independent argument and evidence.

A drug can alter microtubule structure, neural transport, excitability, respiration, anesthetic uptake and behavior through overlapping pathways. Quantum mechanics underlies chemistry generally; the relevant contrast is a **specified, independently detectable quantum state or effect causally required by the proposed mechanism**, versus named rival pathways that do not require that feature. Calling one pathway “classical” below is shorthand for that restricted contrast, not a claim that biological matter obeys fundamentally classical physics.

## 2. Exact counterexample: a strong assay correlation is not enough

Define a hypothetical binary quantum feature `Q`, a classical-pathway variable `C`, a behavioral proxy `Y`, an intervention `X`, and a noisy assay `M`. None is asserted to be a real or measured property of microtubules. `X` might stand for a treatment assignment. Let `U` and `N` be independent background and assay-error bits, with `P(U=1)=1/4` and `P(N=1)=1/10`. The `1/10` is an **invented demonstration value**, not an assay calibration. All additions below are XOR.

Introduce a second controllable intervention `S`, initially fixed at zero. Compare:

| Model | State `Q` | Pathway `C` | Behavior `Y` | Assay |
|---|---|---|---|---|
| Q-causal | `X ⊕ U ⊕ S` | `X ⊕ U` | `Q` | `M = Q ⊕ N` |
| C-only | `X ⊕ U ⊕ S` | `X ⊕ U` | `C` | `M = Q ⊕ N` |
| Shadow C | `X ⊕ U ⊕ S` | `X ⊕ U ⊕ S` | `C` | `M = Q ⊕ N` |

At `S=0`, **all three models have exactly the same full joint distribution of `(M,Y)` for each randomized `X`**, including a strong positive association of assay and behavior. The response means `P(Y=1 | X=0)=1/4` and `P(Y=1 | X=1)=3/4` are also identical. But an ideal, explicitly stipulated `do(Q=q)` that changes `Q` while holding the equations for `C` fixed gives:

| Model | `E[Y | do(Q=0), X=0, S=0]` | `E[Y | do(Q=1), X=0, S=0]` | Difference |
|---|---:|---:|---:|
| Q-causal | 0 | 1 | 1 |
| C-only | 1/4 | 1/4 | 0 |
| Shadow C | 1/4 | 1/4 | 0 |

Thus even observing a randomized treatment effect, a quantum-sensitive assay and their joint association does not establish that changing the assayed state changes behavior. Randomizing `X` does not randomize `Q` independently of other consequences of `X`. This is a concrete specialization of the usual mediator-identification problem; it is not an assertion that either `Q` or `C` exists in a real brain.

The artificial `do(Q)` operation is **not** a claim that quantum coherence can be toggled independently of its substrate or energy budget. Its physical implementability is precisely the difficult task. For example, an intervention that changes a phase coherence could also alter populations, heat, signaling, structural stability, or measurement access; an ideal causal arrow is not a laboratory instrument.

## 3. A selective intervention helps—but an exclusion claim must be earned

At `X=0`, varying `S` changes the expected outcome by **1/2** in Q-causal and **0** in C-only. If the proposed intervention really acts on `Q` but leaves this particular alternative pathway unaffected, it discriminates these two stipulated mechanisms. The conditional conclusion is useful: it tells us exactly what a good control must protect.

However, Shadow C has `C = X ⊕ U ⊕ S`. It produces the **same full `(M,Y)` distribution as Q-causal in all four `X,S` arms**. Yet under the ideal `do(Q)` it has no Q-to-Y effect. Randomizing `S`, measuring the assay, and seeing the predicted outcome are therefore not enough against an unmeasured pathway that is also changed by `S`. The shadow model is a mathematical adversary, not a documented biological mechanism. The remedy is not to insist that every conceivable shadow has been ruled out: it is to identify the real candidate bypasses, measure and bound them, challenge the intervention's selectivity, and state the residual assumption. Otherwise the effect of the *instrument* is identified but the contribution of the quantum feature is not.

The [verifier](verification/microtubule_mediation_rival.py) enumerates every `U,N` value for all four arms and checks the joint equalities and controlled interventions exactly. The [receipt](verification/microtubule_mediation_rival.json) contains all 48 probabilities. It is an algebra check, not a neuroscience inference. The construction does not require an external clock: `X` and `S` label local experimental settings in stipulated mathematical models, not a fundamental time parameter. The listed substitutions are not thereby established to be physically feasible or genuinely possible in the user's strongest sense; see [the actuality and causal-inference analysis](ACTUALITY_CAUSAL_INFERENCE_AND_BELL.md).

## 4. A quantitative conditional gate

For an actual proposed intervention, choose one operationally validated state feature `q` and a prespecified outcome `Y`. At a fixed `X`, suppose the following **strong model** is warranted for each experimental unit:

```text
Y(s) = α + θ q(s) + d(s),      s ∈ {0,1}.
```

Here `θ` is a common additive Q-effect on the declared outcome scale; `d(s)` contains all other effects of changing `S`. Units may have different `α`, `q(s)` and `d(s)`. This common-effect model is an assumption, not a general theorem about brains or a consequence of observing `q`. Let `ΔY = E[Y(1)-Y(0)]`, `Δq = E[q(1)-q(0)]`, and assume a scientifically justified bound `|E[d(1)-d(0)]| ≤ ε`. Then

```text
ΔY = θ Δq + δ,   |δ| ≤ ε.
```

If `0 < l ≤ Δq ≤ u` and `ΔY > ε ≥ 0`, it follows algebraically that

```text
(ΔY − ε)/u ≤ θ ≤ (ΔY + ε)/l.
```

**Illustration only:** with `ΔY=0.08`, `Δq ∈ [0.20,0.40]`, and `ε=0.02`, the conditional range is `θ ∈ [0.15,0.50]`. These numbers are invented; they do not estimate any biological effect. If the credible bypass allowance reaches `ε ≥ |ΔY|`, a zero quantum contribution is no longer excluded by this criterion. If `Δq` may be zero or change sign, the displayed quotient interval is invalid. If the common-effect model fails, interaction, nonlinearity, heterogeneous response, saturation or selection may make this formula inappropriate; use an explicitly justified alternative instead.

For actual inference, treatment contrast, quantum-state change and bypass bound must refer to the **same target population and outcome scale**. Include uncertainty in all three, measurement error and calibration drift. Simultaneous confidence sets or another valid joint uncertainty procedure are required; inserting point estimates and a convenient after-the-fact `ε` is not a confidence interval. A small bound on measured covariates alone does not bound all unmeasured pathways. The assay may itself perturb the sample, and an ex-vivo signal does not automatically calibrate the living preparation. If `ε` cannot be defended, report the result as **not identified**, not as zero bypass.

## 5. Prospective experiment: staged, not a ready-to-run clinical protocol

1. **Specify the physics.** Before choosing an endpoint, give the quantum model's state, preparation, interaction, spatial scale, coherence witness or bounded nonclassicality criterion, relevant lifetime and predicted effect size. Show why the proposed witness distinguishes the claimed quantum feature from specified semiclassical and technical alternatives. If the model invokes collapse, spell out its dynamics and show consistency with applicable model-specific experimental bounds. Neither fluorescence intensity nor an oscillatory signal alone is a universal coherence or entanglement witness.
2. **Validate the assay independently.** Calibrate sensitivity, specificity, negative controls, perturbation by the probe, temperature, tissue scattering, heating and ordinary chemistry. Bench preparations and living tissue are separate stages; phase-sensitive optical signals may still admit classical-field explanations. Resolve the relation between the in-vitro optical effect and the proposed in-vivo state. Do not assume a 10% error rate from the toy.
3. **Establish the intervention.** Develop and validate a perturbation that changes the predeclared quantum feature at a relevant site and scale while limiting structural, thermal, receptor, transport, metabolic and uptake changes. Include sham and alternative perturbations with overlapping nonquantum effects, positive/negative quantum-witness controls and reversibility. This is a demanding open engineering requirement; no such selective intervention is claimed available here. Control matching must not depend solely on outcomes measured after treatment.
4. **Randomize and compare rivals.** With independent ethics review, randomize the intervention and applicable controls, blind measurement, prespecify dosing, sex, species, outcome, exclusions and analysis, and independently replicate. Quantify treatment interaction and absolute effects, not just p-values. Predeclare a credible bypass bound `ε`, the minimal effect, simultaneous uncertainty and an explicit result that would challenge the specified quantum model; if the assay or selectivity fails, report the test as inconclusive rather than a negative verdict on all quantum theories.
5. **Separate state, function and experience.** Use complementary physiological and behavioral measures, including motor/respiratory and anesthetic-concentration controls. LORR is useful but not equivalent to experience. Human report studies, when safe and ethically appropriate, could add a separately calibrated phenomenal contrast; reports are also imperfect, and this proposal does not justify risky human interventions. Show the quantum signature causally improves a predeclared prediction beyond nonquantum neural rivals rather than merely co-varying with sedation.

A positive outcome under the validated assumptions would strengthen a particular quantum-functional account. It would still not by itself establish Penrose's objective-reduction mechanism, a unique subject boundary or the ontological claim that reality's intrinsic nature is experience. Conversely, a null result within a sensitive, well-calibrated regime would constrain **the specified model and regime**, not every conceivable quantum-consciousness theory. The protocol above is an analysis plan, not preregistration or a frozen executable experimental design; future researchers must fix actual operational parameters before collecting confirmatory data.

## 6. Relation to the whole-framework obligations

This gate provides a possible path for testing a **local physical interface**, not a derivation of the absolute. If a quantum feature were found to be causally important for reportable states, the separate questions would remain: why it has an experiential aspect at all; which organized processes constitute individual subjects; whether there is a further universal *subject*, not merely a connected physical whole; and why the whole is necessarily actual. These cannot be silently inferred from entanglement or from the word “quantum.”

The [subject-interface gate](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) and [experiential-grounding rivals](EXPERIENTIAL_GROUNDING_RIVAL_BATTERY_GATE.md) show why even a good physical readout leaves independently specified subject and grounding questions. An identity thesis need not posit conversion from physics to experience, but it must specify and justify the identity and its conditions. Nothing in this gate commits the project to a literal simulator, fundamental spacetime, an external universal clock, or a process by which mere possibilities become actual. The strongest-possibility-equals-actuality thesis does not establish which mathematical countermodel describes reality. The full foundation battery remains incomplete.

Run `python verification/microtubule_mediation_rival.py`. A passing script checks finite stated equations; it is neither an independent replication nor a framework or consciousness-theory pass.
