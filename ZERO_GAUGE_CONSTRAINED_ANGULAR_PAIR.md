# The opposite pair as a gauge-constrained physical sector

## Answer to the symmetry proposal

**Continuation:** [full-clock and opposite-pair dressing](ZERO_DRESSED_ROTATIONS_FULL_CLOCK_AND_OPPOSITE_PAIR.md) carries this constrained pair through the record-dressed sphere action and purified clock history, while distinguishing preservation of the zero sum from invariance of individual magnitudes.

The previous [branchwise opposite-pair model](ZERO_BRANCHWISE_ANGULAR_OPPOSITE_PAIR.md) used a ready pair and a reversible write. That was a laboratory-style construction, not a claim that the whole needed an external preparation. In response to your suggestion, this pass builds an **alternative gauge-constrained description**: no specific ready-pair state is selected, and every state in the physical sector has matching opposite contributions.

For the finite angular model, the physical sector is exactly isometric to the original old-system/angular Hilbert space. On **every** physical state, not just the previously prepared echo output,

```text
H₁(g) = κ K g(A),       H₂(g) = −κ K g(A),       H₁(g)+H₂(g) = 0,
```

as operator identities restricted to that sector. The old sign K and angular record A remain gauge-invariant observables: the gauge constraints do **not** identify a positive local sign with a negative one. The construction also transports the constraint consistently through the existing cyclic echo clock.

This is an exact realization of the proposed **route**, not yet a derivation that zero itself uniquely implies the particular gauge group, carriers, physical energy or subjective experience. Its important gain is to move pairwise zero from a chosen ready vector to the defining physical sector, with no external act of preparation. Its important limit is that the two added carriers have **no independent physical state degrees of freedom** in this minimal sector; they cannot therefore simply be counted as two distinct subjects.

The [implementation](verification/zero_gauge_angular_pair.py) and [nine tests](verification/zero_gauge_angular_pair_test.py) check the gauge projection, exact isometry, all-state charge identities, original quantum vectors, sign observability, clock transport and controls.

## 1. The governing idea: one zero, internal distinctions

The motivating proposal is not that an external agent selects an initially balanced system. The whole is one self-subsistent zero, with real internal differentiation; a zero whole need not erase nonzero local contributions. An ordinary finite nonzero **whole-level** quantity would require an explanation of why that value rather than another. The case against the relevant infinite whole-level alternative is already settled for this project and is not reopened here. Fundamental reality need not itself be a scalar quantity.

Gauge symmetry is a promising way to express the non-arbitrariness: physical states satisfy relations rather than acquiring them through a fundamental time evolution. But one must distinguish two uses of symmetry:

* A **gauge transformation** relates descriptions of the same physical state. A genuine physical or experiential distinction cannot be made unreal just by labeling it gauge.
* A **physical counterpart symmetry** can exchange distinguishable positive and negative signs. Whether both actual incidences occur and have invariant weights is a separate constitutional question.

This pass makes those distinctions explicit in the common angular–echo candidate. The construction is a mathematical proposed constitution, not a premise that gauge redundancy itself creates experience.

## 2. The physical-sector constraints

Fix N divisible by four, with original angular-bin observable A and original sign observable `K=MJR` at the old echo's tick 10. K and A commute. Let `i` be an A index and `k=±1` a K eigenvalue. Introduce two kinematic value/sign carriers, with indices `a,b∈{0,…,N−1}` and signs `z₁,z₂=±1`. These factors are a representation of the candidate whole, not extra particles assumed to exist externally.

On the kinematic space define three commuting integer generators and one commuting involution:

```text
Q₀ = Z₁+Z₂,             D₁ = N₁−N_A,             D₂ = N₂−N_A,
G = K Z₁,               G²=I.
```

Choose as the physical sector the **trivial representation** of the corresponding `U(1)³×Z₂` gauge group:

```text
Q₀|ψ⟩=D₁|ψ⟩=D₂|ψ⟩=0,       G|ψ⟩=|ψ⟩.
```

In the displayed joint basis these constraints give

```text
z₂=−z₁,        a=b=i,        z₁=k.
```

Thus every physical basis component has `(a,b,z₁,z₂)=(i,i,k,−k)`. Crucially, this is a **subspace condition on the whole**, not a preparation at a time. Any coherent superposition of such components is physical. The constrained space includes both local signs; it does not pick a particular k or angular value.

