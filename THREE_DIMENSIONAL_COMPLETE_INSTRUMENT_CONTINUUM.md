# Nonperturbative 3+1 two-field continuum limit: a restricted result

## Result

For the **specific smooth, compactly switched bilinear two-field model** on a fixed 3+1-dimensional spacetime described in [the preceding gate](THREE_DIMENSIONAL_SMOOTH_PROBE_CAUSALITY_GATE.md), the Fourier-cutoff Bogoliubov transformations converge nonperturbatively to a Fock-implementable continuum transformation. After irrelevant cutoff-dependent phases are removed, the implementing unitaries converge strongly. On the common compact-space, positive-mass energy domain, this gives convergence of the **complete field–probe–qubit–record instrument** in energy-constrained trace distance, including arbitrary reference entanglement and each subnormalized record outcome, for both source orders.

The mechanism is not the 1+1 proof's instantaneous Hilbert–Schmidt estimate, which fails in 3+1. Instead, an oscillatory **frequency-sum primitive** of the pair block is Hilbert–Schmidt; integrating the exact finite-cutoff evolution by parts and controlling the remaining bounded one-particle dynamics yields convergence of the full pair block, not merely its first-order term. The convergence result below is qualitative: it does **not** supply a practical cutoff or an explicit finite-N channel error.

