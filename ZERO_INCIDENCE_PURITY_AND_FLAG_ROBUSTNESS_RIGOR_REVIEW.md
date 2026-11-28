# Incidence, purity and physical flags: quantitative robustness

## Result and scope

The [joint incidence/echo construction](ZERO_JOINT_CONSTITUTION_INCIDENCE_AND_ECHO.md) proves that a **pure** physical marginal forces two positive incidence-type blocks to be constant multiples of that state, while leaving their overall type weight free. The [identity-pair flag construction](ZERO_IDENTITY_PAIR_PHYSICAL_FLAG_AND_INCIDENCE.md) shows that perfectly identifying those types with a coherent physical flag is incompatible with preserving that same pure marginal on all effects.

This review strengthens both exact statements:

1. For a nearly pure finite-dimensional physical marginal, type–physical-event correlations are bounded, but may be of **square-root order** in the impurity. A witness uses the original sphere/echo source vector and its existing gauge-compatible relative-sign operator.
2. In the original balanced Bell-pair flag, approximate preservation of the full coherent physical state and approximate flag identification obey a **sharp error tradeoff**. For example, trace distance at most `0.1` from the ideal state requires at least `0.2` total flag/type mismatch in the stated bookkeeping model.

The incidence types, the physical–experiential interpretation, and the admissibility of all effects remain hypotheses. A controlled mixed physical state is not the original exact pure preparation. These are finite-model compatibility bounds, not measurements of subjects or proof of a whole-level zero.

## 1. The pure-marginal theorem and a useful approximate version

On the stipulated finite physical Hilbert space H, let positive type blocks `B,J` satisfy

```text
B≥0,  J≥0,  B+J=ρ,  Tr ρ=1,  α=Tr B.
```

They may be viewed as a state `B⊕J` on the **proposed** two-type incidence algebra; forgetting the type returns the physical state ρ on all physical effects. If `ρ=|ψ⟩⟨ψ|`, positivity gives `B=αρ`, `J=(1−α)ρ`. Thus for every physical effect `0≤E≤I`,

```text
Tr(BE)=α Tr(ρE).
```

The pure state fixes the form of conditioning, not α. The conclusion depends on the strong full-marginal/effect premise; a rule defined only on the commuting record algebra has a different domain. It does not identify these blocks with real subjects or demonstrate an experiential weight.

Now let `P` be a largest-eigenvalue projector of ρ, with eigenvalue `1−δ`, and `Q=I−P`. Write `m=max(α,1−α)`. For every effect E,

```text
|Tr(BE) − α Tr(ρE)|
  ≤ min{ α(1−α),  m δ + (1/2) sqrt[δ(1−δ)] }.       (1)
```

Here `δ=0` recovers the exact result. In finite dimension this δ is also the trace distance `D(ρ,P)` from the selected pure eigenstate, where `D(X,Y)=||X−Y||₁/2`.

### Proof of (1)

Put `X=B−αρ`, so `Tr X=0`. For an effect, `|Tr XE|≤||X||₁/2`. Let `q=Tr(QBQ)`, so `0≤q≤δ` and `Tr(PBP)=α−q`. Since P is an eigenprojector of ρ, its P–Q block vanishes, and

```text
|Tr(PXP)| = |αδ−q| ≤ mδ,
||QXQ||₁ ≤ (1−α)q + α(δ−q) ≤ mδ.
```

For the off-diagonal block `b=PBQ`, positivity of B and J gives

```text
||b||₁ ≤ sqrt[(α−q)q],
||b||₁ ≤ sqrt[(1−δ−α+q)(δ−q)].
```

Because their P–Q blocks are opposite, the two bounds apply to the same b. The minimum is at most half their sum, which by Cauchy–Schwarz is at most `sqrt[δ(1−δ)]/2`. Splitting X into its diagonal and off-diagonal Hermitian blocks gives

```text
||X||₁/2 ≤ mδ + (1/2)sqrt[δ(1−δ)].
```

Independently, the two-outcome classical joint distribution of type and E gives `|Tr XE|≤α(1−α)`. Taking the minimum proves (1). This bound is not claimed globally optimal at every α,δ; the example below shows its **square-root order and coefficient 1/2** cannot be improved uniformly at α=1/2.

If a specified ideal pure state `P₀` has `⟨ψ₀|ρ|ψ₀⟩≥1−ε`, the largest eigenvalue is at least `1−ε`, hence `δ≤ε`. For `0≤ε≤1/2`, the right-hand square-root expression is increasing in δ, so ε gives a valid—possibly conservative—bound. Certifying that fidelity for the *full* physical marginal can be much harder than measuring selected records.

For an event with `p_E=Tr(ρE)>0`,

