# Toward a localized identity candidate in constrained gravity

## Result

The previous [two-scalar model](ZERO_EXPERIENCE_INTRINSIC_IDENTITY_RELATIONAL_GRAVITY.md) put zero constraint, relational time and physical distinctions in one model, but it was homogeneous and had no local apparatus. This pass takes a concrete step beyond that: it uses the repository's **already specified generally covariant gravity–clock–rod–signal–detector action** to derive a spatially localized, clock-relative response to two physically distinct preparations. The signal, detector, clock, rods and geometry all enter the same coupled constraints; the detector is not a free-standing abstract bit attached afterward.

With opposite signal preparations and the **same nonzero detector preparation**, the full initial Hamiltonian and momentum constraints have the same exact small-amplitude solutions. The global canonical Hamiltonian constraint vanishes on each solution. Yet at a selected relational event, the detector's initial clock-relative acceleration differs between the two preparations. The difference is a property of the interaction and is invariant under spacetime redescription where the clock–rod chart is valid.

This is a **localized physical distinction**, not yet an enduring record, an actual subject, a feeling, or proof of the actual universe's total energy. The field-theory construction exists only in a stipulated effective model and in a short-time patch; the signal is not itself spatially compact, although its interaction with the detector can be localized. We do not equate the compact-universe constraint with energy merely because it is zero. Exact algebraic checks are [here](verification/zero_local_relational_identity_detector_test.py).

## 1. The user's task, kept intact

The working aim is the self-sufficient, fully intelligible whole, with experience as an **intrinsic identity in the appropriate organization**. A subject's lived occurrence and its physical occurrence would not be two things connected by a causal bridge. Its structural organization could be described and tested from within the world; its lived character could be directly acquainted with, without being exhausted by a verbal or mathematical description. These are complementary access to one reality, not ingredients needing an external joiner.

The present calculation does not pretend that direct experience is a detector output or that an unanchored number means unpleasantness. It supplies a more realistic **physical side on which a specific identity could eventually be assessed**: a localized response involving physically embodied references, gravity and a detector. Brute fact and unresolved regress are not being reopened as research alternatives; the whole's nature and all the model's choices remain affirmative derivation targets.

## 2. A single coupled physical construction

Use the action of [the relational detector construction](RELATIONAL_MATTER_DETECTOR_GRAVITY.md), with its conventions `16πG=1`, three-torus spatial topology, and canonical matter fields:

```text
S = ∫ d⁴x √−g [ R
    − 1/2 (∇T)² − f²/2 Σᵢ(∇θⁱ)²
    − 1/2 (∇Φ)² − 1/2 (∇χ)²
    − λ W(T,θ) Φχ − κ₄(Φ²+χ²)² ].
```

`T` is a scalar clock, the three circle-valued `θⁱ` are physical rods, `Φ` is a signal field and `χ` a detector field. `f,κ₄>0`; `λ` and the smooth bounded rod/clock profile W are specified model inputs. The subscript on κ₄ distinguishes the quartic coupling from the gravitational constant in the previous FLRW note. A smooth W can be localized in a finite interval of T and a small rod-coordinate patch. Its profile is a chosen part of the action, not a derived autonomous observer or experimental schedule.

All these fields gravitate. Compact boundaryless slices have the standard canonical Hamiltonian of the form

```text
H[N,Nⁱ] = ∫Σ (N ℋ + Nⁱ ℋᵢ) d³x,
ℋ = 0,       ℋᵢ = 0.
```

Hence this generator vanishes on the constraint surface, with no usual spatial-infinity boundary term. A zero constraint permits nonzero energy in the signal, detector, reference fields and geometry; it is not an operationally established total energy for the actual cosmos. The action, topology, parameters, profile and states are not derived from zero's nature in this calculation.

At ε=0 the explicit background initial data in the earlier construction have `f=1/2`, clock momentum `τ=3/2`, `ψ=1` and `α=1`. The reference fields contribute positive initial matter density `(3f²+τ²)/2=3/2` while the gravitational term in the Hamiltonian constraint is `−3α²/2=−3/2`. The full constraint is zero. The coupled, perturbed data below retain clock, rods, signal and detector contributions: the calculation does not assume that a physical reference is energy-free. The α=1 branch is the one used in the cited initial-data example; no assertion of expanding rather than contracting orientation is needed here.

## 3. Two preparations with the same initial zero constraint

The earlier exact-data existence argument uses

```text
hᵢⱼ=ψ(z)⁴δᵢⱼ,        πⁱʲ=α√h hⁱʲ,
T=0, P_T=τ,          θⁱ=xⁱ mod 2π, P_θⁱ=0,
Φ_s=s ε b cos z,     P_Φ=0,
χ=0,                 P_χ=ε p(1+cos z),
s=+1 or −1.
```

