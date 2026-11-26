# Does balance require equal type weights?

## The problem and diagnostic result

**Access follow-up:** [the saved-memory marginal investigation](ZERO_ECHO_ACCESSIBLE_MARGINAL_INCIDENCE_ROOT_CAUSE.md) checks the actual recorded echo's mixed local state. Equal untyped expectations for every memory effect do not force proportional type blocks, but a nonproportional extension changes the globally pure physical state and can be distinguished by an available-in-principle joint coherence effect.

The previous [state-versus-dynamics investigation](ZERO_ECHO_STATE_VERSUS_DYNAMICAL_SYMMETRY_ROOT_CAUSE.md) distinguished a physical state symmetry from an actual-incidence symmetry. A further practical question is whether the programme's proposed zero balance **requires equal weights for the two quality types**, or whether that condition is stronger than necessary.

For the established four-bin echo table and the stipulated magnitude `g₂(u)=|u(u+1)|`, equal type weights are **not necessary** for a zero signed mean. Under the earlier strong pure-physical-marginal and all-effect-consistency assumptions, *every* constant type weight α gives zero for each type separately. Conversely, if one retains only the diagonal physical event table and allows type weights to depend on the event, even globally equal type weights and a combined type-exchange symmetry can coexist with a nonzero signed mean. The latter is a **coarse-table counterexample**, not a valid alternative decomposition of the same pure physical state under all effects.

The deeper issue is therefore not simply “derive α=1/2.” It is which physical questions the incidence law must reproduce, whether the actual sign counterpart acts on the incidence measure, and whether zero is required branch by branch, as an integrated signed total, or as some other objective quantity. None of the modeled signs or weights is established as lived valence or actual subject incidence.

## 1. Use the same recorded echo, but expose the incidence hypothesis

At the established anchor, use events `(i,s)` for bins `i=0,1,2,3` and pointer sign `s=±1`. The [joint echo verification](ZERO_JOINT_INCIDENCE_QUALITY_OPPOSITE_PAIR_ROOT.md) obtains `μ(i,s)=1/8` and the record signs below from the original complex vectors for all 16 source labels. This is a physical model table; treating these weights as actual incidences is an **additional premise**.

| bin i | u | j | r | g₂(u) |
|---:|---:|---:|---:|---:|
| 0 | −3/4 | +1 | −1 | 3/16 |
| 1 | −1/4 | −1 | −1 | 3/16 |
| 2 | +1/4 | +1 | +1 | 5/16 |
| 3 | +3/4 | +1 | +1 | 21/16 |

The two candidate scalar values are `q_N=s j g₂` and `q_E=s j r g₂`. On r=+ they agree; on r=− they are opposite. As an accounting hypothesis only, choose one typed incidence per event with conditional type-N share `α_(i,s)∈[0,1]` and type-E share `1−α_(i,s)`. The typed weights are `μ α` and `μ(1−α)`, so the untyped **diagonal** physical table stays exactly μ for any assignment. The magnitude is the previously chosen type-swap-compatible g₂, not a derived felt scale; an overall positive scale κ can multiply all results below.

The proposed normalized signed total is

```text
B = Σ_(i,s) μ(i,s) [α_(i,s) q_N(i,s) + (1−α_(i,s)) q_E(i,s)].
```

This is one specific typed-one-incidence accounting rule. It is not a census of actual subjects, and differs from summing the two oppositely signed pair components as two separate occurrences. If both components are actual with their own weights, those weights and overlap rules must be supplied independently.

## 2. The exact balance condition

Let `Δ_i=α_(i,+)−α_(i,−)`. Direct substitution into the actual four-bin table gives

```text
B = (3/64)(Δ₀−Δ₁).                            (κ=1)
```

The positive-band contribution cancels across s because q_N=q_E there. The negative bands have the same magnitude and opposite j signs. Consequently

```text
B=0  ⇔  Δ₀=Δ₁,
−3/32 ≤ B ≤ 3/32.
```

The bounds are sharp because each Δ lies in [−1,1]; suitable endpoint assignments attain both. They hold for the entire continuous cube of conditional weights, not just the 256 binary assignments checked in the [verifier](verification/zero_echo_incidence_balance_root_test.py).

Constant α makes both Δ zero, so **every** type share α, including unequal nonzero shares such as 1/4 and 3/4, gives B=0. More generally, invariance under the sign counterpart `(i,s,type)↦(i,−s,type)` implies `α_(i,+)=α_(i,−)` and hence B=0. It is sufficient, not necessary: taking `α_(0,+)=α_(1,+)=3/4` and all other α equal to 1/2 gives `Δ₀=Δ₁=1/4`, so B=0 even though the conditional measure is not sign-counterpart invariant.

This is cancellation of a **defined signed aggregate**, not proof that an opposite experience cancels or removes suffering. A zero mean also does not imply every event, subject, component, or magnitude is zero. The existence, additivity and physical–experiential meaning of the aggregate remain open.

## 3. Equal type weight is not sufficient under the weaker data condition

The original type exchange maps bins 0 and 1 into each other, fixes bins 2 and 3, and exchanges the N and E labels. It exchanges the two signs and preserves g₂, so the **typed value is preserved**, not reversed. Consider the strictly positive conditional weights