```text
|P(B|E)−α| ≤ min{max(α,1−α), bound(δ,α)/p_E}.
```

This is a state-specific bound, not a channel theorem or a guarantee for events of zero probability. Rare conditioning can amplify an otherwise small joint discrepancy.

## 2. Sharp square-root witness on the existing echo carrier

Use the old normalized physical source `|ψ⟩` at a selected old-clock label in the actual sphere/echo setup, and the previously constructed relative-sign operator O implemented by `value_history`. On the stated valid sector, `O²=I` and O preserves the specified gauge and charge conditions. The existing preparation has `⟨ψ|O|ψ⟩=0`. Let

```text
|φ⟩=O|ψ⟩,       ⟨ψ|φ⟩=0,
|ψ_±⟩=sqrt(1−δ)|ψ⟩ ± sqrt(δ)|φ⟩,
B=|ψ_+⟩⟨ψ_+|/2,  J=|ψ_-⟩⟨ψ_-|/2,
ρ_δ=(1−δ)|ψ⟩⟨ψ| + δ|φ⟩⟨φ|.
```

Both candidate blocks are positive, have type weights 1/2, and sum to the **same** physical `ρ_δ`; that state is δ away in trace distance from the original ideal `|ψ⟩⟨ψ|`. The independent-type extension `B=J=ρ_δ/2` has the same physical marginal and type totals. For `E=(I+O)/2` restricted to the valid sector,

```text
Tr(ρ_δ E)=1/2,
Tr(BE)−(1/2)Tr(ρ_δ E) = (1/2)sqrt[δ(1−δ)],
P(B|E)−1/2 = sqrt[δ(1−δ)].
```

Thus exact purity eliminates this correlation, but a δ-sized impurity can support a square-root-sized type correlation. The tests use the original complex history vectors at labels `0,7,15`, verify orthogonality and gauge/charge conditions on both vectors, and calculate this witness. The formal effect is gauge-compatible in the specified finite construction; its physical implementation, joint interface, and identification with a first-person question still require independent justification. The example does not claim `ρ_δ` is the actual original state, nor that the two type blocks are two real subjects.

A separate rare-event control uses `ρ_δ=(1−δ)P+δQ`, `B=(1/2−δ)P+δQ`, `J=P/2`, and `E=Q`, for `0<δ<1/2`. Both types have total weight 1/2 and the joint discrepancy is only δ/2, yet `P(B|E)=1` because `p_E=δ`. Q is a formal global projector; a confined observer is not assumed to have access to it.

## 3. A sharp physical-flag/coherence tradeoff

The prior identity-pair construction has a balanced physical flag `P₀,P₁` and a norm-one Hermitian coherence witness D satisfying

```text
P₀+P₁=I,  D P₀=P₁ D,  Tr(ρ_*D)=1,
Tr(ρ_*P₀)=Tr(ρ_*P₁)=1/2,
ρ_*=|Ψ⟩⟨Ψ|.
```

For its source pair D is `X_S X_F`; during the specified unitary history the transported `D_t` preserves the analogous relation because the reference flag is not acted upon. The witness may involve a joint interface and is not automatically accessible to either putative subject.

Let candidate type blocks B,J sum to some physical marginal `ρ̃`. If B is intended to correspond to flag 0 and J to flag 1, define the **total** flag/type mismatch

```text
η = Tr(BP₁)+Tr(JP₀),       0≤η≤1.
```

This definition concerns a joint bookkeeping assignment on all effects, not an experimental estimate of phenomenal identity. By positivity, off-diagonal block Cauchy–Schwarz, and the flag-odd property of D,

```text
|Tr(ρ̃D)|
 ≤ 2[sqrt(Tr(BP₀)Tr(BP₁)) + sqrt(Tr(JP₀)Tr(JP₁))]
 ≤ 2sqrt[η(1−η)].
```

If `ε=D(ρ̃,ρ_*)`, the norm-one witness also gives `Tr(ρ̃D)≥1−2ε`. Consequently

```text
ε ≥ max{0, 1/2 − sqrt[η(1−η)]}.                  (2)
```

For `ε<1/2`, solving (2) gives

```text
η ≥ [1−sqrt(1−4(1/2−ε)²)]/2.
```

At `ε=0`, mismatch is at least 1/2; at `ε=0.1`, at least 1/5; and a perfectly sharp identification `η=0` requires trace distance at least 1/2. This is stronger than merely saying the pure, sharp case is incompatible: it quantifies the cost of approximate compatibility.

**Sharpness in the actual pair subspace.** In either fixed sphere-sign sector let `u₀,u₁` be the two normalized Bell components in flag sectors 0 and 1, exchanged by D, so `|Ψ⟩=(u₀+u₁)/sqrt(2)`. For `0≤η≤1/2`, use

