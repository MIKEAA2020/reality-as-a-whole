# Intrinsic quality and the best accessible angular reconstruction

## Result

This pass brings the preserved [Russellian intrinsic-experience conversation](sources/uploads/DeepSeek_Russellian-experience-intrinsic-matter_20261104-2323.txt) and [experience/non-optimality conversation](sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261106-2010.txt) into the same coherent sphere–echo candidate. It does not replace experience with a probability or treat an old physical sign as a feeling. The constructive question is narrower:

> Given the actual original quantum echo with its added angular record, what is the best reconstruction of either proposed signed-magnitude observable using only the old system, echo memory and composed apparatus, **without access to the new angular record**?

For the two already studied magnitude candidates the answer is unique, exact and different. The least mean-square error is **5/96** for `g₁=|u|` and **31/180** for `g₂=|u(u+1)|`, with κ=1 in the continuous model. Both are strictly positive. The best old-carrier reconstruction uses the physical band records and preserves the candidate signs; it cannot recover the within-band magnitudes. The result is checked by applying operators to the **original complex quantum vectors**, not only by a scalar toy table.

This is an operational statement about a specified model and measurement task. It does not prove that a real experience is an observable, that Born weight is subjective incidence, or that the old carrier is a subject. Under the further hypothesis that a subject's magnitude is a single-valued function of precisely that old reduced physical state, the full varying angular magnitude cannot be its intrinsic quality on all the displayed conditional preparations. A different intrinsic relation or larger carrier is not excluded.

Implementation: [exact rational moments](verification/zero_intrinsic_angular_estimation.py) and [three quantum/continuum tests](verification/zero_intrinsic_angular_estimation_test.py).

## 1. Audit, adaptation and the intended identity

The Russellian transcript starts with the user's proposal that experience is the **intrinsic nature of matter**, then explores an experiential whole with emergent space and time. The user's later correction is governing: one reality may be intrinsically experiential while containing genuinely distinct finite subjects; neither a conscious electron nor a universal agent is assumed. The transcript's unsourced `[reference:n]` tokens are not independently verifiable citations. Its distinctions are useful conceptual inputs, not evidence that its particular identity has been derived.

The non-optimality transcript preserves the user's demand for both structural intelligibility without residue and experiential intelligibility through acquaintance. It also stresses a non-best local world and predictive/generative power. Its suggested functional `F(Φ,R)` does **not** follow uniquely from unity and richness, and finitude by itself does not establish harm; see the [two-transcript source audit](TWO_EXPERIENCE_AND_REALITY_TRANSCRIPTS_SYNTHESIS.md). Keep acquaintance and real suffering as data to be respected, but do not use inexpressibility as a waiver of the structural and identity problems. No positive contribution makes a negative felt occurrence unreal.

**Plan:** retain the existing common sign candidate and the two full magnitude candidates; use the actual coherent angular record and original echo, rather than introducing a separate consciousness metric; quantify exactly what a proposed restricted carrier can reconstruct; then distinguish a conditional physical approximation from a physical–experiential identity. This is one integrated model with explicit extra inputs, not a claim that the transcripts themselves supplied these numerical operators.

## 2. The candidate sign and what the old carrier actually sees

At tick 10 the old echo memory has `R=B` on the actual prepared support. Let `J` be the current j sign and `M` the pointer. The earlier conditional quality selection gave the transported sign

```text
K = M J R = s z,
```

if the proposed boundary, ready calibration and composite-echo neutrality are granted. Those are substantive premises; unitarity alone does not make K felt. The two full candidate observables are

```text
V₁ = κ K |u|,                 V₂ = κ K |u(u+1)|,       κ>0.
```

The angular register A and the `du/2` distribution are stipulated additions. At the post-echo reading, the **old quantum system and R** can distinguish three mutually orthogonal band states, with physical Born weights:

| Angular band | Post-echo record | Weight | Mean g₁ | Mean g₂ |
|---|---|---:|---:|---:|
| `−1<u<−1/2` | `R=−, J=+` | 1/4 | 3/4 | 1/6 |
| `−1/2<u<0` | `R=−, J=−` | 1/4 | 1/4 | 1/6 |
| `0<u<1` | `R=+, J=+` on support | 1/2 | 1/2 | 5/6 |

The signs s and z, and hence K, are read from the specified old pointer/record algebra. For each fixed sign and band, the continuum vector-valued wavefunction is **constant in u** in the old-system/R factors. Thus, after a specified angular-bin readout and withholding A, every u within the same band has the same normalized old conditional state. Source/reservoir controls depend on B, not u within that band; composing the explicitly purified apparatus and a fixed clock anchor leaves this indistinguishability intact, as established in the [previous pass](ZERO_COHERENT_ANGULAR_RESERVOIR_CLOCK_ACCESS.md).

This is a statement about the actual prepared model and this conditional-readout experiment. The older carrier may be in a genuinely different state for a different preparation or after a new interaction with A. No j-only or surface-confined inhabitant is automatically granted M, R, the apparatus or any new interaction.

## 3. The uniquely best old-carrier approximation

Grant, for this calculation, access to the entire old system, the echo memory, pointer, purified apparatus and clock anchor—but **not A**. Consider any POVM on those accessible factors, including an arbitrary ancilla prepared independently of the modeled state and an arbitrary classical estimate made from its outcome. The target is the result of the commuting physical angular and signed-quality measurement in the specified joint model, and error is squared numerical error averaged with the prepared physical Born weights. This is not a claim about how experiences are actually counted.

