# A conservation-preserving instrument for the internal sphere

**Continuation:** [zero-sector memory and causal incidence](ZERO_SECTOR_MEMORY_CAUSAL_INCIDENCE_CONSTRUCTION.md) adds a copyable encoded memory and ideal storage gap, constructs a branchwise opposite-sign candidate using source/receiver roles, and tests the resulting symmetry and record-multiplicity limitations. These physical records are not established subjects or experiences.

**Process-storage scope:** [the Abaee preprint analysis](ABAEE_NO_UNIVERSAL_PROCESS_CURRYING_SPHERE_AUDIT.md) distinguishes our fixed, specified finite instrument from universal exact process programming, and distinguishes reversal of its coherent dilation from recovery after discarding the pointer.

## The connection

The preceding [zero-spin constitution](ZERO_CONSTRAINT_TO_UNIQUE_ENTANGLED_CONSTITUTION.md) found a sphere of relational states inside a four-spin zero sector, but an isolated two-spin singlet cannot accommodate sharp individual spin records while remaining in its strict zero sector. Separately, the [five-ray bridge](ZERO_SPHERE_CONSERVATION_QUANTUM_PROBABILITY_BRIDGE.md) found conservation-derived probabilities and steering, assuming qubits and measurement operations.

Here those constructions meet in one explicit finite model:

> Encode each of two logical qubits in four physical spins of total spin zero. Encode a three-outcome pointer in the spin-zero sector of six more spins. A rotationally invariant unitary correlates the pointer with a conserved-sphere three-outcome measurement. Every joint state and every pointer-conditioned branch remains in exact total physical spin zero. For a specified logical singlet, the three pointer weights and remote conditional states reproduce the conserved trine's `1/3` steering weights and signed directional balance.

This answers a specific obstruction: **nontrivial relational quantum records need not be represented by a sharp spin on one constituent, and can be correlated without leaving the whole's exact physical spin-zero sector.** It does not derive the quantum representation, actual spacetime, actual subjects, felt qualities or selected experiences from zero. A correlated quantum pointer is not automatically a definite lived record. The construction is a coherent bridge under stated inputs, not a completed self-subsistent ontology.

## 1. The relational system and its partner

For four spin-½ factors, write

```text
|0_L⟩ = |singlet⟩₁₂ |singlet⟩₃₄,
|1_L⟩ = (2|singlet⟩₁₃ |singlet⟩₂₄ − |0_L⟩)/√3.
```

These orthonormal vectors span the four-spin total-spin-zero subspace `H₀^(4)`. Its pure states form `CP¹ ≅ S²`. Two invariant operators `P_12=(I−σ₁·σ₂)/4` and `P_13=(I−σ₁·σ₃)/4`, restricted to this subspace, have matrices

```text
P_12 = (I+Z_L)/2,
P_13 = I/2 − Z_L/4 + √3 X_L/4.
```

Consequently the logical Pauli operators can be constructed from physical rotational scalars, e.g.

```text
Z_L = 2P_12 − I,
X_L = (4P_13 + 2P_12 − 3I)/√3,
```

on `H₀^(4)`. These operators act as stated on that sector; their action outside it need not be Pauli. Their commutator supplies the third logical direction. No physical rotation axis is selected by these pair-singlet observables.

Take **two** such encoded subsystems, `A` and `B`, and prepare the logical singlet

```text
|Ψ⁻_L⟩_AB = (|0_L 1_L⟩ − |1_L 0_L⟩)/√2.
```

It has reduced logical state `I/2` on each block. This is an additional preparation/constraint on the relational degrees of freedom: physical total-spin zero alone does not imply this logical singlet. Each four-spin block has physical spin zero separately, so the complete `AB` state does too. A logical singlet is invariant under a *common change of logical qubit frame*, but physical spatial rotations act trivially on each entire zero-spin block. Logical Bloch rotations should not be confused with physical spatial rotations.

## 2. A pointer that also lives inside zero

