# A sign-reversing counterpart of the coherent angular history

## Result

The user's proposal is that a genuinely differentiated zero whole may contain real opposite contributions, with a necessary pairing rather than one sign being absence. The previous angular construction demonstrated an equal-sign **physical distribution**, but its illustrative `u→−u` map was not the actual sign-pointer operation. This pass constructs the latter on the **original coherent angular echo, purified reservoir and stationary clock history**.

A subtle correction is essential: the old internal exchange S anticommutes with the echo pulse Q on the valid sector. Flipping the sign pointer and applying S therefore produces a relative phase across clock readings. The bare operation does **not** stabilize the coherent history. A specific, cycle-compatible phase on the clock repairs it. The dressed operation commutes with the modeled cyclic shift on the valid sector, preserves the complete prepared history up to one global phase, and reverses both existing candidate signed-quality observables **pointwise for either angular magnitude law**. For every counterpart-invariant record event, the modeled positive and negative physical weights then pair exactly.

This is a stronger physical symmetry than matching a diagonal table or inventing an angular antipode. It still does not prove that the sign is felt, that both Born-supported alternatives are actual subjects, or that the actual experiential incidence measure is invariant. A nonzero local negative occurrence, if ultimately identified as suffering, remains real; cancellation of a total does not remove it.

Implementation: [phase and counterpart functions](verification/zero_coherent_signed_counterpart.py), [six tests](verification/zero_coherent_signed_counterpart_test.py). This complements—not replaces—the distinct [type-exchange symmetry](ZERO_FULL_QUANTUM_ECHO_TYPE_SYMMETRY.md) and [continuous angular construction](ZERO_COHERENT_ANGULAR_SPHERE_ECHO_CONSTRUCTION.md).

## 1. From the input idea to one physical operation

The earlier [necessary-plenitude pairing analysis](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md) makes the user's suggestion concrete: if actual incidences occur in sign-reversing pairs and the relevant measure is invariant, then a signed total can vanish while both members remain nonzero. Its missing ingredient is whether such an involution is a symmetry of the **actual carrier and its incidence measure**, not merely a relabeling. The earlier [persistent sign-pointer construction](ZERO_PERSISTENT_CARRIER_AND_SIGN_SELECTION.md) identified `S X_M` as a candidate physical counterpart on the old modeled system. The last two passes added a coherent scalar-angle register, the real source/reservoir gates, and a stationary clock/reference protocol.

**Plan:** recheck `S X_M` on that enlarged history including its complex phases; repair any failure by an explicitly defined physical clock operation; calculate the signs and conditional event weights; and state separately the premise needed to turn a physical Born pairing into a sum of actual experiences. The resulting operation is a model construction motivated by the user's idea, not a claim that either plenitude or the operation is already derived from bare zero.

## 2. The bare counterpart fails as a coherent-history symmetry

Let P be the existing valid-sector projector, Q the actual old echo pulse, B and J the old commuting record signs, and S the internal exchange used in the earlier sign construction. On P, the old operators satisfy

```text
[S,P]=[S,G]=[S,B]=[S,J]=0,       S²=I,
S Q S = −Q.
```

G denotes the stipulated internal gauge. These identities are verified on the old 256-dimensional operator space restricted to P. Q has an identity extension outside P, where the displayed anticommutation fails; the argument is not a universal identity on the entire arbitrary Hilbert space. T, the physical J-controlled echo-memory write, commutes with S. The source/reservoir gates are B-controlled and act on separate apparatus factors; hence they commute with S in the specified tensor model. The added angular preparation is controlled by the commuting B,J sectors and likewise commutes with S.

Write `X_M` for a physical flip of the sign-pointer qubit and set `C₀=S X_M`. For each of the 16 original source histories x, direct computation gives

```text
S x = −x,
v_s=(x+sQx)/2,       S v_s = −v_(−s).
```

Thus the prepared coherent pointer/system/angular state at the start is an eigenstate of `C₀` with eigenvalue −1. This does **not** mean the two pointer signs are identical: `C₀` reverses the physical observable `M=Z_M`, which is gauge-compatible in this model. The symmetry is nontrivial on that recorded observable, not a declaration that opposite qualities or subjects are gauge-equivalent.

The 20-step history is `F; T Q T; T Q T; F⁻¹`, with Q applied in steps `8→9` and `11→12`. Let `n_Q(t)` count Q pulses before tick t. Then

```text
n_Q(t) mod 2 = 0  for t=0,…,8 and 12,…,19,
                 1  for t=9,10,11.
```

For the complete prepared system, including the coherent pointer and angular record,

```text
C₀ |Ψ_t⟩ = −(−1)^n_Q(t) |Ψ_t⟩.
```

