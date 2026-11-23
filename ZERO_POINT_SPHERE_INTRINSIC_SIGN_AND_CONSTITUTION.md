# Zero's internal sphere: a direct test of physical and experiential constitution

## Why this is the next foundational step

The target remains the user's stronger thesis: **zero's own constitution determines actual physical organization, real subjects and their felt character**, without an external creator or unexplained independent remainder. A global zero equation or a drawing of a point and sphere cannot by itself establish that thesis.

Rather than beginning with another assumed physical system, this note asks what the proposed **internally differentiated sphere itself** supplies. Under the previous conditional identification of the sphere with `CP¹`, it gives a concrete, observer-independent relational sign. The same calculation shows exactly why that sign is not yet felt valence and what a non-circular identity must additionally determine.

The result is a constructive constraint, not a claim of a completed derivation or a general impossibility theorem.

## 1. The first nontrivial frame-independent relation

Assume, as in the [sphere–Lorentz construction](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md), that the internal directions form the complex projective sphere `CP¹`, and consider the proper orthochronous Lorentz action by Möbius transformations. This is substantive input: neither `CP¹` nor a Lorentz action has been derived from an ordinary zero point.

A Möbius transformation can send any ordered triple of distinct sphere points to any other ordered triple. For example, any triple can be sent to `(0,1,∞)`. Therefore, **any scalar function of up to three distinct, individually labelled rays alone that is invariant under this action must be constant**. A nonconstant invariant of this restricted kind first becomes possible with four rays: after the first three are normalized, the fourth still has an invariant relational position.

This is a precise finding for the point–sphere programme: with only the projective rays and no other structure, one cannot obtain a varying observer-independent sign from a single direction or a pair or triple of distinct directions. The result does not rule out scalars built from two *nonprojective* vectors, additional fields, scales, a material rest frame or other physical information; those are different inputs.

For four ordered, distinct rays `z₁,z₂,z₃,z₄`, use

```text
X = (z₁−z₂)(z₃−z₄) / [(z₁−z₃)(z₂−z₄)].
```

