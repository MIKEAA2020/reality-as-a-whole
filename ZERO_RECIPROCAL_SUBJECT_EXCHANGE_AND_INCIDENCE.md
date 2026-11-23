# Reciprocal subject-candidate exchange within the spherical whole

**Sharp-current continuation:** [the experiential-response analysis](ZERO_SHARP_RECIPROCAL_CURRENTS_AND_EXPERIENTIAL_RESPONSE.md) identifies an exactly sharp opposite-current stage, embeds it in a five-state autonomous clock with a nonzero clock-conditioned actual-current mean, and proves the precise odd-response condition for pairwise balance. The full clock current is not generally sharp, and neither subjecthood nor felt quality is inferred.

## What is new

The previous [relational sphere construction](ZERO_RELATIONAL_CONSTITUTION_TO_CONSERVED_RECORD_TRANSFER.md) correlated one energized memory with a battery loss. That was a genuine conserved transfer, but it left an important gap: the proposed subjects could not be made to balance merely by pointing to an unexperienced battery.

Here the **same uniquely selected spherical record state** controls a reciprocal exchange in which *both* memory candidates undergo nonzero changes, equal and opposite to each other. Each also exchanges energy with its own battery; the two batteries separately balance as a group. The signs are not painted on afterward: they follow from a specified Hamiltonian and the earlier directional record. An autonomous clock version embeds preparation, the reciprocal exchange and reset in a single time-independent Hamiltonian.

There is also a precise negative result: **even symmetric, positive, exchange-covariant incidence weights can spoil the subject-candidate balance**. Equal weighting cannot be derived simply from symmetry. This calculation locates the substantive experiential issue rather than hiding it in an accounting convention.

The finite construction does not show that memories are actual subjects or that gains and losses are pleasure and suffering. Both are hypotheses to be tested, not definitions of experience. Its physical charges and zero penalty do not establish an objective whole-level energy zero or a complete zero-residue ontology. The stronger thesis remains that zero's own constitution should determine physical organization *and* actual experience; the following makes one part of that demand more exact.

## 1. Bring the earlier correlated sphere into the exchange

Use the previous encoded 22-spin system with tetrahedral reference `C`, logical qubits `A,B`, and record qubits `R_A,R_B`. Its specified relational constraints select the invariant joint state `|Ω⟩`. For each reference label `i` and record pair,

```text
R_A R_B = 01  ⇒  n_i·σ_A = +1,  n_i·σ_B = −1,
R_A R_B = 10  ⇒  n_i·σ_A = −1,  n_i·σ_B = +1.
```

The statements are conditional Born-rule correlations: each of the eight label/record pairs has weight `1/8`. They do not alone select an actual record or subject.

Add the same four spin-zero encoded qubit blocks used previously: two candidate memories `M₁,M₂` and two batteries `W₁,W₂`, in order `(M₁,W₁,M₂,W₂)`. Initially use `|0110⟩`. Let `N_j=|1⟩⟨1|_j`; define the bare total

```text
H₀ = N_M₁ + N_W₁ + N_M₂ + N_W₂.
```

The initial value is 2, not 0. All logical factors live inside specified physical spin-singlet sectors. There are **38 physical spins** before adding the clock. The encoded factorization, initial preparation, physical interpretation of `N`, and interactions are inputs, not derived from zero.

## 2. A four-body exchange with two independently balanced sectors

On the four added qubits define

```text
|a⟩ = |0110⟩,       |b⟩ = |1001⟩,
P_ab = |a⟩⟨a| + |b⟩⟨b|,
G = |b⟩⟨a| + |a⟩⟨b|,       G²=P_ab.
```

`G` vanishes outside this two-state sector. With `ħ=1`, set `U(t)=exp(−itG)`. This is a four-block correlated exchange, not a claim about realistic spatial locality. It conserves all four quantities

```text
N_M₁+N_W₁,      N_M₂+N_W₂,
N_M₁+N_M₂,      N_W₁+N_W₂.
```

