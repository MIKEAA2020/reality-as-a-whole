# Modular flow, real-space RG and instruments in one Ising model

## Why this addresses the source leads

The source's A5 and G5 suggest a modular–renormalization connection; P3 proposes an update/coarse-graining unification. The earlier [formalization recheck](CLAUDE_TIME_FORMALIZATION_RIGOR_RECHECK.md) gave a useful dephasing control but explicitly did **not** calculate an RG transformation. Here the **same interacting thermal spin system** supplies an exact real-space RG step, two modular flows, a state-preserving quantum coarse map and competing instruments.

The result is constructive in both directions. Real-space decimation and its coupling flow are calculated exactly, and a specified state-preserving coarse map becomes approximately modular-compatible at high temperature for bounded modular parameters. But neither the natural embedding nor that coarse map intertwines the two modular flows exactly for any positive coupling. The purely classical observable algebra has trivial modular flow even while its RG coupling changes. Moreover, the same unselected decimation channel can arise from different instruments with different conditional states.

This is a finite lattice statistical-mechanics model and an exact one-dimensional Ising RG, **not** the regulated interacting continuum QFT/beta-function calculation requested as the full A5/G5 target. It does not establish a universal obstruction to every possible modular/RG map, a physical clock, gravity, intrinsic experience, or zero energy. Space and thermodynamic temperature are inputs of this effective diagnostic, not asserted fundamental properties of the current programme.

## 1. Exact decimation and an independently checked scale law

Take three qubits labeled 1,2,3, open boundaries, finite inverse temperature `β_th>0`, and

```text
H_phys=−J(Z₁Z₂+Z₂Z₃),    J>0,     K=β_th J,
ρ₁₂₃ = exp[K(Z₁Z₂+Z₂Z₃)]/Tr exp[K(Z₁Z₂+Z₂Z₃)].
```

The Hamiltonian is diagonal, but the **full quantum observable algebra** is `M₈(C)`, not only its diagonal classical subalgebra. We retain spins 1,3 and trace out spin 2. For `z_i=±1`, summing the middle spin gives

```text
Σ_(z₂=±1) exp[K z₂(z₁+z₃)]
   = 2 sqrt(cosh 2K) exp[K' z₁z₃],
K' = (1/2) log cosh(2K),
ρ₁₃ = exp(K' Z₁Z₃)/(4 cosh K').
```

This is the standard exact decimation of a 1D zero-field nearest-neighbor Ising chain; the open three-spin calculation includes the normalization explicitly. Repeating the same local sum on alternating sites of a longer even chain gives the factor-two blocking rule. Independently, the classical transfer matrix has eigenvalues `2 cosh K` and `2 sinh K`, so its eigenvalue ratio is `tanh K`. The spacing-doubled correlations require

```text
tanh K' = (tanh K)²,
```

which reproduces the same K'. At every finite `K>0`, `0<K'<K`: this is a genuine nontrivial scale transformation, not a dephasing channel relabeled as RG.

For a continuous **mathematical interpolation** of this discrete semigroup, set scale label `ℓ=log b` and

```text
K(ℓ) = artanh[(tanh K₀)^(exp ℓ)],
β_RG(K) = dK/dℓ = sinh K cosh K log(tanh K) < 0   (K>0).
```

At `ℓ=log 2` the rule is exactly K'; integer blocking factors also match. Noninteger blocking and the continuous beta function depend on this chosen interpolation; they are not uniquely derived physical lattice operations. The scale label ℓ is not modular parameter s, laboratory time or experienced time. No continuum-field or gravitational beta function is inferred.

## 2. The natural embedding fails to intertwine modular flows

Use the faithful finite-state convention

```text
σ_s^ρ(A)=ρ^(is) A ρ^(−is),
L_ρ(A) = dσ_s^ρ(A)/ds |_(s=0) = −i[−log ρ,A].
```

On the full and reduced systems `−logρ` is respectively `−K(Z₁Z₂+Z₂Z₃)+constant` and `−K' Z₁Z₃+constant`. Embed a retained observable into the full system by `ι(A₁₃)=A₁₃⊗I₂`, with tensor indices placed in their physical order. For `X₁`,

```text
L_ρ(ι(X₁))       = −2K Y₁Z₂,
ι(L_ρ₁₃(X₁))     = −2K' Y₁Z₃,
||L_ρ(ι(X₁)) − ι(L_ρ₁₃(X₁))|| = 2(K+K') > 0.
```

The norm uses the full three-spin algebra; `Z₂` and `Z₃` commute and have independent ± eigenvalues. Consequently the natural embedding cannot intertwine these two modular automorphism groups for all s unless `K=0`. The reduced coupling links the retained sites across the eliminated middle site; it is nearest-neighbor on the *coarse lattice*, not a proof of continuum nonlocality or of an area law. This is one finite example relevant to A2's locality question, not a general non-wedge modular-locality theorem.

On the diagonal **classical** subalgebra, by contrast, both modular flows are pointwise the identity because the Gibbs states commute with every observable there. Yet K changes to K'. Thus, in this explicit algebra, nontrivial RG cannot be identified with a nontrivial modular automorphism. That observation does not exclude a different algebra, state family, noncommutative blocking or additional map.

## 3. Even a state-preserving CP coarse map has a controlled mismatch

