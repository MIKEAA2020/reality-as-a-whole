# A robust relational-frustration gate: hidden connections, hidden channels and experience

## Status and result

This continues the user's proposal that misalignment in a relational, intrinsically experiential organization may contribute to discomfort. It builds on [the phase-frustration model](VIBRATIONAL_DISSONANCE_EXPERIENCE_TEST.md), [the music and quantum audit](MUSIC_QUANTUM_EXPERIENCE_SOURCE_AUDIT.md) and [the substrate-independence interface](SELF_EXISTENT_EXPERIENTIAL_SUBSTRATE_INDEPENDENCE.md). It does not assume a universal subject or actual simulations.

**Two results pull in opposite directions:**

1. If a sufficiently incompatible cycle of independently identified interaction channels is inside a specified system, its positive absolute frustration survives arbitrary additional nonnegative phase costs—even costs involving hidden nodes. A quantitative, error-tolerant lower bound follows.
2. Even perfect observation and phase-only intervention on all three nodes need not identify the interaction channels: opposite channels can cancel in the *net* phase dynamics while retaining a nonzero channel-level frustration. Thus the first result is usable only when the channels and their preferred offsets are independently identified or adequately bounded.

This is a mathematical advance in a small illustrative model: it does not measure neural frustration, identify unpleasantness, or establish the nature or necessity of the whole. The general connection between phase-lag cycle compatibility and frustration is established prior art; see [cycle holonomy and oscillator compatibility](https://arxiv.org/html/2604.19682v2). Our contribution here is this particular **measurement-error and arbitrary-extension certificate**, its contrast with normalization/state excess, and the explicit phase-only channel-confounding gate; no claim of priority over the underlying mathematics is made.

## 1. Definitions and physical commitments

For a finite graph of phase variables `φ_i`, an oriented edge/channel `e=(i,j)` has a fixed nonnegative weight `k_e` and preferred phase offset `a_e` (modulo `2π`). Define

```text
E(φ) = Σ_e k_e [1 − cos(φ_i − φ_j − a_e)],
F = min_φ E(φ),          D(φ) = E(φ) − F.
```

`F` is the minimum joint incompatibility relative to the individual zero-cost edge baselines. `D` is excess cost at an actual configuration. A local phase-reference redefinition changes `φ_i` and `a_ij` together and preserves both the cost and cycle sum. It is not a physical change of the oscillators.

An edge here is an independently meaningful **interaction channel**, not a mere EEG correlation. Parallel channels with different preferences are allowed and are counted separately. If the effective model has directed, nonconservative, higher-order, amplitude-dependent or cross-frequency couplings, the displayed potential and proofs cannot simply be assumed to apply. Phase phases, weight units, channel identity, subject boundary, time window and scale need independent specification. The minimization is a mathematical operation on allowed configurations; it does not assert a mechanism making possibilities actual.

## 2. Certificate for an imperfectly measured cycle

Consider any simple oriented cycle `C` of length `m≥2` whose true weights obey `k_e≥k_min≥0`. Reverse an edge's offset sign when traversing it opposite its chosen orientation. Let

```text
d = dist_circle(Σ_(e in C) a_e, 0),  0 ≤ d ≤ π.
```

For **every** assignment of phases, its cycle cost satisfies

```text
E_C(φ) ≥ 2 k_min d² / (m π²).                         (1)
```

Proof: choose each edge residual `r_e` as a representative in `[-π,π]` of `φ_i−φ_j−a_e`. Since phase differences telescope around the cycle, `Σr_e` is congruent to `−Σa_e` modulo `2π`; hence `|Σr_e|≥d`. On `[-π,π]`, `1−cos r≥2r²/π²`, and Cauchy–Schwarz gives `Σr_e²≥(Σr_e)²/m≥d²/m`. Substitution proves (1). The bound is generally **conservative**, not asserted sharp.

Now suppose all the cycle channels remain present with the same individual costs, and the rest of a finite graph contributes an arbitrary **nonnegative** cost, possibly involving hidden vertices, extra edges or parallel channels. For every full configuration, `E_all≥E_C`; therefore

```text
F_all = min E_all ≥ min E_C ≥ 2 k_min d²/(m π²).       (2)
```

No assumption of small hidden edges or a fully known topology is needed for this *absolute lower bound*. The crucial assumptions are that the originally identified cycle really is part of the relevant modeled system; its channel costs and baselines remain unchanged; all added modeled terms are nonnegative relative to their own baselines; and the common phase domain/potential model is valid. Hidden context may change the original couplings rather than merely add terms; then (2) cannot be used without new bounds. Subject constitution is not supplied by the graph.

### Incorporating offset uncertainty

Suppose estimated offsets `â_e` have independent or simultaneous deterministic circular error bounds `dist_circle(a_e,â_e)≤δ_e`, and each true weight is at least a validated `k_min`. Let `d̂` be the estimated cycle distance. The triangle inequality on the circle implies

```text
d ≥ d_low := max(0, d̂ − Σ_e δ_e),
F_all ≥ 2 k_min d_low²/(m π²).                         (3)
```

If the error intervals are statistical rather than deterministic, the conclusion has only their **simultaneous joint coverage**, not each marginal coverage. No claim about a real estimation procedure or 95% coverage is made.

### Worked numerical example

For three directed edges, estimate every preference as `π`, bound each circular error by `π/12`, and each weight below by `9/10`. The estimated cycle distance is `π`, so `d_low=3π/4`. In the cost units specified by the weights,

```text
F_all ≥ (2/3)(9/10)(3/4)² = 27/80 = 0.3375.
```

This holds for all continuously varying offsets and weights meeting those bounds and for all allowed nonnegative extensions. The known, unperturbed three-edge antiphase triangle has the stronger exact value `F_C=3/2`; the certificate need not match that exact optimum. If the three cycle weights are also at most `11/10` and there are **no extra edges**, choose three equal residuals with magnitude `d/3`: this gives `F_C≤3(11/10)(1−cos(π/3))=33/20=1.65`. The upper bound is for the triangle only; unknown extra costs can increase the full-graph F without a finite bound. The verifier checks 5,000 seeded parameter/state/gauge examples and the explicit constructions; the continuum result is the proof, not sampling.

## 3. Why this does not secure every mismatch measure

**Normalization can erase a uniform guarantee.** Start with the exact unit-weight antiphase triangle (`F=3/2`). Attach `N` new leaf vertices by unit-weight zero-offset edges. Every new leaf can match its parent, so the additional costs can all vanish without changing the triangle minimum: `F_all=3/2`. But if frustration is divided by total edge weight, it becomes

```text
F_all / Σ_e k_e = (3/2)/(3+N) → 0.
```

At `N=100` it is `3/206 ≈ .01456`. The nonzero lower bound on the **absolute** additive F does not imply a nonzero normalized bound as arbitrary context is added. This matters if a proposed experiential quantity is scale normalized. Leaves and all other graph elements are purely mathematical, not automatically parts of an experiential subject.

**State-dependent excess D need not increase when channels are added.** In the original unit antiphase triangle, at `φ_0=φ_1=φ_2=0`, `E=6`, `F=3/2`, hence `D=9/2`. Add a unit in-phase channel in parallel on each pair. For each pair, the opposing costs sum to `2` at every phase difference; the total is therefore constantly `6`, its new `F=6`, and its `D=0` at the same configuration. We have increased minimum structural conflict but decreased state excess. This is an exact model example, not a claim that adding a real neural connection would have that effect.

Thus hypotheses identifying unpleasantness with `F`, `D`, normalized frustration, or dissipation make different predictions. A structural lower bound cannot silently be substituted for a state-dependent or subjective one.

## 4. Channel-level frustration is not identified by net phase behavior alone

Consider the doubled triangle above:

- **A:** each pair has equal in-phase and antiphase channels. The edge-cost sum is identically `6`, the channel-baseline `F_A=6`, and its phase force `−∇E_A` is zero for every configuration.
- **B:** there are no phase-dependent interaction channels, so `F_B=0` relative to the absent-channel baseline. Include the same phase-independent background energy `6` if comparing absolute total energy rather than phase forces. That background is not an interaction channel and is subtracted as a baseline in the channel-frustration definition.

The two models have the same total phase-dependent potential (indeed the same total potential after the constant background is included), the same zero phase force, and therefore the same node-phase behavior under every external control or clamp **whose action is specified only on those phase variables** and leaves the hidden interaction mechanisms unchanged. This includes arbitrary phase-setting tests, not just passive observations. They nevertheless differ in the stipulated channel-based F because A has two genuine opposing contributions and B does not.

The contrast is conditional on the channel decomposition being physically meaningful and correctly assigned; otherwise F itself is ill-defined. A channel-selective intervention, direct measurement of its constituents, internal fluctuations or other outputs can break the operational equivalence. The example does **not** say that two complete physical systems are identical in all observables, or that no experiment can ever tell them apart. It does say that matching the full phase-only input–output map is insufficient to identify this F if cancellation and the alternative decomposition remain admissible.

This is a concrete limit on a naive substrate-independence claim. If the admissible organizational equivalence preserves only that phase input–output map, A and B are equivalent yet have different channel-level F: therefore F does **not** factor through that equivalence. A substrate-independent theory that wants F must either preserve independently meaningful channel organization, choose a different invariant, or relinquish F as its determining variable. This does not decide whether A and B are the same subject or feel the same: the relevant subject and experience-preserving equivalence are precisely what remain open.

Coupling reconstruction is an existing research area, not invented here. [Kralemann and colleagues](https://ar5iv.labs.arxiv.org/html/1102.3064) discuss reconstructing phase dynamics and note loss of coverage under full synchronization; a [2025 inference study](https://journals.plos.org/complexsystems/article?id=10.1371%2Fjournal.pcsy.0000063) studies reconstruction under particular weak-coupling/model assumptions. The exact cancellation above is a separate ambiguity between channel decompositions when only their sum is accessible; the existence of successful inference methods under narrower assumptions does not remove it. Neural source leakage and common input provide further practical challenges; see [Bastos and Schoffelen](https://doi.org/10.3389/fnsys.2015.00175) and this [causal-connectivity analysis](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011574).

## 5. The empirical bridge: what must now be demonstrated

An informative study needs all three gates, not just one:

1. **Subject and scale:** identify a defensible local subject/episode, analysis interval, candidate oscillatory components and physical channel baselines. Do not use unpleasantness reports to select the subject or tune the physical variable being tested. Human reports anchor the target but do not solve subject constitution in general.
2. **Channel identifiability:** fit explicitly competing channel models and external/common-input alternatives, use independent perturbation or physiological constraints where ethically and technically justified, and report joint uncertainty on weights and oriented offsets. If phase-only data admit both opposing-channel and net-only models, return **unidentified**, not a falsely precise F. Check robustness to signal leakage, limited phase coverage, noise, hidden channels, and non-potential dynamics; use negative controls and out-of-model simulations.
3. **Phenomenal discrimination:** predefine F, D and simple stimulus/context/sensory-intensity comparison predictors, then evaluate independently measured unpleasantness and other dimensions on genuinely held-out participants and contexts. Separately analyze equality or equivalence with meaningful prespecified margins; a nonsignificant difference is not equivalence. Pleasant challenge, relief, neutral states and nonpainful aversion are important tests. A successful prediction is evidence for a model, not a proof of metaphysical identity.

Potentially informative context manipulation is already known: [Zunhammer et al. (2018)](https://doi.org/10.1001/jamaneurol.2018.2017) meta-analyzed individual data from 603 participants in 20 placebo-imaging studies and found moderate effects on pain reports but much smaller effects on the neurologic pain signature. This distinguishes reported pain from *one measured fMRI signature*, not from all neural processing, the whole nervous system, or independently measured F. It neither confirms nor refutes the proposed channel-frustration identity. No raw data from that meta-analysis were inspected here, and standard fMRI signatures do not by themselves identify oscillatory channel offsets.

A useful **pre-data decision rule** is: proceed to an F–experience comparison only if the admissible uncertainty set separates relevant values of F and the independent report assay has sufficient reliability. Otherwise the correct result is underidentification. A deliberately strong fixed-boundary, fixed-scale `U=g(F)` rule is challenged by independently justified equal-F cases with meaningfully different unpleasantness, subject to measurement/error margins and its declared domain; more flexible identity hypotheses must specify which additional state and context variables determine their predictions. This is not a request to harm participants: any future intervention would require ethical review, voluntary consent, safe limits and unrestricted withdrawal.

## 6. Consequences for the whole-account

This result makes the user's suggestion more precise, not less relevant. **Local incompatibility can be objective and robust to hidden context** within the declared model, so it need not be dismissed as mere subjective labeling. But objective incompatibility is not yet shown to be a feeling, and the channel organization is not established by waveform similarity or phase-only dynamics. A subject boundary, the relevant intrinsic-quality relation, and a measure for plural experiences remain independent open obligations in the [framework battery](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md).

The analysis uses an effective local phase description and does not introduce an external universal clock or a creator. It derives neither quantum mechanics nor spacetime, nor does it decide why the self-sufficient experiential ground is self-existent or why all genuine possibilities are actual within it. Existing physical derivations and subject tests remain separate prerequisites.

## Reproduction

Run `python verification/frustration_hidden_channel_gate.py` for the [receipt](verification/frustration_hidden_channel_gate.json). It checks the conditional bound at 5,000 seeded triangle states, the gauge transformation, exact example fractions and opposing-channel force cancellation. The proof covers the continuous cases; the checks do not certify a real interaction graph or identify any experience.