The first two give each memory its battery counterflow. The latter two mean the memories' aggregate energy and the batteries' aggregate energy are **separately** conserved for *every state*. In particular, using `J_X=i[G,N_X]`,

```text
J_M₁ = −J_M₂ = −J_W₁ = J_W₂                         (operator identities).
```

These are stronger than cancellation in a selected average. The memory-only relation does not require counting batteries as subjects. It does, however, use an explicitly engineered correlated interaction; it is not a consequence of arbitrary energy conservation.

Correlate the initial exchange orientation with the prior record by the unitary

```text
X_ab = I − P_ab + G,
V_prep = |0⟩⟨0|_R_A ⊗ I + |1⟩⟨1|_R_A ⊗ X_ab,
|Ξ(0)⟩ = V_prep (|Ω⟩ ⊗ |a⟩).
```

Thus record `01` has exchange initial state `|a⟩`, and record `10` has `|b⟩`. `V_prep` is reversible, acts only on the scalar record and exchange blocks, and commutes with all four conserved quantities. It can itself be generated in a finite interaction interval by the specified Hamiltonian `(π/2τ)|1⟩⟨1|_R_A (P_ab−G)`; no universal measurement processor is claimed. Define `|Ξ(t)⟩=(I⊗U(t))|Ξ(0)⟩`.

For `0<t<π/2`, conditioning on the record gives

```text
                         R_A R_B=01       R_A R_B=10
⟨J_M₁⟩                     +sin(2t)          −sin(2t)
⟨J_M₂⟩                     −sin(2t)          +sin(2t)
⟨J_W₁⟩                     −sin(2t)          +sin(2t)
⟨J_W₂⟩                     +sin(2t)          −sin(2t).
```

Here these are *conditional quantum expectations*, not direct readouts of feeling; they do not generally imply sharp current values. There is an important exception: [the sharp-current continuation](ZERO_SHARP_RECIPROCAL_CURRENTS_AND_EXPERIENTIAL_RESPONSE.md) shows that at `t=π/4` both opposing currents are sharp in each record branch and exactly correlated with the reference. The unconditional `⟨J_M₁⟩` is zero, because the two record branches have equal weight. At the writing endpoint `t=π/2`, the conditional mean currents vanish while the endpoint energy changes are nonzero:

| Record | A spin along reference | `(ΔN_M₁, ΔN_M₂)` | `(ΔN_W₁, ΔN_W₂)` |
|---|---:|---|---|
| `01` | `+1` | `(+1,−1)` | `(−1,+1)` |
| `10` | `−1` | `(−1,+1)` | `(+1,−1)` |

There is one unit of memory gain **and** one unit of memory loss in each record branch. This is a real improvement over assigning a negative feeling to a blank bit: if the memories were subjects and felt value could be identified with their signed energy changes, neither side would need to be replaced by a battery or by the absence of an experience. But those two italicized identifications remain unestablished.

The initial and final energy values can be compared with an explicitly specified two-time projective energy-measurement protocol, conditional on the record. Such a protocol can disturb coherent histories; the pure unmeasured state is not itself a selected classical trajectory. At this endpoint the initial local energies commute with their corresponding endpoint change operators, but instantaneous current and local energy need not be simultaneously sharp.

## 3. The sphere–record–current relation is one equation, not an analogy

Let the earlier direction-controlled observable be

```text
T_dir = Σ_i |i⟩⟨i|_C ⊗ (n_i·σ_A) ⊗ I_B.
```

On the selected sphere state, `T_dir` and `Z_R_A` have the same recorded sign. In the exchange model the coherent whole obeys

```text
⟨T_dir J_M₁⟩_t = ⟨Z_R_A J_M₁⟩_t = sin(2t),
⟨J_M₁⟩_t = 0,
T_dir (N_M₁−N_M₂)|Ξ(π/2)⟩ = |Ξ(π/2)⟩.
```