Six physical spin-½ factors have a five-dimensional total-spin-zero sector `H₀^(6)`: its singlet multiplicity is

```text
C(6,3) − C(6,2) = 5.
```

Choose an orthonormal basis `|r_0⟩,…,|r_4⟩` of that sector. The verification constructs it by orthogonalizing products of three two-spin singlets and directly checks the resulting five vectors against all three total-spin operators. Set the pointer initially to `|r_0⟩`; use `r_0,r_1,r_2` for the three distinct pointer outcomes. The other two dimensions are available in the unitary extension and need not appear in the initial measurement outputs.

For any pointer label, the projector `|r_i⟩⟨r_i|`, extended by zero outside `H₀^(6)`, commutes with all physical total-spin components. A selected pointer branch is therefore still in the zero sector. These are relational, multi-spin pointer states, not individual sharp-spin records.

Altogether the model uses 14 physical spins in three blocks `A`, `B` and `R`. It assumes their factorization, logical basis, initial preparation and measurement interaction. The three independently zero blocks occupy only a subset of the complete 14-spin zero sector; exact total spin zero by itself does not require this block structure.

## 3. Connecting the conserved trine to an invariant interaction

For the earlier symmetric five-ray relation

```text
3 k(0) + k(2) = 2 k(1) + k(i) + k(−i),
```

in its intrinsic center frame, the three directions form a trine and have conserved energy fractions `q_i=1/3`. Select a logical frame and identify the trine with

```text
n₀=(0,0,1),   n₁=(√3/2,0,−1/2),   n₂=(−√3/2,0,−1/2).
```

The choice of logical-frame alignment is an **additional identification**, not a derivation of physical spatial directions from encoded rotational scalars. The directions are unitarily equivalent to the trine in the earlier center frame. Define logical effects and their positive square roots

```text
Π_i = (I+n_i·σ_L)/2,
F_i = (2/3)Π_i,       K_i = √(2/3)Π_i,
Σ_i F_i = Σ_i K_i†K_i = I.
```

The conserved center-frame fractions thus coincide with the Born weights only for the specified maximally mixed logical state; they are not universal state-independent outcome probabilities.

Define the linear map on `H₀^(4)⊗|r_0⟩` by

```text
V: |ψ⟩|r_0⟩ ↦ Σ_(i=0)^2 K_i|ψ⟩|r_i⟩.
```

Because `ΣK_i†K_i=I`, this map preserves all inner products. Its two orthonormal input columns and two output columns can each be extended to an orthonormal basis of the 10-dimensional space `H₀^(4)⊗H₀^(6)`. Mapping the first full basis to the second gives an explicit unitary `U` on that space; the test constructs it by Gram–Schmidt and checks both `U†U=UU†=I` and the three required operator blocks. Extend `U` by the identity on the orthogonal complement in the full `2^10`-dimensional A–R spin space. Both the 10-dimensional subspace and its complement are invariant under physical rotations, and rotations act as the identity on the subspace. Therefore the extended `U` commutes with all components of physical total spin. It also commutes with the total spin of block `A` and of block `R` separately.

A self-adjoint logarithm of this finite-dimensional `U`, extended by zero outside the invariant subspace, supplies an autonomous interaction Hamiltonian generating the unitary in a chosen interaction time. This existence statement does **not** show that the Hamiltonian is spatially local, a feasible few-body interaction, relativistic or naturally selected. It also does not identify its energy zero with a whole-level energy constraint.

At every intermediate time generated by this invariant Hamiltonian, an initially zero-spin state remains zero. Measuring the invariant pointer label after the interaction also maps it to a zero-spin branch. This is stronger than merely getting zero as an average. It is nonetheless a standard conditional quantum instrument: it does not solve the problem of which outcome is actually experienced.

## 4. Steering and signed balance in the same zero sector

Start from `|Ψ⁻_L⟩_AB|r_0⟩` and apply the above interaction on `A,R`. For pointer result `i`, the unnormalized reduced state of `B` is

