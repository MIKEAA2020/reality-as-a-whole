# One system linking sphere conservation, quantum records and opposite currents

## Result

This construction joins several previously separate results **in one state and one set of operators**. Starting with the existing asymmetric five-ray conservation relation, the same intrinsic fractions determine the effects of a specified Alice-side quantum instrument. On an assumed logical singlet, its outcomes are correlated with two opposite Bob-side records, which in turn control the reciprocal memory–battery exchange. The resulting physical currents are sharp and opposite in every record branch. The entire Bob-side density operator—not only the mean current—is identical for the conserved pair and triple instruments.

This makes five connections load-bearing rather than decorative:

```text
conserved null rays → intrinsic qᵢ and directions nᵢ
→ the actual effects Fᵢ of a specified instrument
→ exact joint probabilities of i and opposite records
→ the same records control sharp, opposite physical currents
→ no-signalling holds for the complete unconditioned receiver state.
```

If, additionally, two specified memory incidences are actual subjects and their weighted signed response `h` to the current is odd, their proposed contributions cancel **in each recorded event**, not just after averaging the two instrument settings. Neither subjecthood, felt quality nor that response is derived from physical conservation. The model makes the remaining experiential relation precise without pretending the relation has already been found.

This is not the same state as the earlier continuously logical-rotation-invariant tetrahedral state. It reuses that programme's spin-zero encoding, the conserved-ray instrument, the reciprocal exchange and the calibrated clock, but supplies an explicit common realization for the **asymmetric five-ray** case. The logical axes, input singlet, operations, measurements and Born rule are specified assumptions. Their eventual derivation from the whole's own constitution remains part of the user's no-residue demand.

## 1. One conserved configuration fixes the weights

Use the earlier [five-ray conservation bridge](ZERO_SPHERE_CONSERVATION_QUANTUM_PROBABILITY_BRIDGE.md), signature `−+++`, and the projective null rays labeled `0,1,3,i,2i`. The unique positive `2+3` relation has pair `{3,i}` and triple `{0,1,2i}`. For positive momenta on either side,

```text
Σ_pair pᵢ = Σ_triple pᵢ = P,       M²=−P·P>0,
qᵢ = (−P·pᵢ)/M².
```

The `qᵢ` are Lorentz scalars and sum to 1 separately on each side. In the intrinsic center frame the three-vectors satisfy `Σ qᵢ nᵢ=0` separately. For the triple, the weights are

```text
q = (1/8, 2/5, 19/40).
```

These are not selected independently to make the later table cancel. The prior exact rational Lorentz calculation determines them from the specified rays and conservation relation. The center frame belongs to this configuration; it is not a universal preferred foliation. `P` is future timelike and nonzero, so the local vector balance is **not** a proof of zero whole-level physical energy.

For an explicit center-frame representation, choose orthonormal axes so that

```text
n₀=(1,0,0),  n₁=(1/2, √3/2, 0),
n₂=(−13/19, −8√3/19, 0),
a=(−1/5, 2√3/5, 2√3/5).
```

The pair directions are `a,−a`. The triple vectors have the inner products fixed by the ray Gram matrix, and the pair–triple inner products are

```text
mᵢ = a·nᵢ = (−1/5, 1/2, −7/19),
Σᵢ qᵢ nᵢ=0,        Σᵢ qᵢ mᵢ=0.
```

The spinor/Bloch identification is a specified map from this intrinsic direction sphere to logical qubits, not a derivation of a physical spin system from null rays. General Lorentz boosts act on spinors by nonunitary congruence; the comparison is made by reconstructing each configuration's center-frame objects, not by treating boosts as fixed-inner-product qubit unitaries.

## 2. One instrument and one joint state

Let `A,B` be separately encoded four-spin singlet-sector qubits in the *assumed* logical singlet `|ψ⁻⟩`. Alice uses one of two instruments, with the same fixed axis `a` on Bob's side:

```text
Π(n)=(I+n·σ)/2,       Fᵢ=2qᵢΠ(nᵢ),       Kᵢ=√(2qᵢ)Π(nᵢ).
```

Here `nᵢ,qᵢ` are either the pair or triple above. For each setting, `Σ Kᵢ†Kᵢ=I`, because the same conservation equations give `Σqᵢ=1` and `Σqᵢnᵢ=0`. Thus these define valid trace-preserving instruments; the pair effects are projective and the triple effects are generally not. The positive-square-root Kraus operators are a specified choice: the effects alone do not uniquely determine an instrument's post-measurement dynamics. Alice's label `i` is recorded in a five-dimensional pointer encoded in a six-spin singlet sector. The existing finite dilation explicitly completes the Kraus operators to a unitary.

