# Deriving the eigencondition and Hamiltonian from zero: a constructive program

## The question and the advance

The user asks what it would take to derive the preceding Hamiltonian and its `U=+1` eigencondition **from zero's own constitution**, and to work through as many steps as necessary.

Here is a substantive conditional derivation, not merely a list of future tasks:

1. The earlier **first signed balance** is `G₁=J₁−Z_R Z_T=0`.
2. In the *same* all-sector work–record–target circuit, there is a complementary signed balance `G₂=X_W+Z_R X_T`. On the active work subspace,

   ```text
   G₂² = 2(I−U),       U=−Z_R X_W X_T.
   ```

   Therefore `G₂|Ψ⟩=0` **derives** the previous `U|Ψ⟩=|Ψ⟩`; it need not be stated as a separate eigencondition if the complementary zero is independently justified.
3. The two balances are components of a three-direction algebra. Their commutator implies a third: `G₃=Z_W−Y_T`. The actual coherent state in both lab sectors and all 16 clock labels satisfies all three exactly.
4. Their invariant quadratic operator `Σ_i G_i²` yields a canonical nonnegative **zero-penalty**. On the active subspace it is exactly `I−P`, where P is the previously selected two-dimensional space. No independently tuned relative coefficients are needed once this particular three-direction algebra and its normalization are given.

This moves the eigencondition and an explicitly constructed Hamiltonian-like operator **one level closer to zero**: two complementary balances select the interface state, and their algebra gives the penalty. But the deeper task remains to derive the three signed components, their relative orientation, the active space and their physical/experiential interpretation from zero's constitution, not to assume them because they make the construction work. Calling a positive penalty a *physical Hamiltonian* requires a further dynamical argument. Nothing in these tests establishes a fundamental foliation, objective cosmic-energy zero, actual subjects, or a phenomenal sign.

Reproducible verifier: [verification/zero_constitution_hamiltonian_phase_gate_test.py](verification/zero_constitution_hamiltonian_phase_gate_test.py). Prior construction: [branchwise balance and conditional selection](ZERO_BRANCHWISE_BALANCE_AND_CONDITIONAL_SELECTION.md), [all-sector involution](ZERO_ALL_SECTOR_EXACT_RECORD_INVOLUTION.md).

**Orientation continuation:** [relative orientation and an internal reference](ZERO_RELATIONAL_ORIENTATION_AND_INTERNAL_REFERENCE.md) builds a charge-balanced internal reference and an invariant relative-phase observable, and proves an uncorrelated-input preparation obstruction.

## 1. Three signed balances already present in the interface

Within the original physical model, let W be the active two-state work subspace, R the record and T the target. Set `J₁=−Y_W`. Define two operator triples:

```text
work contribution A = ( J₁,       X_W,       Z_W )
other contribution B = (−Z_R Z_T, Z_R X_T,  −Y_T )
whole contribution G = A+B.
```

The work operators commute with the record–target operators. Each triple separately has the standard Pauli-type commutation relations, with our normalization:

```text
[A_i,A_j] = 2i ε_ijk A_k,
[B_i,B_j] = 2i ε_ijk B_k,
[A_i,B_j] = 0,
[G_i,G_j] = 2i ε_ijk G_k.
```

The work triple is not introduced as three unrelated matrices. In the original four-bit work register, the existing exchange generator is exactly `X_W`; its commutator with the first memory occupation gives `J₁=i[X_W,n_M1]`; and `Z_W=P_act(n_M2−n_M1)P_act`. Thus the original exchange and occupation structure generates the work-side algebra. The counterpart is an explicit **record-controlled** representation, not automatically the earlier lab's directional generators or literal physical spatial angular momentum. Its relationship to the existing sphere directions and its relative orientation remain problems to derive. The component `B₂`, for example, is a joint record–target observable; its assignment does not imply an R-only system can read T.

The two first total components are

```text
G₁ = J₁ − Z_R Z_T,
G₂ = X_W + Z_R X_T.
```

`G₁=0` is the prior branchwise balance. For `G₂`, the individual terms commute and square to one. Therefore **if G₂ is measured**, its two contributions are also nonzero and opposite on the zero state. But `G₁` and `G₂` do not commute. The joint-kernel claim does not mean their individual components can all be assigned simultaneous sharp values; either component pair can be measured in its own measurement context.

By the commutator relation, a vector annihilated by both `G₁` and `G₂` is also annihilated by `G₃`. This is an exact operator result, not a numerical inference.

## 2. The eigencondition follows from a complementary zero

Define the prior involution `U=−Z_R X_W X_T`. On the active work space,

```text
G₂² = (X_W+Z_R X_T)² = 2(I+Z_R X_W X_T) = 2(I−U).
```

Since `G₂` is Hermitian,

```text
G₂|Ψ⟩=0   ⇔   U|Ψ⟩=|Ψ⟩.
```

Consequently

