# A finite spherical reference with a continuously symmetric whole

**Integrated relational continuation:** [the joint selector and transfer construction](ZERO_RELATIONAL_CONSTITUTION_TO_CONSERVED_RECORD_TRANSFER.md) adds explicit directional-matching and relational-coherence conditions that, together with opposite records and the invariant sector, uniquely select this recorded state. It carries those same records into conserved memory–battery transfers. These extra relations and their experiential interpretation remain to be derived.

**Relational-purity continuation:** [the additive-dynamics audit](ABAEE_ADDITIVE_DYNAMICS_AND_EXACT_DIAMOND_RADIUS.md) checks that the two states below have equal local A and B marginals but AB purities 1/3 and 1, and separates state-dependent conserved transfers from composition-additive channel scalars.

## Main result

The earlier [spherical-reference model](ZERO_SPHERICAL_PLENITUDE_AND_BRANCHWISE_RECORD_BALANCE.md) used an infinite-dimensional `L²(S²)` reference. Here is a finite alternative, in the same physical spin-zero framework:

- A six-spin singlet sector supplies a finite reference with four distinguishable tetrahedral labels.
- Two four-spin logical systems and two four-spin record registers produce opposite records for each of those four labels, with exact zero of their signed sum.
- Although the four **selectable labels** have only tetrahedral symmetry, the resulting **joint quantum state** can have exact continuous logical `SO(3)` symmetry. A separate, explicitly constructed continuously invariant Hamiltonian prepares that particular state.

The distinction is important: a finite state can be continuously symmetric without being a device that exactly selects every direction. This avoids the inference ruled out by the [process-programming analysis](ABAEE_NO_UNIVERSAL_PROCESS_CURRYING_SPHERE_AUDIT.md), while giving the point–sphere proposal a more economical realization.

There is also a sharp limitation. A second, physically different state satisfies the same physical spin-zero condition, the same continuous logical rotational symmetry, the same exact opposite-record identity and the same eight joint reference/record probabilities. It differs in its internal correlations. Thus these stated conditions alone do not uniquely determine the physical constitution. The example does not disprove the stronger thesis that zero's *own* constitution could determine it; it specifies what additional implication that thesis must supply.

## 1. A reference made from zero-spin structure

A system `C` of six spin-½ factors has a five-dimensional total-physical-spin-zero subspace. Choose orthonormal singlet states `|r₀⟩,…,|r₄⟩`; use the first four as reference labels. Four further blocks `A,B,R_A,R_B` each use the two-dimensional total-spin-zero sector of four spins. Thus the complete finite system contains **22 physical spins** and, in the chosen encoded subspace, each block separately has exact physical total spin zero.

Assign the four reference labels the tetrahedral logical directions

```text
n₀=(+1,+1,+1)/√3,    n₁=(+1,−1,−1)/√3,
n₂=(−1,+1,−1)/√3,    n₃=(−1,−1,+1)/√3.
```

They obey

```text
(1/4) Σ_i n_i = 0,
(1/4) Σ_i n_i n_iᵀ = I₃/3.
```

These are the first and second moments of the uniform round sphere. Four labels do **not** contain every direction, and matching two moments is not equality of the full angular distributions. The choice of spin representations, factorization and tetrahedral identification is part of the model, not derived from a bare point or from zero.

The transformations below are a **logical** `SO(3)` acting on multiplicity degrees of freedom within physical singlet sectors. Physical spin rotations act trivially on those sectors. We do not identify this logical symmetry with spatial Lorentz symmetry or derive spacetime from it.

## 2. A finite exact record processor

Prepare the uniform reference label superposition and logical singlet

```text
|s⟩_C = (1/2) Σ_i |r_i⟩,
|Φ⟩ = |s⟩_C |Ψ⁻⟩_AB |00⟩_R_A R_B.
```

For each `n_i`, use the same paired logical measurement gates as before. The reference-controlled unitary `U_tet` applies those gates in label sector `i`. Every operation acts inside the chosen physical singlet blocks, extended by identity where appropriate. Its output is

