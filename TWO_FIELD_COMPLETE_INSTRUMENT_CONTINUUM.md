# Complete continuum limit for the restricted two-field probe

**Subsequent dimensional test:** [the 3+1 smooth-probe gate](THREE_DIMENSIONAL_SMOOTH_PROBE_CAUSALITY_GATE.md) obtains a complete finite-cutoff order bound and a finite time-integrated first-order pair kernel, but not a full 3+1 cutoff-to-continuum instrument limit.

## Result

For the specific **1+1-dimensional massive two-field model** in [the local probe report](LOCAL_TWO_FIELD_PROBE_AND_CUTOFF_ORDER.md), there is a common-Fock-space cutoff-to-continuum bound for the **complete field–probe–qubit–record instrument**, including arbitrary reference entanglement and all four subnormalized recorded outcomes. It applies to both source/readout orders under one normal-ordered total input-energy constraint. This goes beyond the previous bound, which compared only the two orders at the same cutoff.

The calculation combines standard bosonic quadratic-operator estimates, a low-energy truncation argument, and the established local field–probe construction of [Fewster and Verch](https://arxiv.org/abs/1810.06512). Energy-constrained channel metrics are established prior work; see [Shirokov](https://arxiv.org/abs/1706.00361) and [Winter](https://arxiv.org/abs/1712.10267). The quantitative specialization and the treatment of this particular cutoff/readout are the contribution here; no claim is made that these general methods are new.

The bound is deliberately very conservative. It is not a physically useful cutoff prescription. This is a restricted model result, **not** a complete physical apparatus, 3+1-dimensional QFT result, gravity/refoliation theorem, or solution of the experiential foundation.

## 1. Common space and operations

Use the full real sine-and-cosine Fock spaces of two free scalar fields on a circle of circumference `2π`, with masses `m_A=.5`, `m_B=.7`. The positive normal-ordered free energy is

```text
H=H_A+H_B=Σ_{k∈Z} ω_A,k a_k†a_k + Σ_{k∈Z} ω_B,k b_k†b_k,
ω_A,k=√(k²+m_A²),    ω_B,k=√(k²+m_B²),    m_*=min(m_A,m_B).
```

This complex Fourier notation is equivalent to the real-mode calculation in the companion verifier. The two fields may be arbitrarily entangled with each other and with any reference. The initial field marginal satisfies `Tr(Hρ)≤E`. A fresh readout qubit is separately prepared in `|0_z>`.

The source, compact smooth interaction, and outgoing probe readout use exactly the smears and switching profiles in [the preceding report](LOCAL_TWO_FIELD_PROBE_AND_CUTOFF_ORDER.md):

```text
H_int(t)=λ χ(t) ∫F(x) Φ(t,x) Ψ(t,x) dx,
χ(t)=b_a(t−T),  F(x)=F_d(x−y),
```

with `∫χ=1`, `d=.4`, `a=.08`, `y=π/2`, `T=.3`. Here `F_d` and `b_a` are normalized nonnegative compact `C∞` bumps. At cutoff N each field is projected onto `|k|≤N`, and the resulting interaction acts as identity on the untouched tail. Let `V_N` be the exact finite-mode time-ordered interaction-picture unitary, embedded into the **same infinite Fock space**. The readout qubit couples with strength `η` to the outgoing probe field smeared with a separate smooth compact bump, then is measured and copied to two classically noisy bits as before. The field, probe, measured qubit and record bits are retained.

The continuum operation will be defined as a strong unitary limit of the `V_N`; its identification with the standard local coupled-field scattering operation is justified in Section 3. No Fourier tail is reset to vacuum or discarded.

## 2. A uniform interaction-channel estimate

Set

```text
F̂(p)=(1/(2π))∫F(x)e^(−ipx)dx,
W_F=Σ_p |F̂(p)|²=||F||₂²/(2π),
W_A=Σ_k 1/(k²+m_A²)=π coth(πm_A)/m_A,
W_B=Σ_k 1/(k²+m_B²)=π coth(πm_B)/m_B,
κ̄²=(W_F/4) √(W_A W_B),
δ̄_N²=(W_F/4)[√(2W_B/N)+√(2W_A/N)],  N≥1.
```

Expansion of the smeared field product gives four bilinear creation/annihilation kernels. Their entries have magnitude `|F̂(k±l)|/(2√(ω_A,k ω_B,l))`; they are Hilbert–Schmidt in 1+1 dimensions. Cauchy–Schwarz over the mode index gives `κ̄` as a uniform upper bound on each full kernel's Hilbert–Schmidt norm. For the kernel tail where either `|k|>N` or `|l|>N`, the same inequality and `Σ_{|k|>N}1/(k²+m²)≤2/N` give the upper bound `δ̄_N`. Thus `δ̄_N=O(N⁻¹/⁴)`; this is a deliberately weak bound, not the actual observed rate.

Let `𝒩=𝒩_A+𝒩_B`. On the finite-particle core, the usual sectorwise Hilbert–Schmidt estimates for pairs of creation/annihilation operators imply the deliberately loose bounds

```text
||(H_int,M(t)−H_int,N(t))ψ||
    ≤ 4 |λχ(t)| δ̄_N ||(𝒩+2)ψ||,            M≥N,
||[𝒩,H_int,N(t)]ψ||
    ≤ 4 |λχ(t)| κ̄ ||(𝒩+2)ψ||.
```

The first holds uniformly in M. The second and Grönwall's inequality give, uniformly in N and time during the coupling,

```text
||(𝒩+2)V_N(t)ψ|| ≤ exp(4|λ|κ̄) ||(𝒩+2)ψ||.
```

These estimates are first applied to finite-particle vectors and extended by closure; finite-mode quadratic Hamiltonians and their time-dependent evolutions have the usual invariant number-operator domains. Duhamel's formula then makes the `V_N` a Cauchy sequence on that core. The same estimate for the adjoint evolutions gives a **unitary** strong limit `V`, not merely an isometric limit.

To obtain a uniform energy-constrained channel bound, project a purified field–reference input on `H≤R` and its complement. Since `H≥m_*𝒩`, the low-energy vector obeys `||(𝒩+2)ψ_low||≤(R/m_*+2)||ψ_low||`; Markov's inequality gives `||ψ_high||≤√(E/R)`. The unitary difference is at most 2 on the high-energy part. Duhamel and the pure-state trace-distance estimate then give, for any `R>0`,

```text
||Ad(V_N)−Ad(V)||_{⋄,E} ≤ I_N(E;R),
I_N(E;R) := min{2,
  8|λ|exp(4|λ|κ̄) δ̄_N (R/m_*+2) + 4√(E/R)}.     (1)
```

The untouched reference is included throughout. For fixed E, take `R=δ̄_N^(−2/3)` when the tail is nonzero: (1) goes to zero. The displayed analytic majorant gives a very conservative `O(N⁻¹/¹²)` rate for E>0. Optimizing R may improve constants but does not make this a practical cutoff requirement. At E=0 one can instead take R arbitrarily small in (1).

## 3. Relation to the continuum local field model

The strong limit above is constructed on the two-field free Fock space, not asserted from numerical data. The finite-mode Heisenberg transformations are the Galerkin solutions of the coupled linear Klein–Gordon equations. In the classical free-energy norm the compact smooth multiplication `F(x)` is bounded, the Fourier projectors converge strongly, and a Duhamel/Grönwall argument gives strong convergence of these Galerkin solutions to the unique local coupled-field solution. Thus the limiting unitary implements the same scattering transformation on the field Weyl algebra, up to an irrelevant scalar phase.

This identifies the limiting **channel** with the specified local two-field scattering model; it does not re-prove the general Fewster–Verch framework. Their continuum causal-factorization theorem and finite propagation imply that the chosen source and interaction, whose spacetime supports are strictly spacelike, commute. The readout acts on the outgoing probe and qubit only, so the two continuum complete ordered instruments coincide for this selected pair. Fixed N can still exhibit regulator leakage.

## 4. Complete readout and both source orders

Write `h_j` for the outgoing probe's spatial readout coefficients, `χ̂_r` for its normalized smooth switching transform and `ω_B,j` for probe frequencies. With the entire field and probe retained, the readout-tail bound is

```text
A_N=Σ_{|j|>N} |h_jχ̂_r(ω_B,j)|²/ω_B,j²,
T_N=Σ_{|j|>N} |h_jχ̂_r(ω_B,j)|²/ω_B,j,
L_N(E)=min{2, 2|η|√(4E A_N+T_N)}.
```

To compare the readouts, telescope through the **cutoff** interaction `V_N`, not through the continuum interaction. `V_N` acts only on modes `|j|≤N`, so it leaves the probe tail Hamiltonian and its expected energy unchanged, even with arbitrary initial entanglement. The readout-tail estimate is therefore applied with the original E; no unproved bound on the total energy after the interacting continuum operation is needed. Including the common qubit measurement and record postprocessing,

```text
||J_N−J||_{⋄,E} ≤ min{2, I_N(E;R)+L_N(E)}.       (2)
```

For an explicit elementary readout majorant, let `L₁=||F_d'||₁`. The normalized positive time switching has `|χ̂_r|≤1`, and Fourier integration by parts yields

```text
A_N ≤ L₁²/(3πN³),       T_N ≤ L₁²/(2πN²).
```

These bounds include both positive and negative Fourier indices.

The source is the smooth system-momentum source of the preceding report. For its spatial coefficients `f_j` and time transform `χ̂_s`, set

```text
F_N^s=Σ_{|j|>N}|f_jχ̂_s(ω_A,j)|²,
G_N^s=Σ_{|j|>N}ω_A,j |f_jχ̂_s(ω_A,j)|²,
S_N(E)=min{2, 2|g|[√(2E F_N^s)+√(G_N^s/2)]},
E_src=(g²/2)Σ_j ω_A,j² |f_jχ̂_s(ω_A,j)|²,
E⁺=(√E+√E_src)².
```

Smoothness makes these source tails vanish. The source-transformed input energy is at most `E⁺`. For the two complete orders,

```text
||J_N∘Ad(U_s,N) − J∘Ad(U_s)||_{⋄,E}
 ≤ min{2, S_N(E)+I_N(E⁺;R)+L_N(E⁺)},
||Ad(U_s,N)∘J_N − Ad(U_s)∘J||_{⋄,E}
 ≤ min{2, S_N(E)+I_N(E;R)+L_N(E)}.             (3)
```

For the second line, the **cutoff** instrument leaves the high system modes untouched, so the source-tail energy is still bounded by the input E even though the instrument may change the low-mode energy. Each subnormalized recorded outcome and the nonselective output inherit these bounds by postprocessing. A normalized conditional state requires a positive lower bound on that outcome's probability.

For completeness, a sufficient source-tail majorant follows from `L₂=||F_d''||₁`:

```text
F_N^s ≤ L₂²/(3πN³),
G_N^s ≤ (L₂²/π)[1/(2N²)+m_A/(3N³)].
```

Thus both expressions in (3) vanish under the stated fixed-smear, finite-energy assumptions. No claim of unrestricted diamond-norm convergence follows.

## 5. Numerical controls and what they do not show

The [verifier](verification/two_field_instrument_continuum.py) computes finite-M kernel norms, checks them against the analytic infinite-tail majorant, checks number-relative interaction and commutator bounds on a truncated six-oscillator Fock matrix, and solves the finite-mode symplectic equations. It evaluates the exact Gaussian-vacuum output trace distance for cutoff N versus common finite M=4. With weak coupling `λ=.02`, N=2, M=4, the observed vacuum distance is about `.00896`, below a non-vacuous finite-M bound of `.07493`. The N=M distance is mathematically zero; the floating-point determinant evaluation leaves a roughly `1.1×10⁻⁷` numerical residual.

For the full-strength illustrative case, E=100, the simple interaction majorant is still the maximal value 2 through the small cutoffs tested. A round `N=10^52` gives an interaction-only bound around `.00514` using floating-point constants. This astronomical number is an illustration of how **loose and impractical** the analytic certificate is, not a physical requirement, an optimal cutoff, or an interval-certified numerical result. It does not include the source and readout terms. The Gaussian controls do not prove the all-input/infinite-dimensional estimate; Sections 2–4 provide the conditional analytic argument.

Run using the pinned `verification/requirements-field-probe.txt`; the JSON output records constants, finite-M tails, sample bounds and controls.

## 6. Scope and remaining work

- The total **input** energy and masses are imposed; a complete switching, source, pointer, record, reset and gravitational energy budget is absent. The proof avoids assuming a total post-interaction energy bound where it is not established.
- The source and field–field interaction are local in the chosen fixed 1+1 background; the outgoing readout qubit and records remain idealized externally controlled apparatus. The calculation does not establish an autonomous, relativistic record memory.
- The Hilbert–Schmidt argument uses one spatial dimension. In 3+1 on a spatial three-torus, even the `k+l=0` terms of the **instantaneous** pair-creation kernel give the lower bound `|F̂(0)|²/4 × Σ_{k∈Z³} 1/(ω_A,k ω_B,k)`, which diverges for the normalized nonzero spatial coupling. The verifier lists finite-cutoff partial sums. Thus the number-relative instantaneous-kernel proof above fails in 3D. This does **not** prove that the smoothly time-switched 3+1 scattering operation fails to exist: temporal oscillations and established renormalized/covariant constructions require a separate analysis. Ultraviolet behavior, renormalization and representation domains remain open.
- Gravity, refoliation, emergent spacetime, subjects, phenomenal identity and necessary actuality remain open. A passed restricted operational subproblem is not a complete framework or an empirical prediction.
