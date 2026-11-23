# An intrinsic 2+3 grouping from the sphere and physical conservation

## Main result

The previous [relative-sign construction](ZERO_SPHERE_RELATIVE_SUBJECT_ORIENTATION.md) needed three reference directions and two test directions, but did not determine which directions had which roles. There is a substantive way to determine a `2+3` split **from the directions themselves**, provided they are five generic future lightlike rays in an effective `3+1`-dimensional Lorentzian space:

> There is a unique division of the five rays into a group of two and a group of three for which positive multiples of the two sides have equal total four-momentum. The positive coefficients are unique up to one common scale.

The grouping is unchanged by relabelling, positive rescaling of ray representatives, Lorentz transformations and spatial reflection. The common total is timelike, so it also determines its own local center-of-momentum frame rather than requiring a preferred external observer.

This is a genuine structural connection between the internal sphere and a possible physical conservation law. It is **not** a derivation that the zero whole contains five directions, that a physical interaction occurs, or that its legs are subjects. The conserved zero is a local four-momentum *difference*, not automatically global physical energy or signed experience.

## 1. Derivation from five null directions

Let `k₁,…,k₅` represent five future-directed, nonzero null rays, and assume **genericity**: every four representatives are linearly independent. Five vectors in a four-dimensional real vector space have a linear relation

```text
c₁k₁ + c₂k₂ + c₃k₃ + c₄k₄ + c₅k₅ = 0.
```

The genericity assumption gives rank four, so this relation is unique up to a nonzero common factor, and all five `cᵢ` are nonzero. One explicit choice is the alternating list of four-vector determinant cofactors. Because all `kᵢ` are future-directed, all the coefficients cannot have the same sign: the time component would not sum to zero.

Could the signs divide `1+4`? No. After moving the negative terms to the other side, one side would be a positive multiple of one null vector, while the other would be a positive sum of at least two distinct future null vectors. In signature `−+++`, two nonparallel future null vectors have negative inner product; their positive sum is timelike, not null. The two sides therefore cannot be equal.

Both signs must occur at least twice. With five nonzero coefficients, the sign counts are exactly `2+3`. Reversing all coefficients exchanges the names “positive” and “negative,” but the **smaller pair and larger triple are unique**. Define `pᵢ=|cᵢ|kᵢ`. Then

```text
Σ_(pair) pᵢ = Σ_(triple) pᵢ = P.
```

Every `pᵢ` is future null with positive energy in any future inertial frame. The mathematical equation has the kinematics of a locally conserved massless `2↔3` process. Which direction is incoming and which outgoing is not determined by the undirected ray configuration alone; time orientation, process dynamics and any physical selection rules matter. The existence of kinematically allowed momenta does not prove that a particular quantum field theory has a nonzero amplitude for them.

Positive ray rescalings change the coefficient representatives inversely, up to a common factor, and leave the partition intact. Relabelling only relabels the resulting pair and triple. A simultaneous Lorentz transformation preserves the relation. Thus the grouping is not imposed by selecting names or a frame.

## 2. A concrete exact example

Represent the five projective points `0,1,2,i,−i` by future null vectors

```text
k(z=x+iy)=(1+x²+y², 2x, 2y, x²+y²−1).
```

The unique relation, reduced by a common factor, is

```text
3k(0) + k(2) = 2k(1) + k(i) + k(−i) = (8,4,0,0).
```

Thus the pair is `{0,2}` and the triple is `{1,i,−i}`. Each side has future timelike total `P=(8,4,0,0)` with `−P²=48`. All five four-vector components balance, not just one selected energy component. The test code verifies the partition under all `5!` relabellings, positive rescalings, a nontrivial Lorentz boost and spatial reflection.

The four-momentum equation is a **zero difference across one proposed interaction**, while the common total momentum is not zero. It is not a proof of the total energy of the universe. Nor does it by itself supply an interaction law, actual matter or an experiencing subject.

## 3. A physically defined local reference frame

Because `P` is a positive sum of two distinct future null momenta, it is future timelike. Its unit four-velocity

```text
u = P/√(−P²)
```

is therefore determined by the configuration itself. Energies `Eᵢ=−pᵢ·u` are positive Lorentz scalars when both the physical momenta and `u` are transformed together. They are energies in the interaction's center-of-momentum frame, not automatically energies in the rest frame of any actual subject.

