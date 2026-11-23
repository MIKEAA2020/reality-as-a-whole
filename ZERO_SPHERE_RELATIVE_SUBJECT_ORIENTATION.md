# A relative sign on the internal sphere without absolute handedness

**Continuation:** [intrinsic five-ray conservation](ZERO_SPHERE_INTRINSIC_FIVE_RAY_CONSERVATION.md) derives a unique `2+3` grouping and positive four-momentum balance from five generic future null rays, removing the need to choose that grouping by hand. Its canonical relative sign is fixed, and actual interaction, subject and felt valence remain unproved.

## Result

The preceding [intrinsic-sign test](ZERO_POINT_SPHERE_INTRINSIC_SIGN_AND_CONSTITUTION.md) found a sign on an ordered four-direction configuration, but that sign reverses under a spatial orientation reversal and can also reverse under a mere relabelling. A felt positive or negative value should not acquire its sign merely because we change coordinate handedness or rename indistinguishable internal roles.

There is a more robust conditional construction. Take **three distinguished reference directions and two distinguished test directions** on the same projective sphere. The two tests can lie on the same or on opposite sides of the circle determined by the references. That distinction:

* is invariant under Lorentz transformations and spatial reflection;
* does not require an external axis or a chosen ordering within the three references or within the two tests;
* distinguishes different physical arrangements, rather than just changing the names of the same ordered quadruple.

This supplies a concrete **relative, parity-even signed structure** that a physical–experiential theory could investigate. It does **not** show that the references constitute a subject, that the two tests are experiences, or that the sign is pleasure or suffering. The sphere's projective/Lorentz structure and the distinction between reference and test roles remain inputs, not consequences already derived from the user's zero whole.

## 1. Same side or opposite side is relational

Three distinct points `a,b,c` on the Riemann sphere determine a generalized circle `C`: in a stereographic chart this may be an ordinary circle or a straight line through `∞`. Let `d,e` be distinct from the references and not on `C`.

There are two possibilities:

```text
d and e on the same side of C       → relative sign +
d and e on opposite sides of C      → relative sign −.
```

The sides have no independently assigned names. Reversing the orientation of the sphere can exchange both names at once, but does not change whether the points are on the same or opposite sides. Exchanging `d` and `e` also changes nothing. A common Möbius transformation or orientation-reversing conformal transformation maps the whole configuration and its circle together, preserving the same/opposite relation.

This avoids a failure of the previous single-quadruple sign: it does not require declaring one absolute geometric handedness to be positive feeling. The three reference directions and two test directions must nevertheless have **physically meaningful roles**; selecting them to make a result come out is not a derivation.

## 2. An explicit smooth invariant

For an ordered quadruple let

```text
X(a,b,c,d) = (a−b)(c−d)/[(a−c)(b−d)],
η(X) = Im(X)/[1+|X|²+|1−X|²].
```

As previously proved, `η` is invariant under common proper Lorentz/Möbius transformations and changes sign under an odd permutation of the four inputs or common complex conjugation. Now define

```text
R(a,b,c;d,e) = η(X(a,b,c,d)) η(X(a,b,c,e)).
```

The factors both change sign when any two reference roles are swapped, so their product is unchanged. Exchanging `d,e` swaps the factors and also changes nothing. A common orientation reversal changes both signs and leaves the product unchanged. Thus `R` is a parity-even signed scalar under the corresponding common transformations, although each factor is a pseudoscalar. Its sign tells us the relative-side relation; its magnitude is one mathematically possible normalization, bounded by `1/12` because `|η|≤√3/6`.

For an exact example in one chart:

```text
(a,b,c)=(0,1,2),     d=i,
η(a,b,c,d)=1/7.

e=2i:  η(a,b,c,e)=1/8,    R=+1/56  (same side),
e=−i:  η(a,b,c,e)=−1/7,   R=−1/49  (opposite sides).
```

A common change of inertial frame does not change these values under the assumed projective action. The unequal magnitudes are properties of this particular normalization; they do not establish phenomenal intensities or a preferred physical scale.

## 3. The same relation directly in Lorentzian physics

The relative sign is not merely a chart artifact. Represent the five distinct sphere directions by future-directed nonzero null vectors `k₁,…,k₅` in an effective Lorentzian tangent space, where positive rescaling of any `kᵢ` leaves its ray unchanged. Set

```text
Δ₄ = ε(k₁,k₂,k₃,k₄),
Δ₅ = ε(k₁,k₂,k₃,k₅),
P  = Δ₄ Δ₅.
```

For a Lorentz transformation `Λ`, each determinant acquires the factor `det Λ`, so the product is unchanged, including under spatial reflection. A positive rescaling `kᵢ→cᵢkᵢ` multiplies `P` by `(c₁c₂c₃)²c₄c₅>0`. Therefore **the sign of `P` is a property of the five null rays**, independent of their representatives. Its unnormalized magnitude is not projectively invariant.