The products act on different factors and commute. These statements connect the reference direction, its record, the sign of local exchange, and the final memory distinction in the **same quantum state**. They are not just separately normalized sums. They do not make a continuous direction eigenket available, turn the four-label device into a universal sharp-direction processor, or identify logical rotations with physical spacetime rotations.

The joint coherence constraint from the previous report is transported with the interaction: if `V(t)=U(t)V_prep`, then

```text
V(t) Q V(t)† |Ξ(t)⟩ = |Ξ(t)⟩.
```

The original untransported `Q` has expectation zero after the record-controlled preparation: the relation has become a joint record–exchange coherence, not a local record quality. A state selector for each fixed `t` can be obtained by conjugating the earlier unique gapped selector `H_rel` and a four-qubit penalty whose unique ground is `|0110⟩`:

```text
H_aux = N_M₁+(I−N_W₁)+(I−N_M₂)+N_W₂,
H_sel(t) = V(t) [H_rel⊗I + I⊗H_aux] V(t)†.
```

Each `H_sel(t)` has unique zero ground `|Ξ(t)⟩`, gap 1 in the stipulated encoded space, preserves the displayed physical charges and is invariant under the specified logical continuous rotations. This is a *family of tailored selectors*, not the autonomous Hamiltonian generating the trajectory and not a relaxation process. A zero of this positive operator is not by itself a cosmological energy zero.

## 4. One autonomous clock–record construction

To avoid assuming that an outside agent switches the preparation and exchange, add a six-spin singlet-sector clock with four states `|0⟩,…,|3⟩`; the total is now **44 physical spins**. Take

```text
V₀=I,      V₁=V_prep,      V₂=U(π/2)V_prep,      V₃=I,
K = Σ_(k=0)^3 |k⟩⟨k| ⊗ V_k,
A = Σ_(k=0)^3 (|k+1 mod 4⟩⟨k| + |k⟩⟨k+1 mod 4|),
H_clock = H₀ + g K(A⊗I)K†,     g>0.
```

The ordered link operations are `V₁`, `V₂V₁†`, `V₃V₂†`, `V₀V₃†`; their product around the cycle is identity. Every `V_k` preserves each of the four physical charges above, so `H_clock` does too. All work interactions are logical-rotation scalars and act in physical singlet blocks. This is one time-independent, closed Hamiltonian—not a claim that its interactions are local, naturally realized or compelled by zero.

With the clock initially `0`, the prior selected work state and the indicated `|a⟩`, the four clock-conditioned work states are, respectively, initial, correlated preparation, reciprocal-exchange endpoint, and reset. Ignoring the common `H₀=2` phase, their clock amplitudes at parameter `t` are

```text
cos²(gt),  −i sin(gt)cos(gt),  −sin²(gt),  −i sin(gt)cos(gt).
```

At `gt=π/2`, clock 2 has probability 1 and the endpoint table applies; at `gt=π`, the initial state recurs. At clock labels 1 and 2, conditioning gives the corresponding prepared and exchanged records. The continuous-current formulas in §2 refer to the standalone `G` interaction, not to the clock Hamiltonian's instantaneous currents. The clock is periodic, its conditions can be superposed, and the setup does not produce an irreversible classical sequence or select an actual experience. The evolution parameter and clock are part of this finite model, **not** a preferred fundamental spacetime foliation.

## 5. An exact test of the experiential bridge

Consider the specific candidate hypothesis:

- the two memory blocks, and not their batteries, each constitute an actual subject incidence;
- in a definite, suitably registered event, its signed contribution is `v_j=κ ΔN_Mj` with `κ>0`;
- both incidences have equal weight.

Then the endpoint table gives nonzero opposite subject-candidate contributions in each branch:

```text
(v₁,v₂) = (+κ,−κ)  or  (−κ,+κ),       v₁+v₂=0.
```

A current-based version would use the conditional rates in §2 and integrate over the specified interval. Neither proposal asserts that an unconditional quantum expectation is itself a locally accessible feeling. Both still owe an independent account of actual subjects, felt character, sign, the unit `κ`, occurrence, and the correspondence to a physical history. If the negative value represents real suffering, the other contribution does not make that suffering unreal or justify it; and the opposite positive number is not automatically pleasure. The exchange algebra does not resolve the user's deeper question of what can actually counterbalance experience.