`X` is unchanged by a common Möbius transformation and hence by the assumed proper Lorentz action. It need not be real. The definition extends to `∞` by projective coordinates or limits. Four directions are concyclic (allowing a line through `∞`) exactly when `X` is real; see the [cross-ratio theorem](https://ncatlab.org/nlab/show/Moebius+transformation).

## 2. An intrinsic, signed relational quantity

Define

```text
η(X) = Im(X) / [1 + |X|² + |1−X|²].
```

This dimensionless quantity is observer-independent under common proper Lorentz transformations. It is positive or negative for differently oriented non-concyclic quadruples, and zero for concyclic ones. An example is

```text
(z₁,z₂,z₃,z₄) = (0,1,2,i),
X = 3/4 + i/4,      η = 1/7.
```

The normalization has a useful property: **every odd permutation of the four roles reverses `η`, and every even permutation leaves it unchanged**. For example, one transposition maps `X` to `X/(X−1)`. Its imaginary part changes by `−1/|X−1|²`, while the denominator changes by `+1/|X−1|²`; the magnitude is preserved and the sign reverses. The other permutations follow from the standard six cross-ratio transforms. The code checks all 24 permutations explicitly.

Writing `X=x+iy` gives

```text
η = y / {2[(x−1/2)² + y² + 3/4]},
|η| ≤ √3/6.
```

Thus we have a finite signed relation derived *from an assumed ordered projective configuration*, with no external spatial axis or preferred inertial observer. This is a candidate structural carrier for differentiation, not a measurement of energy, a quantum amplitude, a pain scale or consciousness.

The orientation qualification is essential. A common orientation-reversing complex conjugation sends `η→−η`; `η` is a pseudoscalar with respect to an orientation reversal, not an ordinary parity-even scalar by itself. If physical valence is an ordinary scalar, any identification needs a physically justified orientation structure transforming with the rest of the description, or another invariant construction. No universal left/right preference has been established.

## 3. Why the ordering must be physically real, not a relabelling

There is a direct constraint on a putative intrinsic identity. If the four roles are **physically indistinguishable**, an odd permutation is merely relabelling the same unordered configuration. A genuine scalar property of that configuration must then have the same value after the relabelling. But `η` reverses:

```text
physical relabelling invariance:  v(πq)=v(q),
η is alternating:                η(πq)=−η(q) for odd π.
```

Consequently the proposal `v=αη` with fixed nonzero `α` cannot define nonzero valence on such an unordered configuration. This is a proof about the stated construction, not a prohibition on signed experience.

A successful constitution would have to determine distinctions among the roles—potentially from actual causal organization or an intrinsic subject-relative relation—so that exchanging them is a **physical change**, not just a change of names. Such roles need not be external to the whole. But simply labelling one direction “subject” or “suffering” would assume precisely what is to be explained. Nor has it been shown that a subject is represented by four null rays, or that four rays are sufficient to constitute one.

## 4. What zero balance would require

Suppose, conditionally, that actual experiential incidences form a measure space `(S,μ)`, that each incidence has an independently determined ordered four-ray configuration `q(s)`, and that its valence is

```text
v(s) = α η(q(s)),
```

with a justified common physical/experiential scale `α`. If there is a measure-preserving involution `T` on actual incidences such that `q(Ts)` is an odd permutation of `q(s)`, then `v(Ts)=−v(s)` and

```text
∫_S v dμ = 0
```

provided the integral is well defined. This gives a transparent **sufficient** balance principle. Each nonzero value remains nonzero locally; it is not erased by the sum.

But the premise is strong. A formal permutation of four labels is not automatically a second real experience, an actual subject, or a measure-preserving map of incidences. A complete history must actually contain the paired incidences, with the required weights. For this particular involutive pairing, positive and negative magnitudes and measures match, so nonzero positive and negative incidences have equal total measure. **Zero balance in general does not require that pairing or equal frequencies.**

For example, if two actual types have values `+2a` and `−a` and incidence weights `1/3` and `2/3`, their weighted total is zero. A physical–experiential theory would have to derive those magnitudes and weights; this arithmetic does not count the types as real. Nor can the sign balance of all 24 mathematical label permutations be used as an experiential total: those labels may describe the same physical configuration 24 times.

## 5. The non-circularity test: same structure, different interpretations

The candidate demonstrates both progress and the remaining logical gap. Even granting all of the sphere, its orientation, four actual role-labelled rays and `η`, the following possible *formal assignments* respect the same proper Lorentz invariance and the same odd-permutation sign reversal:

```text
v₁=αη,       v₂=−αη,       v₃=αη³.
```

`v₁` and `v₂` assign opposite signs to the same fixed, oriented, physically role-labelled configuration; `v₃` assigns a different magnitude. If each is combined with the same measure-preserving odd involution above, each has a zero total. Therefore the stated mathematical properties do not select a unique mapping to felt sign and intensity. This is a conditional underdetermination result about these axioms, not evidence that nature metaphysically permits all three, or that no deeper zero constitution can select one.

Actual first-person reports, known bodily organization, causal effects and physical dynamics can help discriminate a proposed mapping. Such evidence does not automatically prove a metaphysical identity; conversely, the fact that conscious experience is known from within is genuine evidence, not a defect in the programme. The proposed identity must explain why the physical and experiential descriptions are one constitution, not infer feeling merely because an invariant can be signed.

Likewise, the initial collapse `π(0,n)=0` does not, by itself, fix `CP¹`, the four roles, the actual relational configurations or the physical laws: the projection forgets the distinctions it maps to the point. Claiming that these structures are **intrinsic** rather than externally added is the hypothesis; establishing why this intrinsic structure is necessary is the foundational task.

## 6. A sharper formulation of the research target

An acceptable, non-circular candidate `T` for zero's own constitution must do the following **as one integrated account**, not list the desired conclusions as definitions:

1. Independently motivate why `T` is a self-subsistent zero whole and why its relevant whole-level quantity has an objective zero, without treating zero energy, a vanishing Hamiltonian constraint, a zero vector and zero experience as interchangeable.
2. Show why `T` admits actual internal distinctions, and determine the physical structure and dynamics relevant to the observed world without requiring an arbitrary external reference or fixed fundamental foliation.
3. Derive which organization constitutes an actual subject and what distinguishes its roles. Any equivalences of descriptions must preserve real subject and qualitative facts; mathematical permutations cannot automatically multiply or eliminate experiences.
4. Determine the real sign and magnitude of its felt character, not merely a mathematical pseudoscalar or a sign convention, and provide consequences independently checkable against experience and physics.
5. Derive the actual incidence measure and any whole-level cancellation. A sufficient pairing or divergence law is not enough if actual incidence, support and boundaries are imposed solely to obtain zero.

The `η` construction gives a concrete test for step 3: an unlabelled sphere is too symmetrical for this alternating signed relation; a physically individuated relational orientation could support it. Step 4 is where geometry and actual feeling must be shown to be one rather than merely associated. **The present note does not derive that identity or claim that zero has already determined the actual world.** It also does not conclude that the user's no-residue demand is unsatisfiable.

## Verification

`python -m unittest verification.zero_sphere_intrinsic_orientation_test -v` checks the cross-ratio and sign under projective transformations, all 24 role permutations, projective scaling and the point at infinity, orientation reversal, an explicit `η=1/7` example, the analytic bound and alternative signed/weighted assignments. The triple-transitivity and involution arguments are mathematical proofs described above; the tests check finite instances. No test establishes actual physical subjects, valence or self-subsistence.
