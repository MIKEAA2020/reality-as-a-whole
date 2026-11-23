# When a zero constraint determines a nontrivial quantum constitution

**Continuation:** [a zero-sector sphere instrument](ZERO_INVARIANT_SPHERE_STEERING_INSTRUMENT.md) builds an encoded multi-spin pointer and rotationally invariant measurement interaction, linking the relational qubit to the earlier conserved-ray steering weights without leaving physical total-spin zero. It does not derive definite experiential records.

## The main result

Rather than starting from a selected quantum state and asking whether some average balances, consider the reverse question: **can a physical zero condition determine the state?**

For a system of exactly two spin-½ subsystems, the condition that their **total spin vector is zero** uniquely determines their joint quantum state, up to an overall phase:

```text
|Ψ⁻⟩ = (|01⟩ − |10⟩)/√2.
```

This is the entangled singlet used in the earlier sphere and Bell constructions. It was previously assumed there; here it follows from a specified zero constraint and specified quantum representation. The two individual spins do not vanish: matched measurements have opposite nonzero outcomes, while the total outcome is exactly zero. The local reduced state is `I/2`.

There is a further connection to the user's point–sphere proposal: for **four** specified spin-½ factors, the zero-total-spin sector is a two-complex-dimensional space. Its normalized pure states form an internal projective sphere `CP¹ ≅ S²`, and relational spin observables distinguish directions on that sphere while preserving the zero constraint. The sphere is not imposed as an external spatial object; it follows mathematically from the stipulated four-spin representation and zero condition.

These are direct examples of **zero constraining a particular internally differentiated physical organization**. They do not demonstrate that zero *as such* entails two or four spinors, that these subsystems are subjects, that spin is felt valence, or that total spin is the whole's energy or experiential quantity. Those differences are essential to the user's stronger goal. Nor is the two-spin uniqueness general: the four-spin zero sector contains the whole internal sphere, not one uniquely selected state.

## 1. Why demanding zero as an operator is too strong

Let `A` and `B` be two independent subsystem Hilbert spaces. If one demands

```text
V_A⊗I + I⊗V_B = 0
```

as an identity on the **entire** tensor-product space, then both local operators must be constants of opposite sign. To see this, take the partial trace over B:

```text
dim(B) V_A + tr(V_B) I_A = 0.
```

Thus `V_A` is a scalar; tracing over A gives the corresponding result for `V_B`. No nontrivial state-dependent local observable is possible under that strong hypothesis.

That does not mean local differentiation is incompatible with a zero whole. There is another possibility: the total observable is nonzero on the mathematical state space, but the **actual physical state belongs to its zero sector**. The physical space could itself be constrained to that sector. For such a state, a zero total can coexist with nonzero local fluctuations and correlations.

This distinction is particularly relevant to the user's necessitarianism: a necessary constitution, if independently established, may determine the actual constrained state rather than require every formally imaginable tensor-product state to be actual. The formal alternative states used in the argument are not asserted to be genuinely possible complete worlds.

## 2. Two spinors: zero total spin fixes the state

Assume two qubit factors with the ordinary spin-½ representation. Let

```text
T_x = σ_x⊗I + I⊗σ_x,
T_y = σ_y⊗I + I⊗σ_y,
T_z = σ_z⊗I + I⊗σ_z.
```

These are the total-spin components measured in units of `ħ/2`. Require

```text
T_x|ψ⟩ = T_y|ψ⟩ = T_z|ψ⟩ = 0.
```

The proof of uniqueness is elementary. From `T_z|ψ⟩=0`,

```text
|ψ⟩ = α|01⟩ + β|10⟩.
```

Applying `T_x` gives `(α+β)(|00⟩+|11⟩)`, so `β=−α`. Normalization then yields the singlet, with only an irrelevant overall phase remaining. The singlet also satisfies the `T_y` equation. In fact, zero total spin along **any two nonparallel axes** suffices: rotate one to `z`, write the other as a nonzero linear combination of `z` and `x`, and use the same proof.

