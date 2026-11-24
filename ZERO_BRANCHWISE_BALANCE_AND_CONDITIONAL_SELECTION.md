# Branchwise cancellation and conditional selection in the all-sector circuit

## Main result

The prior [all-sector involution](ZERO_ALL_SECTOR_EXACT_RECORD_INVOLUTION.md) paired opposite outcomes at equal Born weight. The existing circuit permits a stronger statement: **two commuting, nonzero physical observables have exactly opposite sharp values in every jointly measured branch**, even before different branches are averaged.

On the active record–work–target subsystem, write

```text
A = J₁,                     B = −Z_R Z_T,
Q = A+B = J₁−Z_R Z_T.
```

Here `J₁` is the specified standalone-exchange work-current probe, `Z_R` is the original record and `Z_T` is the target memory. In the actual coherent all-sector state, including every relative-clock readout label,

```text
Q|Ψ⟩ = 0,                 A²|Ψ⟩ = B²|Ψ⟩ = |Ψ⟩,
[A,B] = 0.
```

Thus a joint measurement finds `(A,B)=(+1,−1)` or `(−1,+1)` in each branch: neither contribution is zero. The involution already found reverses **both** contributions. This is a branchwise physical cancellation, not the claim that the subsystems are absent. The work observable and the record–target product act on different tensor factors, but B requires an interface that can access both record and target.

A second result makes a non-arbitrary *conditional* selection possible. Let `U=−Z_R X_W X_T` be the previously found involution and `L=Z_R J₁ Z_T`. The two conditions

```text
Q|Ψ⟩=0,       U|Ψ⟩=|Ψ⟩
```

select exactly **one maximally entangled work–target state for each fixed R value**. A specified positive, charge-compatible Hamiltonian implements this selection as its ground space. This is a constructive candidate for a zero-and-symmetry constitution of the interface, not yet a derivation of its ingredients, a dynamical preparation, or a selection of the whole universe.

Verifier: [verification/zero_all_sector_branchwise_balance_test.py](verification/zero_all_sector_branchwise_balance_test.py). All conclusions are for the given finite model. In particular, A and B are not identified with objective total energy or felt valence; subjecthood and actual outcomes are not inferred from registers or Born weights.

## 1. From a copied relation to branchwise opposites

The established circuit has the active work states `|a⟩=|0110⟩`, `|b⟩=|1001⟩`, work observable `J₁=−Y_W`, record `Z_R`, and

```text
K = Z_R J₁,                 h = (I−K)/2.
```

The target gate records `h` in `T`: target `Z_T=+1` for h=0 and `Z_T=−1` for h=1. Therefore the fully evolved state obeys

```text
L|Ψ⟩=|Ψ⟩,                 L = K Z_T = Z_R J₁ Z_T.
```

Because the factors commute and square to identity on the active space,

```text
Q² = 2(I−L).
```

Hence `L=+1` is equivalent to `Q=0` on the active space. This is not a coincidence imposed after averaging: it is the algebraic consequence of the explicit target gate faithfully recording the relation. It is also not an independent new conservation law: the relation and its target were designed into the circuit.

For a fixed original record eigenvalue `r=±1`, the joint eigenvalues satisfy `j₁=r z_T`. In particular, on the already studied event

```text
relative-clock window,  r=+1,  T=1:
J₁=−1,          −Z_R Z_T=+1,          Q=0.
```

That event has Born weight `3/64` in the specified full state, including both the code and its complement. The two values are simultaneous sharp outcomes of commuting operators; this is not an assertion that noncommuting work occupations all have simultaneous values. `J₁` remains the current defined from the standalone work exchange, not automatically the current of the complete interaction.

The previous involution preserves r and maps `J₁→−J₁`, `Z_T→−Z_T`; therefore it maps `(A,B)` to `(−A,−B)`. Its invariance yields equal weights for these two **joint** branches at each fixed sector, clock label, Alice and Bob pointer outcome, and r. This supplies both the per-branch zero and the within-cell pairing, without pretending that the unequal 158- and 96-dimensional lab sectors are exchanged.

## 2. What exactly is selected by zero plus the involution?

For `r=±1`, define the normalized work eigenstates

```text
|j⟩ = (|a⟩ − i j |b⟩)/√2,       J₁|j⟩=j|j⟩.
```

With R fixed to r, `Q=0` allows a two-dimensional correlated space spanned by `|j=r⟩|0⟩_T` and `|j=−r⟩|1⟩_T`. It does **not** alone choose their amplitudes. The involution exchanges them with the circuit's definite relative phases. Imposing its `+1` eigencondition yields the unique normalized vector, up to an overall phase,

```text
|χ_r⟩ = ( |j=r⟩|0⟩_T + i |j=−r⟩|1⟩_T ) / √2.
```

Its Schmidt coefficients are both `1/√2`. It is maximally entangled between the work and target qubits, while each has a maximally mixed reduction. The verifier directly recovers this unique rank-one work–target density at each fixed r, in **both** actual physical lab sectors with all 16 clock labels retained. The prior target/record causality qualification remains: a reduced state for R alone does not acquire the work or target information.

For the entire active `R⊗W⊗T` space, the projector

```text
P = (I+U)(I+L)/4
```