```text
v₀=sqrt(1−η)u₀+sqrt(η)u₁,
v₁=sqrt(η)u₀+sqrt(1−η)u₁,
B=|v₀⟩⟨v₀|/2,   J=|v₁⟩⟨v₁|/2.
```

Their mismatch is η, their type totals are both 1/2, and the physical marginal is exactly `1/2−sqrt[η(1−η)]` away from the ideal pure state. Thus equality holds in (2). The tests check both actual Bell-sector pair states and several η values.

The saturation family **does not preserve the original exact second pair relation** `Q_x=X_S−X_F` except at η=1/2: indeed `Q_x²=2(I−D)` and `Tr(ρ̃ Q_x²)=4ε` for this construction. It does preserve the conditional `Q_z` relation in the pair subspace. If a candidate requires all original pair relations or additional physical constraints to remain exact, it may exclude the saturating examples and impose stronger limits; (2) remains a necessary bound. These are deliberately constructed physical marginals, not an assertion that the ideal history has physically dephased or that an experience measures a flag.

## 4. Rechecking angular quality at different access levels

The [angular reconstruction](ZERO_INTRINSIC_QUALITY_ANGULAR_RECONSTRUCTION.md) works on a further extension of the echo carrier, with a stipulated uniform angular distribution `du/2`. On that prepared state, and given the sign K, the old record distinguishes the two negative-u bands and the positive-u band but not different u values within one band. We independently integrated the two candidate magnitudes `g₁=|u|` and `g₂=|u(u+1)|`. The mean-square errors below are in units of κ²:

| Information made available | g₁ minimum | g₂ minimum |
|---|---:|---:|
| K only | 1/12 | 17/60 |
| K plus the coarse R sign | 1/12 | 31/180 |
| K plus the complete three-band record | 5/96 | 31/180 |

The R-level row sharpens the earlier comparison: R adds **no** improvement for g₁ under this distribution, but already supplies all the three-band information useful for g₂. This is a comparison of declared readouts/estimators, not a claim that an actually confined subject can access K or R. Both candidates have mean magnitude 1/2 and zero signed mean under the stated symmetric Born preparation, but their magnitude second moments differ: `E[g₁²]=1/3` and `E[g₂²]=8/15`. They are therefore not the same proposed physical quality observable, even though the first signed moments agree.

The earlier quantum test checks that old conditional states are identical within each band for its preparation, so independently prepared ancillas and operations restricted to that old state cannot reveal which within-band u was selected. This is a conditional access result, not a metaphysical prohibition on richer intrinsic relations or a deduction of felt quality from an observable. Its angular extension and the purity/flag perturbations above are **different hypothetical modifications** of the common echo carrier; this review does not assert they are jointly prepared in a single experiment.

## 5. Relation to quality, gauge and the wider audit

The earlier local echo quality theorem selects `κsjr` only after a specific boundary, ready calibration and composite-neutrality premise. The relative-sign construction supplies an operator invariant under a **specified** diagonal gauge but odd under a different counterpart. Neither result makes an incidence label a subject or a physical parity into felt valence. The new bounds assume the relevant effects are in the physical algebra and the type blocks define a normalized additive extension; the flag theorem assumes the proposed type–flag joint questions are meaningful. If instead the constitution uses only a compatible record algebra, an explicitly contextual rule, or a different subject ontology, it need not satisfy those premises.

This also distinguishes **gauge compatibility** from **access**: an operator can respect the mathematical constraints while requiring a joint interface unavailable within a confined realm. A local observer's inability to report a candidate quality does not prove experience absent. Conversely, a globally available effect or a numerically inferred magnitude is not evidence of an actual experience. Space and time here are effective model ingredients, not fundamental postulates of the user's framework.

The constructive follow-through for P1 and A4 is now quantitative: derive which incidence questions and interfaces are physically/experientially legitimate, certify purity or coherence at the appropriate scope, and compare any proposed subject/quality law with (1)–(2). Equal incidence weights or a phase-paired balance cannot simply be inferred from mathematical zero. These bounds do not refute the stronger possibility that the actual zero constitution uniquely determines its subjects and measure; they identify conditions it must meet without invoking a universal subject or treating suffering as erased by a global sum.

## Verification

[Focused tests](verification/zero_incidence_purity_robustness_test.py) check random positive-block controls, the original complex echo vector and constrained relative-sign witness, the rare-event example, both conditional Bell-pair sectors, saturation of the flag/coherence tradeoff, and independent exact angular-access integrals. They are not evidence that the selected incidence algebra or phenomenological interpretations are actual.