A natural state-dependent coarse map from full observables to retained observables is

```text
R_ρ(A) = ρ₁₃^(−1/2) Tr₂[ρ₁₂₃^(1/2) A ρ₁₂₃^(1/2)] ρ₁₃^(−1/2).
```

All states here are full rank. The map is completely positive, unital and state-preserving in the sense `Tr(ρ₁₃ R_ρ(A))=Tr(ρ₁₂₃ A)`. It is a chosen Petz-type/weighted coarse map, not the unique physical RG channel. It need not be a left inverse to the embedding on noncommuting observables.

For `X₁` and `Y₁Z₂`, direct evaluation gives

```text
c = cosh K / sqrt(cosh 2K),     d = sinh K / sqrt(cosh 2K),
R_ρ(X₁) = c X₁,                R_ρ(Y₁Z₂) = d Y₁Z₃.
```

Comparing maps with the **same types** `M₈→M₄`,

```text
[R_ρ L_ρ − L_ρ₁₃ R_ρ](X₁)
  = −2(Kd−K'c)Y₁Z₃,
||[R_ρ L_ρ − L_ρ₁₃ R_ρ](X₁)||
  = 2c [K tanh K − (1/2)log cosh(2K)].
```

The bracket is strictly positive for `K>0`. Its derivative is

```text
sech²K · [K−tanh K/(1+tanh²K)] > 0,
```

and it vanishes at K=0. Hence this specified state-preserving map fails exact modular intertwining at every positive K. At K=1/2 the infinitesimal operator-norm defect is about `0.0257225671` in dimensionless modular-parameter units. This does not prove that some other physically motivated map cannot work.

The complete finite-s expression makes the approximation and its limits explicit:

```text
R_ρ(σ_s^ρ(X₁)) − σ_s^ρ₁₃(R_ρ(X₁)) = a(s)X₁+b(s)Y₁Z₃,
a(s)=c[cos(2Ks)−cos(2K's)],
b(s)=−d sin(2Ks)+c sin(2K's),
||difference||=sqrt[a(s)²+b(s)²].
```

Even allowing a constant linear reparameterization `s↦q s` of the reduced flow does not make this map intertwine for all s. Equality of the X coefficient forces `qK'=±K`; equality of the YZ coefficient would then require `d=±c` with the corresponding sign, impossible at finite positive K. Choosing `q=K tanh K/K'` can cancel the first derivative on this one observable, but the finite-s functions still differ. This does not exclude arbitrary nonlinear, observable-dependent or entirely different physical constructions.

The Pauli terms anticommute and square to I. For fixed bounded s the difference tends to zero as K→0; the derivative defect is `(2/3)K⁴+O(K⁶)`. This is a **conditional high-temperature approximate compatibility**, not a clock derivation. Convergence is not uniform over all s: taking `s=π/(2K)` makes the norm tend to 2 as `K→0+`. The large-s choice itself diverges, so it does not contradict the bounded-s limit.

## 4. Decimation is not a unique selective update

On the same three-spin system, define two instruments whose output is the retained spins:

```text
I^Z_±(τ)=Tr₂[(I₁⊗P^Z_±⊗I₃) τ (I₁⊗P^Z_±⊗I₃)],
I^X_±(τ)=Tr₂[(I₁⊗P^X_±⊗I₃) τ (I₁⊗P^X_±⊗I₃)].
```

For **every** input τ, summing either instrument over its outcomes gives the same channel `Tr₂ τ`. Thus unselected decimation alone does not select a particular outcome or determine a recorded poststate. On the Ising ρ, each ± outcome has probability 1/2, but

```text
⟨Z₁⟩ conditioned on middle Z=+1 = tanh K,
⟨Z₁⟩ conditioned on middle X=+1 = 0.
```

The different selected instruments can therefore have different subsequent predictions even though both have the same unselected physical coarse-graining. They are different measurement implementations, not an assertion that discarding a spin is itself a selective collapse. This advances P3's **typed comparison** within the same model, but does not unify physical collapse with Wilsonian RG, settle definite outcomes, or make a record an experience.

## 5. What remains for the actual research programme

- **A5/G5:** specify a regulated field theory and independently defined scale and modular observables; establish appropriate domains and compare maps, beta functions and controlled continuum limits. The Ising example gives a known, calculable diagnostic and a candidate approximate regime, not the requested full QFT result.
- **A2:** compare modular generators for a specified non-wedge region in a field model; coarse-lattice adjacency here does not establish general modular locality or entropy-area laws.
- **P3:** identify the relevant update/instrument and physical coarse-graining in a shared model and compare all outputs. Matching unselected states does not fix conditional dynamics or a phenomenological outcome.
- **Time and the zero framework:** derive physical clock calibration, emergent geometry and any relation to the objective whole-energy separately. A Gibbs parameter and dimensionless modular flow were inputs; neither supplies intrinsic experience, a universal subject, or a replacement for internally experienced succession.

## Verification

[Tests](verification/claude_time_ising_modular_rg_review_test.py) independently check the decimation against the transfer matrix, the interpolated beta function, both modular comparisons, complete positivity via explicit Kraus operators, the exact finite-s formula and its nonuniform limit, and the two instruments. Their scope is the finite model; they do not prove the broader physical or experiential programme.
