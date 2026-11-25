# Independent sphere rotations dressed by real quantum records

## The advance

The [previous spherical pass](ZERO_SYMMETRY_POINT_SPHERE_QUANTUM_PLENITUDE.md) obtained a no-preference result for the **directional marginal**, but explicitly did not establish invariance of the correlated quantum state. Here we construct an independent-rotation action on that actual state, not just on its probability distribution. A rotation changing the relative angle is accompanied by a unitary transformation of the existing echo records. The records remain real and distinguishable; in particular, an `R+`, `B+` record is carried to an `R−`, `B−` record when the angle crosses the relevant boundary.

This realizes a stronger, conditional unity between internal sphere and differentiated quantum record: the same symmetry relates whole configurations, not an isolated geometrical label. It also gives a sharper no-preference selection **within a specified family**. The construction is adapted to the model's record history, however; it does not yet derive that action, its carrier or a physical–experiential identity from zero. The [implementation](verification/zero_dressed_sphere_rotations.py) and [nine tests](verification/zero_dressed_sphere_rotations_test.py) make the dependencies and controls reproducible.

## 1. What must be transported

Use the original coherent echo and its 16 source-history labels. On the spherical lift, write `u=m·n` for two unit internal directions. Suppressing endpoints and band boundaries, the actual uniform-amplitude state has three old-record sectors:

| sector | relative angle | actual record |
|---|---|---|
| 0 | `0<u<1` | `R+` |
| 1 | `−1<u<−1/2` | `R−`, `J+` |
| 2 | `−1/2<u<0` | `R−`, `J−` |

The N=4 step basis has two positive bins, one in each negative band. After the spherical isometry's `√N` factor, the vector-valued wavefunction is constant within each of these three regions. Its old-system record changes with the region, so bare independent rotations do **not** preserve it. Simultaneous rotations preserve u and do preserve it.

Fix the positive sign pointer first. At each of the 16 source labels, normalize the actual record vector in each sector. Their three 16-by-16 Gram matrices agree numerically to better than `10⁻¹²`. Each has rank seven and nonzero eigenvalues

```text
1/4, 1/4, 7/6, 7/6, 37/12, 37/12, 7.
```

Thus the entire family of records—not merely one selected tick—has the same inner-product structure in all three sectors. If `C_a` is the matrix of its 16 normalized vectors in sector a and `G=C_a†C_a`, diagonalize the common positive part of G and set `E_a=C_a Q Λ^(−1/2)`. The seven columns of `E_a` are orthonormal and have the same expansion coefficients for each source in each sector. The eigendecomposition is a numerical construction; degeneracies permit different frame bases but the matched partial isometries are unchanged by a common basis change. Tests check equality, rank and transport numerically, not as an independent symbolic proof of exact rational entries.

Sector 0 lives in the R+ carrier and 1 and 2 in orthogonal J sectors of R−. Their seven-dimensional spans are consequently mutually orthogonal in the full old-record-plus-R space. Define `V_0=I`; let `V_1` and `V_2` swap the corresponding frames with `E_0` and act as identity on their orthogonal complement. Each `V_a` is unitary and self-adjoint. It carries each normalized actual source in sector 0 to the corresponding source in sector a, preserving arbitrary coherent superpositions across the source labels. This is a family-adapted construction, not a claim that all conceivable record states have such a relation.

A naive single map for both sign pointers does not work: their pooled Gram structures differ between bands. Instead use the original physical sign counterpart S. For negative pointer define `V_a^−=S V_a^+ S`; S is a genuine transformation of the old carrier, not identification of opposite signs. The tests check all 16 labels for both signs and verify compatibility of the two maps. They also check that the frames, including their S images, lie in the original gauge and valid subspaces. As each swap acts as identity on the orthogonal complement, it preserves those subspaces. The earlier separately added angular opposite pair is not acted on in this new verifier; its constrained extension needs its own transported operator before claiming this full new action for that enlarged carrier.

## 2. The actual dressed group action

Let `X=S²×S²` with normalized product-area measure and let `H_R` be the old-record-plus-echo carrier. Include the sign pointer as a separate orthogonal control and set `V(x)=Σ_s |s⟩⟨s|⊗V^s_sector(m·n)`. The definition on the few boundary sets is arbitrary; those sets and their rotated preimages have measure zero.

For `g=(A,B)∈SO(3)×SO(3)`, define on `L²(X,H_R)` (including the sign control)

```text
(U_g ψ)(x) = V(x) V(g⁻¹x)† ψ(g⁻¹x),
             g⁻¹(m,n)=(A⁻¹m,B⁻¹n).
```

