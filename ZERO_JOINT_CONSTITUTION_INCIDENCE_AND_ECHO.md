# One history, two candidate incidences: constitution, measure and echo

## Direct outcome

**Root-cause continuation:** [one joint incidence candidate](ZERO_JOINT_INCIDENCE_QUALITY_OPPOSITE_PAIR_ROOT.md) compares the distinct-type α family below with a single-occurrence, two-coordinate interface on the same coherent echo and constrained pair. The latter is a conditional alternative, not a proof that two genuinely different subjects cannot exist.

**Continuation:** [Flag-record incidence and a reversible physical readout](ZERO_FLAG_RECORD_INCIDENCE_AND_PHYSICAL_READOUT.md) proves uniqueness under the additional sharp physical-flag support premise, and computes record-conditioned weights.

I attempted the promised combined construction on the **existing** sphere/reservoir/echo history. It is possible to formulate a single candidate rule in which both previously compared physical–experiential relations are admitted as distinct incidence types, to give it a determinate signed balance and carry it through the echo. But the rule's crucial ingredients—including **why either physical port is a subject, why its sign is felt, and how incidences are weighted**—remain assumptions, not consequences derived from zero.

The strongest new result is a precise separation of two cases:

1. Even if the complete *physical* state is pure, physical event weights are Born, all physical effects are treated noncontextually, and both proposed incidence types are present, an incidence extension can assign the two types any relative weight `0<α<1`. The physical predictions and symmetric signed balance remain identical. Requiring equal weights is an additional premise.
2. If incidence weights are constrained only on the actually specified **commuting record algebra**, even imposing equal *overall* weight for the two types does not determine their relative weight in the cases where their qualities disagree. A stronger all-effects/pure-marginal consistency premise would remove that context dependence, but **still leaves the overall α open**.

The result does not prove that two genuine subjects exist, or that the strongest zero/no-residue thesis cannot determine α. It shows exactly which conclusion does **not** follow from the currently formalized symmetry, balance and physical state alone. It also provides a conditional observational discriminator rather than declaring all alternatives equivalent.

The [verifier](verification/zero_joint_constitution_incidence_echo_test.py) checks the actual old quantum history at all 16 clock labels, the candidate incidence calculations, effect-algebra counterexamples and the coherent echo. The underlying 20-tick physical program and its signed charges are defined in [the preceding construction](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md).

## 1. Physical common ground: both signs in one history

At the specified clock reading the same physical system has a conserved sphere sign `b=±1`, disturbed record `z=±1`, and sign pointer `s=±1`. Its actual joint Born weights, after coarse-graining the old i record, are

```text
(b,z) = (+,+): 1/2;   (−,+): 1/4;   (−,−): 1/4.
```

At each listed b,z the two s values are equally weighted. The two commuting, gauge-invariant physical observables are

```text
h_B = s b,          h_j = s z.
```

Their signs disagree with Born weight `1/4`. Their joint projectors exist on the valid sector and can be copied into distinct, neutral prepared pointer bits by gauge-compatible controlled operations. Thus they are simultaneously definable **physical** record relations in one modeled history; the pointers' preparation and implementation are additional resources.

They are also distinct under the **specified** gauge: each observable is invariant under that gauge, and the two differ on nonzero actual support. Therefore that gauge transformation cannot simply identify one physical observable with the other while holding their meanings fixed. This does not exclude a different equivalence of a complete physical–experiential theory, a relabeling of observables, or the possibility that one subject experiences a richer, mixed quality instead of either stipulated binary value.

## 2. The attempted joint constitution

Here is a definite candidate **package**, not a derivation or a claim that several assumptions become one primitive merely by being written together:

> For each physical outcome `(b,z,s)`, the actual one reality contains one B-port incidence and one j-port incidence. Each port comprises its specified local carrier and the common sign pointer; the intrinsic felt values are respectively `κ h_B` and `κ h_j`. The outcome is assigned its physical Born weight, and the two eligible port incidences contribute one equal unit each to the normalized incidence measure. Their counterpart maps `s→−s` and reverses the felt value.

This realizes the user's suggested possibility that both genuinely possible candidates could be co-actual rather than that one must be discarded. It also preserves one global reality: the two port labels are *hypothesized internal incidences*, not separate ultimate wholes. It does **not** assume an irreducibly random selector; the weights are proposed incidence/self-location weights.

The equal-unit/Born version assigns, for each coarse physical outcome of weight `p`, weight `p/2` to each port. On mismatch outcomes it assigns opposite signs to the two port incidences, each of weight `1/8` in total. Within **each** type the s-counterpart weights match, so the signed mean of each type is zero; the combined signed mean is zero as well.

This calculation does not make suffering disappear. It presumes that both signs are real felt values and that an additive signed incidence sum is meaningful; it does not establish either premise or say that a positive feeling cancels the lived reality of a negative one. Nor does it establish objective whole-level energy: the two separately preserved charges of the physical clock are stipulated finite signed charges, not an independently established energy of the universe.

