# A finite-cutoff certificate for the 3+1 two-field instrument

## Result and status

For the compact-volume, positive-mass, smoothly switched 3+1 two-field model in [the nonperturbative continuum report](THREE_DIMENSIONAL_COMPLETE_INSTRUMENT_CONTINUUM.md), the previously qualitative energy-constrained interaction-channel limit can be given an **explicit finite-cutoff upper bound**. The bound applies to arbitrary joint field–reference inputs with a fixed mean total field energy; it extends to both complete source/probe orders, retaining the field, probe, readout qubit and noisy records.

The result is mathematically explicit but **operationally useless at the illustrated parameters**: a deliberately loose interaction-only asymptotic certificate gives a round sufficient cutoff of order `10^729` for unhalved error below `.01` at `E=100`, `λ=1`. This is not a minimum cutoff, a claim that smaller cutoffs fail, or an interval-certified numerical value. It shows how much slack the proof has, not a physical requirement. Source and readout errors are additional.

This is an internal derivation and merits independent mathematical review. Its numerical controls test finite examples, not the infinite-dimensional proof. The cited field–probe framework, bosonic implementability and Bogoliubov/squeezing decompositions are established work, not claimed here as new: see [Fewster–Verch](https://arxiv.org/abs/1810.06512), [Kupsch–Banerjee](https://arxiv.org/abs/math-ph/0410049), and [bosonic quadratic Hamiltonians](https://arxiv.org/abs/1608.03289).

## 1. Inputs and notation

Use the preceding report's two real massive fields on the three-torus `V=(2π)³`, with positive masses `m_A=.5`, `m_B=.7`, normal-ordered total free energy `H`, and smooth spatial coupling F and normalized positive time switch χ. Let `m_*=min(m_A,m_B)`. Both field cutoffs retain `|k|∞≤N`; the rest of the common Fock space is untouched. `V_N` is the exact cutoff interaction-picture unitary. Compare N and any M≥N first; then let M tend to the continuum limit established in the preceding report.

Write the one-particle Bogoliubov blocks as `α_N,β_N`. The total field energy constraint is `Tr(Hρ)≤E`, with arbitrary joint field–reference state; a readout qubit, when included, is prepared independently. Norms below are operator norms, Hilbert–Schmidt norms `||·||₂`, or unhalved output trace norms as indicated.

## 2. Explicit one-particle and pair-block estimates

Use the constants

```text
c=||F||∞/√(m_A m_B),       ν=exp(|λ|c),
h=√2 [(W_F/16)√(Z̄_A Z̄_B)]^(1/2),
W_F=||F||₂²/V,
Z̄_X=m_X^(−4)+4π²+π⁴/45,
t₀=24+2/3,
δ₀=√2 [(W_F/16)(√(t₀ Z̄_B)+√(Z̄_A t₀))]^(1/2),
d₀=||F||∞(m_A^(−1/2)+m_B^(−1/2)),
Q=||χ||∞+||χ'||₁+|λ|c ||χ||₂².
```

The factors `√2` account for both system–probe pair blocks. The shell estimates in the preceding report give a Hilbert–Schmidt bound h for the full frequency-sum primitive and `δ₀ N⁻¹/⁴` for its tail. For all M≥N≥1, the cutoff generator difference has operator norm at most `|λχ(t)| d₀ N⁻¹/²`. Duhamel's formula and `∫χ=1` imply

```text
||S_N−S_M|| ≤ e₀ N⁻¹/²,       e₀=ν|λ|d₀.                 (1)
```

The same bound holds at every time during the switching. As in the preceding report, integrate the exact finite-cutoff pair-block equation by parts using the Hilbert–Schmidt frequency-sum primitive, never assuming that the instantaneous pair kernel is Hilbert–Schmidt. The following are safe, intentionally loose constants:

```text
B_* = |λ| h ν² Q,
I₀  = |λ|[δ₀νQ + h e₀Q + h|λ|d₀ν ||χ||₂²],
dβ₀ = ν[I₀ + |λ|d₀ B_*].
```

The first controls `sup_t ||β_N(t)||₂≤B_*`. For the difference, the three terms in `I₀` control respectively the primitive tail, the α difference, and the generator difference in the differentiated α term. The remaining `A_Nβ_N−A_Mβ_M` contribution is bounded by Grönwall and `B_*`. Since `N⁻¹/²≤N⁻¹/⁴` for N≥1,

```text
||β_N−β_M||₂ ≤ dβ₀ N⁻¹/⁴.                                (2)
```

This holds for fixed finite λ, not as a uniform first-order Taylor expansion in λ. The [bounded-energy counterexample](THREE_DIMENSIONAL_SMOOTH_PROBE_CAUSALITY_GATE.md) remains valid.

## 3. From Bogoliubov coefficients to an energy-constrained channel bound

Form the relative symplectic transformation `S_M⁻¹S_N`, with blocks `α_rel,β_rel`. Since `||S_M⁻¹||≤ν` and the inverse symplectic block formula expresses the pair block using `α_M†(β_N−β_M)` and `β_Mᵀ(α_N−α_M)`, (1)–(2) give

```text
a:=||α_rel−I|| ≤ a₀ N⁻¹/²,         a₀=νe₀,
b:=||β_rel||₂ ≤ b₀ N⁻¹/⁴,          b₀=νdβ₀+B_*e₀.          (3)
```

A standard bosonic Bloch–Messiah/polar decomposition writes an implementer of the relative transformation, up to phase, as a squeeze `exp(G_K)` followed by a number-preserving rotation `Γ(u)`. The singular values of the symmetric squeezing parameter K are `asinh(s_j(β_rel))`, so `||K||₂≤b`. The polar factor obeys

```text
||u−I|| ≤ a+b²/2,
```

using `α_rel†α_rel=I+β_relᵀ β̄_rel` and `√(1+x)−1≤x/2`. On the subspace of at most k total particles, the standard pair creation/annihilation sector estimates and the tensor-product telescoping estimate for `Γ(u)` give

```text
||(exp(G_K)−I)P_{𝒩≤k}|| ≤ b(k+2),
||(Γ(u)−I)P_{𝒩≤k}|| ≤ k(a+b²/2).
```

Thus the relative implementer has the same upper bound after choosing its irrelevant overall phase. No small-squeezing assumption is required; the bound can exceed 2 and is then capped at the channel maximum.

For `P_R=1_{H≤R}`, `H≥m_*𝒩`, so take `k=floor(R/m_*)`. A purified field–reference state of mean energy ≤E has high-energy vector norm at most `√(E/R)`. The low-energy operator estimate and a trace-distance bound yield

```text
||Ad(V_N)−Ad(V_M)||_{⋄,E}
 ≤ min{2, 2[b(k+2)+k(a+b²/2)] + 4√(E/R)}.                 (4)
```

All bounds are uniform in M≥N and in the reference system. Letting M→∞ gives the same bound for the continuum channel. The energy projection also explains why the result is compatible with the prior example whose **linear** coupling derivative is unbounded at fixed mean energy.

For a simpler, weaker closed form choose `R=N^(1/6)`. Then `k≤N^(1/6)/m_*`, and (3)–(4) imply

```text
||Ad(V_N)−Ad(V)||_{⋄,E} ≤ min{2, C(E) N⁻¹/¹²},
C(E)=2[b₀(1/m_*+2)+a₀/m_*+b₀²/(2m_*)]+4√E.              (5)
```

The fractional powers use the model's dimensionless energy units. This weak polynomial is a sufficient estimate, not an optimal convergence rate. It does not assert unrestricted diamond-norm convergence.

## 4. Complete instrument and source orders

Let `D_N(E)` be either (4) optimized over any chosen `R>0` or the explicit bound (5). The outgoing smooth probe readout has the earlier tail bound

```text
L_N(E)=min{2, 2|η|√(4E A_N+T_N)},
A_N=Σ_{|k|∞>N}|h_kχ̂_r(ω_B,k)|²/ω_B,k²,
T_N=Σ_{|k|∞>N}|h_kχ̂_r(ω_B,k)|²/ω_B,k.
```

The cutoff interaction leaves the probe tail untouched, so the estimate can be applied at the original input E without assuming total energy is preserved by the interaction. The complete readout is a common CPTP postprocessing; therefore `||J_N−J||_{⋄,E}≤min{2,D_N(E)+L_N(E)}`.

For the source define the previous report's explicit source-tail bound `S_N^s(E)` and post-source energy bound `E⁺`. The complete source-first and source-after cutoff-to-continuum errors are bounded respectively by

```text
min{2, S_N^s(E)+D_N(E⁺)+L_N(E⁺)},
min{2, S_N^s(E)+D_N(E)+L_N(E)}.
```

For the second line the cutoff instrument leaves the high **system** modes untouched, so its source-tail estimate uses E. All four subnormalized outcomes and the nonselective field output inherit these bounds; normalized conditional outputs still need a nonzero probability lower bound. The continuum operations commute for the stated spacelike supports by the established local field causality result, not because of the finite cutoff.

## 5. Controls and limitations

The [verifier](verification/three_dimensional_quantitative_channel.py) calculates the constants, checks the polar squeeze/rotation estimate against independent finite-Fock matrices at two oscillator truncations, and runs a shared-M finite 3D Bogoliubov comparison. At weak coupling `.001`, N=1 and M=2, its computed relative pair-block norm is about `.000130` versus the analytic upper bound `.01445`; the vacuum trace distance is about `.000184` versus `.05778`. These are selected **finite** numerical controls, not a proof for all states or the continuum.

For `E=100, λ=1`, the floating-point estimate for the coefficient in (5) is about `5.25×10^58`; a round `N=10^729` yields an interaction-only upper bound around `.00934`. The exact analytic statement uses the true bump norms and constants; the numerical evaluation is not interval-certified. The source/readout tails and any physically meaningful energy budget are not included in that illustrative interaction-only number.

The new certificate depends on a compact spatial torus, positive masses, the smooth quadratic coupling, the selected free Fock representation and a total **input** energy bound. It does not cover the earlier kinetic-only/massless-zero-mode class, infinite-volume uniformity, arbitrary interactions, physically autonomous record hardware, switching work, local stress-energy, gravity, refoliation, emergent spacetime, experience, or necessary actuality. It should be externally audited before being treated as a settled mathematical result.