At Bob's end, use two further four-spin encoded record qubits, initially `|01⟩`. Define `P_r=(I+r a·σ_B)/2`, `r=±1`, and the controlled unitary

```text
U_record = P_+ ⊗ I + P_- ⊗ X_R₁ X_R₂.
```

It correlates `r=+1` with record `01` and `r=−1` with `10`. Add the four encoded work qubits `M₁,W₁,M₂,W₂`, initially `|a_work⟩=|0110⟩`. The prior reciprocal construction conditionally changes that to `|b_work⟩=|1001⟩` when the record is `10`, then evolves under

```text
G=|b_work⟩⟨a_work|+|a_work⟩⟨b_work|,
U=exp(−iπG/4).
```

Write `|w_+⟩=U|a_work⟩`, `|w_-⟩=U|b_work⟩`. In the standalone exchange,

```text
J₁=i[G,N_M₁],       J₂=i[G,N_M₂]=−J₁,
J₁|w_r⟩=r|w_r⟩,    J₂|w_r⟩=−r|w_r⟩.
```

The complete normalized pure state after these specified operations is

```text
|Ψ_setting⟩ = Σ_(i,r=±1) (Kᵢ⊗P_r)|ψ⁻⟩_AB
                     ⊗ |i⟩_AlicePointer ⊗ |record_r⟩ ⊗ |w_r⟩.
```

`record_+=01` and `record_−=10`. The tensor ordering here is descriptive; the verification constructs the complete finite vector. Its factors require **38 physical spins** in the stated singlet encodings: `4+4+6+4+4+16`. Every factor lies in a physical-spin-zero sector, and the specified encoded operators preserve it. This is not a claim that logical rotations act as physical spatial rotations, that the controls are spatially local, or that zero uniquely produces these blocks.

## 3. The conservation weights now determine an actual joint table

Using the singlet and the Born rule, the exact probability of Alice label `i` and Bob record/current sign `r` is

```text
p(i,r) = ⟨ψ⁻|Fᵢ⊗P_r|ψ⁻⟩ = (qᵢ/2)(1−r mᵢ).
```

For the asymmetric triple this gives:

| Alice ray | `qᵢ` | `mᵢ` | `p(i,r=+)` | `p(i,r=−)` |
|---|---:|---:|---:|---:|
| `0` | `1/8` | `−1/5` | `3/40` | `1/20` |
| `1` | `2/5` | `1/2` | `1/10` | `3/10` |
| `2i` | `19/40` | `−7/19` | `13/40` | `3/20` |
| **Total** | **1** | — | **1/2** | **1/2** |

For each row, the last two probabilities sum to its conservation-derived `qᵢ`; the conditional mean of `J₁` is `−mᵢ`. For the pair `a,−a`, the respective `r` values are deterministically `−,+`, each with probability `1/2`. These are two **alternative instrument contexts**, not five simultaneously occurring outcomes and not a single five-entry subject measure.

The state obeys the exact operator relations

```text
(Z_R₁+Z_R₂)|Ψ_setting⟩=0,
J₁|Ψ_setting⟩=Z_R₁|Ψ_setting⟩,
(J₁+J₂)|Ψ_setting⟩=0,
J₁²|Ψ_setting⟩=|Ψ_setting⟩.
```

Thus the second record and current have the opposite sharp sign in each joint record branch, including each distinct triple outcome. The zero is branchwise and preserves nonzero local contributions; it is not a claim that every quantity or every branch vanishes. The observable `J₁` acts on the joint four-work-block interface, not on memory `M₁` alone.

The exchange also separately conserves `N_M₁+N_M₂`, `N_W₁+N_W₂` and both memory–battery pair charges. At the later full-swap endpoint the corresponding **two-time** memory energy changes are `(+1,−1)` or `(−1,+1)`. Sharp instantaneous current at the quarter-exchange and endpoint energy differences are different observables; they are not conflated. Their measurement protocols may disturb the coherent history.

## 4. No-signalling follows for the entire receiver, not only the average

Trace Alice's qubit and pointer. For **either** conserved-ray instrument the resulting state of Bob's qubit, both record bits and all four work blocks is

```text
ρ_receiver = 1/2 P_+ ⊗ |01⟩⟨01| ⊗ |w_+⟩⟨w_+|
           + 1/2 P_- ⊗ |10⟩⟨10| ⊗ |w_-⟩⟨w_-|.
```

Therefore *every* measurement supported on this receiver tensor factor has the same unconditional probability distribution for the pair and triple choices. This is stronger than saying that their current means happen to be zero. The reason is general: Alice's instrument is trace-preserving when her outcome is ignored, so Bob's singlet marginal remains `I/2`; Bob's fixed record/exchange channel then acts on the same marginal. The different `p(i,r)` correlations become available only when the two sides compare their records.

