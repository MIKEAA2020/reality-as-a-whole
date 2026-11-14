# Schlosshauer: decoherence, records and the subject boundary

## Source and decision

The supplied file is Maximilian Schlosshauer, “[Decoherence, the measurement problem, and interpretations of quantum mechanics](https://doi.org/10.1103/RevModPhys.76.1267),” *Reviews of Modern Physics* **76**, 1267–1305, published 23 February 2005. The supplied 39-page PDF has SHA-256 `2e6f1b7eacf9deaf7b09bf615f22ab3e9a21f18a1dff3164f20e2e4241362dd7`. It is a 2005 review, not an up-to-date survey of all subsequent work. The arXiv version is [quant-ph/0312059](https://arxiv.org/abs/quant-ph/0312059); do not assume that version is byte-identical to the supplied published PDF.

The central constraint for our framework is **not** that decoherence proves an experiential whole or disproves definite experience. It explains, within specified system–environment dynamics, why some interference becomes hard to observe locally and why certain records are more stable. It does not by itself supply a unique actual outcome, a subject selector, the Born rule without additional assumptions, or a derivation of the system–environment split from a timeless absolute. Different interpretations add different commitments.

This report applies two points from the supplied review to our existing instrument and constitution gates: a bounded-access distinguishability calculation, and an explicit near-degenerate eigenbasis stress test. The underlying decoherence, trace-distance and eigenvector facts are established, not novel discoveries. The numerical cases are illustrative consequences for our project, not experimental results. The original PDF is identified by hash but is not copied to this public repository.

## 1. What the paper actually says

- **Reduced records versus global state.** In Secs. III.B–III.D (printed pp. 1274–1277; PDF pp. 8–11), the author explains that tracing over environmental degrees of freedom gives local predictions, assuming the usual probability rule. A nearly diagonal reduced state has the same local statistics as a corresponding mixture, but the total state can remain coherent. Treating the reduced state as ignorance about one already selected result would assume what a single-outcome account must explain.
- **Pointer basis versus diagonalization.** In Sec. III.E.4 (printed pp. 1281–1282; PDF pp. 15–16), he explicitly warns that instantaneous Schmidt states—eigenvectors of a reduced density matrix—are not generally the same as interaction-stable pointer states. Near-degenerate populations can make a tiny residual off-diagonal term determine a very different eigenbasis. This is directly relevant to any proposed rule that uses spectral components to individuate subjects or branches.
- **Outcome interpretations differ.** In Sec. IV and the conclusion (printed pp. 1284–1303; PDF pp. 18–37), he discusses relative-state, collapse, Bohmian, modal and consistent-histories approaches. His argument that decoherence alone does not solve definite outcomes is especially explicit under the standard eigenstate–eigenvalue interpretation; it is not a theorem that all relative-state or other interpretations fail. In collapse models, decoherence and the extra collapse dynamics can coexist, and approximate tails remain an issue.
- **Subsystems and probabilities are separate assumptions.** Sec. III.A (printed p. 1274; PDF p. 8) says the system/environment decomposition is nontrivial, especially at the scale of the universe. Sec. III.F discusses Zurek's envariance proposal and questions concerning its assumptions; it should not be represented either as automatically deriving the Born rule from tracing alone or as a universally rejected proof. The paper suggests subjective definiteness may be sufficient, but that philosophical position is not established by the decoherence calculation.

The author analyzes physical quantum models with system/environment splits and evolution. He does not derive their applicability to a timeless, necessarily actual experiential absolute, nor claim that laboratory environments are external to the whole. An environment for a subsystem can consist of other degrees of freedom **inside** the whole.

## 2. A quantitative access boundary

Consider an idealized, normalized state with `S` and a pointer `A`, plus `N` environmental fragments:

```text
|Ψ⟩ = a |0⟩S |0⟩A ⊗ᵢ |e₀⟩ᵢ + b |1⟩S |1⟩A ⊗ᵢ |e₁⟩ᵢ,
|a|² + |b|² = 1,       ⟨e₁|e₀⟩ = c,       |c| ≤ 1.
```

Compare it with the explicitly different global state obtained by deleting the cross terms in this **declared branch basis**:

```text
ρmix = |a|² |0,0,e₀…⟩⟨0,0,e₀…|
     + |b|² |1,1,e₁…⟩⟨1,1,e₁…|.
```

The latter is a mathematical comparator; no particular physical collapse law is assumed. Let an observer have unrestricted joint access to `S`, `A` and `k` selected environmental fragments, while the other `m=N−k` fragments are inaccessible and traced out. Under the product-fragment assumption, the difference between the two reduced states is a two-dimensional off-diagonal block with magnitude `|ab| |c|^m`. Therefore

```text
D = (1/2)||ρcoh,accessible − ρmix,accessible||₁ = |ab| |c|^m.
```

For equal prior probabilities, the ideal optimal single-shot success probability is the standard Helstrom value `(1+D)/2`. This assumes that the two preparations are defined, prior weights are equal, and an optimal joint measurement on *all* declared accessible degrees of freedom is implementable; it is not a proposed practical brain experiment.

For `a=b=1/√2` and `c=1/2`:

| Inaccessible fragments `m` | Trace distance | Best equal-prior success |
|---:|---:|---:|
| 0 | 1/2 | 0.750000 |
| 1 | 1/4 | 0.625000 |
| 4 | 1/32 | 0.515625 |
| 10 | 1/2048 | 0.500244 |

This is an upper limit on distinguishability under the stated access restriction, not a claim that the full state is physically collapsed. If the inaccessible branch environments are exactly orthogonal, the accessible trace distance is exactly zero; if they overlap, it is merely small. Independent repetitions may accumulate evidence, and opening access to more fragments changes the model and can increase distinguishability. The model supplies no universal rate for real environments.

The result sharpens the [one-slot collapse identifiability gate](CONSCIOUSNESS_COLLAPSE_IDENTIFIABILITY_GATE.md): identical accessible channels or records cannot distinguish those particular mechanisms **at that interface**, but access to environmental correlations or additional interventions can distinguish specified dilations. It does not prove that a conscious observer can perform such a measurement or that a global interference observable is feasible for a macroscopic brain.

## 3. A near-degeneracy test for a subject or branch selector

The review already gives the general warning in its Eq. 3.23, credited to earlier work. The following is a direct numerical stress case, not a new general theorem.

Let the physically specified interaction select `|0⟩,|1⟩` as stable pointer states in a simple nondemolition dephasing model. At one time take

```text
ρ = [[1/2 + δ, ε], [ε, 1/2 − δ]],
ε = 0.01,    δ = ε² = 0.0001.
```

This is a valid density matrix. It is extremely close to its pointer-basis diagonal: their trace distance is `ε = 0.01`. Yet its dominant eigenvector is rotated relative to `|0⟩` by

```text
θ = (1/2) arctan(ε/δ) ≈ 0.7804 radians,
|⟨0|vmax⟩|² ≈ 0.505.
```

So the eigenvector is almost an equal superposition of the two pointer states. As `ε→0` with `δ=ε²`, the off-diagonal tends to zero while `θ→π/4`. This does not contradict spectral perturbation theory: the population gap also tends to zero. It shows why small off-diagonal terms alone do not imply a nearby eigenbasis; a relevant spectral gap must also be controlled.

A stronger selector instability uses `ρ± = I/2 ± ε X` with `0<ε<1/2`. Their trace distance is `2ε`, which can be arbitrarily small, while their uniquely top-ranked eigenprojectors `|+⟩⟨+|` and `|−⟩⟨−|` have trace distance **1**. Both can arise in the same controlled-dephasing setup from different initial phase preparations. A selector that assigns categorically different branches or subjects to the top eigenvector therefore needs a gap, robustness margin, or an alternative stability criterion. At the exact degeneracy the top eigenvector is not uniquely defined.

This is a **conditional test of that spectral selector**, not a proof that all possible subject rules are unstable. The actual four-spin C/L rules in [our frozen protocol](SUBJECT_CONSTITUTION_INTERFACE_PROTOCOL.md) are graph rules, not reduced-density-matrix eigenvector rules; this example does not invalidate their finite checks. It identifies an additional admission condition for a *future* quantum spectral constitution rule: demonstrate physically specified subsystem selection, controlled gaps or a stable set-valued/tie treatment, and robustness under measurement error and permitted relabelings. None of those guarantees phenomenal identity.

## 4. What changes for the current programme

1. **Instrument continuum.** The [3+1 refined cutoff](THREE_DIMENSIONAL_REFINED_CUTOFF_CERTIFICATE.md) is a conditional, energy-constrained interaction-channel estimate for a specified field–probe split. If independently validated and completed with its missing apparatus/source/readout errors, it could bound differences in accessible instrument statistics within its domain. It does not by itself prove a particular outcome occurred, recover an unobserved environmental state, determine subjects, or close the fundamental system-split problem.
2. **Quantum consciousness.** The [microtubule gate](MICROTUBULE_QUANTUM_CAUSAL_DISCRIMINATION_GATE.md) requires a particular state, coherence witness and causally selective intervention. Schlosshauer motivates checking its environment and accessible observables; he does not provide a microtubule coherence time or an empirical test of Orch OR.
3. **Intrinsic experience and unity.** A locally diagonal state cannot establish either that experience is intrinsic or that the whole is a universal *subject*. Even evidence for subject-relative definite experiences would still require a justified subject-constitution rule and a defense of experiential rather than neutral grounding; compare [the grounding rivals](EXPERIENTIAL_GROUNDING_RIVAL_BATTERY_GATE.md). Conversely, decoherence does not show that experience is impossible or irrelevant.
4. **Timeless absolute and actuality.** No external environment, fundamental clock, literal simulator or process of turning possibility into actuality is required by this audit. The toy's ordering describes an effective laboratory analysis. Deriving that ordering, the relevant subsystem algebra and the Born weights from the user's timeless whole remains open; a partial trace cannot be used as a substitute for those derivations.

A future candidate should therefore state separately: (i) the accessible algebra and internal complement; (ii) dynamics and pointer-stability condition; (iii) physically or interpretively specified outcome/branch rule; (iv) non-circular subject incidence and experience; and (v) justification of probability weights. A failure at one gate cannot be repaired by relabeling success at another. The formal foundation battery remains incomplete.

## Reproduction and limitations

Run `python verification/decoherence_record_boundary.py`. The [receipt](verification/decoherence_record_boundary.json) checks the product-overlap distinguishability values exactly as rationals and the eigenbasis example numerically. It does not inspect raw experimental data, prove an actual biological environment has those overlaps, establish a subject, or independently validate the inherited continuum certificate. The general expressions follow from the displayed two-dimensional block; finite numerical checks are not proofs of every physical case.