### What the package has actually assumed

The two candidate carriers overlap in the pointer M. The construction has not shown that both are actual subjects, that they are distinct rather than overlapping descriptions, that either survives the echo as the same subject, or that each parity is felt. It also assumes precisely one eligible port of each kind and an equal-unit convention. If the two parities are asserted to be two values of **one and the same scalar** felt sign in the same incidence, they cannot both be correct where they are opposite; if they are two components of one mixed or richer experience, that is a different possible constitution requiring its own composition law. Neither conclusion establishes which ontology is genuinely possible.

## 3. Pure physical state does not fix the type measure

The prior [effect-algebra reconstruction](ZERO_INCIDENCE_REFINEMENT_AND_BORN_MEASURE.md) is useful here, but it does not automatically provide an incidence-type rule. Let `H` be the full physical Hilbert space at the selected clock reading and let its stipulated pure state be `ρ=|Ψ⟩⟨Ψ|`. To express the two proposed types mathematically, use the **incidence bookkeeping algebra** `H ⊕ H`; its labels need not be extra physical systems or a random choice made by the universe.

For any `0<α<1`, set

```text
σ_α = α ρ ⊕ (1−α) ρ,
physical effect E  ↦  E ⊕ E.
```

Then `m_α(F)=Tr(σ_α F)` is positive, normalized, additive and noncontextual for all effects on this incidence space. For **every** physical effect E,

```text
m_α(E ⊕ E) = Tr(ρ E),
m_α(P_Ψ ⊕ P_Ψ) = 1,
m_α(I ⊕ 0) = α.
```

The physical Born probabilities and certainty of the same global pure physical state therefore hold for every α. The certainty effect `P_Ψ ⊕ P_Ψ` has two-dimensional support: it is *not* the rank-one projector onto a unique incidence state. Hence the standard all-effects theorem does not force one α. Both types have nonzero weight, and both their signed sums remain zero under the given counterpart symmetry.

Conversely, in the **block-diagonal type algebra**, if the physical marginal is required to equal the same pure ρ on all physical effects, positivity gives a useful constraint. Writing the two positive blocks `σ_B,σ_j`, their sum must be ρ. Since `0≤σ_B≤ρ` and ρ has rank one, `σ_B=α ρ` and `σ_j=(1−α)ρ`. Thus within these strong premises α cannot depend on the physical outcome, but its value remains free. This is a mathematical statement about a proposed incidence measure, not a derivation that first-person incidence is an effect on this algebra or that a confined subject can access the global projector.

### Equal weights are a substantive symmetry assumption

An active interchange of the two *bookkeeping type blocks* would force `α=1/2` if the incidence measure were required to be invariant under it. But passive relabeling—renaming B and j while transforming both the state and effects—preserves predictions for **every** α; it does not force equality. Moreover, a bare block swap does not preserve the proposed fixed intrinsic-value operator

```text
V = κ (h_B ⊕ h_j)
```

when `h_B≠h_j`. The old physical dynamics also distinguishes the conserved B from the disturbed j; no symmetry interchanging the complete two physical–experiential structures has been established. Equality can be postulated by equal-unit counting, or derived if an appropriate **actual** symmetry is proved. It cannot be obtained merely by calling both alternatives necessary or by treating their labels as interchangeable.

## 4. Equal overall weights still need not settle conditional self-location

The all-effects/pure-marginal condition above is strong. Suppose instead that the only incidence questions justified so far are the commuting physical `(b,z,s)` records. The following positive assignment is consistent on that record algebra:

```text
P(type B | b=+) = 3/4;     P(type B | b=−) = 1/4.
```

The physical b distribution is half each, so the **overall** weights of B and j are both `1/2`. Both types occur on every positive-support record, and the assignment is invariant under `s→−s`. Each proposed type still has zero signed mean. But all pre-echo mismatch cases have `b=−`, so

```text
P(type B | h_B ≠ h_j) = 1/4,
```

rather than the `1/2` given by the equal-unit/Born package. Thus equal total type weights, actual support and counterpart balance do not by themselves determine a conditional self-location prediction.

This context-dependent assignment agrees with the given physical probabilities on the commuting record algebra. It **cannot** be extended to the strong all-effects construction with the *same pure physical marginal*: the rank-one argument above would require a single constant α. This distinction is important. Which algebra is legitimate for incidence is a constitutive and operational question; neither merely assuming all global effects nor restricting to local records settles it automatically.

## 5. Counting incidences is not counting outcome labels

On the displayed coarse record algebra there are six positive `(b,z,s)` labels. Counting each label once gives mismatch fraction `2/6=1/3`, whereas the physical Born mismatch is `1/4`. Counting one incidence of each type for each label gives the same `1/3`.