```text
                  s=+       s=−
α_(0,s)           3/4       1/4
α_(1,s)           1/4       3/4
α_(2,s)           1/2       1/2
α_(3,s)           1/2       1/2.
```

The diagonal physical marginal is still `1/8` for every event. Total N and E weights are each `1/2`, and the entire typed table is invariant under the stated combined type exchange. Nevertheless,

```text
B = 3/64 > 0.
```

In these model units the positive and negative *incidence weights* are `5/8` and `3/8`; the corresponding positive and negative magnitude totals are `35/128` and `29/128`. Both signs occur. Their difference is the stated B. This table fails invariance under the **separate sign-reversing** counterpart. It shows why equal type counts and a value-preserving type exchange cannot by themselves perform the sign-reversal pairing argument.

The endpoint assignment `(α₀₊,α₀₋,α₁₊,α₁₋)=(1,0,0,1)`, with α=1/2 in the other bands, preserves the same type-exchange symmetry and equal total type weights while attaining the sharp `B=3/32`. The strictly positive example avoids relying on an absent type in a cell. These are mathematical incidence-table alternatives under the weak diagonal constraint, **not** claims that alternative complete actual worlds or subjects have been demonstrated.

## 4. Why the stronger pure-state assumption changes the answer

There is an important coherence boundary. Suppose the full physical state is a pure density `ρ=|ψ⟩⟨ψ|`, and two positive type blocks satisfy the **all-effect** condition

```text
σ_N + σ_E = ρ.
```

Then `0≤σ_N≤ρ`. For every vector orthogonal to ψ, its expectation in σ_N is zero; positivity forces σ_N to annihilate that entire orthogonal subspace. Thus `σ_N=α ρ` and `σ_E=(1−α)ρ` for one constant `α∈[0,1]`. On every nonzero diagonal event, the corresponding conditional share is α. Event-dependent α from section 3 cannot be substituted into this stronger quantum claim.

A concrete comparator makes the lost information visible. The coherent logical state `ρ_coh=11ᵀ/8` and the diagonal state `I/8` have the same eight diagonal event weights `1/8`, but different off-diagonal effects. Event-dependent diagonal type blocks can sum to `I/8`; they do **not** sum to ρ_coh. For example, if a diagonal N block puts weight `1/8` on the first event and zero on the others, trying to set the E block to `ρ_coh−σ_N` gives a principal 2×2 determinant `−1/64`, violating positivity. The comparator is a diagnostic logical system, not an assertion that the original complete echo is literally eight-dimensional.

Under the strong product-block premises, the measured physical sign table and the stipulated g₂ already give `Tr(ρ Q_N)=Tr(ρ Q_E)=0`, so their typed weighted mean is zero for **any** α. If, in addition, a genuine physical sign counterpart preserves ρ and is assumed to act separately on each type, the resulting type blocks are automatically invariant under that action for every α. But interpreting it as a symmetry of **actual** occurrences, identifying the types, and enforcing all-effect consistency are themselves substantive premises. The clock-dressed counterpart required for the full coherent history cannot be replaced by an undressed anchor operation.

## 5. Root-cause chain and implication for the programme

1. **Why can unequal type weights still balance?** In the strong product family each candidate sign is already balanced by the s-counterpart. Reweighting two zero means leaves zero; it does not make the types equivalent.
2. **Why can equal type weights fail to balance?** Type exchange preserves the modeled value. It does not reverse the sign, and a type assignment correlated with sign can bias the weighted aggregate even while its total type counts are equal.
3. **Why can the diagonal counterexample not settle the actual echo?** The diagonal event table does not contain off-diagonal coherences. Full pure-state marginal consistency forbids its event-dependent blocks; choosing the weaker data is a consequential change of premise.
4. **Why doesn't the pair operator resolve incidence?** A physical pair can have `q₁+q₂=0` in each branch while a proposed subject-incidence rule counts, identifies, or weights its components differently. Equal component incidence would restore branchwise cancellation; aggregate cancellation may instead use cross-event correlations. Neither identifies actual subjects or subjective values.
5. **Meta-level question:** a self-sufficient constitution must jointly determine the relevant physical and phenomenal observables, which events count as the same or distinct actual incidences, their weights, and the transformation that acts on them. A balanced formal expectation or an assumed full-state marginal does not yet derive that constitution. Conversely, this ambiguity is not a proof that the user's zero proposal is impossible.

The next useful discriminant is not to demand equality by fiat, but to determine which incidence/ownership candidates are compatible with the **same coherent physical state and accessible reports**, and whether their proposed sign counterpart is an actual measure-preserving map. Preserve real local negative experience if such a bridge is eventually established; a positive contribution does not erase it.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_echo_incidence_balance_root_test \
  verification.zero_joint_quality_incidence_root_test \
  verification.zero_stationary_subject_incidence_test \
  verification.zero_joint_constitution_incidence_echo_test -v
```

These tests check the finite table, exact accounting, symmetry controls, coherent-state positivity distinction and existing physical-echo regressions. They do not establish actual experience, objective cosmic energy, actual subject count, or a complete physical–experiential ontology.