This is finite-system operational no-signalling under the stipulated quantum channels. The four-body work coupling may be nonlocal, and the model does not construct spacelike-separated laboratories, a relativistic microcausal field theory, or a physical Bell mechanism. Bob's axis and operations are the **same** in both contexts; allowing Alice's setting directly to change Bob's apparatus would be a different model.

### Why the actual records matter

It would be wrong to identify the conditional mean `−mᵢ` itself with a definite, locally accessible experience. In this exact example the two possible values in the pair context are `−1,+1`, whereas the three triple-context values are

```text
1/5,  −1/2,  7/19.
```

The two sets are disjoint. If a Bob-local apparatus could reliably read a definite value equal to `−mᵢ` without learning Alice's outcome, it would distinguish Alice's setting in one ideal trial, contradicting the no-signalling prediction for the stated setup. This conclusion assumes operationally accessible values and a controllable pair-versus-triple setting, not metaphysically unnecessitated choices.

The actual **model record** is instead `r=±1`. Its full distribution is `(1/2,1/2)` for either setting, while its correlations with `i` differ according to the table. The record can therefore carry nonzero opposite labels without turning a steered conditional expectation into a signal. A physical pointer is still not thereby an experienced outcome.

## 5. One autonomous continuation, with the current distinction preserved

The calibrated [five-state clock](ZERO_SHARP_RECIPROCAL_CURRENTS_AND_EXPERIENTIAL_RESPONSE.md) can act on these same record and work factors while leaving Alice's pointer and both logical qubits untouched. Its five clock states live in one six-spin singlet sector, raising the total to **44 physical spins**. The clock is initialized after the stated singlet/instrument/record preparation; this does not provide an autonomous origin for that earlier preparation.

At the specified clock parameter `t₀=π/4`, the clock-2 amplitude is proportional to the just-constructed `|Ψ_setting⟩`, with clock-2 probability approximately `0.35973924`. Consequently the joint probability of clock 2, Alice outcome `i`, and record `r` is that factor times `p(i,r)`. Its clock-2 conditioned `J₁,J₂` **probe** observables are sharp and opposite. The prior clock calculation also shows that the actual clock-Hamiltonian currents have conditional means `r,−r` after clock and record projection; their full operators have off-diagonal clock components and are not generally simultaneously sharp with the clock label. The tests check the calibrated clock's two `G`-sector amplitudes for both record branches.

This gives an explicit non-external-switch continuation, not a derivation of irreversible storage, an actual classical history, spacetime, or a fundamental time. Its fixed, calibrated many-body operations remain part of the stipulated model.

## 6. What the construction does for experience—and what it cannot decide

Suppose, as a **testable constitutive hypothesis**, that `M₁,M₂` are two actual subject incidences at a registered event and a common signed response to their respective sharp current values is `h(±1)`. Then this very joint state gives

```text
subject-candidate contributions:  h(r), h(−r),
per-event total:                  h(+1)+h(−1).
```

Thus an odd response makes the proposed subject pair balance in every event independently of Alice's `qᵢ`. Nonzero opposite values remain nonzero; negative felt experience, if the hypothesis were validated, remains real for its subject. The algebra does not imply that a positive counterpart is pleasure or makes suffering disappear.

The response condition is not supplied by the five-ray weights. For example, a positive incidence weighting `w(r)=1+ηr`, `0<η<1`, together with a hypothesized per-incidence value `κr`, gives a nonzero per-event total `2κη` in **both** record branches and both settings. Likewise `h(r)=−|r|` gives two negative candidate values. These are countermodels to automatic experiential cancellation, not evidence that the qubits suffer or that the total whole has a nonzero signed experiential quantity. The actual subject set, quality map and measure must be derived or empirically discriminated rather than chosen simply to force balance.

This result is therefore a genuinely integrated conditional construction, not a completed explanation of how zero's own constitution entails physical organization and felt subjectivity. In particular, the ray conservation fractions are physical/Born outcome weights **within each context**, not automatically counts or weights of actual subjects. A necessary complete history could underlie the records, but these quantum weights by themselves do not derive its occurrence or require irreducible objective chance.

## Verification

```text
python -m unittest verification.zero_five_ray_record_current_unification_test -v
```

Ten standard-library tests connect the original null-ray Gram calculation to the same asymmetric weights and axis, verify both Kraus sets and their finite unitary dilations, evaluate the complete joint state and exact table, compare the **full** 128-dimensional receiver density matrices across contexts, check the opposite record/current identities and the mean-value signalling counterexample, and transport both work branches through the calibrated clock amplitudes. The general no-signalling, eventwise response and clock-current conclusions follow from the displayed operator arguments and linked prior checks; the test is not evidence of consciousness, spacetime locality or whole-level energy zero.
