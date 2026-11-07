# Weak coupling and partial observation: a subject-constitution gate

**Status:** exact finite model, conditional reconstruction bound and a restricted identifiability obstruction. This extends the [factorization and redescription gate](SUBJECT_CONSTITUTION_FACTORIZATION_GATE.md). It does not establish actual subjects, phenomenal unity, a theory of neural systems or a completed framework.

## Result

A system can have a uniquely preferred **approximate physical factorization** even when its components interact. In the specified four-state example below, the factorization `XY` has defect `1/48`, while its alternatives have defects `1/8` and `527/2304`. The result is invariant under transported state redescriptions and remains identifiable under a quantified error budget.

But if only `X` is accessible, three different full-system models—including one with no cross-coupling and one whose preferred factorization is different—give exactly the same `X` observations under every finite adaptive `X`-only intervention policy. That is an obstruction to inferring this hidden structure **from that restricted data**, not a proof that no other measurements could resolve it.

Neither finding tells us how many subjects there are. A postulate equating factors with subjects would still require justification and discriminating experiential evidence.

## 1. Previous work and what is new here

The previous gate introduced an explicitly representation-covariant factorization defect and tested exact independent products. This note extends **that specific gate** to weak coupling, calibrated noisy outputs, a reconstruction margin and an unobserved component. The individual tools—measurement-error models, causal abstraction, concentration bounds and subsystem relativity—are established ideas, not claimed inventions:

- [Massidda et al., *Causal Abstraction with Soft Interventions*](https://proceedings.mlr.press/v213/massidda23a/massidda23a.pdf): state and intervention mappings and the conditions for causal abstraction. Our invertible finite redescription is much simpler, not a general causal-abstraction theorem.
- [Zanardi, *Virtual Quantum Subsystems*](https://doi.org/10.1103/PhysRevLett.87.077901): observables and available physical operations matter to subsystem structure. The present model is classical and does not apply that quantum theorem.
- [NeurIPS work on latent variables with measurement error](https://proceedings.neurips.cc/paper_files/paper/2022/file/05b63fa06784b71aab3939004e0f0a0d-Paper-Conference.pdf): measurement error and hidden causes can limit causal identifiability under specified models. Our small counterexample is an independent illustration, not a replacement for those results.
- [IIT 4.0](https://doi.org/10.1371/journal.pcbi.1011465) and its [intrinsic-unit proposal](https://www.biorxiv.org/content/10.1101/2024.04.12.589163v2.full) use specific intrinsic-causal postulates and grain-selection methods. Our score is **not IIT**, is not an approximation to its `φ` or `Φ`, and does not evaluate IIT.

## 2. Weakly coupled dynamics

For local states `x,y ∈ {0,1}`, set

```
x' = x XOR E_x
 y' = y XOR E_y XOR (C AND x)
P(E_x=1)=1/4, P(E_y=1)=1/3, P(C=1)=1/16,
```

with independent fresh noise variables at each internal update. This is a finite diagnostic, not a biological brain, a simulation hypothesis or an external universal clock. The update order is local to the model.

At fixed `x`, the flip probability of `y` is

```
q_x = 1/3 + x/48.
```

Consequently the `y` flip probability changes by `1/48` when the input `x` is changed, holding the input `y` fixed. This is a directed **one-step** cross-influence in this stipulated kernel. It is not a claim about pain, experience or the strength of a real neural connection.

As in the prior gate, the candidate decompositions are the pairs of balanced binary observables `XY`, `XZ` and `YZ`, where `Z=X XOR Y`. For each pair, the defect `D` is the maximum of (a) the worst one-step total variation distance from the product of the two output marginals and (b) the worst change in a factor's output marginal between inputs that agree on that factor. It therefore measures the model's failure to have conditionally independent, locally autonomous factor transitions. Both terms depend on the specified transition and candidate domain.

Exact rational calculation gives:

| Candidate factors | Defect `D` | Interpretation within this test |
|---|---:|---|
| `X,Y` | `1/48` | Unique smallest defect; **not** exactly independent |
| `X,Z` | `1/8` | Larger defect |
| `Y,Z` | `527/2304` | Larger defect |

The margin between the smallest and the next smallest is `5/48`. The unique-minimum rule identifies a stable approximate decomposition **within this finite candidate set**, not a uniquely privileged ontology in all possible candidate spaces. A continuous score does not decide whether a small connection unifies subjects or whether subjects may overlap.

The verifier checks that all three scores transform correctly under all 24 bijective state redescriptions. As before, candidate observables and any interventions must be transported with their physical meaning: a merely renamed coordinate clamp is not necessarily the same physical operation. We do not require arbitrary mixing transformations to preserve physical locality, cost or operational accessibility unless those features are actually transported and preserved.

## 3. What calibrated partial observation can recover

Suppose the **starting state can be prepared exactly**, but after one update both bits are observed through independent binary readout channels, each flipping its bit with known probability `η=1/8`. This is incomplete/noisy observation, not a fully hidden subsystem. Fresh readout noise is assumed independent of the state, dynamics, preparation and other sensor noise. With state order `00,01,10,11`, let the output channel be `M` and the observed row be `K_s M`.

The channel is invertible. Each one-bit inverse is

```
[ 7/6  −1/6 ]
[−1/6   7/6 ],
```

and `M⁻¹` is their tensor product. Its maximum absolute row sum is `κ=16/9`. Thus noise amplifies reconstruction error. When `η→1/2` for both bits, `κ=(1−2η)⁻²` diverges; at `η=1/2` the channel is singular and this inverse procedure does not apply.

For an observed row estimate within total variation `δ` of `K_s M`, multiply by `M⁻¹` and project the signed result to a nearest probability vector in L1. The script uses positive-part normalization, which is one such projection for a vector summing to one. The true probability row is also in the simplex, so the triangle inequality gives

```
max_s TV(K̂_s, K_s) ≤ ε = 2κδ = (32/9)δ.
```

The factor `2` accounts for the projection. If the known channel is replaced by a separately calibrated `M̂` with maximum row TV error `τ`, then the same argument gives `ε ≤ 2κ̂(δ+τ)` using the inverse norm `κ̂` of the assumed invertible `M̂`; this assumes the calibration error bound applies to the actual readout channel in the test. Unmodeled preparation errors, sensor correlations, drift or state-dependent errors are **not** covered automatically.

The previous gate establishes `|D_K̂(F)−D_K(F)|≤3ε` for every candidate. Hence the minimum remains unique if

```
ε < (5/48)/6 = 5/288.
```

For the cross-influence, the two estimated `y`-flip probabilities can each be wrong by up to `ε`, so the observed difference is certainly nonzero if `ε < (1/48)/2 = 1/96`. The first condition certifies which candidate has least defect; the second certifies this particular nonzero cross-influence. **Neither certifies subjects.**

### An explicit, conservative sampling example

With `M` exactly known, choose `δ=1/512`. Then `ε≤1/144`, satisfying both conditions. If each of the four input states is prepared exactly and independently sampled `n` times, entrywise frequency errors no larger than `1/1024` imply every observed row has TV error at most `1/512`. A Hoeffding union bound over 16 outcome probabilities gives failure probability at most `32 exp(−2n/1024²)`. Thus `n=3,387,671` **per input state** suffices for a 95% bound.

This is a deliberately loose, worst-case sufficient bound, not a recommended experiment or a simulated dataset. It counts neither calibration trials nor preparation, time-correlation, model-selection or readout-system errors. With nonzero calibrated `τ`, the same two conclusions require `δ+τ<3/1024` for the coupling margin and `δ+τ<5/1024` for the factorization margin, when `κ̂=16/9`; the stricter first bound implies both. The code verifies the arithmetic and one exact rational perturbation/reconstruction example, not every perturbation or the empirical validity of the assumptions.

## 4. What a fully hidden component prevents

Now restrict the observer to `X` readout and interventions that clamp `X` or leave it alone; `Y` is never read. Compare three models on the *same formal* state space:

- **A: weak coupling.** The kernel above, with `X→Y` influence `1/48` and least-defect factorization `XY`.
- **B: no coupling.** The same independent `X` and `Y` flip laws with the `C AND x` term removed. Its `X→Y` influence is zero.
- **C: mixed hidden completion.** Conjugate A's kernel by `(x,y)→(x,x XOR y)`, then regard the resulting two coordinates as the candidate model's state variables. Its unique least-defect factorization, expressed in those coordinates, is `XZ`, not `XY`.

For every hidden `y`, all three have the same marginal transition for `x`:

```
P(x' ≠ x | x,y) = 1/4.
```

Consequently, after any allowed `X`-only clamp, the next visible-output law is the same. If a policy selects the next clamp from previous `X` observations, equality of the history distributions follows by induction, for **any finite number of steps**, the same initial visible-state distribution and any hidden-state distributions. Randomized adaptive policies also agree if their action-selection probabilities are the same functions of the observed history. The code independently exhausts the `3^7 = 2,187` deterministic adaptive policies through three transitions for `x₀=0`, with `y₀` uniform. The general induction is an analytic argument; the code does not enumerate infinitely many histories.

Model C illustrates the danger of importing inaccessible labels as if they were physical evidence. Conjugation gives a representation of A, but an `X` clamp that leaves the displayed hidden coordinate fixed in C is **not generally the transported clamp** from A. They are presented here as distinct completions with the same restricted visible interface, not silently declared physically equivalent under all interventions. If `Y` could be manipulated or read, or additional meaningful locality/operation structure were supplied, the completions could be distinguished. Under the specified `X`-only interface they cannot.

This obstruction applies to **physical dynamics before subject attribution**. It is stronger for the present workflow than merely showing that two phenomenal labels can be attached to the same full kernel: the available data may not even identify the factorization to which a subject rule would be applied. Nevertheless it is a deliberately one-way-hidden example, not a universal no-go for latent-variable inference.

## 5. A targeted way to break the hidden-state ambiguity

The full-kernel reconstruction in section 3 is not the only possible approach. Consider a narrower, new interface that makes `Y` *occasionally* observable and can prepare `y=0`, but need not recover the entire transition kernel. Prepare `x=0` in one arm and `x=1` in the other. After one update, suppose the `Y` sensor produces a reading independently with probability `r`; when it reads, it independently flips the true bit with probability `η`. Record `W=1` only if the sensor reads and reports `1`, and `W=0` otherwise; retain the erasure flag separately for calibration.

Under models A and B above, the expected arm difference is respectively

```
A: E[W|x=1] − E[W|x=0] = r(1−2η)/48,
B: E[W|x=1] − E[W|x=0] = 0.
```

For `r=1/4` and `η=1/8`, the contrast is `1/256`. An exactly missing `Y` readout (`r=0`) gives no contrast, as in the restricted-interface obstruction. This calculation requires the same calibrated, state-independent readout rate and error in both arms and no direct intervention effect on the sensor; it does not apply merely because a real detector sometimes returns a value.

With independent trials and the specified A-versus-B distributions, use the difference of the two sample means and a threshold of `1/512`. Hoeffding's inequality bounds either hypothesis's classification error by `exp(−n(1/256)²/4)` with `n` trials per arm. The sufficient `n=967,018` per arm makes each error at most `0.025`. This is an illustrative, highly conservative bound, not an observed result, a minimum required sample size or a human protocol. It assumes reliable `Y` preparation, no hidden cross-cueing or confounding, and correctly calibrated sensor availability/error; it excludes calibration uncertainty and systematic error. A small false contrast due to any of these failures could overwhelm the signal.

This targeted test distinguishes **these two specified physical kernels**, not subjects: both rivals from the previous gate can retain the same report law, and model C is not tested by this A-versus-B calculation. Its value is to exhibit exactly which added access can break one hidden-channel ambiguity and at what idealized cost.

## 6. Consequences for the framework

1. **Do not impose a zero-coupling boundary on subjects.** Weak cross-influence need not erase a stable approximate physical factorization, but the choice of score, candidate class and threshold is substantive and does not establish two subjects.
2. **Separate two types of uncertainty.** Section 3 bounds statistical and calibrated readout error under strong preparation and channel assumptions. Section 4 is structural nonidentifiability even with unlimited `X`-only data. More data of the same restricted kind cannot by itself repair the latter.
3. **Do not derive measure from an arbitrary factorization.** A subject measure requires an independently justified reference class and weighting rule. The most nearly autonomous binary factors in this toy do not supply either.
4. **Carry interventions through redescriptions.** The two displayed hidden completions are indistinguishable only under their specified limited interface; physically important costs, locality and controls could break the apparent symmetry.
5. **Retain the experiential and physics gaps.** Report linkage, subject incidence and persistence, qualitative valence, actual brain dynamics, quantum theory and emergent spacetime are not derived. The entire calculation is compatible with the project's timeless-whole target: local Markov steps are only internal model order, and hypothetical models are not claims about genuinely possible unrealized total worlds.

## 7. Next discriminating gate

A useful next step is to specify a **common-source versus genuine joint-access** experiment with an explicit hidden-channel model, then determine which interventions on a physically plausible network make the rivals' report distributions diverge. Competing subject theories must independently derive those predictions; a joint report is not automatically a joint subject. The design must account for available neural pathways, indirect cues, sensor calibration, no-report and report-error controls, ethical limits, and the difference between access and experience. If the proposed theories have identical observable laws, the outcome must remain **underdetermined**.

The finite quantitative machinery above can help specify a recovery and uncertainty budget, but it cannot substitute for an independently supported subject–experience bridge or for a derivation of actual physics.

## Reproduction

Run `python verification/weak_coupling_partial_observation_gate.py`. It imports the previous standard-library verifier as a module and writes a deterministic [JSON receipt](verification/weak_coupling_partial_observation_gate.json). It checks exact scores, all 24 state bijections, inverse-channel algebra, a particular perturbed recovery, the sampling-bound arithmetic, the targeted partial-readout contrast and 2,187 restricted adaptive policies. The general error inequalities and arbitrary-horizon induction above are proofs, not claims that the script exhausts infinitely many kernels or histories. The frozen [v1 framework](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) is unchanged.
