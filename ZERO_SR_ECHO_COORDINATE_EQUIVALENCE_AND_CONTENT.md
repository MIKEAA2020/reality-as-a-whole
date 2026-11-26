# Coordinate equivalence and experiential content in the SR-inspired echo

## Result and correction

In the [previous candidate](ZERO_SR_ECHO_SPECIFIC_CONSTITUTION_AND_CALIBRATION.md), the same echo signs supported a family of proposed quality coordinates

```text
Qκ = G(S, κT).
```

The free coefficient κ was shown not to be selected by the stipulated active symmetries. **That does not, by itself, establish a family of physically or phenomenally different constitutions.** For any nonzero κ, `Qκ` is an invertible rescaling of `Q₁`. When the metric, reference orientation, report rule and outcome labels are transformed consistently, the complete *specified model description* gives the same distances, physical statistics, candidate owner labels and predictions. A conditional distinction becomes meaningful only when the compared descriptions are tied to a common, independently fixed qualitative scale or another non-transforming reference.

By contrast, `κ=0` is not an invertible rescaling: it collapses the `T=+` and `T=−` content values on the disagreement sector. This is a real **difference in the stated candidate content maps**, though it is not evidence that either map is the actual experience. The underlying physical T record remains present.

This sharpens the previous report. Its numerical κ=1 versus κ=2 comparison is legitimate **only under its explicit shared calibrated-scale and fixed-decoder premises**; the bare difference `3/16` versus `3/8` is not alone a phenomenological difference. Likewise, fixing an ordinary Euclidean metric separately in both coordinate systems is not the same as transporting one metric between them. The previous report's `κ²=1` result is valid under that fixed-matrix premise; it is not a coordinate-invariant selection of κ by the echo itself.

The executable [coordinate-equivalence checks](verification/zero_sr_echo_coordinate_equivalence_test.py) use the same physical echo table and the existing reduced clock. This is a finite structural and operational audit, not proof that any coordinate is felt.

## 1. Exact passive change of coordinates

Recall the commuting sign relations

```text
N=MJ, K=MJR, R=NK,
S=(N+K)/2, T=(N−K)/2,
S²=(I+R)/2, T²=(I−R)/2, S²+T²=I.
```

At the anchor of the selected record table, let `Q₁=G(S,T)`, with G positive. For every real nonzero κ define

```text
Aκ = diag(1,κ),       Qκ=Aκ Q₁,
Aκ⁻¹ = diag(1,1/κ).
```

The transformation is a bijection on the proposed two-dimensional coordinate space and on its supported content values. It is an exact change of description of the stated mathematical candidate **if all its structures are carried along**. It is not a new physical gate and need not represent a physical gauge transformation. Whether real phenomenal organization has exactly this coordinate freedom is a further question.

Two active operations from the echo are the type exchange `D=diag(1,−1)` and the joint-sign counterpart `C=−I`. Both commute with `Aκ`:

```text
AκD=DAκ,      AκC=CAκ.
```

Thus the active symmetry action is represented by the same matrices after this particular passive reparameterization. The facts that an *active* operation changes a model record and a *passive* change relabels the description must not be confused. In particular, this calculation does not identify opposite actual experiences or turn suffering into a gauge artifact.

The aligned and disagreement sectors are retained: nonzero κ maps `(±G,0)` to itself and `(0,±G)` to `(0,±κG)`. Sign orientation can also be reversed by κ<0. Whether that reversal is a harmless change of coordinates or changes a physically/phenomenally anchored orientation depends on what other structure has been fixed.

## 2. The metric must transform too

Let the candidate reference metric in `Q₁` coordinates be `H₁=I`. If this *same* metric is expressed in `Qκ` coordinates, then

```text
Hκ=Aκ⁻ᵀH₁Aκ⁻¹ = diag(1,1/κ²),
||Qκ||²_Hκ = (Qκ)ᵀHκQκ = ||Q₁||²_H₁ = G².
```

For κ=2, `(0,3/16)` is described as `(0,3/8)`, but its norm under `diag(1,1/4)` remains `3/16`. Every pairwise distance among the actual eight modeled events is likewise preserved; the checks cover positive and negative rational gains. Thus the previous `κ²=1` follows only if one insists that **the numerical metric matrix is I in the κ coordinates as well**. That is a legitimate extra physical/phenomenal scale premise, but it changes the comparison unless independently justified.

There is an additional limitation not captured by checking vector lengths alone. For example, at κ=2 each actual Q lies on one of the two axes. Every matrix

```text
H = [[1, b], [b, 1/4]],        |b|<1/2,
```

is positive definite and gives all these actual vectors squared norm `G²`; the cross-term is invisible in individual norms because `S·T=0` on the joint spectrum. Yet it changes the distance between an aligned-sector point and a disagreement-sector point. If the active type swap `D` is independently required to be a **metric isometry**, `DᵀHD=H` forces `b=0`. This is another conditional way to constrain the geometry, not a reason to assume subjective quality has that metric or that swap is phenomenally isometric.

More generally, a metric need not be Euclidean or even applicable to all qualitative aspects. Neither an algebraic isomorphism nor choice of coordinates establishes a phenomenal geometry. Conversely, no external causal mechanism is needed if a justified metric and experience really are intrinsic aspects of the same constitution.

## 3. One report, consistently transported

For an illustrative scalar readout of the reference second axis, define `Y=Q₁,₂+η`, where η denotes a specified noise variable. In κ coordinates, **the same readout** is

```text
Y=(1/κ)Qκ,₂+η.
```

On the selected event with `G=3/16,T=+1`, both descriptions give the same signal `3/16`; the test checks both noise signs and several positive and negative κ. With identical noise law, they give exactly the same modeled report distribution. This is not an experimentally validated report from an experiencer: it shows only how a specified readout changes coordinates.