Here ε is sufficiently small, `τ≠0`, and the momentum variables are canonical densities. The detector is in the **same nonzero-momentum preparation** for both signal signs. Although χ initially vanishes, its momentum does not; “ready” would be an additional interpretation, not a consequence of its initial field value.

For either sign, each scalar contribution to the initial momentum constraint `P_A ∂ᵢA` vanishes separately. The exact Hamiltonian constraint in the stated ansatz depends on Φ through its squared gradient and fourth power. Since `χ=0`, the interaction potential `λWΦχ` vanishes on the initial slice. Therefore **the full initial constraint equation is identical for s=+1 and s=−1**, for any fixed ψ and α; by the earlier local implicit-function argument, the same exact small-ε constrained solution `(ψ,α)` works for both signs. The [test](verification/zero_local_relational_identity_detector_test.py) checks this equality directly for rational inputs; the exact existence result is the analytic argument in the earlier note, not something established by sampling.

The two preparations are physically different only with a meaningful sign calibration: their Φ values are opposite while the detector momentum and the reference fields are held fixed. The initial energy terms shown in the constraint are unchanged by the signal sign. That does **not** mean the matter configurations are identical or that all subsequent geometries coincide.

## 4. The same relational event, different local responses

Where the four reference fields define an invertible local chart, set

```text
χ_rel(t,r) = χ(X⁻¹(t,r)),     X=(T,θ¹,θ²,θ³).
```

This is invariant under a spacetime diffeomorphism acting on all the fields: the event moves with its physical reference values. It is a relational field value in the chosen model, not an assertion of a globally valid reference frame. Clocks and rods can fail, intersect, or cease to be invertible.

At the initial relational event `T=0, θ=r`, the initial detector values and first relational derivatives coincide for the two preparations. The interaction-induced part of the second relational-time derivative, at the same initial geometry, is

```text
A_s(r) ≡ [∂²_T χ_rel]_{λ,s} − [∂²_T χ_rel]_{0,s}
       = −s λ ε b W(0,r) cos(r_z) ψ(r_z)¹² / τ².
```

The `λ=0` reference here is a comparison solution, not an additional component outside the physical world. For the sign-reversed preparations at λ=0, the action has a separate `Φ→−Φ` symmetry, so the detector and the reference fields have the same evolution on a common locally unique development. The complete initial relational acceleration difference for the λ theory is thus

```text
[∂²_T χ_rel]_{λ,+} − [∂²_T χ_rel]_{λ,−}
    = −2 λ ε b W(0,r) cos(r_z) ψ(r_z)¹² / τ².
```

This uses the response calculation and exact-data existence scope of [the earlier construction](RELATIONAL_MATTER_DETECTOR_GRAVITY.md), not a newly performed nonlinear evolution. At `r_z=0`, `W(0,r)=1`, `b=2`, `τ=3/2`, the difference becomes

```text
−(16/9) λ ε ψ(0)¹².
```

Since `ψ(0)>0`, it is nonzero when `λε≠0`. For small positive relational time h, equal initial values and first derivatives give

```text
χ_rel,+ (h,r) − χ_rel,− (h,r)
  = −(8/9) λ ε ψ(0)¹² h² + o(h²).
```

Thus the responses are distinct for sufficiently small nonzero h, given the assumed smooth local solutions and nonzero coupling. The calculation supplies **no explicit duration, error bound or noise tolerance**. At zeroth order in ε, `ψ(0)=1`; for `λ=1`, `ε=1/100`, the acceleration difference at that approximation is `−4/225`. That numerical substitution is not an exact solved perturbed metric.

When W vanishes at the event, the displayed **immediate interaction-induced acceleration** vanishes there. That is an initial local control, not a claim that a signal can never propagate there later. W and the clock/rod fields are included in the same action; the profile's localization is in physical reference-field coordinates, not an externally supplied spacetime chart. A choice of patch and its apparatus is nonetheless stipulated, not derived from a subject-boundary law.

## 5. A symmetry and reference control

The action has the simultaneous internal transformation

```text
(Φ,χ,P_Φ,P_χ) → (−Φ,−χ,−P_Φ,−P_χ),
(g,T,θ and their momenta unchanged).
```

But that is **not** the operation used in section 3: flipping only the signal leaves `P_χ` fixed, while the simultaneous transformation reverses its nonzero value. Thus the earlier [geometry-only sign no-go](RELATIONAL_SIGNAL_GEOMETRY_NO_GO.md), which used detector momentum zero and simultaneously sign-related preparations, cannot be applied uncritically to claim identical full geometry for our two detector-prepared solutions. The initial geometries match; their later geometries have not been calculated. Conversely, the present result does not refute the earlier exact no-go, which concerns a different pair of preparations.