```text
|Ω⟩ = (1/2) Σ_i |r_i⟩ |ψ(n_i)⟩,
(Z_R_A+Z_R_B)|Ω⟩=0,
Z_R_A²|Ω⟩=Z_R_B²|Ω⟩=|Ω⟩.
```

Under the specified Born rule, each reference label `i` has probability `1/4`, and for each `i` the only joint record values are `(+1,−1)` and `(−1,+1)`, each with conditional probability `1/2`. The eight reference–record outcomes therefore have weight `1/8` each. Exact cancellation holds in every joint record outcome, not only on averaging over them.

The four logical reference labels can select four exact fixed-labelled measurements. This does not supply a continuum of exact selectable measurements: the finite-memory no-programming constraint applies when a fixed processor is required to implement an arbitrary sharp direction exactly for every input. Nor is a coherent pointer correlation already a definite experience.

## 3. A finite state with full continuous symmetry

Define a reference scalar and three orthonormal vector states:

```text
|s⟩ = (1/2) Σ_i |r_i⟩,
|v_a⟩ = (√3/2) Σ_i (n_i)_a |r_i⟩,       a=x,y,z.
```

The tetrahedral moment equations make these four vectors orthonormal. Give this four-dimensional space the logical representation `1⊕3`: `|s⟩` is invariant and the `|v_a⟩` transform as a three-vector. The unused fifth singlet can be left invariant. On `A,B`, use the same logical spin-½ rotation on each block; the record-label registers are unchanged. This representation is a specified internal logical symmetry, not physical angular momentum of the six-spin singlets.

Let

```text
R_+ = |01⟩ + |10⟩,      R_- = |01⟩ − |10⟩,
|t_a⟩ = σ_a^A |Ψ⁻⟩_AB.
```

Direct calculation rewrites the *same finite output state* as

```text
|Ω⟩ = (1/2) |s⟩|Ψ⁻⟩R_+
      + (1/(2√3)) Σ_a |v_a⟩|t_a⟩R_-.
```

The first term is a scalar. The `|t_a⟩` transform as a vector, so the contraction `Σ_a|v_a⟩|t_a⟩` is also a scalar. Consequently `|Ω⟩` is invariant under **every** common logical `SO(3)` rotation, not just the tetrahedral subgroup. Its reduced reference state is

```text
ρ_C = (1/2)|s⟩⟨s| + (1/6) Σ_a |v_a⟩⟨v_a|,
```

which is also invariant. This is a substantive distinction between a whole's continuous symmetry and the discreteness of a particular internal readout.

The specific reference-controlled processor `U_tet` is covariant under the 12 proper tetrahedral rotations, not arbitrary logical rotations. For a generic rotation, the four reference basis labels mix rather than permute as a closed set. The test checks the two generators of the 12-element subgroup and a non-tetrahedral control. Exact continuous invariance of the **output state** does not make this discrete controlled gate a universal all-direction processor.

## 4. A continuously invariant preparation—at a cost

There is a second preparation that respects the full logical symmetry. The initial `|Φ⟩` and final `|Ω⟩` are orthogonal and individually invariant. Define

```text
H_sym = i(|Ω⟩⟨Φ| − |Φ⟩⟨Ω|),       ħ=1.
```

It is Hermitian and commutes with every common logical rotation. On the two-state span of `|Φ⟩,|Ω⟩`,

```text
exp(−i H_sym π/2)|Φ⟩ = |Ω⟩.
```

Extend it by zero outside the encoded subspace; it also preserves physical total spin zero. Thus **one finite, continuously invariant Hamiltonian** can prepare the symmetric opposite-record state.

The cost matters. This Hamiltonian is explicitly tailored to the particular global initial and final states. It is a many-body construction, not an independently justified local interaction, and it is not a processor implementing every directional measurement on arbitrary input. No objective whole-level energy zero follows from its spectrum or an energy-reference shift. The representation, preparation and interaction remain assumptions; symmetry has not yet generated them from zero.