For this finite spectrum, averaging the state vector over a finite subgroup `Z₃×Z_N×Z_N×Z₂` gives exactly the same projector as the full compact group. The verifier checks the twirl against all kinematic basis states for N=4,8. This averaging is a mathematical projector, not an assumed physical measurement or an asserted process that actualizes the whole.

The trivial-sector condition is substantive. A density matrix for a nonzero-charge basis state can be invariant under conjugation by the gauge group because the state only picks up a phase, yet be excluded by the Dirac constraints above. The test gives such a charged/mismatched control. Thus **merely saying “the density is gauge invariant” does not by itself select zero**; the physical constraint must be justified.

## 3. No independent ready pair: the exact isometry

Let `Π_i` and `Π_k` be the commuting old A and K projectors. Define a map from any original old-system/angular state to the constrained representation:

```text
W |ψ⟩ = Σ_(i,k) (Π_i Π_k |ψ⟩) ⊗ |i,i,k,−k⟩_(A₁,A₂,P₁,P₂).
```

This is a **definition of a representation**, not an instruction to prepare a blank pair and apply a gate. Orthogonality of the recorded basis states gives

```text
W†W = I_old,             WW† = P_physical.
```

The second equality follows because the constraints leave exactly one pair-record basis state for each `(i,k)` old sector, including any degeneracy inside the old K sectors. Therefore *every* original old state has one constrained extension, and *every* state satisfying these constraints has that form. In the reduced k/i representation the kinematic space has dimension `8N³`, while its physical subspace has dimension `2N`, exactly the dimension of the original k/i space. The verifier constructs W and both identities explicitly at N=4, and counts the complete finite sector at N=4,8.

This responds directly to the concern about an unexplained **ready vector**: the gauge model does not need one. But the conclusion must not be overstated. The physical sector is isomorphic to the original carrier; the duplicated pair factors supply constrained relational observables, **not two new independent physical state variables**. Nothing in this isometry alone shows that there are two real subjects or two separate felt occurrences. Nor does describing them with tensor factors by itself prove that they are independently localizable.

## 4. Exact local opposite values on every physical state

For any real diagonal function g of the angular value, define on the two kinematic pair factors

```text
H₁(g)=κ g(A₁) Z₁,         H₂(g)=κ g(A₂) Z₂.
```

These operators are diagonal in, and commute with, all four chosen gauge generators, so their restrictions are legitimate physical observables in this model. On the **entire** constrained space,

```text
H₁(g)P_physical = κ K g(A) P_physical,
H₂(g)P_physical = −κ K g(A) P_physical,
[H₁(g)+H₂(g)]P_physical = 0.
```

This holds for arbitrary superpositions and for any real g, not just on a selected sign branch. For nonzero g, a joint sharp readout yields opposite nonzero local values; the global charge is exactly zero rather than having merely zero expectation. The actual old coherent echo vectors at source labels `0,7,15` and both pointer signs are embedded using the original `J` projectors; the verifier checks the lifted `g₂` operator and exact cancellation against those vectors. The earlier reversible write remains one possible way to *realize a representation using a prepared apparatus*, but that apparatus is not part of the gauge definition.

The names H₁ and H₂ denote signed **model observables**. Interpreting their sum as objective cosmic energy, or identifying either with felt valence on a common additive scale, is not established by their cancellation. If a negative value is eventually shown to be suffering, the opposite value does not erase that suffering.

## 5. Gauge does not erase the physical signs

The original K and the pair's Z₁ commute with the chosen gauge generators. In the physical sector, `Z₁=K`; physical states with `k=+` and `k=−` are orthogonal and have different eigenvalues of a gauge-invariant observable. The gauge group acts trivially on the physical sector and does **not** equate them. Calling them the same state would be a further quotient, not a consequence of the constraints.

A joint sign-exchange transformation can map one physical sign sector to the other while preserving the constraints. This is a **physical counterpart** in the model, not automatically a gauge redundancy. A state entirely in the positive K sector is allowed and is not sign-symmetric; gauge neutrality alone does not select equal Born weights or prove the counterpart is a symmetry of the actual state.