```text
σ_(B|i) = tr_A[(F_i⊗I)|Ψ⁻_L⟩⟨Ψ⁻_L|]
        = (1/3)(I−n_i·σ_L)/2.
```

Its trace gives `Pr(i)=1/3=q_i`, and the normalized conditional logical state points opposite to `n_i`. Without conditioning on the pointer result,

```text
Σ_i σ_(B|i) = I/2.
```

Thus the local logical state of `B` is independent of whether this trace-preserving operation is applied on `A,R`. This is ordinary quantum no-signalling at the level of the stipulated tensor factors and inaccessible outcome-averaged state; it is not by itself a relativistic local-field construction or a proof that all proposed experiential observables are non-signalling.

Along logical axis `a=n₀`, the conditional means of the remote logical observable `a·σ_L` are

```text
−a·n_i = (−1, +1/2, +1/2),
Σ_i q_i (−a·n_i) = 0.
```

The same fractions therefore appear in center-frame conservation, the stipulated quantum outcome probabilities and this conditional signed balance. **These are three context-specific outcome weights and conditional expectation values**, not three simultaneously actual subjects or a sum of actual felt valences. The positive terms do not erase any suffering. A full physical–experiential relation and actual incidence measure remain to be derived, and assigning conditional means directly to accessible experiences would encounter the earlier [steering no-signalling constraint](ZERO_EXPERIENCE_STEERING_NO_SIGNALLING_CONSTITUTION.md).

The construction also works for the asymmetric conserved triple: use `F_i=2q_iΠ_i`, its positive square root `K_i=√(2q_i)Π_i`, and the same isometry-completion argument. For the previous rays `0,1,3,i,2i`, the test independently matches the intrinsic triple direction dot products and weights `(1/8,2/5,19/40)` to a logical realization and constructs its unitary dilation. It also works for the pair as a separate measurement context by the same completeness argument; that pair instrument is not explicitly constructed in the new tests. Contexts are alternatives, not five jointly realized outcomes.

## 5. What is established and what remains essential

The model integrates a precise chain:

```text
physical spin-zero sector → relational qubit sphere
+ conserved center-frame trine → complete logical POVM
+ an encoded zero-sector pointer and invariant unitary
+ a specified logical singlet → conserved-sector steering and signed balance.
```

It is a stronger coherence result than merely placing several analogies next to one another: a unitary measurement coupling and its pointer-conditioned branches remain within the same physical zero-spin framework. The pointer interaction is reversible: `U†` erases the correlation. Its correlations do not themselves supply stable memory, a single necessary outcome, an experienced subject, or felt positive and negative valence. Necessity of a global history is not the same as deriving that history or the empirical probability measure from the Born weights.

The identification of the encoded projective sphere with the earlier center-frame sphere is an explicit mathematical identification. The encoded logical `SU(2)` acts on *multiplicity* degrees of freedom invisible to physical rotations; it is not automatically the spinor representation of physical Lorentz transformations. A Lorentz-covariant dynamical theory, relational localization, and a basis-independent physical reason for that identification must be supplied before claiming an emergent spacetime derivation. Nor does physical spin zero establish zero energy or zero experiential quantity.

The central no-residue demand remains exactly as strong as before: explain why zero's own constitution entails the representation, relational subsystem structure, relevant observable and interaction, the actual records and subjects, their felt characters and the incidence rule. The present construction establishes a compatible physical mechanism **conditional on these inputs**, not that these inputs are self-subsistent or exhaust the whole.

## Verification

```text
python -m unittest verification.zero_invariant_sphere_instrument_test -v
```

Eight standard-library tests construct the six-spin singlet pointer, verify invariant encoded operations and unitary dilations for the symmetric and asymmetric triples, check exact-sector preservation and steering/no-signalling, and test state dependence and reversibility. Floating-point comparisons have numerical tolerances. The tests verify the finite specified model, not an empirical consciousness claim or the origin of the assumptions.
