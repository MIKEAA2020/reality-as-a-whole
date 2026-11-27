# Clock-preparation and correlation robustness

## Result and scope

For the *specified* second-clock/cursor setup, the [fiber-transport analysis](ZERO_CLOCK_FIBER_TRANSPORT_AND_LOST_RECORD.md) gives an exact reduced instrument only after a chosen fiber identification, with the clock prepared independently. The [centered-smearing review](ZERO_SECOND_CLOCK_POVM_TAIL_AND_SMEARING_RIGOR_REVIEW.md) bounds the resulting ideal comparison by `<0.03777` in half-diamond norm for its specific pure clock state β.

This pass gives explicit perturbation guarantees and a counterexample:

1. For any **independently prepared** clock state γ with `D(γ,β)≤ε`, the same specified reduced instrument stays within `0.03777+ε` in half-diamond norm of the prior ideal instrument (capped at 1). No symmetry or centering of γ is required.
2. For a **correlated** system–reference–clock input, the comparison is state-specific: it is bounded by `0.03777+κ`, where `κ=D(ρ_SXR,ρ_SX⊗β)`. This is not a diamond-norm claim for a channel on S alone.
3. Because β is pure, a clock marginal with `D(ρ_R,β)≤ε` does constrain such correlations, but generally at **square-root**, not linear, order. A covariant finite-clock control produces a `√[ε(1−ε)]` event-probability shift although the clock marginal is only ε away from β.

D denotes half the trace norm. These guarantees assume the same fixed apparatus Hamiltonian, ready ancillas, chosen orbit-dilation instrument and fiber reduction as the earlier construction. They do not certify a real device, arbitrary implementation perturbations, a physical R-relative switch, whole-level zero energy, subjects or felt succession. The present programme treats space and time as non-fundamental constructs and experience as intrinsic.

## 1. Rechecking the fiber and correlated-input identity

Let `U(t)=U_A(t)⊗U_R(t)`, `A_m=Π_m⊗√E_R(B)`, `K_m(t)=ℓ^−1/2 U(t)†A_mU(t)`. The POVM normalization already checked in the [second-clock review](ZERO_SECOND_CLOCK_POVM_TAIL_AND_SMEARING_RIGOR_REVIEW.md) gives `Σ_m∫K_m(t)†K_m(t)dt=I` weakly. Thus `Vψ={K_m(t)ψ}_{m,t}` is an isometry into the direct-integral orbit-label space. The decomposable multiplication `D:{f(t)↦U(t)f(t)}` is unitary there, and

```text
(DVψ)_m(t)=ℓ^−1/2 A_m U(t)ψ
```

holds in the direct-integral Hilbert space, including an untouched reference X. This is an identity for **one chosen dilation** and its transported observables; D is controlled by a mathematical label, not a demonstrated accessible physical feed-forward.

For any input `ρ_AXR` define

```text
E_t=U_R(t)†E_R(B)U_R(t),
α_t=ℓ^−1 Tr_R[(I_AX⊗√E_t)ρ_AXR(I_AX⊗√E_t)].
```

The α_t are positive, subnormalized trace-class operators and `∫Tr α_t dt=1`. After D, recording m and tracing R and the orbit label, partial-trace cyclicity gives the exact transported operation

```text
S_m(ρ_AXR)=∫ dt (Π_m⊗I_X)(U_A(t)⊗I_X) α_t
                        (U_A(t)†⊗I_X)(Π_m⊗I_X).
```

For the product `ρ_AX⊗β`, `α_t=q_β(t)ρ_AX`, recovering the earlier scalar-smeared instrument. With correlations, α_t generally changes its *normalized* apparatus/reference state with t, so a single ρ_AX and scalar kernel cannot be silently substituted. Ancillas are subsequently traced exactly as in the selected output convention. The continuum identity is an operator argument; the [finite cyclic tests](verification/zero_clock_preparation_robustness_test.py) are controls, not a simulation of the massive-cursor continuum.

## 2. Independent imperfect clock: a channel-level bound

For any clock density γ, the orbit-clock POVM

```text
G(dt)=ℓ^−1 U_R(t)†E_R(B)U_R(t) dt
```

is normalized in the weak sense. It induces the probability distribution `q_γ(dt)=Tr[γG(dt)]`. Measurement contractivity gives

```text
TV(q_γ,q_β) ≤ D(γ,β) ≤ ε.
```

With a clock independently prepared from the complete S–X input and the same fixed ready ancillas, both transported reduced instruments are mixtures of the *same* scalar-slice instruments with these two kernels. Complete-channel contractivity, equivalently the total-variation bound on the mixture, yields

```text
(1/2)||C_J,γ−C_J,β||_diamond ≤ ε,
(1/2)||C_J,γ−C_L(r)||_diamond ≤ min(1, 0.03777+ε).
```

The baseline term is strict below 0.03777; the capped statement is written non-strictly. This holds for a mixed, biased or asymmetric γ, without incorrectly reusing the centered-kernel cancellation for it. It includes arbitrary input/reference entanglement but **not** correlations with R or changes to the physical instrument, coupling, bin or ancilla preparation. A bound on ε is a trace-distance preparation assumption; finitely many calibration trials do not automatically establish it.

