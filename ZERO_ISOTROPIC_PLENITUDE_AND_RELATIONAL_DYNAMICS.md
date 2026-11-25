# From chosen orientations to isotropic zero—and a test of plenitude

## Answer in brief

**Yes: there is a substantive next move.** The previous unique-history construction chose a relative phase and a memory-ready direction. In this round those choices are replaced, in an explicit model, by **rotationally invariant zero-spin pairings**. A symmetric exchange Hamiltonian then transfers a record correlation without selecting a spatial direction; the entire clock-extended state satisfies the same complementary-zero constraints.

But zero total spin alone does not select the pairings. To test the user's plenitude proposal rather than simply choosing one, I also imposed symmetry under **all permutations** of the four spin factors. In this finite model the result is sharp:

1. Total spin zero leaves a two-dimensional space, not a unique pure state.
2. Symmetry between all four factors selects a unique **mixed** state on that space; there is no pure state of the four factors alone invariant under both spin rotations and all permutations.
3. There is a canonical invariant pure state after adding a two-dimensional conjugate reference representation. It treats the singlet multiplicity symmetrically, but that reference and its representation are additional structure.
4. If a closed Hamiltonian on the four factors preserves total spin zero **and commutes with every permutation**, it is scalar on the zero-spin subspace: it cannot produce internal state change there. Nontrivial record dynamics require additional relational structure, a weaker symmetry, or a larger model—not a preferred external direction by necessity.

This does not prove that a self-sufficient zero is impossible. It replaces three ad hoc axis/phase conditions with a principled invariance requirement, then shows exactly what invariance does and does not determine in a concrete model. The spin representation, the symmetry, the pair relationships, reference systems and exchanges are not derived from zero itself; this is not yet the requested complete derivation of subjectivity or physical law.

Verifier: [verification/zero_isotropic_singlet_history_test.py](verification/zero_isotropic_singlet_history_test.py).

## 1. Let balance determine a pair's relational state, not an axis

Use the earlier complementary-zero kernel `K` with logical Pauli operators

```text
X_L = X_R J_W X_T,       Z_L = Z_R,       Y_L = −i Z_L X_L.
```

They commute with the previously specified `C₁,C₂,C₃` and `L`, and form a spin-half algebra on K. Introduce a pointer/reference qubit B, memory M and another reference qubit N. We are using a **specified common SU(2) action** on B, L, M and N. The logical L action is encoded in R–W–T–F; B can later be embedded into the earlier environment. Neither action is shown to be a physical spatial rotation.

For two spin-half factors define

```text
Q_ab = [3I + X_a X_b + Y_a Y_b + Z_a Z_b]/4.
```

`Q_ab` is the projector onto their triplet sector. Its zero sector is the unique singlet

```text
|s⟩_ab = (|0⟩_a|1⟩_b − |1⟩_a|0⟩_b)/√2.
```

A simultaneous rotation on the two factors leaves this vector invariant. No axis or phase is picked by the singlet; both one-factor reduced states are `I/2`, and corresponding spin components are perfectly opposite along **any common axis**. The construction requires a rule identifying what counts as the *same* rotation on the factors. Changing that identification can move the phase choice into the representation, so its physical basis is a real dependency, not a solved problem.

Take the two relational conditions

```text
Q_BL = 0,           Q_MN = 0,
|ψ₀⟩ = |s⟩_BL ⊗ |s⟩_MN.
```

Within the old K sector, they specify one ray. Unlike the prior `Z_M=+1` constraint, the memory has no preferred pure ready direction: it is internally entangled with N. The two pair constraints replace the previous phase-alignment and ready-axis selectors with a rotationally invariant relation. The pairing **BL and MN** remains a choice.

A conditional readout of N can supply a relationally defined orientation, but is not needed for the transfer calculation below. No individual observer is assumed to access B, M or N merely because these operators exist.

## 2. Exchange produces direction-independent record transfer

Use the spin-exchange involution

```text
H = Swap_LM = [I + X_L X_M + Y_L Y_M + Z_L Z_M]/2,
H²=I,                 U(θ)=cos θ I − i sin θ H.
```