A sign is usable only relative to a convention or a physical sign reference. In a schematic calibrated description let an oriented detector contrast be `D`, and reference orientation `r=±1`; then `rD` is unchanged if both D and r are relabelled with opposite signs. Flipping D while holding a physically fixed reference unchanged is a different operation. This is an algebraic consistency condition, **not** a constructed reference apparatus or a declaration that the model's internal sign symmetry is gauge. If it is gauged in a more complete theory, a sign-sensitive observable must be relationally dressed with appropriate physical reference resources. Their stress energy, preparation and coupling remain to be included.

The response comparison requires an actual calibration or a justified common-baseline model before it can be used as a measurement. We have not constructed an operational baseline subtraction, readout, localized memory, error distribution or probabilities.

## 6. Candidate subject and experience: what would be the identity?

Consider a **proposal**, not a conclusion: a localized, suitably integrated physical occurrence `O` involving an interacting signal–detector network within a specified rod patch is part of an actual subject `S`. An internal contrast of that occurrence might be present to S as a specific experience. If such a proposal is correct, the physical occurrence is not causing a second immaterial occurrence; the directly lived aspect and the physically described aspect are one and the same `O`.

The present apparatus is **not shown to be sufficiently organized for S to exist**. In particular:

- A localized interaction or detection response does not supply phenomenal unity, subject boundaries, persistence, memory, self-access or an actual report.
- A prescribed W and a chosen rod patch do not select a subject; a physical boundary and an experiential boundary need not coincide.
- Neither sign of Φ, χ, acceleration, nor any bit is inherently pleasure, pain or neutral. The direct anchor and actual physical correspondence must be established, rather than specified by naming one sign “suffering.”
- The sign-responsive detector is a physical part of the same constrained model, but it is **not yet a retained or trusted record**, and its response to a stimulus is not by itself subjective experience.
- Direct experience need not be expressible completely in language; but the proposal must still identify the right occurrence, structural relations and experiential contrast. First-person evidence is part of reality and need not be an external substance.

A noncausal identity is not undermined merely because we use different vocabularies, just as the SR length relation needs no separate squeezing force. Yet the current model only proves a relational physical response given its action. It does not derive that this response **is** a particular experience or that the action is the self-sufficient ultimate constitution.

## 7. What this advances and what to do next

Compared with the homogeneous scalar threshold, this construction has a **localized interaction, physical reference fields and a genuinely gravitating detector**, all within one set of constraints. It separates a physical signal flip from a passive sign redescription and gives a definite short-time contrast. This meets part of the proposed physical recovery task without making a categorical identification of scalar fields and minds.

The next concrete tasks are to (1) replace the stipulated reference orientation and W with physical preparation and local readout, retaining their gravitational contributions; (2) build a stable finite-time record with controlled errors and show which relational occurrence it records; (3) propose and independently motivate a subject boundary and qualitative identity, then compare actual first-person and physical evidence; and (4) derive the relevant whole-level energy and the action/organization from the self-sufficient nature rather than inferring them from the word zero. Existing [finite-window detector calculations](RELATIONAL_SIGNAL_GEOMETRY_NO_GO.md) offer a separate global-mode perturbative starting point but do not already implement this localized full nonlinear record.

A subsequent [three-dimensional localized finite-window calculation](ZERO_LOCALIZED_FINITE_WINDOW_GRAVITY_RESPONSE.md) evaluates the first-order detector difference on the expanding gravitating reference background after the coupling is switched off. The signal persists at sampled times but is still drifting; it is not a durable record or a full nonlinear evolution.

The report does not require every field or physical subsystem to be a subject, a cosmic observer, an external clock, or a universal experiential sum. Nor does it infer a unique or necessary identity from the existence of a detector. It preserves the user's demand that a completed account leave no independent remainder, while stating exactly which parts of this candidate have and have not been derived.

## Verification

```sh
PYTHONPATH=verification:. python -m unittest \
 verification.zero_local_relational_identity_detector_test \
 verification.zero_intrinsic_identity_relational_gravity_test \
 verification.zero_constraint_reference_recovery_test -v
```

The new six checks verify equality of the displayed exact initial constraint expression under signal sign flip, acceleration algebra and its vanishing controls, equality of initial sign-even matter terms, the distinction from simultaneous field reversal, and covariance of the abstract reference-relative sign. They assume the source model's differential equations and analytical short-time formula; they do not numerically evolve the coupled Einstein system or establish existence of a conscious subject. See [the original GR initial-data report](RELATIONAL_MATTER_DETECTOR_GRAVITY.md) for the second-order verification and the separate implicit-function argument.