## 3. Correlated inputs: joint-distance and pure-marginal bounds

Include the fixed ready ancillas in the mathematical input convention. The chosen isometry, fiber unitary, classical outcome readout and partial traces together define a CPTP map Λ from S–X–R inputs to the recorded S–X output. For any correlated `ρ_SXR`, let `ρ_SX=Tr_R ρ_SXR` and

```text
κ=D(ρ_SXR,ρ_SX⊗β).
```

Contractivity and the known product-state comparison give

```text
D(Λ(ρ_SXR), (C_L(r)⊗id_X)(ρ_SX))
    ≤ min(1, κ+0.03777).
```

This compares the same system–reference marginal, with all memory outcomes retained. It is a **state-dependent** statement: correlated inputs do not define a channel on the system marginal alone. For a marginal supported in P or Q, the earlier sector-specific false/missed record bound similarly becomes at most `min(1,κ+0.0003416)` for the specified memory event. Correlations with X are included; errors in fixed cursor/flag/memory preparation or in Λ itself require an additional independently justified term.

There is also a bound using the clock marginal alone **because β is pure**. Suppose `D(ρ_R,β)≤ε` and set `P=I_SX⊗β`, `p=Tr(Pρ)=1−q`. The two-outcome measurement `{P,I−P}` gives `q≤ε`. In the `β⊕β⊥` block decomposition,

```text
ρ = [[A,C],[C†,B]],        Tr A=p,  Tr B=q,
ρ_SX = A + Tr_R B.
```

Positivity factors `C=A^(1/2) K B^(1/2)` with `||K||≤1`, so `||C||₁≤√[q(1−q)]`. The block-diagonal difference from `ρ_SX⊗β` has trace norm `2q`, and the off-diagonal part has trace norm `2||C||₁`; hence

```text
κ ≤ q+√[q(1−q)].
```

For `0≤ε≤1/2`, this is at most `ε+√[ε(1−ε)]`. A second bound holds throughout `0≤ε≤1`: let `τ=⟨β|ρ|β⟩≤ρ_SX`. The root fidelity satisfies

```text
F_root(ρ,ρ_SX⊗β)
 = Tr √(√τ ρ_SX √τ) ≥ Tr τ = p,
κ ≤ √(1−p²) ≤ √(2ε−ε²).
```

The first inequality uses operator monotonicity of square root; the second is the fidelity–trace-distance inequality. Accordingly one may use

```text
B(ε)=min{√(2ε−ε²), ε+√[ε(1−ε)]},     0≤ε≤1/2,
B(ε)=√(2ε−ε²),                            1/2<ε≤1,
κ≤B(ε).
```

In particular ε=0 forces an exactly pure clock marginal and hence an exact product with S–X. For small ε the bounds scale as `O(√ε)`, so a linear `κ≤ε` claim is not justified from clock marginal closeness alone. These are upper bounds, not an assertion that they are globally optimal.

## 4. Explicit covariant finite-clock counterexamples

The independent [test](verification/zero_clock_preparation_robustness_test.py) uses a two-step cyclic clock, **not** the continuous positive-frequency clock. Let `U_A=Z`, `U_R=Z`, clock-bin effect `E=|+⟩⟨+|` and memory projector `Π₀=|+⟩⟨+|`. The normalized two-term orbit effect is

```text
F₀=|++⟩⟨++|+|−−⟩⟨−−|=(I+X⊗X)/2,
[F₀,Z⊗Z]=0.
```

First, `ρ_AR=(|++⟩⟨++|+|−−⟩⟨−−|)/2` and `(I/2)⊗(I/2)` have identical apparatus and clock marginals, yet F₀ has probabilities 1 and 1/2. Thus separate marginals alone do not fix a relational effect in general.

Second, let `β=|0⟩⟨0|` and `|ψ⟩=√(1−ε)|00⟩+√ε|11⟩`. The actual clock marginal is ε away from β, and its apparatus marginal is diagonal. Nevertheless

```text
Tr(F₀|ψ⟩⟨ψ|) − Tr[F₀(ρ_A⊗β)] = √[ε(1−ε)].
```

At ε=0.04 the difference is about 0.196, exceeding ε. This establishes that generic correlated, covariant effect comparisons cannot be controlled linearly by pure-clock marginal trace distance alone. It does not prove the exact same shift for the specified continuum cursor instrument or that such a preparation occurs physically.

## 5. Verification and remaining work

The tests check the fiber/cyclic identities, matching marginals with different probabilities, the square-root witness, independent-clock total-variation contraction and many finite mixed correlated states against B(ε), including a reference factor. The inequalities above are analytic; finite sampling does not prove them for every infinite-dimensional input.

The actionable next step is to justify or measure joint preparation error, not merely clock fidelity, and to analyze controlled clock–apparatus interactions and locality on the same physical carrier. The abstract fiber identity, added clock, extreme cursor parameters and internal records do not establish a physical clock switch, a universal subject or a complete zero/experience constitution.