H commutes with all three old `C_i`, with L and S, and with the generators of the **common** SU(2) action on B,L,M,N. Hence it preserves the old complementary zeros and total spin zero throughout the history. The verifier also extends all three logical factors to the original 16-state work register and checks the declared work-number charges and orientation charge. Coupling those factors to an assumed neutral M preserves those charges; the old-environment encoding of B has not been shown local or charge-neutral. The interaction remains stipulated; its locality and implementation have not been derived.

Initially B is perfectly anticorrelated with L along any common axis, and B and M have no correlation. At `θ=π/2`, exchange transfers the L partner to M: B and M are perfectly anticorrelated and L and N are paired. For B and M measured along the same arbitrary axis, with results `b,m=±1`,

```text
P(b,m | θ) = [1 − b m sin²θ]/4,
P(opposite | θ) = [1 + sin²θ]/2.
```

At `π/4` the opposite-outcome probability is `3/4` and the mutual information is approximately `0.188722` bits. At `π/2` they are `1` and `1` bit. These are Born-rule readout statistics of the model. They do not establish actual outcomes, irreversible recording or a conscious subject.

For the finite clock window `θ∈[π/2−π/8, π/2+π/8]`, the window probability is `1/4`, the conditional opposite-outcome probability is approximately `0.975079`, and the mutual information is `0.831757` bits. The history is cyclic and reversible; nothing here establishes a permanent record.

## 3. One invariant zero-eigenstate for the history

Let the two-level reference clock have `Z_C` and define the stationary constraint and isometry

```text
𝒞 = H − Z_C,
W = |+⟩_C (I+H)/2 + |−⟩_C (I−H)/2,
𝒞 W = 0,             W†W=I.
```

Let `H_cas=(C₁²+C₂²+C₃²)/8`, and understand identities on the other factors. The following is a sum of commuting positive projectors:

```text
H_whole = H_cas + (I−L)/2 + 𝒞²/4
          + W Q_BL W† + W Q_MN W†.
```

Its zero kernel has **dimension one**, with smallest nonzero eigenvalue 1 in the chosen units. The unique whole is `|Ω⟩=W|ψ₀⟩`. It is annihilated by each old `C_i`, by `𝒞`, and by the common total-spin generators. The operator and state are invariant under the specified simultaneous SU(2) action. The clock-dressed pair terms constrain the whole history relationally rather than applying a preparation pulse in external time.

The phase POVM gives normalized conditional state `U(θ)|ψ₀⟩` with uniform phase density `1/π` on `[0,π)`. The designated θ=0 relation is still encoded in the dressed constraints and the clock's phase convention; rotation invariance does not by itself derive that clock relation. `H_whole` is a constraint operator, not a demonstrated objective cosmic-energy Hamiltonian. The overall units and the specific Hilbert spaces also remain inputs.

As before, one may map B into a two-dimensional subspace of the previously specified old environment. The verifier constructs the isometry from the actual coherent `1/128` code and `127/128` complement state, retaining the old clocks and labs. This preserves the old state algebraically, but the map is state-dependent and generally nonlocal; it does not explain the old amplitudes or provide an operational interface to confined inhabitants.

## 4. The decisive test: total zero does not pick a pairing

For four spin halves, require only the original K condition and

```text
(X_B+X_L+X_M+X_N)|ψ⟩ = 0,
(Y_B+Y_L+Y_M+Y_N)|ψ⟩ = 0,
(Z_B+Z_L+Z_M+Z_N)|ψ⟩ = 0.
```

The joint kernel has **dimension two**. Both

```text
|s⟩_BL |s⟩_MN       and       |s⟩_BM |s⟩_LN
```

lie in it, and their squared overlap is `1/4`. They are distinguishable by the specified pair-correlation observables: the second has `⟨Q_BL⟩=3/4`, rather than zero. Thus *global* rotational balance does not entail *pairwise* balance for the chosen pairing. Imposing the latter is stronger, even though its individual pair quantities are themselves zero.