For the explicit example, the pair has equal energies `2√3` each and the triple has equal energies `4/√3` each. Consequently

```text
2 × (2√3) = 3 × (4/√3) = 4√3.
```

This is a concrete positive-energy balance with unequal numbers on the two sides. It does not select a fundamental foliation: `u` is a local frame determined by this particular interaction. It does presuppose effective Lorentzian geometry, actual momenta and a particular interaction.

## 4. What happens to the previous signed sphere invariant?

For any choice of a reference triple and complementary test pair, the previous report defined

```text
P_rel = ε(k_a,k_b,k_c,k_d) ε(k_a,k_b,k_c,k_e).
```

Take the unique coefficient relation `Σ cᵢkᵢ=0` and wedge it with the three references. It gives

```text
c_d Δ_d + c_e Δ_e = 0,
Δ_d=ε(k_a,k_b,k_c,k_d),  Δ_e=ε(k_a,k_b,k_c,k_e).
```

For generic data, both determinants and both coefficients are nonzero, so

```text
sign(P_rel) = −sign(c_d c_e).
```

The canonical test pair found above consists of the two coefficients with the **same sign**. Therefore its previous relative sign is always negative. This reveals both the gain and a limit:

* the `3+2` grouping is now determined intrinsically, rather than chosen by the analyst;
* the resulting sign is constant across all such generic canonical configurations, so this rule alone **cannot distinguish positive from negative felt states**.

For the ten mathematically possible `3+2` partitions of a generic five-ray set, six have opposite-sign coefficients in the test pair and hence `P_rel>0`; four have same-sign test coefficients and hence `P_rel<0`. This follows from a `2+3` sign split: `2×3=6` opposite-sign pairs and `C(2,2)+C(3,2)=4` same-sign pairs. These ten formal partitions are **not ten subjects or ten actual experiences**, and their `6:4` ratio is not an experiential probability.

## 5. Testing a possible experience–energy bridge

The exact event makes a tempting model clear. Suppose, purely as a test, that its two pair legs and three triple legs are five real experiential incidences, equally weighted; assign one side positive valence proportional to `Eᵢ` and the other negative valence proportional to `Eᵢ`. Conservation would give an exact signed sum of zero. In the explicit example the negative fraction could be `3/5`, with the positive values individually `3/2` times the negative magnitudes.

This is **not** a result about actual suffering. It assumes, rather than establishes, that interaction legs are subjects, that each has one incidence, that its felt magnitude is its center-frame energy, and that a chosen side is unpleasant. Those are exactly the constitutive questions at issue. Reversing the phenomenal sign assignment leaves the physics and conservation equation unchanged. A local conservation law alone cannot decide which side feels positive or negative.

Nor is center-of-momentum energy automatically subject-frame energy: a single subject could be extended, massive, multicomponent or unrelated to these hypothetical external legs. The use of `u` removes an arbitrary *coordinate observer* for this interaction; it does not derive a subject, select the actual subject's reference frame, or establish an objective experiential measure.

## 6. What the construction contributes to zero's constitution

It replaces one arbitrary ingredient in the prior sphere proposal with a **derived internal relation**: given generic five null directions, the unique positive conservation relation determines their `2+3` grouping. It also gives a nontrivial physical interpretation—an allowed local four-momentum balance—and an internally determined frame, without presuming a cosmic observer or fundamental foliation.

But the assumptions are substantive: `CP¹`/null directions, dimension, five actual channels, genericity, the physical process and the overall energy scale are not derived from a zero point. Degenerate cases with four coplanar null directions require separate treatment; the verifier rejects them rather than forcing a split. The direction of the interaction, real subjects, valence, incidence, laws and whole-level zero also remain to be established. The user's no-residue target is not met simply by renaming a local conservation identity as experience.

The focused next task is to determine whether an actual physical–experiential constitution selects a subject and a sign from such relations **without using the desired experiential answer as its selection rule**. The generic canonical split shows why that task is nontrivial: the geometry selects the roles, but its own previous relative sign does not vary.

## Verification

```text
python -m unittest verification.zero_sphere_five_ray_conservation_test verification.zero_sphere_relative_orientation_test -v
```

Tests check the exact positive momentum relation, all 120 label permutations, representative rescaling, boost/reflection, the unique role partition, the canonical relative sign and the intrinsic center-frame energy balance. The `2+3` theorem is proved above; finite checks do not prove it, establish an actual interaction, or verify experience.
