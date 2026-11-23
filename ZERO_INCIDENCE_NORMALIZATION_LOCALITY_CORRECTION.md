# When normalized incidence is not a local experience

## Result and correction

The [incidence-frame construction](ZERO_CONSERVATION_INCIDENCE_FRAME_CONSTRUCTION.md) produced a common mathematical normalization for overlapping supports and the conserved sphere POVMs. That connection is valid. But interpreting the resulting normalized share as the **actual intensity of a local subject's experience** requires an additional condition that was not proved:

> A normalized share of all subject incidences can depend on a distant, noninteracting subsystem, even when the local subject's physical state and local presence are unchanged.

I give an exact commuting-projector example below. It makes a useful distinction:

* A normalized share can be a **global accounting or self-location quantity**. Its dependence on what else exists does not by itself signal or alter an actual local experience.
* An outcome or phenomenal value that is **locally accessible to a particular subject** cannot be assigned that global share without showing how it respects operational no-signalling.

This corrects the earlier report's proposed interpretation; it does not invalidate its frame identity or imply that nonlocal correlations, necessitarianism or zero totality are impossible. Nor does an abstract normalized accounting rule require a literal simulator or an external selector.

## 1. Two independent subsystems, two simultaneous candidate incidences

Use finite qubit factors `A` and `B`; no interaction is needed. As a **formal test**, let

```text
P_A = |0⟩⟨0|_A ⊗ I_B,
P_B = I_A ⊗ |0⟩⟨0|_B.
```

Pretend `P_A` and `P_B` are the propositions that the respective candidate subject incidences are present. They commute and can both be true. These projectors are not evidence that qubits are subjects, and overlap of their **global-state subspaces** is not automatically overlap of physical subjects or of their experiences. This example tests what follows if one uses such projectors as the inputs of the previous incidence normalization.

With equal weights, set `S=P_A+P_B`. On its support the frame effects are

```text
E_A = S^(−1/2) P_A S^(−1/2),
E_B = S^(−1/2) P_B S^(−1/2).
```

In the basis `|00⟩,|01⟩,|10⟩,|11⟩`, they are

```text
E_A     = diag(1/2, 1, 0, 0),
E_B     = diag(1/2, 0, 1, 0),
E_empty = diag(  0, 0, 0, 1),
E_A + E_B + E_empty = I.
```

When both candidate incidences are present, the normalized A and B shares are each `1/2`. When only A is present, A's share is `1`. This is a mathematically legitimate global accounting rule. The effects are positive; no noncommutativity is needed for the issue below.

## 2. Why the A-share is not an A-local physical quantity

Compare these product states:

```text
ρ₀ = |0⟩⟨0|_A ⊗ |0⟩⟨0|_B,
ρ₁ = |0⟩⟨0|_A ⊗ |1⟩⟨1|_B.
```

A local bit flip on `B` changes `ρ₀` into `ρ₁`; `A`'s reduced state and local candidate-presence value remain the same. But

```text
tr(ρ₀ E_A)=1/2,       tr(ρ₁ E_A)=1,
tr(ρ₀ P_A)=tr(ρ₁ P_A)=1.
```

`E_A` is not of the local form `F_A⊗I_B`: for fixed A state, its diagonal value changes with B. Consequently it cannot be implemented as an A-only quantum measurement in this model. A global measurement of `E_A` may use information from both factors and is not a superluminal local measurement.

If, **in addition**, one asserted that the A subject locally experiences or can report this normalized value, and that B's change is controllable at spacelike separation in an appropriate physical realization, the proposed extra phenomenological rule would permit a detectable remote influence. Those are additional assumptions. The algebra alone is not evidence of actual signalling or that such experiments are physically realized.

The same problem occurs if one replaces “incidence probability” by a local signed value. Here the stipulated local signed operator `V_A=P_A` has local expectation `1` in both states, while dividing it by the global multiplicity produces `E_A`, whose value changes from `1/2` to `1`. **A rule that is valid as global allocation is not thereby a law of local felt intensity.**