has rank 2: one state for each r. The selection is therefore real but conditional. It leaves the R distribution, relative phases and correlations with the labs, references, clock, and other environmental degrees of freedom unselected. In particular, it does not derive the sphere geometry, all-sector state, a subject, or the overall measure.

**Important distinction:** invariance of a density matrix, `UρU†=ρ`, does not imply the `+1` eigencondition. Both the + and − U eigenstates in the `Q=0` space have U-invariant density matrices; they are orthogonal and have opposite expectation of U. Thus *symmetry alone* does not select the specific coherent phase. Treating `U=+1` as a constitutive constraint or a ground-state condition is an additional substantive input, not a consequence of the zero sum.

## 3. An explicit charge-compatible selection Hamiltonian

The operators can be extended to the full 16-state physical work register, not just its active two-dimensional code:

- `J₁` acts as the existing physical current and vanishes outside the active pair;
- `P_act` projects onto `|0110⟩,|1001⟩`;
- `V_W` exchanges those two states and is identity on the other 14 states.

Set

```text
U_full = −Z_R V_W X_T,
L_full = Z_R J₁ Z_T,
Q_full = J₁ − Z_R P_act Z_T,
H_sel = (I−L_full)/2 + (I−U_full)/2.
```

`U_full` is an involution, the two Hermitian terms commute, and both are positive. The full-space identity is

```text
Q_full² = 2(P_act−L_full).
```

The first term of `H_sel` also penalizes the inactive work sector. On the complete `2×16×2=64`-dimensional R–W–T space, its spectrum is exactly

```text
energy      0     1/2     1     3/2     2
multiplicity 2      28      4      28     2.
```

Thus the ground space is exactly the two-dimensional selected space above, with a gap of `1/2` in the chosen units. `H_sel` commutes with the existing work total-number and specified pair-number charges; it acts trivially on the physical labs and reference clocks, and R/T are neutral in the declared energy assignment. It therefore respects the already declared balances. It is, however, **an additional specified interaction**, involving the actual R–W–T factors. Its coefficients, locality, physical energy accounting and origin are not derived from zero. Being a ground state of a stipulated Hamiltonian does not show that the given closed system dynamically prepares it or that this Hamiltonian is the objective total energy of the universe.

## 4. A direct preparation control

The target gate creates the exact Q relation; the relation is not conserved throughout the original preparation. If the preceding work phase is α and the target is still in its ready state, the code-sector state obeys

```text
⟨Q²⟩ before the target gate = 4 sin²α.
```

After the perfect target gate, `Q=0` for every α, but

```text
⟨U⟩ after the gate = sin(2α).
```

The existing α=`π/4` pulse reaches `⟨U⟩=1`; α=`π/8` instead yields `1/√2`, despite exact final Q balance. Moreover `⟨U⟩=0` before the target gate, so at α=`π/4` the gate changes it from 0 to 1. A closed unitary commuting with U could not do that. The existing preparation protocol is consequently **not** a demonstrated U-symmetric dynamics throughout.

This makes the constructive gain and the remaining task precise: zero plus an imposed U eigencondition can uniquely determine the local correlated state at fixed r, and a concrete conserving candidate Hamiltonian has that kernel; neither zero alone nor the original preparation proves that this selection is necessary. A deeper self-sufficient constitution would need to determine U, its relevant eigencondition and the interaction, rather than insert them as independent choices.

## 5. Relevance to actual subjectivity and suffering

The structure is suitable for testing a proposed experiential bridge because each joint branch already contains two sharp opposite values. But a formal assignment such as `felt_A=κA` and `felt_B=κB` assumes all of the difficult parts: that there are two actual subjects, that their relevant experiences correspond to these particular operators, that B's joint R–T information is within the second subject's domain, and that κ and the incidence measure have physical meaning. The transformation reverses the signs of the *observables*; it does not establish that it reverses felt valence.

Even under that proposed bridge, `−κA,−κB` obeys the same zero and symmetry equations while reversing which contribution is called suffering. Thus the current physical conditions do not determine the experiential orientation. If a valid bridge eventually identifies one branch contribution as negative felt valence, the equal positive counterpart is a distinct contribution and **does not erase the suffering**. Nor does the current model establish that both outcomes of a quantum state are actual occurrences: that belongs to the incidence proposal, not the Born calculation.

The physically informative next challenge is to derive, from one constitution rather than separate choices, the counterpart algebra, U eigencondition, actual incidence and the physical–experiential map. The new exact branchwise balance identifies a concrete object on which that challenge can be tested; it is not a license to rename an engineered correlation as literal non-existence.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_all_sector_branchwise_balance_test -v
```

The seven tests cover the physical work-space extension, both terms and their sharp joint branches, all sectors and clock labels, the 64-dimensional spectrum and charge commutators, fixed-r rank-one/Schmidt structure, the ± involution control, and the gate/preparation control. Related computations and embeddings are tested in the [involution verifier](verification/zero_all_sector_record_involution_test.py) and [all-sector verifier](verification/zero_all_sector_sphere_clock_work_test.py). These tests check stipulated finite quantum models, not consciousness, actual occurrence, global-energy ontology or metaphysical necessity.