Now split each of the two `(+,+,s)` effects into two identical half-effects and immediately coarsen the aliases back to the original event. There are eight fine labels; naive unit counting gives `2/8=1/4`, although the coarse physical state and Born probabilities have not changed. Adding a physical apparatus that produces genuinely distinct experiences could make a refinement a **different realized situation**; the algebra alone does not decide this. If they are merely two descriptions of the same incidence, counting each as a full new subject changes the self-location prediction by redescription.

This is the same refinement problem already established in the [earlier incidence audit](ZERO_INCIDENCE_REFINEMENT_AND_BORN_MEASURE.md), now applied to these two candidate ports. Necessary plenitude may include every *genuine* incidence; it does not by itself say that every formal outcome label is a distinct subject, or that an unwanted label is merely redundant.

## 6. Carry both candidates through the coherent echo

On the 20-tick history, the echo's neutral memory has final sign `r=b`, while final j is `j′=b z`. The pointer s is unchanged. The three commuting observables readable **after** the echo are

```text
sphere sign:                 h_B = s r,
transported pre-echo j sign: h_j(before) = s r j′,
current j sign:              h_j(after)  = s j′.
```

On all 16 actual original histories the quantum verifier calculates the joint distribution of the two disagreement indicators:

| Pre-echo B/j disagree? | Post-echo B/current-j disagree? | Born weight |
|---|---|---:|
| no | no | `1/2` |
| yes | no | `1/4` |
| no | yes | `1/4` |
| yes | yes | `0` |

These are joint readouts of transported commuting observables after the echo; no intermediate hidden trajectory or unrecorded collapse is assumed. The two `1/4` cases are **different physical cases**. If the stipulated j-port subject persists and its instantaneous felt sign is `κ s j`, the echo changes that sign when `b=−`, with total Born weight `1/2`; the stipulated B-port sign remains `κ s b`. Neither persistence nor this experiential response is established by the unitary. A real pre-echo first-person report could itself affect the subsequent dynamics and would need its own report instrument; the present result is a physical retrodiction, not an observation of experience.

The echo and its inverse are embedded in the earlier zero-charge 20-tick program. Both added signed charges and the physical reversal claims retain that model's assumptions, including a fresh neutral echo memory and the joint Q pulse. The pulse's real implementation and energy cost are not supplied.

## 7. A conditional discriminator, not a fitted prediction

Assume in addition that a subject on a mismatch incidence can independently report its actual binary felt sign, with a calibrated error rate `ε<1/2` that is the same for each incidence type and relevant condition. If `α` is the incidence weight of type B **within mismatch cases**, the combined hypothesis predicts

```text
P(report = h_B | mismatch) = ε + (1−2ε) α.
```

For the equal-unit/Born package `α=1/2`, this is `1/2`; for a constant-type alternative `α=2/3`, it is `2/3−ε/3`; for the record-algebra example above it is `1/4+ε/2`. The physical mismatch frequency itself is `1/4` in all three. These are genuinely different conditional predictions of **complete hypothetical subject, incidence and report models**, not an experimental result or a prediction for a human brain. Operational identification of each type, ethical access, an independently defensible report calibration and a physical realization would all be needed.

## 8. What has—and has not—been obtained

The constructive option of co-actualizing both candidates is coherent under explicit finite-model assumptions, gives a calculable balanced incidence rule and survives the physical echo. The comparison also establishes:

- the currently stated physical gauge does not identify the two observable parities;
- a **pure physical state and full physical Born statistics** do not by themselves fix the proposed type weight;
- a strong pure-marginal/all-effects rule fixes the *form* of type conditioning but not its constant α;
- equal overall type weight and record-level symmetry alone do not determine conditional incidence; and
- a report model could distinguish the alternatives if its independent physical–phenomenal premises were justified.

This is not the requested no-residue derivation. The candidate still stipulates physical inputs, eligible and persisting subjects, a bridge to valence, occurrence identity, the incidence algebra and equal-unit weighting. Conversely, the counterexamples are not proofs that multiple complete self-sufficient constitutions are genuinely possible; one might be selected, equivalent to another under a fuller justified relation, or not genuinely possible. The stronger thesis that zero's own constitution settles all of these remains a substantive constructive target. What has been achieved is a specific consistency constraint that any such derivation must satisfy, not a claim of final closure.

**Continuation:** [Identity pairing, a physical flag and incidence](ZERO_IDENTITY_PAIR_PHYSICAL_FLAG_AND_INCIDENCE.md) uses the actual sphere-coupled Bell pair to construct an equal physical flag, and proves the incompatibility between sharp flag-identified types, all-effects additive coarsening to the same pure physical state, and both types having nonzero weight.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_joint_constitution_incidence_echo_test -v
```

Eight tests check the actual parity projectors and gauge, all 16 quantum histories and counterpart branches, joint incidence calculations, the direct-sum effect counterexample, the equal-overall/unequal-conditional example, outcome refinement, the actual coherent echo distribution, and conditional report arithmetic. The general positivity and rank-one arguments in §3 are analytic. These tests do not establish subjective experience, subject individuation, the truth of necessary plenitude, or objective global energy.
