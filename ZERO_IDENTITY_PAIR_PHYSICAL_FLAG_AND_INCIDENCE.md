# Can an actual zero-balanced pair determine incidence weights?

## Result

The sphere/reservoir construction already contains a natural candidate for the missing equal-weight rule: its **actual first source–reference Bell pair**. Two exact relational zero conditions fix that pair, conditional on the sphere sign, and its reference bit has equal Born weight in either value. If those two physical reference values are **additionally** identified with the two proposed incidence types, they give the equal `1/2 : 1/2` type weights on the earlier coarse `(b,z,s)` records.

That is a constructive answer, but not a derivation of the incidence rule from zero. The identification of reference value with subject type is an extra physical–experiential proposal, and the two reference outcomes are refinements of the physical history—not automatically two subjects.

More sharply, there is an exact incompatibility among three tempting requirements:

1. the two types are **perfectly identified by the sharp physical reference flag**, both with nonzero weight;
2. their nonnegative, additive weights are defined on **all physical effects** and sum to the Born weight of the same full pure physical state; and
3. the physical state retains coherence between the two reference values.

They cannot all hold simultaneously. This is a consequence of positivity and a rank-one physical marginal, not a proof that the user's one-reality or plenitude proposal is false. It identifies which strong bridge assumptions must be revised or justified. The actual finite circuit also exhibits a physical coherence witness: the bare pair coherence is lost locally while a source record is written, but an appropriately transported **joint** witness stays sharp and the complete program reverses.

The [verifier](verification/zero_identity_pair_incidence_record_test.py) uses the actual source, reference, finite stores and echo schedule from [the 20-tick sphere construction](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md). No new spectator pair or purported physical subject is inserted.

## 1. The identity pairing is already inside the sphere history

Let `S` and `F` be the **first** source and its paired reference, and let B be the old conserved sphere observable. The actual source interface transforms the initially prepared Bell pair, so for a B-eigenvalue `b=±1` its pair state is

```text
b=+1:  (|00⟩ + |11⟩)/√2,
b=−1:  (|10⟩ + |01⟩)/√2,
```

where the order is S,F. On the joint prepared state define

```text
Q_z = Z_S − B Z_F,
Q_x = X_S − X_F.
```

Both annihilate it exactly immediately after the interface. Equivalently, the commuting involutions

```text
G_z = B Z_S Z_F,          G_x = X_S X_F
```

have value +1. On the 2×2×2 space B,S,F their common +1 sector has dimension **2**, with one pair state for each B value. Thus the two relations uniquely fix the pair **conditional on B**, while leaving arbitrary sphere-sector amplitudes and correlations with the rest. The reference F is maximally mixed in either sector, so its two physical readout values have weight 1/2 even conditional on the old `(b,z,s)` record.

This is an actual realization of the previously studied [dual identity pairing](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md), now tied to the source used by the sphere clock. It is not a derivation that the pair, the two operators or their normalization must exist. `Q_z` and `Q_x` are **relational operator differences**, not automatically energy or felt valence, and they should not be added to the two separately stipulated signed-energy charges.

## 2. A concrete equal-weight proposal—and its extra content

Write the reference's computational bit as `x₀=0,1`, and propose the eligibility rule

```text
x₀=0  →  a B-port incidence with felt sign κ s b;
x₀=1  →  a j-port incidence with felt sign κ s z.
```

In the constructed state, `x₀` is independent of the old simultaneous `(b,z,s)` records. If its two refined outcomes are treated as actual incidences with their Born weights, this rule gives each proposed type weight `1/2` at every old record. The s-counterpart still balances each type's stipulated signed values. This is a precise **conditional** route from the actual pair to the equal weights that the previous [joint-incidence test](ZERO_JOINT_CONSTITUTION_INCIDENCE_AND_ECHO.md) had to stipulate.

But the rule supplies more than a measure. It declares that a physical reference bit determines **which subject boundary and experiential bridge** applies. Neither the Bell state nor the relational constraints give that meaning to the flag. The reverse identification, `0→j, 1→B`, has exactly the same coarse `(type,b,z,s)` weights but different type–flag correlations. On a fixed b,z,s branch, tracing the source and reference leaves the same old state for either x₀; consequently, a rule that chooses between these boundaries solely from that old reduced state cannot implement this flag-dependent selection. One could include an actual F interface in the relevant constitution, allow genuinely distinct intrinsic incidences not determined by that state, or reject this particular rule—but the interface and identity rule must be justified rather than inferred from confinement.