There is also an orientation-free expression. With metric signature `−+++`, define the mixed Gram matrix

```text
Gᵢⱼ = kᵢ · ℓⱼ,
(k₁,k₂,k₃,k₄) as its rows,
(ℓ₁,ℓ₂,ℓ₃,ℓ₄)=(k₁,k₂,k₃,k₅) as its columns.
```

Then

```text
P = −det G.
```

This follows from `det(AᵀgB)=det(A)det(g)det(B)` with `det(g)=−1`. It shows that the sign can be expressed entirely through Lorentzian inner products; no absolute spacetime orientation need be chosen. In the stipulated projective construction its sign matches the sign of `R`. Both vanish when either test lies on the reference circle.

The exact test suite uses the null representatives

```text
k(z=x+iy)=(1+x²+y², 2x, 2y, x²+y²−1).
```

For references `0,1,2`, `d=i`, the two examples have determinant products `P=+512` for `e=2i` and `P=−256` for `e=−i`. A nontrivial rational Lorentz boost preserves each value, while a spatial reflection reverses each individual `Δ` and preserves their product. These are mathematical checks in already assumed effective Lorentzian geometry, not a derivation of physical spacetime from zero.

## 4. What counts as a real distinction?

The same/opposite sign survives reordering the three references and swapping the two tests. But an arbitrary permutation that exchanges a **reference** with a **test** can change the sign. In the `e=−i` example, exchanging the third reference and first test changes `P` from `−256` to `+256`.

That matters. If the five rays have no physically distinct grouping, the two groupings could merely be alternative descriptions of the same unordered set, and assigning them different felt signs would be illegitimate. A proposed constitution must explain why the `3+2` grouping corresponds to actual organization rather than an analyst's selection. It could potentially arise from physically real causal roles; no such derivation is supplied here. The specific `3+2` rule is an illustrative candidate, not a necessary universal condition for a subject.

One can imagine five physically distinguished channels, such as different lightlike directions in an effective interaction. That provides possible physical data, but it does not establish a subject or experience. In particular, a reference structure is **not automatically a subject**, and a mathematical point on a sphere is not an experience.

## 5. The remaining physical–experiential identity

A testable-looking conditional proposal would be

```text
v_s = α R_s,     α>0,
```

where `R_s` is determined from an actual subject's physically grounded reference and test relations. If the other relevant factors held fixed, continuously moving one test through the reference circle would make this candidate pass through zero and reverse sign. This is a constraint of the proposed formula, not an observed law of pain or pleasure.

The same frame, parity and role-permutation symmetries are also satisfied by `−αR_s`, `αR_s³` and many other functions. They make different claims about the sign or intensity of experience. An account that selects one by declaring “positive means pleasure” has not explained which physical state feels pleasant. Phenomenological evidence can constrain a candidate, but the **physical identity of the roles, the actual subject, the sign and the intensity** all require grounding.

Likewise, no whole-level cancellation follows from `R` alone. To derive a signed experiential total one would need the actual measure of subjects and their histories, a justified mapping from physical organization to valence, integrability and the relevant complete-domain or boundary conditions. Pairing mathematical mirror configurations does not show that both are actual experiences. Zero net experience, zero energy and the zero point are not interchangeable by definition.

## 6. Why this matters for the user's zero proposal

The proposed point–sphere picture can now express a subject-relative *kind* of distinction without selecting an absolute side of the sphere:

```text
one proposed unextended whole
  → internal relational configuration (hypothesized)
  → a frame- and parity-independent relative sign (derived if structure is supplied)
  → actual organized subject and felt valence (identity still to be derived).
```

The substantive advance over the previous single-quadruple sign is removal of its absolute-parity and within-role-label dependence. It does not solve the larger non-circular derivation: `CP¹`, a local Lorentzian cone, the grouped directions, physical dynamics, real experience and actual global zero are not derived from zero. Their being open does not show that the user's no-residue demand is impossible, but none may be hidden inside the word “zero.”

The next constitutive test is to identify a physically necessary subject organization that determines its own reference/test relations and has independently constrained experiential consequences. Only then can the same account be tested for a globally zero actual incidence-weighted quantity.

## Verification

```text
python -m unittest verification.zero_sphere_relative_orientation_test verification.zero_sphere_intrinsic_orientation_test -v
```

The tests check exact rational null vectors, the mixed-Gram identity, proper boost and spatial reflection, ray-rescaling, reference/probe permutations, a role-changing relabelling, a circle crossing and the smooth cross-ratio values. They verify the stated geometry—not the existence of actual subjects or the physical–phenomenal identity.