Let H denote the old-readable `(s,band)` record and let Y denote an arbitrary allowed measurement outcome. Within each H sector the old conditional quantum state does not depend on u. Hence, conditional on H, the distribution of Y does not depend on u. For any estimate `a(Y)`, the elementary conditional-variance identity gives

```text
E[(V − a(Y))²]
 = E[ Var(V | H) ] + E[( E[V | H] − a(Y) )²].
```

The first term cannot be reduced by any measurement on the old carrier. Equality is achieved by measuring the three orthogonal bands and K and reporting the conditional mean. Within the tested support the minimizing estimate is unique up to events of zero physical weight:

```text
V̂₁ = κ K × { 3/4, 1/4, 1/2 } in the three bands,
V̂₂ = κ K × { 1/6, 1/6, 5/6 } in the three bands.
```

These are implemented using **old record projectors**, not using u as a secret classical control. For `V̂₂`, the magnitude estimate depends only on R on the actual support; for `V̂₁` the two negative-band J values are also needed. K itself remains the earlier conditional sign rule. The estimates are useful physical approximations, not new assertions that the averages are what anyone feels.

Exact integration with `du/2` gives

```text
min E[(V₁−V̂₁)²] = κ² · 5/96,
min E[(V₂−V̂₂)²] = κ² · 31/180.
```

For `g₁`, the lower and upper negative bands each contribute `1/192` and the positive band contributes `1/24`. For `g₂` they contribute `1/720`, `1/720` and `61/360`. In particular, the larger `g₂` residual comes mostly from the positive band; its exact full-swap invariance does not make the quality magnitude accessible to the old boundary.

The [verifier](verification/zero_intrinsic_angular_estimation_test.py) calculates these rational continuous integrals independently, and applies the actual `MJR g` operator and old-only projector estimator to original old-system/R/A quantum vectors for source labels `0,7,15`, both s signs and N=4,8. It also checks that a constant perturbation of all the predicted magnitudes increases squared error by exactly its square. A separate N=8 test explicitly compares full old quantum columns: equal within each band and orthogonal between bands. The continuous proof follows from the common `L²(du)` wavefunction, not from extrapolating a single finite matrix.

## 4. What the signs and a zero total do—and do not—select

Under the stipulated equal s distribution, K has equal positive and negative physical weight and is independent of u. Both examples have the same overall mean magnitude:

```text
E[g₁] = E[g₂] = 1/2,
E[V_i 1_(K=+)] = +κ/4,
E[V_i 1_(K=−)] = −κ/4,
E[V_i] = 0.
```

Consequently the **same signed physical total and the same two sign-conditioned first moments** are compatible with both magnitude laws. Those equalities do not determine the law or erase local negative contributions. If the negative sign is later justified as suffering, it denotes real suffering in its own incidence; the positive contribution does not undo that lived occurrence.

For comparison, a physical observer supplied only with K, under the equal-s preparation and no other u-correlated side information, has optimal prediction `κ K/2`. Its two mean-square errors are respectively `κ²/12` and `17κ²/60`. Supplying the old band records reduces the errors to `5κ²/96` and `31κ²/180`; supplying the full angular record makes this particular physical reconstruction exact. This is a comparison of **explicitly specified access algebras**, not an inference that a real confined subject can report any of them. Other prepared side information, a different distribution or an intervention coupling A can change the result.

The earlier full physical swap takes the negative half-band into its reflected partner. `g₂` is unchanged pointwise; `g₁` is not. The reconstructed g₂ means agree across those two bands, while the reconstructed g₁ means differ. This provides a compatible old-record approximation for the symmetry-respecting candidate, but neither pointwise symmetry nor its approximation selects g₂ uniquely: many other functions obey the same reflection. An experiential incidence measure must independently be invariant under the relevant full physical–experiential transformation before the earlier equal-type incidence theorem applies.

## 5. Experiential and structural intelligibility remain connected

The useful source distinction is not that structure has failed while experience is dismissed, or that acquaintance eliminates all physical questions. The concrete model now identifies **what the structural description cannot reconstruct at the selected boundary** and what an enlarged carrier supplies. One could consistently investigate at least the following distinct constitutive claims:

1. The relevant intrinsic subject is restricted to the old carrier and its quality is a function of its reduced physical state. Then the varying full `g₁` or `g₂` value fails that candidate sufficiency condition on the displayed bin preparations.
2. The actual subject includes the angular record, or a physically justified relation to it. Then the particular access obstruction is removed, but subject unity, persistence and the identity between the recorded physical observable and actual felt character still need determination.
3. Intrinsic quality is not determined by that instantaneous accessible reduced state. Then the locality principle must be replaced by a justified larger relational/history rule; indistinguishability alone neither refutes nor establishes such a rule.

These are **conditional explanatory architectures**, not a declaration that each is genuinely metaphysically possible or an instruction to select whichever leaves acceptable residue. The user's strongest possibility–actuality proposal requires determining which distinctions are genuinely actual, rather than declaring inconvenient alternatives impossible. A successful zero constitution must jointly determine the physical carrier, actual subject incidences, their qualitative identity, sign and magnitude, and the relevant aggregation—not append independent primitives simply because the model can represent them.

The present computation is an advance toward that demand: it derives the unique optimal old-carrier observable for two concrete candidates and exposes the exact information that the extra angular carrier contributes. It does not derive the physical angular distribution, the physical–experiential identity, empirical consciousness predictions, objective cosmic energy, or the self-sufficiency of zero. Structural estimator error is not a numerical measure of suffering, harm or moral value.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_intrinsic_angular_estimation_test \
 verification.zero_coherent_clock_angular_history_test \
 verification.zero_quantum_angular_echo_test -v
```