A more general finite-dimensional check makes the distinction exact. An observable on `A⊗B` is unchanged under **every** unitary acting on `B` in **every** state only if it belongs to the local algebra `B(H_A)⊗I_B`; conversely, every such local observable is invariant. The proof is that the commutant of the full `B`-unitary algebra is precisely `B(H_A)⊗I_B`. This is a strong, state-uniform condition. A particular physical theory may have more restricted interventions, constraints, or local algebras; the example does not derive spacetime locality from tensor factorization.

## 3. Simultaneous subjects are not exclusive measurement outcomes

The underlying candidate-presence operators in this example are

```text
N_A=P_A,        N_B=P_B,       N_total=P_A+P_B.
```

On `|00⟩`, both `N_A` and `N_B` equal one, and `N_total` equals two. A **count or incidence measure** is allowed to exceed one; it is not a single-event probability. This representation preserves coexistence and makes each local quantity independent of the other subsystem's local operations.

By contrast, the normalized effects `E_A,E_B,E_empty` describe an exclusive three-outcome POVM. An interpretation in which that POVM **samples** a candidate incidence can legitimately yield `1/2` when two are present and `1` when only one is present. Such a global self-location/accounting probability is not automatically a change in either subject's experience, and it cannot be identified with actual subject count or felt magnitude merely because it is normalized. How such a selection or credence is physically/epistemically justified remains a separate question.

There is a sharp reason one should not demand both individual effects be local and at the same time require an exhaustive **two-outcome** exclusive POVM:

```text
F_A⊗I_B + I_A⊗F_B = I_A⊗I_B
```

forces `F_A=c I_A` and `F_B=(1−c)I_B`. Taking a partial trace over either factor proves this. Hence such a POVM cannot have nontrivial locally state-dependent presence effects for both subsystems. This result assumes exactly two exhaustive outcomes and finite tensor-product factors. Adding a third outcome allows local effects—for example `P_A/2`, `P_B/2`, and the positive remainder—but then the remainder can occur even when exactly one candidate is present. It cannot simply be read as “no subject exists.”

## 4. What changes in the balance proposal

The earlier reciprocal-multiplicity identity remains a valid **local accounting theorem** under its premises. But if `m_i` includes distant subject incidences and `h_i/m_i` is asserted to be the local experience of each subject, then the model must prove the resulting experienced value is local or otherwise respects no-signalling. In this explicit toy mapping it is not. In a physically localized overlap, the multiplicity might instead be determined by genuinely local organization; that possibility is not excluded and must be established case by case.

A safer starting point is to keep two separate mathematical objects:

1. **Actual, subject-indexed local contributions**—not required to sum to one, and able to include several simultaneous subjects and real negative values.
2. **Normalized sampling or self-location weights**, derived only when an appropriately justified reference class and measure are specified.

For illustration, `V_A=P_A` and `V_B=−P_B` give simultaneous `+1` and `−1` in `|00⟩`, whose sum is zero. Each is locally defined. In `|01⟩` their sum is `+1`. This is a stipulated physical operator assignment, **not** an identity with pleasure and suffering, and it shows that locality and coexistence do not themselves force global zero. Nor does zero make the negative local value disappear.

The remaining task is therefore not to normalize first and call the result a subject. It is to derive a local physical–experiential identity and actual subject-incidence measure from the proposed self-sufficient constitution, and then show why their **actual whole-level signed quantity** is zero. A successful explanation might make the accounting and local intensity coincide for specific intrinsic reasons; that agreement cannot be assumed generally.

## Verification

```text
python -m unittest verification.zero_subject_normalization_locality_test -v
```

Eight finite-dimensional tests check the frame effects, the remote bit flip and nonlocal operator, simultaneous counts, the two-local-effect constraint in a finite control, the three-outcome remainder, and a local signed-value example. The general two-effect and operator-locality claims are argued above; the tests do not establish actual subjects, physical superluminal signalling, an experiential law or zero's constitution.