If one instead stipulates the *same numerical decoder* `Y=Qκ,₂+η` for κ=1 and κ=2 **on a common independently anchored scale**, the two predictions are `3/16` and `3/8`. Then, with the earlier independently justified matched calibration `|E Y−Qκ,₂|≤ε`, the intervals are disjoint for `ε<3/32`. This comparison is conditional on an anchored decoder, not an automatic consequence of a free coordinate re-description. It compares distinct combined commitments about quality and reporting; a measured report, with proper uncertainty and independent phenomenal reference, could in principle challenge one or both.

The active matter is not whether a bridge causes experience, but whether a particular intrinsic scale, qualitative orientation and subject/report relation are warranted. Transforming just the quality coordinates while freezing the metric and decoder can create a spurious apparent difference; transforming everything does not remove a genuinely anchored difference.

## 4. Zero gain is a genuine loss of the stated content distinction

`Q₀=G(S,0)` cannot be obtained from `Q₁` by an invertible coordinate change. On `R=−`, the original `T=+1` and `T=−1` values both become `(0,0)`. The actual eight-event table has these distributions over the *candidate content labels*:

| Content description | Distinct values | Physical event weights by value | Best event guess from these labels |
|---|---:|---|---:|
| `Qκ`, κ≠0 | 6 | four at `1/8`, two at `1/4` | `3/4` |
| `Q₀` | 5 | four at `1/8`, one at `1/2` | `5/8` |

The classical entropies of these specific label distributions are respectively `5/2` and `2` bits. They are information about a **uniform physical event label under the stated preparation**, not amounts of consciousness or subject counts. The distinction is that `Q₀` collapses two content classes that `Qκ` with nonzero κ distinguishes.

Nor does `Q₀=(0,0)` mean there is no experience: even under a theory taking Q₀ to be a signed or partial content, there could be other qualities, and the physical record still contains T. To conclude that T changes the experience, the constitution must independently identify T-sensitive structure with a phenomenal distinction. This model does not do that. Nor does an eight-event table establish eight subjects.

## 5. Physical effects and coherent disturbance

As an **instrument choice**, not as an automatic consequence of subjective content, compare an ideal fine measurement of `(S,T)` with an ideal coarse measurement of S, which discards the T distinction. In the four-state joint-sign representation, nonzero rescaling of T merely relabels the same fine projectors. Setting κ=0 groups both disagreement projectors into one coarse outcome.

For the specified coherent disagreement-sector state

```text
|ψ⟩=(|N=+,K=−⟩+|N=−,K=+⟩)/√2,
```

an ideal Lüders measurement of S leaves the state unchanged when its result is discarded; a fine T measurement followed by discarding the result dephases its two branches and has fidelity `1/2` with `|ψ⟩`. The earlier [actual-echo coherence controls](ZERO_ECHO_CONSTITUTIVE_MODES_AND_COHERENCE.md) connect this abstract two-branch representation to selected complex echo branches. A recorded coarse outcome could also come from a fine measurement whose result was hidden, so outcome labels alone do not determine disturbance. Neither instrument is thereby a subjective access mechanism.

## 6. Clock, owner and incidence

The [reduced clock construction](ZERO_ECHO_MODE_INSTRUMENTS_CLOCK_TRANSPORT.md) transports a fixed anchor effect through the `T–Q–T` gates. For all reduced record basis states and four checkpoints, the new checks show that applying `Aκ` before or after this anchor transport gives the same transformed mode value. The established clock-twirled fine projectors commute with the reduced shift W; their physical effects are unchanged when their outcomes are bijectively relabeled by nonzero κ.

For the prior **stipulated** ledger-owner rule and uniform checkpoint sampling, the joint table of `(quality label, ledger, checkpoint)` is likewise carried bijectively to the κ representation, with the same weights. This does not establish the owner rule or turn the checkpoint-selection probability into an actual incidence law. Coherent superpositions, full apparatus, local access and whether any subject experiences the anchor rather than an instantaneous quantity remain open.

## 7. What this contributes to the SR analogy

The lesson is closer to the user's relativity point than a comparison of raw coordinate values. In SR, one compares descriptions of one geometrical situation by transforming the whole relevant structure; one does not introduce an external compression force to make those descriptions agree. Here, the candidate's nonzero coordinate rescalings similarly preserve its stipulated structure only when metric and readout are transformed with them. This is an analogy of **method**, not an assertion that a physical reference frame is a subject or that the echo coordinates are Lorentz transformations.

What follows internally is precise: nonzero rescalings preserve the defined quality partition and, under a transported metric, all its pair distances; zero gain loses a distinction. What remains to establish is whether the two-mode structure is experiential, which physical distinctions belong to one subject's quality, what metric or qualitative relations are intrinsically meaningful, and how actual occurrence and incidence follow. A deeper constitution might settle these without an outside coercer, but this calculation does not yet derive it.

The [next pass](ZERO_SR_ECHO_INTRINSIC_DISTINGUISHABILITY_AND_ACCESS.md) derives a basis-independent operational distance on the selected coherent echo and constructs a clock-invariant unsharp pointer. It separates the resulting physical geometry and access tradeoff from a still-unestablished phenomenal geometry or subject.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_sr_echo_coordinate_equivalence_test \
 verification.zero_sr_echo_constitution_test \
 verification.zero_echo_mode_clock_transport_test -v
```

The tests cover the specified mathematical reparameterizations, physical-table partitions, toy Lüders instruments and reduced clock. They are not phenomenal observations or a proof of a complete physical–experiential identity.