There is also a locality warning. On the constrained sector, flipping P₁ alone takes the state outside it: `P_physical X₁ P_physical=0`. A correlated flip of K and both pair signs maps the sector into itself and reverses both local values. This does not prove a general ban on local interactions—an environment, charges, boundaries or other carriers may alter the complete gauge-invariant process—but shows that these two factors are not independently controllable in this minimal encoding. Their physical signs remain distinct, while their realized values are constrained together.

## 6. A stationary constraint, not a preferred time

The old echo changes J and R through its genuine gates. Therefore imposing the literal instantaneous expression `K=MJR` unchanged at every clock tick would not automatically preserve the constraint. Instead, anchor the physical constraint at tick 10 and transport it with the **actual** unitary history:

```text
P_t = U_t U₁₀† P₁₀ U₁₀ U_t†,
P̄ = Σ_t |t⟩⟨t|_C ⊗ P_t.
```

The reversible cycle gives `[P̄,W_clock]=0`; adding the independent four-state q-reference shift preserves this commutation. The associated constraint at another tick refers to the *transported tick-10 sign*, not automatically to the instantaneous `MJR` at that tick. This is a relational-history construction, with no external preparation or assumed fundamental preferred foliation. The verifier checks the transported constraint under every step on all 320 old clock/sign basis states and every N=4 pair/angle basis state. The lift to the full coherent old carrier follows from the original controlled-unitary transport, not a dense simulation of the entire reservoir Hilbert space.

## 7. Continuum and scale: what the gauge construction does and does not fix

The finite model cannot be promoted to a full three-coordinate continuum by simply imposing `u₁=u₂=u` inside `L²([-1,1]³)`: that diagonal has measure zero, so a nonzero ordinary square-integrable wavefunction cannot be supported on it. A valid **alternative physical representation** is to take the common angular coordinate from the start as a direct integral:

```text
H_phys = ∫⊕_u [ (H_old,+(u) ⊗ |+,−⟩) ⊕ (H_old,−(u) ⊗ |−,+⟩) ] du/2,
Wψ(u)  = Σ_(k=±) Π_k ψ(u) ⊗ |k,−k⟩.
```

For bounded g, `W†W=I`, and the same two restricted charge identities follow pointwise almost everywhere. Both value records now act by the **same multiplication coordinate** u on the physical space. This is a well-defined continuous constrained representation of the prior scalar-angle `L²` construction; it is not a proof that a naively projected three-factor continuum exists, a full `S²` carrier, or a demonstration of independently localized angular records. The direct-integral carrier and measure are specified model structures.

Gauge matching and zero hold for both earlier functions `g₁=|u|` and `g₂=|u(u+1)|`, and for any other diagonal g. Thus they do not alone determine the magnitude law. A mere common change of units does not alter **dimensionless ratios**. At N=4, for example, the first-to-second-bin magnitude ratio is 3 for g₁ and 1 for g₂. If those bin distinctions and ratios are physically meaningful, one common rescaling cannot make the two laws identical. Whether a fuller justified equivalence could relate them, or which descriptions are genuinely actual, is a separate constitutional issue—not a license to posit an arbitrary whole-level value or reopen the settled infinity comparison.

A scale transformation can be treated as gauge only if it changes no physical or experiential distinction. It cannot be used to erase real differences in felt intensity by definition. Nor does this model determine the subjective incidence measure or identify either carrier with a subject.

## 8. What the constructive route requires next

The user's suggestion yields a genuine improvement: a pointwise zero pair can be represented as the **entire physical gauge sector**, not as a specially prepared ancillary state, and the actual coherent echo can be embedded into it. The nonzero local signs survive as gauge-invariant physical observables. A different joint sign flip can be studied as a physical counterpart; it is not automatically a gauge relabeling.

To reach the stronger no-residue target, the next constitutional step is to show why these matching constraints and this gauge group follow from zero itself, why the same structure has the requisite actual experiential identity and plural subject incidences, and why its physical observables and units recover real energy and spacetime. Those are not treated as acceptable brute facts, and the finite mathematical alternatives are not declared genuinely possible merely because they can be written down. The construction neither proves the full target nor shows it is impossible.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_gauge_angular_pair_test \
 verification.zero_pairwise_angular_charge_test \
 verification.zero_coherent_signed_counterpart_test -v
```
