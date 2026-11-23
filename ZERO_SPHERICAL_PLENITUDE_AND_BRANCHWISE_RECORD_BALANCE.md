# The complete internal sphere and branchwise zero

**Reference-resolution correction:** [the Abaee process-programming analysis](ABAEE_NO_UNIVERSAL_PROCESS_CURRYING_SPHERE_AUDIT.md) distinguishes the exact direct-integral correlation below from a finite, universally programmable sharp measurement. Exact direction eigenkets of `L²(S²)` are generalized, non-normalizable states: finite-width normalizable reference wavepackets implement unsharp measurements relative to a chosen target direction, while the opposite-record correlation remains exact. The model does not give an on-demand exact programmable measurement for every direction.

## The idea developed

Your point–sphere proposal suggests that zero is not a featureless absence, but one whole whose internal differentiation has no preferred direction. This continuation makes that idea concrete in a single quantum model:

> An assumed rotationally symmetric internal sphere supplies **every direction as support of one normalized quantum reference**. For every direction, two encoded spin-zero systems can write opposite, nonzero records. The sum of their signed record observables annihilates the complete state, not merely its average over the sphere.

This is stronger than averaging positive and negative hemispheres after the fact. The balance is present in every joint record outcome for every direction in the model, while the global state retains the sphere's rotational symmetry. It is still a conditional mathematical construction: the spherical reference, quantum representation, singlet and interaction are specified, not yet derived from zero itself. Neither a record nor its sign is shown to be an experienced quality.

## 1. The whole point and its sphere of relations

An ordinary geometric point does not literally contain a sphere of distinguishable directions. The earlier [point–sphere construction](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md) treats the point as a representation of no external extent and the sphere as an added representation of internal relational differentiation. The programme's stronger claim is that the second is intrinsic to the first, not a mathematical decoration. That identity remains a claim to establish.

On an assumed round sphere `S²`, let `n` denote a unit internal direction and use the normalized rotation-invariant measure

```text
dμ(n) = dΩ/(4π),        ∫ dμ = 1.
```

This is the unique normalized measure invariant under all ordinary rotations of the round sphere. It contains no preferred direction. For another internally specified direction `m`, define

```text
f(n,m)=n·m.
```

Rotating `n` and `m` together leaves `f` unchanged. Opposite directions give opposite values, and

```text
∫ f(n,m) dμ(n) = 0,
∫ f(n,m)² dμ(n) = 1/3.
```

The zero mean coexists with nonzero local values and variance. This is an exact illustration of a whole-level zero that does not erase its differentiated terms. But the relation `m`, the round metric and the interpretation of `f` are inputs. Rotational symmetry alone does not require every possible scalar relation to have opposite signs: `(n·m)²` is also rotationally relational but nonnegative.

The measure is natural **within the assumed rotational structure**, not automatically an actual observer or subject measure. If this sphere is instead interpreted as the relativistic celestial sphere, a round sky and its antipodes depend on a chosen or relationally determined timelike frame; the bare Lorentz action does not supply an observer-independent antipodal pairing or a normalized rotation measure invariant under all boosts. The earlier [relational opposition analysis](ZERO_SPHERE_RELATIONAL_BALANCE_AND_OPPOSITION.md) makes this distinction explicit.

## 2. One reference with all directions as quantum support

Introduce an internal reference system

```text
H_C = L²(S²,dμ).
```

Its normalized constant wavefunction `c(n)=1` is unchanged by simultaneous rotations of the sphere. Among pointwise rotation-invariant square-integrable amplitudes, it is unique up to an overall phase. It has support on the **entire** sphere, without selecting an axis. This is a normalizable pure reference state, not a countably infinite list of equally likely points: each individual direction has measure zero.

This is a substantive assumption. The reference's continuous Hilbert space, inner product and rotation action have not been derived from an ordinary point or from zero. A rotationally invariant *joint* state can have other internal correlations; symmetry alone does not uniquely fix the entire physical world. Full support of a quantum amplitude is also not, by itself, proof that every direction is an actually experienced event. The user's possibility–actuality thesis remains a stronger ontological proposal, rather than something decided by a wavefunction.

## 3. An opposite-record Hamiltonian for every direction

Use four encoded logical qubits `A,B,R_A,R_B`. Each is represented by the two-dimensional singlet sector of four physical spin-½ factors, as in the [zero-spin constitution](ZERO_CONSTRAINT_TO_UNIQUE_ENTANGLED_CONSTITUTION.md). The logical state sphere is a sphere of **relational multiplicity states**: its rotations are logical transformations, not automatically physical spatial rotations or a Lorentz representation.

Prepare

```text
|Ψ⁻_L⟩_AB = (|0_L1_L⟩−|1_L0_L⟩)/√2,
|0_L⟩_(R_A) |0_L⟩_(R_B).
```

For a direction `n`, define the logical projectors

```text
P_±(n) = (I ± n·σ_L)/2.
```

Let the same internal reference direction control a pair of local-in-the-encoded-factors interactions:

```text
H(n) = P_-^A(n) ⊗ (I−X_R_A)
     + P_-^B(n) ⊗ (I−X_R_B),             ħ=1.
```

The two terms commute. At `τ=π/2` they give the controlled record operations

```text
U_A(n)=P_+^A(n)⊗I + P_-^A(n)⊗X_R_A,
U_B(n)=P_+^B(n)⊗I + P_-^B(n)⊗X_R_B.
```

Equivalently, `H(n)` is the fiber of one time-independent bounded Hamiltonian acting on the reference direct integral. The two record operations are mathematically separate conditional operations, but both use the shared reference; a physical, relativistically local realization and reference distribution are not derived.