The local quadratic probe model and its causal scattering framework are established in [Fewster and Verch](https://arxiv.org/abs/1810.06512). The bosonic Hilbert–Schmidt implementability criterion is established work, discussed for example by [Torre and Varadarajan](https://arxiv.org/abs/hep-th/9811222). This report gives a specific conditional cutoff argument for this model, not a claim to have solved general QFT, quantum gravity or the experiential foundation. The numerical checks are controls, not an independent proof.

## 1. Scope and common setting

Use all definitions of the preceding 3D report: the system and probe are free real Klein–Gordon fields of masses `m_A=.5`, `m_B=.7` on a three-torus of side `2π`, coupled by

```text
H_int(t)=λ χ(t) ∫ F(x) Φ(t,x)Ψ(t,x) dx,
χ(t)=b_a(t−T),  ∫χ=1,
```

where F and χ are real compact smooth functions with the declared spacelike-separated source and interaction supports. The cutoff retains the cube `|k|∞≤N` in both fields and acts as identity on the tail. The source and the later probe-field/qubit/two-bit readout are the smooth operations specified there. The qubit, source control, memory and switching are not a complete relativistic apparatus.

Put every cutoff and the limit on the **same** two-field free Fock space, with normal-ordered `H=H_A+H_B` and arbitrary field–reference input satisfying `Tr(Hρ)≤E`. Positive masses and compact spatial volume matter: H has finite-dimensional spectral subspaces below every finite energy. No claim is made for the earlier massless special-zero-mode dynamics or an infinite-volume energy class.

## 2. The finite-cutoff one-particle evolution

Let `h=h_A⊕h_B` be the complex one-particle space, and write the finite-cutoff interaction-picture Bogoliubov map in doubled form

```text
S_N(t) = [ α_N(t)   β_N(t) ] ,
         [ β̄_N(t)   ᾱ_N(t) ]
Ṡ_N(t) = G_N(t) S_N(t),     S_N(t₀)=I,
G_N(t) = [ A_N(t)   B_N(t) ] .
         [ B̄_N(t)   Ā_N(t) ]
```

Bars denote conjugation in the chosen mode basis; signs and factors of `i` are included in A and B. All equations here are finite-cutoff identities embedded in the full one-particle space. The mixed number-preserving and pair blocks are combinations of `ω_A^(−1/2) F ω_B^(−1/2)` and free phase rotations, multiplied by `λχ/2`. Thus

```text
||G_N(t)|| ≤ c|λχ(t)|,
∫||G_N(t)||dt ≤ L:=c|λ|∫|χ|,       c=||F||∞/√(m_A m_B).
```

The constant is a deliberately loose block-norm bound. Since `ω_X^(−1/2)` is compact on the torus, Fourier projection yields `G_N→G` in operator norm **uniformly** on the compact switching interval, with an `O(N⁻¹/²)` bound for fixed masses and F. Duhamel and Grönwall imply `S_N→S` uniformly in one-particle operator norm and `||S_N(t)||≤e^L`. In particular, `α_N` and its time derivative converge in operator norm uniformly in t. This alone is insufficient for Fock implementation: we also need convergence of `β_N` in Hilbert–Schmidt norm.

## 3. Frequency-sum primitive and full pair-block convergence

For a pair of system/probe modes the instantaneous off-diagonal kernel contains

```text
B_N,kl(t) ∝ λχ(t) F̂(k+l)e^(i[ω_A,k+ω_B,l]t)/(2√(ω_A,kω_B,l)),
```

with both field-species blocks included. This kernel is not uniformly Hilbert–Schmidt in 3D. Define instead, for each block, its oscillatory primitive

```text
C_N,kl(t)= F̂(k+l)e^(i[ω_A,k+ω_B,l]t)
            /[2i√(ω_A,kω_B,l)(ω_A,k+ω_B,l)].
```

The derivative is the corresponding pair kernel without `λχ`. With `V=(2π)³`, `W_F=||F||₂²/V`, and

```text
Z_X(4)=Σ_{k∈Z³} ω_X,k^(−4),
T_X(N,4)=Σ_{|k|∞>N} ω_X,k^(−4),
```

Cauchy–Schwarz and `(ω_A+ω_B)²≥4ω_Aω_B` give, for **one** system/probe block,

```text
||C||₂² ≤ (W_F/16)√(Z_A(4)Z_B(4)),
||C−C_N||₂² ≤ (W_F/16)[√(T_A(N,4)Z_B(4))
                              +√(Z_A(4)T_B(N,4))].              (1)
```

The second species block is its transpose/conjugate and adds at most a factor `√2` to the doubled Hilbert–Schmidt norm. Both bounds are uniform in t. The sums are finite and their tails vanish. For N≥1 one explicit, loose certificate is

```text
Z_X(4) ≤ m_X^(−4)+4π²+π⁴/45,
T_X(N,4) ≤ 24/N+2/(3N³),
```

using `24n²+2` lattice points on the cube shell `|k|∞=n`. Thus the primitive tail is `O(N⁻¹/⁴)` under this majorant. These bounds are for C, **not** for the instantaneous B block.

The exact block equation is

```text
β̇_N=A_Nβ_N+B_N ᾱ_N.
```

At finite N, integrate the second term by parts using `B_N=λχ Ċ_N` (up to the absorbed block signs):

```text
∫_{t₀}^t B_N ᾱ_N
 = λχ(t)C_N(t)ᾱ_N(t)
   −λ∫_{t₀}^t χ'(s) C_N(s)ᾱ_N(s)ds
   −λ∫_{t₀}^t χ(s) C_N(s) ᾱ̇_N(s)ds.                 (2)
```

The initial boundary term vanishes because χ vanishes at `t₀`; the displayed upper boundary also vanishes at the end of the switching interval. Equation (2) is first an identity in the **finite-cutoff** theory: we do not assert that `Ċ` is Hilbert–Schmidt at infinite cutoff.

Using (1), `||α_N||≤e^L`, `||α̇_N(t)||≤c|λχ(t)|e^L`, and the bounded A block gives a uniform finite bound on the Hilbert–Schmidt norm of the integrated term. Grönwall applied to the block equation then gives a uniform `||β_N(t)||₂` bound. Moreover, `C_N` is Cauchy uniformly in Hilbert–Schmidt norm, while `α_N` and `α̇_N` are Cauchy uniformly in operator norm. The right side of (2) is therefore Hilbert–Schmidt Cauchy uniformly in t. In the remaining integral `∫A_Nβ_N`, use convergence of `A_N` in operator norm and the uniform `β_N` Hilbert–Schmidt bound; Grönwall then shows

```text
||β_N(t_f)−β_M(t_f)||₂ → 0  as N,M→∞.
```

This argument is nonperturbative in fixed finite λ. It uses the free one-particle cutoff and the specified smooth switching; it does not assert that every intermediate instantaneous interaction Hamiltonian exists as a Fock operator in 3D.

## 4. Fock implementers and phase-insensitive channel limit

The limiting bounded symplectic transformation S has a Hilbert–Schmidt pair block, so the cited bosonic implementability theorem gives a Fock unitary V implementing it. For finite N choose the phase of the Gaussian implementer V_N so that its vacuum overlap is positive. This phase choice does not change any channel.

For these zero-displacement bosonic Gaussian transformations, the vacuum image is a normalized squeezed vector with Hilbert–Schmidt squeezing parameter Z_N determined continuously by `α_N,β_N`; see the Fock-space canonical-transformation construction of [Kupsch and Banerjee](https://arxiv.org/abs/math-ph/0410049). The symplectic identities and the uniform `||S_N||` bound keep `||Z_N||` strictly below one uniformly. Operator-norm convergence of α and Hilbert–Schmidt convergence of β imply Hilbert–Schmidt convergence of Z; the associated trace-class determinants and normalized squeezed vacua converge. The action on Weyl vectors then gives

```text
phase-adjusted V_N → V strongly,
phase-adjusted V_N† → V† strongly.
```

The adjoint conclusion also follows by applying the same squeezed-vector argument to the inverse symplectic transformations. The phases are not asserted to converge as physically meaningful action phases; channels are phase-insensitive. The limiting one-particle evolution is the Galerkin limit of the local coupled Klein–Gordon equations, so its Weyl scattering transformation is the declared local continuum model.

Let `P_R=1_{H≤R}` and

```text
γ_N(R)=||(phase-adjusted V_N−V)P_R||.
```

`P_R` has finite rank, so strong convergence gives `γ_N(R)→0` for each fixed R. For any field–reference purification with field energy at most E, Markov's inequality bounds the high-energy norm by `√(E/R)`. Consequently

```text
||Ad(V_N)−Ad(V)||_{⋄,E} ≤ min{2, 2γ_N(R)+4√(E/R)}.      (3)
```

Take N→∞ at fixed R and then R→∞. The supremum includes arbitrary references; no finite-dimensional restriction on the reference is used. Equation (3) is a qualitative bound: γ_N is not evaluated here and this work supplies no explicit N-to-error rate for it.

## 5. Complete instruments and both orders

Let `J_N,J` include the interaction, outgoing smooth probe-field/qubit coupling, the measured retained qubit and both noisy record bits. As in the [1+1 proof](TWO_FIELD_COMPLETE_INSTRUMENT_CONTINUUM.md), telescope the readout through **V_N**. That cutoff interaction leaves the high probe modes untouched, so their expected energy remains no greater than the input E even if both fields and a reference were initially entangled. If h is the outgoing readout smear, define

```text
A_N=Σ_{|k|∞>N}|h_kχ̂_r(ω_B,k)|²/ω_B,k²,
T_N=Σ_{|k|∞>N}|h_kχ̂_r(ω_B,k)|²/ω_B,k,
L_N(E)=min{2, 2|η|√(4E A_N+T_N)},
I_N(E;R)=min{2, 2γ_N(R)+4√(E/R)}.
```

Smooth compact smears make `A_N,T_N→0`. No total post-interaction energy bound is used. Then

```text
||J_N−J||_{⋄,E} ≤ min{2, I_N(E;R)+L_N(E)}.              (4)
```

For the source, let

```text
F_N^s=Σ_{|k|∞>N}|f_kχ̂_s(ω_A,k)|²,
G_N^s=Σ_{|k|∞>N}ω_A,k |f_kχ̂_s(ω_A,k)|²,
S_N^s(E)=min{2, 2|g|[√(2E F_N^s)+√(G_N^s/2)]},
E_src=(g²/2)Σ_k ω_A,k²|f_kχ̂_s(ω_A,k)|²,
E⁺=(√E+√E_src)².
```

All source sums have finite limits. Source-first and source-after comparisons satisfy, respectively,

```text
||J_N∘Ad(U_s,N)−J∘Ad(U_s)||_{⋄,E}
 ≤ min{2, S_N^s(E)+I_N(E⁺;R)+L_N(E⁺)},
||Ad(U_s,N)∘J_N−Ad(U_s)∘J||_{⋄,E}
 ≤ min{2, S_N^s(E)+I_N(E;R)+L_N(E)}.                     (5)
```

For the second bound the cutoff instrument leaves the high system modes untouched, so the source-tail estimate uses the original E. Both right sides tend to zero in the stated two-limit sense. Each recorded subnormalized map and the nonselective output inherit the bound by postprocessing; normalized conditional states additionally require a positive outcome-probability lower bound. The selected source and interaction supports are spacelike, so the continuum orders agree by local field causality. This is not a gravitational refoliation argument.

## 6. Controls and remaining limitations

The [verifier](verification/three_dimensional_bogoliubov_continuum.py) checks finite-M primitive Hilbert–Schmidt sums against (1)'s majorants and solves the **full finite-mode**, time-ordered 3D Bogoliubov ODE, checking both canonical identities. For a shared M=2 space, the N=1 and N=2 pair blocks differ in Hilbert–Schmidt norm by about `.1300`; this is a small-cutoff control, not evidence for the infinite limit. At coupling `.02`, the computed squared pair-block norm agrees with the prior first-order expression to about `1.3×10⁻⁷` relative. These computations do not independently establish the functional-analytic argument.

- The result assumes positive masses, compact volume, a free-field Fock representation, the specified smooth coupling/readout and a normal-ordered **total input-energy** bound. It is not an unrestricted diamond-norm result, nor a proof for arbitrary interactions, infinite volume, massless zero modes or the earlier kinetic-only class.
- The qubit, controller, source, record copying/noise/reset, switching work and stress-energy are not physically closed. We do not infer a bound on the full apparatus or geometry from the field-channel convergence.
- The model is fixed-background 3+1 field theory. Dynamical Einstein constraints, self-consistent backreaction and refoliation remain open; no emergent spacetime or temporal ontology is derived.
- Nothing here proves experience, subject individuation, necessary actuality or a complete self-sufficient account. The analytically proposed result merits independent mathematical review; passing the numerical controls is not such a review.