This flag proposal is also not the same as the prior *one B incidence and one j incidence per fully specified outcome*. Here the two types are assigned to **different x₀-refined outcomes**. Treating both as actual invokes the proposed incidence/plenitude rule; it does not follow just because a quantum expansion contains both components. A necessitated measure need not be an objective lottery.

## 3. The physical flag gives a strong consistency test

Let `ρ=|Ψ⟩⟨Ψ|` denote the full, still-pure conditional physical state immediately after the sphere/source interface, including the old system and all purifying systems. Let `P₀,P₁` be the two sharp projectors for F. In this actual preparation

```text
Tr(ρ P₀) = Tr(ρ P₁) = 1/2.
```

Suppose a proposed incidence theory assigns nonnegative, additive and noncontextual **type weights for every physical effect**, represented by positive operators `σ_B, σ_j`, such that

```text
σ_B + σ_j = ρ,
σ_B is supported on P₀,   σ_j is supported on P₁,
Tr σ_B > 0,  Tr σ_j > 0.
```

These premises formalize both a sharp physical flag and the requirement that forgetting the type reproduce the same pure physical Born state for *all* physical effects. Positivity gives `0≤σ_B≤ρ`. Since ρ has rank one, `σ_B=α ρ` and `σ_j=(1−α)ρ`. For `0<α<1`, each has support on both reference sectors, because Ψ does. Neither can be supported exclusively on its assigned flag. **Therefore no such pair exists.**

This sharpens, rather than contradicts, the earlier direct-sum result. An equal independent type assignment `σ_B=ρ/2` and `σ_j=ρ/2` preserves all physical Born probabilities, but it is **not** the proposed physical-flag rule: for instance, its joint weight for `(type B, x₀=0)` is `1/4`, whereas the flag rule gives `1/2`. Both have the same marginal type and flag weights of `1/2`. Equal marginals do not establish that the incidence type is physically identified by the flag.

There are legitimate alternatives, each with different premises:

- define incidence weights only on a compatible record algebra, rather than on all global effects;
- describe an actual flag-reading instrument and include its physical consequences and any reporting apparatus;
- allow a type that is not a sharp physical flag or does not sum to physical Born weights on all effects; or
- supply a different physical–experiential ontology that explains why the applicable incidence questions have another structure.

The theorem does **not** show that coherent quantum branches cannot both be actual or experienced. It rules out the stated combination of all-effect additivity, a sharp flag, a pure physical marginal and both nonzero type weights. Treating quantum state expansions as actual incidences, or insisting on a global all-effects probability for them, are themselves substantive choices.

## 4. An explicit coherent witness

The flag proposal has a familiar implementation on the compatible flag algebra: use the two unnormalized blocks

```text
σ_B = P₀ ρ P₀,       σ_j = P₁ ρ P₁.
```

They each have trace `1/2`, are supported on their flags, and agree with the original Born state on flag-commuting record effects. But their sum is the **dephased** state, not the original pure ρ. The actual source pair supplies a sharp witness:

```text
D = X_S X_F,
Tr(ρ D) = 1,
Tr[(P₀ρP₀ + P₁ρP₁) D] = 0.
```

D flips both S and F and anticommutes with `Z_F`. The physical pair state is an eigenstate of D in *both* B sectors. Thus the competing incidence prescriptions make the same coarse type weights but do not represent the same global physical state on all effects. This is a mathematical consistency test; merely saying a flag labels an actual experience is not itself a physical collapse or a measurement.

The circuit makes the issue more concrete. At clock ticks after the source has written a record, the **bare** observable D no longer has expectation 1, because the source is entangled with the working memory, store and reservoir. Nevertheless, if `U_t` is the specified physical gate sequence from the post-interface state, then

```text
D_t = U_t D U_t†,
D_t |Ψ_t⟩ = |Ψ_t⟩,
{D_t, Z_F} = 0.
```

The reference F is not acted upon by those gates. Hence the full state has `⟨D_t⟩=1`, while the sum of its two reference-dephased blocks has `⟨D_t⟩=0`. D_t can involve the source, reservoir and energy store and is not automatically accessible to either confined subject. After the inverse program, D itself is sharp again. Thus inaccessible or dephased *local* coherence is not the same as information erased from the closed whole.

