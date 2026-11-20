# Quantum erasure, Bell correlations and selection of perspectives

## Purpose and result

This gate connects three requirements that are easy to confuse: (1) a coherent quantum model must reproduce interference and its erasure, (2) a local hidden-variable account must meet Bell's assumptions or explicitly relax them, and (3) a proposed measure on perspectives must specify what is being selected and how. The calculations are **benchmark models**, not a new derivation of quantum mechanics or evidence that qubits experience anything.

The most consequential constraint for the larger account is that **the existence of all listed perspectives is not enough to determine their observed correlations**. The weight and selection rule also matter. In an explicit local toy model, every experimental setting has the same detection and coincidence rates and the detected outcomes have balanced marginals, yet postselection produces the algebraic CHSH value `4`. The full data, including no-detection events, are local. This is a known detection-loophole effect, used here to stress-test the proposed perspective/measure interface—not a novel Bell theorem or an explanation of loophole-free experiments.

## 1. Sources and reading scope

- Englert, [*Fringe Visibility and Which-Way Information: An Inequality*](https://doi.org/10.1103/PhysRevLett.77.2154): cited for established visibility–distinguishability results. Original full text was not read for this gate.
- Chiou and Hsu, [*Complementarity relations of a delayed-choice quantum eraser in a quantum circuit*](https://arxiv.org/html/2207.03946v1): abstract, introduction and beginning of the simple model (first two of 20 HTML chunks) read, not the full text, figures, appendices, code or experimental data. The authors present a related circuit, differing visibility definitions and IBM experiments; our numerical examples are not a replication.
- Horodecki, Horodecki and Horodecki, [*Violating Bell inequality by mixed spin-1/2 states: necessary and sufficient condition*](https://doi.org/10.1016/0375-9601(95)00214-N): bibliographic record and abstract-level descriptions inspected; the original full paper and proof were not read. Its two-qubit CHSH result is standard; only a specific choice of observables is needed below.
- Branciard, [*Detection Loophole in Bell experiments: How post-selected local correlations can look non-local*](https://arxiv.org/html/1010.1178v2), [published version](https://doi.org/10.1103/PhysRevA.83.032123): abstract and first of ten HTML chunks read, not the full article, figures or proof. Detection-loophole models and their polytopes are established research.
- Emmerson, [*Bell–CHSH Under Setting-Dependent Selection: Sharp Total-Variation Bounds and an Experimental Audit Protocol*](https://doi.org/10.3390/quantum8010008): abstract and search-retrieved selected passages read; not the complete article or proof. The bound used in §4 is explicitly stated there and is **not claimed as new**.
- Hensen et al., [*Experimental loophole-free violation of a Bell inequality using entangled electron spins separated by 1.3 km*](https://arxiv.org/abs/1508.05949): abstract read for this gate, not full paper, supplements or raw data. The earlier [Bell assessment](ACTUALITY_CAUSAL_INFERENCE_AND_BELL.md) records reported results and their assumptions; this gate does not reanalyze them.

## 2. Interference and the eraser

First, consider a balanced path qubit `A` coupled to a marker `B`:

```text
|Ψ> = (|0>|m₀> + |1>|m₁>)/√2,
⟨m₀|m₀⟩ = ⟨m₁|m₁⟩ = 1.
```

For an ideal equal-amplitude output analyzer whose phase is scanned, the **unconditional** path fringe visibility is `V=|⟨m₀|m₁⟩|`. This is a standard two-path result, conditional on the preparation and visibility definition. For pure equal-prior marker states, optimal distinguishability `D=√(1−V²)`; more general preparations and mixed markers give appropriate inequalities instead. The verifier independently evaluates an overlap `3/5`, obtaining fringe maxima `4/5`, minima `1/5`, and `V=3/5`.

Next take orthogonal path-marker correlations, with a tunable retained coherence:

```text
ρ_v = (|00><00| + |11><11| + v|00><11| + v|11><00|)/2,
0 ≤ v ≤ 1.
```

For `v=1`, this is the pure, perfectly path-marked Bell state; for smaller `v`, it may arise by discarding an additional system correlated with the two alternatives. Let the path analyzer measure `Xφ=cosφ X+sinφ Y` with result `a=±1`, and measure the marker either in its path basis `Z` or its complementary basis `X`, with result `b=±1`. Standard Born probabilities give

```text
P(a,b | Xφ, X) = (1 + ab v cosφ)/4,
P(a,b | Xφ, Z) = 1/4,
P(a | Xφ, X) = P(a | Xφ, Z) = 1/2.
```

Conditional on `b=+1` or `b=−1` in the complementary measurement, the path results show opposite-phase fringes of visibility `v`; combined, these fringes cancel. A path-basis read supplies path correlation with a `Z` path measurement, but gives no conditional path-interference fringes in this `Xφ` comparison. Changing or delaying the marker measurement does **not** change the already available unconditional path statistics. The conditioned patterns require the outcomes to be compared; there is no faster-than-light signalling or necessary retroactive rewriting of an earlier record.

**Important distinction:** measuring the marker in `X` and sorting the `b` results is not the same procedure as measuring `Z`, discarding its result, and then claiming the original coherence survives. In the latter case the unread `Z` measurement dephases `ρ_v` to `ρ_0` in this model. The verifier checks both procedures. A complete reversal that controls all relevant record carriers is a further distinct procedure, analyzed for the friend circuit in [the earlier record tradeoff gate](REVERSIBLE_FRIEND_RECORD_COMPLEMENTARITY.md).

## 3. The same state as a Bell benchmark

For this same `ρ_v`, choose `A₀=Z`, `A₁=X`, and

```text
B₀ = (Z + vX)/√(1+v²),   B₁ = (Z − vX)/√(1+v²).
S = E₀₀ + E₀₁ + E₁₀ − E₁₁ = 2√(1+v²).
```

Thus any `v>0` violates the standard local CHSH bound 2 in this *ideal family* when these `v`-dependent settings are used; at `v=3/5`, `S=2√34/5 ≈ 2.3324`. This number is a quantum prediction for a stipulated state and settings, not an experimental result. It is also the two-qubit maximum for this family by the cited Horodecki criterion, but the gate needs only the explicitly exhibited value. Other states, noise and settings need not obey this relation between eraser visibility and CHSH.

Performing the unread `Z` marker measurement physically changes the state to `ρ_0`; using the **same original settings** gives `S=2/√(1+v²)`, not the original value. Re-optimizing at `ρ_0` gives a maximum of `2`. Importantly, the quantum eraser's conditional fringes and the Bell score are evaluated in different measurement contexts, not a single simultaneous measurement of noncommuting observables.

The conventional `|S|≤2` inference assumes bounded outcomes, Bell-local factorization and an appropriate common source-variable distribution across settings, plus experiment-specific sampling and timing controls. No-signalling is weaker than Bell-local factorization. Violating CHSH excludes that *joint set of assumptions*, not locality in every possible sense, determinism as such, or the user's timeless ontology. It also does not uniquely establish one quantum interpretation.

## 4. Perspective selection: an explicit diagnostic

The project's strong possibility–actuality thesis allows all members of the following **finite table** to be actual local occurrences within a single whole; it does not supply their weights. For a mathematical test only, assign uniform weights to all 32 rows with settings `(x,y)` and hidden variable `λ=(u,v,r)`, each bit in `{0,1}`. Each setting pair occurs with each `λ` once. The bits `u,v` are source-side guesses, independent of the actual settings before selection; `r` is a shared random sign bit.

Local response rules are:

```text
Alice: if x=u, report a=(-1)^r; otherwise no detection.
Bob:   if y=v, report b=(-1)^(r+uv); otherwise no detection.
```

Each site uses its own setting and the pre-existing shared variable only. Each local detector fires on half the rows; both fire on one quarter for **every** setting pair. Among coincidence rows each local outcome is balanced, yet

```text
(E₀₀,E₀₁,E₁₀,E₁₁) = (1,1,1,−1),    S_selected = 4.
```

That is a formal superquantum PR-box pattern in the **selected** data, not a physical quantum prediction. Conditioning on coincidence means `u=x, v=y`, so the selected `λ` distributions differ maximally across setting pairs despite their initial independence. If no detection is instead assigned the fixed outcome `+1` on every row, the same full table has correlations `(1/2,1/2,1/2,0)` and `S=3/2`. The complete local outcome distributions, including no-click, are no-signalling in this construction. Equal marginal detection rates and balanced detected outcomes do not prove fair sampling.

The verifier also constructs a second local selection model that matches a **quantum**, rather than superquantum, benchmark: at `v=3/5`, take Bob's fixed observables `(3Z±4X)/5`. The quantum joint distributions have balanced marginals and correlations `(3/5,3/5,12/25,−12/25)`, giving `S=54/25=2.16`. In the second model, `λ=(u,v,r,k)` is uniform over source guesses `u,v`, a sign bit `r` and `k=0,…,49`, independently of the settings. The same local detection rules apply. On detection Alice reports `(-1)^r`; Bob multiplies that sign by `(-1)^(uv)` and by `+1` when `k<40` for `u=0` or `k<37` for `u=1`, otherwise by `−1`. The complete table contains 1,600 equally weighted occurrences. For each setting pair, one quarter are coincidences; their **full joint outcome probabilities**, not only CHSH, match the ideal quantum probabilities at these four settings. This explicit construction is an application of the known detection loophole, not a literature-wide novelty claim. It does not match an ideal quantum experiment's all-trial no-click statistics and is not a universal simulation of quantum correlations.

Neither low-efficiency model reproduces an event-ready experiment that has already closed the particular detection loophole under its stated controls. Neither is a diagnosis of Hensen et al. or evidence of a hidden selection of conscious observers.

### Quantifying what a proposed selection rule must explain

Suppose a candidate *Bell-local* model has bounded local response functions fixed across contexts and, **after its specified selection**, four normalized hidden-variable distributions `ν_xy` over a common space. If selection depends on outcomes, the relevant local response randomness must be included in `λ`, so that selection does not silently change the response functions at fixed `λ`. For any common reference distribution `μ`, the cited Emmerson bound is

```text
|S_selected| ≤ 2 + 2 ∑_(x,y) TV(ν_xy, μ),
TV(p,q) = 1/2 ∑_λ |p(λ)−q(λ)|.
```

The same expression holds for probability measures using the usual supremum definition of total variation, provided all four distributions refer to a common hidden-variable space and response functions. If a candidate claims the ideal `v=3/5` Bell score arises **solely through such selected local responses**, it requires

```text
∑ TV(ν_xy, μ) ≥ (2√34/5 − 2)/2 ≈ 0.1662,
```

for every common `μ`; equivalently the mean of the four distances must be at least `0.04155`. These are necessary bounds, not sufficient models, and neither the hidden-variable distributions nor their total-variation distances are observable from outcome marginals alone. The cited paper addresses stronger and sharp selection bounds. No total-variation estimate of real subjects, nor attribution of experimental Bell violation to subject selection, has been made here.

## 5. Consequences for the whole-account

A viable account needs a map from physical trial/record data to a domain of experiences, then a justified weighting or self-location rule. It must not implicitly treat setting-dependent selected populations as if they were one common ensemble. If it proposes to explain a Bell violation through selection **and** retains Bell-local response functions, it inherits bounds such as the above and must supply independently constrained selection variables, losses, timing and controls. If it instead retains standard quantum statistics, the simple local-selection explanation is not required. Either way, adding perspective labels by itself supplies neither a measure nor an explanation of the physical correlations.

This is a conditional interface requirement, not a claim that perspectives are detector clicks or that any selection occurs. The prior [contextuality gate](CONTEXTUAL_PLENITUDE_AND_RECORD_IDENTITY_GATE.md) constrains a different claim—one context-independent assignment of compatible observables—and the [Bell analysis](ACTUALITY_CAUSAL_INFERENCE_AND_BELL.md) distinguishes actual local contrasts from unperformed same-token counterfactuals. Neither is a proof of subjects, experiential unity, spacetime emergence or necessary existence. The finite indices above need not be a fundamental clock; they do not derive local temporal experience.

## 6. Reproducibility and next dependencies

Run `PYTHONPATH=<numpy environment> python verification/eraser_bell_selection_gate.py`. The [script](verification/eraser_bell_selection_gate.py) checks a pure-marker overlap, 21 values of `v`, 25 phase values each, the relevant Born probabilities, coherent versus unread-marker protocols, CHSH observables, and the entire exact 32-row and 1,600-row selection tables. [Results](verification/eraser_bell_selection_gate.json) combine floating-point quantum checks with exact rational local frequencies. These are not independent proofs of the general results or measurements on hardware.

To advance beyond this benchmark: specify at least one candidate experiential constitution and selection law *before* looking at the target correlations; specify its relation to physically recorded and missing trials, its invariance under equivalent representations, and an independently calibratable prediction. Compare it with actual event-ready or loss-aware data under the correct protocol. Until such a candidate exists, no subject measure, necessary plenitude, or decisive solution to the underlying physics problem has been established.