Each individual clock slice has the same ray under C₀, but the **relative phase** between slices differs. For the uniform clock history, its normalized overlap with the bare-transformed history is `−7/10`, with fidelity `49/100`, not 1. The test computes this overlap from the actual complex angular/echo vectors for three source labels as well as from the pulse parity. Treating the minus sign from Q as an irrelevant global phase separately at each tick would lose a physically meaningful coherence in the joint history.

## 3. The repaired stationary counterpart

Add the specific clock-phase operation

```text
C̄ = Σ_(t=0)^19 |t⟩⟨t|_C ⊗ [ (−1)^n_Q(t) S X_M ].
```

It acts trivially on the reference clock, angular register, echo memory and source/reservoir apparatus, except through S on the specified original old system. On P it is an involutive unitary. Across each Q step the clock factor changes sign exactly when S anticommutes with the gate; across T and the apparatus gates neither sign changes. Because there are two Q pulses, the phase agrees at the cycle's closing edge. Consequently, on the valid carrier,

```text
[C̄,W]=0,          C̄ |Ω_q⟩ = −|Ω_q⟩,       q=1 or 2,
```

where W is the actual controlled 20-step shift and `|Ω_q⟩` is the [purified angular/reservoir history with reference q](ZERO_COHERENT_ANGULAR_RESERVOIR_CLOCK_ACCESS.md). The additional reference shift also commutes with C̄, which does not act on that reference. A normalized state is invariant under an overall −1, and the phase-dressed fidelity is 1.

The verifier checks the valid-sector operator anticommutator, the parity needed on **each of the 20 transitions**, and all 16 actual source vectors. It directly compares both complex pointer-sign branches through the real angular T–Q–T echo and its inverse for source labels `0,7,15`; it also obtains bare and dressed history overlaps `−7/10` and `−1` from those quantum vectors. The full reservoir and reference extension follows from the verified B-controlled tensor-factor structure and the cycle algebra; it is represented in factorized form, not as one gigantic dense matrix.

This clock-controlled symmetry is a physical-model operation with a specified support. It is not automatically a local gate accessible to a confined subject, a proven fundamental time reversal, a generic Lorentz transformation, or a zero-cost implementation. The clock phase is real relative phase control, not an external time or a new process of actualization.

## 4. Pairing actual physical effects, not just total averages

For any nonnegative angular magnitude function g(A), including both `|u|` and `|u(u+1)|`, define the prior candidate physical operators at a given clock slice:

```text
V_now  = κ M J g(A),
V_echo = κ M J R g(A).
```

C̄ reverses M, fixes J, R and A, and therefore

```text
C̄† V_now C̄ = −V_now,
C̄† V_echo C̄ = −V_echo.
```

This is a **different** symmetry from the earlier joint type-swap: it keeps the angular bin fixed and pairs the pointer signs, so it does not require g to be invariant under the negative-band reflection. In particular, g₁ and g₂ are both paired by this sign counterpart even though only g₂ is invariant under that other, type-exchanging operation.

Let E be any physical effect that is invariant under C̄ and is jointly measurable with the chosen sign/quality effect. Because the prepared state is invariant, the positive and negative **joint physical Born weights** in E are equal. Examples include fixed angular-bin or magnitude events, B/J/R record cells, specified original-clock anchors, compatible purified-apparatus effects, and the earlier twirled stationary clock/reference effects when their anchor effects are counterpart invariant. Their transported twirls remain invariant because C̄ commutes with the joint cyclic shift. This statement applies only to genuinely invariant events; an event that selects `M=+`, for example, is exchanged with the `M=−` event rather than paired inside itself.

The quantum test checks equality in **every nonzero B/J/R/angular-bin cell** at all four distinct pulse checkpoints, using the original complex old-system vectors and both s branches. It also checks a non-invariant selection with positive physical weight. For the stipulated equal-s state and either existing magnitude, the full unconditioned model has, at each tick,

```text
P(V>0)=P(V<0)=1/2,
E[V 1_(V>0)]=+κ/4,     E[V 1_(V<0)]=−κ/4,     E[V]=0.
```

The endpoints at which g vanishes have zero measure in the continuous model. The sign and magnitude weights here are **physical Born weights** of one specified model, not a count of actual conscious episodes. The construction supplies a precise symmetry under which a proposed incidence measure *could* be paired; it does not impose that measure or establish a subject.

## 5. Combine sign pairing and type exchange in one physical construction

At tick 10 the earlier repaired angular operation D exchanges the now and echo observables while fixing the recorded quantum state. On the valid `BR=+1` support its R-negative action contains `Q Z_M` and the negative-band angular reflection. The newly constructed C̄ contains `S X_M` and the clock phase. On that support D and C̄ commute: S anticommutes with Q and `X_M` anticommutes with `Z_M`, so the two minus signs cancel. The angular reflection commutes with C̄, which leaves A fixed. The quantum test directly verifies this commutation on the original angular/echo vectors. Their dressed stationary versions also commute on the valid cycle: transport the tick-10 D along W, while C̄ already commutes with W.