The extra equal-incidence premise is mathematically consequential. Let the endpoint change operators on the initial work space be

```text
D_j = U(π/2)† N_Mj U(π/2) − N_Mj.
```

For the constructed exchange, `D₂=−D₁` and `D₁²=P_ab`. For real `0<η<1`, choose the **positive** history-dependent candidate weights

```text
W₁=I+ηD₁,      W₂=I+ηD₂.
```

They have eigenvalues among `1−η,1,1+η`, so they are strictly positive and commute with the changes. A swap `S_pair` of the two memory–battery pairs swaps both `D₁↔D₂` and `W₁↔W₂`: the rule is exchange-covariant. More strongly, the coherent prepared state itself obeys `(Q⊗S_pair)|Ξ(t)⟩=|Ξ(t)⟩` throughout the standalone exchange; here `Q` flips the two record branches with their associated singlet/triplet sign. Nevertheless,

```text
W₁D₁ + W₂D₂ = 2η P_ab.
```

The prepared state is entirely in `P_ab`, so the weighted signed total is `2η` (or `2κη` under the candidate valence scaling) in **either** record branch. Equal branch probabilities, separately conserved memory energy, nonzero opposite local changes, positivity, and exchange covariance therefore do not imply a zero incidence-weighted total. The weights are a *counterexample*, not a claim about actual conscious incidence; actual weights might instead be equal or satisfy some other balancing law. The calculation shows that the law must be supplied or derived, not silently assumed from physical symmetry.

For this pair with nonzero `v₁=−v₂`, independent positive scalar incidence weights `w₁,w₂` give `w₁v₁+w₂v₂=(w₁−w₂)v₁`; equal weights are necessary and sufficient for this particular event to balance. For a network, the earlier [overlap balance theorem](ZERO_SUBJECT_LOCALITY_AND_OVERLAP_WEIGHTED_BALANCE.md) gives the corresponding edge-weighted condition. These are conditional mathematical facts, not a proof that the relevant weights, subjects or formal alternative states are metaphysically possible whole worlds.

## 6. Consequence for the zero programme

The new construction connects the prior components at the level of equations:

```text
relationally selected sphere state
→ reference–record sign correlation
→ correlated, pairwise-conserving memory and battery exchange
→ nonzero opposite changes within the proposed subject pair
→ a conditional zero for equal actual incidence.
```

The first four arrows are established within the specified finite system; the last requires the stated experiential and incidence assumptions. A second, positive and symmetry-covariant incidence rule produces nonzero residue, so symmetry cannot substitute for a subject/measure principle. That is a precise target for the stronger view that zero's own constitution fixes both physical differentiation and experiential incidence—not a reason to weaken it or to pretend the remaining facts are harmless brute inputs.

The construction avoids a preferred cosmic foliation, and the selected equal Born weights are not a derivation of an actual history or an assertion of irreducible objective chance. It also does not derive continuum spacetime, physical locality, the interaction, subject unity, phenomenal quality, or cosmological energy zero. The next advance must address whether a non-circular subject-and-incidence principle follows from the whole's proposed constitution and discriminates genuine suffering from a merely signed physical transfer.

## Verification

```text
python -m unittest verification.zero_reciprocal_subject_exchange_test -v
```

The 11 standard-library tests verify the exchange generator and unitary, all four conserved quantities and current identities, direction/record preparation, conditional currents and endpoint changes, the exact positive-weight counterexample and exchange covariance, transported coherence, the gapped-selector construction, and the autonomous clock's Schrödinger amplitudes and endpoint/reset. The operator conservation and positive-weight equalities hold algebraically for all states; the clock's exact amplitude formulas and selector's spectral claims follow from the analytic constructions, with numerical checks at representative points. The tests do not verify subjecthood, felt valence, an actual history, spatial locality or whole-level energy.