```text
G₁|Ψ⟩=G₂|Ψ⟩=0  ⇒  G₃|Ψ⟩=0 and U|Ψ⟩=|Ψ⟩.
```

At a fixed record value `r=±1`, these equations have a unique work–target solution up to phase:

```text
|χ_r⟩ = (|j=r⟩|0⟩_T + i |j=−r⟩|1⟩_T)/√2,
|j⟩ = (|0110⟩ − i j |1001⟩)/√2.
```

It is maximally entangled and its work and target reductions are each `I/2`. The complete common kernel is two-dimensional, one solution for each r. The verifier confirms that the actual code and complement circuit components, not just an invented representative, lie in it before and after each of the 16 clock readouts. Thus the demonstrated result is not confined to the earlier small code branch.

Within the previously specified pulse family, `G₁=0` holds after the target operation for any work phase α, whereas

```text
⟨G₂²⟩ = ⟨G₃²⟩ = 2[1−sin(2α)].
```

The complementary zero selects α=`π/4` in the tested interval `0≤α≤π/4`. This derives the phase **conditional on the specified complementary operator and pulse family**; it does not yet derive that operator or family from zero.

## 3. The canonical zero-penalty from the algebra

Let the work operators be extended by zero outside the existing `|0110⟩,|1001⟩` active subspace; let `P_act` project onto it. Extend each B term with `P_act` as well. The three full-space G operators retain the same algebra, act on the physical 16-dimensional work register and commute with the model's declared total work-number and specified work-pair charges. They act trivially on the labs and references.

The quadratic Casimir

```text
C = G₁²+G₂²+G₃²
```

is positive and commutes with all three G components. In the active R–W–T space its eigenvalues are 0 on the common zero space and 8 on the orthogonal triplet space. Therefore

```text
H_flat = (I−P_act) + C/8 = I−P,
P = (P_act+L)(I+U_full)/4,
L = Z_R J₁ Z_T.
```

Here `U_full` exchanges the two active work states, acts as identity on the other work states, and has the same record and target factors as U. In the full `2×16×2` R–W–T space, P has rank 2 and `H_flat` has spectrum `0` twice and `1` sixty-two times. It is the **unique orthogonal projector with kernel P**, so the finite algebra canonically fixes this normalized penalty *given P*. It also commutes with `G₁` and the original specified charges.

This is not yet a derivation of the universe's Hamiltonian. The full-space term `I−P_act` excludes inactive work states and is another selection input; the unit gap is a normalization, not an independently derived physical energy scale. Even when P is fixed, the prior `H_sel` has the same ground space but different excited energies `0, 1/2, 1, 3/2, 2`. A zero space does not uniquely determine dynamics. The flat penalty is zero throughout its ground space and does not by itself produce the nontrivial clock–record dynamics in the larger circuit. A relational clock and the relevant dynamical generator must be derived or justified separately; this does not assume external time or rule out relational motion in a constrained whole.

## 4. The hidden active-sector requirement

The full-space first balance is

```text
Q_full = J₁ − Z_R P_act Z_T.
```

Its zero kernel has dimension **60 out of 64**: it includes the 56-dimensional inactive R–W–T space. Even adding the `+1` involution condition leaves 30 dimensions: the two active solutions and 28 inactive ones. Hence the previous two-dimensional result relied on the actual circuit's already prepared active work support. This was correctly stated as an active-subspace result, but it is a necessary explicit part of the present derivation, not a consequence of `Q_full=0` alone.

To eliminate this residual freedom without an external selector, a deeper theory must explain why the active representation, or an equivalent intrinsic criterion, is part of zero's constitution. Simply discarding the inactive states is not an explanation.

## 5. The relative orientation problem: a concrete test, not an assertion

The three-component construction does not yet determine **which** complementary orientation occurs. Define, on active W,

```text
D(θ) = exp(−iθ J₁/2),
X_W(θ) = cos θ X_W + sin θ Z_W,
Z_W(θ) = cos θ Z_W − sin θ X_W.
```

Rotate the work triple by `D(θ)` while leaving its counterpart fixed. For every θ this gives another complete three-direction zero algebra, the same first balance `G₁`, the same model charge commutators, and the candidate involution

```text
U_θ = −Z_R X_W(θ) X_T.
```

Its active common kernel is selected by

```text
|χ_r(θ)⟩ = [|j=r⟩|0⟩_T + i e^(i r θ)|j=−r⟩|1⟩_T]/√2.
```

The verifier applies `D(θ)` to the actual code and complement states. All recorded i, j, r, h and target Born tables remain identical, all branches retain `G₁=0`, and the corresponding rotated G triple annihilates them. Nevertheless, when the original physical U₀ is held fixed as an observable,

```text
⟨U₀⟩ = cos θ;
```

at θ=`π`, the whole state is orthogonal to the original, while those tested record tables remain the same. The resulting U₀ probe acts on R–W–T jointly; its algebraic compatibility with the model's declared charges does not make it available to a confined record or prove a spacetime-local implementation.