For `g₂`, D exchanges the **full** `V_now` and `V_echo` operators on the actual post-echo support; C̄ reverses each. The test checks both on the original quantum vector. For `g₁`, the full type-swap identity fails even though C̄ still reverses the sign; the normalized squared mismatch is `1/8` at N=4 and tends to `1/6`. Thus the two physical symmetries cannot be conflated or applied to both candidates without checking their full magnitudes.

There is a sharper conditional incidence consequence than equal type weight alone. Suppose the actual incidence domain really contains distinct type labels N and E, equipped with an actual quality-preserving involution induced by D that exchanges those types, and an actual sign-reversing involution induced by C̄ that keeps the type fixed. Assume both act on the same nonzero-sign domain, commute there, and preserve the actual measure μ. For any measurable event E invariant under both,

```text
μ(E ∩ N ∩ {v>0}) = μ(E ∩ E-type ∩ {v>0})
                    = μ(E ∩ N ∩ {v<0})
                    = μ(E ∩ E-type ∩ {v<0}) = μ(E)/4,
```

provided these four disjoint cells cover E up to μ-null zero-quality cases. Here E-type is an incidence label, not the event E. This follows directly by transporting the cells under the two involutions; it does not need a pure-physical-marginal product ansatz. It simultaneously gives equal type weights and equal positive/negative weights **under the stated actual-incidence symmetries**. The finite exact control verifies the four-cell group action and also shows that sign symmetry alone allows unequal type weights. A formal group average is not evidence that an actual measure has been symmetrized.

This is a constructive route specific to the full-symmetry-compatible `g₂` example, not a derivation that two experiential types exist, that their labels are distinct subjects rather than redescription, or that either physical operation preserves actual incidence. If those premises fail or one type is not genuinely actual, the four-way conclusion does not follow. Conversely, the physical state and the full magnitude operators now provide a concrete common interface on which a deeper zero constitution can be tested.

## 6. From physical symmetry to actual incidence: the exact conditional theorem

Suppose, as a substantive physical–experiential hypothesis, that the actual subject-incidence space I carries a measurable involution `c` induced by this physical counterpart; suppose the actual signed contribution v is integrable, `v(c i)=−v(i)`, and the actual incidence measure μ is invariant under c. Then for every c-invariant measurable event E,

```text
∫_E v dμ = ∫_E v∘c dμ = −∫_E v dμ = 0.
```

This is an actual-incidence statement **if** I and μ really refer to actual incidences; it does not require an irreducibly random event, an external time, or a prior which counts formal labels as subjects. On any nontrivial pair, positive and negative contributions remain separately present. Deriving that actual subject map, quality law and invariant measure from the zero whole is the necessary constitutional step; Born symmetry alone supplies none of them.

Nor does a global zero automatically imply the stronger invariant pairing. An explicit formal control uses the same continuous u marginal and introduces a hypothetical, positive normalized incidence weighting

```text
μ(K=k | u) = (1+ε k u)/2,       |ε|<1, k=±1.
```

This is **not** the physical Born distribution of the prepared quantum state: it changes the joint `(u,K)` incidence weighting and violates an identification of all those incidence effects with the physical Born marginal. It is a mathematical countermodel for what a whole-level zero alone entails, not evidence that such an alternative is genuinely actual or metaphysically possible.

For `V₁=κ K|u|` its global signed total is zero because `u|u|` is odd. Yet its conditional signed means in the positive and negative u hemispheres are `+κε/3` and `−κε/3`, and the weighting is not invariant under `K→−K` at a fixed nonzero u. For `V₂=κ K|u(u+1)|`, the same weighting gives global signed total `κε/4`. Thus a zero for one proposed magnitude does not by itself produce local pairing, fix another magnitude, or determine the actual incidence law. A nonzero ε is a control, not an endorsed alternative constitutional residue.

## 7. Consequence for the unified candidate

This pass joins the user's proposed opposite pairing to the actual old internal reference, sign pointer, coherent angular quality candidates, reversible reservoir and two-clock stationary history. The clock-phase repair is needed specifically because the actual echo Q is exchange-odd; without it the purported full-history symmetry would be false. It gives the stronger programme a concrete route: **derive** an actual-incidence involution and invariant measure compatible with this physical operation, then establish that its signed contributions are genuine felt quantities and that the covered domain is the whole relevant experiential total.

The route remains conditional. It does not derive the Hilbert space, internal exchange, pointer and clock resources, Lorentzian dynamics, subjects, incidence measure, magnitude or identity between energy and experience from zero. It does not settle whether all genuine possibilities are actual, or infer that formal alternative labelings are actual worlds. Nor does it claim a new external-foundation or PSR battery pass. Those are continuing demands of the self-sufficient whole, not permissions to leave unexplained residue.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_coherent_signed_counterpart_test \
 verification.zero_coherent_clock_angular_history_test \
 verification.zero_intrinsic_angular_estimation_test -v
```