The vector condition is invariant under a common rotation of the two spins. It does not choose a preferred direction in the center frame. This connects to the [point–sphere construction](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md): the complex two-component representation supplies a sphere of spinor directions, and the previous conserved five-ray relation supplies a candidate center frame. But the identification of those spinors with two actual spin subsystems, the existence of the constraint and the quantum dynamics are new physical assumptions. A shared spin-frame comparison between separated systems would also need a relativistic account; there is no assumed fundamental cosmic foliation here.

## 3. Zero is stronger than a zero mean

Define the positive operator

```text
P_triplet = (T_x²+T_y²+T_z²)/8
          = (3I + σ_x⊗σ_x + σ_y⊗σ_y + σ_z⊗σ_z)/4.
```

It is the projector onto the three-dimensional triplet subspace. Its kernel is the one-dimensional singlet subspace. For **any** density matrix `ρ`, the condition

```text
tr(ρ P_triplet)=0
```

therefore forces `ρ=|Ψ⁻⟩⟨Ψ⁻|`: positivity implies `ρ` has support only in the kernel. A single specified scalar zero thus determines the joint mixed or pure state within this assumed two-qubit theory. Equivalently, zero of the sum of positive squares entails all three total-spin constraints.

For any unit direction `n`, define `T_n=n·T`. In the singlet,

```text
⟨T_n⟩ = 0,       ⟨T_n²⟩ = 0,
⟨(n·σ_A)²⟩ = ⟨(n·σ_B)²⟩ = 1.
```

The second equation is important: the total is not merely zero **on average**. A joint sharp measurement along the same axis yields opposite outcomes, each `±1`, with total zero for every allowed joint outcome. The local marginal for either side is `I/2`; local outcomes are equally weighted under the Born rule. Measurements on different axes are not all jointly sharp, so this does not license assigning simultaneous definite spin values for every direction.

If a future physical–experiential identity connected the two actual local measurement outcomes to opposite felt contributions, this would be a concrete route to real local signs and an exact zero **for that matched measurement**. But neither the existence of two subjects nor that identity follows from a singlet. A necessary global state also does not, by itself, explain which definite record occurs or derive an experiential incidence measure. No negative experience is erased by the formal cancellation.

**An important constraint-versus-measurement distinction:** if the *entire physical Hilbert space of the isolated pair* were strictly the one-dimensional singlet sector, then a single local spin operator would not preserve that sector: `P_singlet (n·σ_A) P_singlet=0`. A matched sharp `z` outcome such as `|01⟩` remains in the `T_z=0` sector but not in the full total-spin-zero sector. Thus the two nonzero outcomes cannot simply be treated as unrestricted internal observables of a permanently isolated, strictly one-dimensional physical space. One may instead treat the singlet as the prepared state of a larger unconstrained state space, or include the measuring apparatus and any required angular-momentum transfer in a larger closed system. A theory imposing exact total-spin zero on that larger whole must show how the apparatus and records respect its constraint. The ideal spin probabilities above do not themselves supply that completion.

## 4. A physical Hamiltonian—and what its zero means

A simple rotationally invariant effective Hamiltonian is

```text
H = λ P_triplet,      λ>0.
```

It is nonnegative and has the unique zero-energy ground state `|Ψ⁻⟩`; the triplet sector has energy `λ`. Thus the same constraint can be presented as the unique ground state of a concrete interacting spin Hamiltonian. This does **not** establish that a zero of physical energy uniquely explains reality: the two-spin Hilbert space, its interaction, the value `λ`, and the ground-state condition are assumed. For example, an antiferromagnetic Heisenberg interaction `λ σ_A·σ_B/4` has the same singlet but ground energy `−3λ/4`; writing `λP_triplet` adds `3λI/4`. In this isolated model the energy reference can be shifted. That is not a derivation of an objective whole-level energy zero.

Nor is a projector Hamiltonian automatically self-existent or cosmologically realized. The constructive result is the conditional uniqueness of a nontrivial quantum state under a well-defined zero constraint, not the derivation of the constraint from zero's own nature.

## 5. The same zero does not always determine a unique organization

For four spin-½ systems, impose zero total spin in the same sense. There are at least two distinct normalized states:

```text
|A⟩ = |singlet⟩₁₂ ⊗ |singlet⟩₃₄,
|B⟩ = |singlet⟩₁₃ ⊗ |singlet⟩₂₄,
```

with tensor factors ordered by their physical site labels. Both satisfy all three total-spin-zero equations. They are distinct: their inner-product magnitude is `1/2`. Direct calculation gives a **two-dimensional** zero-total-spin sector for four qubits. Consequently zero total spin alone does not select a unique four-partite state or pairing.

### A zero-sector sphere with genuine relational observables

There is a constructive alternative to treating this degeneracy merely as failure. Choose the orthonormal basis

```text
|0_L⟩ = |A⟩,             |1_L⟩ = (2|B⟩−|A⟩)/√3.
```

A general normalized zero-spin state, modulo global phase, is a point in `CP¹ ≅ S²`. This sphere parametrizes **states internal to the zero sector**, not positions in a pre-existing space or an automatic derivation of physical spacetime. Its points are distinct candidate internal organizations of this stipulated system, not necessarily separate actual worlds or simultaneously actual experiences.

Crucially, there are operators acting within this sector, rather than only local operators that leave it. Define the relational pair-singlet tests

```text
P_ij = (I − σ_i·σ_j)/4.
```

Each commutes with all three components of the total spin, so it preserves exact vector zero. Restricted to the logical basis,

```text
P_12 = [ 1   0 ],        P_13 = [ 1/4    √3/4 ],
       [ 0   0 ]                 [ √3/4   3/4  ].
```

These are distinct, noncommuting rank-one projectors. Their noncommutation supplies a third, phase-sensitive relational observable `i[P_12,P_13]`. Together the two tests and their commutator span the nontrivial Hermitian operators of the logical qubit: writing a zero-sector state as `(I+r·σ_L)/2`, its three real Bloch components can be recovered from their expectations. Thus the sphere is not just a relabeling of one indistinguishable state: rotationally invariant internal relations can distinguish its directions **without violating total spin zero**.

This is an explicit mathematical point-to-sphere analogue: the total-spin vector is pinned to the zero point, yet the constraint's internal solution space carries a sphere of quantum relations. It is not literally the blow-up sphere of spatial directions, nor does this one representation prove the two spheres are physically identical. The construction presupposes quantum tensor factors, their labels and a spin representation; four-spin zero permits a sphere but does not choose a point on it. A full measurement with conserved apparatus and definite experiential records is still a separate problem.

This is a finite representation-theoretic distinction, not an assertion that all these states are genuinely possible complete physical–experiential realities. It shows where the two-qubit result gets its strength: **zero plus a specified representation and subsystem content**, not an unqualified equation `0=0`.

## 6. The direct foundational implication

The route now has a precise form:

```text
specified intrinsic quantum representation
+ a zero constraint strong enough to have a one-state kernel
→ one nontrivial joint physical organization
→ local nonzero, correlated outcomes under specified measurements.
```

This is closer to the user's demand than simply imposing local positive and negative numbers after selecting a system: the state itself is fixed by the constraint. It also illustrates why actual-state constraints can preserve local differentiation without demanding an operator vanish on every formal state.

To reach the proposed **zero-radius, self-sufficient whole**, the remaining derivation must explain why zero's own constitution entails the relevant representation, constraint and concrete actuality; why it selects the actual physical organization at realistic scale despite the four-spin degeneracy; and why particular local physical organizations are actual subjects with their particular felt qualities and incidence weights. Total spin zero and a shiftable model Hamiltonian do not establish a global energy or signed experiential zero. The result does not settle those requirements, but it supplies an explicit physical case of the type of implication the programme seeks.

## Verification

```text
python -m unittest verification.zero_spin_constitution_test -v
```

Ten tests check the one- versus two-axis kernels, the positive projector and unique singlet, opposite matched spin outcomes, the distinction between a strict singlet sector and sharp local records, local mixed state and variance, and the four-spin zero sector with its noncommuting constraint-preserving relational observables. These are finite checks of the stated quantum mathematics, not evidence that qubits are subjects or that the whole's zero has been derived.