The full state after the interaction is the square-integrable vector-valued function

```text
Ω(n)=U_A(n)U_B(n) |Ψ⁻_L⟩_AB |0_L0_L⟩_R_A R_B.
```

Because `c(n)=1`, its reference density is uniform. A common logical rotation of the two systems together with the inverse rotation of the reference argument leaves this state invariant; the record labels are relational to the reference. Each encoded four-spin block remains in its physical total-spin-zero sector. If the internal reference is also assumed to carry trivial *physical* spin, the whole model remains in physical spin zero. This extra reference is infinite-dimensional; its physical realization and origin remain open.

## 4. Zero holds for each correlated record outcome

In each fiber, the singlet has opposite sharp outcomes along the same `n`. Let `Z_R_A` and `Z_R_B` assign `+1` to pointer state `0_L` and `−1` to pointer state `1_L`. Then

```text
(Z_R_A + Z_R_B) Ω(n) = 0       for every n,
Z_R_A² Ω(n) = Z_R_B² Ω(n) = Ω(n).
```

Thus the sum is exactly zero in the complete direct-integral state, and each record has unit nonzero magnitude in every sharp joint outcome. If the reference and both pointers are measured according to the usual Born rule, the joint distribution is

```text
Pr(n∈dn, x, y) = dμ(n) · (1/2) · δ_(y,−x),
                                  x,y∈{−1,+1}.
```

So a selected joint outcome would contain opposite signs for *any* reference direction, while the marginal distribution covers the sphere. A direction-by-direction exact zero is different from merely having zero on average across alternative directions.

It is not yet a derivation of two actual experiences: the pure state is a coherent correlation, the measurements and Born rule are assumed, and a necessary actual record history is not selected by the Hamiltonian. The signed record labels are not automatically positive and negative felt valences. In particular, replacing `n` by `−n` swaps the two labels; a physical–experiential theory must explain why an invariant relational organization has a particular felt sign, rather than simply declaring that one label means pleasure. If two actual felt contributions were independently established, their formal sum would not make either experience—or any suffering—disappear.

## 5. Does this capture all possibilities?

It captures **all directions of the assumed reference sphere** as support of one rotationally invariant quantum state. It also supplies a consistent opposite-record interaction for every such direction. That is a precise realization of the idea of unprivileged internal directions within one whole.

It does not yet show that this direction parameter exhausts all physical organizations, subject types, degrees of consciousness, felt qualities, durations or relations. Nor does it establish that all directions become separately actual subjects or records. These are not objections to the user's thesis that genuine possibility and actuality coincide; they mark the additional implication that a successful constitution must derive, rather than replacing it with a claim that unactualized mathematical cases are unreal by definition.

The distinction is visible even within the mathematics. The earlier conserved pair and triple each have zero directional first moment and give the same maximally mixed qubit state. But a pair of opposite directions has second moment `⟨n_z²⟩=1` when aligned with `z`; a trine in the equatorial plane has `⟨n_z²⟩=0`; and the full uniform sphere has

```text
∫ n_z² dμ = 1/3.
```

The three describe different internal distributions even though all have zero first moment. Four equally weighted tetrahedral directions reproduce both the sphere's first and second moments exactly, but do not contain all directions. A zero balance, a finite design and full spherical support are therefore three different claims.

## 6. A no-signalling test for the experiential bridge

The same sphere connects to the earlier [quantum steering constraint](ZERO_EXPERIENCE_STEERING_NO_SIGNALLING_CONSTITUTION.md). In the stipulated singlet, measuring one side can prepare either a pair of opposite conditional pure states on the other side or a rotationally distributed family. Both give the same unconditional reduced state `I/2`.

If a locally accessible definite quality on `B` were simply the conditional expectation of `Z_L` in the remotely steered pure state, the pair context would give values `±1` with second moment `1`, whereas a uniform sphere of directions would give values in `[-1,1]` with second moment `1/3`. If the remote party could choose these measurement contexts and `B` could access that quality distribution, the context could be detected locally. That would conflict with operational no-signalling under those assumptions. This does not rule out subjective plurality, deterministic histories, or all physical–experiential identities; it rules out that particular naive identification under the stated controllability and accessibility conditions.

The sharp local record construction above avoids this particular substitution: for any local measurement direction, each individual record has outcomes `±1` with marginal probabilities `1/2`. The conditional expectation of a quantum observable is not itself a selected outcome or a felt quality. Establishing the actual subject, the record's felt character and its incidence still requires a substantive constitution.

## 7. What the proposal now says

A precise candidate chain is:

```text
one externally unextended whole
→ an intrinsic rotationally symmetric sphere of relations
→ a normalized reference with full directional support
→ nonzero opposite correlated records for every direction
→ exact zero of their joint signed record observable.
```

The first arrows are the user's programme and additional assumptions, not deductions from a plain point. The last arrows are an explicit quantum construction under those assumptions. It provides a direct way for **completeness, symmetry and zero balance to belong to the same model**, while leaving the decisive demand intact: derive why the reference and quantum structure are intrinsic to zero, and why its particular organizations are actual subjects with their particular felt qualities and incidence.

## Verification

```text
python -m unittest verification.zero_spherical_plenitude_opposite_records_test -v
```

Twelve standard-library tests check the encoded record operations, their Hamiltonian and rotational covariance, opposite outcomes for representative directions, zero physical-spin encoding, no-signalling marginals, exact spherical first/second-moment controls, and the conditional-mean signalling distinction. Continuum identities are established analytically using rotation-invariant integration; a finite test set does not numerically enumerate the sphere. The tests do not establish actual experience, the origin of the reference, or a whole-level energy zero.