## 5. Symmetry plus zero still leaves a concrete distinction

Consider the different normalized state

```text
|Ω₀⟩ = |s⟩_C |Ψ⁻⟩_AB (|01⟩−|10⟩)_R_A R_B/√2.
```

Like `|Ω⟩`, it lies in physical spin-zero sectors, is invariant under the full specified logical `SO(3)`, and obeys

```text
(Z_R_A+Z_R_B)|Ω₀⟩=0.
```

It gives the **same** eight `1/8` probabilities when the reference labels and both pointer labels are read. Yet `⟨Ω₀|Ω⟩=0`: the states are distinct. A relational test distinguishes them: the logical `AB` singlet projector has expectation `1` in `|Ω₀⟩` but `1/2` in `|Ω⟩`. In `|Ω₀⟩` the reference is not correlated with the logical systems in the same way.

Therefore physical spin zero, continuous logical rotational invariance, exact signed record zero **and those record probabilities** do not alone determine all physical relations in this stipulated Hilbert space. These are formal state alternatives, not an assertion that both are genuinely possible complete worlds. The user's claim that genuine possibility equals actuality can remain in force; it must explain why the actual constitution includes the specific correlations, not merely label the others unreal.

## 6. Testing a subject-and-valence rule

For `|Ω⟩`, both individual record registers have the same unconditional reduced state:

```text
ρ_R_A = ρ_R_B = I/2.
```

Test the candidate: **a subject's definite signed quality is a common function solely of its own present reduced record state**. That rule assigns the two registers the same value. If their signed values must also sum to zero, both must be zero. In particular, the natural expectation `tr(ρ_R Z_R)` is zero for each, despite the perfect opposite correlations in joint outcomes.

This candidate cannot produce two nonzero definite opposite qualities from the unconditional local states. It does not rule out a constitution based on an actual definite record, causal history, a genuinely relational organization, or a physical–experiential identity not reducible to this local density matrix. Those alternatives must specify subjects, actual incidence and felt character without equating a Born conditional state with an accessible feeling that would violate the earlier steering/no-signalling constraint.

The signs in `Z_R_A` and `Z_R_B` are **record labels**. Their identification with positive and negative felt valence is not derived. If actual negative experience is eventually identified, its reality is not undone by another contribution's opposite sign.

## 7. Necessity and frequencies

The eight equal joint weights can be matched by a finite record block containing each labelled outcome once. Their `8!` formal orderings all have the same counts, so the weights alone do not determine an ordered history. This is not a claim that the alternatives are genuinely possible complete worlds, nor a physical outcome-selection mechanism.

On the user's proposal a complete actual history is necessary; a necessary outcome is not irreducibly open chance in that sense. A successful construction must still derive why the actual internally situated records realize the applicable statistics. Neither the finite reference nor its continuous state symmetry provides that derivation by itself.

## What follows

The result brings three parts of the proposal closer together: **finite physical spin-zero structure, continuous symmetry of the whole, and nonzero opposite records with exact joint zero** coexist in one explicit model. The alternative `|Ω₀⟩` identifies a precise obstacle to treating those features as a complete constitution: they do not fix internal correlations. The remaining task is to show how zero's own constitution determines the relevant correlations, subjects, actual records and felt qualities together—rather than selecting the state, symmetry action or experiential mapping independently.

## Verification

```text
python -m unittest verification.finite_tetrahedral_zero_reference_test -v
```

Twelve standard-library tests check the six-spin reference sector, tetrahedral moments and orthonormal decomposition, the finite controlled record gate, logical rotational invariance, its tetrahedral versus full-symmetry distinction, the tailored invariant Hamiltonian, the two distinct symmetric zero-record states, local reduced states and the difference between outcome weights and record order. The all-rotation statements follow from the displayed invariant scalar/vector decomposition; numerical tests sample representative rotations. None establishes physical spacetime, actual experiences or a no-residue foundation.