## 5. The actual 20-tick record and coherence ledger

The verifier calculates the bare pair coherence `⟨D⟩` exactly from the actual source-controlled permutations, thermal purifiers, finite stores, auxiliary coding and echo. It also calculates the optimal guess of the source bit `y₀=x₀ XOR b_bit` using **R₀ alone**:

| Clock readings | `⟨X_S X_F⟩` | Best `P(guess y₀ from R₀)` |
|---|---:|---:|
| 0–1 | 1 | 1/2 |
| 2 | 0 | 1/2 |
| 3–17 | 0 | 1 |
| 18 | 0 | 1/2 |
| 19–20 | 1 | 1/2 |

The same result holds for the tested pure or initially Gibbs auxiliary bit. At tick 2, before R₀ has acquired the record, coherence has already gone into correlations with the working bit and finite store. At tick 18, R₀ has relinquished it but the reverse write is not yet complete. Thus R₀'s access alone does not characterize all information retained by the environment. The echo is a specified joint physical intervention, and the completed inverse restores the original pure state and preparation.

The `Q_z` relation remains exact from ticks 1–19 because the gates leave S, F and B's relevant Z labels intact; at ticks 0 and 20 the undressed relation `Z_S−Z_F=0` holds. `Q_x=X_S−X_F` annihilates the state only when the bare pair coherence is 1; its transported version does so at every tick. The two separately constructed signed-energy charges remain zero throughout the tested prepared histories. None of these identities is an observed cosmological energy or an experiential cancellation law.

## 6. Is the equal flag a symmetry of the *whole* proposal?

Immediately after the source interface, `D=X_S X_F` flips the reference flag while preserving the prepared pair state. It leaves the old b,z,s labels unchanged. But under the proposed flag-to-type interpretation it switches between `κ s b` and `κ s z`:

- where b=z, the assigned sign is unchanged;
- where b≠z, it is reversed.

Therefore this operation is neither a **universal sign-reversing experiential counterpart** nor a valence-preserving interchange for the proposed type map on the whole support. It also does not automatically preserve the subsequent source-writing interaction as an active symmetry of the complete physical law. The transported D_t is a symmetry of the **state** under the specified unitary history, but that is not the same as a symmetry of every physical and experiential structure.

This is the decisive gap in a tempting claim that equal type weights follow from “no preferred label.” The actual identity pair provides equal physical flag weights. The intrinsic type map and its symmetry require a further argument. A passive relabeling of both flag and its meaning is not an active symmetry that selects an incidence measure.

## 7. Constructive significance for the zero proposal

The result advances the user's proposal in two concrete ways:

1. A pair of relational zero conditions on an **already coupled physical pair** yields a canonical, exactly equal reference, without requiring the local source or sphere contributions themselves to vanish. Its physical coherence and local record can be tracked and reversibly restored.
2. The pure-marginal theorem turns “derive subject weighting from that reference” into a precise test. A sharp physical incidence flag, all-effects noncontextual type weights and an unchanged full pure physical state cannot all be assumed together when both flags are populated. A viable constitution must say which incidence algebra and physical interface are appropriate, rather than silently using mutually incompatible assumptions.

The result does not show that the relevant actual experiential quantity is additive, that a negative feeling has a compensating opposite, or that the reference labels actual subjects. An intrinsic positive counterpart, if required by a whole-level signed experiential zero, still needs a substantive identity and incidence measure; a mathematical cancellation does not erase suffering. Nor does the result prove that zero cannot be self-sufficient. The key constructive task is to show why a physical–experiential constitution should use one of the compatible alternatives in §3, and how its choice yields actual subjects, felt qualities and predictions without an external selector.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_identity_pair_incidence_record_test -v
```

Six tests check the actual conditional Bell-pair zero sector, the 20-tick source and charge ledger, bare coherence and R₀ record reliability across both the 14- and 20-tick programs, the flag-based incidence arithmetic, the sharp-flag pure-state conflict, and a coherent transported-witness illustration. The general positivity/rank-one result is analytic. The checks do not establish actual subjects, phenomenal valence, objective global energy, or necessity of the chosen source pairing.