Let D be multiplication by V(x), and let P_g be the ordinary pullback. Then `U_g=D P_g D†`. Since D is a measurable pointwise unitary and rotations preserve product area, U is unitary. In particular,

```text
U_g U_h = U_(gh),             U_g† = U_(g⁻¹).
```

The group law is a consequence of the formula, not an inference from finitely many samples. Strong continuity follows by unitary conjugation from the standard strongly continuous rotation representation, despite the stepwise V. At the level of pointwise representatives, only almost-everywhere statements are needed.

For a common rotation `(A,A)`, u is unchanged, so the record dressing is `V(x)V(g⁻¹x)†=I` almost everywhere. For independent rotations it need not be identity. Because the two sign-controlled dressings are S-conjugates, the pointer-exchanging S operation intertwines them. The earlier full-clock counterpart includes a separate clock-dependent phase; the dressing is independent of clock label, so it commutes with that phase and is compatible with that previously derived dressed counterpart on the supported history. This does not assert that bare S alone fixes that coherent clock history.

The explicit frame transport sends every one of the actual 16 sector-0 source vectors to its corresponding vector in either other sector. Therefore the **continuous, uniform-amplitude spherical lift of their coherent history**, with its existing record and sign correlations, is fixed by every `U_g` at the post-echo checkpoint, for any coherent superposition of the 16 source labels. The 16 labels are not the 20 clock ticks. The action on all other echo checkpoints and on the B-dependent purified reservoir is not established; the latter may require its own dressing. The tests verify the group composition on a nonconstant complex test wave, common rotations, counterpart covariance, and the actual post-echo records for both signs, in addition to frame-unitarity and cocycle checks. They sample group elements and points; the conjugation argument establishes the general group identity conditional on the stated construction.

## 3. What no-preference now selects

For a fixed nonzero reference record vector `r`, consider the scalar family

```text
ψ_f(x)=f(x)V(x)r.
```

Its invariance under all dressed independent rotations is equivalent to invariance of f under the ordinary product-rotation pullback. Since `SO(3)×SO(3)` acts transitively, an invariant square-integrable scalar is constant almost everywhere. Normalization fixes the magnitude (but not an overall phase). For the angular-only family `f=f(u)`, this selects the uniform `du/2` distribution. The earlier strictly positive cosine reweighting is not invariant: unequal values of f at two relative angles give different transported amplitudes even though its old marginal constraints and weaker symmetries remain intact.

This is stronger than selecting a directional marginal: the **correlated actual record** is included in the stipulated action. It remains conditional on this family and on this particular record dressing. The entire invariant subspace is `D` applied to the constant `H_R`-valued functions; choosing a different reference vector generally gives a different invariant state. Invariance does not uniquely select the quantum history, relative phases in arbitrary other families, the representation, or a complete ontology. In particular, every normalized positive angular density can be made invariant under a differently constructed action or measure; one cannot infer the selected dressing merely by demanding invariance of a state. Necessity and genuine-possibility conditions remain substantive questions, not labels with which to dismiss formal alternatives.

The continuous comparison uses the actual function `sqrt(1+ε cos(2πu))`. The finite-bin counterexample in the previous pass uses its **midpoint values** and produces a stepwise density; those are different constructions, not an exact identification. Both demonstrate failure of this fixed stronger invariance when their weights vary across a rotation orbit.

## 4. Relation to the larger zero and experience programme

The model makes a unified, testable claim about its own structures: internally differentiated configurations with real polarity and distinct records can transform as a coherent whole, while common rotations leave their relative record relations untouched. It does not require an external preparer as a cosmological cause; nevertheless the model's state, angle space, area measure, gate history and chosen representation remain specified inputs. Treating an active record-changing transformation as **gauge equivalence** would require further physical argument, particularly because the records are distinguishable observables. Nor does a mathematical unitary demonstrate a locally accessible physical operation.

The model charge and earlier exact opposite-pair cancellation are not automatically global physical energy or a signed felt quantity. Opposite sign is not absence of experience, and no calculation here makes pleasure erase suffering. Nothing establishes that the sign, record or clock labels are subjects, that Born weights are actual incidences, or that experience is identical to the intrinsic aspect of this carrier. The model also does not recover spacetime, locality, relativity or the necessity of all genuine possibilities. It is a constructive bridge towards those tasks, not a completed no-residue physical–experiential whole. The actual external foundation F0–F5 artifacts remain unavailable; prior PSR-5 results are restricted-formal, not an independent full replay.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_dressed_sphere_rotations_test -v
```

The numerical frame construction is built from the repository's original coherent histories. Boundary values are omitted intentionally; no finite sample alone proves the analytic group law or the ontology.