This is the exact next explanatory fork:

- If θ changes a physically available relational phase, zero's constitution must determine the relative orientation, or account for all genuine alternatives and their actual incidences and measure.
- If it is **gauge**, the full physical observable algebra and incidence rule must be invariant under `D(θ)`; one cannot simply declare it gauge while retaining U₀ as an observable distinguishing those states.

Both remain live possibilities. The family demonstrates nonuniqueness under the **specific stated equations**, not a no-go theorem against a deeper constitutive account.

There is also a discrete sign point: U and −U implement exactly the same conjugation of observables, but their `+1` eigenspaces are orthogonal. A target phase flip exchanges these two spaces while preserving the first balance and the declared charges. Thus the sign of an operator representing a transformation does not by itself choose which physically distinguishable subspace is actual. The complementary G₂ rule supplies a choice only if its orientation/sign is justified.

## 6. Step-by-step program to reach the user's full demand

The goal is not to accept unexplained remainders. These are the successive results a successful zero-constitution account must establish, with concrete checks rather than renamed postulates.

1. **Characterize zero intrinsically.** State what zero is as a self-subsistent whole, and what counts as an intrinsic differentiation rather than added data. Give a construction rule whose output is not an arbitrary state dressed with the label “zero.” Ordinary arithmetic `0=+x−x` alone does not supply x or actual incidence; that observation does not refute a richer constitution of zero.
2. **Derive the physical dual algebra.** From that rule obtain the work-like and counterpart representations, their tensor/relational composition, and the meaning of the three signed G components. Reproduce the observed interface algebra above as a consequence, not by choosing it. Explain why the active sector is intrinsic or how apparently inactive sectors are themselves incorporated.
3. **Derive the relative orientation or gauge quotient.** Resolve the explicit θ family in §5. If it is a physical degree of freedom, explain its necessary realization and measure; if gauge, show why all admissible observables—including incidence and experiential distinctions—respect that quotient. Do not identify a merely renamed copy with a second subject.
4. **Derive the eigencondition.** With the derived orientation, prove complementary zero `G₂=0`; §2 then gives `U=+1` without imposing that eigencondition separately. Show that the needed `G₁=0` and active support also follow, and extend beyond this finite interface.
5. **Derive physical dynamics rather than only a penalty.** Obtain an invariant Casimir or its appropriate generalization, justify why it represents a physical generator or constraint, determine relational scales and interactions, and recover the pre-existing sphere–clock–work histories. Same kernel does not mean same Hamiltonian. Address genuine locality, resources, and emergent spacetime without a preferred fundamental foliation.
6. **Derive actuality, incidence and measure.** Specify whether and how the paired possibilities are distinct actual occurrences, how their weights are fixed, and how outcomes/records arise. An involution on Hilbert space and equal Born probabilities do not by themselves supply actual subjects or an outcome ontology. Infinite sums would additionally need a justified measure and convergence.
7. **Derive the experiential interface.** Establish why particular physical/relational incidences are felt, how subject boundaries and local access arise, and what maps physical opposite contributions to opposite *felt* values. Test the map against confined-report/no-signalling constraints; target T's explicit access is not automatically R's access. The overall sign-reversed experiential assignment remains a rival until the constitution distinguishes it.
8. **Close whole-level accounting and empirical checks.** If the fundamental additive quantity is energy or experience, define its objective whole-level composition and physically meaningful counterpart, not merely a Hamiltonian constraint. If a real negative felt contribution is balanced, it remains suffering for that subject. Derive recoverable physical predictions, and compare them with data and established relativity/quantum constraints.

The user's proposal that genuine possibility and actuality coincide could enter step 6 as a substantive principle, provided the account explains what makes the possibilities genuine and fixes their incidence measure. It cannot by itself decide whether θ is physical or gauge, nor turn an arbitrary operator sign into felt valence.

## What this round has accomplished

**Established in the specified physical model:** the involution eigencondition follows from a complementary signed zero; its third balance follows algebraically; the common-zero Casimir gives an exact normalized projector penalty; the physical all-sector states realize the construction; and a phase family identifies the remaining orientation question concretely.

**Still to derive:** why these particular balances, relative orientation, active representation and dynamics follow from the self-sufficient zero-whole, and how the same constitution entails actual plural experience. These are not declared acceptable residues. They are the remaining load-bearing parts of the requested derivation.

## Run

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_constitution_hamiltonian_phase_gate_test -v
```

The tests cover the physical 64-dimensional extensions, zero-kernel dimensions, both SU(2) algebras and their common Casimir, derivation of the eigencondition, the actual coherent circuit across both sectors and every clock label, pulse controls, distinct excited spectra, charge compatibility, and the θ/sign counterfamilies. Tests verify the stipulated finite mathematics, not metaphysical necessity or experience.