Nor does diagonal rotational symmetry pick the exchange dynamics. As a control, replace `H=Swap_LM` by `H'=Swap_BM`. Both are invariant under the same global rotations, commute with the earlier balances, and each yields a unique zero eigenstate when its clock and the same dressed singlet constraints are used. Yet B–M readouts under H become perfectly anticorrelated at `π/2`, whereas under H′ their table stays uniform at every θ. With these factors and clock/readout conventions held fixed, the two produce distinct predictions. Whether a more complete theory relates the alternatives by a gauge transformation must be argued, not assumed.

## 5. Can plenitude remove the pairing choice?

Consider the four spin factors as interchangeable for this test and require invariance under **all** their permutations as well as total spin zero. This is a stronger hypothesis than merely requiring a zero total; in the actual record application B,L,M,N have different roles, so making them interchangeable is not automatic.

Let `P₀` project onto the two-dimensional total-spin-zero space. The unique density operator supported there and invariant under all permutations is

```text
ρ₀ = P₀/2,          Tr(ρ₀²)=1/2.
```

Every pair then has the same isotropic correlation, `⟨σ_i^a σ_j^a⟩=−1/3` for `i≠j` and `a=x,y,z`. No pairing is privileged. The uniqueness follows because the adjacent swaps act irreducibly on the two-dimensional singlet multiplicity: their common matrix commutant consists only of scalar multiples of the identity. The verifier checks its dimension directly.

There is **no pure four-factor state** whose density operator has both these symmetries. A pure permutation-invariant density would span a one-dimensional permutation representation, so adjacent swaps would all act by the same sign. The verifier finds neither such vector in the zero-spin subspace. In particular, summing pairing states with arbitrary signs or normalizing a naive list is not an automatic pure-state solution.

A canonical pure extension does exist. If `V` is the two-dimensional singlet multiplicity and an extra reference carries the conjugate representation `V*`, then

```text
|Ω_sym⟩ = (|v₁⟩|v₁*⟩ + |v₂⟩|v₂*⟩)/√2
```

is independent of the orthonormal basis in the appropriate tensor sense, invariant under the permutation representation `D⊗D*`, and unique up to phase under that invariance. Tracing out the reference gives `P₀/2`. This is a coherent purification, not a claim that a classical random pairing was selected. It still **adds** a reference and its transformation law; it does not establish that all physically or experientially genuine possibilities exist or fix their incidence measure.

There is also a concrete dynamical cost. For a Hamiltonian acting on the four spins alone that preserves the spin-zero sector and commutes with all permutations, its restriction to that sector must lie in the one-dimensional commutant. It is therefore proportional to the identity there and changes any zero-spin state only by a phase. With one conjugate reference and a unique total invariant ray, a symmetry-preserving Hamiltonian likewise cannot move that ray without additional invariant multiplicity. This is a finite-model theorem, **not** a universal no-go for symmetric relational physics. A larger reference/clock with nontrivial representation or invariant multiplicities may allow dynamics without selecting an external orientation; establishing one is the constructive next test.

## 6. What has actually been derived, and what has not

This round yields more than another chosen endpoint: the conditions of isotropy determine each singlet pair without selecting a phase or direction; exchange yields exact all-history balance and a measurable record-transfer law; and the permutation calculation makes the plenitude-versus-dynamics tension explicit. It also exposes a new route: carry the pairing multiplicity in a relational reference and seek a **larger invariant interaction with nontrivial invariant dynamics**.

But the assertion that zero's own constitution necessitates these groups, representations, equal weighting, references or interactions remains open. The calculations do not establish actual subject incidences, a signed experiential quantity, a physical negative-energy counterpart or an objectively defined whole energy. A spin opposite is not thereby the opposite of felt suffering, and cancellation would not make a subject's suffering unreal. The user's proposal that all genuine possibilities necessarily actualize remains a substantive principle to investigate, not an assumption that the above mixed density has proved.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_isotropic_singlet_history_test \
  verification.zero_stationary_whole_unique_history_test \
  verification.zero_invariant_all_history_record_clock_test -v
```

The twelve new tests verify the spin/constraint algebra, unique stationary kernel and gap, finite-clock transfer, alternate dynamics and pairings, mapping to the earlier coherent state, permutation-invariant mixed state, absence of a pure four-spin solution and canonical purification. NumPy is required.
